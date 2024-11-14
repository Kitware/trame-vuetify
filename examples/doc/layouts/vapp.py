from trame.app import get_server
from trame.ui.vuetify3 import VAppLayout
from trame.widgets import vuetify3 as v3


class App:
    def __init__(self, server=None):
        self.server = get_server(server)
        self._build_ui()

    def _build_ui(self):
        with VAppLayout(self.server, fill_height=True) as self.ui:
            with v3.VContainer(fluid=True, classes="fill-height bg-green-accent-1"):
                v3.VAlert(
                    title="Vuetify - VApp layout",
                    text="Layout example",
                    border="start",
                    border_color="info",
                    closable=True,
                )


def main():
    app = App()
    app.server.start()


if __name__ == "__main__":
    main()
