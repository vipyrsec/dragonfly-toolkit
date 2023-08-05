"""Testing the CLI."""

from dragonfly_cli.app import app
from typer.testing import CliRunner

runner = CliRunner()


def test_app() -> None:
    """Test that the app can display it's help message."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit" in result.stdout
