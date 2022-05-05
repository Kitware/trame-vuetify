from trame_client.ui.core import AbstractLayout
from trame_client.widgets import html
from trame_vuetify.widgets import vuetify


def get_trame_versions():
    import pkg_resources

    output = []
    for pkg in pkg_resources.working_set:
        if pkg.key.startswith("trame"):
            output.append(f"{pkg.key.replace('trame-', '')} == {pkg.version}")

    return "\n".join(output)


class VAppLayout(AbstractLayout):
    def __init__(self, _server, template_name="main", **kwargs):
        super().__init__(
            _server,
            vuetify.VApp(id="app", trame_server=_server),
            template_name=template_name,
            **kwargs,
        )


class SinglePageLayout(VAppLayout):
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
                    indeterminate=("trame__busy",),
                    background_opacity=1,
                    bg_color="#01549b",
                    color="#04a94d",
                    size=16,
                    width=3,
                    classes="ml-n3 mr-1",
                ),
                footer.add_child(
                    f'<a href="https://kitware.github.io/trame/" class="grey--text lighten-1--text text-caption text-decoration-none" target="_blank">Powered by trame</a>'
                )
                vuetify.VSpacer()
                reload = self.server.controller.on_server_reload
                if reload.exists():
                    with vuetify.VBtn(
                        x_small=True,
                        icon=True,
                        click=f"trigger('{self.server.trigger_name(reload)}')",
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
                    '<a href="https://www.kitware.com/" class="grey--text lighten-1--text text-caption text-decoration-none" target="_blank">© 2021 Kitware Inc.</a>'
                )


class SinglePageWithDrawerLayout(SinglePageLayout):
    """
    A layout that takes the whole screen, adding a |layout_vuetify_link| for a toolbar, a content, a drawer, and a footer.
    :param name: Text for this page's browser tab (required)
    :type name: str
    :param show_drawer: Whether the drawer is open. Default True
    :type show_drawer: bool
    :param width: How many pixels wide the drawer should be
    :type width: Number
    :param show_drawer_name: The name referencing the drawer's state. Default "drawerOpen".
    :type show_drawer_name: str
    >>> SinglePageWithDrawer("Page with drawer").start()
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
