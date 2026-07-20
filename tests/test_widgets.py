from trame.app import get_server


def test_vuetify():
    from trame.widgets.vuetify import VBtn

    server = get_server("test-widget-vuetify", client_type="vue2")

    VBtn(trame_server=server)


def test_vuetify2():
    from trame.widgets.vuetify2 import VBtn

    server = get_server("test-widget-vuetify2", client_type="vue2")

    VBtn(trame_server=server)


def test_vuetify3():
    from trame.widgets.vuetify3 import VBtn

    server = get_server("test-widget-vuetify3", client_type="vue3")

    VBtn(trame_server=server)
