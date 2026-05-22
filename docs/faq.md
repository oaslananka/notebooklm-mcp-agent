# FAQ

## Is this official Google software?

No. It integrates with NotebookLM through `notebooklm-py`, an unofficial library.

## Does stdio require HTTP authentication?

No. stdio inherits the local caller's permissions.

## Can public HTTP run without auth?

No. Public HTTP fails at startup unless `bearer` or `github-oauth` is configured.
