# require trame-client>=2.15
from trame.app import get_server
from trame.widgets import vuetify3
from trame.ui.vuetify3 import SinglePageLayout

VUETIFY_CONFIG = {
    "theme": {
        "themes": {
            "seb": {
                "dark": True,
                "colors": {
                    "primary": "#faa",
                    "secondary": "#afa",
                },
            }
        }
    }
}


class ThemeExample:
    def __init__(self, server=None, table_size=10):
        self.server = get_server(server, client_type="vue3")
        self.ui = self._build_ui()

    def _build_ui(self):
        with SinglePageLayout(
            self.server, full_height=True, vuetify_config=VUETIFY_CONFIG
        ) as layout:
            layout.root.theme = "seb"
            with layout.toolbar.clear() as toolbar:
                toolbar.density = "compact"
                toolbar.title = "Theme Example"

            with layout.content:
                with vuetify3.VContainer(fluid=True):
                    with vuetify3.VRow():
                        with vuetify3.VCol():
                            vuetify3.VBtn("Hello", color="primary", block=True)
                        with vuetify3.VCol():
                            vuetify3.VBtn("World", color="secondary", block=True)

            return layout


# -----------------------------------------------------------------------------
# Standalone execution
# -----------------------------------------------------------------------------
def main():
    app = ThemeExample()
    app.server.start()


if __name__ == "__main__":
    main()
