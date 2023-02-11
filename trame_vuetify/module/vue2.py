from pathlib import Path

serve_path = str(Path(__file__).with_name("vue2-serve").resolve())
serve = {"__trame_vuetify": serve_path}
scripts = ["__trame_vuetify/trame-vuetify.umd.min.js"]
styles = ["__trame_vuetify/trame-vuetify.css"]
vue_use = ["trame_vuetify"]


def setup(server, **kargs):
    client_type = "vue2"
    if hasattr(server, "client_type"):
        client_type = server.client_type

    if client_type != "vue2":
        raise TypeError(
            f"Server using client_type='{client_type}' while we expect 'vue2'"
        )
