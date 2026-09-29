import trame_server
from trame.app import TrameApp

from trame.ui.vuetify4 import VAppLayout
from trame.widgets import html
from trame.widgets import vuetify4 as v4

v4.enable_lab()


class MonthPickerExample(TrameApp):
    def __init__(self, server: trame_server.Server | str | None = None) -> None:
        super().__init__(server)

        self.state.month_range = ["2026-09", "2026-12"]

        self._build_ui()

    def _build_ui(self) -> None:
        with VAppLayout(self.server):
            with v4.VMain():
                with html.Div(classes="d-flex flex-column align-center ga-5 mt-3"):
                    html.Span("Selected range: {{ month_range.join(' - ') }}")
                    v4.VMonthPicker(
                        v_model=("month_range",),
                        multiple="range",
                        color="primary",
                        months_columns=3,
                        hide_header=True,
                    )


def main():
    app = MonthPickerExample()
    app.server.start()


if __name__ == "__main__":
    main()
