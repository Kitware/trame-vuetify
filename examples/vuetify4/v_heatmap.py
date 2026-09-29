import trame_server
from trame.app import TrameApp

from trame.ui.vuetify4 import SinglePageLayout
from trame.widgets import html
from trame.widgets import vuetify4 as v4

v4.enable_lab()


class HeatmapExample(TrameApp):
    def __init__(self, server: trame_server.Server | str | None = None) -> None:
        super().__init__(server)

        self.state.week_rows = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        self.state.week_columns = [f"W{i + 1}" for i in range(12)]
        self.state.heatmap_items = [
            {
                "row": row,
                "column": column,
                "value": (
                    (col_idx + 3) * 17 + (row_idx + 2) * 23 + col_idx * row_idx * 7
                )
                % 100,
            }
            for col_idx, column in enumerate(self.state.week_columns)
            for row_idx, row in enumerate(self.state.week_rows)
        ]
        self.state.heatmap_thresholds = [
            {"min": "0", "color": "#172033"},
            {"min": "20", "color": "#193b4d"},
            {"min": "40", "color": "#1d6370"},
            {"min": "60", "color": "#20a08c"},
            {"min": "80", "color": "#55d6a9"},
        ]
        self.state.heatmap_legend = {
            "labels": [
                "Quiet",
                "Low",
                "Normal",
                "Busy",
                "Hot",
            ],
        }
        self.state.cell_size = [24, 24]

        self._build_ui()

    def _build_ui(self) -> None:
        with SinglePageLayout(self.server) as layout:
            with layout.content:
                with html.Div(classes="d-flex flex-column align-center ga-5 mt-3"):
                    v4.VHeatmap(
                        classes="w-66",
                        items=("heatmap_items",),
                        rows=("week_rows",),
                        columns=("week_columns",),
                        thresholds=("heatmap_thresholds",),
                        cell_size=("cell_size",),
                        gap=5,
                        legend=("heatmap_legend",),
                        rounded="6",
                        hover=True,
                    )


def main():
    app = HeatmapExample()
    app.server.start()


if __name__ == "__main__":
    main()
