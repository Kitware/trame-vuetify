import asyncio

from trame.app import get_server

from trame.ui.vuetify4 import VAppLayout
from trame.widgets import html, vuetify4

# -----------------------------------------------------------------------------
# Trame setup
# -----------------------------------------------------------------------------

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

state.trame__title = "Menu example"
state.drawer_open = False
state.menu_items = ["one", "two", "three"]
state.theme = "dark"


@ctrl.add("on_server_reload")
def print_item(item):
    print("Clicked on", item)


async def busy():
    await asyncio.sleep(5)


# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------


with VAppLayout(server) as layout:
    layout.root.theme = ("theme",)
    with vuetify4.VLayout():
        with vuetify4.VAppBar():
            with html.Div(classes="d-flex w-100"):
                vuetify4.VBtn(icon="mdi-menu", click="drawer_open = !drawer_open")
                vuetify4.VSpacer()
                vuetify4.VCheckboxBtn(
                    v_model="theme",
                    density="compact",
                    false_icon="mdi-theme-light-dark",
                    false_value="dark",
                    true_icon="mdi-theme-light-dark",
                    true_value="light",
                    classes="pa-0 ma-0",
                    style="max-width: 30px",
                )
                with vuetify4.VBtn(icon=True, click=busy):
                    vuetify4.VIcon("mdi-sleep")
                with vuetify4.VMenu(location="bottom"):
                    with vuetify4.Template(v_slot_activator="{ props }"):
                        with vuetify4.VBtn(icon=True, v_bind="props"):
                            vuetify4.VIcon("mdi-dots-vertical")
                    with vuetify4.VList():
                        with vuetify4.VListItem(
                            v_for="(item, i) in menu_items",
                            key="i",
                            value=["item"],
                        ):
                            vuetify4.VListItemTitle(
                                "{{ item }}", click=(print_item, "[item]")
                            )
        with vuetify4.VMain():
            html.P("This example shows how to build your own drawer layout")
        with vuetify4.VNavigationDrawer(
            model_value=("drawer_open",),
            width=350,
        ):
            html.Div("Theme: {{ theme }}")
            html.Div("Busy: {{ trame__busy }}")


if __name__ == "__main__":
    server.start()
