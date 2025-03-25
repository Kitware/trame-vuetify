from trame_client.ui.core import AbstractLayout
from trame_client.widgets import html
from trame_vuetify.widgets import vuetify3

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
    :param vuetify_config: Dict structure to configure vuetify
    """

    def __init__(self, _server, template_name="main", vuetify_config=None, **kwargs):
        super().__init__(
            _server,
            vuetify3.VApp(trame_server=_server, **kwargs),
            template_name=template_name,
            **kwargs,
        )
        if vuetify_config:
            self.server.state.trame__vuetify3_config = vuetify_config


class SinglePageLayout(VAppLayout):
    """
    Layout composed of the following structure:

    :param _server: Server to bound the layout to
    :param template_name: Name of the template (default: main)
    :param vuetify_config: Dict structure to configure vuetify


    .. code-block::

        <v-app>
            <v-layout>                              # layout.app_layout
                <v-app-bar>                         # layout.toolbar
                    <v-app-bar-nav-icon />          # layout.icon
                    <v-toolbar-title>               # layout.title
                        Trame application
                    </v-toolbar-title>
                </v-app-bar>
                <v-main />                          # layout.content
                <v-footer app border class="my-0 py-0">    # layout.footer
                    < ... />
                </v-footer>
            </v-layout>
        </v-app>

    """

    def __init__(self, _server, template_name="main", **kwargs):
        super().__init__(_server, template_name=template_name, **kwargs)
        with self:
            with vuetify3.VLayout() as app_layout:
                self.app_layout = app_layout
                with vuetify3.VAppBar() as toolbar:
                    self.toolbar = toolbar
                    self.icon = vuetify3.VAppBarNavIcon()
                    self.title = vuetify3.VToolbarTitle("Trame application")

                self.content = vuetify3.VMain()

                with vuetify3.VFooter(
                    app=True, classes="my-0 py-0", border=True
                ) as footer:
                    self.footer = footer
                    vuetify3.VProgressCircular(
                        indeterminate=("!!trame__busy",),
                        color="#04a94d",
                        size=16,
                        width=3,
                        classes="ml-n3 mr-1",
                    )
                    footer.add_child(
                        '<a href="https://kitware.github.io/trame/" '
                        'class="text-grey-lighten-1 text-caption text-decoration-none" '
                        'target="_blank">Powered by trame</a>'
                    )
                    vuetify3.VSpacer()
                    reload = self.server.controller.on_server_reload
                    if reload.exists():
                        with vuetify3.VBtn(
                            size="x-small",
                            density="compact",
                            icon=True,
                            # border=True,
                            elevation=0,
                            click=self.on_server_reload,
                            classes="mx-2",
                        ):
                            vuetify3.VIcon("mdi-autorenew", size="small")

                    with vuetify3.VTooltip(location="top"):
                        with vuetify3.Template(v_slot_activator=("{ props }",)):
                            vuetify3.VIcon(
                                "mdi-help-circle",
                                size=14,
                                classes="mr-4",
                                v_bind=("props",),
                            )
                        html.Pre(get_trame_versions())

                    footer.add_child(
                        '<a href="https://www.kitware.com/" '
                        'class="text-grey-lighten-1 text-caption text-decoration-none" '
                        'target="_blank">© 2025 Kitware Inc.</a>'
                    )

    def on_server_reload(self):
        self.server.controller.on_server_reload(self.server)


class SinglePageWithDrawerLayout(SinglePageLayout):
    """
    Layout composed of the following structure:

    :param _server: Server to bound the layout to
    :param template_name: Name of the template (default: main)
    :param vuetify_config: Dict structure to configure vuetify

    :param show_drawer: Start with drawer open (default: True)
    :param width: Drawer width in pixel (default: 300)

    .. code-block::

        <v-app>
            <v-layout>                              # layout.app_layout
                <v-app-bar>                        # layout.toolbar
                    <v-app-bar-nav-icon />          # layout.icon
                    <v-toolbar-title>               # layout.title
                        Trame application
                    </v-toolbar-title>
                </v-app-bar>
                <v-main />                          # layout.content
                <v-footer app border class="my-0 py-0">    # layout.footer
                    < ... />
                </v-footer>

                <v-navigation-drawer                # layout.drawer
                    app
                    clipped
                    stateless
                    v-model="{template_name}_drawer"
                    width="width"
                />
            </v-layout>

        </v-app>

    """

    def __init__(
        self, _server, template_name="main", show_drawer=True, width=300, **kwargs
    ):
        super().__init__(_server, template_name=template_name, **kwargs)
        drawer_name = f"{template_name}_drawer"
        with self.app_layout:
            self.drawer = vuetify3.VNavigationDrawer(
                disable_resize_watcher=True,
                disable_route_watcher=True,
                permanent=True,
                location="left",
                v_model=(f"{drawer_name}", {drawer_name: show_drawer}),
                width=width,
            )
        self.icon.click = f"{drawer_name} = !{drawer_name}"
