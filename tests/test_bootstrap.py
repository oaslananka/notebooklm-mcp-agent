from notebooklm_mcp_agent import __version__


def test_version_is_bootstrap_release() -> None:
    assert __version__ == "1.0.0"
