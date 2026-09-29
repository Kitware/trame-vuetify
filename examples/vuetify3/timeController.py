import asyncio
from trame.app import get_server, asynchronous
from trame.widgets import vuetify3 as v3
from trame.ui.vuetify3 import SinglePageLayout

# -----------------------------------------------------------------------------
# Trame setup
# -----------------------------------------------------------------------------


class TimeController(v3.VCol):
    def __init__(
        self, name="time_controller", ranges=[(0, 100, 1)], values=[50], **kwargs
    ):
        super().__init__(**kwargs)

        self._base = name
        self.server.state[self.key_ranges] = ranges
        self.server.state[self.key_values] = values

        with self:
            with v3.Template(v_for=f"range, idx in {self.key_ranges}"):
                v3.VSlider(
                    min=("range[0]",),
                    max=("range[1]",),
                    step=("range[2]",),
                    model_value=(f"{self.key_values}[idx]",),
                    update_modelValue=f"{self.key_values}[idx] = $event; flushState('{self.key_values}');",
                    hide_details=True,
                    density="compact",
                    show_ticks="always",
                )
            with v3.VRow(classes="d-flex justify-space-around my-2"):
                v3.VBtn(
                    icon="mdi-skip-previous",
                    density="compact",
                    variant="flat",
                    click=self.first,
                )
                v3.VBtn(
                    icon="mdi-chevron-left",
                    density="compact",
                    variant="flat",
                    click=self.previous,
                )
                v3.VBtn(
                    icon="mdi-play", density="compact", variant="flat", click=self.play
                )
                v3.VBtn(
                    icon="mdi-stop", density="compact", variant="flat", click=self.stop
                )
                v3.VBtn(
                    icon="mdi-chevron-right",
                    density="compact",
                    variant="flat",
                    click=self.next,
                )
                v3.VBtn(
                    icon="mdi-skip-next",
                    density="compact",
                    variant="flat",
                    click=self.last,
                )

    @property
    def key_ranges(self):
        return f"{self._base}_ranges"

    @property
    def key_values(self):
        return f"{self._base}_values"

    @property
    def key_play(self):
        return f"{self._base}_playing"

    async def _play_loop(self):
        while self.server.state[self.key_play]:
            await asyncio.sleep(0.1)
            with self.server.state:
                self.next()

    def get_values(self):
        return self.server.state[self.key_values]

    def set_values(self, v):
        self.server.state[self.key_values] = v

    def get_ranges(self):
        return self.server.state[self.key_ranges]

    def set_ranges(self, v):
        self.server.state[self.key_ranges] = v

    def validate_ranges(self):
        ranges = self.get_ranges()
        values = self.get_values()
        size = len(values)
        indexes = list(range(size))[::-1]
        for idx in indexes:
            min, max, _ = ranges[idx]
            v = values[idx]
            if v < min:
                values[idx] = max
                if idx > 0:
                    values[idx - 1] -= ranges[idx - 1][2]
            if v > max:
                values[idx] = min
                if idx > 0:
                    values[idx - 1] += ranges[idx - 1][2]

    def next(self):
        ranges = self.get_ranges()
        new_value = list(self.get_values())
        new_value[-1] += ranges[-1][2]
        self.set_values(new_value)
        self.validate_ranges()

    def first(self):
        first_value = []
        for r in self.get_ranges():
            first_value.append(r[0])
        self.server.state[self.key_values] = first_value

    def last(self):
        last_value = []
        for r in self.get_ranges():
            last_value.append(r[1])
        self.server.state[self.key_values] = last_value

    def previous(self):
        ranges = self.get_ranges()
        new_value = list(self.get_values())
        new_value[-1] -= ranges[-1][2]
        self.set_values(new_value)
        self.validate_ranges()

    def play(self):
        if self.server.state[self.key_play]:
            return

        self.server.state[self.key_play] = True
        asynchronous.create_task(self._play_loop())

    def stop(self):
        self.server.state[self.key_play] = False


class DemoApp:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self.time_controller = None
        self._build_ui()

    @property
    def state(self):
        return self.server.state

    def setup_1(self):
        self.state[self.time_controller.key_ranges] = [
            (1999, 2024, 1),
            (1, 12, 1),
            (1, 31, 1),
        ]
        self.state[self.time_controller.key_values] = [
            1999,
            1,
            1,
        ]

    def setup_2(self):
        self.state[self.time_controller.key_ranges] = [
            (1999, 2024, 1),
            (1, 12, 1),
            (1, 31, 1),
            (0, 24, 1),
            (0, 59, 1),
        ]
        self.state[self.time_controller.key_values] = [
            1999,
            1,
            1,
            0,
            0,
        ]

    def _build_ui(self):
        with SinglePageLayout(self.server) as layout:
            with layout.content:
                self.time_controller = TimeController()

            with layout.toolbar:
                v3.VSpacer()
                v3.VBtn("1", click=self.setup_1)
                v3.VBtn("2", click=self.setup_2)
                v3.VLabel(f"{{{{ {self.time_controller.key_values} }}}}")


if __name__ == "__main__":
    app = DemoApp()
    app.server.start()
