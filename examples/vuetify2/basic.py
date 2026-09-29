import asyncio
from trame.app import get_server
from trame.widgets import vuetify, html
from trame.ui.vuetify import SinglePageWithDrawerLayout

# -----------------------------------------------------------------------------
# Trame setup
# -----------------------------------------------------------------------------

server = get_server()
server.client_type = "vue2"
state, ctrl = server.state, server.controller

state.menu_items = ["one", "two", "three"]


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
    with layout.toolbar as toolbar:
        toolbar.dense = True
        vuetify.VSpacer()
        vuetify.VCheckbox(
            v_model="$vuetify.theme.dark",
            dense=True,
            hide_details=True,
            off_icon="mdi-theme-light-dark",
            on_icon="mdi-theme-light-dark",
            trueValue="light",
            classes="pa-0 ma-0",
        )
        with vuetify.VBtn(icon=True, click=busy):
            vuetify.VIcon("mdi-sleep")
        with vuetify.VMenu():
            with vuetify.Template(v_slot_activator="{ on, attrs }"):
                with vuetify.VBtn(icon=True, v_bind="attrs", v_on="on"):
                    vuetify.VIcon("mdi-dots-vertical")
            with vuetify.VList():
                with vuetify.VListItem(
                    v_for="(item, i) in menu_items",
                    key="i",
                    value=["item"],
                ):
                    vuetify.VListItemTitle("{{ item }}", click=(print_item, "[item]"))

    with layout.drawer:
        html.Div("Theme: {{ $vuetify.theme.dark }}")
        html.Div("Busy: {{ trame__busy }}")

    # layout.drawer.style = "background: red;"
    # print(layout.html)

if __name__ == "__main__":
    server.start()
