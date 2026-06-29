from pathlib import Path
from trame_vuetify import __version__

serve_path = str(Path(__file__).with_name("vue2-serve").resolve())
serve = {f"__trame_vuetify2_{__version__}": serve_path}
scripts = [f"__trame_vuetify2_{__version__}/trame-vuetify.umd.min.js"]
styles = [f"__trame_vuetify2_{__version__}/trame-vuetify.css"]
vue_use = ["trame_vuetify"]


def setup(server, **kargs):
    client_type = "vue2"
    if hasattr(server, "client_type"):
        client_type = server.client_type

    if client_type != "vue2":
        raise TypeError(
            f"Server using client_type='{client_type}' while we expect 'vue2'"
        )
