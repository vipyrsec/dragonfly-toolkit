"""Commands for interacting with packages."""

from typing import Annotated, Optional

import typer
from requests import Session
from rich import print

from letsbuilda.pypi import PyPIServices

app = typer.Typer()


@app.command()
def metadata(name: str, version: Annotated[Optional[str], typer.Argument()] = None) -> None:
    """Get metadata for a package."""
    http_session = Session()
    client = PyPIServices(http_session)
    print(client.get_package_metadata(name, version))
