from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class DragonflyToolkitApp(App):
    """A Textual app to interact with Vipyr Dragonfly tooling."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark