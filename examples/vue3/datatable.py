"""pip install Faker"""

from trame.app import get_server
from trame.widgets import vuetify3
from trame.ui.vuetify3 import SinglePageLayout
from trame.decorators import TrameApp, change, life_cycle, hot_reload

from faker import Faker

FAKE_DATA = Faker()
PROFILE_KEEP = {"name", "residence", "job", "company", "sex", "mail", "ssn"}


def fake_profile(id):
    profile = FAKE_DATA.profile()
    return {"id": id, **{k: profile[k] for k in PROFILE_KEEP}}


@TrameApp()
class TableExample:
    def __init__(self, server=None, table_size=10):
        self.server = get_server(server, client_type="vue3")
        self.table_size = table_size
        self.ui = self._build_ui()
        self.load_data()

    @property
    def state(self):
        return self.server.state

    @life_cycle.server_reload
    @life_cycle.server_ready
    def reload_ui(self, *args, **kwargs):
        self.ui = self._build_ui()

    def load_data(self):
        self.state.table_content = [fake_profile(i) for i in range(self.table_size)]
        self.state.table_header = [
            dict(
                key="name",
                title="Name",
                align="left",
                sortable=True,
            ),
            dict(
                key="residence",
                title="Address",
                align="center",
            ),
            dict(
                key="job",
                title="Title",
                align="center",
            ),
            dict(
                key="company",
                title="Company",
                align="center",
                sortable=True,
            ),
            dict(
                key="sex",
                title="Sex",
                align="center",
                sortable=True,
            ),
            dict(
                key="mail",
                title="E-Mail",
                align="left",
                sortable=True,
            ),
        ]

    @change("table_selection_id")
    def on_selection(self, table_selection_id, table_content, **kwargs):
        if len(table_selection_id) == 1:
            selected_item = table_content[table_selection_id[0]]
            self.state.selected_email = selected_item.get("mail")
            print(selected_item)
        else:
            self.state.selected_email = None
            print("No selection")

    @hot_reload
    def _build_ui(self):
        with SinglePageLayout(self.server, full_height=True) as layout:
            with layout.toolbar.clear() as toolbar:
                toolbar.density = "compact"
                toolbar.title = "Data Table Example"
                vuetify3.VSpacer()
                vuetify3.VLabel(
                    "{{ selected_email }}",
                    v_show=("selected_email", ""),
                    classes="mx-2",
                )

            with layout.content:
                # content.classes = "fill-height"
                with vuetify3.VDataTableVirtual(
                    # For style
                    density="compact",
                    fixed_header=True,
                    height="calc(100vh - 48px - 22px)",
                    hover=True,
                    # For content
                    headers=("table_header", []),
                    items=("table_content", []),
                    # For selection
                    v_model=("table_selection_id", []),
                    select_strategy="single",
                    item_value=("v => v.id",),
                ):
                    with vuetify3.Template(v_slot_item="slotData"):
                        vuetify3.VDataTableRow(
                            v_bind="slotData.props",
                            click="slotData.toggleSelect({value: slotData.item.id, selectable: true})",
                            classes=(
                                "{ 'bg-blue': slotData.isSelected([{value: slotData.item.id, selectable: true}])}",
                            ),
                        )

            # print(layout)
            return layout


def main():
    app = TableExample()
    app.server.start()


if __name__ == "__main__":
    main()
