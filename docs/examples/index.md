# trame-vuetify

Trame includes all standard HTML tags by default, but for crafting visually appealing user interfaces, Vuetify provides an advantage with its curated, high-quality component library.

## Installation

To integrate Vuetify into your __trame__ application, you can either install the trame-vuetify package or define it as a dependency within your project.

If you'd like to set up a fresh virtual environment with both __trame__ and __trame-vuetify__, simply run the following commands:

```sh
# Linux and macOS
python3 -m venv .venv
source .venv/bin/activate
pip install trame trame-vuetify

# Windows
python3 -m venv .venv
.\.venv\Scripts\activate
pip install trame trame-vuetify
```

## Usage

Trame-vuetify comes pre-configured with __Vuetify 2__, __Vuetify 3__, and __Vuetify Labs__. The appropriate version is automatically selected based on your trame server initialization (`client_type="vue2/3"`). If `vue2` is specified, __Vuetify 2__ will be used, while `vue3` will load __Vuetify 3__.

To use __Vuetify Labs__, set `client_type="vue3"` and also request the lab in the vuetify3 widget module, as shown below.

```python
from trame.app import get_server
from trame.ui.vuetify3 import VAppLayout
from trame.widgets import vuetify3

# Needed to enable experimental components before official release
vuetify3.enable_lab()

class App:
    def __init__(self, server=None):
        self.server = get_server(client_type="vue3")
        self._build_ui()

    def _build_ui(self):
        with VAppLayout(self.server) as layout:
            self.ui = layout

            vuetify3.VBtn("Hello from the Lab")


if __name__ == "__main__":
    app = App()
    app.server.start()
```

## Learning the syntax

When experimenting with Vuetify, it’s a good idea to start with the [PlayGround](https://play.vuetifyjs.com/) to explore the components and their APIs. You can refer to the [Vuetify 3](https://vuetifyjs.com/en/components/all/) or [Vuetify 2](https://v2.vuetifyjs.com/en/) documentation to learn more about the available components for building your user interface.

Once you're ready to convert your PlayGround template into Python for Trame, you can follow a set of guidelines to ensure a smooth transition.

__From the vue template...__

```html
<v-card>
  <v-card-title>Hello</v-card-title>
  <v-card-text>
    World
    <v-text-field
       label="Max value"
       v-model.number="maxValue"
    />
    <v-slider
       v-model="slider"
       min="1"
       :max="maxValue"
       hide-details
    />
  <v-card-text>
</v-card>
```

__To Python for trame...__

```python
from trame.widgets import vuetify3 as v3

# [...]

with v3.VCard() as card:        # Use camel case for class name (<v-card>)
    v3.VCardTitle("Hello")      # Component with text as child
    with v3.VCardText("World"): # use with to nest other components under
        v3.VTextField(          # Replace any invalid character ".-:"" to "_" in keyword
            # We use a tuple to define the variable name and its default/initial value
            v_model_number=("maxValue", 10), 
        )
        v3.VSlider(
            # We use a tuple to define the variable name and its default/initial value
            v_model=("slider", 5),
            # Will be converted to string (min="1")
            min=1,
            # Tuple needed to force evaluation (:max="maxValue")
            max=("maxValue",), 
            # Implicit boolean attribue, need explicit assignemnt in Python
            hide_detail=True 
        )
    
    # To validate/debug, you can print any part of the hierarchy and compare it with the one expected from the playground
    print(card)

```

If any attributes are missing, you can register custom ones using `__properties=[(py_key, js_attr), ...]` and `__events=[(py_key, js_attr), ...]`. Additionally, you can include raw attributes with `raw_attrs=['@click.stop="exit = true"', ...]`. For more details, the [Widget API](https://trame.readthedocs.io/en/latest/core.widget.html#widget) provides further guidance.

## Missing an example and running into issue?

Looking for examples to help you make the most of each component? The [Assist+](./support.html#the-assist) product provides hands-on guidance, including custom examples tailored to your needs.

And if you’re focused on reliable support and peace of mind, our [Essential](./support.html#the-essential) plan ensures comprehensive bug fixes across all [supported libraries](https://github.com/topics/trame-maintenance-program) as part of our maintenance program.