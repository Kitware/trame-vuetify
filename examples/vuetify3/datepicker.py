# WIP: not functional yet... Need to register serializer
from trame.app import get_server
from trame.widgets import vuetify3
from trame.ui.vuetify3 import SinglePageLayout
from trame.decorators import TrameApp, change


@TrameApp()
class DatePickerExample:
    def __init__(self, server=None, table_size=10):
        self.server = get_server(server, client_type="vue3")
        self.ui = self._build_ui()

    def today(self):
        self.server.state.selected_date = dict(
            date="2024-01-30",
            format="iso",
            _type="js-date",
        )

    @change("selected_date")
    def on_date_changed(self, selected_date, **kwargs):
        print(f"Date: {selected_date}")

    def _build_ui(self):
        with SinglePageLayout(self.server, full_height=True) as layout:
            with layout.toolbar.clear() as toolbar:
                toolbar.density = "compact"
                toolbar.title = "Date Picker Example"
                vuetify3.VLabel("{{ selected_date }}")
                vuetify3.VBtn("Today", click="selected_date = new Date()")
                vuetify3.VBtn("Today Py", click=self.today)

            with layout.content:
                with vuetify3.VContainer(fluid=True):
                    vuetify3.VDatePicker(
                        v_model=("selected_date", None),
                    )

            return layout


# -----------------------------------------------------------------------------
# Standalone execution
# -----------------------------------------------------------------------------
def main():
    app = DatePickerExample()
    app.server.start()


if __name__ == "__main__":
    main()
