from trame_client.ui.core import AbstractLayout
from trame_client.widgets import html
from trame_vuetify.widgets import vuetify

__all__ = [
    "VAppLayout",
    "SinglePageLayout",
    "SinglePageWithDrawerLayout",
]


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
    """

    def __init__(self, _server, template_name="main", **kwargs):
        super().__init__(
            _server,
            vuetify.VApp(id="app", trame_server=_server),
            template_name=template_name,
            **kwargs,
        )


class SinglePageLayout(VAppLayout):
    """
    Layout composed of the following structure:

    :param _server: Server to bound the layout to
    :param template_name: Name of the template (default: main)


    .. code-block::

        <v-app id="app">
            <v-app-bar app>                     # layout.toolbar
                <v-app-bar-nav-icon />          # layout.icon
                <v-toolbar-title>               # layout.title
                    Trame application
                </v-toolbar-title>
            </v-app-bar>
            <v-main />                          # layout.content
            <v-footer app class="my-0 py-0">    # layout.footer
                < ... />
            </v-footer>
        </v-app>

    """

    def __init__(self, _server, template_name="main", **kwargs):
        super().__init__(_server, template_name=template_name, **kwargs)
        with self:
            with vuetify.VAppBar(app=True) as toolbar:
                self.toolbar = toolbar
                self.icon = vuetify.VAppBarNavIcon()
                self.title = vuetify.VToolbarTitle("Trame application")
            self.content = vuetify.VMain()
            with vuetify.VFooter(app=True, classes="my-0 py-0") as footer:
                self.footer = footer

                vuetify.VProgressCircular(
                    indeterminate=("!!trame__busy",),
                    background_opacity=1,
                    bg_color="#01549b",
                    color="#04a94d",
                    size=16,
                    width=3,
                    classes="ml-n3 mr-1",
                )

                footer.add_child(
                    '<a href="https://kitware.github.io/trame/" '
                    'class="grey--text lighten-1--text text-caption text-decoration-none" '
                    'target="_blank">Powered by trame</a>'
                )
                vuetify.VSpacer()
                reload = self.server.controller.on_server_reload
                if reload.exists():
                    with vuetify.VBtn(
                        x_small=True,
                        icon=True,
                        click=self.on_server_reload,
                        classes="mx-2",
                    ):
                        vuetify.VIcon("mdi-autorenew", x_small=True)

                with vuetify.VTooltip(top=True):
                    with vuetify.Template(v_slot_activator="{on, attrs}"):
                        vuetify.VIcon(
                            "mdi-help-circle",
                            x_small=True,
                            classes="mr-4",
                            v_bind="attrs",
                            v_on="on",
                            __properties=[("v_bind", "v-bind"), ("v_on", "v-on")],
                        )
                    html.Pre(get_trame_versions())

                footer.add_child(
                    '<a href="https://www.kitware.com/" '
                    'class="grey--text lighten-1--text text-caption text-decoration-none" '
                    'target="_blank">© 2025 Kitware Inc.</a>'
                )

    def on_server_reload(self):
        self.server.controller.on_server_reload(self.server)


class SinglePageWithDrawerLayout(SinglePageLayout):
    """
    Layout composed of the following structure:

    :param _server: Server to bound the layout to
    :param template_name: Name of the template (default: main)
    :param show_drawer: Start with drawer open (default: True)
    :param width: Drawer width in pixel (default: 300)

    .. code-block::

        <v-app id="app">
            <v-app-bar app>                     # layout.toolbar
                <v-app-bar-nav-icon />          # layout.icon
                <v-toolbar-title>               # layout.title
                    Trame application
                </v-toolbar-title>
            </v-app-bar>
            <v-main />                          # layout.content
            <v-footer app class="my-0 py-0">    # layout.footer
                < ... />
            </v-footer>
            <v-navigation-drawer                # layout.drawer
                app
                clipped
                stateless
                v-model="{template_name}_drawer"
                width="width"
            />
        </v-app>

    """

    def __init__(
        self, _server, template_name="main", show_drawer=True, width=300, **kwargs
    ):
        super().__init__(_server, template_name=template_name, **kwargs)
        drawer_name = f"{template_name}_drawer"
        with self:
            self.drawer = vuetify.VNavigationDrawer(
                app=True,
                clipped=True,
                stateless=True,
                v_model=(drawer_name, show_drawer),
                width=width,
            )
        self.toolbar.clipped_left = True
        self.icon.click = f"{drawer_name} = !{drawer_name}"
