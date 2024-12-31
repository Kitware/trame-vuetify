from trame_vuetify.widgets.vuetify3 import *  # noqa F403


def initialize(server):
    from trame_vuetify.module import vue3

    server.enable_module(vue3)
