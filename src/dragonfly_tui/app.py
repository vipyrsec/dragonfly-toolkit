"""App builder."""

from typing import ClassVar, Self

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class DragonflyToolkitApp(App):
    """A Textual app to interact with Vipyr Dragonfly tooling."""

    BINDINGS: ClassVar[list[tuple[str, str, str]]] = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self: Self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self: Self) -> None:
        """An action to toggle dark mode."""  # noqa: D401 - no.
        self.dark = not self.dark


if __name__ == "__main__":
    DragonflyToolkitApp().run()
