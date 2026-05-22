"""Runtime settings for the NotebookLM MCP server."""

from __future__ import annotations

from enum import StrEnum
from ipaddress import ip_address
from pathlib import Path
from typing import Any, Self
from urllib.parse import urlparse

from pydantic import Field, SecretStr, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class TransportMode(StrEnum):
    """Supported MCP transport modes."""

    STDIO = "stdio"
    HTTP = "http"


class AuthMode(StrEnum):
    """Supported remote authentication modes."""

    NONE = "none"
    BEARER = "bearer"
    GITHUB_OAUTH = "github-oauth"


class LogFormat(StrEnum):
    """Supported structured logging renderers."""

    JSON = "json"
    CONSOLE = "console"


def _blank_secret(value: SecretStr | None) -> bool:
    return value is None or not value.get_secret_value().strip()


def _is_loopback_host(host: str) -> bool:
    normalized = host.strip().strip("[]").casefold()
    if normalized in {"localhost", "ip6-localhost"}:
        return True
    try:
        return ip_address(normalized).is_loopback
    except ValueError:
        return False


def _is_loopback_url(value: str) -> bool:
    parsed = urlparse(value)
    return bool(parsed.hostname and _is_loopback_host(parsed.hostname))


class Settings(BaseSettings):
    """Validated configuration loaded from CLI overrides, environment, and `.env`."""

    model_config = SettingsConfigDict(
        env_prefix="NOTEBOOKLM_MCP_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        validate_assignment=True,
    )

    transport: TransportMode = TransportMode.STDIO
    http_host: str = "0.0.0.0"  # noqa: S104  # nosec B104
    http_port: int = Field(default=8080, ge=1, le=65535)
    http_path: str = "/mcp"
    base_url: str | None = None
    stateless_http: bool = True

    auth_mode: AuthMode = AuthMode.NONE
    bearer_token: SecretStr | None = None
    github_client_id: str | None = None
    github_client_secret: SecretStr | None = None
    github_redirect_path: str = "/auth/callback"
    oauth_required_scopes: str = "read:user,user:email"
    oauth_allowed_users: str | None = "oaslananka"

    notebooklm_auth_json: SecretStr | None = None
    notebooklm_auth_file: Path = Path("~/.config/notebooklm-agent/notebooklm_auth.json")

    data_dir: Path = Path("~/.local/share/notebooklm-agent")
    session_db: str | None = None

    log_level: str = "INFO"
    log_format: LogFormat = LogFormat.JSON

    destructive_requires_confirm: bool = True
    default_poll_interval_sec: int = Field(default=15, ge=1)
    default_poll_timeout_sec: int = Field(default=600, ge=1)

    @field_validator("notebooklm_auth_file", "data_dir", mode="after")
    @classmethod
    def expand_user_paths(cls, value: Path) -> Path:
        """Normalize user-relative paths from defaults, env, and CLI overrides."""
        return value.expanduser()

    @classmethod
    def from_overrides(cls, **overrides: Any) -> Self:
        """Create settings with CLI override values while still honoring env sources."""
        return cls(**{key: value for key, value in overrides.items() if value is not None})

    @model_validator(mode="after")
    def validate_configuration(self) -> Self:
        """Finalize derived defaults and fail fast on unsafe authentication settings."""
        if self.session_db is None:
            session_db = f"sqlite+aiosqlite:///{(self.data_dir / 'sessions.db').as_posix()}"
            object.__setattr__(self, "session_db", session_db)
        elif "{DATA_DIR}" in self.session_db:
            object.__setattr__(
                self,
                "session_db",
                self.session_db.replace("{DATA_DIR}", self.data_dir.as_posix()),
            )
        if self.transport is TransportMode.HTTP and self.auth_mode is AuthMode.NONE:
            if not _is_loopback_host(self.http_host):
                raise ValueError("auth_mode=none is allowed only for stdio or loopback HTTP")
            if self.base_url and not _is_loopback_url(self.base_url):
                raise ValueError("public base_url requires bearer or github-oauth auth")
        if self.auth_mode is AuthMode.BEARER and _blank_secret(self.bearer_token):
            raise ValueError("bearer_token required when auth_mode=bearer")
        if self.auth_mode is AuthMode.GITHUB_OAUTH:
            missing: list[str] = []
            if not self.github_client_id:
                missing.append("github_client_id")
            if _blank_secret(self.github_client_secret):
                missing.append("github_client_secret")
            if not (self.oauth_allowed_users or "").strip():
                missing.append("oauth_allowed_users")
            if missing:
                joined = ", ".join(missing)
                raise ValueError(f"{joined} required when auth_mode=github-oauth")
        return self
