from pathlib import Path

serve_path = str(Path(__file__).with_name("vue3-serve").resolve())
serve = {"__trame_vuetify3": serve_path}
scripts = ["__trame_vuetify3/vuetify3.js"]
styles = ["__trame_vuetify3/vuetify3.css", "__trame_vuetify3/css/mdi.css"]
vue_use = ["Vuetify.createVuetify(trame.state.get('trame__vuetify3_config')||{})"]


def setup(server, **kargs):
    client_type = "vue2"
    if hasattr(server, "client_type"):
        client_type = server.client_type

    if client_type != "vue3":
        raise TypeError(
            f"Server using client_type='{client_type}' while we expect 'vue3'"
        )
