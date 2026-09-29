from trame_client.ui.core import AbstractLayout

from trame_vuetify.widgets import vuetify4

__all__ = ["VAppLayout"]


def get_trame_versions():
    import importlib.metadata

    from trame_client.utils.version import get_version

    output = []
    for pkg in importlib.metadata.distributions():
        name = pkg.metadata.get("Name", "")
        if name.startswith("trame"):
            version = get_version(name)
            output.append(f"{name.replace('trame-', '')} == {version}")

    return "\n".join(output)


class VAppLayout(AbstractLayout):
    """
    Layout composed of just a `<v-app />`

    :param _server: Server to bound the layout to
    :param template_name: Name of the template (default: main)
    :param vuetify_config: Dict structure to configure vuetify
    """

    def __init__(self, _server, template_name="main", vuetify_config=None, **kwargs):
        super().__init__(
            _server,
            vuetify4.VApp(trame_server=_server, **kwargs),
            template_name=template_name,
            **kwargs,
        )
        if vuetify_config:
            self.server.state.trame__vuetify4_config = vuetify_config
