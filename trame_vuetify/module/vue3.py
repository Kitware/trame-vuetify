from pathlib import Path
from trame_vuetify import __version__

serve_path = str(Path(__file__).with_name("vue3-serve").resolve())
serve = {f"__trame_vuetify3_{__version__}": serve_path}
scripts = [f"__trame_vuetify3_{__version__}/vuetify3.js"]
styles = [
    f"__trame_vuetify3_{__version__}/vuetify3.css",
    f"__trame_vuetify3_{__version__}/css/mdi.css",
    "https://fonts.googleapis.com/css?family=Roboto:300,400,500",
]
vue_use = ["Vuetify.createVuetify(trame.state.get('trame__vuetify3_config')||{})"]


def setup(server, **kargs):
    client_type = "vue2"
    if hasattr(server, "client_type"):
        client_type = server.client_type

    if client_type != "vue3":
        msg = f"Server using client_type='{client_type}' while we expect 'vue3'"
        raise TypeError(msg)
