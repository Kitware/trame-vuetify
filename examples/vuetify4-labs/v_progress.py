import asyncio

import trame_server
from trame.app import TrameApp
from trame.app.asynchronous import create_task

from trame.ui.vuetify4 import VAppLayout
from trame.widgets import html
from trame.widgets import vuetify4 as v4

v4.enable_lab()


class ProgressExample(TrameApp):
    def __init__(self, server: trame_server.Server | str | None = None) -> None:
        super().__init__(server)

        self.state.indeterminate = False
        self.state.loading = False
        self.state.migration_progress = 74

        self.build_ui()

    def build_ui(self) -> None:
        with VAppLayout(self.server) as self.ui:
            with v4.VMain():
                v4.VProgress(
                    model_value=("migration_progress",),
                    label=(
                        "!loading ? 'Ready' : migration_progress < 80 ? 'Loading...' : 'Almost Done...'",
                    ),
                    color="primary",
                    bg_color="surface-variant",
                    rounded=True,
                    indeterminate=("indeterminate",),
                )
                with html.Div(classes="w-100 justify-items-center mt-4"):
                    with html.Div(classes="d-flex w-75 align-center ga-4"):
                        v4.VBtn(
                            children="Start",
                            click=self._on_click,
                            disabled=("loading",),
                        )
                        v4.VSlider(
                            v_model=("migration_progress",),
                            min=0,
                            max=100,
                            step=1,
                            color="primary",
                            hide_details=True,
                            disabled=("loading",),
                        )
                        v4.VCheckbox(
                            v_model=("indeterminate",),
                            label="Indeterminate?",
                            hide_details=True,
                        )

    def _on_click(self) -> None:
        create_task(self._animate())

    async def _animate(
        self, duration: float = 3.0, end_value: int = 100, steps: int = 100
    ) -> None:
        """Incrementally increase a value from 0 to `end_value` over `duration` seconds."""
        self.state.loading = True
        self.state.migration_progress = 0
        # This is just so the animation has time to play for the progress bar resetting
        self.state.flush()
        await asyncio.sleep(0.5)

        sleep_time = duration / steps

        for i in range(steps):
            self.state.migration_progress = (i + 1) * end_value / steps
            self.state.flush()
            await asyncio.sleep(sleep_time)

        self.state.loading = False
        self.state.flush()


def main():
    app = ProgressExample()
    app.server.start()


if __name__ == "__main__":
    main()
