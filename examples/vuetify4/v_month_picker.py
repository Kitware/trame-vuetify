from trame.app import get_server
from trame.decorators import TrameApp

from trame.ui.vuetify4 import SinglePageLayout
from trame.widgets import html
from trame.widgets import vuetify4 as v4

v4.enable_lab()


@TrameApp()
class MonthPickerExample:
    def __init__(self) -> None:
        self.server = get_server(None)
        self.state = self.server.state

        self.state.month_range = ["2026-09", "2026-12"]

        self._build_ui()

    def _build_ui(self) -> None:
        with SinglePageLayout(self.server) as layout:
            with layout.content:
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
