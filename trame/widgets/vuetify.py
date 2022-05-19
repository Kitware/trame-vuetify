from trame_vuetify.widgets.vuetify import *


def initialize(server):
    from trame_vuetify import module

    server.enable_module(module)
