def test_import_modules():
    from trame.modules import vuetify, vuetify2, vuetify3, vuetify3_lab

    assert vuetify
    assert vuetify2
    assert vuetify3
    assert vuetify3_lab


def test_import_widgets():
    from trame.widgets import vuetify, vuetify2, vuetify3

    assert vuetify
    assert vuetify2
    assert vuetify3
