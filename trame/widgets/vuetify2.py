from trame_vuetify.widgets.vuetify import *


def initialize(server):
    from trame_vuetify.module import vue2

    server.enable_module(vue2)
