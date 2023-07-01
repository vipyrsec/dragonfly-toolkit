import typer

app = typer.Typer()


@app.command()
def interactive():
    from dragonfly_tui.app import DragonflyToolkitApp
    DragonflyToolkitApp().run()


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")
