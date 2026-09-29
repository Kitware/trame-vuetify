from trame_vuetify.widgets.vuetify4 import *  # noqa F403


def initialize(server):
    from trame_vuetify.module import v4

    server.enable_module(v4)
