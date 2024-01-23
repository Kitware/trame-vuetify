# require trame-client>=2.15
from trame.app import get_server
from trame.widgets import vuetify3
from trame.ui.vuetify3 import SinglePageLayout
from trame.decorators import TrameApp

NB_STEPS = 5


@TrameApp()
class StepperExample:
    def __init__(self, server=None, table_size=10):
        self.server = get_server(server, client_type="vue3")
        self.ui = self._build_ui()

    def done(self):
        print("We are done...")

    def _build_ui(self):
        with SinglePageLayout(self.server, full_height=True) as layout:
            with layout.toolbar.clear() as toolbar:
                toolbar.density = "compact"
                toolbar.title = "Stepper Example"

            with layout.content:
                with vuetify3.VStepper(
                    v_model=("current_step", 0),
                    items=("steps", [f"Step {i+1}" for i in range(NB_STEPS)]),
                ):
                    with vuetify3.Template(raw_attrs=["v-slot:item.1"]):
                        with vuetify3.VCard(title="Step one", flat=True):
                            vuetify3.VCardText("You need to start here")
                    with vuetify3.Template(raw_attrs=["v-slot:item.2"]):
                        with vuetify3.VCard(title="Step two", flat=True):
                            vuetify3.VCardText("Good middle ground")
                    with vuetify3.Template(raw_attrs=["v-slot:item.3"]):
                        with vuetify3.VCard(title="Step three", flat=True):
                            vuetify3.VCardText("You made it")
                    for i in range(4, NB_STEPS + 1):
                        with vuetify3.Template(raw_attrs=[f"v-slot:item.{i}"]):
                            with vuetify3.VCard(title=f"Step {i} (auto)", flat=True):
                                vuetify3.VCardText(
                                    f"You are getting close {i}/{NB_STEPS}"
                                )

                    # Custom Actions
                    with vuetify3.Template(raw_attrs=['v-slot:actions="{prev, next}"']):
                        with vuetify3.VCardActions():
                            vuetify3.VBtn(
                                "Previous",
                                disabled=("current_step === 1",),
                                click="prev",
                            )
                            vuetify3.VSpacer()
                            vuetify3.VBtn(
                                "Next",
                                v_show=f"current_step < {NB_STEPS}",
                                click="next",
                            )
                            vuetify3.VBtn(
                                "Finish",
                                v_show=f"current_step === {NB_STEPS}",
                                click=self.done,
                            )

            return layout


# -----------------------------------------------------------------------------
# Standalone execution
# -----------------------------------------------------------------------------
def main():
    app = StepperExample()
    app.server.start()


if __name__ == "__main__":
    main()
