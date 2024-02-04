"""App builder."""

import typer

from .commands_pypi import app as pypi_app

app = typer.Typer()
app.add_typer(pypi_app, name="pypi")


@app.command()
def interactive() -> None:
    """Launch the TUI."""
    from dragonfly_tui.app import DragonflyToolkitApp  # noqa: PLC0415

    DragonflyToolkitApp().run()
