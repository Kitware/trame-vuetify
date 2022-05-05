from pathlib import Path

# Compute local path to serve
serve_path = str(Path(__file__).with_name("serve").resolve())

# Serve directory for JS/CSS files
serve = {"__trame_vuetify": serve_path}

# List of JS files to load (usually from the serve path above)
scripts = [
    "__trame_vuetify/trame-vuetify.umd.min.js",
]

# List of CSS files to load (usually from the serve path above)
styles = [
    "__trame_vuetify/trame-vuetify.css",
]

# List of Vue plugins to install/load
vue_use = ["trame_vuetify"]
