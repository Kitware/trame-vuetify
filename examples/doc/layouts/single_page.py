from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3 as v3


class App:
    def __init__(self, server=None):
        self.server = get_server(server)
        self._build_ui()

    def _build_ui(self):
        with SinglePageLayout(self.server, fill_height=True) as layout:
            self.ui = layout  # for jupyter

            layout.title.set_text("My App")
            with layout.icon:
                v3.VIcon("mdi-brain")

            with layout.toolbar as tb:
                tb.density = "compact"
                tb.classes = "bg-light-blue-accent-1"
                v3.VSpacer()
                v3.VBtn(icon="mdi-refresh", density="compact")

            with layout.content:
                with v3.VContainer(fluid=True, classes="fill-height bg-green-accent-1"):
                    v3.VAlert(
                        title="Vuetify - Single Page Layout",
                        border="start",
                        border_color="info",
                        closable=True,
                    )

            with layout.footer as footer:
                footer.classes = "bg-amber-lighten-5"


def main():
    app = App()
    app.server.start()


if __name__ == "__main__":
    main()
