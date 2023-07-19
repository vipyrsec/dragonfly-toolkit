from typing import Annotated,Optional

import typer
from requests import Session

from letsbuilda.pypi import PyPIServices

app = typer.Typer()


@app.command()
def interactive():
    from dragonfly_tui.app import DragonflyToolkitApp

    DragonflyToolkitApp().run()


@app.command()
def package_metadata(name: str, version: Annotated[Optional[str] , typer.Argument()] = None):
    http_session = Session()
    client = PyPIServices(http_session)
    print(client.get_package_metadata(name, version))
