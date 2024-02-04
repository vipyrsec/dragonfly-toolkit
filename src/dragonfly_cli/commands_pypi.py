"""Commands for interacting with PyPI."""

from typing import Annotated, Optional

import typer
from httpx import Client
from letsbuilda.pypi import PyPIServices
from rich import print

app = typer.Typer(help="Interact with PyPI")


@app.command()
def package_metadata(
    name: str,
    version: Annotated[Optional[str], typer.Argument()] = None,
) -> None:
    """Get metadata for a package."""
    http_client = Client()
    client = PyPIServices(http_client)
    print(client.get_package_metadata(name, version))


@app.command()
def distribution_contents(
    name: str,
    version: Annotated[Optional[str], typer.Argument()] = None,
) -> None:
    """Get package contents."""
    http_client = Client()
    client = PyPIServices(http_client)
    print(client.get_package_metadata(name, version))
