"""App builder."""

import typer

from .package_commands import app as packages_app

app = typer.Typer()
app.add_typer(packages_app, name="packages")


@app.command()
def interactive() -> None:
    """Launch the TUI."""
    from dragonfly_tui.app import DragonflyToolkitApp

    DragonflyToolkitApp().run()
