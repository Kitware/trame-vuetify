#!/usr/bin/env python3

import sys
import argparse
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DEST_FILE = BASE_DIR / Path("trame_vuetify/widgets/vuetify3.py")
INPUT_JSON = BASE_DIR / Path("vue3/web-types.json")
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


def to_class_name(name):
    tokens = [word.capitalize() for word in name.split("-")]
    return "".join(tokens)


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


def get_docs(tag):
    url = tag.get("doc-url", "https://vuetifyjs.com/en/introduction/why-vuetify/")
    url = url.replace("www.", "")  # www redirects to start page

    name = tag.get("name")
    attributes = tag.get("attributes", [])
    params = ""
    for attribute in attributes:
        raw_name = attribute.get("name")
        attribute_name = raw_name.replace("-", "_")
        attribute_type = attribute.get("value", {}).get("type", "string")
        description = attribute.get("description")
        if "](" in description:
            # Hide descriptions with markdown
            description = f"See description |{name}_vuetify_link|."
        params += f"""
    :param {attribute_name}: {description}
    :type {attribute_type}:"""

    events = tag.get("events")
    event_params = ""
    for event in events:
        entry = event.get("name")
        description = event.get("description")

        # Ignore calendar events, AbstractElement events
        if "<" not in entry and entry not in ["mouseup", "mousedown", "click"]:
            entry = entry.replace(":", "_").replace("-", "_")
            event_params += f"\n    :param {entry}: {description}"

    if len(event_params):
        event_params = "\n    Events\n" + event_params

    return f"""
    \"\"\"
    Vuetify's {name} component. See more info and examples |{name}_vuetify_link|.

    .. |{name}_vuetify_link| raw:: html

        <a href="{url}" target="_blank">here</a>

    {params}
    {event_params}
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
        class_name = to_class_name(name)
        # tag_name = tag.get("doc-url").replace("https://www.vuetifyjs.com/api/", "")
        attributes = get_attributes(tag)
        events = get_events(tag)
        docs = get_docs(tag)
        for slot in tag.get("slots", []):
            slots_names.add(slot.get("name"))

        # Add to __all__
        _all.add(class_name)

        class_def = f"""
class {class_name}(HtmlElement):{docs}
    def __init__(self, children=None, **kwargs):
        super().__init__("{name}", children, **kwargs)"""

        if class_name in tts_sensitive_elements:
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
