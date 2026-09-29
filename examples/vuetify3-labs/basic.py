import asyncio
from trame.app import get_server
from trame.widgets import vuetify3, html
from trame.ui.vuetify3 import SinglePageWithDrawerLayout

# -----------------------------------------------------------------------------
# Trame setup
# -----------------------------------------------------------------------------

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

state.menu_items = ["one", "two", "three"]
state.theme = "dark"

vuetify3.enable_lab()


@ctrl.add("on_server_reload")
def print_item(item):
    print("Clicked on", item)


async def busy():
    await asyncio.sleep(5)


# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------

state.trame__title = "Menu example"

with SinglePageWithDrawerLayout(server) as layout:
    layout.root.theme = ("theme",)
    with layout.toolbar as toolbar:
        toolbar.dense = "compact"
        vuetify3.VSpacer()
        vuetify3.VCheckboxBtn(
            v_model="theme",
            density="compact",
            false_icon="mdi-theme-light-dark",
            false_value="dark",
            true_icon="mdi-theme-light-dark",
            true_value="light",
            classes="pa-0 ma-0",
            style="max-width: 30px",
        )
        with vuetify3.VBtn(icon=True, click=busy):
            vuetify3.VIcon("mdi-sleep")
        with vuetify3.VMenu(location="bottom"):
            with vuetify3.Template(v_slot_activator="{ props }"):
                with vuetify3.VBtn(icon=True, v_bind="props"):
                    vuetify3.VIcon("mdi-dots-vertical")
            with vuetify3.VList():
                with vuetify3.VListItem(
                    v_for="(item, i) in menu_items",
                    key="i",
                    value=["item"],
                ):
                    vuetify3.VListItemTitle("{{ item }}", click=(print_item, "[item]"))

    with layout.drawer:
        html.Div("Theme: {{ theme }}")
        html.Div("Busy: {{ trame__busy }}")

    # layout.drawer.style = "background: red;"
    # print(layout.html)

if __name__ == "__main__":
    server.start()
