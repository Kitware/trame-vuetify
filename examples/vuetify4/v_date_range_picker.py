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

        self.state.date_range = []
        self.state.independent_months = False

        self._build_ui()

    def _build_ui(self) -> None:
        with SinglePageLayout(self.server) as layout:
            with layout.content:
                with html.Div(classes="d-flex flex-column align-center ga-5 mt-3"):
                    html.Span(
                        "Selected range: {{date_range.map(d => d.toISOString().slice(0, 10)).join(' - ')}}"
                    )
                    v4.VCheckbox(
                        v_model=("independent_months",),
                        label="Independent Months?",
                    )
                    v4.VDateRangePicker(
                        v_model=("date_range",),
                        independent_months=("independent_months",),
                        color="primary",
                        width="100%",
                    )


def main():
    app = MonthPickerExample()
    app.server.start()


if __name__ == "__main__":
    main()
