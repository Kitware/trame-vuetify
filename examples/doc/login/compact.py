from trame.app import get_server
from trame.ui.vuetify3 import VAppLayout
from trame.widgets import vuetify3 as v3


class App:
    def __init__(self, server=None):
        self.server = get_server(server)
        self._build_ui()

    @property
    def state(self):
        return self.server.state

    def auth(self):
        if self.state.login_email != "trame@kitware.com":
            self.state.error_msg = "Invalid login"
            return

        if self.state.login_password != "password":
            self.state.error_msg = "Invalid password"
            return

        self.state.error_msg = None
        self._auth_ui()

    def _auth_ui(self):
        with VAppLayout(self.server, fill_height=True) as self.ui:
            with v3.VMain(classes="h-100 d-flex align-center justify-center"):
                v3.VAlert(
                    title="Logged in...",
                    border="start",
                    border_color="success",
                    classes="w-50 flex-0-0",
                )

    def _build_ui(self):
        with VAppLayout(self.server, fill_height=True) as self.ui:
            with v3.VMain():
                with v3.VContainer(classes="h-100 pa-4", fluid=True):
                    with v3.VRow(align="center", classes="h-100", justify="center"):
                        with v3.VSheet(
                            classes="flex-1-1 px-4", color="background", max_width=420
                        ):
                            with v3.VSheet(
                                border="opacity-25 thin",
                                classes="overflow-hidden",
                                rounded="lg",
                            ):
                                v3.VTextField(
                                    v_model=("login_email", ""),
                                    density="compact",
                                    flat=True,
                                    hide_details=True,
                                    placeholder="Email",
                                    rounded="lg",
                                    variant="solo",
                                )
                                v3.VDivider()
                                v3.VTextField(
                                    v_model=("login_password", ""),
                                    type="password",
                                    density="compact",
                                    flat=True,
                                    hide_details=True,
                                    placeholder="Password",
                                    rounded="lg",
                                    variant="solo",
                                )

                            v3.VBtn(
                                block=True,
                                classes="text-none my-8",
                                color="primary",
                                flat=True,
                                rounded="lg",
                                text="Log In",
                                click=self.auth,
                            )

                            v3.VAlert(
                                v_if="error_msg",
                                title=("error_msg", None),
                                type="error",
                            )


def main():
    app = App()
    app.server.start()


if __name__ == "__main__":
    main()
