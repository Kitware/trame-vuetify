from trame.app import get_server
from trame.widgets import vuetify3, html
from trame.ui.vuetify3 import SinglePageLayout
import itertools
import random


# -----------------------------------------------------------------------------
# Trame setup
# -----------------------------------------------------------------------------

server = get_server(client_type="vue3")
state, ctrl = server.state, server.controller

vuetify3.enable_lab()

newid = itertools.count().__next__

MAX_DEPTH = 5


def generate_node(n_children, depth=0):
    key = newid()
    children = []
    if depth < MAX_DEPTH:
        children = [
            generate_node(random.randint(0, 5), depth + 1) for i in range(n_children)
        ]

    if len(children):
        return dict(id=key, title=f"Node {key}", children=children)

    return dict(id=key, title=f"Node {key}")


TREE = [generate_node(random.randint(0, 5), 0) for i in range(5)]

with SinglePageLayout(server) as layout:
    with layout.toolbar:
        html.Div("{{ active_node }}")
    with layout.content:
        vuetify3.VTreeview(
            # style
            slim=True,
            density="compact",
            # data
            item_value="id",
            items=("tree", TREE),
            # activation logic
            activated=("active_node", []),
            activatable=True,
            active_strategy="single-independent",
            update_activated="active_node = $event",  # Emits the item when it is clicked to select.)
        )

if __name__ == "__main__":
    server.start()
