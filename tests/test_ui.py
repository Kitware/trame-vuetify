def test_single_page_layout(server):
    from trame.ui.vuetify3 import SinglePageLayout

    layout = SinglePageLayout(server)

    assert layout.server is server
