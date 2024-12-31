#!/usr/bin/env python3

import sys
import argparse
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DEST_FILE = BASE_DIR / Path("trame_vuetify/widgets/vuetify.py")
INPUT_JSON = BASE_DIR / Path("vue2/node_modules/vuetify/dist/json/web-types.json")
HEADER_FILE = Path(__file__).with_name(".header.py")

# ----------------------------------------
# Helpers
# ----------------------------------------

with open(HEADER_FILE) as header:
    module_header = header.read()

tts_sensitive_elements = [
    "VSelect",
    "VDataTable",
]


def get_attributes(tag):
    attributes = []
    for attribute in tag.get("attributes"):
        name = attribute.get("name")
        if "(" in name:
            entry = expand_parenthetical(name, attributes)
        else:
            entry = '"' + name.replace("-", "_") + '",'
            types = attribute.get("value", {}).get("type")
            if "function" in types:
                entry += "  # JS functions unimplemented"
            attributes.append(entry)

    joined_attributes = "\n            ".join(attributes)
    return f"""
        self._attr_names += [
            {joined_attributes}
        ]"""


def get_events(tag):
    events = []
    for event in tag.get("events"):
        entry = event.get("name")
        if "<" in entry:
            expand_dom_events(entry, events)
        else:
            if "-" in entry or ":" in entry:
                _entry = entry.replace(":", "_").replace("-", "_")
                entry = f'("{_entry}", "{entry}"),'
            else:
                entry = f'"{entry}",'
            events.append(entry)

    joined_events = "\n            ".join(events)
    return f"""
        self._event_names += [
            {joined_events}
        ]"""


def clean_description(description):
    description = description.replace("\n", " ").replace("\\|", "|")
    return split_description(link_description(description))


def link_description(description):
    if "](" in description:
        description = description.replace("[", "`")
        description = description.replace("](", " <")
        description = description.replace(")", ">`_")
    return description


def split_description(description):
    if len(description) > 80:
        tokens = description.split(" ")
        description_lines = []
        while len(tokens):
            line = []
            while len(" ".join(line)) < 60 and len(tokens):
                line.append(tokens.pop(0))
            description_lines.append(" ".join(line))
            line = []
        if len(line):
            description_lines.append(" ".join(line))

        description = "\n        ".join(description_lines)
    return description


def get_docs(tag):
    url = tag.get("doc-url", "https://vuetifyjs.com/en/introduction/why-vuetify/")
    url = url.replace("www.", "")  # www redirects to start page

    name = tag.get("name")
    attributes = tag.get("attributes", [])
    params = []
    for attribute in attributes:
        raw_name = attribute.get("name")
        attribute_name = raw_name.replace("-", "_")
        attribute_type = attribute.get("value", {}).get("type", "string")
        description = clean_description(attribute.get("description"))

        params.append(
            f"\n      {attribute_name} ({attribute_type}):\n        {description}"
        )

    events = tag.get("events")
    for event in events:
        entry = event.get("name")
        description = clean_description(event.get("description"))

        # Ignore calendar events, AbstractElement events
        if "<" not in entry and entry not in ["mouseup", "mousedown", "click"]:
            entry = entry.replace(":", "_")
            params.append(f"\n      {entry} (event):\n        {description}")

    if len(params):
        params.insert(0, "\n\n    Args:")

    params = "".join(params)

    return f"""
    \"\"\"
    Vuetify's {name} component.
    See more `info and examples <{url}>`_.{params}
    \"\"\"
    """


def expand_parenthetical(attribute, attributes):
    sizes = ["sm", "md", "lg", "xl"]
    numbers = list(range(13)) if "0" in attribute else list(range(1, 13))

    prefix = ""
    if "offset-" in attribute:
        prefix = "offset_"
    if "order-" in attribute:
        prefix = "order_"

    for size in sizes:
        for number in numbers:
            attributes.append(f'"{prefix}{size}{number}",')


def expand_dom_events(event, events):
    dom_events = [
        "click",
        "dblclick",
        "mousedown",
        "mouseenter",
        "mouseleave",
        "mousemove",
        "mouseover",
        "mouseout",
        "mouseup",
        "focus",
    ]
    for dom_event in dom_events:
        events.append(f'("{dom_event}_date", "{dom_event}:date"),')
        events.append(f'("{dom_event}_month", "{dom_event}:month"),')
        events.append(f'("{dom_event}_year", "{dom_event}:year"),')


# ----------------------------------------
# Generator
# ----------------------------------------


def generate_vuetify(input_file, output_file):
    with open(input_file) as vuetify_input:
        loaded = json.loads(vuetify_input.read())
    tags = loaded.get("contributions", {}).get("html", {}).get("tags")

    generated_module = ""
    slots_names = set()
    _all = set()
    _all.add("Template")
    _all.add("dataframe_to_grid")

    # Extract information and generate class definitions
    for tag in tags:
        name = tag.get("name")
        tag_name = tag.get("doc-url").replace("https://www.vuetifyjs.com/api/", "")
        attributes = get_attributes(tag)
        events = get_events(tag)
        docs = get_docs(tag)
        for slot in tag.get("slots", []):
            slots_names.add(slot.get("name"))

        # Add to __all__
        _all.add(name)

        class_def = f"""
class {name}(HtmlElement):{docs}
    def __init__(self, children=None, **kwargs):
        super().__init__("{tag_name}", children, **kwargs)"""

        if name in tts_sensitive_elements:
            class_def += "\n        self.ttsSensitive()"

        if attributes is not None:
            class_def += attributes

        if events is not None:
            class_def += events

        class_def += "\n\n"

        generated_module += class_def

    # Generate slots input
    generated_slot_names = ["slot_names = ["]
    slots_names = list(slots_names)
    slots_names.sort()
    for name in slots_names:
        generated_slot_names.append(f'    "{name}",')
    generated_slot_names.append("]")
    generated_slot_names.append("Template.slot_names.update(slot_names)")
    generated_slot_names.append("")

    # Generate __all__
    generated_all = ["__all__ = ["]
    class_names = list(_all)
    class_names.sort()
    for name in class_names:
        generated_all.append(f'    "{name}",')
    generated_all.append("]")

    with open(output_file, "w") as vuetify_module:
        vuetify_module.write(
            "##########################################################\n"
        )
        vuetify_module.write("# DO NOT EDIT: GENERATED FILE\n")
        vuetify_module.write(
            "# => instead run: $ROOT/vue-components/generate_python.py\n"
        )
        vuetify_module.write(
            "##########################################################\n\n"
        )
        vuetify_module.write(module_header)
        vuetify_module.write("\n\n")
        vuetify_module.write("\n".join(generated_slot_names))
        vuetify_module.write("\n\n")
        vuetify_module.write("\n".join(generated_all))
        vuetify_module.write("\n")
        vuetify_module.write(generated_module)


# ----------------------------------------
# Command line interface
# ----------------------------------------


def init_argparse():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]",
        description="Generate vuetify module for trame",
    )
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output")
    return parser


if __name__ == "__main__":
    if INPUT_JSON.exists():
        try:
            generate_vuetify(INPUT_JSON, DEST_FILE)
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {err.strerror}", file=sys.stderr)
    else:
        print("Need to run the following command first:")
        print(" $ npm i")
