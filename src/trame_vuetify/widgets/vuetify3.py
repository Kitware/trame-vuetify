##########################################################
# DO NOT EDIT: GENERATED FILE
# => instead run: $ROOT/vue-components/generate_python.py
##########################################################

# ruff: noqa: E501

from trame_client.widgets.core import AbstractElement, Template  # noqa

USE_LAB = False


def enable_lab():
    global USE_LAB
    USE_LAB = True


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            if USE_LAB:
                from trame_vuetify.module import vue3_lab

                self.server.enable_module(vue3_lab)
            else:
                from trame_vuetify.module import vue3

                self.server.enable_module(vue3)


try:
    import numpy as np
    from numbers import Number
except Exception:
    # dataframe_to_grid won't work
    pass

type_mapper = {
    "b": ["textColumn"],
    "i": [],  # ["numericColumn", "numberColumnFilter"],
    "u": [],  # ["numericColumn", "numberColumnFilter"],
    "f": [],  # ["numericColumn", "numberColumnFilter"],
    "c": [],
    "m": [],  # ['timedeltaFormat'],
    "M": [],  # ["dateColumnFilter", "shortDateTimeFormat"],
    "O": [],
    "S": [],
    "U": [],
    "V": [],
}

directives = {
    "v-click-outside": {
        "arguments": [],
        "modifiers": [],
    },
    "v-intersect": {
        "arguments": [],
        "modifiers": ["once", "quiet"],
    },
    "v-mutate": {
        "arguments": [],
        "modifiers": ["attr", "char", "child", "immediate", "once", "sub"],
    },
    "v-resize": {
        "arguments": [],
        "modifiers": [],
    },
    "v-ripple": {
        "arguments": [],
        "modifiers": ["center", "circle", "stop"],
    },
    "v-scroll": {
        "arguments": [],
        "modifiers": [],
    },
    "v-tooltip": {
        "arguments": [
            "top",
            "bottom",
            "start",
            "end",
            "left",
            "right",
            "center",
            "center-center",
            "top-start",
            "top-end",
            "top-left",
            "top-right",
            "top-center",
            "bottom-start",
            "bottom-end",
            "bottom-left",
            "bottom-right",
            "bottom-center",
            "start-top",
            "start-bottom",
            "start-center",
            "end-top",
            "end-bottom",
            "end-center",
            "left-top",
            "left-bottom",
            "left-center",
            "right-top",
            "right-bottom",
            "right-center",
        ],
        "modifiers": [],
    },
    "v-touch": {
        "arguments": [],
        "modifiers": [],
    },
}

for directive, description in directives.items():
    py_directive = directive.replace("-", "_")
    AbstractElement.register_directive(py_directive, directive)

    for argument in description["arguments"]:
        py_argument = argument.replace("-", "_")
        AbstractElement.register_directive(
            f"{py_directive}_{py_argument}", f"{directive}:{argument}"
        )

    for modifier in description["modifiers"]:
        py_modifier = modifier.replace("-", "_")
        AbstractElement.register_directive(
            f"{py_directive}_{py_modifier}", f"{directive}.{modifier}"
        )


def cast_to_serializable(value):
    isoformat = getattr(value, "isoformat", None)
    if (isoformat) and callable(isoformat):
        return isoformat()
    elif isinstance(value, Number):
        if np.isnan(value) or np.isinf(value):
            return value.__str__()
        return value

    return value.__str__()


def dataframe_to_grid(dataframe, options={}):
    """
    Transform a dataframe for use with a VDataTable

    Args:
      dataframe:
        A pandas dataframe
      options:
        Control which columns are sortable, filterable, grouped, aligned, etc.
        A dictionary where keys are the columns from the dataframe and values
        are Vuetify DataTableHeader objects. See more info |header_doc_link|.

    Returns:
      The headers and rows for the table component.

    Usage example:

       headers, rows = vuetify.dataframe_to_grid(dataframe)
       VDataTable(headers=("table_headers", headers), items=("table_rows", rows))

    `Vuetify documentation <https://vuetifyjs.com/en/api/v-data-table/#props-headers>`_
    """
    headers = {}
    for col_name in dataframe.columns:
        headers[col_name] = {"text": col_name, "value": col_name}
        if options.get(col_name):
            headers[col_name].update(options.get(col_name))

    return list(headers.values()), dataframe.map(cast_to_serializable).to_dict(
        orient="records"
    )


slot_names = [
    "actions",
    "activator",
    "additional",
    "append",
    "append-inner",
    "append-item",
    "badge",
    "body",
    "body.append",
    "body.prepend",
    "bottom",
    "browse",
    "category",
    "center",
    "chip",
    "clear",
    "close",
    "colgroup",
    "controls",
    "counter",
    "data-table-group",
    "data-table-select",
    "day",
    "day-body",
    "day-header",
    "day-label",
    "day-label-header",
    "day-month",
    "decrement",
    "default",
    "details",
    "divider",
    "empty",
    "error",
    "event",
    "expanded-row",
    "extension",
    "filter",
    "first",
    "footer",
    "footer.prepend",
    "group-header",
    "group-summary",
    "header",
    "header-item",
    "header.data-table-expand",
    "header.data-table-select",
    "headers",
    "headline",
    "icon",
    "image",
    "increment",
    "input",
    "interval",
    "interval-header",
    "item",
    "item-label",
    "item.data-table-expand",
    "item.data-table-select",
    "label",
    "last",
    "legend",
    "legend-text",
    "load-more",
    "loader",
    "loading",
    "media",
    "message",
    "month",
    "next",
    "no-data",
    "opposite",
    "placeholder",
    "prepend",
    "prepend-inner",
    "prepend-item",
    "prev",
    "pullDownPanel",
    "selection",
    "sources",
    "subheader",
    "subtitle",
    "tab",
    "tbody",
    "text",
    "tfoot",
    "thead",
    "thumb",
    "thumb-label",
    "tick-label",
    "title",
    "toggle",
    "tooltip",
    "top",
    "track-false",
    "track-true",
    "window",
    "wrapper",
    "year",
]
Template.slot_names.update(slot_names)


__all__ = [
    "Template",
    "VAlert",
    "VAlertTitle",
    "VApp",
    "VAppBar",
    "VAppBarNavIcon",
    "VAppBarTitle",
    "VAutocomplete",
    "VAvatar",
    "VBadge",
    "VBanner",
    "VBannerActions",
    "VBannerText",
    "VBottomNavigation",
    "VBottomSheet",
    "VBreadcrumbs",
    "VBreadcrumbsDivider",
    "VBreadcrumbsItem",
    "VBtn",
    "VBtnGroup",
    "VBtnToggle",
    "VCalendar",
    "VCard",
    "VCardActions",
    "VCardItem",
    "VCardSubtitle",
    "VCardText",
    "VCardTitle",
    "VCarousel",
    "VCarouselItem",
    "VCheckbox",
    "VCheckboxBtn",
    "VChip",
    "VChipGroup",
    "VClassIcon",
    "VCode",
    "VCol",
    "VColorInput",
    "VColorPicker",
    "VCombobox",
    "VComponentIcon",
    "VConfirmEdit",
    "VContainer",
    "VCounter",
    "VDataIterator",
    "VDataTable",
    "VDataTableFooter",
    "VDataTableHeaders",
    "VDataTableRow",
    "VDataTableRows",
    "VDataTableServer",
    "VDataTableVirtual",
    "VDateInput",
    "VDatePicker",
    "VDatePickerControls",
    "VDatePickerHeader",
    "VDatePickerMonth",
    "VDatePickerMonths",
    "VDatePickerYears",
    "VDefaultsProvider",
    "VDialog",
    "VDialogBottomTransition",
    "VDialogTopTransition",
    "VDialogTransition",
    "VDivider",
    "VEmptyState",
    "VExpandTransition",
    "VExpandXTransition",
    "VExpansionPanel",
    "VExpansionPanelText",
    "VExpansionPanelTitle",
    "VExpansionPanels",
    "VFab",
    "VFabTransition",
    "VFadeTransition",
    "VField",
    "VFieldLabel",
    "VFileInput",
    "VFileUpload",
    "VFileUploadItem",
    "VFooter",
    "VForm",
    "VHotkey",
    "VHover",
    "VIcon",
    "VIconBtn",
    "VImg",
    "VInfiniteScroll",
    "VInput",
    "VItem",
    "VItemGroup",
    "VKbd",
    "VLabel",
    "VLayout",
    "VLayoutItem",
    "VLazy",
    "VLigatureIcon",
    "VList",
    "VListGroup",
    "VListImg",
    "VListItem",
    "VListItemAction",
    "VListItemMedia",
    "VListItemSubtitle",
    "VListItemTitle",
    "VListSubheader",
    "VLocaleProvider",
    "VMain",
    "VMaskInput",
    "VMenu",
    "VMessages",
    "VNavigationDrawer",
    "VNoSsr",
    "VNumberInput",
    "VOtpInput",
    "VOverlay",
    "VPagination",
    "VParallax",
    "VPicker",
    "VPickerTitle",
    "VPie",
    "VPieSegment",
    "VPieTooltip",
    "VProgressCircular",
    "VProgressLinear",
    "VPullToRefresh",
    "VRadio",
    "VRadioGroup",
    "VRangeSlider",
    "VRating",
    "VResponsive",
    "VRow",
    "VScaleTransition",
    "VScrollXReverseTransition",
    "VScrollXTransition",
    "VScrollYReverseTransition",
    "VScrollYTransition",
    "VSelect",
    "VSelectionControl",
    "VSelectionControlGroup",
    "VSheet",
    "VSkeletonLoader",
    "VSlideGroup",
    "VSlideGroupItem",
    "VSlideXReverseTransition",
    "VSlideXTransition",
    "VSlideYReverseTransition",
    "VSlideYTransition",
    "VSlider",
    "VSnackbar",
    "VSnackbarQueue",
    "VSpacer",
    "VSparkline",
    "VSpeedDial",
    "VStepper",
    "VStepperActions",
    "VStepperHeader",
    "VStepperItem",
    "VStepperVertical",
    "VStepperVerticalActions",
    "VStepperVerticalItem",
    "VStepperWindow",
    "VStepperWindowItem",
    "VSvgIcon",
    "VSwitch",
    "VSystemBar",
    "VTab",
    "VTable",
    "VTabs",
    "VTabsWindow",
    "VTabsWindowItem",
    "VTextField",
    "VTextarea",
    "VThemeProvider",
    "VTimePicker",
    "VTimePickerClock",
    "VTimePickerControls",
    "VTimeline",
    "VTimelineItem",
    "VToolbar",
    "VToolbarItems",
    "VToolbarTitle",
    "VTooltip",
    "VTreeview",
    "VTreeviewGroup",
    "VTreeviewItem",
    "VValidation",
    "VVideo",
    "VVideoControls",
    "VVideoVolume",
    "VVirtualScroll",
    "VWindow",
    "VWindowItem",
    "dataframe_to_grid",
    "enable_lab",
]


class VAlert(HtmlElement):
    """
    Vuetify's VAlert component.
    See more `info and examples <https://vuetifyjs.com/api/v-alert>`_.

    Args:
      title (string):
        Specify a title text for the component.
      text (string):
        Specify content text for the component.
      border (boolean, 'top', 'end', 'bottom', 'start'):
        Adds a colored border to the component.
      border_color (string):
        Specifies the color of the border. Only used in combination with
        **border** prop. Accepts any color value.
      closable (boolean):
        Adds a close icon that can hide the alert.
      close_icon (enum):
        Change the default icon used for **closable** alerts.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      type ('success', 'info', 'warning', 'error'):
        Create a specialized alert that uses a contextual color and has
        a pre-defined icon.
      close_label (string):
        Text used for *aria-label* on **closable** alerts. Can also be
        customized globally in [Internationalization](/customization/internationalization).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          false, string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      model_value (boolean):
        Controls whether the component is visible or hidden.
      prominent (boolean):
        Displays a larger vertically centered icon to draw more attention.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      icon_sizes (enum):
        An array of tuples that define the icon sizes for each named size.

        Enum values: [
          ['default', 'small', 'x-small', 'large', 'x-large', number][]
        ]
      icon_size (string, number):
        The specific size of the icon, can use named sizes.
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'static', 'relative', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes the component's border-radius.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      click_close (event):
        Emitted when close icon is clicked.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAlert", children, **kwargs)
        self._attr_names += [
            "title",
            "text",
            "border",
            ("border_color", "borderColor"),
            "closable",
            ("close_icon", "closeIcon"),
            "type",
            ("close_label", "closeLabel"),
            "icon",
            ("model_value", "modelValue"),
            "prominent",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            ("icon_sizes", "iconSizes"),
            ("icon_size", "iconSize"),
            "location",
            "position",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
        ]
        self._event_names += [
            ("click_close", "click:close"),
            ("update_modelValue", "update:modelValue"),
        ]


class VAlertTitle(HtmlElement):
    """
    Vuetify's VAlertTitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-alert-title>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAlertTitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VApp(HtmlElement):
    """
    Vuetify's VApp component.
    See more `info and examples <https://vuetifyjs.com/api/v-app>`_.

    Args:
      overlaps (string[]):
        **FOR INTERNAL USE ONLY**
      theme (string):
        Specify a theme for this component and all of its children.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VApp", children, **kwargs)
        self._attr_names += [
            "overlaps",
            "theme",
        ]
        self._event_names += []


class VAppBar(HtmlElement):
    """
    Vuetify's VAppBar component.
    See more `info and examples <https://vuetifyjs.com/api/v-app-bar>`_.

    Args:
      title (string):
        Specify a title text for the component.
      flat (boolean):
        Removes the component's **box-shadow**.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      density ('default', 'prominent', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Designates a specific height for the toolbar. Overrides the heights
        imposed by other props, e.g. **prominent**, **dense**, **extended**,
        etc.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location ('top', 'bottom'):
        Aligns the component towards the top or bottom.
      absolute (boolean):
        Applies position: absolute to the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      name (string):
        Assign a specific name for layout registration.
      image (string):
        Specifies a [v-img](/components/images) as the component's background.
      collapse (boolean):
        Morphs the component into a collapsed state, reducing its maximum width.
      collapse_position ('end', 'start'):
        Specifies side to attach the collapsed toolbar.
      extended (boolean):
        Use this prop to increase the height of the toolbar _without_
        using the `extension` slot for adding content. May be used in
        conjunction with the **extension-height** prop. When false, will
        not show extension slot even if content is present.
      extension_height (string, number):
        Designate an explicit height for the `extension` slot.
      floating (boolean):
        Applies **display: inline-flex** to the component.
      order (string, number):
        Adjust the order of the component in relation to its registration order.
      scroll_target (string):
        The element to target for scrolling events. Uses `window` by default.
      scroll_threshold (string, number):
        The amount of scroll distance down before **scroll-behavior** activates.
      scroll_behavior (enum):
        Specify an action to take when the scroll position of **scroll-target**
        reaches **scroll-threshold**. Accepts any combination of hide,
        inverted, collapse, elevate, and fade-image. Multiple values
        can be used, separated by a space.

        Enum values: [
          (string & {}), 'hide', 'fully-hide', 'inverted', 'collapse',
          'elevate', 'fade-image'
        ]
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAppBar", children, **kwargs)
        self._attr_names += [
            "title",
            "flat",
            "border",
            ("model_value", "modelValue"),
            "density",
            "height",
            "elevation",
            "location",
            "absolute",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "name",
            "image",
            "collapse",
            ("collapse_position", "collapsePosition"),
            "extended",
            ("extension_height", "extensionHeight"),
            "floating",
            "order",
            ("scroll_target", "scrollTarget"),
            ("scroll_threshold", "scrollThreshold"),
            ("scroll_behavior", "scrollBehavior"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VAppBarNavIcon(HtmlElement):
    """
    Vuetify's VAppBarNavIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-app-bar-nav-icon>`_.

    Args:
      symbol (any):
        The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
        used to hook into group functionality for components like [v-btn-toggle](/components/btn-toggle)
        and [v-bottom-navigation](/components/bottom-navigations/).
      flat (boolean):
        Removes the button box shadow. This is different than using the 'flat' variant.
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      active_color (string):
        The applied color when the component is in an active state.
      base_color (string):
        Sets the color of component when not focused.
      prepend_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend**
        slot before default content.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      block (boolean):
        Expands the button to 100% of available space.
      readonly (boolean):
        Puts the button in a readonly state. Cannot be clicked or navigated
        to by keyboard.
      slim (boolean):
        Reduces padding to 0 8px.
      stacked (boolean):
        Displays the button as a flex-column.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      text (string, number, boolean):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/)
        component. The button will become _round_.

        Enum values: [
          boolean, string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAppBarNavIcon", children, **kwargs)
        self._attr_names += [
            "symbol",
            "flat",
            "replace",
            "tag",
            "disabled",
            "height",
            "size",
            "value",
            "width",
            "theme",
            "active",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "block",
            "readonly",
            "slim",
            "stacked",
            "ripple",
            "text",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            ("selected_class", "selectedClass"),
            "loading",
            "location",
            "position",
            "rounded",
            "tile",
            "href",
            "exact",
            "to",
            "color",
            "variant",
            "icon",
        ]
        self._event_names += []


class VAppBarTitle(HtmlElement):
    """
    Vuetify's VAppBarTitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-app-bar-title>`_.

    Args:
      text (string):
        Specify content text for the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAppBarTitle", children, **kwargs)
        self._attr_names += [
            "text",
            "tag",
        ]
        self._event_names += []


class VAutocomplete(HtmlElement):
    """
    Vuetify's VAutocomplete component.
    See more `info and examples <https://vuetifyjs.com/api/v-autocomplete>`_.

    Args:
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      search (string):
        Text input used to filter items.
      type (string):
        Sets input type.
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      reverse (boolean):
        Reverses the orientation.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      rounded (string, number, boolean):
        Adds a border radius to the input.
      tile (boolean):
        Removes any applied **border-radius** from the component.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      name (string):
        Sets the component's name attribute.
      autocomplete (string):
        Helps influence browser's suggestions. Special value **suppress**
        manipulates fields `name` attribute while **off** relies on browser's
        good will to stop suggesting values. Any other value is passed
        to the native `autocomplete` on the underlying element.
      disabled (boolean):
        Removes the ability to click or target the input.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      placeholder (string):
        Sets the input’s placeholder text.
      id (string):
        Sets the DOM id on the component.
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      autofocus (boolean):
        Enables autofocus.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      auto_select_first (boolean, 'exact'):
        When searching, will always highlight the first option and select
        it on blur. `exact` will only highlight and select exact matches.
      clear_on_select (boolean):
        Reset the search text when a selection is made while using the
        **multiple** prop.
      filter_mode ('every', 'some', 'union', 'intersection'):
        Controls how the results of `customFilter` and `customKeyFilter`
        are combined. All modes only apply `customFilter` to columns
        not specified in `customKeyFilter`.  - **some**: There is at
        least one match from either the custom filter or the custom key
        filter. - **every**: All columns match either the custom filter
        or the custom key filter. - **union**: There is at least one
        match from the custom filter, or all columns match the custom
        key filters. - **intersection**: There is at least one match
        from the custom filter, and all columns match the custom key
        filters.
      no_filter (boolean):
        Do not apply filtering when searching. Useful when data is being
        filtered server side.
      custom_filter (FilterFunction):
        Function used to filter items, called for each filterable key
        on each item in the list. The first argument is the filterable
        value from the item, the second is the search term, and the third
        is the internal item object. The function should return true
        if the item should be included in the filtered list, or the index
        of the match in the value if it should be included with the result
        highlighted.
      custom_key_filter (unknown):
        Function used on specific keys within the item object. `customFilter`
        is skipped for columns with `customKeyFilter` specified.
      filter_keys (string, string[]):
        Array of specific keys to filter on the item.
      chips (boolean):
        Changes display of selections to chips.
      closable_chips (boolean):
        Enables the [closable](/api/v-chip/#props-closable) prop on all
        [v-chip](/components/chips/) components.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      hide_selected (boolean):
        Do not display in the select menu items that are already selected.
      list_props (unknown):
        Pass props through to the `v-list` component. Accepts an object
        with anything from [v-list](/api/v-list/#props) props, camelCase
        keys are recommended.
      base_color (string):
        Sets the color of the input when it is not focused.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      items (any[]):
        Can be an array of objects or strings. By default objects should
        have **title** and **value** properties, and can optionally have
        a **props** property containing any [VListItem props](/api/v-list-item/#props).
        Keys to use for these can be changed with the **item-title**,
        **item-value**, and **item-props** props.
      item_title (SelectItemKey):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      item_children (SelectItemKey):
        This property currently has **no effect**.
      item_props (SelectItemKey):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      item_type (SelectItemKey):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/list-items.json))
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3888: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      menu (boolean):
        Renders with the menu open by default.
      menu_icon (enum):
        Sets the the spin icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      menu_props (unknown):
        Pass props through to the `v-menu` component. Accepts an object
        with anything from [v-menu](/api/v-menu/#props) props, camelCase
        keys are recommended.
      no_data_text (string):
        Text shown when no items are provided to the component.
      open_on_clear (boolean):
        Open's the menu whenever the clear icon is clicked.
      item_color (string):
        Sets color of selected items.
      no_auto_scroll (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/Select.json))
      close_text (string):
        Text set to the inputs `aria-label` and `title` when input menu is closed.
      open_text (string):
        Text set to the inputs **aria-label** and **title** when input menu is open.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outside the component's input, uses the
        same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      readonly (boolean):
        Puts input in readonly state.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      counter_value (number, js_fn):
        Function returns the counter display text.
      model_modifiers (unknown):
        **FOR INTERNAL USE ONLY**
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
      update_search (event):
        Event emitted when the search value changes.
      update_menu (event):
        Event that is emitted when the component's menu state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAutocomplete", children, **kwargs)
        self._attr_names += [
            "flat",
            "search",
            "type",
            ("model_value", "modelValue"),
            "error",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            "name",
            "autocomplete",
            "disabled",
            "multiple",
            "placeholder",
            "id",
            "prefix",
            "role",
            "autofocus",
            "label",
            ("auto_select_first", "autoSelectFirst"),
            ("clear_on_select", "clearOnSelect"),
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            "chips",
            ("closable_chips", "closableChips"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            ("list_props", "listProps"),
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("item_type", "itemType"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("item_color", "itemColor"),
            ("no_auto_scroll", "noAutoScroll"),
            ("close_text", "closeText"),
            ("open_text", "openText"),
            "counter",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "readonly",
            "rules",
            ("validate_on", "validateOn"),
            "focused",
            ("hide_details", "hideDetails"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "loading",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_search", "update:search"),
            ("update_menu", "update:menu"),
        ]


class VAvatar(HtmlElement):
    """
    Vuetify's VAvatar component.
    See more `info and examples <https://vuetifyjs.com/api/v-avatar>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      theme (string):
        Specify a theme for this component and all of its children.
      start (boolean):
        Applies margin at the end of the component.
      end (boolean):
        Applies margin at the start of the component.
      text (string):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      image (string):
        Apply a specific image using [v-img](/components/images/).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAvatar", children, **kwargs)
        self._attr_names += [
            "tag",
            "size",
            "theme",
            "start",
            "end",
            "text",
            "border",
            "density",
            "rounded",
            "tile",
            "color",
            "variant",
            "icon",
            "image",
        ]
        self._event_names += []


class VBadge(HtmlElement):
    """
    Vuetify's VBadge component.
    See more `info and examples <https://vuetifyjs.com/api/v-badge>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      label (string):
        The **aria-label** used for the badge.
      height (string, number):
        Sets the height for the component.
      max (string, number):
        Sets the maximum number allowed when using the **content** prop
        with a `number` like value. If the content number exceeds the
        maximum value, a `+` suffix is added.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      bordered (boolean):
        Applies a **2px** by default and **1.5px** border around the
        badge when using the **dot** property.
      content (string, number):
        Text content to show in the badge.
      dot (boolean):
        Reduce the size of the badge and hide its contents.
      floating (boolean):
        Move the badge further away from the slotted content. Equivalent
        to an 8px offset.
      inline (boolean):
        Display as an inline block instead of absolute position. **location**,
        **floating**, and **offset** will have no effect.
      model_value (boolean):
        Controls whether the component is visible or hidden.
      offset_x (string, number):
        Offset the badge on the x-axis.
      offset_y (string, number):
        Offset the badge on the y-axis.
      text_color (string):
        Applies a specified color to the control text - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBadge", children, **kwargs)
        self._attr_names += [
            "tag",
            "label",
            "height",
            "max",
            "width",
            "theme",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "location",
            "rounded",
            "tile",
            "color",
            "icon",
            "bordered",
            "content",
            "dot",
            "floating",
            "inline",
            ("model_value", "modelValue"),
            ("offset_x", "offsetX"),
            ("offset_y", "offsetY"),
            ("text_color", "textColor"),
            "transition",
        ]
        self._event_names += []


class VBanner(HtmlElement):
    """
    Vuetify's VBanner component.
    See more `info and examples <https://vuetifyjs.com/api/v-banner>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      stacked (boolean):
        Forces the banner actions onto a new line. This is not applicable
        when the banner has `lines="one"`.
      text (string):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      sticky (boolean):
        Applies `position: sticky` to the component with `top: 0`. You
        can find more information on the [MDN documentation for sticky
        position](https://developer.mozilla.org/en-US/docs/Web/CSS/position).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      avatar (string):
        Designates a specific src image to pass to the thumbnail.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      mobile (boolean):
        Applies the mobile banner styles.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      lines ('one', 'two', 'three'):
        The amount of visible lines of text before it truncates.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBanner", children, **kwargs)
        self._attr_names += [
            "tag",
            "height",
            "width",
            "theme",
            "stacked",
            "text",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "location",
            "position",
            "sticky",
            "rounded",
            "tile",
            "color",
            "icon",
            "avatar",
            ("bg_color", "bgColor"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "lines",
        ]
        self._event_names += []


class VBannerActions(HtmlElement):
    """
    Vuetify's VBannerActions component.
    See more `info and examples <https://vuetifyjs.com/api/v-banner-actions>`_.

    Args:
      density (string):
        Adjusts the vertical height used by the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBannerActions", children, **kwargs)
        self._attr_names += [
            "density",
            "color",
        ]
        self._event_names += []


class VBannerText(HtmlElement):
    """
    Vuetify's VBannerText component.
    See more `info and examples <https://vuetifyjs.com/api/v-banner-text>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBannerText", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VBottomNavigation(HtmlElement):
    """
    Vuetify's VBottomNavigation component.
    See more `info and examples <https://vuetifyjs.com/api/v-bottom-navigation>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      name (string):
        Assign a specific name for layout registration.
      mode (string):
        Changes the orientation and active state styling of the component.
      disabled (boolean):
        Puts all children components into a disabled state.
      height (string, number):
        Sets the height for the component.
      max (number):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allows one to select multiple items.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      base_color (string):
        Sets the color of component when not focused.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      absolute (boolean):
        Applies **position: absolute** to the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      grow (boolean):
        Force all [v-btn](/components/buttons) children to take up all
        available horizontal space.
      order (string, number):
        Adjust the order of the component in relation to its registration order.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_active (event):
        Event that is emitted when the active state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBottomNavigation", children, **kwargs)
        self._attr_names += [
            "tag",
            "name",
            "mode",
            "disabled",
            "height",
            "max",
            "multiple",
            "theme",
            "active",
            ("base_color", "baseColor"),
            "border",
            "density",
            "elevation",
            ("selected_class", "selectedClass"),
            "absolute",
            "rounded",
            "tile",
            "color",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "grow",
            "order",
            "mandatory",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_active", "update:active"),
        ]


class VBottomSheet(HtmlElement):
    """
    Vuetify's VBottomSheet component.
    See more `info and examples <https://vuetifyjs.com/api/v-bottom-sheet>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      location (Anchor):
        Specifies the anchor point for positioning the component, using
        directional cues to align it either horizontally, vertically,
        or both..
      absolute (boolean):
        Applies **position: absolute** to the content element.
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          {      component: ComponentPublicInstanceConstructor<
          CreateComponentPublicInstanceWithMixins<          {} & { target?:
          HTMLElement, [x: number, y: number], undefined } & {
             $children?:, VNodeChild, { $stable?: boolean, undefined },
          js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn, [x: number, y: number], undefined } & {
                     $children?:, VNodeChild, { $stable?: boolean, undefined
          }, js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn, [x: number, y: number], undefined } & {
                     $children?:, VNodeChild, { $stable?: boolean, undefined
          }, js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn
        ]
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      inset (boolean):
        Reduces the sheet content maximum width to 70%.
      fullscreen (boolean):
        Changes layout for fullscreen display.
      scrollable (boolean):
        When set to true, expects a `v-card` and a `v-card-text` component
        with a designated height. For more information, check out the
        [scrollable example](/components/dialogs#scrollable).
      close_on_back (boolean):
        Closes the overlay content when the browser's back button is
        pressed or `$router.back()` is called, cancelling the original
        navigation. `persistent` overlays will cancel navigation and
        animate as if they were clicked outside instead of closing.
      contained (boolean):
        Limits the size of the component and scrim to its offset parent.
        Implies `absolute` and `attach`. (Note: The parent element must
        have position: relative.).
      content_class (any):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      content_props (any):
        Apply custom properties to the content.
      opacity (string, number):
        Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
      no_click_animation (boolean):
        Disables the bounce effect when clicking outside of the content
        element when using the persistent prop.
      persistent (boolean):
        Clicking outside of the element or pressing esc key will not deactivate it.
      scrim (string, boolean):
        Accepts true/false to enable background, and string to define color.
      z_index (string, number):
        The z-index used for the component.
      target (enum):
        For locationStrategy="connected", specify an element or array
        of x,y coordinates that the overlay should position itself relative
        to. This will be the activator element by default.

        Enum values: [
          Element, (string & {}), 'parent', 'cursor', ComponentPublicInstance,
          [number, number]
        ]
      activator_props (unknown):
        Apply custom properties to the activator.
      open_on_click (boolean):
        Activate the component when the activator is clicked.
      open_on_hover (boolean):
        Activate the component when the activator is hovered.
      open_on_focus (boolean):
        Activate the component when the activator is focused.
      close_on_content_click (boolean):
        Closes component when you click on its content.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        Increases distance from the target. When passed as a pair of
        numbers, the second value shifts anchor along the side and away
        from the target.
      stick_to_target (boolean):
        Enables the overlay content to go off-screen when scrolling.
      viewport_margin (string, number):
        Sets custom viewport margin for the overlay content
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
      retain_focus (boolean):
        Captures and keeps focus within the content element when using
        **Tab** and **Shift**+**Tab**. Recommended to be `false` when
        using external tools that require focus such as TinyMCE or vue-clipboard.
      capture_focus (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/focusTrap.json))
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBottomSheet", children, **kwargs)
        self._attr_names += [
            "disabled",
            "height",
            "width",
            "theme",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "location",
            "absolute",
            ("model_value", "modelValue"),
            "transition",
            "activator",
            "inset",
            "fullscreen",
            "scrollable",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            "persistent",
            "scrim",
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "eager",
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            ("stick_to_target", "stickToTarget"),
            ("viewport_margin", "viewportMargin"),
            ("scroll_strategy", "scrollStrategy"),
            ("retain_focus", "retainFocus"),
            ("capture_focus", "captureFocus"),
            "attach",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VBreadcrumbs(HtmlElement):
    """
    Vuetify's VBreadcrumbs component.
    See more `info and examples <https://vuetifyjs.com/api/v-breadcrumbs>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Removes the ability to click or target the component.
      items (enum):
        An array of strings or objects used for automatically generating
        children components.

        Enum values: [
          (, string, (Partial<LinkProps> & { title: string; disabled: boolean }))[]
        ]
      active_color (string):
        The applied color when the component is in an active state.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      divider (string):
        Specifies the dividing character between items.
      active_class (string):
        The class applied to the component when it is in an active state.
      item_props (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VBreadcrumbs.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBreadcrumbs", children, **kwargs)
        self._attr_names += [
            "tag",
            "disabled",
            "items",
            ("active_color", "activeColor"),
            "density",
            "rounded",
            "tile",
            "color",
            "icon",
            ("bg_color", "bgColor"),
            "divider",
            ("active_class", "activeClass"),
            ("item_props", "itemProps"),
        ]
        self._event_names += []


class VBreadcrumbsDivider(HtmlElement):
    """
    Vuetify's VBreadcrumbsDivider component.
    See more `info and examples <https://vuetifyjs.com/api/v-breadcrumbs-divider>`_.

    Args:
      divider (string, number):
        Specifies the dividing character between items.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBreadcrumbsDivider", children, **kwargs)
        self._attr_names += [
            "divider",
        ]
        self._event_names += []


class VBreadcrumbsItem(HtmlElement):
    """
    Vuetify's VBreadcrumbsItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-breadcrumbs-item>`_.

    Args:
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      title (string):
        Specify a title text for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      width (string, number):
        Sets the width for the component.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      active_color (string):
        The applied color when the component is in an active state.
      max_width (string, number):
        Sets the maximum width for the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      active_class (string):
        The class applied to the component when it matches the current
        route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class)
        on the [vue-router](https://router.vuejs.org/) documentation.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBreadcrumbsItem", children, **kwargs)
        self._attr_names += [
            "replace",
            "tag",
            "title",
            "disabled",
            "width",
            "active",
            ("active_color", "activeColor"),
            ("max_width", "maxWidth"),
            "href",
            "exact",
            "to",
            "color",
            ("active_class", "activeClass"),
        ]
        self._event_names += []


class VBtn(HtmlElement):
    """
    Vuetify's VBtn component.
    See more `info and examples <https://vuetifyjs.com/api/v-btn>`_.

    Args:
      symbol (any):
        The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
        used to hook into group functionality for components like [v-btn-toggle](/components/btn-toggle)
        and [v-bottom-navigation](/components/bottom-navigations/).
      flat (boolean):
        Removes the button box shadow. This is different than using the 'flat' variant.
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      active_color (string):
        The applied color when the component is in an active state.
      base_color (string):
        Sets the color of component when not focused.
      prepend_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend**
        slot before default content.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      block (boolean):
        Expands the button to 100% of available space.
      readonly (boolean):
        Puts the button in a readonly state. Cannot be clicked or navigated
        to by keyboard.
      slim (boolean):
        Reduces padding to 0 8px.
      stacked (boolean):
        Displays the button as a flex-column.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      text (string, number, boolean):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/)
        component. The button will become _round_.

        Enum values: [
          boolean, string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      spaced ('start', 'end', 'both'):
        Extends content to the edges to move main content from prepend and append slots.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtn", children, **kwargs)
        self._attr_names += [
            "symbol",
            "flat",
            "replace",
            "tag",
            "disabled",
            "height",
            "size",
            "value",
            "width",
            "theme",
            "active",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "block",
            "readonly",
            "slim",
            "stacked",
            "ripple",
            "text",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            ("selected_class", "selectedClass"),
            "loading",
            "location",
            "position",
            "rounded",
            "tile",
            "href",
            "exact",
            "to",
            "color",
            "variant",
            "icon",
            "spaced",
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VBtnGroup(HtmlElement):
    """
    Vuetify's VBtnGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-btn-group>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of component when not focused.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      divided (boolean):
        Add dividers between children [v-btn](/components/buttons) components.
      direction ('horizontal', 'vertical'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VBtnGroup.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtnGroup", children, **kwargs)
        self._attr_names += [
            "tag",
            "theme",
            ("base_color", "baseColor"),
            "border",
            "density",
            "elevation",
            "rounded",
            "tile",
            "color",
            "variant",
            "divided",
            "direction",
        ]
        self._event_names += []


class VBtnToggle(HtmlElement):
    """
    Vuetify's VBtnToggle component.
    See more `info and examples <https://vuetifyjs.com/api/v-btn-toggle>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Puts all children components into a disabled state.
      max (number):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allows one to select multiple items.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of component when not focused.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      rounded (string, number, boolean):
        Round edge buttons.
      tile (boolean):
        Removes the component's border-radius.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      divided (boolean):
        Add dividers between children [v-btn](/components/buttons) components.
      direction ('horizontal', 'vertical'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VBtnGroup.json))
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtnToggle", children, **kwargs)
        self._attr_names += [
            "tag",
            "disabled",
            "max",
            "multiple",
            "theme",
            ("base_color", "baseColor"),
            "border",
            "density",
            "elevation",
            ("selected_class", "selectedClass"),
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            "mandatory",
            "divided",
            "direction",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VCalendar(HtmlElement):
    """
    Vuetify's VCalendar component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar>`_.

    Args:
      type (enum):
        A string which is one of `month`, `week`, `day`, `4day`, `custom-weekly`,
        `custom-daily`, and `category`. The custom types look at the
        `start` and `end` dates passed to the component as opposed to
        the `value`.

        Enum values: [
          'category', 'day', 'month', 'week', '4day', 'custom-weekly', 'custom-daily'
        ]
      start (string, number, Date):
        The starting date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      end (string, number, Date):
        The ending date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      model_value (string, number, Date):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      category_days (string, number):
        The number of days to render in the `category` view.
      categories (enum):
        Specifies what categories to display in the `category` view.
        This controls the order of the categories as well. If the calendar
        uses events any categories specified in those events not specified
        in this value are dynamically rendered in the view unless `category-hide-dynamic`
        is true.

        Enum values: [
          string, (string, { name: string; categoryName: string; [string]: any })[]
        ]
      category_text (string, ((      category: string, js_fn):
        If categories is a list of objects, you can use this to determine
        what property to print out as the category text on the calendar.
        You can provide a function to do some logic or just define the
        prop name. It's similar to item-text on v-select
      max_days (number):
        The maximum number of days to display in the custom calendar
        if an `end` day is not set.
      category_hide_dynamic (boolean):
        Sets whether categories specified in an event should be hidden
        if it's not defined in `categories`.
      category_show_all (boolean):
        Set whether the `category` view should show all defined `categories`
        even if there are no events for a category.
      category_for_invalid (string):
        The category to place events in that have invalid categories.
        A category is invalid when it is not a string. By default events
        without a category are not displayed until this value is specified.
      weekdays (string, number[]):
        Specifies which days of the week to display. To display Monday
        through Friday only, a value of `[1, 2, 3, 4, 5]` can be used.
        To display a week starting on Monday a value of `[1, 2, 3, 4,
        5, 6, 0]` can be used.
      first_day_of_week (string, number):
        Sets the first day of the week, starting with 0 for Sunday. (Note:
        not guaranteed to work when using custom date adapters.)
      first_day_of_year (string, number):
        Sets the day that determines the first week of the year, starting
        with 0 for Sunday. For ISO 8601 this should be 4. (Note: not
        guaranteed to work when using custom date adapters.)
      weekday_format (CalendarTimestamp):
        Formats day of the week string that appears in the header to specified locale
      day_format (CalendarTimestamp):
        Formats day of the month string that appears in a day to a specified locale
      locale (string):
        The locale of the calendar.
      now (string):
        Override the day & time which is considered now. This is in the
        format of `YYYY-MM-DD hh:mm:ss`. The calendar is styled according
        to now.
      events ({ [string]: any }[]):
        An array of event objects with a property for a start timestamp
        and optionally a name and end timestamp. If an end timestamp
        is not given, the value of start will be used. If no name is
        given, you must provide an implementation for the `event` slot.
      event_start (string):
        Set property of *event*'s start timestamp.
      event_end (string):
        Set property of *event*'s end timestamp.
      event_timed (string, js_fn):
        If Dates or milliseconds are used as the start or end timestamp
        of an event, this prop can be a string to a property on the event
        that is truthy if the event is a timed event or a function which
        takes the event and returns a truthy value if the event is a
        timed event.
      event_category (string, js_fn):
        Set property of *event*'s category. Instead of a property a function
        can be given which takes an event and returns the category.
      event_height (number):
        The height of an event in pixels in the `month` view and at the
        top of the `day` views.
      event_color (string, js_fn):
        A background color for all events or a function which accepts
        an event object passed to the calendar to return a color.
      event_text_color (string, js_fn):
        A text color for all events or a function which accepts an event
        object passed to the calendar to return a color.
      event_name (CalendarEventParsed):
        Set property of *event*'s displayed name, or a function which
        accepts an event object passed to the calendar as the first argument
        and a flag signalling whether the name is for a timed event (true)
        or an event over a day.
      event_overlap_threshold (string, number):
        A value in minutes that's used to determine whether two timed
        events should be placed in column beside each other or should
        be treated as slightly overlapping events.
      event_overlap_mode (CalendarEventParsed):
        One of `stack`, `column`, or a custom render function
      event_more (boolean):
        Whether the more 'button' is displayed on a calendar with too
        many events in a given day. It will say something like '5 more'
        and when clicked generates a `click:more` event.
      event_more_text (string):
        The text to display in the more 'button' given the number of hidden events.
      event_ripple (boolean, Record<string, any>):
        Applies the `v-ripple` directive.
      event_margin_bottom (number):
        Margin bottom for event
      [`${string}_date`] (event):
        Any event on the day of the month link. The second argument is
        the day & time object.
      [`${string}_dayCategory`] (event):
        Any event on a day in the `category` view. The second argument
        is the day object.
      [`${string}_day`] (event):
        Any event on a day. The second argument is the day object.
      [`${string}_event`] (event):
        Any event on a specific event. The second argument is the day & time object.
      [`${string}_interval`] (event):
        Any event at a specific interval label in the `day` view. The
        second argument is the day & time object.
      [`${string}_more`] (event):
        Any event on the `X more` button on views with too many events
        in a day. The second argument is the day & time object.
      [`${string}_timeCategory`] (event):
        Any event at a specific time in the `category` view. The second
        argument is the day & time object.
      [`${string}_time`] (event):
        Any event at a specific time in the `day` view. The second argument
        is the day & time object.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendar", children, **kwargs)
        self._attr_names += [
            "type",
            "start",
            "end",
            ("model_value", "modelValue"),
            ("category_days", "categoryDays"),
            "categories",
            ("category_text", "categoryText"),
            ("max_days", "maxDays"),
            ("category_hide_dynamic", "categoryHideDynamic"),
            ("category_show_all", "categoryShowAll"),
            ("category_for_invalid", "categoryForInvalid"),
            "weekdays",
            ("first_day_of_week", "firstDayOfWeek"),
            ("first_day_of_year", "firstDayOfYear"),
            ("weekday_format", "weekdayFormat"),
            ("day_format", "dayFormat"),
            "locale",
            "now",
            "events",
            ("event_start", "eventStart"),
            ("event_end", "eventEnd"),
            ("event_timed", "eventTimed"),
            ("event_category", "eventCategory"),
            ("event_height", "eventHeight"),
            ("event_color", "eventColor"),
            ("event_text_color", "eventTextColor"),
            ("event_name", "eventName"),
            ("event_overlap_threshold", "eventOverlapThreshold"),
            ("event_overlap_mode", "eventOverlapMode"),
            ("event_more", "eventMore"),
            ("event_more_text", "eventMoreText"),
            ("event_ripple", "eventRipple"),
            ("event_margin_bottom", "eventMarginBottom"),
        ]
        self._event_names += [
            ("[`${string}_date`]", "[`${string}:date`]"),
            ("[`${string}_dayCategory`]", "[`${string}:dayCategory`]"),
            ("[`${string}_day`]", "[`${string}:day`]"),
            ("[`${string}_event`]", "[`${string}:event`]"),
            ("[`${string}_interval`]", "[`${string}:interval`]"),
            ("[`${string}_more`]", "[`${string}:more`]"),
            ("[`${string}_timeCategory`]", "[`${string}:timeCategory`]"),
            ("[`${string}_time`]", "[`${string}:time`]"),
        ]


class VCard(HtmlElement):
    """
    Vuetify's VCard component.
    See more `info and examples <https://vuetifyjs.com/api/v-card>`_.

    Args:
      flat (boolean):
        Removes the card's elevation.
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the href or to prop.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      title (string, number, boolean):
        Specify a title text for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      prepend_icon (enum):
        Prepends a [v-icon](/components/icons/) component to the header.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      text (string, number, boolean):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      image (string):
        Apply a specific background image to the component.
      subtitle (string, number, boolean):
        Specify a subtitle text for the component.
      append_avatar (string):
        Appends a [v-avatar](/components/avatars/) component after default
        content in the **append** slot.
      hover (boolean):
        Applies **4dp** of elevation when hovered (default 2dp). You
        can find more information on the [elevation page](/styles/elevation).
      prepend_avatar (string):
        Prepends a [v-avatar](/components/avatars/) component in the
        **prepend** slot before default content.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCard", children, **kwargs)
        self._attr_names += [
            "flat",
            "replace",
            "link",
            "tag",
            "title",
            "disabled",
            "height",
            "width",
            "theme",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "ripple",
            "text",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "loading",
            "location",
            "position",
            "rounded",
            "tile",
            "href",
            "exact",
            "to",
            "color",
            "variant",
            "image",
            "subtitle",
            ("append_avatar", "appendAvatar"),
            "hover",
            ("prepend_avatar", "prependAvatar"),
        ]
        self._event_names += []


class VCardActions(HtmlElement):
    """
    Vuetify's VCardActions component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-actions>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardActions", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCardItem(HtmlElement):
    """
    Vuetify's VCardItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-item>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      title (string, number, boolean):
        Specify a title text for the component.
      prepend_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend**
        slot before default content.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      subtitle (string, number, boolean):
        Specify a subtitle text for the component.
      append_avatar (string):
        Appends a [v-avatar](/components/avatars/) component after default
        content in the **append** slot.
      prepend_avatar (string):
        Prepends a [v-avatar](/components/avatars/) component in the
        **prepend** slot before default content.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardItem", children, **kwargs)
        self._attr_names += [
            "tag",
            "title",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "density",
            "subtitle",
            ("append_avatar", "appendAvatar"),
            ("prepend_avatar", "prependAvatar"),
        ]
        self._event_names += []


class VCardSubtitle(HtmlElement):
    """
    Vuetify's VCardSubtitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-subtitle>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      opacity (string, number):
        Sets the component's opacity value
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardSubtitle", children, **kwargs)
        self._attr_names += [
            "tag",
            "opacity",
        ]
        self._event_names += []


class VCardText(HtmlElement):
    """
    Vuetify's VCardText component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-text>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      opacity (string, number):
        Sets the component's opacity value
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardText", children, **kwargs)
        self._attr_names += [
            "tag",
            "opacity",
        ]
        self._event_names += []


class VCardTitle(HtmlElement):
    """
    Vuetify's VCardTitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-title>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardTitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCarousel(HtmlElement):
    """
    Vuetify's VCarousel component.
    See more `info and examples <https://vuetifyjs.com/api/v-carousel>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      reverse (boolean):
        Reverse the normal transition direction.
      progress (string, boolean):
        Displays a carousel progress bar. Requires the **cycle** prop and **interval**.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      cycle (boolean):
        Determines if the carousel should cycle through images.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      color (string):
        Applies a color to the navigation dots - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      direction ('horizontal', 'vertical'):
        The transition direction when changing windows.
      interval (string, number):
        The duration between image cycles. Requires the **cycle** prop.
      delimiter_icon (enum):
        Sets icon for carousel delimiter.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_delimiters (boolean):
        Hides the carousel's bottom delimiters.
      hide_delimiter_background (boolean):
        Hides the bottom delimiter background.
      continuous (boolean):
        Determines whether carousel is continuous.
      next_icon (enum):
        The displayed icon for forcing pagination to the next item.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        The displayed icon for forcing pagination to the previous item.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      show_arrows (string, boolean):
        Displays arrows for next/previous navigation.
      touch (TouchHandlers):
        Provide a custom **left** and **right** function when swiped left or right.
      crossfade (boolean):
        Enables crossfade transition.
      transition_duration (number):
        Overrides transition duration.
      vertical_arrows (boolean, 'left', 'right'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VWindow.json))
      vertical_delimiters (boolean, 'left', 'right'):
        Displays carousel delimiters vertically.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCarousel", children, **kwargs)
        self._attr_names += [
            "tag",
            "reverse",
            "progress",
            "disabled",
            "height",
            "theme",
            "cycle",
            ("selected_class", "selectedClass"),
            "color",
            ("model_value", "modelValue"),
            "mandatory",
            "direction",
            "interval",
            ("delimiter_icon", "delimiterIcon"),
            ("hide_delimiters", "hideDelimiters"),
            ("hide_delimiter_background", "hideDelimiterBackground"),
            "continuous",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            "touch",
            "crossfade",
            ("transition_duration", "transitionDuration"),
            ("vertical_arrows", "verticalArrows"),
            ("vertical_delimiters", "verticalDelimiters"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VCarouselItem(HtmlElement):
    """
    Vuetify's VCarouselItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-carousel-item>`_.

    Args:
      alt (string):
        Alternate text for screen readers. Leave empty for decorative images.
      disabled (boolean):
        Prevents the item from becoming active when using the "next"
        and "prev" buttons or the `toggle` method.
      height (string, number):
        Sets the height for the component.
      src (enum):
        The image URL. This prop is mandatory.

        Enum values: [
          string, { src: string; srcset: string; lazySrc: string; aspect: number }
        ]
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      width (string, number):
        Sets the width for the component.
      draggable (boolean, 'true', 'false'):
        Controls the `draggable` behavior of the image. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable).
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      position (string):
        Applies [object-position](https://developer.mozilla.org/en-US/docs/Web/CSS/object-position)
        styles to the image and placeholder elements.
      absolute (boolean):
        Applies position: absolute to the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      inline (boolean):
        Display as an inline element instead of a block, also disables flex-grow.
      transition (string, boolean):
        The transition to use when switching from `lazy-src` to `src`.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.
      content_class (any):
        Apply a custom class to the internal content element.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      options (IntersectionObserverInit):
        Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
        constructor.
      cover (boolean):
        Resizes the background image to cover the entire container.
      gradient (string):
        The gradient to apply to the image. Only supports [linear-gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient)
        syntax, anything else should be done with classes.
      lazy_src (string):
        Something to show while waiting for the main image to load, typically
        a small base64-encoded thumbnail. Has a slight blur filter applied.
          NOTE: This prop has no effect unless either `height` or `aspect-ratio`
        are provided.
      sizes (string):
        For use with `srcset`, see [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes).
      srcset (string):
        A set of alternate images to use based on device size. [Read
        more...](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset).
      aspect_ratio (string, number):
        Calculated as `width/height`, so for a 1920x1080px image this
        will be `1.7778`. Will be calculated automatically if omitted.
      crossorigin ('', 'anonymous', 'use-credentials'):
        Specify that images should be fetched with CORS enabled [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#crossorigin)
      referrerpolicy (enum):
        Define which referrer is sent when fetching the resource [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#referrerpolicy)

        Enum values: [
          'origin', 'no-referrer', 'no-referrer-when-downgrade', 'origin-when-cross-origin',
          'same-origin', 'strict-origin', 'strict-origin-when-cross-origin',
          'unsafe-url'
        ]
      reverse_transition (string, boolean):
        Sets the reverse transition.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCarouselItem", children, **kwargs)
        self._attr_names += [
            "alt",
            "disabled",
            "height",
            "src",
            "value",
            "width",
            "draggable",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            ("selected_class", "selectedClass"),
            "position",
            "absolute",
            "rounded",
            "tile",
            "color",
            "inline",
            "transition",
            ("content_class", "contentClass"),
            "eager",
            "options",
            "cover",
            "gradient",
            ("lazy_src", "lazySrc"),
            "sizes",
            "srcset",
            ("aspect_ratio", "aspectRatio"),
            "crossorigin",
            "referrerpolicy",
            ("reverse_transition", "reverseTransition"),
        ]
        self._event_names += []


class VCheckbox(HtmlElement):
    """
    Vuetify's VCheckbox component.
    See more `info and examples <https://vuetifyjs.com/api/v-checkbox>`_.

    Args:
      type (string):
        Provides the default type for children selection controls.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the component.
      indeterminate (boolean):
        Sets an indeterminate state for the checkbox.
      multiple (boolean):
        Changes expected model to an array.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      width (string, number):
        Sets the width for the component.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the input is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      indeterminate_icon (enum):
        The icon used when in an indeterminate state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_value (any):
        Sets value for truthy state.
      false_value (any):
        Sets value for falsy state.
      defaults_target (string):
        The target component to provide defaults values for.
      false_icon (enum):
        The icon used when inactive.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_icon (enum):
        The icon used when active.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3729: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when appended icon is clicked.
      update_focused (event):
        Event that is emitted when the component's focus state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCheckbox", children, **kwargs)
        self._attr_names += [
            "type",
            "name",
            "error",
            "label",
            "disabled",
            "indeterminate",
            "multiple",
            "value",
            "width",
            "id",
            "theme",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "ripple",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "color",
            ("model_value", "modelValue"),
            "direction",
            "messages",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("indeterminate_icon", "indeterminateIcon"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
        ]


class VCheckboxBtn(HtmlElement):
    """
    Vuetify's VCheckboxBtn component.
    See more `info and examples <https://vuetifyjs.com/api/v-checkbox-btn>`_.

    Args:
      type (string):
        Provides the default type for children selection controls.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the component.
      indeterminate (boolean):
        Puts the control in an indeterminate state. Used with the [indeterminate-icon](#props-indeterminate-icon)
        property.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of the input when it is not focused.
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      inline (boolean):
        Puts children inputs into a row.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      indeterminate_icon (enum):
        Icon used when the component is in an indeterminate state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_value (any):
        Sets value for truthy state.
      false_value (any):
        Sets value for falsy state.
      defaults_target (string):
        The target component to provide defaults values for.
      false_icon (enum):
        The icon used when inactive.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_icon (enum):
        The icon used when active.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3729: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_indeterminate (event):
        Event that is emitted when the component's indeterminate state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCheckboxBtn", children, **kwargs)
        self._attr_names += [
            "type",
            "name",
            "error",
            "label",
            "disabled",
            "indeterminate",
            "multiple",
            "value",
            "id",
            "theme",
            ("base_color", "baseColor"),
            "readonly",
            "ripple",
            "density",
            "color",
            "inline",
            ("model_value", "modelValue"),
            ("indeterminate_icon", "indeterminateIcon"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_indeterminate", "update:indeterminate"),
        ]


class VChip(HtmlElement):
    """
    Vuetify's VChip component.
    See more `info and examples <https://vuetifyjs.com/api/v-chip>`_.

    Args:
      filter (boolean):
        Displays a selection icon when selected.
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the href or to prop.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      label (boolean):
        Applies a medium size border radius.
      disabled (boolean):
        Removes the ability to click or target the component.
      size (string, number):
        Sets the height, padding and the font size of the component.
        Accepts only predefined options: **x-small**, **small**, **default**,
        **large**, and **x-large**.
      value (any):
        The value used when a child of a [v-chip-group](/components/chip-groups).
      draggable (boolean):
        Makes the chip draggable.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of component when not focused.
      prepend_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend**
        slot before default content.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      text (string, number, boolean):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      active_class (string):
        The class applied to the component when it matches the current
        route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class)
        on the [vue-router](https://router.vuejs.org/) documentation.
      append_avatar (string):
        Appends a [v-avatar](/components/avatars/) component after default
        content in the **append** slot.
      prepend_avatar (string):
        Prepends a [v-avatar](/components/avatars/) component in the
        **prepend** slot before default content.
      closable (boolean):
        Adds remove button and then a chip can be closed.
      close_icon (enum):
        Change the default icon used for **close** chips.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      close_label (string):
        Text used for *aria-label* on the close button in **close** chips.
        Can also be customized globally in [Internationalization](/customization/internationalization).
      filter_icon (enum):
        Change the default icon used for **filter** chips.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      pill (boolean):
        Remove `v-avatar` padding.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
      click_close (event):
        Emitted when close icon is clicked.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VChip", children, **kwargs)
        self._attr_names += [
            "filter",
            "replace",
            "link",
            "tag",
            "label",
            "disabled",
            "size",
            "value",
            "draggable",
            "theme",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "ripple",
            "text",
            "border",
            "density",
            "elevation",
            ("selected_class", "selectedClass"),
            "rounded",
            "tile",
            "href",
            "exact",
            "to",
            "color",
            "variant",
            ("model_value", "modelValue"),
            ("active_class", "activeClass"),
            ("append_avatar", "appendAvatar"),
            ("prepend_avatar", "prependAvatar"),
            "closable",
            ("close_icon", "closeIcon"),
            ("close_label", "closeLabel"),
            ("filter_icon", "filterIcon"),
            "pill",
        ]
        self._event_names += [
            "click",
            ("update_modelValue", "update:modelValue"),
            ("group_selected", "group:selected"),
            ("click_close", "click:close"),
        ]


class VChipGroup(HtmlElement):
    """
    Vuetify's VChipGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-chip-group>`_.

    Args:
      symbol (any):
        The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
        used to hook into group functionality for components like [v-btn-toggle](/components/btn-toggle)
        and [v-bottom-navigation](/components/bottom-navigations/).
      filter (boolean):
        Applies an checkmark icon in front of every chip for using it like a filter.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Puts all children components into a disabled state.
      max (number):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allows one to select multiple items.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of component when not focused. Recommended with
        `color` or `filter` to properly highlight selected items.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Sets the designated mobile breakpoint for the component.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      content_class (any):
        Adds classes to the slide group item.
      direction ('horizontal', 'vertical'):
        Switch between horizontal and vertical modes.
      column (boolean):
        Remove horizontal pagination and wrap items as needed.
      next_icon (enum):
        Specify the icon to use for the next icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        Specify the icon to use for the prev icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      show_arrows (string, boolean):
        Force the display of the pagination arrows.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3729: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      center_active (boolean):
        Forces the selected chip to be centered.
      scroll_to_active (boolean):
        Keeps the last active element visible when resizing the scrollable container.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VChipGroup", children, **kwargs)
        self._attr_names += [
            "symbol",
            "filter",
            "tag",
            "disabled",
            "max",
            "multiple",
            "theme",
            ("base_color", "baseColor"),
            ("selected_class", "selectedClass"),
            "color",
            "variant",
            ("model_value", "modelValue"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "mandatory",
            ("content_class", "contentClass"),
            "direction",
            "column",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            ("value_comparator", "valueComparator"),
            ("center_active", "centerActive"),
            ("scroll_to_active", "scrollToActive"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VClassIcon(HtmlElement):
    """
    Vuetify's VClassIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-class-icon>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VClassIcon", children, **kwargs)
        self._attr_names += [
            "tag",
            "icon",
        ]
        self._event_names += []


class VCode(HtmlElement):
    """
    Vuetify's VCode component.
    See more `info and examples <https://vuetifyjs.com/api/v-code>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCode", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCol(HtmlElement):
    """
    Vuetify's VCol component.
    See more `info and examples <https://vuetifyjs.com/api/v-col>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      sm (string, number, boolean):
        Changes the number of columns on small and greater breakpoints.
      md (string, number, boolean):
        Changes the number of columns on medium and greater breakpoints.
      lg (string, number, boolean):
        Changes the number of columns on large and greater breakpoints.
      xl (string, number, boolean):
        Changes the number of columns on extra large and greater breakpoints.
      xxl (string, number, boolean):
        Changes the number of columns on extra extra large and greater breakpoints.
      order (string, number):
        Sets the default [order](https://developer.mozilla.org/en-US/docs/Web/CSS/order)
        for the column.
      offset (string, number):
        Sets the default offset for the column.
      cols (string, number, boolean):
        Sets the default number of columns the component extends. Available
        options are: **1 -> 12** and **auto**.
      offset_sm (string, number):
        Changes the offset of the component on small and greater breakpoints.
      offset_md (string, number):
        Changes the offset of the component on medium and greater breakpoints.
      offset_lg (string, number):
        Changes the offset of the component on large and greater breakpoints.
      offset_xl (string, number):
        Changes the offset of the component on extra large and greater breakpoints.
      offset_xxl (string, number):
        Changes the offset of the component on extra extra large and
        greater breakpoints.
      order_sm (string, number):
        Changes the order of the component on small and greater breakpoints.
      order_md (string, number):
        Changes the order of the component on medium and greater breakpoints.
      order_lg (string, number):
        Changes the order of the component on large and greater breakpoints.
      order_xl (string, number):
        Changes the order of the component on extra large and greater breakpoints.
      order_xxl (string, number):
        Changes the order of the component on extra extra large and greater breakpoints.
      align_self ('start', 'end', 'center', 'auto', 'baseline', 'stretch'):
        Applies the [align-items](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items)
        css property. Available options are: **start**, **center**, **end**,
        **auto**, **baseline** and **stretch**.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCol", children, **kwargs)
        self._attr_names += [
            "tag",
            "sm",
            "md",
            "lg",
            "xl",
            "xxl",
            "order",
            "offset",
            "cols",
            ("offset_sm", "offsetSm"),
            ("offset_md", "offsetMd"),
            ("offset_lg", "offsetLg"),
            ("offset_xl", "offsetXl"),
            ("offset_xxl", "offsetXxl"),
            ("order_sm", "orderSm"),
            ("order_md", "orderMd"),
            ("order_lg", "orderLg"),
            ("order_xl", "orderXl"),
            ("order_xxl", "orderXxl"),
            ("align_self", "alignSelf"),
        ]
        self._event_names += []


class VColorInput(HtmlElement):
    """
    Vuetify's VColorInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-color-input>`_.

    Args:
      title (string):
        Specify a title text for the component.
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      type (string):
        Sets input type.
      model_value (string, Record<string, unknown>):
        Represents the committed v-model value
      error (boolean):
        Puts the input in a manual error state.
      reverse (boolean):
        Reverses the orientation.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width of the color picker.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      position ('fixed', 'static', 'relative', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Adds a border radius to the input.
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      name (string):
        Sets the component's name attribute.
      autocomplete (string):
        Helps influence browser's suggestions. Special value **suppress**
        manipulates fields `name` attribute while **off** relies on browser's
        good will to stop suggesting values. Any other value is passed
        to the native `autocomplete` on the underlying element.
      disabled (boolean):
        Removes the ability to click or target the input.
      placeholder (string):
        Sets the input’s placeholder text.
      id (string):
        Sets the DOM id on the component.
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      autofocus (boolean):
        Enables autofocus.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      mode ('rgb', 'rgba', 'hsl', 'hsla', 'hex', 'hexa'):
        The current selected input type. Syncable with `v-model:mode`.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outside the component's input, uses the
        same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      readonly (boolean):
        Puts input in readonly state.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      append_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **append-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      dirty (boolean):
        Manually apply the dirty state styling.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      counter_value (number, js_fn):
        Function returns the counter display text.
      model_modifiers (unknown):
        **FOR INTERNAL USE ONLY**
      hide_pip (boolean):
        Hide pip icon
      color_pip (boolean):
        Synchronize pip color with current value
      pip_icon (string):
        The icon used for pip
      pip_location ('prepend', 'append', 'prepend-inner', 'append-inner'):
        Move pip icon to a different slot
      pip_variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Variant of the pip control
      cancel_text (string):
        Text for the cancel button
      ok_text (string):
        Text for the ok button
      hide_actions (boolean):
        Prevent showing the default actions buttons. Does not affect
        `<component :is="actions" />`
      canvas_height (string, number):
        Height of canvas.
      dot_size (string, number):
        Changes the size of the selection dot on the canvas.
      hide_canvas (boolean):
        Hides canvas.
      hide_sliders (boolean):
        Hides sliders.
      hide_inputs (boolean):
        Hides inputs.
      modes (('rgb', 'rgba', 'hsl', 'hsla', 'hex', 'hexa')[]):
        Sets available input types.
      show_swatches (boolean):
        Displays color swatches.
      swatches_max_height (string, number):
        Sets the maximum height of the swatches section.
      divided (boolean):
        Adds a divider between the header and controls.
      landscape (boolean):
        Puts the picker into landscape mode.
      hide_header (boolean):
        Hide the picker header.
      hide_title (boolean):
        Hide the picker title.
      hide_eye_dropper (boolean):
        Hides eyedropper icon.
      eye_dropper_icon (enum):
        Icon used to trigger EyeDropper API.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      swatches (enum):
        Sets the available color swatches to select from. 2D array of
        rows and columns, accepts any color format the picker does.

        Enum values: [
          (, string, number, {      readonly h: number      readonly s:
          number      readonly v: number      readonly a?: number, undefined
             }, {      readonly r: number      readonly g: number
          readonly b: number      readonly a?: number, undefined    },
          {      readonly h: number      readonly s: number      readonly
          l: number      readonly a?: number, undefined    })[][]
        ]
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VColorInput", children, **kwargs)
        self._attr_names += [
            "title",
            "flat",
            "border",
            "type",
            ("model_value", "modelValue"),
            "error",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "position",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            "name",
            "autocomplete",
            "disabled",
            "placeholder",
            "id",
            "prefix",
            "role",
            "autofocus",
            "label",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "mode",
            "counter",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "readonly",
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "loading",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
            ("hide_pip", "hidePip"),
            ("color_pip", "colorPip"),
            ("pip_icon", "pipIcon"),
            ("pip_location", "pipLocation"),
            ("pip_variant", "pipVariant"),
            ("cancel_text", "cancelText"),
            ("ok_text", "okText"),
            ("hide_actions", "hideActions"),
            ("canvas_height", "canvasHeight"),
            ("dot_size", "dotSize"),
            ("hide_canvas", "hideCanvas"),
            ("hide_sliders", "hideSliders"),
            ("hide_inputs", "hideInputs"),
            "modes",
            ("show_swatches", "showSwatches"),
            ("swatches_max_height", "swatchesMaxHeight"),
            "divided",
            "landscape",
            ("hide_header", "hideHeader"),
            ("hide_title", "hideTitle"),
            ("hide_eye_dropper", "hideEyeDropper"),
            ("eye_dropper_icon", "eyeDropperIcon"),
            "swatches",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
        ]


class VColorPicker(HtmlElement):
    """
    Vuetify's VColorPicker component.
    See more `info and examples <https://vuetifyjs.com/api/v-color-picker>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      mode ('rgb', 'rgba', 'hsl', 'hsla', 'hex', 'hexa'):
        The current selected input type. Syncable with `v-model:mode`.
      title (string):
        Specify a title text for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width of the color picker.
      theme (string):
        Specify a theme for this component and all of its children.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (string, Record<string, unknown>):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      divided (boolean):
        Adds a divider between the header and controls.
      hide_header (boolean):
        Hide the picker header.
      canvas_height (string, number):
        Height of canvas.
      dot_size (string, number):
        Changes the size of the selection dot on the canvas.
      hide_canvas (boolean):
        Hides canvas.
      hide_sliders (boolean):
        Hides sliders.
      hide_inputs (boolean):
        Hides inputs.
      modes (('rgb', 'rgba', 'hsl', 'hsla', 'hex', 'hexa')[]):
        Sets available input types.
      show_swatches (boolean):
        Displays color swatches.
      swatches_max_height (string, number):
        Sets the maximum height of the swatches section.
      landscape (boolean):
        Puts the picker into landscape mode.
      hide_title (boolean):
        Hide the picker title.
      hide_eye_dropper (boolean):
        Hides eyedropper icon.
      eye_dropper_icon (enum):
        Icon used to trigger EyeDropper API.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      swatches (enum):
        Sets the available color swatches to select from. 2D array of
        rows and columns, accepts any color format the picker does.

        Enum values: [
          (, string, number, {      readonly h: number      readonly s:
          number      readonly v: number      readonly a?: number, undefined
             }, {      readonly r: number      readonly g: number
          readonly b: number      readonly a?: number, undefined    },
          {      readonly h: number      readonly s: number      readonly
          l: number      readonly a?: number, undefined    })[][]
        ]
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_mode (event):
        Selected mode.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VColorPicker", children, **kwargs)
        self._attr_names += [
            "tag",
            "mode",
            "title",
            "disabled",
            "height",
            "width",
            "theme",
            "border",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "location",
            "position",
            "rounded",
            "tile",
            "color",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "divided",
            ("hide_header", "hideHeader"),
            ("canvas_height", "canvasHeight"),
            ("dot_size", "dotSize"),
            ("hide_canvas", "hideCanvas"),
            ("hide_sliders", "hideSliders"),
            ("hide_inputs", "hideInputs"),
            "modes",
            ("show_swatches", "showSwatches"),
            ("swatches_max_height", "swatchesMaxHeight"),
            "landscape",
            ("hide_title", "hideTitle"),
            ("hide_eye_dropper", "hideEyeDropper"),
            ("eye_dropper_icon", "eyeDropperIcon"),
            "swatches",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_mode", "update:mode"),
        ]


class VCombobox(HtmlElement):
    """
    Vuetify's VCombobox component.
    See more `info and examples <https://vuetifyjs.com/api/v-combobox>`_.

    Args:
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      type (string):
        Sets input type.
      reverse (boolean):
        Reverses the orientation.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      menu (boolean):
        Renders with the menu open by default.
      delimiters (string[]):
        Accepts an array of strings that will trigger a new tag when
        typing. Does not replace the normal Tab and Enter keys.
      autocomplete (string):
        Helps influence browser's suggestions. Special value **suppress**
        manipulates fields `name` attribute while **off** relies on browser's
        good will to stop suggesting values. Any other value is passed
        to the native `autocomplete` on the underlying element.
      disabled (boolean):
        Removes the ability to click or target the input.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      placeholder (string):
        Sets the input’s placeholder text.
      width (string, number):
        Sets the width for the component.
      id (string):
        Sets the DOM id on the component.
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      autofocus (boolean):
        Enables autofocus.
      theme (string):
        Specify a theme for this component and all of its children.
      items (any[]):
        Can be an array of objects or strings. By default objects should
        have **title** and **value** properties, and can optionally have
        a **props** property containing any [VListItem props](/api/v-list-item/#props).
        Keys to use for these can be changed with the **item-title**,
        **item-value**, and **item-props** props.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the outside the component's input, uses the
        same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts input in readonly state.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      rounded (string, number, boolean):
        Adds a border radius to the input.
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      item_props (SelectItemKey):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3729: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      always_filter (boolean):
        When enabled, dropdown list will always show items matching non-empty
        value within the field. Recommended when the list is meant to
        show suggestions rather than options to choose from. For optimal
        UX, should be combined with `:menu-icon="false"` and `hide-selected`.
      auto_select_first (boolean, 'exact'):
        When searching, will always highlight the first option and select
        it on blur. `exact` will only highlight and select exact matches.
      clear_on_select (boolean):
        Reset the search text when a selection is made while using the
        **multiple** prop.
      filter_mode ('every', 'some', 'union', 'intersection'):
        Controls how the results of `customFilter` and `customKeyFilter`
        are combined. All modes only apply `customFilter` to columns
        not specified in `customKeyFilter`.  - **some**: There is at
        least one match from either the custom filter or the custom key
        filter. - **every**: All columns match either the custom filter
        or the custom key filter. - **union**: There is at least one
        match from the custom filter, or all columns match the custom
        key filters. - **intersection**: There is at least one match
        from the custom filter, and all columns match the custom key
        filters.
      no_filter (boolean):
        Disables all item filtering.
      custom_filter (FilterFunction):
        Function used to filter items, called for each filterable key
        on each item in the list. The first argument is the filterable
        value from the item, the second is the search term, and the third
        is the internal item object. The function should return true
        if the item should be included in the filtered list, or the index
        of the match in the value if it should be included with the result
        highlighted.
      custom_key_filter (unknown):
        Function used on specific keys within the item object. `customFilter`
        is skipped for columns with `customKeyFilter` specified.
      filter_keys (string, string[]):
        Array of specific keys to filter on the item.
      chips (boolean):
        Changes display of selections to chips.
      closable_chips (boolean):
        Enables the [closable](/api/v-chip/#props-closable) prop on all
        [v-chip](/components/chips/) components.
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      hide_selected (boolean):
        Do not display in the select menu items that are already selected.
      list_props (unknown):
        Pass props through to the `v-list` component. Accepts an object
        with anything from [v-list](/api/v-list/#props) props, camelCase
        keys are recommended.
      item_title (SelectItemKey):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      item_children (SelectItemKey):
        This property currently has **no effect**.
      item_type (SelectItemKey):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/list-items.json))
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      menu_icon (enum):
        Sets the the spin icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      menu_props (unknown):
        Pass props through to the `v-menu` component. Accepts an object
        with anything from [v-menu](/api/v-menu/#props) props, camelCase
        keys are recommended.
      no_data_text (string):
        Text shown when no items are provided to the component.
      open_on_clear (boolean):
        Open's the menu whenever the clear icon is clicked.
      item_color (string):
        Sets color of selected items.
      no_auto_scroll (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/Select.json))
      close_text (string):
        Text set to the inputs `aria-label` and `title` when input menu is closed.
      open_text (string):
        Text set to the inputs **aria-label** and **title** when input menu is open.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      counter_value (number, js_fn):
        Function returns the counter display text.
      model_modifiers (unknown):
        **FOR INTERNAL USE ONLY**
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
      update_search (event):
        Event emitted when the search value changes.
      update_menu (event):
        Event that is emitted when the component's menu state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCombobox", children, **kwargs)
        self._attr_names += [
            "flat",
            "type",
            "reverse",
            "name",
            "error",
            "label",
            "menu",
            "delimiters",
            "autocomplete",
            "disabled",
            "multiple",
            "placeholder",
            "width",
            "id",
            "prefix",
            "role",
            "autofocus",
            "theme",
            "items",
            "active",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "loading",
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "eager",
            ("item_props", "itemProps"),
            "direction",
            "messages",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            "focused",
            ("hide_details", "hideDetails"),
            ("value_comparator", "valueComparator"),
            ("always_filter", "alwaysFilter"),
            ("auto_select_first", "autoSelectFirst"),
            ("clear_on_select", "clearOnSelect"),
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            "chips",
            ("closable_chips", "closableChips"),
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            ("list_props", "listProps"),
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_type", "itemType"),
            ("return_object", "returnObject"),
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("item_color", "itemColor"),
            ("no_auto_scroll", "noAutoScroll"),
            ("close_text", "closeText"),
            ("open_text", "openText"),
            "counter",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            "clearable",
            ("clear_icon", "clearIcon"),
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_search", "update:search"),
            ("update_menu", "update:menu"),
        ]


class VComponentIcon(HtmlElement):
    """
    Vuetify's VComponentIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-component-icon>`_.

    Args:
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VComponentIcon", children, **kwargs)
        self._attr_names += [
            "icon",
            "tag",
        ]
        self._event_names += []


class VConfirmEdit(HtmlElement):
    """
    Vuetify's VConfirmEdit component.
    See more `info and examples <https://vuetifyjs.com/api/v-confirm-edit>`_.

    Args:
      model_value (unknown):
        Represents the committed v-model value
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      disabled (boolean, ('cancel', 'save')[]):
        Control the disabled state of action buttons. If not provided,
        internal logic will be used to determine the disabled state.
      cancel_text (string):
        Text for the cancel button
      ok_text (string):
        Text for the ok button
      hide_actions (boolean):
        Prevent showing the default actions buttons. Does not affect
        `<component :is="actions" />`
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      cancel (event):
        The event emitted when the user clicks the Cancel button
      save (event):
        The event emitted when the user clicks the Save button
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VConfirmEdit", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "color",
            "disabled",
            ("cancel_text", "cancelText"),
            ("ok_text", "okText"),
            ("hide_actions", "hideActions"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "cancel",
            "save",
        ]


class VContainer(HtmlElement):
    """
    Vuetify's VContainer component.
    See more `info and examples <https://vuetifyjs.com/api/v-container>`_.

    Args:
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      fluid (boolean):
        Removes viewport maximum-width size breakpoints.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VContainer", children, **kwargs)
        self._attr_names += [
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "tag",
            "fluid",
        ]
        self._event_names += []


class VCounter(HtmlElement):
    """
    Vuetify's VCounter component.
    See more `info and examples <https://vuetifyjs.com/api/v-counter>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      max (string, number):
        Sets the maximum allowed value.
      value (string, number):
        Sets the current counter value.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          { component: Component }
        ]
      active (boolean):
        Determines whether the counter is visible or not.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCounter", children, **kwargs)
        self._attr_names += [
            "disabled",
            "max",
            "value",
            "transition",
            "active",
        ]
        self._event_names += []


class VDataIterator(HtmlElement):
    """
    Vuetify's VDataIterator component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-iterator>`_.

    Args:
      search (string):
        Text input used to filter items.
      model_value (any[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      filter_mode ('every', 'some', 'union', 'intersection'):
        Controls how the results of `customFilter` and `customKeyFilter`
        are combined. All modes only apply `customFilter` to columns
        not specified in `customKeyFilter`.  - **some**: There is at
        least one match from either the custom filter or the custom key
        filter. - **every**: All columns match either the custom filter
        or the custom key filter. - **union**: There is at least one
        match from the custom filter, or all columns match the custom
        key filters. - **intersection**: There is at least one match
        from the custom filter, and all columns match the custom key
        filters.
      no_filter (boolean):
        Disables all item filtering.
      custom_filter (FilterFunction):
        Function to filter items.
      custom_key_filter (unknown):
        Function used on specific keys within the item object. `customFilter`
        is skipped for columns with `customKeyFilter` specified.
      filter_keys (string, string[]):
        Array of specific keys to filter on the item.
      select_strategy ('single', 'page', 'all'):
        Defines the strategy of selecting items in the list. Possible
        values are: 'single' (only one item can be selected at a time),
        'page' ('Select all' button will select only items on the current
        page), 'all' ('Select all' button will select all items in the
        list).
      items (unknown[]):
        An array of strings or objects used for automatically generating
        children components.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3888: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          { component: Component; hideOnLeave: boolean }
        ]
      loading (boolean):
        If `true` and no items are provided, then a loading text will be shown.
      item_selectable (SelectItemKey):
        Property on supplied `items` that contains the boolean value
        indicating if the item is selectable.
      show_select (boolean):
        Shows the column with checkboxes for selecting items in the list.
      page (string, number):
        The current displayed page number (1-indexed).
      initial_sort_order ('desc', 'asc'):
        Specifies the initial sort order when an **toggleSort** is called
        for unsorted property.
      sort_by (SortItem):
        Array of column keys and sort orders that determines the sort
        order of the table.
      multi_sort (enum):
        Let user sort by multiple properties/columns.  - **key**: (optional)
        when set to `ctrl`, user is required to hold a keyboard key (Ctrl
        on PC and Command on Mac) - **mode**: when user selects a new
        column to sort by, it will be set first (`prepend`) or last (`append`)
        in the sort priority. Defaults to `append` - **modifier**: (optional)
        allows user to use both multi-sort modes (`append` and `prepend`)
        simultaneously  **Note**: object notation requires at least **v3.11.0**

        Enum values: [
          boolean, { key: 'ctrl'; mode: 'prepend', 'append'; modifier: 'shift', 'alt' }
        ]
      must_sort (boolean):
        Forces sorting on the column(s).
      custom_key_sort (unknown):
        Function used on specific keys within the item object. `customSort`
        is skipped for columns with `customKeySort` specified.
      items_per_page (string, number):
        Changes how many items per page should be visible. Can be bound
        to external variable using **v-model:itemsPerPage**.. Setting
        this prop to `-1` will display all items on the page.
      expand_on_click (boolean):
        Expands item when the row is clicked.
      show_expand (boolean):
        Shows the expand icon.
      expanded (string[]):
        Array of expanded items. Can be bound to external variable using
        **v-model:expanded**.
      group_by (SortItem):
        Configures attributes (and sort order) to group items together.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_expanded (event):
        Emits when the **expanded** items are updated.
      update_groupBy (event):
        Emits when the **group-by** prop is updated.
      update_page (event):
        Emits when the **page** prop is updated.
      update_itemsPerPage (event):
        Emits when the **items-per-page** prop is updated.
      update_sortBy (event):
        Emits when the **sortBy** prop is updated.
      update_options (event):
        Emits when pagination related properties (page, itemsPerPage,
        sortBy, groupBy, search) is updated.
      update_currentItems (event):
        Emits with the items currently being displayed.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataIterator", children, **kwargs)
        self._attr_names += [
            "search",
            ("model_value", "modelValue"),
            "tag",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            ("select_strategy", "selectStrategy"),
            "items",
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "transition",
            "loading",
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            "page",
            ("initial_sort_order", "initialSortOrder"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            ("items_per_page", "itemsPerPage"),
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_expanded", "update:expanded"),
            ("update_groupBy", "update:groupBy"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_currentItems", "update:currentItems"),
        ]


class VDataTable(HtmlElement):
    """
    Vuetify's VDataTable component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table>`_.

    Args:
      search (string):
        Text input used to filter items.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height of the table rows.
      height (string, number):
        Set an explicit height of table.
      width (string, number):
        Sets the width for the component.
      sticky (boolean):
        Deprecated, use `fixed-header` instead.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies a color to sort badges in the table header.
      filter_mode ('every', 'some', 'union', 'intersection'):
        Controls how the results of `customFilter` and `customKeyFilter`
        are combined. All modes only apply `customFilter` to columns
        not specified in `customKeyFilter`.  - **some**: There is at
        least one match from either the custom filter or the custom key
        filter. - **every**: All columns match either the custom filter
        or the custom key filter. - **union**: There is at least one
        match from the custom filter, or all columns match the custom
        key filters. - **intersection**: There is at least one match
        from the custom filter, and all columns match the custom key
        filters.
      no_filter (boolean):
        Disables all item filtering.
      custom_filter (FilterFunction):
        Function to filter items.
      custom_key_filter (unknown):
        Function used on specific keys within the item object. `customFilter`
        is skipped for columns with `customKeyFilter` specified.
      filter_keys (string, string[]):
        Array of specific keys to filter on the item.
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      expand_icon (enum):
        Icon to display when the expandable row is collapsed.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon to display when the expandable row is expanded.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      select_strategy ('single', 'page', 'all'):
        Defines the strategy of selecting items in the list. Possible
        values are: 'single' (only one item can be selected at a time),
        'page' ('Select all' button will select only items on the current
        page), 'all' ('Select all' button will select all items in the
        list).
      items (any[]):
        An array of strings or objects used for automatically generating
        children components.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3888: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      no_data_text (string):
        Text shown when no items are provided to the component.
      loading (string, boolean):
        Displays `loading` slot if set to `true`
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      item_selectable (SelectItemKey):
        Property on supplied `items` that indicates whether the item is selectable.
      show_select (boolean):
        Shows the select checkboxes in both the header and rows (if using default rows).
      page (string, number):
        The current displayed page number (1-indexed).
      initial_sort_order ('desc', 'asc'):
        Specifies the initial sort order when an unsorted column is clicked.
      sort_by (SortItem):
        Changes which item property (or properties) should be used for
        sort order. Can be bound to external variable using **v-model:sortBy**..
      multi_sort (enum):
        Let user sort by multiple properties/columns.  - **key**: (optional)
        when set to `ctrl`, user is required to hold a keyboard key (Ctrl
        on PC and Command on Mac) - **mode**: when user selects a new
        column to sort by, it will be set first (`prepend`) or last (`append`)
        in the sort priority. Defaults to `append` - **modifier**: (optional)
        allows user to use both multi-sort modes (`append` and `prepend`)
        simultaneously  **Note**: object notation requires at least **v3.11.0**

        Enum values: [
          boolean, { key: 'ctrl'; mode: 'prepend', 'append'; modifier: 'shift', 'alt' }
        ]
      must_sort (boolean):
        Forces sorting on the column(s).
      custom_key_sort (unknown):
        Function used on specific keys within the item object. `customSort`
        is skipped for columns with `customKeySort` specified.
      items_per_page (string, number):
        Changes how many items per page should be visible. Can be bound
        to external variable using **v-model:itemsPerPage**.. Setting
        this prop to `-1` will display all items on the page.
      expand_on_click (boolean):
        Expands item when the row is clicked.
      show_expand (boolean):
        Shows the expand toggle in default rows.
      expanded (string[]):
        Array of expanded items. Can be bound to external variable using
        **v-model:expanded**.
      group_by (SortItem):
        Configures attributes (and sort order) to group items together.
        Can be customized further with `group-header` and `group-summary`
        slots.
      header_props (unknown):
        Pass props to the default header. See [`v-data-table-headers`
        API](/api/v-data-table-headers) for more information.
      cell_props (enum):
        An object of additional props to be passed to each `<td>` in
        the table body. Also accepts a function that will be called for
        each cell. If the same prop is defined both here and in `cellProps`
        in a headers object, the value from the headers object will be
        used.

        Enum values: [
          Record<string, any>, ((      data: Pick<        ItemKeySlot<any>,
                 'value', 'item', 'index', 'internalItem', js_fn
        ]
      disable_sort (boolean):
        Toggles rendering of sort button.
      headers (enum):
        An array of objects that each describe a header column.

        Enum values: [
          {  readonly key?:, (string & {}), 'data-table-group', 'data-table-select',
          'data-table-expand', undefined  readonly value?: SelectItemKey<any>
           readonly title?: string, undefined  readonly fixed?: boolean,
          'end', 'start', undefined  readonly align?: 'end', 'start', 'center',
          undefined  readonly width?: string, number, undefined  readonly
          minWidth?: string, number, undefined  readonly maxWidth?: string,
          number, undefined  readonly nowrap?: boolean, undefined  readonly
          intent?: number, undefined  readonly headerProps?: { readonly
          [x: string]: any }, undefined  readonly cellProps?:, { readonly
          [x: string]: any }, HeaderCellPropsFunction, undefined  readonly
          sortable?: boolean, undefined  readonly sort?: DataTableCompareFunction<any>,
          undefined  readonly sortRaw?: DataTableCompareFunction<any>,
          undefined  readonly filter?: FilterFunction, undefined  readonly
          children?: readonly any[], undefined}[]
        ]
      loading_text (string):
        Text shown when the data is loading.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      group_collapse_icon (enum):
        Icon to display when the row group is expanded.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      group_expand_icon (enum):
        Icon to display when the row group is collapsed.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      row_props (enum):
        An object of additional props to be passed to each `<tr>` in
        the table body. Also accepts a function that will be called for
        each row.

        Enum values: [
          Record<string, any>, ((      data: Pick<ItemKeySlot<any>, 'item', 'index', js_fn
        ]
      hide_default_body (boolean):
        Hides the default body.
      hide_default_footer (boolean):
        Hides the default footer.
      hide_default_header (boolean):
        Hides the default header.
      fixed_header (boolean):
        Fixed header to top of table.
      sort_asc_icon (enum):
        Icon used for ascending sort button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      sort_desc_icon (enum):
        Icon used for descending sort button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      fixed_footer (boolean):
        Use the fixed-footer prop together with the height prop to fix
        the footer to the bottom of the table.
      hover (boolean):
        Adds a hover effects to a table rows.
      striped ('odd', 'even'):
        Applies a background to either **even** or **odd** rows.
      prev_icon (enum):
        Previous icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      next_icon (enum):
        Next icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      first_icon (enum):
        First icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      last_icon (enum):
        Last icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      items_per_page_text (string):
        Text for items-per-page dropdown.
      page_text (string):
        Label for page number.
      first_page_label (string):
        Label for first page.
      prev_page_label (string):
        Label for previous page.
      next_page_label (string):
        Label for next page.
      last_page_label (string):
        Label for last page.
      items_per_page_options ((number, { title: string; value: number })[]):
        Array of options to show in the items-per-page dropdown.
      show_current_page (boolean):
        Show current page number between prev/next icons.
      update_modelValue (event):
        Emits when the component's model changes.
      update_expanded (event):
        Emits when the **expanded** items are updated.
      update_groupBy (event):
        Emits when the **group-by** prop is updated.
      update_page (event):
        Emits when the **page** prop is updated.
      update_itemsPerPage (event):
        Emits when the **items-per-page** prop is updated.
      update_sortBy (event):
        Emits when the **sortBy** prop is updated.
      update_options (event):
        Emits when pagination related properties (page, itemsPerPage,
        sortBy, groupBy, search) is updated.
      update_currentItems (event):
        Emits with the items currently being displayed.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTable", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            "search",
            ("model_value", "modelValue"),
            "density",
            "height",
            "width",
            "sticky",
            "tag",
            "theme",
            "color",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            ("hide_no_data", "hideNoData"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("select_strategy", "selectStrategy"),
            "items",
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            ("no_data_text", "noDataText"),
            "loading",
            "mobile",
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            "page",
            ("initial_sort_order", "initialSortOrder"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            ("items_per_page", "itemsPerPage"),
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
            ("header_props", "headerProps"),
            ("cell_props", "cellProps"),
            ("disable_sort", "disableSort"),
            "headers",
            ("loading_text", "loadingText"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("group_collapse_icon", "groupCollapseIcon"),
            ("group_expand_icon", "groupExpandIcon"),
            ("row_props", "rowProps"),
            ("hide_default_body", "hideDefaultBody"),
            ("hide_default_footer", "hideDefaultFooter"),
            ("hide_default_header", "hideDefaultHeader"),
            ("fixed_header", "fixedHeader"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_footer", "fixedFooter"),
            "hover",
            "striped",
            ("prev_icon", "prevIcon"),
            ("next_icon", "nextIcon"),
            ("first_icon", "firstIcon"),
            ("last_icon", "lastIcon"),
            ("items_per_page_text", "itemsPerPageText"),
            ("page_text", "pageText"),
            ("first_page_label", "firstPageLabel"),
            ("prev_page_label", "prevPageLabel"),
            ("next_page_label", "nextPageLabel"),
            ("last_page_label", "lastPageLabel"),
            ("items_per_page_options", "itemsPerPageOptions"),
            ("show_current_page", "showCurrentPage"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_expanded", "update:expanded"),
            ("update_groupBy", "update:groupBy"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_currentItems", "update:currentItems"),
        ]


class VDataTableFooter(HtmlElement):
    """
    Vuetify's VDataTableFooter component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table-footer>`_.

    Args:
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      prev_icon (enum):
        Previous icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      next_icon (enum):
        Next icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      first_icon (enum):
        First icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      last_icon (enum):
        Last icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      items_per_page_text (string):
        Text for items-per-page dropdown.
      page_text (string):
        Label for page number.
      first_page_label (string):
        Label for first page.
      prev_page_label (string):
        Label for previous page.
      next_page_label (string):
        Label for next page.
      last_page_label (string):
        Label for last page.
      items_per_page_options ((number, { title: string; value: number })[]):
        Array of options to show in the items-per-page dropdown.
      show_current_page (boolean):
        Show current page number between prev/next icons.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableFooter", children, **kwargs)
        self._attr_names += [
            "color",
            ("prev_icon", "prevIcon"),
            ("next_icon", "nextIcon"),
            ("first_icon", "firstIcon"),
            ("last_icon", "lastIcon"),
            ("items_per_page_text", "itemsPerPageText"),
            ("page_text", "pageText"),
            ("first_page_label", "firstPageLabel"),
            ("prev_page_label", "prevPageLabel"),
            ("next_page_label", "nextPageLabel"),
            ("last_page_label", "lastPageLabel"),
            ("items_per_page_options", "itemsPerPageOptions"),
            ("show_current_page", "showCurrentPage"),
        ]
        self._event_names += []


class VDataTableHeaders(HtmlElement):
    """
    Vuetify's VDataTableHeaders component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table-headers>`_.

    Args:
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      sticky (boolean):
        Deprecated, use `fixed-header` instead.
      color (string):
        Applies a color to sort badges in the table header.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      initial_sort_order ('desc', 'asc'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableHeaders.json))
      multi_sort (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableHeaders.json))
      header_props (unknown):
        Additional props to be be passed to the default header
      disable_sort (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableHeaders.json))
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      fixed_header (boolean):
        Sticks the header to the top of the table.
      sort_asc_icon (enum):
        Icon used for ascending sort button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      sort_desc_icon (enum):
        Icon used for descending sort button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableHeaders", children, **kwargs)
        self._attr_names += [
            "density",
            "sticky",
            "color",
            "loading",
            "mobile",
            ("initial_sort_order", "initialSortOrder"),
            ("multi_sort", "multiSort"),
            ("header_props", "headerProps"),
            ("disable_sort", "disableSort"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("fixed_header", "fixedHeader"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
        ]
        self._event_names += []


class VDataTableRow(HtmlElement):
    """
    Vuetify's VDataTableRow component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table-row>`_.

    Args:
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      item (unknown):
        Data (key, index and column values) of the displayed item.
      expand_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      cell_props (enum):
        Props to be applied to the cell.

        Enum values: [
          Record<string, any>, ((      data: Pick<        ItemKeySlot<unknown>,
                 'value', 'item', 'index', 'internalItem', js_fn
        ]
      index (number):
        Row index.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      contextmenu (event):
        The event emitted when the user clicks the context menu button.
      dblclick (event):
        The event emitted when the user double clicks the row.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableRow", children, **kwargs)
        self._attr_names += [
            "density",
            "color",
            "item",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "mobile",
            ("cell_props", "cellProps"),
            "index",
            ("mobile_breakpoint", "mobileBreakpoint"),
        ]
        self._event_names += [
            "click",
            "contextmenu",
            "dblclick",
        ]


class VDataTableRows(HtmlElement):
    """
    Vuetify's VDataTableRows component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table-rows>`_.

    Args:
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      expand_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      items (DataTableItem):
        An array of strings or objects used for automatically generating
        children components.
      no_data_text (string):
        Text shown when no items are provided to the component.
      loading (string, boolean):
        Displays `loading` slot if set to `true`
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      cell_props (enum):
        An object of additional props to be passed to each `<td>` in
        the table body. Also accepts a function that will be called for
        each cell. If the same prop is defined both here and in `cellProps`
        in a headers object, the value from the headers object will be
        used.

        Enum values: [
          Record<string, any>, ((      data: Pick<        ItemKeySlot<any>,
                 'value', 'item', 'index', 'internalItem', js_fn
        ]
      loading_text (string):
        Text shown when the data is loading.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      group_collapse_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableGroupHeaderRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      group_expand_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableGroupHeaderRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      row_props (enum):
        An object of additional props to be passed to each `<tr>` in
        the table body. Also accepts a function that will be called for
        each row.

        Enum values: [
          Record<string, any>, ((      data: Pick<ItemKeySlot<any>, 'item', 'index', js_fn
        ]
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableRows", children, **kwargs)
        self._attr_names += [
            "density",
            "color",
            ("hide_no_data", "hideNoData"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "items",
            ("no_data_text", "noDataText"),
            "loading",
            "mobile",
            ("cell_props", "cellProps"),
            ("loading_text", "loadingText"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("group_collapse_icon", "groupCollapseIcon"),
            ("group_expand_icon", "groupExpandIcon"),
            ("row_props", "rowProps"),
        ]
        self._event_names += []


class VDataTableServer(HtmlElement):
    """
    Vuetify's VDataTableServer component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table-server>`_.

    Args:
      search (string):
        Text input used to filter items.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Use the height prop to set the height of the table.
      width (string, number):
        Sets the width for the component.
      sticky (boolean):
        Deprecated, use `fixed-header` instead.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies a color to sort badges in the table header.
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      expand_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      select_strategy ('single', 'page', 'all'):
        Defines the strategy of selecting items in the list. Possible
        values are: 'single' (only one item can be selected at a time),
        'page' ('Select all' button will select only items on the current
        page), 'all' ('Select all' button will select all items in the
        list).
      items (any[]):
        An array of strings or objects used for automatically generating
        children components.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3888: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      no_data_text (string):
        Text shown when no items are provided to the component.
      loading (string, boolean):
        Displays `loading` slot if set to `true`
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      item_selectable (SelectItemKey):
        Property on supplied `items` that indicates whether the item is selectable.
      show_select (boolean):
        Shows the column with checkboxes for selecting items in the list.
      page (string, number):
        The current displayed page number (1-indexed).
      initial_sort_order ('desc', 'asc'):
        Specifies the initial sort order when an unsorted column is clicked.
      sort_by (SortItem):
        Array of column keys and sort orders that determines the sort
        order of the table.
      multi_sort (enum):
        Let user sort by multiple properties/columns.  - **key**: (optional)
        when set to `ctrl`, user is required to hold a keyboard key (Ctrl
        on PC and Command on Mac) - **mode**: when user selects a new
        column to sort by, it will be set first (`prepend`) or last (`append`)
        in the sort priority. Defaults to `append` - **modifier**: (optional)
        allows user to use both multi-sort modes (`append` and `prepend`)
        simultaneously  **Note**: object notation requires at least **v3.11.0**

        Enum values: [
          boolean, { key: 'ctrl'; mode: 'prepend', 'append'; modifier: 'shift', 'alt' }
        ]
      must_sort (boolean):
        Forces sorting on the column(s).
      custom_key_sort (unknown):
        Function used on specific keys within the item object. `customSort`
        is skipped for columns with `customKeySort` specified.
      items_per_page (string, number):
        The number of items to display on each page.
      expand_on_click (boolean):
        Expands item when the row is clicked.
      show_expand (boolean):
        Shows the expand icon.
      expanded (string[]):
        Array of expanded items. Can be bound to external variable using
        **v-model:expanded**.
      group_by (SortItem):
        Defines the grouping of the table items.
      header_props (unknown):
        Pass props to the default header. See [`v-data-table-server`
        API](/api/v-data-table-server) for more information.
      cell_props (enum):
        An object of additional props to be passed to each `<td>` in
        the table body. Also accepts a function that will be called for
        each cell. If the same prop is defined both here and in `cellProps`
        in a headers object, the value from the headers object will be
        used.

        Enum values: [
          Record<string, any>, ((      data: Pick<        ItemKeySlot<any>,
                 'value', 'item', 'index', 'internalItem', js_fn
        ]
      items_length (string, number):
        Number of all items.
      disable_sort (boolean):
        Toggles rendering of sort button.
      headers (enum):
        An array of objects that each describe a header column.

        Enum values: [
          {  readonly key?:, (string & {}), 'data-table-group', 'data-table-select',
          'data-table-expand', undefined  readonly value?: SelectItemKey<any>
           readonly title?: string, undefined  readonly fixed?: boolean,
          'end', 'start', undefined  readonly align?: 'end', 'start', 'center',
          undefined  readonly width?: string, number, undefined  readonly
          minWidth?: string, number, undefined  readonly maxWidth?: string,
          number, undefined  readonly nowrap?: boolean, undefined  readonly
          intent?: number, undefined  readonly headerProps?: { readonly
          [x: string]: any }, undefined  readonly cellProps?:, { readonly
          [x: string]: any }, HeaderCellPropsFunction, undefined  readonly
          sortable?: boolean, undefined  readonly sort?: DataTableCompareFunction<any>,
          undefined  readonly sortRaw?: DataTableCompareFunction<any>,
          undefined  readonly filter?: FilterFunction, undefined  readonly
          children?: readonly any[], undefined}[]
        ]
      loading_text (string):
        Text shown when the data is loading.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      group_collapse_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableGroupHeaderRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      group_expand_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableGroupHeaderRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      row_props (enum):
        An object of additional props to be passed to each `<tr>` in
        the table body. Also accepts a function that will be called for
        each row.

        Enum values: [
          Record<string, any>, ((      data: Pick<ItemKeySlot<any>, 'item', 'index', js_fn
        ]
      hide_default_body (boolean):
        Hides the default body.
      hide_default_footer (boolean):
        Hides the default footer.
      hide_default_header (boolean):
        Hides the default header.
      fixed_header (boolean):
        Use the fixed-header prop together with the height prop to fix
        the header to the top of the table.
      sort_asc_icon (enum):
        Icon used for ascending sort button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      sort_desc_icon (enum):
        Icon used for descending sort button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      fixed_footer (boolean):
        Use the fixed-footer prop together with the height prop to fix
        the footer to the bottom of the table.
      hover (boolean):
        Will add a hover effect to a table's row when the mouse is over it.
      striped ('odd', 'even'):
        Applies a background to either **even** or **odd** rows.
      prev_icon (enum):
        Previous icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      next_icon (enum):
        Next icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      first_icon (enum):
        First icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      last_icon (enum):
        Last icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      items_per_page_text (string):
        Text for items-per-page dropdown.
      page_text (string):
        Label for page number.
      first_page_label (string):
        Label for first page.
      prev_page_label (string):
        Label for previous page.
      next_page_label (string):
        Label for next page.
      last_page_label (string):
        Label for last page.
      items_per_page_options ((number, { title: string; value: number })[]):
        Array of options to show in the items-per-page dropdown.
      show_current_page (boolean):
        Show current page number between prev/next icons.
      update_modelValue (event):
        Emits when the component's model changes.
      update_expanded (event):
        Emits when the **expanded** prop is updated.
      update_groupBy (event):
        Emits when the **group-by** prop is updated.
      update_page (event):
        Emits when the **page** prop is updated.
      update_itemsPerPage (event):
        Emits when the **items-per-page** prop is updated.
      update_sortBy (event):
        Emits when the **sortBy** prop is updated.
      update_options (event):
        Emits when pagination related properties (page, itemsPerPage,
        sortBy, groupBy, search) is updated.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableServer", children, **kwargs)
        self._attr_names += [
            "search",
            ("model_value", "modelValue"),
            "density",
            "height",
            "width",
            "sticky",
            "tag",
            "theme",
            "color",
            ("hide_no_data", "hideNoData"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("select_strategy", "selectStrategy"),
            "items",
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            ("no_data_text", "noDataText"),
            "loading",
            "mobile",
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            "page",
            ("initial_sort_order", "initialSortOrder"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            ("items_per_page", "itemsPerPage"),
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
            ("header_props", "headerProps"),
            ("cell_props", "cellProps"),
            ("items_length", "itemsLength"),
            ("disable_sort", "disableSort"),
            "headers",
            ("loading_text", "loadingText"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("group_collapse_icon", "groupCollapseIcon"),
            ("group_expand_icon", "groupExpandIcon"),
            ("row_props", "rowProps"),
            ("hide_default_body", "hideDefaultBody"),
            ("hide_default_footer", "hideDefaultFooter"),
            ("hide_default_header", "hideDefaultHeader"),
            ("fixed_header", "fixedHeader"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_footer", "fixedFooter"),
            "hover",
            "striped",
            ("prev_icon", "prevIcon"),
            ("next_icon", "nextIcon"),
            ("first_icon", "firstIcon"),
            ("last_icon", "lastIcon"),
            ("items_per_page_text", "itemsPerPageText"),
            ("page_text", "pageText"),
            ("first_page_label", "firstPageLabel"),
            ("prev_page_label", "prevPageLabel"),
            ("next_page_label", "nextPageLabel"),
            ("last_page_label", "lastPageLabel"),
            ("items_per_page_options", "itemsPerPageOptions"),
            ("show_current_page", "showCurrentPage"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_expanded", "update:expanded"),
            ("update_groupBy", "update:groupBy"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
        ]


class VDataTableVirtual(HtmlElement):
    """
    Vuetify's VDataTableVirtual component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table-virtual>`_.

    Args:
      search (string):
        Text input used to filter items.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Use the height prop to set the height of the table.
      width (string, number):
        Sets the width for the component.
      sticky (boolean):
        Deprecated, use `fixed-header` instead.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies a color to sort badges in the table header.
      filter_mode ('every', 'some', 'union', 'intersection'):
        Controls how the results of `customFilter` and `customKeyFilter`
        are combined. All modes only apply `customFilter` to columns
        not specified in `customKeyFilter`.  - **some**: There is at
        least one match from either the custom filter or the custom key
        filter. - **every**: All columns match either the custom filter
        or the custom key filter. - **union**: There is at least one
        match from the custom filter, or all columns match the custom
        key filters. - **intersection**: There is at least one match
        from the custom filter, and all columns match the custom key
        filters.
      no_filter (boolean):
        Disables all item filtering.
      custom_filter (FilterFunction):
        Function used to filter items, called for each filterable key
        on each item in the list. The first argument is the filterable
        value from the item, the second is the search term, and the third
        is the internal item object. The function should return true
        if the item should be included in the filtered list, or the index
        of the match in the value if it should be included with the result
        highlighted.
      custom_key_filter (unknown):
        Function used on specific keys within the item object. `customFilter`
        is skipped for columns with `customKeyFilter` specified.
      filter_keys (string, string[]):
        Array of specific keys to filter on the item.
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      expand_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      select_strategy ('single', 'page', 'all'):
        Defines the strategy of selecting items in the list. Possible
        values are: 'single' (only one item can be selected at a time),
        'page' ('Select all' button will select only items on the current
        page), 'all' ('Select all' button will select all items in the
        list).
      items (any[]):
        An array of strings or objects used for automatically generating
        children components.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3888: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      no_data_text (string):
        Text shown when no items are provided to the component.
      loading (string, boolean):
        Displays `loading` slot if set to `true`
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      item_selectable (SelectItemKey):
        Property on supplied `items` that indicates whether the item is selectable.
      show_select (boolean):
        Shows the column with checkboxes for selecting items in the list.
      initial_sort_order ('desc', 'asc'):
        Specifies the initial sort order when an unsorted column is clicked.
      sort_by (SortItem):
        Array of column keys and sort orders that determines the sort
        order of the table.
      multi_sort (enum):
        Let user sort by multiple properties/columns.  - **key**: (optional)
        when set to `ctrl`, user is required to hold a keyboard key (Ctrl
        on PC and Command on Mac) - **mode**: when user selects a new
        column to sort by, it will be set first (`prepend`) or last (`append`)
        in the sort priority. Defaults to `append` - **modifier**: (optional)
        allows user to use both multi-sort modes (`append` and `prepend`)
        simultaneously  **Note**: object notation requires at least **v3.11.0**

        Enum values: [
          boolean, { key: 'ctrl'; mode: 'prepend', 'append'; modifier: 'shift', 'alt' }
        ]
      must_sort (boolean):
        Forces sorting on the column(s).
      custom_key_sort (unknown):
        Function used on specific keys within the item object. `customSort`
        is skipped for columns with `customKeySort` specified.
      expand_on_click (boolean):
        Expands item when the row is clicked.
      show_expand (boolean):
        Shows the expand icon.
      expanded (string[]):
        Array of expanded items. Can be bound to external variable using
        **v-model:expanded**.
      group_by (SortItem):
        Defines the grouping of the table items.
      header_props (unknown):
        Pass props to the default header.
      cell_props (enum):
        An object of additional props to be passed to each `<td>` in
        the table body. Also accepts a function that will be called for
        each cell. If the same prop is defined both here and in `cellProps`
        in a headers object, the value from the headers object will be
        used.

        Enum values: [
          Record<string, any>, ((      data: Pick<        ItemKeySlot<any>,
                 'value', 'item', 'index', 'internalItem', js_fn
        ]
      disable_sort (boolean):
        Toggles rendering of sort button.
      headers (enum):
        An array of objects that each describe a header column.

        Enum values: [
          {  readonly key?:, (string & {}), 'data-table-group', 'data-table-select',
          'data-table-expand', undefined  readonly value?: SelectItemKey<any>
           readonly title?: string, undefined  readonly fixed?: boolean,
          'end', 'start', undefined  readonly align?: 'end', 'start', 'center',
          undefined  readonly width?: string, number, undefined  readonly
          minWidth?: string, number, undefined  readonly maxWidth?: string,
          number, undefined  readonly nowrap?: boolean, undefined  readonly
          intent?: number, undefined  readonly headerProps?: { readonly
          [x: string]: any }, undefined  readonly cellProps?:, { readonly
          [x: string]: any }, HeaderCellPropsFunction, undefined  readonly
          sortable?: boolean, undefined  readonly sort?: DataTableCompareFunction<any>,
          undefined  readonly sortRaw?: DataTableCompareFunction<any>,
          undefined  readonly filter?: FilterFunction, undefined  readonly
          children?: readonly any[], undefined}[]
        ]
      loading_text (string):
        Text shown when the data is loading.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      group_collapse_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableGroupHeaderRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      group_expand_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableGroupHeaderRow.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      row_props (enum):
        An object of additional props to be passed to each `<tr>` in
        the table body. Also accepts a function that will be called for
        each row.

        Enum values: [
          Record<string, any>, ((      data: Pick<ItemKeySlot<any>, 'item', 'index', js_fn
        ]
      hide_default_body (boolean):
        Hides the default body.
      hide_default_header (boolean):
        Hides the default header.
      fixed_header (boolean):
        Sticks the header to the top of the table.
      sort_asc_icon (enum):
        Icon used for ascending sort button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      sort_desc_icon (enum):
        Icon used for descending sort button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      fixed_footer (boolean):
        Use the fixed-footer prop together with the height prop to fix
        the footer to the bottom of the table.
      hover (boolean):
        Will add a hover effect to a table's row when the mouse is over it.
      striped ('odd', 'even'):
        Applies a background to either **even** or **odd** rows.
      item_height (string, number):
        Height in pixels of each item to display.
      item_key (SelectItemKey):
        The property on each item that is used as a unique key.
      update_modelValue (event):
        Emits when the component's model changes.
      update_expanded (event):
        Emits when the **expanded** prop is updated.
      update_groupBy (event):
        Emits when the **group-by** prop is updated.
      update_sortBy (event):
        Emits when the **sortBy** prop is updated.
      update_options (event):
        Emits when pagination related properties (page, itemsPerPage,
        sortBy, groupBy, search) is updated.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableVirtual", children, **kwargs)
        self._attr_names += [
            "search",
            ("model_value", "modelValue"),
            "density",
            "height",
            "width",
            "sticky",
            "tag",
            "theme",
            "color",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            ("hide_no_data", "hideNoData"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("select_strategy", "selectStrategy"),
            "items",
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            ("no_data_text", "noDataText"),
            "loading",
            "mobile",
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            ("initial_sort_order", "initialSortOrder"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
            ("header_props", "headerProps"),
            ("cell_props", "cellProps"),
            ("disable_sort", "disableSort"),
            "headers",
            ("loading_text", "loadingText"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("group_collapse_icon", "groupCollapseIcon"),
            ("group_expand_icon", "groupExpandIcon"),
            ("row_props", "rowProps"),
            ("hide_default_body", "hideDefaultBody"),
            ("hide_default_header", "hideDefaultHeader"),
            ("fixed_header", "fixedHeader"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_footer", "fixedFooter"),
            "hover",
            "striped",
            ("item_height", "itemHeight"),
            ("item_key", "itemKey"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_expanded", "update:expanded"),
            ("update_groupBy", "update:groupBy"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
        ]


class VDateInput(HtmlElement):
    """
    Vuetify's VDateInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-date-input>`_.

    Args:
      title (string):
        Specify a title text for the component.
      text (string):
        Specify content text for the component.
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      type (string):
        Sets input type.
      model_value (unknown):
        Represents the committed v-model value
      error (boolean):
        Puts the input in a manual error state.
      reverse (boolean):
        Reverses the orientation.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Width of the picker.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location (Anchor):
        Specifies the date picker's location. Can combine by using a
        space separated string.
      position ('fixed', 'static', 'relative', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Adds a border radius to the input.
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      name (string):
        Sets the component's name attribute.
      autocomplete (string):
        Helps influence browser's suggestions. Special value **suppress**
        manipulates fields `name` attribute while **off** relies on browser's
        good will to stop suggesting values. Any other value is passed
        to the native `autocomplete` on the underlying element.
      disabled (boolean):
        Removes the ability to click or target the input.
      max (unknown):
        Maximum allowed date/month (ISO 8601 format).
      min (unknown):
        Minimum allowed date/month (ISO 8601 format).
      multiple (number, boolean, (string & {}), 'range'):
        Allow the selection of multiple dates. The **range** value selects
        all dates between two selections.
      placeholder (string):
        Sets the input’s placeholder text.
      id (string):
        Sets the DOM id on the component.
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      autofocus (boolean):
        Enables autofocus.
      header (string):
        Text shown when no **display-date** is set.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      menu (boolean):
        Renders with the menu open by default.
      transition (string):
        The transition used when changing months into the future
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outside the component's input, uses the
        same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      readonly (boolean):
        Makes the picker readonly (doesn't allow to select new date).
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      append_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **append-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      dirty (boolean):
        Manually apply the dirty state styling.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      counter_value (number, js_fn):
        Function returns the counter display text.
      model_modifiers (unknown):
        **FOR INTERNAL USE ONLY**
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      cancel_text (string):
        Text for the cancel button
      ok_text (string):
        Text for the ok button
      hide_actions (boolean):
        Hide the Cancel and OK buttons, and automatically update the
        value when a date is selected.
      divided (boolean):
        Adds a divider between the header and controls.
      landscape (boolean):
        Puts the picker into landscape mode.
      hide_header (boolean):
        Hide the picker header.
      hide_title (boolean):
        Hide the picker title.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      prev_icon (enum):
        Icon used for the previous button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      next_icon (enum):
        Icon used for the next button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      month (string, number):
        Sets the month.
      year (number):
        Sets the year.
      display_format (string, js_fn):
        The format of the date that is displayed in the input. Can use
        any format [here](/features/dates/#format-options) or a custom
        function.
      update_on (('blur', 'enter')[]):
        Specifies when the text input should update the model value.
        If empty, the text field will go into read-only state.
      input_format (string):
        Format for manual date input. Use yyyy, mm, dd with separators
        '.', '-', '/' (e.g. 'yyyy-mm-dd', 'dd/mm/yyyy').
      header_color (string):
        Allows you to set a different color for the header when used
        in conjunction with the `color` prop.
      header_date_format (string):
        Allows you to customize the format of the date selection text
        that appears in the header of the calendar.
      landscape_header_width (string, number):
        Sets header width when in landscape mode.
      control_height (string, number):
        Sets the height of the controls.
      control_variant ('docked', 'modal'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      no_month_picker (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      mode_icon (enum):
        Icon used for the mode button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      month_text (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      year_text (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      view_mode ('month', 'year', 'months'):
        Sets the view mode of the date picker.
      hide_weekdays (boolean):
        Hides the weekdays.
      show_week (boolean):
        Toggles visibility of the week numbers in the body of the calendar.
      reverse_transition (string):
        The transition used when changing months into the past
      events (enum):
        Array of dates or object defining events or colors or function
        returning boolean/color/array of colors.

        Enum values: [
          string[], js_fn, boolean, string[]), Record<string, string, boolean, string[]>
        ]
      event_color (enum):
        Sets the color for event dots. It can be string (all events will
        have the same color) or `object` where attribute is the event
        date and value is boolean/color/array of colors for specified
        date or `function` taking date as a parameter and returning boolean/color/array
        of colors for that date.

        Enum values: [
          string, boolean, string[], Record<string, string, boolean, string[]>,
          js_fn, boolean, string[])
        ]
      show_adjacent_months (boolean):
        Toggles visibility of days from previous and next months.
      weekdays ((0, 1, 2, 4, 5, 6, 3)[]):
        Array of weekdays.
      weeks_in_month ('static', 'dynamic'):
        A dynamic number of weeks in a month will grow and shrink depending
        on how many days are in the month. A static number always shows
        7 weeks.
      first_day_of_week (string, number):
        Sets the first day of the week, starting with 0 for Sunday. (Note:
        not guaranteed to work when using custom date adapters.)
      first_day_of_year (string, number):
        Sets the day that determines the first week of the year, starting
        with 0 for Sunday. For ISO 8601 this should be 4. (Note: not
        guaranteed to work when using custom date adapters.)
      allowed_dates (unknown[], js_fn):
        Restricts which dates can be selected.
      weekday_format ('long', 'short', 'narrow'):
        Allows you to customize the format of the weekday string that
        appears in the body of the calendar. Uses `'narrow'` by default.
        (Note: not guaranteed to work when using custom date adapters.)
      allowed_months (number[], js_fn):
        Restricts which months can be selected.
      allowed_years (number[], js_fn):
        Restricts which years can be selected.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
      update_menu (event):
        Event that is emitted when the component's menu state changes.
      cancel (event):
        The event emitted when the user clicks the Cancel button
      save (event):
        The event emitted when the user clicks the Save button
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDateInput", children, **kwargs)
        self._attr_names += [
            "title",
            "text",
            "flat",
            "border",
            "type",
            ("model_value", "modelValue"),
            "error",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "location",
            "position",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            "name",
            "autocomplete",
            "disabled",
            "max",
            "min",
            "multiple",
            "placeholder",
            "id",
            "prefix",
            "role",
            "autofocus",
            "header",
            "label",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "menu",
            "transition",
            "counter",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "readonly",
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "loading",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
            "mobile",
            ("cancel_text", "cancelText"),
            ("ok_text", "okText"),
            ("hide_actions", "hideActions"),
            "divided",
            "landscape",
            ("hide_header", "hideHeader"),
            ("hide_title", "hideTitle"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("prev_icon", "prevIcon"),
            ("next_icon", "nextIcon"),
            "month",
            "year",
            ("display_format", "displayFormat"),
            ("update_on", "updateOn"),
            ("input_format", "inputFormat"),
            ("header_color", "headerColor"),
            ("header_date_format", "headerDateFormat"),
            ("landscape_header_width", "landscapeHeaderWidth"),
            ("control_height", "controlHeight"),
            ("control_variant", "controlVariant"),
            ("no_month_picker", "noMonthPicker"),
            ("mode_icon", "modeIcon"),
            ("month_text", "monthText"),
            ("year_text", "yearText"),
            ("view_mode", "viewMode"),
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
            ("reverse_transition", "reverseTransition"),
            "events",
            ("event_color", "eventColor"),
            ("show_adjacent_months", "showAdjacentMonths"),
            "weekdays",
            ("weeks_in_month", "weeksInMonth"),
            ("first_day_of_week", "firstDayOfWeek"),
            ("first_day_of_year", "firstDayOfYear"),
            ("allowed_dates", "allowedDates"),
            ("weekday_format", "weekdayFormat"),
            ("allowed_months", "allowedMonths"),
            ("allowed_years", "allowedYears"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_menu", "update:menu"),
            "cancel",
            "save",
        ]


class VDatePicker(HtmlElement):
    """
    Vuetify's VDatePicker component.
    See more `info and examples <https://vuetifyjs.com/api/v-date-picker>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      header (string):
        Text shown when no **display-date** is set.
      title (string):
        Specify a title text for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      max (unknown):
        Maximum allowed date/month (ISO 8601 format).
      min (unknown):
        Minimum allowed date/month (ISO 8601 format).
      multiple (number, boolean, (string & {}), 'range'):
        Allow the selection of multiple dates. The **range** value selects
        all dates between two selections.
      width (string, number):
        Width of the picker.
      theme (string):
        Specify a theme for this component and all of its children.
      active (string, string[]):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      text (string):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (string):
        The transition used when changing months into the future
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      divided (boolean):
        Adds a divider between the header and controls.
      weekdays ((0, 1, 2, 3, 4, 5, 6)[]):
        Array of weekdays.
      first_day_of_week (string, number):
        Sets the first day of the week, starting with 0 for Sunday. (Note:
        not guaranteed to work when using custom date adapters.)
      first_day_of_year (string, number):
        Sets the day that determines the first week of the year, starting
        with 0 for Sunday. For ISO 8601 this should be 4. (Note: not
        guaranteed to work when using custom date adapters.)
      weekday_format ('long', 'short', 'narrow'):
        Allows you to customize the format of the weekday string that
        appears in the body of the calendar. Uses `'narrow'` by default.
        (Note: not guaranteed to work when using custom date adapters.)
      month (string, number):
        Sets the month.
      events (enum):
        Array of dates or object defining events or colors or function
        returning boolean/color/array of colors.

        Enum values: [
          string[], js_fn, boolean, string[]), Record<string, string, boolean, string[]>
        ]
      event_color (enum):
        Sets the color for event dots. It can be string (all events will
        have the same color) or `object` where attribute is the event
        date and value is boolean/color/array of colors for specified
        date or `function` taking date as a parameter and returning boolean/color/array
        of colors for that date.

        Enum values: [
          string, boolean, string[], Record<string, string, boolean, string[]>,
          js_fn, boolean, string[])
        ]
      year (number):
        Sets the year.
      show_week (boolean):
        Toggles visibility of the week numbers in the body of the calendar.
      hide_header (boolean):
        Hides the header.
      next_icon (enum):
        Sets the icon for next month/year button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        Sets the icon for previous month/year button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      reverse_transition (string):
        The transition used when changing months into the past
      landscape (boolean):
        Changes the picker to landscape mode.
      hide_title (boolean):
        Hide the picker title.
      header_color (string):
        Allows you to set a different color for the header when used
        in conjunction with the `color` prop.
      header_date_format (string):
        Allows you to customize the format of the date selection text
        that appears in the header of the calendar.
      landscape_header_width (string, number):
        Sets header width when in landscape mode.
      control_height (string, number):
        Sets the height of the controls.
      control_variant ('docked', 'modal'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      no_month_picker (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      mode_icon (enum):
        Icon displayed next to the current month and year, toggles year
        selection when clicked.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      month_text (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      year_text (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      view_mode ('month', 'year', 'months'):
        Determines which picker in the date or month picker is being
        displayed. Allowed values: `'month'`, `'months'`, `'year'`.
      hide_weekdays (boolean):
        Hides the weekdays.
      show_adjacent_months (boolean):
        Toggles visibility of days from previous and next months.
      weeks_in_month ('static', 'dynamic'):
        A dynamic number of weeks in a month will grow and shrink depending
        on how many days are in the month. A static number always shows
        7 weeks.
      allowed_dates (unknown[], js_fn):
        Restricts which dates can be selected.
      allowed_months (number[], js_fn):
        Restricts which months can be selected.
      allowed_years (number[], js_fn):
        Restricts which years can be selected.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_month (event):
        Emitted when the month changes.
      update_year (event):
        Emitted when the year changes.
      update_viewMode (event):
        Emitted when the view mode changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePicker", children, **kwargs)
        self._attr_names += [
            "tag",
            "header",
            "title",
            "disabled",
            "height",
            "max",
            "min",
            "multiple",
            "width",
            "theme",
            "active",
            "text",
            "border",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "location",
            "position",
            "rounded",
            "tile",
            "color",
            ("model_value", "modelValue"),
            "transition",
            ("bg_color", "bgColor"),
            "divided",
            "weekdays",
            ("first_day_of_week", "firstDayOfWeek"),
            ("first_day_of_year", "firstDayOfYear"),
            ("weekday_format", "weekdayFormat"),
            "month",
            "events",
            ("event_color", "eventColor"),
            "year",
            ("show_week", "showWeek"),
            ("hide_header", "hideHeader"),
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("reverse_transition", "reverseTransition"),
            "landscape",
            ("hide_title", "hideTitle"),
            ("header_color", "headerColor"),
            ("header_date_format", "headerDateFormat"),
            ("landscape_header_width", "landscapeHeaderWidth"),
            ("control_height", "controlHeight"),
            ("control_variant", "controlVariant"),
            ("no_month_picker", "noMonthPicker"),
            ("mode_icon", "modeIcon"),
            ("month_text", "monthText"),
            ("year_text", "yearText"),
            ("view_mode", "viewMode"),
            ("hide_weekdays", "hideWeekdays"),
            ("show_adjacent_months", "showAdjacentMonths"),
            ("weeks_in_month", "weeksInMonth"),
            ("allowed_dates", "allowedDates"),
            ("allowed_months", "allowedMonths"),
            ("allowed_years", "allowedYears"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_month", "update:month"),
            ("update_year", "update:year"),
            ("update_viewMode", "update:viewMode"),
        ]


class VDatePickerControls(HtmlElement):
    """
    Vuetify's VDatePickerControls component.
    See more `info and examples <https://vuetifyjs.com/api/v-date-picker-controls>`_.

    Args:
      disabled (string, boolean, string[]):
        Removes the ability to click or target the component.
      active (string, string[]):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      text (string):
        Specify content text for the component.
      next_icon (enum):
        Icon used for the next button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        Icon used for the previous button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      control_height (string, number):
        Sets the height of the controls.
      control_variant ('docked', 'modal'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      no_month_picker (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      mode_icon (enum):
        Icon used for the mode button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      month_text (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      year_text (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      view_mode ('month', 'year', 'months'):
        Sets the view mode of the date picker.
      click_year (event):
        Event fired when clicking the date text.
      click_month (event):
        Event fired when clicking on the month.
      click_prev (event):
        Event fired when clicking the previous button.
      click_next (event):
        Event fired when clicking the next button.
      click_prev_year (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
      click_next_year (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerControls", children, **kwargs)
        self._attr_names += [
            "disabled",
            "active",
            "text",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("control_height", "controlHeight"),
            ("control_variant", "controlVariant"),
            ("no_month_picker", "noMonthPicker"),
            ("mode_icon", "modeIcon"),
            ("month_text", "monthText"),
            ("year_text", "yearText"),
            ("view_mode", "viewMode"),
        ]
        self._event_names += [
            ("click_year", "click:year"),
            ("click_month", "click:month"),
            ("click_prev", "click:prev"),
            ("click_next", "click:next"),
            ("click_prev_year", "click:prev-year"),
            ("click_next_year", "click:next-year"),
        ]


class VDatePickerHeader(HtmlElement):
    """
    Vuetify's VDatePickerHeader component.
    See more `info and examples <https://vuetifyjs.com/api/v-date-picker-header>`_.

    Args:
      header (string):
        Sets the header content.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      transition (string):
        Sets the transition when the header changes.
      click_append (event):
        Emitted when appended icon is clicked.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerHeader", children, **kwargs)
        self._attr_names += [
            "header",
            ("append_icon", "appendIcon"),
            "color",
            "transition",
        ]
        self._event_names += [
            "click",
            ("click_append", "click:append"),
        ]


class VDatePickerMonth(HtmlElement):
    """
    Vuetify's VDatePickerMonth component.
    See more `info and examples <https://vuetifyjs.com/api/v-date-picker-month>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      max (unknown):
        Sets the maximum date of the month.
      min (unknown):
        Sets the minimum date of the month.
      multiple (number, boolean, (string & {}), 'range'):
        Sets the multiple of the month.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (unknown[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (string):
        The transition used when changing months into the future
      weekdays ((0, 1, 2, 3, 4, 5, 6)[]):
        Sets the weekdays of the month.
      first_day_of_week (string, number):
        Sets the first day of the week, starting with 0 for Sunday. (Note:
        not guaranteed to work when using custom date adapters.)
      first_day_of_year (string, number):
        Sets the day that determines the first week of the year, starting
        with 0 for Sunday. For ISO 8601 this should be 4. (Note: not
        guaranteed to work when using custom date adapters.)
      weekday_format ('long', 'short', 'narrow'):
        Allows you to customize the format of the weekday string that
        appears in the body of the calendar. Uses `'narrow'` by default.
        (Note: not guaranteed to work when using custom date adapters.)
      month (string, number):
        Sets the month.
      events (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerMonth.json))

        Enum values: [
          string[], js_fn, boolean, string[]), Record<string, string, boolean, string[]>
        ]
      event_color (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerMonth.json))

        Enum values: [
          string, boolean, string[], Record<string, string, boolean, string[]>,
          js_fn, boolean, string[])
        ]
      year (string, number):
        Sets the year.
      show_week (boolean):
        Show the week number.
      reverse_transition (string):
        The transition used when changing months into the past
      hide_weekdays (boolean):
        Hide the days of the week letters.
      show_adjacent_months (boolean):
        Show adjacent months.
      weeks_in_month ('static', 'dynamic'):
        A dynamic number of weeks in a month will grow and shrink depending
        on how many days are in the month. A static number always shows
        7 weeks.
      allowed_dates (unknown[], js_fn):
        Sets the allowed dates of the month.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_month (event):
        Fired when the month changes.
      update_year (event):
        Fired when the year changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerMonth", children, **kwargs)
        self._attr_names += [
            "disabled",
            "max",
            "min",
            "multiple",
            "color",
            ("model_value", "modelValue"),
            "transition",
            "weekdays",
            ("first_day_of_week", "firstDayOfWeek"),
            ("first_day_of_year", "firstDayOfYear"),
            ("weekday_format", "weekdayFormat"),
            "month",
            "events",
            ("event_color", "eventColor"),
            "year",
            ("show_week", "showWeek"),
            ("reverse_transition", "reverseTransition"),
            ("hide_weekdays", "hideWeekdays"),
            ("show_adjacent_months", "showAdjacentMonths"),
            ("weeks_in_month", "weeksInMonth"),
            ("allowed_dates", "allowedDates"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_month", "update:month"),
            ("update_year", "update:year"),
        ]


class VDatePickerMonths(HtmlElement):
    """
    Vuetify's VDatePickerMonths component.
    See more `info and examples <https://vuetifyjs.com/api/v-date-picker-months>`_.

    Args:
      height (string, number):
        Sets the height for the component.
      max (unknown):
        Sets the maximum selectable date. Months after this date will be disabled.
      min (unknown):
        Sets the minimum selectable date. Months before this date will be disabled.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      year (number):
        Sets the year for the given months.
      allowed_months (number[], js_fn):
        Restricts which months can be selected.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerMonths", children, **kwargs)
        self._attr_names += [
            "height",
            "max",
            "min",
            "color",
            ("model_value", "modelValue"),
            "year",
            ("allowed_months", "allowedMonths"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VDatePickerYears(HtmlElement):
    """
    Vuetify's VDatePickerYears component.
    See more `info and examples <https://vuetifyjs.com/api/v-date-picker-years>`_.

    Args:
      height (string, number):
        Sets the height for the component.
      max (unknown):
        Sets the maximum date of the month.
      min (unknown):
        Sets the minimum date of the month.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      allowed_years (number[], js_fn):
        Restricts which years can be selected.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerYears", children, **kwargs)
        self._attr_names += [
            "height",
            "max",
            "min",
            "color",
            ("model_value", "modelValue"),
            ("allowed_years", "allowedYears"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VDefaultsProvider(HtmlElement):
    """
    Vuetify's VDefaultsProvider component.
    See more `info and examples <https://vuetifyjs.com/api/v-defaults-provider>`_.

    Args:
      reset (string, number):
        Reset the default values up the nested chain by {n} amount.
      disabled (boolean):
        Turns off all calculations of new default values for improved
        performance in situations where defaults propagation isn't necessary.
      root (string, boolean):
        Force current defaults to match the application root defaults.
      scoped (boolean):
        Prevents the ability for default values to be inherited from parent components.
      defaults ({  global: Record<string, unknown>  [string]: Record<string, unknown>}):
        Specify new default prop values for components. Keep in mind
        that this will be merged with previously defined values.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDefaultsProvider", children, **kwargs)
        self._attr_names += [
            "reset",
            "disabled",
            "root",
            "scoped",
            "defaults",
        ]
        self._event_names += []


class VDialog(HtmlElement):
    """
    Vuetify's VDialog component.
    See more `info and examples <https://vuetifyjs.com/api/v-dialog>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      location (Anchor):
        Specifies the anchor point for positioning the component, using
        directional cues to align it either horizontally, vertically,
        or both..
      absolute (boolean):
        Applies **position: absolute** to the content element.
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          {      component: ComponentPublicInstanceConstructor<
          CreateComponentPublicInstanceWithMixins<          {} & { target?:
          HTMLElement, [x: number, y: number], undefined } & {
             $children?:, VNodeChild, { $stable?: boolean, undefined },
          js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn, [x: number, y: number], undefined } & {
                     $children?:, VNodeChild, { $stable?: boolean, undefined
          }, js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn, [x: number, y: number], undefined } & {
                     $children?:, VNodeChild, { $stable?: boolean, undefined
          }, js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn
        ]
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      fullscreen (boolean):
        Changes layout for fullscreen display.
      scrollable (boolean):
        When set to true, expects a `v-card` and a `v-card-text` component
        with a designated height. For more information, check out the
        [scrollable example](/components/dialogs#scrollable).
      close_on_back (boolean):
        Closes the overlay content when the browser's back button is
        pressed or `$router.back()` is called, cancelling the original
        navigation. `persistent` overlays will cancel navigation and
        animate as if they were clicked outside instead of closing.
      contained (boolean):
        Limits the size of the component and scrim to its offset parent.
        Implies `absolute` and `attach`. (Note: The parent element must
        have position: relative.).
      content_class (any):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      content_props (any):
        Apply custom properties to the content.
      opacity (string, number):
        Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
      no_click_animation (boolean):
        Disables the bounce effect when clicking outside of a `v-dialog`'s
        content when using the **persistent** prop.
      persistent (boolean):
        Clicking outside of the element or pressing **esc** key will not deactivate it.
      scrim (string, boolean):
        Accepts true/false to enable background, and string to define color.
      z_index (string, number):
        The z-index used for the component.
      target (enum):
        For locationStrategy="connected", specify an element or array
        of x,y coordinates that the overlay should position itself relative
        to. This will be the activator element by default.

        Enum values: [
          Element, (string & {}), 'parent', 'cursor', ComponentPublicInstance,
          [number, number]
        ]
      activator_props (unknown):
        Apply custom properties to the activator.
      open_on_click (boolean):
        Activate the component when the activator is clicked.
      open_on_hover (boolean):
        Designates whether component should activate when its activator is hovered.
      open_on_focus (boolean):
        Activate the component when the activator is focused.
      close_on_content_click (boolean):
        Closes component when you click on its content.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        Increases distance from the target. When passed as a pair of
        numbers, the second value shifts anchor along the side and away
        from the target.
      stick_to_target (boolean):
        Enables the overlay content to go off-screen when scrolling.
      viewport_margin (string, number):
        Sets custom viewport margin for the overlay content
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
      retain_focus (boolean):
        Captures and keeps focus within the content element when using
        **Tab** and **Shift**+**Tab**. Recommended to be `false` when
        using external tools that require focus such as TinyMCE or vue-clipboard.
      capture_focus (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/focusTrap.json))
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      afterEnter (event):
        Event that fires after the overlay has finished transitioning in.
      afterLeave (event):
        Event that fires after the overlay has finished transitioning out.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialog", children, **kwargs)
        self._attr_names += [
            "disabled",
            "height",
            "width",
            "theme",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "location",
            "absolute",
            ("model_value", "modelValue"),
            "transition",
            "activator",
            "fullscreen",
            "scrollable",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            "persistent",
            "scrim",
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "eager",
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            ("stick_to_target", "stickToTarget"),
            ("viewport_margin", "viewportMargin"),
            ("scroll_strategy", "scrollStrategy"),
            ("retain_focus", "retainFocus"),
            ("capture_focus", "captureFocus"),
            "attach",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "afterEnter",
            "afterLeave",
        ]


class VDialogBottomTransition(HtmlElement):
    """
    Vuetify's VDialogBottomTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-dialog-bottom-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialogBottomTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VDialogTopTransition(HtmlElement):
    """
    Vuetify's VDialogTopTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-dialog-top-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialogTopTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VDialogTransition(HtmlElement):
    """
    Vuetify's VDialogTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-dialog-transition>`_.

    Args:
      target (HTMLElement, [number, number]):
        Sets the target element for the transition.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialogTransition", children, **kwargs)
        self._attr_names += [
            "target",
        ]
        self._event_names += []


class VDivider(HtmlElement):
    """
    Vuetify's VDivider component.
    See more `info and examples <https://vuetifyjs.com/api/v-divider>`_.

    Args:
      length (string, number):
        Sets the dividers length. Default unit is px.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('dotted', 'dashed', 'solid', 'double'):
        Applies `border-style`.
      inset (boolean):
        Adds indentation (72px) for **normal** dividers, reduces max
        height for **vertical**.
      opacity (string, number):
        Sets the component's opacity value
      vertical (boolean):
        Displays dividers vertically.
      gradient (boolean):
        Adds fading effect for both sides.
      thickness (string, number):
        Sets the dividers thickness. Default unit is px.
      content_offset (string, number, (string, number)[]):
        Increases content spacing from the lines. When passed as an array,
        the second value shifts slot content down (or right in vertical
        mode).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDivider", children, **kwargs)
        self._attr_names += [
            "length",
            "theme",
            "color",
            "variant",
            "inset",
            "opacity",
            "vertical",
            "gradient",
            "thickness",
            ("content_offset", "contentOffset"),
        ]
        self._event_names += []


class VEmptyState(HtmlElement):
    """
    Vuetify's VEmptyState component.
    See more `info and examples <https://vuetifyjs.com/api/v-empty-state>`_.

    Args:
      title (string):
        Specify a title text for the component.
      height (string, number):
        Sets the height for the component.
      size (string, number):
        The size used to control the dimensions of the media element
        inside the component. Can be specified as a number or a string
        (e.g., '50%', '100px').
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      text (string):
        Specify content text for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      href (string):
        The URL the action button links to.
      to (string):
        The URL the action button links to.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      image (string):
        Apply a specific image using [v-img](/components/images/).
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      headline (string):
        A large headline often used for 404 pages.
      action_text (string):
        The text used for the action button.
      justify ('start', 'end', 'center'):
        Control the justification of the text.
      text_width (string, number):
        Sets the width of the text container.
      click_action (event):
        Event emitted when the action button is clicked.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VEmptyState", children, **kwargs)
        self._attr_names += [
            "title",
            "height",
            "size",
            "width",
            "theme",
            "text",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "href",
            "to",
            "color",
            "icon",
            "image",
            ("bg_color", "bgColor"),
            "headline",
            ("action_text", "actionText"),
            "justify",
            ("text_width", "textWidth"),
        ]
        self._event_names += [
            ("click_action", "click:action"),
        ]


class VExpandTransition(HtmlElement):
    """
    Vuetify's VExpandTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-expand-transition>`_.

    Args:
      mode ('default', 'in-out', 'out-in'):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpandTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
        ]
        self._event_names += []


class VExpandXTransition(HtmlElement):
    """
    Vuetify's VExpandXTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-expand-x-transition>`_.

    Args:
      mode ('default', 'in-out', 'out-in'):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpandXTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
        ]
        self._event_names += []


class VExpansionPanel(HtmlElement):
    """
    Vuetify's VExpansionPanel component.
    See more `info and examples <https://vuetifyjs.com/api/v-expansion-panel>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      title (string):
        Specify a title text for the component.
      disabled (boolean):
        Disables the expansion-panel content.
      height (string, number):
        Sets the height for the component.
      value (any):
        Controls the opened/closed state of content.
      width (string, number):
        Sets the width for the component.
      readonly (boolean):
        Makes the expansion panel content read only.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      text (string):
        Specify content text for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      static (boolean):
        Remove title size expansion when selected.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      expand_icon (enum):
        Icon used when the expansion panel is in a expandable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon used when the expansion panel is in a collapsable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_actions (boolean):
        Hide the expand icon in the content title.
      focusable (boolean):
        Makes the expansion panel content focusable.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanel", children, **kwargs)
        self._attr_names += [
            "tag",
            "title",
            "disabled",
            "height",
            "value",
            "width",
            "readonly",
            "ripple",
            "text",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            ("selected_class", "selectedClass"),
            "static",
            "rounded",
            "tile",
            "color",
            ("bg_color", "bgColor"),
            "eager",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("hide_actions", "hideActions"),
            "focusable",
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VExpansionPanelText(HtmlElement):
    """
    Vuetify's VExpansionPanelText component.
    See more `info and examples <https://vuetifyjs.com/api/v-expansion-panel-text>`_.

    Args:
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanelText", children, **kwargs)
        self._attr_names += [
            "eager",
        ]
        self._event_names += []


class VExpansionPanelTitle(HtmlElement):
    """
    Vuetify's VExpansionPanelTitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-expansion-panel-title>`_.

    Args:
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      readonly (boolean):
        Makes the expansion panel content read only.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      static (boolean):
        Remove title size expansion when selected.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      expand_icon (enum):
        Icon used when the expansion panel is in a expandable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon used when the expansion panel is in a collapsable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_actions (boolean):
        Hide the expand icon in the content title.
      focusable (boolean):
        Makes the expansion panel headers focusable.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanelTitle", children, **kwargs)
        self._attr_names += [
            "height",
            "width",
            "readonly",
            "ripple",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "static",
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("hide_actions", "hideActions"),
            "focusable",
        ]
        self._event_names += []


class VExpansionPanels(HtmlElement):
    """
    Vuetify's VExpansionPanels component.
    See more `info and examples <https://vuetifyjs.com/api/v-expansion-panels>`_.

    Args:
      flat (boolean):
        Removes the expansion-panel's elevation and borders.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Puts all children components into a disabled state.
      max (number):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allows one to select multiple items.
      theme (string):
        Specify a theme for this component and all of its children.
      readonly (boolean):
        Makes the entire expansion panel read only.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      static (boolean):
        Remove title size expansion when selected.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes the border-radius.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('default', 'inset', 'accordion', 'popout'):
        Applies a distinct style to the component.
      model_value (any):
        Controls expanded panel(s). Defaults to an empty array when using
        **multiple** prop. It is recommended to set unique `value` prop
        for the panels inside, otherwise index is used instead.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      expand_icon (enum):
        Icon used when the expansion panel is in a expandable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon used when the expansion panel is in a collapsable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_actions (boolean):
        Hide the expand icon in the content title.
      focusable (boolean):
        Makes the expansion-panel headers focusable.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanels", children, **kwargs)
        self._attr_names += [
            "flat",
            "tag",
            "disabled",
            "max",
            "multiple",
            "theme",
            "readonly",
            "ripple",
            "elevation",
            ("selected_class", "selectedClass"),
            "static",
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "mandatory",
            "eager",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("hide_actions", "hideActions"),
            "focusable",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VFab(HtmlElement):
    """
    Vuetify's VFab component.
    See more `info and examples <https://vuetifyjs.com/api/v-fab>`_.

    Args:
      symbol (any):
        The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
        used to hook into group functionality for components like [v-btn-toggle](/components/btn-toggle)
        and [v-bottom-navigation](/components/bottom-navigations/).
      flat (boolean):
        Removes the button box shadow. This is different than using the 'flat' variant.
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      name (string):
        Assign a specific name for layout registration.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      width (string, number):
        Sets the width for the component.
      layout (boolean):
        If true, will effect layout dimensions based on size and position.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      active_color (string):
        The applied color when the component is in an active state.
      base_color (string):
        Sets the color of component when not focused.
      prepend_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend**
        slot before default content.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      block (boolean):
        Expands the button to 100% of available space.
      readonly (boolean):
        Puts the button in a readonly state. Cannot be clicked or navigated
        to by keyboard.
      slim (boolean):
        Reduces padding to 0 8px.
      stacked (boolean):
        Displays the button as a flex-column.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      text (string, number, boolean):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      location (Anchor):
        The location of the fab relative to the layout. Only works when using **app**.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      absolute (boolean):
        Applies **position: absolute** to the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/)
        component. The button will become _round_.

        Enum values: [
          boolean, string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      order (string, number):
        Adjust the order of the component in relation to its registration order.
      offset (boolean):
        Translates the Fab up or down, depending on if location is set
        to **top** or **bottom**.
      app (boolean):
        If true, attaches to the closest layout and positions according
        to the value of **location**.
      appear (boolean):
        Used to control the animation of the FAB.
      extended (boolean):
        An alternate style for the FAB that expects text.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFab", children, **kwargs)
        self._attr_names += [
            "symbol",
            "flat",
            "replace",
            "tag",
            "name",
            "disabled",
            "height",
            "size",
            "value",
            "width",
            "layout",
            "theme",
            "active",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "block",
            "readonly",
            "slim",
            "stacked",
            "ripple",
            "text",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            ("selected_class", "selectedClass"),
            "loading",
            "location",
            "position",
            "absolute",
            "rounded",
            "tile",
            "href",
            "exact",
            "to",
            "color",
            "variant",
            "icon",
            ("model_value", "modelValue"),
            "transition",
            "order",
            "offset",
            "app",
            "appear",
            "extended",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VFabTransition(HtmlElement):
    """
    Vuetify's VFabTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-fab-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFabTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VFadeTransition(HtmlElement):
    """
    Vuetify's VFadeTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-fade-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFadeTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VField(HtmlElement):
    """
    Vuetify's VField component.
    See more `info and examples <https://vuetifyjs.com/api/v-field>`_.

    Args:
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      reverse (boolean):
        Reverses the orientation.
      error (boolean):
        Puts the input in a manual error state.
      details (boolean):
        Controls whether the field generates an `aria-describedby` attribute
        for accessibility.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the input.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      base_color (string):
        Sets the color of the input when it is not focused.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      focused (boolean):
        Forces a focused state styling on the component.
      append_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **append-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      dirty (boolean):
        Manually apply the dirty state styling.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VField", children, **kwargs)
        self._attr_names += [
            "flat",
            "reverse",
            "error",
            "details",
            "label",
            "disabled",
            "id",
            "theme",
            "active",
            ("base_color", "baseColor"),
            "loading",
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            "focused",
            ("append_inner_icon", "appendInnerIcon"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
        ]


class VFieldLabel(HtmlElement):
    """
    Vuetify's VFieldLabel component.
    See more `info and examples <https://vuetifyjs.com/api/v-field-label>`_.

    Args:
      floating (boolean):
        Elevates the label above the slotted content.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFieldLabel", children, **kwargs)
        self._attr_names += [
            "floating",
        ]
        self._event_names += []


class VFileInput(HtmlElement):
    """
    Vuetify's VFileInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-file-input>`_.

    Args:
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      reverse (boolean):
        Reverses the orientation.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the input.
      multiple (boolean):
        Adds the **multiple** attribute to the input, allowing multiple file selections.
      width (string, number):
        Sets the width for the component.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts input in readonly state.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      model_value (File, File[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      chips (boolean):
        Changes display of selections to chips.
      counter (boolean):
        Displays the number of selected files.
      append_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **append-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      dirty (boolean):
        Manually apply the dirty state styling.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      counter_size_string (string):
        The text displayed when using the **counter** and **show-size**
        props. Can also be customized globally on the [internationalization
        page](/customization/internationalization).
      counter_string (string):
        The text displayed when using the **counter** prop. Can also
        be customized globally on the [internationalization page](/customization/internationalization).
      hide_input (boolean):
        Display the icon only without the input (file names).
      show_size (boolean, 1000, 1024):
        Sets the displayed size of selected file(s). When using **true**
        will default to _1000_ displaying (**kB, MB, GB**) while _1024_
        will display (**KiB, MiB, GiB**).
      truncate_length (string, number):
        The length of a filename before it is truncated with ellipsis.
      filter_by_type (string):
        Make the input accept only files matched by one or more [unique
        file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#Unique_file_type_specifiers).
        Applies to drag & drop and selecting folders. Emits `rejected`
        event when some files do not pass through to make it possible
        to notify user and deliver better user experience.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
      click_control (event):
        Emitted when the main input is clicked.
      mousedown_control (event):
        Event that is emitted when using mousedown on the main control area.
      rejected (event):
        Emitted when some of the files from user input, drop or folder
        selection did not pass through `strict-accept` filter.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFileInput", children, **kwargs)
        self._attr_names += [
            "flat",
            "reverse",
            "name",
            "error",
            "label",
            "disabled",
            "multiple",
            "width",
            "id",
            "theme",
            "active",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "loading",
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "direction",
            "messages",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            "chips",
            "counter",
            ("append_inner_icon", "appendInnerIcon"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            ("counter_size_string", "counterSizeString"),
            ("counter_string", "counterString"),
            ("hide_input", "hideInput"),
            ("show_size", "showSize"),
            ("truncate_length", "truncateLength"),
            ("filter_by_type", "filterByType"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("click_control", "click:control"),
            ("mousedown_control", "mousedown:control"),
            "rejected",
        ]


class VFileUpload(HtmlElement):
    """
    Vuetify's VFileUpload component.
    See more `info and examples <https://vuetifyjs.com/api/v-file-upload>`_.

    Args:
      length (string, number):
        Sets the dividers length. Default unit is px.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      name (string):
        Sets the component's name attribute.
      title (string):
        Specify a title text for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      multiple (boolean):
        Allows multiple files to be uploaded.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      model_value (File, File[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      opacity (string, number):
        Sets the component's opacity value
      scrim (string, boolean):
        Determines whether an overlay is used when hovering over the
        component with files. Accepts true/false to enable background,
        and string to define color.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      subtitle (string):
        Specify a subtitle text for the component.
      clearable (boolean):
        Allows for the component to be cleared.
      thickness (string, number):
        Sets the dividers thickness. Default unit is px.
      show_size (boolean):
        Shows the size of the file.
      filter_by_type (string):
        Make the input accept only files matched by one or more [unique
        file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#Unique_file_type_specifiers).
        Applies to drag & drop and selecting folders. Emits `rejected`
        event when some files do not pass through to make it possible
        to notify user and deliver better user experience.
      browse_text (string):
        Text for the browse button.
      divider_text (string):
        Text in the divider.
      hide_browse (boolean):
        Hides the browse button.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      rejected (event):
        Emitted when some of the files from user input, drop or folder
        selection did not pass through `strict-accept` filter.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFileUpload", children, **kwargs)
        self._attr_names += [
            "length",
            "tag",
            "name",
            "title",
            "disabled",
            "height",
            "multiple",
            "width",
            "theme",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "location",
            "position",
            "rounded",
            "tile",
            "color",
            "icon",
            ("model_value", "modelValue"),
            "opacity",
            "scrim",
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "subtitle",
            "clearable",
            "thickness",
            ("show_size", "showSize"),
            ("filter_by_type", "filterByType"),
            ("browse_text", "browseText"),
            ("divider_text", "dividerText"),
            ("hide_browse", "hideBrowse"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "rejected",
        ]


class VFileUploadItem(HtmlElement):
    """
    Vuetify's VFileUploadItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-file-upload-item>`_.

    Args:
      title (string, number, boolean):
        Generates a `v-list-item-title` component with the supplied value.
        Note that this overrides the native [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title)
        attribute, that must be set with `v-bind:title.attr` instead.
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the href or to prop.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control when in an **active**
        state or **input-value** is **true** - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors),
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      value (any):
        The value used for selection. Obtained from [`v-list`](/api/v-list)'s
        `v-model:selected` when the item is selected.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      subtitle (string, number, boolean):
        Specify a subtitle text for the component.
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        Deprecated, use `color` instead.
      active_class (string):
        The class applied to the component when it matches the current
        route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class)
        on the [vue-router](https://router.vuejs.org/) documentation.
      lines (false, 'one', 'two', 'three'):
        The line declaration specifies the minimum height of the item
        and can also be controlled from v-list with the same prop.
      slim (boolean):
        Reduces horizontal spacing for badges, icons, tooltips, and avatars
        to create a more compact visual representation.
      prepend_gap (string, number):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VListItem.json))
      nav (boolean):
        Reduces the width v-list-item takes up as well as adding a border radius.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prepend_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend**
        slot before default content.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      clearable (boolean):
        Allows for the component to be cleared.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      file (File):
        The file object uploaded
      file_icon (string):
        The icon prepending each uploaded file. This will be a preview
        image if the file is an image.
      show_size (boolean):
        Show the size of the file
      append_avatar (string):
        Appends a [v-avatar](/components/avatars/) component after default
        content in the **append** slot.
      prepend_avatar (string):
        Prepends a [v-avatar](/components/avatars/) component in the
        **prepend** slot before default content.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      click_remove (event):
        Emitted when the remove icon is clicked
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFileUploadItem", children, **kwargs)
        self._attr_names += [
            "title",
            "replace",
            "link",
            "border",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            "disabled",
            "value",
            "exact",
            "subtitle",
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            ("active_class", "activeClass"),
            "lines",
            "slim",
            ("prepend_gap", "prependGap"),
            "nav",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "clearable",
            "active",
            "file",
            ("file_icon", "fileIcon"),
            ("show_size", "showSize"),
            ("append_avatar", "appendAvatar"),
            ("prepend_avatar", "prependAvatar"),
            "ripple",
            "href",
            "to",
        ]
        self._event_names += [
            "click",
            ("click_remove", "click:remove"),
        ]


class VFooter(HtmlElement):
    """
    Vuetify's VFooter component.
    See more `info and examples <https://vuetifyjs.com/api/v-footer>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      name (string):
        Assign a specific name for layout registration.
      height (string, number):
        Sets the height for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      absolute (boolean):
        Applies **position: absolute** to the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      order (string, number):
        Adjust the order of the component in relation to its registration order.
      app (boolean):
        Determines the position of the footer. If true, the footer would
        be given a fixed position at the bottom of the viewport. If false,
        the footer is set to the bottom of the page.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFooter", children, **kwargs)
        self._attr_names += [
            "tag",
            "name",
            "height",
            "theme",
            "border",
            "elevation",
            "absolute",
            "rounded",
            "tile",
            "color",
            "order",
            "app",
        ]
        self._event_names += []


class VForm(HtmlElement):
    """
    Vuetify's VForm component.
    See more `info and examples <https://vuetifyjs.com/api/v-form>`_.

    Args:
      disabled (boolean):
        Puts all children inputs into a disabled state.
      readonly (boolean):
        Puts all children inputs into a readonly state.
      model_value (boolean):
        The value representing the validity of the form. If the value
        is `null` then no validation has taken place yet, or the form
        has been reset. Otherwise the value will be a `boolean` that
        indicates if validation has passed or not.
      validate_on (enum):
        Changes the events in which validation occurs.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      fast_fail (boolean):
        Stop validation as soon as any rules fail.
      submit (event):
        Emitted when form is submitted.
      update_modelValue (event):
        Event emitted when the form's validity changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VForm", children, **kwargs)
        self._attr_names += [
            "disabled",
            "readonly",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("fast_fail", "fastFail"),
        ]
        self._event_names += [
            "submit",
            ("update_modelValue", "update:modelValue"),
        ]


class VHotkey(HtmlElement):
    """
    Vuetify's VHotkey component.
    See more `info and examples <https://vuetifyjs.com/api/v-hotkey>`_.

    Args:
      keys (string):
        String representing keyboard shortcuts to display. Supports multiple
        formats: - **Single keys:** `"k"`, `"enter"`, `"escape"` - **Key
        combinations:** `"ctrl+k"`, `"meta+shift+p"`, `"alt+arrowup"`
        - **Sequential actions:** `"ctrl+k-then-p"` (use dash for 'then'
        relationships) - **Multiple shortcuts:** `"ctrl+k meta+p"` (space-separated
        for alternative shortcuts)  Supports platform-aware key names
        like `meta` (becomes Cmd on Mac, Ctrl on PC) and `alt` (becomes
        Option on Mac).
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Controls the visual style and presentation of the hotkey component.
        Supports standard Vuetify variants plus a special contained variant:
         **Standard Variants** (apply styling to individual key elements):
        - **elevated (default):** Raised appearance with shadow, good
        for standalone hotkey displays - **flat:** Solid background without
        shadow, clean and minimal - **tonal:** Subtle tinted background
        without border, balances visibility with restraint - **outlined:**
        Border-only styling without elevation, lightweight and unobtrusive
        - **text:** Minimal styling with text color emphasis only, blends
        with content - **plain:** No background or border, most subtle
        option  **Special Variant** (different visual structure): - **contained:**
        Follows MDN's nested `<kbd>` pattern - wraps all keys in a single
        styled container with unstyled nested elements. Creates a cohesive
        visual unit that clearly groups related keys together. Cannot
        be combined with standard variants. Ideal for complex key combinations
        where you want to show the entire sequence as one unit.

        Enum values: [
          'text', 'flat', 'elevated', 'tonal', 'outlined', 'plain', 'contained'
        ]
      disabled (boolean):
        Applies a disabled visual state to the component.
      prefix (string):
        Text to display before the hotkey.
      suffix (string):
        Text to display after the hotkey.
      display_mode ('symbol', 'text', 'icon'):
        Controls how keyboard keys are visually represented. Affects
        the entire component's appearance: - **icon:** Uses SVG icons
        for keys when appropriate (default) - **symbol:** Uses Unicode
        symbols (⌘, ⌃, ⇧, ⌥) - Allows you to manage presentation of modifier
        keys with fonts - **text:** Uses full text labels (Command, Control,
        Shift, Alt) - most accessible and descriptive
      key_map (unknown):
        Custom key mapping object that defines how individual keys should
        be displayed. Users can import and modify the exported `hotkeyMap`
        to create custom configurations. Each key maps to a `PlatformKeyConfig`
        object with:  ```typescript {   mac?: { symbol?: string, icon?:
        string, text: string },   default: { symbol?: string, icon?:
        string, text: string } } ```  **Usage Example:** ```typescript
        import { hotkeyMap } from 'vuetify/labs/VHotkey'  const customKeyMap
        = {   ...hotkeyMap,   'custom-key': {     default: { text: 'Custom',
        icon: 'custom-icon' },     mac: { text: 'Custom', symbol: '⚡'
        }   } } ```  This enables: - **Custom key definitions:** Add
        support for application-specific keys - **Localization:** Override
        text representations for different languages - **Brand customization:**
        Change how modifier keys appear - **Platform-specific styling:**
        Different representations for Mac vs other platforms  Recommended
        to set at the application level via component defaults rather
        than per-instance for consistency.
      platform ('auto', 'pc', 'mac'):
        Controls platform-specific rendering behavior for keyboard shortcuts.
        Accepts three values: - **`'auto'` (default):** Automatically
        detects the user's platform based on user agent and renders appropriately
        - **`'mac'`:** Forces Mac-style rendering (Command symbols, icons,
        Option key, etc.) - **`'pc'`:** Forces PC-style rendering (Ctrl
        text, Alt key, etc.)  This is particularly useful for: - **Cross-platform
        testing:** Verify how shortcuts appear on different platforms
        - **Design consistency:** Ensure specific platform rendering
        in demos and prototypes - **Development workflow:** Test platform-specific
        behaviors without switching devices - **Documentation:** Show
        platform-specific examples in help content
      inline (boolean):
        Optimizes the component for seamless integration within text
        content and documentation. Applies compact styling with baseline
        alignment, constrained height (1lh), and responsive typography
        that inherits from parent text. Ideal for help documentation,
        tooltips, and instructional content. When using multiple inline
        hotkeys in the same paragraph, increase line-height to prevent
        visual overlap on text wrapping.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VHotkey", children, **kwargs)
        self._attr_names += [
            "keys",
            "border",
            "elevation",
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            "disabled",
            "prefix",
            "suffix",
            ("display_mode", "displayMode"),
            ("key_map", "keyMap"),
            "platform",
            "inline",
        ]
        self._event_names += []


class VHover(HtmlElement):
    """
    Vuetify's VHover component.
    See more `info and examples <https://vuetifyjs.com/api/v-hover>`_.

    Args:
      disabled (boolean):
        Removes hover functionality.
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VHover", children, **kwargs)
        self._attr_names += [
            "disabled",
            ("model_value", "modelValue"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VIcon(HtmlElement):
    """
    Vuetify's VIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-icon>`_.

    Args:
      end (boolean):
        Applies margin at the start of the component.
      start (boolean):
        Applies margin at the end of the component.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      disabled (boolean):
        Removes the ability to click or target the component.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      opacity (string, number):
        Sets the component's opacity value
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VIcon", children, **kwargs)
        self._attr_names += [
            "end",
            "start",
            "icon",
            "tag",
            "theme",
            "color",
            "disabled",
            "size",
            "opacity",
        ]
        self._event_names += []


class VIconBtn(HtmlElement):
    """
    Vuetify's VIconBtn component.
    See more `info and examples <https://vuetifyjs.com/api/v-icon-btn>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      size (string, number):
        Sets the height and width of the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        When undefined (default), the component utilizes its default
        variant, otherwise it will use the activeVariant if active is
        true, or the baseVariant if active is false.
      active_color (string):
        The applied color when the component is in an active state.
      readonly (boolean):
        Puts the button in a readonly state. Cannot be clicked or navigated
        to by keyboard.
      text (string, number, boolean):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      loading (boolean):
        Displays circular progress bar in place of the icon.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      opacity (string, number):
        Sets the component's opacity value
      sizes (enum):
        An array of tuples that define the button sizes for each named size.

        Enum values: [
          ['small', 'default', 'x-small', 'large', 'x-large', number][]
        ]
      icon_color (string):
        Explicit color applied to the icon.
      base_variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        When active is a boolean, this variant is used when active is false.
      hide_overlay (boolean):
        Hides overlay from being displayed when active or focused.
      rotate (string, number):
        The rotation of the icon in degrees.
      icon_sizes (enum):
        An array of tuples that define the icon sizes for each named size.

        Enum values: [
          ['small', 'default', 'x-small', 'large', 'x-large', number][]
        ]
      icon_size (string, number):
        The specific size of the icon, can use named sizes.
      active_icon (enum):
        When active is a boolean, this icon is used when active is true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      active_variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        When active is a boolean, this variant is used when active is true.
      update_active (event):
        Event that is emitted when the active state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VIconBtn", children, **kwargs)
        self._attr_names += [
            "tag",
            "disabled",
            "height",
            "size",
            "width",
            "theme",
            "active",
            ("active_color", "activeColor"),
            "readonly",
            "text",
            "border",
            "elevation",
            "loading",
            "rounded",
            "tile",
            "color",
            "variant",
            "icon",
            "opacity",
            "sizes",
            ("icon_color", "iconColor"),
            ("base_variant", "baseVariant"),
            ("hide_overlay", "hideOverlay"),
            "rotate",
            ("icon_sizes", "iconSizes"),
            ("icon_size", "iconSize"),
            ("active_icon", "activeIcon"),
            ("active_variant", "activeVariant"),
        ]
        self._event_names += [
            ("update_active", "update:active"),
        ]


class VImg(HtmlElement):
    """
    Vuetify's VImg component.
    See more `info and examples <https://vuetifyjs.com/api/v-img>`_.

    Args:
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      position (string):
        Applies [object-position](https://developer.mozilla.org/en-US/docs/Web/CSS/object-position)
        styles to the image and placeholder elements.
      absolute (boolean):
        Applies position: absolute to the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      alt (string):
        Alternate text for screen readers. Leave empty for decorative images.
      src (enum):
        The image URL. This prop is mandatory.

        Enum values: [
          string, { src: string; srcset: string; lazySrc: string; aspect: number }
        ]
      draggable (boolean, 'true', 'false'):
        Controls the `draggable` behavior of the image. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable).
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      content_class (any):
        Apply a custom class to the internal content element.
      transition (enum):
        The transition to use when switching from `lazy-src` to `src`.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      options (IntersectionObserverInit):
        Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
        constructor.
      inline (boolean):
        Display as an inline element instead of a block, also disables flex-grow.
      cover (boolean):
        Resizes the background image to cover the entire container.
      gradient (string):
        The gradient to apply to the image. Only supports [linear-gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient)
        syntax, anything else should be done with classes.
      lazy_src (string):
        Something to show while waiting for the main image to load, typically
        a small base64-encoded thumbnail. Has a slight blur filter applied.
          NOTE: This prop has no effect unless either `height` or `aspect-ratio`
        are provided.
      sizes (string):
        For use with `srcset`, see [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes).
      srcset (string):
        A set of alternate images to use based on device size. [Read
        more...](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset).
      aspect_ratio (string, number):
        Calculated as `width/height`, so for a 1920x1080px image this
        will be `1.7778`. Will be calculated automatically if omitted.
      crossorigin ('', 'anonymous', 'use-credentials'):
        Specify that images should be fetched with CORS enabled [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#crossorigin)
      referrerpolicy (enum):
        Define which referrer is sent when fetching the resource [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#referrerpolicy)

        Enum values: [
          'origin', 'no-referrer', 'no-referrer-when-downgrade', 'origin-when-cross-origin',
          'same-origin', 'strict-origin', 'strict-origin-when-cross-origin',
          'unsafe-url'
        ]
      error (event):
        Emitted if the image fails to load.
      load (event):
        Emitted when the image is loaded.
      loadstart (event):
        Emitted when the image starts to load.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VImg", children, **kwargs)
        self._attr_names += [
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "position",
            "absolute",
            "rounded",
            "tile",
            "color",
            "alt",
            "src",
            "draggable",
            "eager",
            ("content_class", "contentClass"),
            "transition",
            "options",
            "inline",
            "cover",
            "gradient",
            ("lazy_src", "lazySrc"),
            "sizes",
            "srcset",
            ("aspect_ratio", "aspectRatio"),
            "crossorigin",
            "referrerpolicy",
        ]
        self._event_names += [
            "error",
            "load",
            "loadstart",
        ]


class VInfiniteScroll(HtmlElement):
    """
    Vuetify's VInfiniteScroll component.
    See more `info and examples <https://vuetifyjs.com/api/v-infinite-scroll>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      mode ('intersect', 'manual'):
        Specifies if content should load automatically when scrolling
        (**intersect**) or manually (**manual**).
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      direction ('horizontal', 'vertical'):
        Specifies if scroller is **vertical** or **horizontal**.
      side ('start', 'end', 'both'):
        Specifies the side where new content should appear. Either the
        **start**, **end**, or **both** sides.
      margin (string, number):
        Value sent to the intersection observer. Will make the observer
        trigger earlier, by the margin (px) value supplied.
      load_more_text (string):
        Text shown in default load more button, when in manual mode.
      empty_text (string):
        Text shown when there is no more content to load.
      load (event):
        Emitted when reaching the start / end threshold, or if triggered
        when using manual mode.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VInfiniteScroll", children, **kwargs)
        self._attr_names += [
            "tag",
            "mode",
            "height",
            "width",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "color",
            "direction",
            "side",
            "margin",
            ("load_more_text", "loadMoreText"),
            ("empty_text", "emptyText"),
        ]
        self._event_names += [
            "load",
        ]


class VInput(HtmlElement):
    """
    Vuetify's VInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-input>`_.

    Args:
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      name (string):
        Sets the component's name attribute.
      disabled (boolean):
        Removes the ability to click or target the component.
      id (string):
        Sets the DOM id on the component.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the input is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      readonly (boolean):
        Puts input in readonly state.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when appended icon is clicked.
      update_focused (event):
        Event that is emitted when the component's focus state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VInput", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "error",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "color",
            "name",
            "disabled",
            "id",
            "label",
            ("base_color", "baseColor"),
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "readonly",
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
        ]


class VItem(HtmlElement):
    """
    Vuetify's VItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-item>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VItem", children, **kwargs)
        self._attr_names += [
            "disabled",
            "value",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VItemGroup(HtmlElement):
    """
    Vuetify's VItemGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-item-group>`_.

    Args:
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      disabled (boolean):
        Puts all children components into a disabled state.
      max (number):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allows one to select multiple items.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      selected_class (string):
        Configure the selected CSS class. This class will be available
        in `v-item` default scoped slot.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VItemGroup", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "tag",
            "theme",
            "disabled",
            "max",
            "multiple",
            "mandatory",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VKbd(HtmlElement):
    """
    Vuetify's VKbd component.
    See more `info and examples <https://vuetifyjs.com/api/v-kbd>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VKbd", children, **kwargs)
        self._attr_names += [
            "tag",
            "theme",
            "border",
            "elevation",
            "rounded",
            "tile",
            "color",
        ]
        self._event_names += []


class VLabel(HtmlElement):
    """
    Vuetify's VLabel component.
    See more `info and examples <https://vuetifyjs.com/api/v-label>`_.

    Args:
      text (string):
        Specify content text for the component.
      theme (string):
        Specify a theme for this component and all of its children.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLabel", children, **kwargs)
        self._attr_names += [
            "text",
            "theme",
        ]
        self._event_names += [
            "click",
        ]


class VLayout(HtmlElement):
    """
    Vuetify's VLayout component.
    See more `info and examples <https://vuetifyjs.com/api/v-layout>`_.

    Args:
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      full_height (boolean):
        Sets the component height to 100%.
      overlaps (string[]):
        **FOR INTERNAL USE ONLY**
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLayout", children, **kwargs)
        self._attr_names += [
            "height",
            "width",
            ("full_height", "fullHeight"),
            "overlaps",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
        ]
        self._event_names += []


class VLayoutItem(HtmlElement):
    """
    Vuetify's VLayoutItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-layout-item>`_.

    Args:
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      position ('top', 'bottom', 'left', 'right'):
        The position of the item.
      absolute (boolean):
        Applies **position: absolute** to the component.
      name (string):
        Assign a specific name for layout registration.
      size (string, number):
        Sets the height and width of the component.
      order (string, number):
        Adjust the order of the component in relation to its registration order.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLayoutItem", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "position",
            "absolute",
            "name",
            "size",
            "order",
        ]
        self._event_names += []


class VLazy(HtmlElement):
    """
    Vuetify's VLazy component.
    See more `info and examples <https://vuetifyjs.com/api/v-lazy>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      options (IntersectionObserverInit):
        Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
        constructor.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLazy", children, **kwargs)
        self._attr_names += [
            "tag",
            "height",
            "width",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            ("model_value", "modelValue"),
            "transition",
            "options",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VLigatureIcon(HtmlElement):
    """
    Vuetify's VLigatureIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-ligature-icon>`_.

    Args:
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLigatureIcon", children, **kwargs)
        self._attr_names += [
            "icon",
            "tag",
        ]
        self._event_names += []


class VList(HtmlElement):
    """
    Vuetify's VList component.
    See more `info and examples <https://vuetifyjs.com/api/v-list>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      nav (boolean):
        An alternative styling that reduces `v-list-item` width and rounds
        the corners. Typically used with **[v-navigation-drawer](/components/navigation-drawers)**.
      activated (any):
        Array of ids of activated nodes.
      disabled (boolean):
        Puts all children inputs into a disabled state.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      items (any[]):
        Can be an array of objects or strings. By default objects should
        have a **title** property, and can optionally have a **props**
        property containing any [VListItem props](/api/v-list-item/#props),
        a **value** property to allow selection, and a **children** property
        containing more item objects. Keys to use for these can be changed
        with the **item-title**, **item-value**, **item-props**, and
        **item-children** props.
      active_color (string):
        Deprecated, use `color` instead.
      base_color (string):
        Sets the color of component when not focused.
      slim (boolean):
        Reduces horizontal spacing for badges, icons, tooltips, and avatars
        within slim list items to create a more compact visual representation.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      lines (false, 'one', 'two', 'three'):
        Designates a **minimum-height** for all children `v-list-item`
        components. This prop uses [line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp)
        and is not supported in all browsers.
      mandatory (boolean):
        Forces at least one item to always be selected (if available).
      active_class (string):
        The class applied to the component when it is in an active state.
      item_props (SelectItemKey):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      selected (unknown):
        An array containing the values of currently selected items. Can
        be two-way bound with `v-model:selected`.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3729: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      filterable (boolean):
        **FOR INTERNAL USE ONLY** Prevents list item selection using
        [space] key and pass it back to the text input. Used internally
        for VAutocomplete and VCombobox.
      expand_icon (enum):
        Icon to display when the list item is collapsed.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon to display when the list item is expanded.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prepend_gap (string, number):
        Sets the horizontal spacing between prepend slot and the main
        content within list item. Also affects indent to ensure expected
        alignment of group children.
      indent (string, number):
        Overrides the indent size for nested groups.
      activatable (boolean):
        Designates whether the list items are activatable. Additionally,
        sets necessary accessibility attributes internally.
      selectable (boolean):
        Designates whether the list items are selectable. Additionally,
        sets necessary accessibility attributes internally.
      opened (unknown):
        An array containing the values of currently opened groups. Can
        be two-way bound with `v-model:opened`.
      items_registration ('props', 'render'):
        When set to 'props', skips rendering collapsed items/nodes (for
        significant performance gains).
      active_strategy (ActiveStrategy):
        Affects how items with children behave when activated. If not
        specified, the **single-independent** strategy will be used.
        - **leaf:** Only leaf nodes (items without children) can be activated.
        - **single-leaf:** Similar as **leaf**, but only a single item
        can be activated at a time. - **independent:** All nodes can
        be activated whether they have children or not. - **single-independent:**
        Similar as **independent**, but only a single item can be activated
        at a time.
      select_strategy (SelectStrategy):
        Affects how items with children behave when selected. - **leaf:**
        Only leaf nodes (items without children) can be selected. - **independent:**
        All nodes can be selected whether they have children or not.
        - **classic:** Selecting a parent node will cause all children
        to be selected, parent nodes will be displayed as selected if
        all their descendants are selected. Only leaf nodes will be added
        to the model. - **trunk**: Same as classic but if all of a node's
        children are selected then only that node will be added to the
        model.
      open_strategy (OpenStrategy):
        Affects how items with children behave when expanded. - **multiple:**
        Any number of groups can be open at once. - **single:** Only
        one group at each level can be open, opening a group will cause
        others to close. - **list:** Multiple, but all other groups will
        close when an item is selected.
      item_title (SelectItemKey):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      item_children (SelectItemKey):
        Property on supplied `items` that contains its children.
      item_type (SelectItemKey):
        Designates the key on the supplied items that is used for determining
        the nodes type.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      click_open (event):
        Emitted when the list item is opened.
      click_select (event):
        Emitted when the list item is selected.
      update_opened (event):
        Emitted when the list item is opened.
      update_selected (event):
        Emitted when the list item is selected.
      update_activated (event):
        Emitted when the list item is activated.
      click_activate (event):
        Emitted when the list item is activated.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VList", children, **kwargs)
        self._attr_names += [
            "tag",
            "nav",
            "activated",
            "disabled",
            "height",
            "width",
            "theme",
            "items",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            "slim",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "rounded",
            "tile",
            "color",
            "variant",
            ("bg_color", "bgColor"),
            "lines",
            "mandatory",
            ("active_class", "activeClass"),
            ("item_props", "itemProps"),
            "selected",
            ("value_comparator", "valueComparator"),
            "filterable",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("prepend_gap", "prependGap"),
            "indent",
            "activatable",
            "selectable",
            "opened",
            ("items_registration", "itemsRegistration"),
            ("active_strategy", "activeStrategy"),
            ("select_strategy", "selectStrategy"),
            ("open_strategy", "openStrategy"),
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_type", "itemType"),
            ("return_object", "returnObject"),
        ]
        self._event_names += [
            ("click_open", "click:open"),
            ("click_select", "click:select"),
            ("update_opened", "update:opened"),
            ("update_selected", "update:selected"),
            ("update_activated", "update:activated"),
            ("click_activate", "click:activate"),
        ]


class VListGroup(HtmlElement):
    """
    Vuetify's VListGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-group>`_.

    Args:
      title (string):
        Specify a title text for the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      disabled (boolean):
        Puts all children inputs into a disabled state.
      value (any):
        Expands / Collapse the list-group.
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        Deprecated, use `color` instead.
      expand_icon (enum):
        Icon to display when the list item is collapsed.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon to display when the list item is expanded.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      fluid (boolean):
        Removes the left padding assigned for action icons from group items.
      raw_id (string, number):
        Defines the root element's id attribute in the component. If
        it is provided, the id attribute will be dynamically generated
        in the format: "v-list-group--id-[rawId]".
      subgroup (boolean):
        Designate the component as nested list group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListGroup", children, **kwargs)
        self._attr_names += [
            "title",
            "tag",
            "color",
            "disabled",
            "value",
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "fluid",
            ("raw_id", "rawId"),
            "subgroup",
        ]
        self._event_names += []


class VListImg(HtmlElement):
    """
    Vuetify's VListImg component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-img>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListImg", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListItem(HtmlElement):
    """
    Vuetify's VListItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item>`_.

    Args:
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the href or to prop.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      nav (boolean):
        Reduces the width v-list-item takes up as well as adding a border radius.
      title (string, number, boolean):
        Generates a `v-list-item-title` component with the supplied value.
        Note that this overrides the native [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title)
        attribute, that must be set with `v-bind:title.attr` instead.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      value (any):
        The value used for selection. Obtained from [`v-list`](/api/v-list)'s
        `v-model:selected` when the item is selected.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      active_color (string):
        Deprecated, use `color` instead.
      base_color (string):
        Sets the color of component when not focused.
      prepend_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend**
        slot before default content.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      slim (boolean):
        Reduces horizontal spacing for badges, icons, tooltips, and avatars
        to create a more compact visual representation.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      color (string):
        Applies specified color to the control when in an **active**
        state or **input-value** is **true** - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors),
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      lines (false, 'one', 'two', 'three'):
        The line declaration specifies the minimum height of the item
        and can also be controlled from v-list with the same prop.
      active_class (string):
        The class applied to the component when it matches the current
        route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class)
        on the [vue-router](https://router.vuejs.org/) documentation.
      subtitle (string, number, boolean):
        Specify a subtitle text for the component.
      append_avatar (string):
        Appends a [v-avatar](/components/avatars/) component after default
        content in the **append** slot.
      prepend_avatar (string):
        Prepends a [v-avatar](/components/avatars/) component in the
        **prepend** slot before default content.
      prepend_gap (string, number):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VListItem.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItem", children, **kwargs)
        self._attr_names += [
            "replace",
            "link",
            "tag",
            "nav",
            "title",
            "disabled",
            "height",
            "value",
            "width",
            "theme",
            "active",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "slim",
            "ripple",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "rounded",
            "tile",
            "href",
            "exact",
            "to",
            "color",
            "variant",
            "lines",
            ("active_class", "activeClass"),
            "subtitle",
            ("append_avatar", "appendAvatar"),
            ("prepend_avatar", "prependAvatar"),
            ("prepend_gap", "prependGap"),
        ]
        self._event_names += [
            "click",
        ]


class VListItemAction(HtmlElement):
    """
    Vuetify's VListItemAction component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-action>`_.

    Args:
      end (boolean):
        Applies margin at the start of the component.
      start (boolean):
        Applies margin at the end of the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemAction", children, **kwargs)
        self._attr_names += [
            "end",
            "start",
            "tag",
        ]
        self._event_names += []


class VListItemMedia(HtmlElement):
    """
    Vuetify's VListItemMedia component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-media>`_.

    Args:
      end (boolean):
        Applies margin at the start of the component.
      start (boolean):
        Applies margin at the end of the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemMedia", children, **kwargs)
        self._attr_names += [
            "end",
            "start",
            "tag",
        ]
        self._event_names += []


class VListItemSubtitle(HtmlElement):
    """
    Vuetify's VListItemSubtitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-subtitle>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      opacity (string, number):
        Sets the component's opacity value
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemSubtitle", children, **kwargs)
        self._attr_names += [
            "tag",
            "opacity",
        ]
        self._event_names += []


class VListItemTitle(HtmlElement):
    """
    Vuetify's VListItemTitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-title>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemTitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListSubheader(HtmlElement):
    """
    Vuetify's VListSubheader component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-subheader>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      title (string):
        Specify a title text for the component.
      sticky (boolean):
        Sticks the header to the top of the table.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      inset (boolean):
        Insets the subheader without additional spacing, aligning it
        flush with the surrounding content.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListSubheader", children, **kwargs)
        self._attr_names += [
            "tag",
            "title",
            "sticky",
            "color",
            "inset",
        ]
        self._event_names += []


class VLocaleProvider(HtmlElement):
    """
    Vuetify's VLocaleProvider component.
    See more `info and examples <https://vuetifyjs.com/api/v-locale-provider>`_.

    Args:
      messages (unknown):
        Displays a list of messages or a single message if using a string.
      locale (string):
        Specify a locale to use.
      fallback_locale (string):
        Specify a fallback locale to use when a locale is not found.
      rtl (boolean):
        Specify a RTL mode.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLocaleProvider", children, **kwargs)
        self._attr_names += [
            "messages",
            "locale",
            ("fallback_locale", "fallbackLocale"),
            "rtl",
        ]
        self._event_names += []


class VMain(HtmlElement):
    """
    Vuetify's VMain component.
    See more `info and examples <https://vuetifyjs.com/api/v-main>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      scrollable (boolean):
        Specify a custom scrollable function.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMain", children, **kwargs)
        self._attr_names += [
            "tag",
            "height",
            "width",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "scrollable",
        ]
        self._event_names += []


class VMaskInput(HtmlElement):
    """
    Vuetify's VMaskInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-mask-input>`_.

    Args:
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      type (string):
        Sets input type.
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      reverse (boolean):
        Reverses the orientation.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      rounded (string, number, boolean):
        Adds a border radius to the input.
      tile (boolean):
        Removes any applied **border-radius** from the component.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      name (string):
        Sets the component's name attribute.
      autocomplete (string):
        Helps influence browser's suggestions. Special value **suppress**
        manipulates fields `name` attribute while **off** relies on browser's
        good will to stop suggesting values. Any other value is passed
        to the native `autocomplete` on the underlying element.
      disabled (boolean):
        Removes the ability to click or target the input.
      placeholder (string):
        Sets the input’s placeholder text.
      id (string):
        Sets the DOM id on the component.
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      autofocus (boolean):
        Enables autofocus.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outside the component's input, uses the
        same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      readonly (boolean):
        Puts input in readonly state.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      append_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **append-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      dirty (boolean):
        Manually apply the dirty state styling.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      counter_value (number, js_fn):
        Function returns the counter display text.
      model_modifiers (unknown):
        **FOR INTERNAL USE ONLY**
      mask (enum):
        Apply a mask to the input. See [guide](/components/mask-inputs/#guide)
        for more information.

        Enum values: [
          string, {      mask: string      tokens: Record<        string,,
          js_fn, js_fn, { pattern: RegExp; test: undefined }      >
          }
        ]
      return_masked_value (boolean):
        Returns the unmodified masked string.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMaskInput", children, **kwargs)
        self._attr_names += [
            "flat",
            "type",
            ("model_value", "modelValue"),
            "error",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            "name",
            "autocomplete",
            "disabled",
            "placeholder",
            "id",
            "prefix",
            "role",
            "autofocus",
            "label",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "counter",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "readonly",
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "loading",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
            "mask",
            ("return_masked_value", "returnMaskedValue"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
        ]


class VMenu(HtmlElement):
    """
    Vuetify's VMenu component.
    See more `info and examples <https://vuetifyjs.com/api/v-menu>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      id (string):
        The unique identifier of the component.
      theme (string):
        Specify a theme for this component and all of its children.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component. Use `auto` to use the activator width.
      location (Anchor):
        Specifies the anchor point for positioning the component, using
        directional cues to align it either horizontally, vertically,
        or both..
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          {      component: ComponentPublicInstanceConstructor<
          CreateComponentPublicInstanceWithMixins<          {} & { target?:
          HTMLElement, [x: number, y: number], undefined } & {
             $children?:, VNodeChild, { $stable?: boolean, undefined },
          js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn, [x: number, y: number], undefined } & {
                     $children?:, VNodeChild, { $stable?: boolean, undefined
          }, js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn, [x: number, y: number], undefined } & {
                     $children?:, VNodeChild, { $stable?: boolean, undefined
          }, js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn
        ]
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      close_on_back (boolean):
        Closes the overlay content when the browser's back button is
        pressed or `$router.back()` is called, cancelling the original
        navigation. `persistent` overlays will cancel navigation and
        animate as if they were clicked outside instead of closing.
      contained (boolean):
        Limits the size of the component and scrim to its offset parent.
        Implies `absolute` and `attach`. (Note: The parent element must
        have position: relative.).
      content_class (any):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      content_props (any):
        Apply custom properties to the content.
      opacity (string, number):
        Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
      no_click_animation (boolean):
        Disables the bounce effect when clicking outside of the content
        element when using the persistent prop.
      persistent (boolean):
        Clicking outside of the element or pressing esc key will not deactivate it.
      scrim (string, boolean):
        Accepts true/false to enable background, and string to define color.
      z_index (string, number):
        The z-index used for the component.
      target (enum):
        For locationStrategy="connected", specify an element or array
        of x,y coordinates that the overlay should position itself relative
        to. This will be the activator element by default.

        Enum values: [
          Element, (string & {}), 'parent', 'cursor', ComponentPublicInstance,
          [number, number]
        ]
      activator_props (unknown):
        Apply custom properties to the activator.
      open_on_click (boolean):
        Designates whether menu should open on activator click.
      open_on_hover (boolean):
        Designates whether menu should open on activator hover.
      open_on_focus (boolean):
        Activate the component when the activator is focused.
      close_on_content_click (boolean):
        Designates if menu should close when its content is clicked.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only works with
        the **open-on-hover** prop.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only works with
        the **open-on-hover** prop.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        Increases distance from the target. When passed as a pair of
        numbers, the second value shifts anchor along the side and away
        from the target.
      stick_to_target (boolean):
        Enables the overlay content to go off-screen when scrolling.
      viewport_margin (string, number):
        Sets custom viewport margin for the overlay content
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
      retain_focus (boolean):
        Captures and keeps focus within the content element when using
        **Tab** and **Shift**+**Tab**. Recommended to be `false` when
        using external tools that require focus such as TinyMCE or vue-clipboard.
      capture_focus (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/focusTrap.json))
      disable_initial_focus (boolean):
        Deprecated, use `capture-focus` instead. Prevents automatic redirect
        of first `focusin` event. Intended to use on permanently open
        menus or VSpeedDial.
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default. Generally
        not recommended except as a last resort: the default positioning
        algorithm should handle most scenarios better than is possible
        without teleporting, and you may have unexpected behavior if
        the menu ends up as child of its activator.
      submenu (boolean):
        Opens with right arrow and closes on left instead of up/down.
        Implies `location="end"`. Directions are reversed for RTL.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMenu", children, **kwargs)
        self._attr_names += [
            "disabled",
            "height",
            "width",
            "id",
            "theme",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "location",
            ("model_value", "modelValue"),
            "transition",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            "persistent",
            "scrim",
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "eager",
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            ("stick_to_target", "stickToTarget"),
            ("viewport_margin", "viewportMargin"),
            ("scroll_strategy", "scrollStrategy"),
            ("retain_focus", "retainFocus"),
            ("capture_focus", "captureFocus"),
            ("disable_initial_focus", "disableInitialFocus"),
            "attach",
            "submenu",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VMessages(HtmlElement):
    """
    Vuetify's VMessages component.
    See more `info and examples <https://vuetifyjs.com/api/v-messages>`_.

    Args:
      active (boolean):
        Determines whether the messages are visible or not.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          { component: Component; leaveAbsolute: boolean; group: boolean
          }
        ]
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMessages", children, **kwargs)
        self._attr_names += [
            "active",
            "color",
            "transition",
            "messages",
        ]
        self._event_names += []


class VNavigationDrawer(HtmlElement):
    """
    Vuetify's VNavigationDrawer component.
    See more `info and examples <https://vuetifyjs.com/api/v-navigation-drawer>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      name (string):
        Assign a specific name for layout registration.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location ('top', 'left', 'right', 'bottom', 'start', 'end'):
        Controls the edge of the screen the drawer is attached to.
      absolute (boolean):
        Applies **position: absolute** to the component.
      sticky (boolean):
        When true, the drawer will remain visible when scrolling past
        the top of the page.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      image (string):
        Apply a specific background image to the component.
      floating (boolean):
        A floating drawer has no visible container (no border-right).
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Sets the designated mobile breakpoint for the component. This
        will apply alternate styles for mobile devices such as the `temporary`
        prop, or activate the `bottom` prop when the breakpoint value
        is met. Setting the value to `0` will disable this functionality.
      order (string, number):
        Adjust the order of the component in relation to its registration order.
      persistent (boolean):
        Clicking outside or pressing **esc** key will not dismiss the dialog.
      scrim (string, boolean):
        Determines whether an overlay is used when a **temporary** drawer
        is open. Accepts true/false to enable background, and string
        to define color.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      retain_focus (boolean):
        Captures and keeps focus within the content element when using
        **Tab** and **Shift**+**Tab**. Recommended to be `false` when
        using external tools that require focus such as TinyMCE or vue-clipboard.
      capture_focus (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/focusTrap.json))
      disable_resize_watcher (boolean):
        Prevents the automatic opening or closing of the drawer when
        resized, based on whether the device is mobile or desktop.
      disable_route_watcher (boolean):
        Disables opening of navigation drawer when route changes.
      expand_on_hover (boolean):
        Collapses the drawer to a **rail-variant** until hovering with the mouse.
      permanent (boolean):
        The drawer remains visible regardless of screen size.
      rail (boolean):
        Sets the component width to the **rail-width** value.
      rail_width (string, number):
        Sets the width for the component when `rail` is enabled.
      temporary (boolean):
        A temporary drawer sits above its application and uses a scrim
        (overlay) to darken the background.
      touchless (boolean):
        Disable mobile touch functionality.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_rail (event):
        Event that is emitted when the rail model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VNavigationDrawer", children, **kwargs)
        self._attr_names += [
            "tag",
            "name",
            "width",
            "theme",
            "border",
            "elevation",
            "location",
            "absolute",
            "sticky",
            "rounded",
            "tile",
            "color",
            "image",
            "floating",
            ("model_value", "modelValue"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "order",
            "persistent",
            "scrim",
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            ("retain_focus", "retainFocus"),
            ("capture_focus", "captureFocus"),
            ("disable_resize_watcher", "disableResizeWatcher"),
            ("disable_route_watcher", "disableRouteWatcher"),
            ("expand_on_hover", "expandOnHover"),
            "permanent",
            "rail",
            ("rail_width", "railWidth"),
            "temporary",
            "touchless",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_rail", "update:rail"),
        ]


class VNoSsr(HtmlElement):
    """
    Vuetify's VNoSsr component.
    See more `info and examples <https://vuetifyjs.com/api/v-no-ssr>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VNoSsr", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VNumberInput(HtmlElement):
    """
    Vuetify's VNumberInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-number-input>`_.

    Args:
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      type (string):
        **IGNORED** underlying input is always of type 'text'
      reverse (boolean):
        Reverses the orientation.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      autocomplete (string):
        Helps influence browser's suggestions. Special value **suppress**
        manipulates fields `name` attribute while **off** relies on browser's
        good will to stop suggesting values. Any other value is passed
        to the native `autocomplete` on the underlying element.
      disabled (boolean):
        Removes the ability to click or target the input.
      max (number):
        Specifies the maximum allowable value for the input.
      min (number):
        Specifies the minimum allowable value for the input.
      placeholder (string):
        Sets the input’s placeholder text.
      step (number):
        Defines the interval between allowed values when the user increments
        or decrements the input
      width (string, number):
        Sets the width for the component.
      id (string):
        Sets the DOM id on the component.
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      autofocus (boolean):
        Enables autofocus.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the outside the component's input, uses the
        same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts input in readonly state.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      rounded (string, number, boolean):
        Adds a border radius to the input.
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      model_value (number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      inset (boolean):
        Applies an indentation to the dividers used in the stepper buttons.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      decimal_separator (string):
        Expects single character to be used as decimal separator.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      append_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **append-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      dirty (boolean):
        Manually apply the dirty state styling.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      counter_value (number, js_fn):
        Function returns the counter display text.
      model_modifiers (unknown):
        **FOR INTERNAL USE ONLY**
      control_variant ('split', 'default', 'hidden', 'stacked'):
        The color of the control. It defaults to the value of `variant` prop.
      hide_input (boolean):
        Hide the input field.
      precision (number):
        Enforces strict precision. It is expected to be an integer value
        in range between `0` and `15`, or null for unrestricted.
      min_fraction_digits (number):
        Specifies the minimum fraction digits to be displayed (capped
        to `precision`). Defaults to `precision` when not explicitly
        set.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VNumberInput", children, **kwargs)
        self._attr_names += [
            "flat",
            "type",
            "reverse",
            "name",
            "error",
            "label",
            "autocomplete",
            "disabled",
            "max",
            "min",
            "placeholder",
            "step",
            "width",
            "id",
            "prefix",
            "role",
            "autofocus",
            "theme",
            "active",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "loading",
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "inset",
            "direction",
            ("decimal_separator", "decimalSeparator"),
            "messages",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            "focused",
            ("hide_details", "hideDetails"),
            "counter",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_inner_icon", "appendInnerIcon"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
            ("control_variant", "controlVariant"),
            ("hide_input", "hideInput"),
            "precision",
            ("min_fraction_digits", "minFractionDigits"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
        ]


class VOtpInput(HtmlElement):
    """
    Vuetify's VOtpInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-otp-input>`_.

    Args:
      length (string, number):
        The OTP field's length.
      type ('number', 'text', 'password'):
        Supported types: `text`, `password`, `number`.
      model_value (string, number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      disabled (boolean):
        Removes the ability to click or target the input.
      placeholder (string):
        Sets the input’s placeholder text.
      autofocus (boolean):
        Automatically focuses the first input on page load
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      divider (string):
        Specifies the dividing character between items.
      base_color (string):
        Sets the color of the input when it is not focused.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      focused (boolean):
        Forces a focused state styling on the component.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      focus_all (boolean):
        Puts all inputs into a focus state when any are focused
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_focused (event):
        Emitted when the input is focused or blurred
      finish (event):
        Emitted when the input is filled completely and cursor is blurred.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VOtpInput", children, **kwargs)
        self._attr_names += [
            "length",
            "type",
            ("model_value", "modelValue"),
            "error",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "rounded",
            "theme",
            "color",
            "variant",
            "disabled",
            "placeholder",
            "autofocus",
            "label",
            "divider",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "focused",
            "loading",
            ("focus_all", "focusAll"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_focused", "update:focused"),
            "finish",
        ]


class VOverlay(HtmlElement):
    """
    Vuetify's VOverlay component.
    See more `info and examples <https://vuetifyjs.com/api/v-overlay>`_.

    Args:
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      location (Anchor):
        Specifies the anchor point for positioning the component, using
        directional cues to align it either horizontally, vertically,
        or both..
      absolute (boolean):
        Applies **position: absolute** to the content element.
      theme (string):
        Specify a theme for this component and all of its children.
      disabled (boolean):
        Removes the ability to click or target the component.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      close_on_back (boolean):
        Closes the overlay content when the browser's back button is
        pressed or `$router.back()` is called, cancelling the original
        navigation. `persistent` overlays will cancel navigation and
        animate as if they were clicked outside instead of closing.
      contained (boolean):
        Limits the size of the component and scrim to its offset parent.
        Implies `absolute` and `attach`. (Note: The parent element must
        have position: relative.).
      content_class (any):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      content_props (any):
        Apply custom properties to the content.
      opacity (string, number):
        Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
      no_click_animation (boolean):
        Disables the bounce effect when clicking outside of the content
        element when using the persistent prop.
      persistent (boolean):
        Clicking outside of the element or pressing esc key will not deactivate it.
      scrim (string, boolean):
        Accepts true/false to enable background, and string to define color.
      z_index (string, number):
        The z-index used for the component.
      target (enum):
        For locationStrategy="connected", specify an element or array
        of x,y coordinates that the overlay should position itself relative
        to. This will be the activator element by default.

        Enum values: [
          Element, (string & {}), 'parent', 'cursor', ComponentPublicInstance,
          [number, number]
        ]
      activator_props (unknown):
        Apply custom properties to the activator.
      open_on_click (boolean):
        Activate the component when the activator is clicked.
      open_on_hover (boolean):
        Activate the component when the activator is hovered.
      open_on_focus (boolean):
        Activate the component when the activator is focused.
      close_on_content_click (boolean):
        Closes component when you click on its content.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        Increases distance from the target. When passed as a pair of
        numbers, the second value shifts anchor along the side and away
        from the target.
      stick_to_target (boolean):
        Enables the overlay content to go off-screen when scrolling.
      viewport_margin (string, number):
        Sets custom viewport margin for the overlay content
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
      retain_focus (boolean):
        Captures and keeps focus within the content element when using
        **Tab** and **Shift**+**Tab**. Recommended to be `false` when
        using external tools that require focus such as TinyMCE or vue-clipboard.
      capture_focus (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/focusTrap.json))
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_outside (event):
        Event that fires when clicking outside an active overlay.
      keydown (event):
        Emitted when **any** key is pressed.
      afterEnter (event):
        Event that fires after the overlay has finished transitioning in.
      afterLeave (event):
        Event that fires after the overlay has finished transitioning out.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VOverlay", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "location",
            "absolute",
            "theme",
            "disabled",
            "eager",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            "persistent",
            "scrim",
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            ("stick_to_target", "stickToTarget"),
            ("viewport_margin", "viewportMargin"),
            ("scroll_strategy", "scrollStrategy"),
            ("retain_focus", "retainFocus"),
            ("capture_focus", "captureFocus"),
            "transition",
            "attach",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_outside", "click:outside"),
            "keydown",
            "afterEnter",
            "afterLeave",
        ]


class VPagination(HtmlElement):
    """
    Vuetify's VPagination component.
    See more `info and examples <https://vuetifyjs.com/api/v-pagination>`_.

    Args:
      length (string, number):
        The number of pages.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      start (string, number):
        Specify the starting page.
      model_value (number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the selected page button - supports
        utility colors (for example `success` or `purple`) or css color
        (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes
        on the [colors page](/styles/colors#material-colors).
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      aria_label (string):
        Label for the root element.
      active_color (string):
        The applied color when the component is in an active state.
      prev_icon (enum):
        The icon to use for the prev button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      next_icon (enum):
        The icon to use for the next button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      first_icon (enum):
        The icon to use for the first button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      last_icon (enum):
        The icon to use for the last button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      total_visible (string, number):
        Specify the total visible pagination numbers.
      page_aria_label (string):
        Label for each page button.
      current_page_aria_label (string):
        Label for the currently selected page.
      first_aria_label (string):
        Label for the go to first button.
      previous_aria_label (string):
        Label for the previous button.
      next_aria_label (string):
        Label for the next button.
      last_aria_label (string):
        Label for the go to last button.
      ellipsis (string):
        Text to show between page buttons when truncating the list.
      show_first_last_page (boolean):
        Show buttons for going to first and last page.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      next (event):
        Emitted when clicking on go to next button.
      prev (event):
        Emitted when clicking on go to previous button.
      first (event):
        Emitted when clicking on go to first button.
      last (event):
        Emitted when clicking on go to last button.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPagination", children, **kwargs)
        self._attr_names += [
            "length",
            "border",
            "start",
            ("model_value", "modelValue"),
            "density",
            "elevation",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            "disabled",
            "size",
            ("aria_label", "ariaLabel"),
            ("active_color", "activeColor"),
            ("prev_icon", "prevIcon"),
            ("next_icon", "nextIcon"),
            ("first_icon", "firstIcon"),
            ("last_icon", "lastIcon"),
            ("total_visible", "totalVisible"),
            ("page_aria_label", "pageAriaLabel"),
            ("current_page_aria_label", "currentPageAriaLabel"),
            ("first_aria_label", "firstAriaLabel"),
            ("previous_aria_label", "previousAriaLabel"),
            ("next_aria_label", "nextAriaLabel"),
            ("last_aria_label", "lastAriaLabel"),
            "ellipsis",
            ("show_first_last_page", "showFirstLastPage"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "next",
            "prev",
            "first",
            "last",
        ]


class VParallax(HtmlElement):
    """
    Vuetify's VParallax component.
    See more `info and examples <https://vuetifyjs.com/api/v-parallax>`_.

    Args:
      scale (string, number):
        The scale of the parallax image.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VParallax", children, **kwargs)
        self._attr_names += [
            "scale",
        ]
        self._event_names += []


class VPicker(HtmlElement):
    """
    Vuetify's VPicker component.
    See more `info and examples <https://vuetifyjs.com/api/v-picker>`_.

    Args:
      title (string):
        Specify a title text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'static', 'relative', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      divided (boolean):
        Adds a divider between the header and controls.
      landscape (boolean):
        Puts the picker into landscape mode.
      hide_header (boolean):
        Hide the picker header.
      hide_title (boolean):
        Hide the picker title.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPicker", children, **kwargs)
        self._attr_names += [
            "title",
            "border",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "location",
            "position",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            ("bg_color", "bgColor"),
            "divided",
            "landscape",
            ("hide_header", "hideHeader"),
            ("hide_title", "hideTitle"),
        ]
        self._event_names += []


class VPickerTitle(HtmlElement):
    """
    Vuetify's VPickerTitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-picker-title>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPickerTitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VPie(HtmlElement):
    """
    Vuetify's VPie component.
    See more `info and examples <https://vuetifyjs.com/api/v-pie>`_.

    Args:
      title (string):
        Specify a title text for the component.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      rounded (string, number):
        Number passed as corner radius relative to 100x100 SVG viewport
      size (string, number):
        Sets the height and width of the chart (excluding title and legend).
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      items (Record<string, any>, { color: string; pattern: string }[]):
        Data items expected to contain `key`, `title` and `value`.
      item_title (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VPie.json))
      item_value (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VPie.json))
      legend (enum):
        Controls legend visibility, position and text format.

        Enum values: [
          boolean, {      position: 'top', 'bottom', 'left', 'right'
             textFormat:, string, ((v: {            key: string, number,
          js_fn
        ]
      item_key (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VPie.json))
      tooltip (enum):
        Controls tooltip visibility, transition, offset from the cursor
        and formats of title and subtitle.

        Enum values: [
          boolean, {      titleFormat:, string, ((v: {            key:
          string, number, js_fn, string, ((v: {            key: string,
          number, js_fn, false, true, TransitionProps      offset: number
             }
        ]
      palette ((string, { color: string; pattern: string })[]):
        Defines colors and patterns to be applied based on the data items
        order. Data items can also define their colors.
      rotate (string, number):
        Rotates the chart segments clockwise.
      gauge_cut (string, number):
        Allows removing bottom part of the chart to make it into a gauge.
        Expects angle (0-180).
      inner_cut (string, number):
        Specifies inner radius for a donut-style chart as a percent (0-100).
        Without `hide-slice`, inner slice is visible with translucent
        color matching the item.
      hover_scale (string, number):
        Enables interactive behavior by reducing segment size until it
        gets hovered. Expects fraction value (0-0.25).
      gap (string, number):
        Reduces segment size by a specified angle. Recommended to in range (0-10).
      animation (enum):
        Controls duration and easing of the expand/collapse and hover
        effect. Defaults to `easeInOutCubic` over 400ms.

        Enum values: [
          boolean, {      duration: number      easing:, 'linear', 'easeInQuad',
          'easeOutQuad', 'easeInOutQuad', 'easeInCubic', 'easeOutCubic',
          'easeInOutCubic', 'easeInQuart', 'easeOutQuart', 'easeInOutQuart',
          'easeInQuint', 'easeOutQuint', 'easeInOutQuint', 'instant'
           }
        ]
      hide_slice (boolean):
        Makes inner slice invisible instead of semi-transparent.
      reveal (boolean, { duration: number }):
        Enables and controls duration for initial reveal animation. Easing
        function is shared with `animation` prop.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPie", children, **kwargs)
        self._attr_names += [
            "title",
            "density",
            "rounded",
            "size",
            ("bg_color", "bgColor"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            "legend",
            ("item_key", "itemKey"),
            "tooltip",
            "palette",
            "rotate",
            ("gauge_cut", "gaugeCut"),
            ("inner_cut", "innerCut"),
            ("hover_scale", "hoverScale"),
            "gap",
            "animation",
            ("hide_slice", "hideSlice"),
            "reveal",
        ]
        self._event_names += []


class VPieSegment(HtmlElement):
    """
    Vuetify's VPieSegment component.
    See more `info and examples <https://vuetifyjs.com/api/v-pie-segment>`_.

    Args:
      pattern (string):
        Decal pattern to put on top of the outer slice.
      value (number):
        The value used for calculate segment/arc angle size.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      rounded (string, number):
        Number passed as corner radius relative to 100x100 SVG viewport
      color (string):
        Sets segment color to be passed straight to CSS style attribute.
      rotate (string, number):
        Sets segment offset angle.
      inner_cut (string, number):
        Sets inner slice size in percent (0-100).
      hover_scale (string, number):
        Reduces outer radius until segment is hovered. Expects fraction value (0-0.25)
      gap (string, number):
        Reduces segment size by a specified angle. Recommended to in range (0-10).
      animation (enum):
        Controls duration and easing of the expand/collapse and hover
        effect. Defaults to `easeInOutCubic` over 400ms.

        Enum values: [
          boolean, {      duration: number      easing:, 'linear', 'easeInQuad',
          'easeOutQuad', 'easeInOutQuad', 'easeInCubic', 'easeOutCubic',
          'easeInOutCubic', 'easeInQuart', 'easeOutQuart', 'easeInOutQuart',
          'easeInQuint', 'easeOutQuint', 'easeInOutQuint', 'instant'
           }
        ]
      hide_slice (boolean):
        Makes inner slice invisible instead of semi-transparent.
      reveal (boolean, { duration: number }):
        Enables and controls duration for initial reveal animation. Easing
        function is shared with `animation` prop.
      update_active (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VPieSegment.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPieSegment", children, **kwargs)
        self._attr_names += [
            "pattern",
            "value",
            "active",
            "rounded",
            "color",
            "rotate",
            ("inner_cut", "innerCut"),
            ("hover_scale", "hoverScale"),
            "gap",
            "animation",
            ("hide_slice", "hideSlice"),
            "reveal",
        ]
        self._event_names += [
            ("update_active", "update:active"),
        ]


class VPieTooltip(HtmlElement):
    """
    Vuetify's VPieTooltip component.
    See more `info and examples <https://vuetifyjs.com/api/v-pie-tooltip>`_.

    Args:
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      item (enum):
        Data item related to hovered segment

        Enum values: [
          {  key: string, number, symbol  color: string  value: number
           title: string  pattern: string  isActive: boolean  raw: Record<string,
          any>}
        ]
      target ([number, number]):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VPieTooltip.json))
      offset (string, number, number[]):
        Increases distance from the target. When passed as a pair of
        numbers, the second value shifts anchor along the side and away
        from the target.
      transition (enum):
        The transition used when hovering between chart segments

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      title_format (string, ((v: {      key: string, number, js_fn):
        Formatter definition or function. When passed as String macros
        for `[title]` and `[value]` get replaced dynamically.
      subtitle_format (string, ((v: {      key: string, number, js_fn):
        Formatter definition or function. When passed as String macros
        for `[title]` and `[value]` get replaced dynamically.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPieTooltip", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "item",
            "target",
            "offset",
            "transition",
            ("title_format", "titleFormat"),
            ("subtitle_format", "subtitleFormat"),
        ]
        self._event_names += []


class VProgressCircular(HtmlElement):
    """
    Vuetify's VProgressCircular component.
    See more `info and examples <https://vuetifyjs.com/api/v-progress-circular>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      indeterminate (boolean, 'disable-shrink'):
        Constantly animates, use when loading progress is unknown. If
        set to the string `'disable-shrink'` it will use a simpler animation
        that does not run on the main thread.
      size (string, number):
        Sets the diameter of the circle in pixels.
      width (string, number):
        Sets the stroke of the circle in pixels.
      theme (string):
        Specify a theme for this component and all of its children.
      rounded (boolean):
        Rounds the ends of the progress arc for a softer appearance.
        When enabled, the progress stroke will have rounded caps instead
        of square ends.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (string, number):
        The percentage value for current progress.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      rotate (string, number):
        Rotates the circle start point in degrees.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VProgressCircular", children, **kwargs)
        self._attr_names += [
            "tag",
            "indeterminate",
            "size",
            "width",
            "theme",
            "rounded",
            "color",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "rotate",
        ]
        self._event_names += []


class VProgressLinear(HtmlElement):
    """
    Vuetify's VProgressLinear component.
    See more `info and examples <https://vuetifyjs.com/api/v-progress-linear>`_.

    Args:
      model_value (string, number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      reverse (boolean):
        Displays reversed progress (right to left in LTR mode and left to right in RTL).
      height (string, number):
        Sets the height for the component.
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      absolute (boolean):
        Applies position: absolute to the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      indeterminate (boolean):
        Constantly animates, use when loading progress is unknown.
      max (string, number):
        Sets the maximum value the progress can reach.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      opacity (string, number):
        Set the opacity of the progress bar.
      active (boolean):
        Reduce the height to 0, hiding component.
      striped (boolean):
        Adds a stripe background to the filled portion of the progress component.
      stream (boolean):
        An alternative style for portraying loading that works in tandem
        with **buffer-value**.
      bg_opacity (string, number):
        Background opacity, if null it defaults to 0.3 if background
        color is not specified or 1 otherwise.
      buffer_value (string, number):
        The percentage value for the buffer.
      buffer_color (string):
        Sets the color of the buffer bar.
      buffer_opacity (string, number):
        Set the opacity of the buffer bar.
      clickable (boolean):
        Clicking on the progress track will automatically set the value.
      rounded_bar (boolean):
        Applies a border radius to the progress bar.
      chunk_count (string, number):
        Specifies amount of chunks to divide the bar into.
      chunk_width (string, number):
        Defines chunk absolute size. Useful when chunk is narrow.
      chunk_gap (string, number):
        Defines size of the gap between chunks.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VProgressLinear", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "reverse",
            "height",
            "location",
            "absolute",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "indeterminate",
            "max",
            ("bg_color", "bgColor"),
            "opacity",
            "active",
            "striped",
            "stream",
            ("bg_opacity", "bgOpacity"),
            ("buffer_value", "bufferValue"),
            ("buffer_color", "bufferColor"),
            ("buffer_opacity", "bufferOpacity"),
            "clickable",
            ("rounded_bar", "roundedBar"),
            ("chunk_count", "chunkCount"),
            ("chunk_width", "chunkWidth"),
            ("chunk_gap", "chunkGap"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VPullToRefresh(HtmlElement):
    """
    Vuetify's VPullToRefresh component.
    See more `info and examples <https://vuetifyjs.com/api/v-pull-to-refresh>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      pull_down_threshold (number):
        The distance the user must pull down to trigger a refresh.
      load (event):
        Emitted when the user pulls down past the threshold.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPullToRefresh", children, **kwargs)
        self._attr_names += [
            "disabled",
            ("pull_down_threshold", "pullDownThreshold"),
        ]
        self._event_names += [
            "load",
        ]


class VRadio(HtmlElement):
    """
    Vuetify's VRadio component.
    See more `info and examples <https://vuetifyjs.com/api/v-radio>`_.

    Args:
      type (string):
        Provides the default type for children selection controls.
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      name (string):
        Sets the component's name attribute.
      disabled (boolean):
        Removes the ability to click or target the component.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      id (string):
        Sets the DOM id on the component.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3888: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      inline (boolean):
        Puts children inputs into a row.
      true_value (any):
        Sets value for truthy state.
      false_value (any):
        Sets value for falsy state.
      defaults_target (string):
        The target component to provide defaults values for.
      false_icon (enum):
        The icon used when inactive.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_icon (enum):
        The icon used when active.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRadio", children, **kwargs)
        self._attr_names += [
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "theme",
            "color",
            "name",
            "disabled",
            "multiple",
            "value",
            "id",
            "label",
            ("base_color", "baseColor"),
            ("value_comparator", "valueComparator"),
            "readonly",
            "ripple",
            "inline",
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
        ]
        self._event_names += []


class VRadioGroup(HtmlElement):
    """
    Vuetify's VRadioGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-radio-group>`_.

    Args:
      type (string):
        Provides the default type for children selection controls.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      inline (boolean):
        Displays radio buttons in row.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the input is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      defaults_target (string):
        The target component to provide defaults values for.
      false_icon (enum):
        The icon used when inactive.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_icon (enum):
        The icon used when active.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3729: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when appended icon is clicked.
      update_focused (event):
        Event that is emitted when the component's focus state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRadioGroup", children, **kwargs)
        self._attr_names += [
            "type",
            "name",
            "error",
            "label",
            "disabled",
            "height",
            "width",
            "id",
            "theme",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "ripple",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "color",
            "inline",
            ("model_value", "modelValue"),
            "direction",
            "messages",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
        ]


class VRangeSlider(HtmlElement):
    """
    Vuetify's VRangeSlider component.
    See more `info and examples <https://vuetifyjs.com/api/v-range-slider>`_.

    Args:
      reverse (boolean):
        Reverses the slider direction.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the component.
      max (string, number):
        Sets the maximum allowed value.
      min (string, number):
        Sets the minimum allowed value.
      step (string, number):
        If greater than 0, sets step interval for ticks.
      width (string, number):
        Sets the width for the component.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean):
        Applies the [v-ripple](/directives/ripple) directive.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value ((string, number)[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the input is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      thumb_color (string):
        Sets the thumb and thumb label color.
      thumb_label (boolean, 'always'):
        Show thumb label. If `true` it shows label when using slider.
        If set to `'always'` it always shows label.
      thumb_size (string, number):
        Controls the size of the thumb label.
      show_ticks (boolean, 'always'):
        Show track ticks. If `true` it shows ticks when using slider.
        If set to `'always'` it always shows ticks.
      ticks (number[], Record<number, string>):
        Show track ticks. If `true` it shows ticks when using slider.
        If set to `'always'` it always shows ticks.
      tick_size (string, number):
        Controls the size of **ticks**
      track_color (string):
        Sets the track's color
      track_fill_color (string):
        Sets the track's fill color
      track_size (string, number):
        Sets the track's size (height).
      no_keyboard (boolean):
        **FOR INTERNAL USE ONLY** Ignore keyboard events.
      strict (boolean):
        Disallows dragging the ending thumb past the starting thumb and vice versa.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when appended icon is clicked.
      update_focused (event):
        Event that is emitted when the component's focus state changes.
      start (event):
        Slider value emitted at start of slider movement.
      end (event):
        Slider value emitted at the end of slider movement.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRangeSlider", children, **kwargs)
        self._attr_names += [
            "reverse",
            "name",
            "error",
            "label",
            "disabled",
            "max",
            "min",
            "step",
            "width",
            "id",
            "theme",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "ripple",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "elevation",
            "rounded",
            "tile",
            "color",
            ("model_value", "modelValue"),
            "direction",
            "messages",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("thumb_color", "thumbColor"),
            ("thumb_label", "thumbLabel"),
            ("thumb_size", "thumbSize"),
            ("show_ticks", "showTicks"),
            "ticks",
            ("tick_size", "tickSize"),
            ("track_color", "trackColor"),
            ("track_fill_color", "trackFillColor"),
            ("track_size", "trackSize"),
            ("no_keyboard", "noKeyboard"),
            "strict",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            "start",
            "end",
        ]


class VRating(HtmlElement):
    """
    Vuetify's VRating component.
    See more `info and examples <https://vuetifyjs.com/api/v-rating>`_.

    Args:
      length (string, number):
        The amount of items to show.
      model_value (string, number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      name (string):
        Sets the component's name attribute.
      disabled (boolean):
        Removes the ability to click or target the component.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      active_color (string):
        The applied color when the component is in an active state.
      readonly (boolean):
        Removes all hover effects and pointer events.
      clearable (boolean):
        Allows for the component to be cleared by clicking on the current value.
      hover (boolean):
        Provides visual feedback when hovering over icons.
      ripple (boolean):
        Applies the [v-ripple](/directives/ripple) directive.
      item_aria_label (string):
        The **aria-label** used for each item.
      empty_icon (enum):
        The icon displayed when empty.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      full_icon (enum):
        The icon displayed when full.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      half_increments (boolean):
        Allows the selection of half increments.
      item_label_position (string):
        Position of item labels. Accepts 'top' and 'bottom'.
      item_labels (string[]):
        Array of labels to display next to each item..
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRating", children, **kwargs)
        self._attr_names += [
            "length",
            ("model_value", "modelValue"),
            "density",
            "tag",
            "theme",
            "color",
            "name",
            "disabled",
            "size",
            ("active_color", "activeColor"),
            "readonly",
            "clearable",
            "hover",
            "ripple",
            ("item_aria_label", "itemAriaLabel"),
            ("empty_icon", "emptyIcon"),
            ("full_icon", "fullIcon"),
            ("half_increments", "halfIncrements"),
            ("item_label_position", "itemLabelPosition"),
            ("item_labels", "itemLabels"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VResponsive(HtmlElement):
    """
    Vuetify's VResponsive component.
    See more `info and examples <https://vuetifyjs.com/api/v-responsive>`_.

    Args:
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      content_class (any):
        Apply a custom class to the internal content element.
      inline (boolean):
        Display as an inline element instead of a block, also disables flex-grow.
      aspect_ratio (string, number):
        Sets a base aspect ratio, calculated as width/height. This will
        only set a **minimum** height, the component can still grow if
        it has a lot of content.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VResponsive", children, **kwargs)
        self._attr_names += [
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            ("content_class", "contentClass"),
            "inline",
            ("aspect_ratio", "aspectRatio"),
        ]
        self._event_names += []


class VRow(HtmlElement):
    """
    Vuetify's VRow component.
    See more `info and examples <https://vuetifyjs.com/api/v-row>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      align ('end', 'start', 'center', 'baseline', 'stretch'):
        Applies the [align-items](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items)
        css property. Available options are: **start**, **center**, **end**,
        **baseline** and **stretch**.
      dense (boolean):
        Reduces the gutter between `v-col`s.
      no_gutters (boolean):
        Removes the gutter between `v-col`s.
      align_sm ('end', 'start', 'center', 'baseline', 'stretch'):
        Changes the **align-items** property on small and greater breakpoints.
      align_md ('end', 'start', 'center', 'baseline', 'stretch'):
        Changes the **align-items** property on medium and greater breakpoints.
      align_lg ('end', 'start', 'center', 'baseline', 'stretch'):
        Changes the **align-items** property on large and greater breakpoints.
      align_xl ('end', 'start', 'center', 'baseline', 'stretch'):
        Changes the **align-items** property on extra large and greater breakpoints.
      align_xxl ('end', 'start', 'center', 'baseline', 'stretch'):
        Changes the **align-items** property on extra extra large and
        greater breakpoints.
      justify_sm (enum):
        Changes the **justify-content** property on small and greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'space-between', 'space-around', 'space-evenly'
        ]
      justify_md (enum):
        Changes the **justify-content** property on medium and greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'space-between', 'space-around', 'space-evenly'
        ]
      justify_lg (enum):
        Changes the **justify-content** property on large and greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'space-between', 'space-around', 'space-evenly'
        ]
      justify_xl (enum):
        Changes the **justify-content** property on extra large and greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'space-between', 'space-around', 'space-evenly'
        ]
      justify_xxl (enum):
        Changes the **justify-content** property on extra extra large
        and greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'space-between', 'space-around', 'space-evenly'
        ]
      align_content_sm (enum):
        Changes the **align-content** property on small and greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'stretch', 'space-between', 'space-around',
          'space-evenly'
        ]
      align_content_md (enum):
        Changes the **align-content** property on medium and greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'stretch', 'space-between', 'space-around',
          'space-evenly'
        ]
      align_content_lg (enum):
        Changes the **align-content** property on large and greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'stretch', 'space-between', 'space-around',
          'space-evenly'
        ]
      align_content_xl (enum):
        Changes the **align-content** property on extra large and greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'stretch', 'space-between', 'space-around',
          'space-evenly'
        ]
      align_content_xxl (enum):
        Changes the **align-content** property on extra extra large and
        greater breakpoints.

        Enum values: [
          'end', 'start', 'center', 'stretch', 'space-between', 'space-around',
          'space-evenly'
        ]
      justify (enum):
        Applies the [justify-content](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)
        css property. Available options are: **start**, **center**, **end**,
        **space-between** and **space-around**.

        Enum values: [
          'end', 'start', 'center', 'stretch', 'space-between', 'space-around',
          'space-evenly'
        ]
      align_content (enum):
        Applies the [align-content](https://developer.mozilla.org/en-US/docs/Web/CSS/align-content)
        css property. Available options are: **start**, **center**, **end**,
        **space-between**, **space-around** and **stretch**.

        Enum values: [
          'end', 'start', 'center', 'stretch', 'space-between', 'space-around',
          'space-evenly'
        ]
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRow", children, **kwargs)
        self._attr_names += [
            "tag",
            "align",
            "dense",
            ("no_gutters", "noGutters"),
            ("align_sm", "alignSm"),
            ("align_md", "alignMd"),
            ("align_lg", "alignLg"),
            ("align_xl", "alignXl"),
            ("align_xxl", "alignXxl"),
            ("justify_sm", "justifySm"),
            ("justify_md", "justifyMd"),
            ("justify_lg", "justifyLg"),
            ("justify_xl", "justifyXl"),
            ("justify_xxl", "justifyXxl"),
            ("align_content_sm", "alignContentSm"),
            ("align_content_md", "alignContentMd"),
            ("align_content_lg", "alignContentLg"),
            ("align_content_xl", "alignContentXl"),
            ("align_content_xxl", "alignContentXxl"),
            "justify",
            ("align_content", "alignContent"),
        ]
        self._event_names += []


class VScaleTransition(HtmlElement):
    """
    Vuetify's VScaleTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scale-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScaleTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VScrollXReverseTransition(HtmlElement):
    """
    Vuetify's VScrollXReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scroll-x-reverse-transition>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollXReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VScrollXTransition(HtmlElement):
    """
    Vuetify's VScrollXTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scroll-x-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollXTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VScrollYReverseTransition(HtmlElement):
    """
    Vuetify's VScrollYReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scroll-y-reverse-transition>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollYReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VScrollYTransition(HtmlElement):
    """
    Vuetify's VScrollYTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scroll-y-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollYTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSelect(HtmlElement):
    """
    Vuetify's VSelect component.
    See more `info and examples <https://vuetifyjs.com/api/v-select>`_.

    Args:
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      type (string):
        Sets input type.
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      reverse (boolean):
        Reverses the orientation.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width of the select's `v-menu` content.
      width (string, number):
        Sets the width for the component.
      rounded (string, number, boolean):
        Adds a border radius to the input.
      tile (boolean):
        Removes any applied **border-radius** from the component.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      name (string):
        Sets the component's name attribute.
      autocomplete (string):
        Helps influence browser's suggestions. Special value **suppress**
        manipulates fields `name` attribute while **off** relies on browser's
        good will to stop suggesting values. Any other value is passed
        to the native `autocomplete` on the underlying element.
      disabled (boolean):
        Removes the ability to click or target the input.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      placeholder (string):
        Sets the input’s placeholder text.
      id (string):
        Sets the DOM id on the component.
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      autofocus (boolean):
        Enables autofocus.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      chips (boolean):
        Changes display of selections to chips.
      closable_chips (boolean):
        Enables the [closable](/api/v-chip/#props-closable) prop on all
        [v-chip](/components/chips/) components.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      hide_selected (boolean):
        Do not display in the select menu items that are already selected.
      list_props (unknown):
        Pass props through to the `v-list` component. Accepts an object
        with anything from [v-list](/api/v-list/#props) props, camelCase
        keys are recommended.
      base_color (string):
        Sets the color of the input when it is not focused.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      items (any[]):
        Can be an array of objects or strings. By default objects should
        have **title** and **value** properties, and can optionally have
        a **props** property containing any [VListItem props](/api/v-list-item/#props).
        Keys to use for these can be changed with the **item-title**,
        **item-value**, and **item-props** props.
      item_title (SelectItemKey):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey):
        Set property of **items**'s value - **must be primitive**. Dot
        notation is supported. **Note:** This is currently not supported
        with `v-combobox` [GitHub Issue](https://github.com/vuetifyjs/vuetify/issues/5479).
      item_children (SelectItemKey):
        This property currently has **no effect**.
      item_props (SelectItemKey):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      item_type (SelectItemKey):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/list-items.json))
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3888: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      menu (boolean):
        Renders with the menu open by default.
      menu_icon (enum):
        Sets the the spin icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      menu_props (unknown):
        Pass props through to the `v-menu` component. Accepts an object
        with anything from [v-menu](/api/v-menu/#props) props, camelCase
        keys are recommended.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          { component: Component }
        ]
      no_data_text (string):
        Text shown when no items are provided to the component.
      open_on_clear (boolean):
        When using the **clearable** prop, once cleared, the select menu
        will either open or stay open, depending on the current state.
      item_color (string):
        Sets color of selected items.
      no_auto_scroll (boolean):
        Prevents the select menu to scroll to the selected item automatically.
      close_text (string):
        Text set to the inputs `aria-label` and `title` when input menu is closed.
      open_text (string):
        Text set to the inputs **aria-label** and **title** when input menu is open.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outside the component's input, uses the
        same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      readonly (boolean):
        Puts input in readonly state.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      counter_value (number, js_fn):
        Function returns the counter display text.
      model_modifiers (unknown):
        **FOR INTERNAL USE ONLY**
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
      update_menu (event):
        Event that is emitted when the component's menu state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSelect", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            "flat",
            "type",
            ("model_value", "modelValue"),
            "error",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            "name",
            "autocomplete",
            "disabled",
            "multiple",
            "placeholder",
            "id",
            "prefix",
            "role",
            "autofocus",
            "label",
            "chips",
            ("closable_chips", "closableChips"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            ("list_props", "listProps"),
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("item_type", "itemType"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "transition",
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("item_color", "itemColor"),
            ("no_auto_scroll", "noAutoScroll"),
            ("close_text", "closeText"),
            ("open_text", "openText"),
            "counter",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "readonly",
            "rules",
            ("validate_on", "validateOn"),
            "focused",
            ("hide_details", "hideDetails"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "loading",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_menu", "update:menu"),
        ]


class VSelectionControl(HtmlElement):
    """
    Vuetify's VSelectionControl component.
    See more `info and examples <https://vuetifyjs.com/api/v-selection-control>`_.

    Args:
      type (string):
        Provides the default type for children selection controls.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the component.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of the input when it is not focused.
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      inline (boolean):
        Puts children inputs into a row.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      true_value (any):
        Sets value for truthy state.
      false_value (any):
        Sets value for falsy state.
      defaults_target (string):
        The target component to provide defaults values for.
      false_icon (enum):
        The icon used when inactive.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_icon (enum):
        The icon used when active.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3729: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSelectionControl", children, **kwargs)
        self._attr_names += [
            "type",
            "name",
            "error",
            "label",
            "disabled",
            "multiple",
            "value",
            "id",
            "theme",
            ("base_color", "baseColor"),
            "readonly",
            "ripple",
            "density",
            "color",
            "inline",
            ("model_value", "modelValue"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSelectionControlGroup(HtmlElement):
    """
    Vuetify's VSelectionControlGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-selection-control-group>`_.

    Args:
      type (string):
        Provides the default type for children selection controls.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      disabled (boolean):
        Removes the ability to click or target the component.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      inline (boolean):
        Puts children inputs into a row.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      defaults_target (string):
        The target component to provide defaults values for.
      false_icon (enum):
        The icon used when inactive.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_icon (enum):
        The icon used when active.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3729: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSelectionControlGroup", children, **kwargs)
        self._attr_names += [
            "type",
            "name",
            "error",
            "disabled",
            "multiple",
            "id",
            "theme",
            "readonly",
            "ripple",
            "density",
            "color",
            "inline",
            ("model_value", "modelValue"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSheet(HtmlElement):
    """
    Vuetify's VSheet component.
    See more `info and examples <https://vuetifyjs.com/api/v-sheet>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSheet", children, **kwargs)
        self._attr_names += [
            "tag",
            "height",
            "width",
            "theme",
            "border",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "location",
            "position",
            "rounded",
            "tile",
            "color",
        ]
        self._event_names += []


class VSkeletonLoader(HtmlElement):
    """
    Vuetify's VSkeletonLoader component.
    See more `info and examples <https://vuetifyjs.com/api/v-skeleton-loader>`_.

    Args:
      type (enum):
        A string delimited list of skeleton components to create such
        as `type="text@3"` or `type="card, list-item"`. Will recursively
        generate a corresponding skeleton from the provided string. Also
        supports short-hand for multiple elements such as **article@3**
        and **paragraph@2** which will generate 3 _article_ skeletons
        and 2 _paragraph_ skeletons. Please see below for a list of available
        pre-defined options.

        Enum values: [
          (string & {}), 'article', 'button', 'table', 'text', 'image',
          'actions', 'avatar', 'divider', 'subtitle', 'chip', 'heading',
          'sentences', 'paragraph', 'ossein', 'card', 'card-avatar', 'date-picker',
          'date-picker-options', 'date-picker-days', 'list-item', 'list-item-avatar',
          'list-item-two-line', 'list-item-avatar-two-line', 'list-item-three-line',
          'list-item-avatar-three-line', 'table-heading', 'table-thead',
          'table-tbody', 'table-row-divider', 'table-row', 'table-tfoot',
          (, (string & {}), 'article', 'button', 'table', 'text', 'image',
          'actions', 'avatar', 'divider', 'subtitle', 'chip', 'heading',
          'sentences', 'paragraph', 'ossein', 'card', 'card-avatar', 'date-picker',
          'date-picker-options', 'date-picker-days', 'list-item', 'list-item-avatar',
          'list-item-two-line', 'list-item-avatar-two-line', 'list-item-three-line',
          'list-item-avatar-three-line', 'table-heading', 'table-thead',
          'table-tbody', 'table-row-divider', 'table-row', 'table-tfoot'
             )[]
        ]
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      loading (boolean):
        Applies a loading animation with a on-hover loading cursor. A
        value of **false** will only work when there is content in the
        `default` slot.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      boilerplate (boolean):
        Remove the loading animation from the skeleton.
      loading_text (string):
        aria-label for the element in a loading state.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSkeletonLoader", children, **kwargs)
        self._attr_names += [
            "type",
            "height",
            "width",
            "theme",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "loading",
            "color",
            "boilerplate",
            ("loading_text", "loadingText"),
        ]
        self._event_names += []


class VSlideGroup(HtmlElement):
    """
    Vuetify's VSlideGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-group>`_.

    Args:
      symbol (any):
        The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
        used to hook into group functionality for components like [v-btn-toggle](/components/btn-toggle)
        and [v-bottom-navigation](/components/bottom-navigations/).
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Puts all children components into a disabled state.
      max (number):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allows one to select multiple items.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Sets the designated mobile breakpoint for the component.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      content_class (any):
        Adds classes to the slide group item.
      direction ('horizontal', 'vertical'):
        Switch between horizontal and vertical modes.
      next_icon (enum):
        The appended slot when arrows are shown.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        The prepended slot when arrows are shown.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      show_arrows (string, boolean):
        Change when the overflow arrow indicators are shown. By **default**,
        arrows *always* display on Desktop when the container is overflowing.
        When the container overflows on mobile, arrows are not shown
        by default. A **show-arrows** value of `true` allows these arrows
        to show on Mobile if the container overflowing. A value of `desktop`
        *always* displays arrows on Desktop while a value of `mobile`
        always displays arrows on Mobile. A value of `always` always
        displays arrows on Desktop *and* Mobile. Use **never** to turn
        arrows off. Find more information on how to customize breakpoint
        thresholds on the [breakpoints page](/customizing/breakpoints).
      center_active (boolean):
        Forces the selected component to be centered.
      scroll_to_active (boolean):
        Keeps the last active element visible when resizing the scrollable container.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideGroup", children, **kwargs)
        self._attr_names += [
            "symbol",
            "tag",
            "disabled",
            "max",
            "multiple",
            ("selected_class", "selectedClass"),
            ("model_value", "modelValue"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "mandatory",
            ("content_class", "contentClass"),
            "direction",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            ("center_active", "centerActive"),
            ("scroll_to_active", "scrollToActive"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSlideGroupItem(HtmlElement):
    """
    Vuetify's VSlideGroupItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-group-item>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideGroupItem", children, **kwargs)
        self._attr_names += [
            "disabled",
            "value",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VSlideXReverseTransition(HtmlElement):
    """
    Vuetify's VSlideXReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-x-reverse-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideXReverseTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlideXTransition(HtmlElement):
    """
    Vuetify's VSlideXTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-x-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideXTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlideYReverseTransition(HtmlElement):
    """
    Vuetify's VSlideYReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-y-reverse-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideYReverseTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlideYTransition(HtmlElement):
    """
    Vuetify's VSlideYTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-y-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      disabled (boolean):
        Removes the ability to click or target the component.
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation).
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideYTransition", children, **kwargs)
        self._attr_names += [
            "mode",
            "disabled",
            "group",
            "origin",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlider(HtmlElement):
    """
    Vuetify's VSlider component.
    See more `info and examples <https://vuetifyjs.com/api/v-slider>`_.

    Args:
      reverse (boolean):
        Reverses the slider direction.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the component.
      max (string, number):
        Sets the maximum allowed value.
      min (string, number):
        Sets the minimum allowed value.
      step (string, number):
        If greater than 0, sets step interval for ticks.
      width (string, number):
        Sets the width for the component.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean):
        Applies the [v-ripple](/directives/ripple) directive.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (string, number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the input is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      thumb_color (string):
        Sets the thumb and thumb label color.
      thumb_label (boolean, 'always'):
        Show thumb label. If `true` it shows label when using slider.
        If set to `'always'` it always shows label.
      thumb_size (string, number):
        Controls the size of the thumb label.
      show_ticks (boolean, 'always'):
        Show track ticks. If `true` it shows ticks when using slider.
        If set to `'always'` it always shows ticks.
      ticks (number[], Record<number, string>):
        Show track ticks. If `true` it shows ticks when using slider.
        If set to `'always'` it always shows ticks.
      tick_size (string, number):
        Controls the size of **ticks**
      track_color (string):
        Sets the track's color
      track_fill_color (string):
        Sets the track's fill color
      track_size (string, number):
        Sets the track's size (height).
      no_keyboard (boolean):
        **FOR INTERNAL USE ONLY** Ignore keyboard events.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when appended icon is clicked.
      update_focused (event):
        Event that is emitted when the component's focus state changes.
      start (event):
        Slider value emitted at start of slider movement.
      end (event):
        Slider value emitted at the end of slider movement.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlider", children, **kwargs)
        self._attr_names += [
            "reverse",
            "name",
            "error",
            "label",
            "disabled",
            "max",
            "min",
            "step",
            "width",
            "id",
            "theme",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "ripple",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "elevation",
            "rounded",
            "tile",
            "color",
            ("model_value", "modelValue"),
            "direction",
            "messages",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("thumb_color", "thumbColor"),
            ("thumb_label", "thumbLabel"),
            ("thumb_size", "thumbSize"),
            ("show_ticks", "showTicks"),
            "ticks",
            ("tick_size", "tickSize"),
            ("track_color", "trackColor"),
            ("track_fill_color", "trackFillColor"),
            ("track_size", "trackSize"),
            ("no_keyboard", "noKeyboard"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            "start",
            "end",
        ]


class VSnackbar(HtmlElement):
    """
    Vuetify's VSnackbar component.
    See more `info and examples <https://vuetifyjs.com/api/v-snackbar>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      text (string):
        Specify content text for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      location (Anchor):
        Specifies the anchor point for positioning the component, using
        directional cues to align it either horizontally, vertically,
        or both..
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      absolute (boolean):
        Applies **position: absolute** to the content element.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      close_on_back (boolean):
        Closes the overlay content when the browser's back button is
        pressed or `$router.back()` is called, cancelling the original
        navigation. `persistent` overlays will cancel navigation and
        animate as if they were clicked outside instead of closing.
      contained (boolean):
        Limits the size of the component and scrim to its offset parent.
        Implies `absolute` and `attach`. (Note: The parent element must
        have position: relative.).
      content_class (any):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      content_props (any):
        Apply custom properties to the content.
      opacity (string, number):
        Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
      z_index (string, number):
        The z-index used for the component.
      target (enum):
        For locationStrategy="connected", specify an element or array
        of x,y coordinates that the overlay should position itself relative
        to. This will be the activator element by default.

        Enum values: [
          Element, (string & {}), 'parent', 'cursor', ComponentPublicInstance,
          [number, number]
        ]
      activator_props (unknown):
        Apply custom properties to the activator.
      open_on_click (boolean):
        Activate the component when the activator is clicked.
      open_on_hover (boolean):
        Activate the component when the activator is hovered.
      open_on_focus (boolean):
        Activate the component when the activator is focused.
      close_on_content_click (boolean):
        Closes component when you click on its content.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        Increases distance from the target. When passed as a pair of
        numbers, the second value shifts anchor along the side and away
        from the target.
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default.
      vertical (boolean):
        Stacks snackbar content on top of the actions (button).
      multi_line (boolean):
        Deprecated, use `min-height` instead. Increases minimum height.
      timer (string, boolean):
        Display a progress bar that counts down until the snackbar closes.
        Pass a string to set a custom color, otherwise uses `info`.
      timeout (string, number):
        Time (in milliseconds) to wait until snackbar is automatically
        hidden.  Use `-1` to keep open indefinitely (`0` in version <
        2.3 ). It is recommended for this number to be between `4000`
        and `10000`. Changes to this property will reset the timeout.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSnackbar", children, **kwargs)
        self._attr_names += [
            "disabled",
            "height",
            "width",
            "theme",
            "text",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "location",
            "position",
            "absolute",
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            "transition",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "opacity",
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "eager",
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            "attach",
            "vertical",
            ("multi_line", "multiLine"),
            "timer",
            "timeout",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSnackbarQueue(HtmlElement):
    """
    Vuetify's VSnackbarQueue component.
    See more `info and examples <https://vuetifyjs.com/api/v-snackbar-queue>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      text (string):
        Specify content text for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      location (Anchor):
        Specifies the anchor point for positioning the component, using
        directional cues to align it either horizontally, vertically,
        or both..
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      absolute (boolean):
        Applies **position: absolute** to the content element.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      model_value (Anchor):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      close_on_back (boolean):
        Closes the overlay content when the browser's back button is
        pressed or `$router.back()` is called, cancelling the original
        navigation. `persistent` overlays will cancel navigation and
        animate as if they were clicked outside instead of closing.
      contained (boolean):
        Limits the size of the component and scrim to its offset parent.
        Implies `absolute` and `attach`. (Note: The parent element must
        have position: relative.).
      content_class (any):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      content_props (any):
        Apply custom properties to the content.
      opacity (string, number):
        Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
      z_index (string, number):
        The z-index used for the component.
      target (enum):
        For locationStrategy="connected", specify an element or array
        of x,y coordinates that the overlay should position itself relative
        to. This will be the activator element by default.

        Enum values: [
          Element, (string & {}), 'parent', 'cursor', ComponentPublicInstance,
          [number, number]
        ]
      activator_props (unknown):
        Apply custom properties to the activator.
      open_on_click (boolean):
        Activate the component when the activator is clicked.
      open_on_hover (boolean):
        Activate the component when the activator is hovered.
      open_on_focus (boolean):
        Activate the component when the activator is focused.
      close_on_content_click (boolean):
        Closes component when you click on its content.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        Increases distance from the target. When passed as a pair of
        numbers, the second value shifts anchor along the side and away
        from the target.
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default.
      vertical (boolean):
        Stacks snackbar content on top of the actions (button).
      closable (string, boolean):
        Adds a dismiss button that closes the active snackbar.
      close_text (string):
        The text used in the close button when using the **closable** prop.
      multi_line (boolean):
        Deprecated, use `min-height` instead. Increases minimum height.
      timer (string, boolean):
        Display a progress bar that counts down until the snackbar closes.
        Pass a string to set a custom color, otherwise uses `info`.
      timeout (string, number):
        Time (in milliseconds) to wait until snackbar is automatically
        hidden.  Use `-1` to keep open indefinitely (`0` in version <
        2.3 ). It is recommended for this number to be between `4000`
        and `10000`. Changes to this property will reset the timeout.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSnackbarQueue", children, **kwargs)
        self._attr_names += [
            "disabled",
            "height",
            "width",
            "theme",
            "text",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "location",
            "position",
            "absolute",
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            "transition",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "opacity",
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "eager",
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            "attach",
            "vertical",
            "closable",
            ("close_text", "closeText"),
            ("multi_line", "multiLine"),
            "timer",
            "timeout",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSpacer(HtmlElement):
    """
    Vuetify's VSpacer component.
    See more `info and examples <https://vuetifyjs.com/api/v-spacer>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSpacer", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VSparkline(HtmlElement):
    """
    Vuetify's VSparkline component.
    See more `info and examples <https://vuetifyjs.com/api/v-sparkline>`_.

    Args:
      type ('trend', 'bar'):
        Choose between a trendline or bars.
      fill (boolean):
        Using the **fill** property allows you to better customize the
        look and feel of your sparkline.
      height (string, number):
        Height of the SVG trendline or bars.
      labels ((string, number, { value: number })[]):
        An array of string labels that correspond to the same index as
        its data counterpart.
      max (string, number):
        The maximum value of the sparkline.
      min (string, number):
        The minimum value of the sparkline.
      width (string, number):
        Width of the SVG trendline or bars.
      id (string):
        The id of the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value ((string, number, { value: number })[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      gradient (string[]):
        An array of colors to use as a linear-gradient.
      item_value (string):
        The value of the item.
      auto_line_width (boolean):
        Automatically expand bars to use space efficiently.
      auto_draw (boolean):
        Trace the length of the line when first rendered.
      auto_draw_duration (string, number):
        Amount of time (in ms) to run the trace animation.
      auto_draw_easing (string):
        The easing function to use for the trace animation.
      gradient_direction ('top', 'left', 'right', 'bottom'):
        The direction the gradient should run.
      label_size (string, number):
        The label font size.
      line_width (string, number):
        The thickness of the line, in px.
      padding (string, number):
        Low `smooth` or high `line-width` values may result in cropping,
        increase padding to compensate.
      show_labels (boolean):
        Show labels below each data point.
      smooth (string, number, boolean):
        Number of px to use as a corner radius. `true` defaults to 8, `false` is 0.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSparkline", children, **kwargs)
        self._attr_names += [
            "type",
            "fill",
            "height",
            "labels",
            "max",
            "min",
            "width",
            "id",
            "color",
            ("model_value", "modelValue"),
            "gradient",
            ("item_value", "itemValue"),
            ("auto_line_width", "autoLineWidth"),
            ("auto_draw", "autoDraw"),
            ("auto_draw_duration", "autoDrawDuration"),
            ("auto_draw_easing", "autoDrawEasing"),
            ("gradient_direction", "gradientDirection"),
            ("label_size", "labelSize"),
            ("line_width", "lineWidth"),
            "padding",
            ("show_labels", "showLabels"),
            "smooth",
        ]
        self._event_names += []


class VSpeedDial(HtmlElement):
    """
    Vuetify's VSpeedDial component.
    See more `info and examples <https://vuetifyjs.com/api/v-speed-dial>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      id (string):
        The unique identifier of the component.
      theme (string):
        Specify a theme for this component and all of its children.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      location (Anchor):
        Specifies the anchor point for positioning the component, using
        directional cues to align it either horizontally, vertically,
        or both..
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          {      component: ComponentPublicInstanceConstructor<
          CreateComponentPublicInstanceWithMixins<          {} & { target?:
          HTMLElement, [x: number, y: number], undefined } & {
             $children?:, VNodeChild, { $stable?: boolean, undefined },
          js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn, [x: number, y: number], undefined } & {
                     $children?:, VNodeChild, { $stable?: boolean, undefined
          }, js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn, [x: number, y: number], undefined } & {
                     $children?:, VNodeChild, { $stable?: boolean, undefined
          }, js_fn, js_fn, undefined }            'v-slots'?:, { default?:
          false, js_fn, undefined }, undefined          } & { 'v-slot:default'?:
          false, js_fn, js_fn
        ]
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      close_on_back (boolean):
        Closes the overlay content when the browser's back button is
        pressed or `$router.back()` is called, cancelling the original
        navigation. `persistent` overlays will cancel navigation and
        animate as if they were clicked outside instead of closing.
      contained (boolean):
        Limits the size of the component and scrim to its offset parent.
        Implies `absolute` and `attach`. (Note: The parent element must
        have position: relative.).
      content_class (any):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      content_props (any):
        Apply custom properties to the content.
      opacity (string, number):
        Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
      no_click_animation (boolean):
        Disables the bounce effect when clicking outside of the content
        element when using the persistent prop.
      persistent (boolean):
        Clicking outside of the element or pressing esc key will not deactivate it.
      scrim (string, boolean):
        Accepts true/false to enable background, and string to define color.
      z_index (string, number):
        The z-index used for the component.
      target (enum):
        For locationStrategy="connected", specify an element or array
        of x,y coordinates that the overlay should position itself relative
        to. This will be the activator element by default.

        Enum values: [
          Element, (string & {}), 'parent', 'cursor', ComponentPublicInstance,
          [number, number]
        ]
      activator_props (unknown):
        Apply custom properties to the activator.
      open_on_click (boolean):
        Designates whether menu should open on activator click.
      open_on_hover (boolean):
        Opens speed-dial on hover.
      open_on_focus (boolean):
        Activate the component when the activator is focused.
      close_on_content_click (boolean):
        Designates if menu should close when its content is clicked.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only works with
        the **open-on-hover** prop.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only works with
        the **open-on-hover** prop.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        Increases distance from the target. When passed as a pair of
        numbers, the second value shifts anchor along the side and away
        from the target.
      stick_to_target (boolean):
        Enables the overlay content to go off-screen when scrolling.
      viewport_margin (string, number):
        Sets custom viewport margin for the overlay content
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
      retain_focus (boolean):
        Captures and keeps focus within the content element when using
        **Tab** and **Shift**+**Tab**. Recommended to be `false` when
        using external tools that require focus such as TinyMCE or vue-clipboard.
      capture_focus (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/focusTrap.json))
      disable_initial_focus (boolean):
        Deprecated, use `capture-focus` instead. Prevents automatic redirect
        of first `focusin` event. Intended to use on permanently open
        menus or VSpeedDial.
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default.
      submenu (boolean):
        Opens with right arrow and closes on left instead of up/down.
        Implies `location="end"`. Directions are reversed for RTL.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSpeedDial", children, **kwargs)
        self._attr_names += [
            "disabled",
            "height",
            "width",
            "id",
            "theme",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "location",
            ("model_value", "modelValue"),
            "transition",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            "persistent",
            "scrim",
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "eager",
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            ("stick_to_target", "stickToTarget"),
            ("viewport_margin", "viewportMargin"),
            ("scroll_strategy", "scrollStrategy"),
            ("retain_focus", "retainFocus"),
            ("capture_focus", "captureFocus"),
            ("disable_initial_focus", "disableInitialFocus"),
            "attach",
            "submenu",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VStepper(HtmlElement):
    """
    Vuetify's VStepper component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper>`_.

    Args:
      flat (boolean):
        Removes the stepper's elevation.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Puts all children components into a disabled state.
      height (string, number):
        Sets the height for the component.
      max (number):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allows one to select multiple items.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      items ((string, Record<string, any>)[]):
        An array of strings or objects used for automatically generating
        children components.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'relative', 'static', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      mobile (boolean):
        Forces the stepper into a mobile state, removing labels from stepper items.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      item_props (SelectItemKey):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      item_title (SelectItemKey):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      hide_actions (boolean):
        Hide actions bar (prev and next buttons).
      alt_labels (boolean):
        Places the labels beneath the step.
      complete_icon (enum):
        Icon to display when step is marked as completed.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      edit_icon (enum):
        Icon to display when step is editable.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      editable (boolean):
        Marks step as editable.
      error_icon (enum):
        Icon to display when step has an error.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      non_linear (boolean):
        Allow user to jump to any step.
      prev_text (string):
        The text used for the Prev button.
      next_text (string):
        The text used for the Next button.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepper", children, **kwargs)
        self._attr_names += [
            "flat",
            "tag",
            "disabled",
            "height",
            "max",
            "multiple",
            "width",
            "theme",
            "items",
            "border",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            ("selected_class", "selectedClass"),
            "location",
            "position",
            "rounded",
            "tile",
            "color",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "mandatory",
            ("item_props", "itemProps"),
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("hide_actions", "hideActions"),
            ("alt_labels", "altLabels"),
            ("complete_icon", "completeIcon"),
            ("edit_icon", "editIcon"),
            "editable",
            ("error_icon", "errorIcon"),
            ("non_linear", "nonLinear"),
            ("prev_text", "prevText"),
            ("next_text", "nextText"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VStepperActions(HtmlElement):
    """
    Vuetify's VStepperActions component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-actions>`_.

    Args:
      disabled (boolean, 'prev', 'next'):
        Removes the ability to click or target the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      prev_text (string):
        The text used for the Prev button.
      next_text (string):
        The text used for the Next button.
      click_prev (event):
        Event emitted when clicking the prev button.
      click_next (event):
        Event emitted when clicking the next button.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperActions", children, **kwargs)
        self._attr_names += [
            "disabled",
            "color",
            ("prev_text", "prevText"),
            ("next_text", "nextText"),
        ]
        self._event_names += [
            ("click_prev", "click:prev"),
            ("click_next", "click:next"),
        ]


class VStepperHeader(HtmlElement):
    """
    Vuetify's VStepperHeader component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-header>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperHeader", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VStepperItem(HtmlElement):
    """
    Vuetify's VStepperItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-item>`_.

    Args:
      error (boolean):
        Puts the stepper item in a manual error state.
      title (string):
        Specify a title text for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      subtitle (string):
        Specify a subtitle text for the component.
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
      complete_icon (enum):
        Icon to display when step is marked as completed.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      edit_icon (enum):
        Icon to display when step is editable.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      editable (boolean):
        Marks step as editable.
      error_icon (enum):
        Icon to display when step has an error.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      complete (boolean):
        Marks step as complete.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperItem", children, **kwargs)
        self._attr_names += [
            "error",
            "title",
            "disabled",
            "value",
            "ripple",
            ("selected_class", "selectedClass"),
            "color",
            "icon",
            "subtitle",
            "rules",
            ("complete_icon", "completeIcon"),
            ("edit_icon", "editIcon"),
            "editable",
            ("error_icon", "errorIcon"),
            "complete",
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VStepperVertical(HtmlElement):
    """
    Vuetify's VStepperVertical component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-vertical>`_.

    Args:
      flat (boolean):
        Removes the expansion-panel's elevation and borders.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Puts all children components into a disabled state.
      max (number):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allows one to select multiple items.
      theme (string):
        Specify a theme for this component and all of its children.
      items ((string, Record<string, any>)[]):
        An array of strings or objects used for automatically generating
        children components.
      readonly (boolean):
        Makes the entire expansion panel read only.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes the border-radius.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('default', 'inset', 'accordion', 'popout'):
        Applies a distinct style to the component.
      model_value (unknown):
        Controls expanded panel(s). Defaults to an empty array when using
        **multiple** prop. It is recommended to set unique `value` prop
        for the panels inside, otherwise index is used instead.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      mobile (boolean):
        Forces the stepper into a mobile state, removing labels from stepper items.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      item_props (SelectItemKey):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      expand_icon (enum):
        Icon used when the expansion panel is in a expandable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon used when the expansion panel is in a collapsable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      item_title (SelectItemKey):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      hide_actions (boolean):
        Hide actions bar (prev and next buttons).
      focusable (boolean):
        Makes the expansion-panel headers focusable.
      alt_labels (boolean):
        Places the labels beneath the step.
      complete_icon (enum):
        Icon to display when step is marked as completed.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      edit_icon (enum):
        Icon to display when step is editable.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      editable (boolean):
        Marks step as editable.
      error_icon (enum):
        Icon to display when step has an error.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      non_linear (boolean):
        Allow user to jump to any step.
      prev_text (string):
        The text used for the Prev button.
      next_text (string):
        The text used for the Next button.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperVertical", children, **kwargs)
        self._attr_names += [
            "flat",
            "tag",
            "disabled",
            "max",
            "multiple",
            "theme",
            "items",
            "readonly",
            "ripple",
            "elevation",
            ("selected_class", "selectedClass"),
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "mandatory",
            "eager",
            ("item_props", "itemProps"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("hide_actions", "hideActions"),
            "focusable",
            ("alt_labels", "altLabels"),
            ("complete_icon", "completeIcon"),
            ("edit_icon", "editIcon"),
            "editable",
            ("error_icon", "errorIcon"),
            ("non_linear", "nonLinear"),
            ("prev_text", "prevText"),
            ("next_text", "nextText"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VStepperVerticalActions(HtmlElement):
    """
    Vuetify's VStepperVerticalActions component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-vertical-actions>`_.

    Args:
      disabled (boolean, 'prev', 'next'):
        Removes the ability to click or target the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      prev_text (string):
        The text used for the Prev button.
      next_text (string):
        The text used for the Next button.
      click_prev (event):
        Event emitted when clicking the prev button.
      click_next (event):
        Event emitted when clicking the next button.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperVerticalActions", children, **kwargs)
        self._attr_names += [
            "disabled",
            "color",
            ("prev_text", "prevText"),
            ("next_text", "nextText"),
        ]
        self._event_names += [
            ("click_prev", "click:prev"),
            ("click_next", "click:next"),
        ]


class VStepperVerticalItem(HtmlElement):
    """
    Vuetify's VStepperVerticalItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-vertical-item>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      error (boolean):
        Puts the stepper item in a manual error state.
      title (string):
        Specify a title text for the component.
      disabled (boolean):
        Disables the expansion-panel content.
      height (string, number):
        Sets the height for the component.
      value (any):
        Controls the opened/closed state of content.
      width (string, number):
        Sets the width for the component.
      readonly (boolean):
        Makes the expansion panel content read only.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      text (string):
        Specify content text for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      static (boolean):
        Remove title size expansion when selected.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      subtitle (string):
        Specify a subtitle text for the component.
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
      expand_icon (enum):
        Icon used when the expansion panel is in a expandable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon used when the expansion panel is in a collapsable state.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_actions (boolean):
        Hide the expand icon in the content title.
      focusable (boolean):
        Makes the expansion panel content focusable.
      complete_icon (enum):
        Icon to display when step is marked as completed.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      edit_icon (enum):
        Icon to display when step is editable.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      editable (boolean):
        Marks step as editable.
      error_icon (enum):
        Icon to display when step has an error.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      complete (boolean):
        Marks step as complete.
      click_prev (event):
        Event emitted when clicking the previous button
      click_next (event):
        Event emitted when clicking the next button
      click_finish (event):
        Event emitted when clicking the finish button
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperVerticalItem", children, **kwargs)
        self._attr_names += [
            "tag",
            "error",
            "title",
            "disabled",
            "height",
            "value",
            "width",
            "readonly",
            "ripple",
            "text",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            ("selected_class", "selectedClass"),
            "static",
            "rounded",
            "tile",
            "color",
            "icon",
            ("bg_color", "bgColor"),
            "eager",
            "subtitle",
            "rules",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("hide_actions", "hideActions"),
            "focusable",
            ("complete_icon", "completeIcon"),
            ("edit_icon", "editIcon"),
            "editable",
            ("error_icon", "errorIcon"),
            "complete",
        ]
        self._event_names += [
            ("click_prev", "click:prev"),
            ("click_next", "click:next"),
            ("click_finish", "click:finish"),
        ]


class VStepperWindow(HtmlElement):
    """
    Vuetify's VStepperWindow component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-window>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      reverse (boolean):
        Reverse the normal transition direction.
      disabled (boolean):
        Removes the ability to click or target the component.
      theme (string):
        Specify a theme for this component and all of its children.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      direction ('horizontal', 'vertical'):
        The transition direction when changing windows.
      crossfade (boolean):
        Enables crossfade transition.
      transition_duration (number):
        Overrides transition duration.
      vertical_arrows (boolean, 'left', 'right'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VWindow.json))
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperWindow", children, **kwargs)
        self._attr_names += [
            "tag",
            "reverse",
            "disabled",
            "theme",
            ("selected_class", "selectedClass"),
            ("model_value", "modelValue"),
            "direction",
            "crossfade",
            ("transition_duration", "transitionDuration"),
            ("vertical_arrows", "verticalArrows"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VStepperWindowItem(HtmlElement):
    """
    Vuetify's VStepperWindowItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-window-item>`_.

    Args:
      disabled (boolean):
        Prevents the item from becoming active when using the "next"
        and "prev" buttons or the `toggle` method.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      transition (string, boolean):
        The transition used when the component progressing through items.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      reverse_transition (string, boolean):
        Sets the reverse transition.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperWindowItem", children, **kwargs)
        self._attr_names += [
            "disabled",
            "value",
            ("selected_class", "selectedClass"),
            "transition",
            "eager",
            ("reverse_transition", "reverseTransition"),
        ]
        self._event_names += []


class VSvgIcon(HtmlElement):
    """
    Vuetify's VSvgIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-svg-icon>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSvgIcon", children, **kwargs)
        self._attr_names += [
            "tag",
            "icon",
        ]
        self._event_names += []


class VSwitch(HtmlElement):
    """
    Vuetify's VSwitch component.
    See more `info and examples <https://vuetifyjs.com/api/v-switch>`_.

    Args:
      flat (boolean):
        Display component without elevation. Default elevation for thumb
        is 4dp, `flat` resets it.
      type (string):
        Provides the default type for children selection controls.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the component.
      indeterminate (boolean):
        Sets an indeterminate state for the switch.
      multiple (boolean):
        Changes expected model to an array.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      width (string, number):
        Sets the width for the component.
      id (string):
        Sets the DOM id on the component.
      theme (string):
        Specify a theme for this component and all of its children.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      loading (string, boolean):
        Displays circular progress bar. Can either be a String which
        specifies which color is applied to the progress bar (any material
        color or theme color - primary, secondary, success, info, warning,
        error) or a Boolean which uses the component color (set by color
        prop - if it's supported by the component) or the primary color.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      inline (boolean):
        Puts children inputs into a row.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      inset (boolean):
        Enlarge the `v-switch` track to encompass the thumb.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the input is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      true_value (any):
        Sets value for truthy state.
      false_value (any):
        Sets value for falsy state.
      defaults_target (string):
        The target component to provide defaults values for.
      false_icon (enum):
        The icon used when inactive.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_icon (enum):
        The icon used when active.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3729: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when appended icon is clicked.
      update_focused (event):
        Event that is emitted when the component's focus state changes.
      update_indeterminate (event):
        Event that is emitted when the component's indeterminate state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSwitch", children, **kwargs)
        self._attr_names += [
            "flat",
            "type",
            "name",
            "error",
            "label",
            "disabled",
            "indeterminate",
            "multiple",
            "value",
            "width",
            "id",
            "theme",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "ripple",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "loading",
            "color",
            "inline",
            ("model_value", "modelValue"),
            "inset",
            "direction",
            "messages",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("update_indeterminate", "update:indeterminate"),
        ]


class VSystemBar(HtmlElement):
    """
    Vuetify's VSystemBar component.
    See more `info and examples <https://vuetifyjs.com/api/v-system-bar>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      name (string):
        Assign a specific name for layout registration.
      height (string, number):
        Sets the height for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      absolute (boolean):
        Applies **position: absolute** to the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      order (string, number):
        Adjust the order of the component in relation to its registration order.
      window (boolean):
        Increases the system bar height to 32px (24px default).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSystemBar", children, **kwargs)
        self._attr_names += [
            "tag",
            "name",
            "height",
            "theme",
            "elevation",
            "absolute",
            "rounded",
            "tile",
            "color",
            "order",
            "window",
        ]
        self._event_names += []


class VTab(HtmlElement):
    """
    Vuetify's VTab component.
    See more `info and examples <https://vuetifyjs.com/api/v-tab>`_.

    Args:
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      fixed (boolean):
        Forces component to take up all available space up to their maximum
        width (300px), and centers it.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      active_color (string):
        The applied color when the component is in an active state.
      base_color (string):
        Sets the color of component when not focused.
      prepend_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend**
        slot before default content.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts the button in a readonly state. Cannot be clicked or navigated
        to by keyboard.
      slim (boolean):
        Reduces padding to 0 8px.
      stacked (boolean):
        Displays the tab as a flex-column.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      text (string, number, boolean):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/)
        component. The button will become _round_.

        Enum values: [
          boolean, string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      spaced ('start', 'end', 'both'):
        Extends content to the edges to move main content from prepend and append slots.
      inset (boolean):
        Changes the slider to take full height. Automatically propagated from VTabs.
      direction ('horizontal', 'vertical'):
        Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
      slider_color (string):
        Applies specified color to the slider when active on that component
        - supports utility colors (for example `success` or `purple`)
        or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list
        of built-in classes on the [colors page](/styles/colors#material-colors).
      slider_transition_duration (string, number):
        Applies custom slider transition duration. Default duration depends
        on transition type (fade: 400, grow: 350, shift: 225).
      hide_slider (boolean):
        Hides the active tab slider component (no exit or enter animation).
      slider_transition ('shift', 'grow', 'fade'):
        Changes slider transition to one of the predefined animation presets.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTab", children, **kwargs)
        self._attr_names += [
            "replace",
            "fixed",
            "tag",
            "disabled",
            "height",
            "size",
            "value",
            "width",
            "theme",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "slim",
            "stacked",
            "ripple",
            "text",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            ("selected_class", "selectedClass"),
            "loading",
            "rounded",
            "tile",
            "href",
            "exact",
            "to",
            "color",
            "variant",
            "icon",
            "spaced",
            "inset",
            "direction",
            ("slider_color", "sliderColor"),
            ("slider_transition_duration", "sliderTransitionDuration"),
            ("hide_slider", "hideSlider"),
            ("slider_transition", "sliderTransition"),
        ]
        self._event_names += []


class VTable(HtmlElement):
    """
    Vuetify's VTable component.
    See more `info and examples <https://vuetifyjs.com/api/v-table>`_.

    Args:
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Use the height prop to set the height of the table.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      fixed_header (boolean):
        Use the fixed-header prop together with the height prop to fix
        the header to the top of the table.
      fixed_footer (boolean):
        Use the fixed-footer prop together with the height prop to fix
        the footer to the bottom of the table.
      hover (boolean):
        Will add a hover effect to a table's row when the mouse is over it.
      striped ('odd', 'even'):
        Applies a background to either **even** or **odd** rows.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTable", children, **kwargs)
        self._attr_names += [
            "density",
            "height",
            "tag",
            "theme",
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            "hover",
            "striped",
        ]
        self._event_names += []


class VTabs(HtmlElement):
    """
    Vuetify's VTabs component.
    See more `info and examples <https://vuetifyjs.com/api/v-tabs>`_.

    Args:
      symbol (any):
        The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
        used to hook into group functionality for components like [v-btn-toggle](/components/btn-toggle)
        and [v-bottom-navigation](/components/bottom-navigations/).
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Sets the height of the tabs bar.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      color (string):
        Applies specified color to the selected tab - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      disabled (boolean):
        Puts all children components into a disabled state.
      max (number):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allows one to select multiple items.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      items (unknown[]):
        The items to display in the component. This can be an array of
        strings or objects with a property `text`.
      content_class (any):
        Adds classes to the slide group item.
      direction ('horizontal', 'vertical'):
        Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Sets the designated mobile breakpoint for the component.
      prev_icon (enum):
        Left pagination icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      next_icon (enum):
        Right pagination icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      align_tabs ('title', 'end', 'start', 'center'):
        Aligns the tabs to the `start`, `center`, or `end` of container.
        Also accepts `title` to align with the `v-toolbar-title` component.
      fixed_tabs (boolean):
        Tabs will be centered and each tab item will grow up to 300px width.
      stacked (boolean):
        Apply the stacked prop to all children v-tab components.
      grow (boolean):
        Forces tabs to take up all available space.
      hide_slider (boolean):
        Hide's the generated `v-tabs-slider`.
      inset (boolean):
        Changes the slider to take full height. Tabs will also get some
        spacing and customizable rounding.
      inset_padding (string, number):
        Sets custom spacing between tabs for `inset` mode.
      inset_radius (string, number):
        Sets custom border radius for the tabs container `inset` mode.
        Rounding for individual tabs is calculated by subtracting the
        padding.
      slider_color (string):
        Changes the background color of an auto-generated `v-tabs-slider`.
      slider_transition_duration (string, number):
        Applies custom slider transition duration. Default duration depends
        on transition type (fade: 400, grow: 350, shift: 225).
      spaced ('end', 'start', 'both'):
        Extends content to the edges to move main content from prepend and append slots.
      slider_transition ('shift', 'grow', 'fade'):
        Changes slider transition to one of the predefined animation presets.
      center_active (boolean):
        Forces the selected tab to be centered.
      scroll_to_active (boolean):
        Keeps the last active element visible when resizing the scrollable container.
      show_arrows (string, boolean):
        Show pagination arrows if the tab items overflow their container.
        For mobile devices, arrows will only display when using this
        prop.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTabs", children, **kwargs)
        self._attr_names += [
            "symbol",
            ("model_value", "modelValue"),
            "density",
            "height",
            "tag",
            "color",
            "disabled",
            "max",
            "multiple",
            ("bg_color", "bgColor"),
            "mandatory",
            "items",
            ("content_class", "contentClass"),
            "direction",
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("prev_icon", "prevIcon"),
            ("next_icon", "nextIcon"),
            ("selected_class", "selectedClass"),
            ("align_tabs", "alignTabs"),
            ("fixed_tabs", "fixedTabs"),
            "stacked",
            "grow",
            ("hide_slider", "hideSlider"),
            "inset",
            ("inset_padding", "insetPadding"),
            ("inset_radius", "insetRadius"),
            ("slider_color", "sliderColor"),
            ("slider_transition_duration", "sliderTransitionDuration"),
            "spaced",
            ("slider_transition", "sliderTransition"),
            ("center_active", "centerActive"),
            ("scroll_to_active", "scrollToActive"),
            ("show_arrows", "showArrows"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTabsWindow(HtmlElement):
    """
    Vuetify's VTabsWindow component.
    See more `info and examples <https://vuetifyjs.com/api/v-tabs-window>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      reverse (boolean):
        Reverse the normal transition direction.
      disabled (boolean):
        Removes the ability to click or target the component.
      theme (string):
        Specify a theme for this component and all of its children.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      direction ('horizontal', 'vertical'):
        The transition direction when changing windows.
      crossfade (boolean):
        Enables crossfade transition.
      transition_duration (number):
        Overrides transition duration.
      vertical_arrows (boolean, 'left', 'right'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VWindow.json))
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTabsWindow", children, **kwargs)
        self._attr_names += [
            "tag",
            "reverse",
            "disabled",
            "theme",
            ("selected_class", "selectedClass"),
            ("model_value", "modelValue"),
            "direction",
            "crossfade",
            ("transition_duration", "transitionDuration"),
            ("vertical_arrows", "verticalArrows"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTabsWindowItem(HtmlElement):
    """
    Vuetify's VTabsWindowItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-tabs-window-item>`_.

    Args:
      disabled (boolean):
        Prevents the item from becoming active when using the "next"
        and "prev" buttons or the `toggle` method.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      transition (string, boolean):
        The transition used when the component progressing through items.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      reverse_transition (string, boolean):
        Sets the reverse transition.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTabsWindowItem", children, **kwargs)
        self._attr_names += [
            "disabled",
            "value",
            ("selected_class", "selectedClass"),
            "transition",
            "eager",
            ("reverse_transition", "reverseTransition"),
        ]
        self._event_names += []


class VTextField(HtmlElement):
    """
    Vuetify's VTextField component.
    See more `info and examples <https://vuetifyjs.com/api/v-text-field>`_.

    Args:
      flat (boolean):
        Removes elevation (shadow) added to element when using the **solo**
        or **solo-inverted** props.
      type (string):
        Sets input type.
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      reverse (boolean):
        Reverses the input orientation.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      rounded (string, number, boolean):
        Adds a border radius to the input.
      tile (boolean):
        Removes any applied **border-radius** from the component.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      name (string):
        Sets the component's name attribute.
      autocomplete (string):
        Helps influence browser's suggestions. Special value **suppress**
        manipulates fields `name` attribute while **off** relies on browser's
        good will to stop suggesting values. Any other value is passed
        to the native `autocomplete` on the underlying element.
      disabled (boolean):
        Removes the ability to click or target the input.
      placeholder (string):
        Sets the input’s placeholder text.
      id (string):
        Sets the DOM id on the component.
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      autofocus (boolean):
        Enables autofocus.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outside the component's input, uses the
        same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      readonly (boolean):
        Puts input in readonly state.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      append_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **append-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        Applied when using **clearable** and the input is dirty.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      dirty (boolean):
        Manually apply the dirty state styling.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Prepends an icon inside the component's input, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      counter_value (number, js_fn):
        Function returns the counter display text.
      model_modifiers (unknown):
        **FOR INTERNAL USE ONLY**
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
      click_control (event):
        Emitted when the main input is clicked.
      mousedown_control (event):
        Event that is emitted when using mousedown on the main control area.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTextField", children, **kwargs)
        self._attr_names += [
            "flat",
            "type",
            ("model_value", "modelValue"),
            "error",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            "name",
            "autocomplete",
            "disabled",
            "placeholder",
            "id",
            "prefix",
            "role",
            "autofocus",
            "label",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "counter",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "readonly",
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "loading",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("click_control", "click:control"),
            ("mousedown_control", "mousedown:control"),
        ]


class VTextarea(HtmlElement):
    """
    Vuetify's VTextarea component.
    See more `info and examples <https://vuetifyjs.com/api/v-textarea>`_.

    Args:
      flat (boolean):
        Removes box shadow when using a variant with elevation.
      reverse (boolean):
        Reverses the orientation.
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      autocomplete (string):
        Helps influence browser's suggestions. Special value **suppress**
        manipulates fields `name` attribute while **off** relies on browser's
        good will to stop suggesting values. Any other value is passed
        to the native `autocomplete` on the underlying element.
      disabled (boolean):
        Removes the ability to click or target the input.
      placeholder (string):
        Sets the input's placeholder text.
      width (string, number):
        Sets the width for the component.
      id (string):
        Sets the DOM id on the component.
      prefix (string):
        Displays prefix text.
      autofocus (boolean):
        The element should be focused as soon as the page loads.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      readonly (boolean):
        Puts input in readonly state.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Alternative for **max-rows**. Specifies the maximum height in
        pixels (including the field padding) for **auto-grow**.
      max_width (string, number):
        Sets the maximum width for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant (enum):
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused
        and apply color.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      hide_details (boolean, 'auto'):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display.
      counter (string, number, true):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      append_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **append-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      clearable (boolean):
        Allows for the component to be cleared.
      clear_icon (enum):
        The icon used when the **clearable** prop is set to true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      dirty (boolean):
        Manually apply the dirty state styling.
      persistent_clear (boolean):
        Always show the clearable icon when the input is dirty (By default
        it only shows on hover).
      prepend_inner_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend-inner** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      single_line (boolean):
        Label does not move on focus/dirty.
      counter_value ((value: any) => number):
        Display the input length but do not provide any validation.
      model_modifiers (unknown):
        **FOR INTERNAL USE ONLY**
      auto_grow (boolean):
        Automatically grow the textarea depending on amount of text.
      no_resize (boolean):
        Remove resize handle.
      rows (string, number):
        Default row count.
      max_rows (string, number):
        Specifies the maximum number of rows for **auto-grow**.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when append icon is clicked.
      update_focused (event):
        Emitted when the input is focused or blurred
      click_clear (event):
        Emitted when clearable icon clicked.
      click_appendInner (event):
        Emitted when appended inner icon is clicked.
      click_prependInner (event):
        Emitted when prepended inner icon is clicked.
      click_control (event):
        Emitted when the main input is clicked.
      mousedown_control (event):
        Event that is emitted when using mousedown on the main control area.
      update_rows (event):
        Emitted when the number of rows changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTextarea", children, **kwargs)
        self._attr_names += [
            "flat",
            "reverse",
            "name",
            "error",
            "label",
            "autocomplete",
            "disabled",
            "placeholder",
            "width",
            "id",
            "prefix",
            "autofocus",
            "theme",
            "active",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "loading",
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "direction",
            "messages",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            "counter",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_inner_icon", "appendInnerIcon"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
            ("auto_grow", "autoGrow"),
            ("no_resize", "noResize"),
            "rows",
            ("max_rows", "maxRows"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("click_control", "click:control"),
            ("mousedown_control", "mousedown:control"),
            ("update_rows", "update:rows"),
        ]


class VThemeProvider(HtmlElement):
    """
    Vuetify's VThemeProvider component.
    See more `info and examples <https://vuetifyjs.com/api/v-theme-provider>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      with_background (boolean):
        Wraps its children in an element and applies the current theme's
        background color to it.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VThemeProvider", children, **kwargs)
        self._attr_names += [
            "tag",
            "theme",
            ("with_background", "withBackground"),
        ]
        self._event_names += []


class VTimePicker(HtmlElement):
    """
    Vuetify's VTimePicker component.
    See more `info and examples <https://vuetifyjs.com/api/v-time-picker>`_.

    Args:
      title (string):
        Specify a title text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Width of the picker.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location (Anchor):
        Specifies the component's location. Can combine by using a space
        separated string.
      position ('fixed', 'static', 'relative', 'absolute', 'sticky'):
        Sets the position for the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('input', 'dial'):
        Applies a distinct style to the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      max (string):
        Maximum allowed time.
      min (string):
        Minimum allowed time.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      readonly (boolean):
        Puts picker in readonly state.
      divided (boolean):
        Adds a divider between the header and controls.
      hide_header (boolean):
        Hide the picker header.
      hide_title (boolean):
        Hide the picker title.
      view_mode ('hour', 'minute', 'second'):
        The current view mode of the picker.`
      format ('ampm', '24hr'):
        Defines the format of a time displayed in picker. Available options
        are `ampm` and `24hr`.
      period ('am', 'pm'):
        Sets period for 12hr format.
      scrollable (boolean):
        Allows changing hour/minute with mouse scroll.
      use_seconds (boolean):
        Toggles the use of seconds in picker.
      allowed_hours (number[], js_fn):
        Restricts which hours can be selected.
      allowed_minutes (number[], js_fn):
        Restricts which minutes can be selected.
      allowed_seconds (number[], js_fn):
        Restricts which seconds can be selected.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_hour (event):
        Emitted when user selects the hour.
      update_minute (event):
        Emitted when user selects the minute.
      update_period (event):
        Emitted when user clicks the AM/PM button.
      update_second (event):
        Emitted when user selects the second.
      update_viewMode (event):
        Emitted when the view mode changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimePicker", children, **kwargs)
        self._attr_names += [
            "title",
            "border",
            ("model_value", "modelValue"),
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "location",
            "position",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            "disabled",
            "max",
            "min",
            ("bg_color", "bgColor"),
            "readonly",
            "divided",
            ("hide_header", "hideHeader"),
            ("hide_title", "hideTitle"),
            ("view_mode", "viewMode"),
            "format",
            "period",
            "scrollable",
            ("use_seconds", "useSeconds"),
            ("allowed_hours", "allowedHours"),
            ("allowed_minutes", "allowedMinutes"),
            ("allowed_seconds", "allowedSeconds"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_hour", "update:hour"),
            ("update_minute", "update:minute"),
            ("update_period", "update:period"),
            ("update_second", "update:second"),
            ("update_viewMode", "update:viewMode"),
        ]


class VTimePickerClock(HtmlElement):
    """
    Vuetify's VTimePickerClock component.
    See more `info and examples <https://vuetifyjs.com/api/v-time-picker-clock>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      max (number):
        Defines the maximum time value that can be selected.
      min (number):
        Defines the minimum time value that can be selected.
      step (number):
        Defines the increments between selectable times, such as a step
        of 1 for every minute or a larger step for every 5 or 15 minutes.
      readonly (boolean):
        When true, the picker is in a read-only state, and users cannot
        modify the selected time.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      scrollable (boolean):
        Allows the time selection to be scrollable, enhancing user experience
        for devices with scroll inputs.
      double (boolean):
        If set, this probably indicates a double rotation or a mode where
        more than one set of values (like hours and minutes) is displayed
        on the clock at the same time.
      rotate (number):
        Controls rotation, specifying the degree of rotation for the clock hands.
      ampm (boolean):
        Displays time in a 12-hour format.
      displayed_value (any):
        Used to display a custom value on the clock.
      format (Function):
        Specifies the format of the displayed time, either 12-hour or
        24-hour, depending on the component's setup.
      allowed_values ((value: number) => boolean):
        Restricts which hours can be selected.
      change (event):
        The event that is triggered when the selected time is changed.
      input (event):
        The updated bound model.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimePickerClock", children, **kwargs)
        self._attr_names += [
            "disabled",
            "max",
            "min",
            "step",
            "readonly",
            "color",
            ("model_value", "modelValue"),
            "scrollable",
            "double",
            "rotate",
            "ampm",
            ("displayed_value", "displayedValue"),
            "format",
            ("allowed_values", "allowedValues"),
        ]
        self._event_names += [
            "change",
            "input",
        ]


class VTimePickerControls(HtmlElement):
    """
    Vuetify's VTimePickerControls component.
    See more `info and examples <https://vuetifyjs.com/api/v-time-picker-controls>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      value (number):
        The current value of the timepicker.
      readonly (boolean):
        Makes the timepicker readonly.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      hour (string, number):
        The current hour value.
      minute (string, number):
        The current minute value.
      view_mode ('hour', 'minute', 'second'):
        The current view mode of the timepicker. Can be either `hour`,
        `minute`, or `second`.
      ampm (boolean):
        Enables AM/PM mode.
      use_seconds (boolean):
        Enables the display and selection of seconds in the timepicker.
      second (string, number):
        The current second value.
      period ('am', 'pm'):
        The current period value. either `am` or `pm`.
      update_viewMode (event):
        Emitted when the view mode is changed. The event payload is either
        `hour`, `minute`, or `second`.
      update_period (event):
        Emitted when the period is changed. The event payload is either `am` or `pm`.
      update_hour (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      update_minute (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      update_second (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimePickerControls", children, **kwargs)
        self._attr_names += [
            "disabled",
            "value",
            "readonly",
            "color",
            "hour",
            "minute",
            ("view_mode", "viewMode"),
            "ampm",
            ("use_seconds", "useSeconds"),
            "second",
            "period",
        ]
        self._event_names += [
            ("update_viewMode", "update:viewMode"),
            ("update_period", "update:period"),
            ("update_hour", "update:hour"),
            ("update_minute", "update:minute"),
            ("update_second", "update:second"),
        ]


class VTimeline(HtmlElement):
    """
    Vuetify's VTimeline component.
    See more `info and examples <https://vuetifyjs.com/api/v-timeline>`_.

    Args:
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      align ('start', 'center'):
        Places the timeline dot at the top or center of the timeline item.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      icon_color (string):
        Color of the icon.
      direction ('horizontal', 'vertical'):
        Display timeline in a **vertical** or **horizontal** direction.
      justify (string):
        Places timeline line at the center or automatically on the left or right side.
      line_thickness (string, number):
        Thickness of the timeline line.
      line_color (string):
        Color of the timeline line.
      dot_color (string):
        Color of the item dot.
      fill_dot (boolean):
        Remove outer border of item dot, making the color fill the entire dot.
      hide_opposite (boolean):
        Hide opposite content if it exists.
      line_inset (string, number):
        Specifies the distance between the line and the dot of timeline items.
      side ('end', 'start'):
        Display all timeline items on one side of the timeline, either
        **start** or **end**.
      truncate_line ('end', 'start', 'both'):
        Truncate timeline directly at the **start** or **end** of the
        line, or on **both** ends.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimeline", children, **kwargs)
        self._attr_names += [
            "density",
            "tag",
            "theme",
            "align",
            "size",
            ("icon_color", "iconColor"),
            "direction",
            "justify",
            ("line_thickness", "lineThickness"),
            ("line_color", "lineColor"),
            ("dot_color", "dotColor"),
            ("fill_dot", "fillDot"),
            ("hide_opposite", "hideOpposite"),
            ("line_inset", "lineInset"),
            "side",
            ("truncate_line", "truncateLine"),
        ]
        self._event_names += []


class VTimelineItem(HtmlElement):
    """
    Vuetify's VTimelineItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-timeline-item>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      height (string, number):
        Sets the height for the component.
      size (string, number):
        Size of the item dot
      width (string, number):
        Sets the width for the component.
      density ('default', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      icon (enum):
        Apply a specific icon to the inside dot using the [v-icon](/components/icons/)
        component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      icon_color (string):
        Color of the icon.
      side ('start', 'end'):
        Show the item either **before** or **after** the timeline. This
        will override the implicit ordering of items, but will in turn
        be overridden by the `v-timeline` **single-side** prop.
      dot_color (string):
        Color of the item dot.
      fill_dot (boolean):
        Remove outer border of item dot, making the color fill the entire dot.
      hide_dot (boolean):
        Hide the timeline item dot.
      hide_opposite (boolean):
        Hide opposite content if it exists.
      line_inset (string, number):
        Specifies the distance between the line and the dot of the item.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimelineItem", children, **kwargs)
        self._attr_names += [
            "tag",
            "height",
            "size",
            "width",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "rounded",
            "tile",
            "icon",
            ("icon_color", "iconColor"),
            "side",
            ("dot_color", "dotColor"),
            ("fill_dot", "fillDot"),
            ("hide_dot", "hideDot"),
            ("hide_opposite", "hideOpposite"),
            ("line_inset", "lineInset"),
        ]
        self._event_names += []


class VToolbar(HtmlElement):
    """
    Vuetify's VToolbar component.
    See more `info and examples <https://vuetifyjs.com/api/v-toolbar>`_.

    Args:
      title (string):
        Specify a title text for the component.
      flat (boolean):
        Removes the toolbar's box-shadow.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'prominent', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Designates a specific height for the toolbar. Overrides the heights
        imposed by other props, e.g. **prominent**, **dense**, **extended**,
        etc.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      absolute (boolean):
        Applies position: absolute to the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      image (string):
        Specifies a [v-img](/components/images) as the component's background.
      collapse (boolean):
        Puts the toolbar into a collapsed state reducing its maximum width.
      collapse_position ('end', 'start'):
        Specifies side to attach the collapsed toolbar.
      extended (boolean):
        Use this prop to increase the height of the toolbar _without_
        using the `extension` slot for adding content. May be used in
        conjunction with the **extension-height** prop. When false, will
        not show extension slot even if content is present.
      extension_height (string, number):
        Specify an explicit height for the `extension` slot.
      floating (boolean):
        Applies **display: inline-flex** to the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VToolbar", children, **kwargs)
        self._attr_names += [
            "title",
            "flat",
            "border",
            "density",
            "height",
            "elevation",
            "absolute",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "image",
            "collapse",
            ("collapse_position", "collapsePosition"),
            "extended",
            ("extension_height", "extensionHeight"),
            "floating",
        ]
        self._event_names += []


class VToolbarItems(HtmlElement):
    """
    Vuetify's VToolbarItems component.
    See more `info and examples <https://vuetifyjs.com/api/v-toolbar-items>`_.

    Args:
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VToolbarItems", children, **kwargs)
        self._attr_names += [
            "color",
            "variant",
        ]
        self._event_names += []


class VToolbarTitle(HtmlElement):
    """
    Vuetify's VToolbarTitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-toolbar-title>`_.

    Args:
      text (string):
        Specify content text for the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VToolbarTitle", children, **kwargs)
        self._attr_names += [
            "text",
            "tag",
        ]
        self._event_names += []


class VTooltip(HtmlElement):
    """
    Vuetify's VTooltip component.
    See more `info and examples <https://vuetifyjs.com/api/v-tooltip>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      width (string, number):
        Sets the width for the component.
      id (string):
        HTML id attribute of the tooltip overlay. If not set, a globally
        unique id will be used.
      theme (string):
        Specify a theme for this component and all of its children.
      text (string):
        Specify content text for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      location (Anchor):
        Specifies the anchor point for positioning the component, using
        directional cues to align it either horizontally, vertically,
        or both..
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      close_on_back (boolean):
        Closes the overlay content when the browser's back button is
        pressed or `$router.back()` is called, cancelling the original
        navigation. `persistent` overlays will cancel navigation and
        animate as if they were clicked outside instead of closing.
      contained (boolean):
        Limits the size of the component and scrim to its offset parent.
        Implies `absolute` and `attach`. (Note: The parent element must
        have position: relative.).
      content_class (any):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      content_props (any):
        Apply custom properties to the content.
      opacity (string, number):
        Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
      no_click_animation (boolean):
        Disables the bounce effect when clicking outside of the content
        element when using the persistent prop.
      scrim (string, boolean):
        Accepts true/false to enable background, and string to define color.
      z_index (string, number):
        The z-index used for the component.
      target (enum):
        For locationStrategy="connected", specify an element or array
        of x,y coordinates that the overlay should position itself relative
        to. This will be the activator element by default.

        Enum values: [
          Element, (string & {}), 'parent', 'cursor', ComponentPublicInstance,
          [number, number]
        ]
      activator_props (unknown):
        Apply custom properties to the activator.
      open_on_click (boolean):
        Designates whether the tooltip should open on activator click.
      open_on_hover (boolean):
        Designates whether the tooltip should open on activator hover.
      open_on_focus (boolean):
        Activate the component when the activator is focused.
      close_on_content_click (boolean):
        Closes component when you click on its content.
      close_delay (string, number):
        Delay (in ms) after which menu closes (when open-on-hover prop is set to true).
      open_delay (string, number):
        Delay (in ms) after which tooltip opens (when `open-on-hover`
        prop is set to **true**).
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        Increases distance from the target. When passed as a pair of
        numbers, the second value shifts anchor along the side and away
        from the target.
      stick_to_target (boolean):
        Enables the overlay content to go off-screen when scrolling.
      viewport_margin (string, number):
        Sets custom viewport margin for the overlay content
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default.
      interactive (boolean):
        When true, the tooltip will respond to pointer events, allowing
        you to copy text from it.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTooltip", children, **kwargs)
        self._attr_names += [
            "disabled",
            "height",
            "width",
            "id",
            "theme",
            "text",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "location",
            ("model_value", "modelValue"),
            "transition",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            "scrim",
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "eager",
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            ("stick_to_target", "stickToTarget"),
            ("viewport_margin", "viewportMargin"),
            ("scroll_strategy", "scrollStrategy"),
            "attach",
            "interactive",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTreeview(HtmlElement):
    """
    Vuetify's VTreeview component.
    See more `info and examples <https://vuetifyjs.com/api/v-treeview>`_.

    Args:
      search (string):
        The search model for filtering results.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      model_value (unknown[]):
        Allows one to control which nodes are selected. The array contains
        the values of currently selected items. It is equivalent to the
        `v-model:selected`
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Provides an alternative active style for `v-treeview` node. Only
        visible when `activatable` is `true` and should not be used in
        conjunction with the `shaped` prop.
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the active node - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      activated (any):
        Array of ids of activated nodes.
      disabled (boolean):
        Disables selection for all nodes.
      filter_mode ('every', 'some', 'union', 'intersection'):
        Controls how the results of `customFilter` and `customKeyFilter`
        are combined. All modes only apply `customFilter` to columns
        not specified in `customKeyFilter`.  - **some**: There is at
        least one match from either the custom filter or the custom key
        filter. - **every**: All columns match either the custom filter
        or the custom key filter. - **union**: There is at least one
        match from the custom filter, or all columns match the custom
        key filters. - **intersection**: There is at least one match
        from the custom filter, and all columns match the custom key
        filters.
      no_filter (boolean):
        Disables all item filtering.
      custom_filter (FilterFunction):
        Function used to filter items, called for each filterable key
        on each item in the list. The first argument is the filterable
        value from the item, the second is the search term, and the third
        is the internal item object. The function should return true
        if the item should be included in the filtered list, or the index
        of the match in the value if it should be included with the result
        highlighted.
      custom_key_filter (unknown):
        Function used on specific keys within the item object. `customFilter`
        is skipped for columns with `customKeyFilter` specified.
      filter_keys (string, string[]):
        Array of specific keys to filter on the item.
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        Deprecated, use `color` instead.
      active_class (string):
        The class applied to the component when it is in an active state.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      filterable (boolean):
        **FOR INTERNAL USE ONLY** Prevents list item selection using
        [space] key and pass it back to the text input. Used internally
        for VAutocomplete and VCombobox.
      expand_icon (enum):
        Icon used to indicate that a node can be expanded.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon to display when the list item is expanded.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      lines (false, 'one', 'two', 'three'):
        Designates a **minimum-height** for all children `v-list-item`
        components. This prop uses [line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp)
        and is not supported in all browsers.
      slim (boolean):
        Reduces horizontal spacing for badges, icons, tooltips, and avatars
        within slim list items to create a more compact visual representation.
      prepend_gap (string, number):
        Sets the horizontal spacing between prepend slot and the main
        content within list item. Also affects indent to ensure expected
        alignment of group children.
      indent (string, number):
        Overrides the indent size for nested groups.
      activatable (boolean):
        Allows user to mark a node as active by clicking on it.
      selectable (boolean):
        Will render a checkbox next to each node allowing them to be
        selected. Additionally, the **[openOnClick](/api/v-treeview/#props-open-on-click)**
        property will be applied internally.
      opened (any):
        An array containing the values of currently opened groups. Can
        be two-way bound with `v-model:opened`.
      selected (any):
        An array containing the values of currently selected items. Can
        be two-way bound with `v-model:selected`.
      mandatory (boolean):
        Forces at least one item to always be selected (if available).
      items_registration ('props', 'render'):
        When set to 'props', skips rendering collapsed items/nodes (for
        significant performance gains).
      active_strategy (ActiveStrategy):
        Affects how items with children behave when activated. If not
        specified, the **single-independent** strategy will be used.
        - **leaf:** Only leaf nodes (items without children) can be activated.
        - **single-leaf:** Similar as **leaf**, but only a single item
        can be activated at a time. - **independent:** All nodes can
        be activated whether they have children or not. - **single-independent:**
        Similar as **independent**, but only a single item can be activated
        at a time.
      select_strategy (SelectStrategy):
        Affects how items with children behave when selected. - **leaf:**
        Only leaf nodes (items without children) can be selected. - **independent:**
        All nodes can be selected whether they have children or not.
        - **classic:** Selecting a parent node will cause all children
        to be selected, parent nodes will be displayed as selected if
        all their descendants are selected. Only leaf nodes will be added
        to the model. - **trunk**: Same as classic but if all of a node's
        children are selected then only that node will be added to the
        model.
      items (unknown[]):
        An array of items used to build the treeview.
      item_title (SelectItemKey):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey):
        Property on supplied `items` that contains its value.
      item_children (SelectItemKey):
        Property on supplied `items` that contains its children.
      item_props (SelectItemKey):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      item_type (SelectItemKey):
        Designates the key on the supplied items that is used for determining
        the nodes type.
      return_object (boolean):
        When `true` will make `v-model`, `v-model:selected, `v-model:activated`
        and `v-model:opened` return the complete object instead of just
        the key.
      value_comparator (((a: any, b: any, recursionCache: { delete: (key: WeakKey) => boolean; get: (key: WeakKey) => any; has: (key: WeakKey) => boolean; set: (key: WeakKey, value: any) => WeakMap<WeakKey, any>; __@toStringTag@3888: string }) => boolean)):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      open_on_click (boolean):
        When `true` will cause nodes to be opened by clicking anywhere
        on it, instead of only opening by clicking on expand icon. When
        using this prop with `activatable` you will be unable to mark
        nodes with children as active.
      no_data_text (string):
        Text shown when no items are provided to the component.
      hide_actions (boolean):
        Hide the expand icon and loading indicator next to each item title.
      fluid (boolean):
        Removes indentation from nested items.
      false_icon (enum):
        The icon used when inactive.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_icon (enum):
        The icon used when active.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      open_all (boolean):
        When `true` will cause all branch nodes to be opened when component is mounted.
      loading_icon (string):
        Icon used when node is in a loading state.
      indeterminate_icon (enum):
        Icon used when node is in an indeterminate state. Only visible
        when `selectable` is `true`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      selected_color (string):
        The color of the selection checkbox.
      separate_roots (boolean):
        Applies to `default` variant of `indent-lines`. Prevents showing
        lines between root-level nodes.
      indent_lines (boolean, 'default', 'simple'):
        Controls visibility and variant of the indent lines.
      load_children ((item: unknown) => Promise<void>):
        A function used when dynamically loading children. If this prop
        is set, then the supplied function will be run if expanding an
        item that has a `item-children` property that is an empty array.
        Supports returning a Promise.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_open (event):
        Emits the item when it is clicked to open.
      click_select (event):
        Emits the item when it is clicked to select.
      update_opened (event):
        Emits the array of open items when this value changes.
      update_selected (event):
        Emits the array of selected items when this value changes.
      update_activated (event):
        Emits the array of active items when this value changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTreeview", children, **kwargs)
        self._attr_names += [
            "search",
            "border",
            ("model_value", "modelValue"),
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            "activated",
            "disabled",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            ("hide_no_data", "hideNoData"),
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            ("active_class", "activeClass"),
            ("bg_color", "bgColor"),
            "filterable",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "lines",
            "slim",
            ("prepend_gap", "prependGap"),
            "indent",
            "activatable",
            "selectable",
            "opened",
            "selected",
            "mandatory",
            ("items_registration", "itemsRegistration"),
            ("active_strategy", "activeStrategy"),
            ("select_strategy", "selectStrategy"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("item_type", "itemType"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            ("open_on_click", "openOnClick"),
            ("no_data_text", "noDataText"),
            ("hide_actions", "hideActions"),
            "fluid",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            ("open_all", "openAll"),
            ("loading_icon", "loadingIcon"),
            ("indeterminate_icon", "indeterminateIcon"),
            ("selected_color", "selectedColor"),
            ("separate_roots", "separateRoots"),
            ("indent_lines", "indentLines"),
            ("load_children", "loadChildren"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_open", "click:open"),
            ("click_select", "click:select"),
            ("update_opened", "update:opened"),
            ("update_selected", "update:selected"),
            ("update_activated", "update:activated"),
        ]


class VTreeviewGroup(HtmlElement):
    """
    Vuetify's VTreeviewGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-treeview-group>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      title (string):
        Specify a title text for the component.
      disabled (boolean):
        Puts all children inputs into a disabled state.
      value (any):
        Expands / Collapse the list-group.
      active_color (string):
        Deprecated, use `color` instead.
      base_color (string):
        Sets the color of component when not focused.
      prepend_icon (enum):
        Prepends an icon to the component, uses the same syntax as `v-icon`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      expand_icon (enum):
        Icon to display when the list item is collapsed.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      collapse_icon (enum):
        Icon to display when the list item is expanded.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      raw_id (string, number):
        Defines the root element's id attribute in the component. If
        it is provided, the id attribute will be dynamically generated
        in the format: "v-list-group--id-[rawId]".
      fluid (boolean):
        Removes indentation from nested items.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTreeviewGroup", children, **kwargs)
        self._attr_names += [
            "tag",
            "title",
            "disabled",
            "value",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("raw_id", "rawId"),
            "fluid",
        ]
        self._event_names += []


class VTreeviewItem(HtmlElement):
    """
    Vuetify's VTreeviewItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-treeview-item>`_.

    Args:
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the href or to prop.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      nav (boolean):
        Reduces the width of v-list-item takes and adds a border radius.
      title (string, number, boolean):
        Generates a `v-list-item-title` component with the supplied value.
        Note that this overrides the native [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title)
        attribute, that must be set with `v-bind:title.attr` instead.
      disabled (boolean):
        Removes the ability to click or target the component.
      height (string, number):
        Sets the height for the component.
      value (any):
        The value used for selection. Obtained from [`v-list`](/api/v-list)'s
        `v-model:selected` when the item is selected.
      width (string, number):
        Sets the width for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      active_color (string):
        Deprecated, use `color` instead.
      base_color (string):
        Sets the color of component when not focused.
      prepend_icon (enum):
        Creates a [v-icon](/api/v-icon/) component in the **prepend**
        slot before default content.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      slim (boolean):
        Reduces the vertical padding or height of the v-treeview-item,
        making it more compact.
      ripple (boolean, { class: string; keys: string[] }):
        Applies the [v-ripple](/directives/ripple) directive.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      loading (boolean):
        Places the v-treeview-item into a loading state.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      color (string):
        Applies specified color to the control when in an **active**
        state or **input-value** is **true** - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors),
      variant ('flat', 'text', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      lines (false, 'one', 'two', 'three'):
        The line declaration specifies the minimum height of the item
        and can also be controlled from v-list with the same prop.
      active_class (string):
        The class applied to the component when it matches the current
        route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class)
        on the [vue-router](https://router.vuejs.org/) documentation.
      subtitle (string, number, boolean):
        Specify a subtitle text for the component.
      append_avatar (string):
        Appends a [v-avatar](/components/avatars/) component after default
        content in the **append** slot.
      prepend_avatar (string):
        Prepends a [v-avatar](/components/avatars/) component in the
        **prepend** slot before default content.
      prepend_gap (string, number):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VListItem.json))
      hide_actions (boolean):
        Hide the expand icon and loading indicator next to each item title.
      has_custom_prepend (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTreeviewItem.json))
      toggle_icon (enum):
        Allows customization of the icon used to toggle the expansion
        and collapse of treeview branches.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      indent_lines (('none', 'leaf', 'line', 'last-leaf', 'leaf-link')[]):
        Array of indent lines to render next to the item.
      toggleExpand (event):
        Emitted when the item is toggled to expand or collapse.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTreeviewItem", children, **kwargs)
        self._attr_names += [
            "replace",
            "link",
            "tag",
            "nav",
            "title",
            "disabled",
            "height",
            "value",
            "width",
            "theme",
            "active",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "slim",
            "ripple",
            "border",
            "density",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "elevation",
            "loading",
            "rounded",
            "tile",
            "href",
            "exact",
            "to",
            "color",
            "variant",
            "lines",
            ("active_class", "activeClass"),
            "subtitle",
            ("append_avatar", "appendAvatar"),
            ("prepend_avatar", "prependAvatar"),
            ("prepend_gap", "prependGap"),
            ("hide_actions", "hideActions"),
            ("has_custom_prepend", "hasCustomPrepend"),
            ("toggle_icon", "toggleIcon"),
            ("indent_lines", "indentLines"),
        ]
        self._event_names += [
            "click",
            "toggleExpand",
        ]


class VValidation(HtmlElement):
    """
    Vuetify's VValidation component.
    See more `info and examples <https://vuetifyjs.com/api/v-validation>`_.

    Args:
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      name (string):
        Sets the component's name attribute.
      disabled (boolean):
        Removes the ability to click or target the component.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      readonly (boolean):
        Puts input in readonly state.
      rules (enum):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.

        Enum values: [
          (, string, boolean, PromiseLike<ValidationResult>, js_fn, false,
          true), js_fn, [string, any, string])[]
        ]
      validate_on (enum):
        Change what type of event triggers validation to run.

        Enum values: [
          'eager', 'lazy', 'blur', 'input', 'submit', 'invalid-input',
          'blur lazy', 'input lazy', 'submit lazy', 'invalid-input lazy',
          'blur eager', 'input eager', 'submit eager', 'invalid-input eager',
          'lazy blur', 'lazy input', 'lazy submit', 'lazy invalid-input',
          'eager blur', 'eager input', 'eager submit', 'eager invalid-input'
        ]
      validation_value (any):
        The value used when applying validation rules.
      focused (boolean):
        Forces a focused state styling on the component.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_focused (event):
        Event that is emitted when the component's focus state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VValidation", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "error",
            "name",
            "disabled",
            "label",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "readonly",
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_focused", "update:focused"),
        ]


class VVideo(HtmlElement):
    """
    Vuetify's VVideo component.
    See more `info and examples <https://vuetifyjs.com/api/v-video>`_.

    Args:
      type (string):
        Media file type (optional)
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean, (string, number, false, true)[]):
        Applies a border radius to the video container and the controls.
        Accepts array of two values to customize elements separately.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        General color applied to icons and sliders.
      variant ('background', 'player'):
        Applies a distinct style to the component.
      src (string):
        Media file URL
      image (string):
        Apply a specific image as cover before the video is loaded.
      floating (boolean):
        Introduces visual spacing from the video boundaries.
      eager (boolean):
        Silently loades the media file without waiting for user to click.
      playing (boolean):
        Applies correct icon of the default play button.
      progress (number):
        Controls main slider value (0 ~ 100)
      aspect_ratio (string, number):
        Sets the aspect ratio for the playback, calculated as width/height.
      autoplay (boolean):
        Starts loading the media file without waiting for user to click.
        Playback begins once enough data is loaded.
      muted (boolean):
        Hides volume control and disables the playback sound.
      hide_overlay (boolean):
        Hide center play icon.
      no_fullscreen (boolean):
        Disable fullscreen and hide the default fullscreen button.
      start_at (string, number):
        Moves progress to the specified time (in seconds) once the media file is loaded.
      controls_transition (string, boolean, (TransitionProps & { component: any })):
        The reveal transition applied to the VVideoControls component
        once the media file is loaded.
      controls_variant ('default', 'hidden', 'tube', 'mini'):
        Variant passed to the VVideoControls component.
      controls_props (unknown):
        Pass props through to the `v-video-controls` component. Accepts
        an object with anything from [v-video-controls](/api/v-video-controls/#props)
        props, camelCase keys are recommended.
      background_color (string):
        Container background color.
      track_color (string):
        Passed to the main slider `color` prop.
      hide_play (boolean):
        Hides default play button.
      hide_volume (boolean):
        Hides default volume control.
      hide_fullscreen (boolean):
        Hides default fullscreen button.
      split_time (boolean):
        Splits time into elapsed and remaining on each side of the main slider.
      pills (boolean):
        Makes the container transparent and shows inner actions in separated boxes.
      detached (boolean):
        Moves the container below so it won't obstruct the video.
      duration (number):
        Total duration of the video used to calculate displayed time.
      volume (string, number):
        Volume value passed to the underlying control and slots.
      volume_props (Anchor):
        Props passed down to the VVideoVolume component.
      update_playing (event):
        Emitted when playing state changes.
      update_progress (event):
        Emitted when the internal playback progress changes.
      update_volume (event):
        Emitted when the volume changes.
      loaded (event):
        Emitted when the video has loaded and is ready to be played.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VVideo", children, **kwargs)
        self._attr_names += [
            "type",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "rounded",
            "theme",
            "color",
            "variant",
            "src",
            "image",
            "floating",
            "eager",
            "playing",
            "progress",
            ("aspect_ratio", "aspectRatio"),
            "autoplay",
            "muted",
            ("hide_overlay", "hideOverlay"),
            ("no_fullscreen", "noFullscreen"),
            ("start_at", "startAt"),
            ("controls_transition", "controlsTransition"),
            ("controls_variant", "controlsVariant"),
            ("controls_props", "controlsProps"),
            ("background_color", "backgroundColor"),
            ("track_color", "trackColor"),
            ("hide_play", "hidePlay"),
            ("hide_volume", "hideVolume"),
            ("hide_fullscreen", "hideFullscreen"),
            ("split_time", "splitTime"),
            "pills",
            "detached",
            "duration",
            "volume",
            ("volume_props", "volumeProps"),
        ]
        self._event_names += [
            ("update_playing", "update:playing"),
            ("update_progress", "update:progress"),
            ("update_volume", "update:volume"),
            "loaded",
        ]


class VVideoControls(HtmlElement):
    """
    Vuetify's VVideoControls component.
    See more `info and examples <https://vuetifyjs.com/api/v-video-controls>`_.

    Args:
      playing (boolean):
        Applies correct icon of the default play button.
      progress (number):
        Controls main slider value (0 ~ 100)
      theme (string):
        Specify a theme for this component and all of its children.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      color (string):
        General color applied to icons and sliders.
      variant ('default', 'hidden', 'tube', 'mini'):
        Applies a distinct style to the component.
      floating (boolean):
        Introduces visual spacing from the video boundaries.
      fullscreen (boolean):
        Applies correct icon on the default fullscreen button.
      track_color (string):
        Passed to the main slider `color` prop.
      background_color (string):
        Container background color.
      hide_play (boolean):
        Hides default play button.
      hide_volume (boolean):
        Hides default volume control.
      hide_fullscreen (boolean):
        Hides default fullscreen button.
      split_time (boolean):
        Splits time into elapsed and remaining on each side of the main slider.
      pills (boolean):
        Makes the container transparent and shows inner actions in separated boxes.
      detached (boolean):
        Moves the container below so it won't obstruct the video.
      duration (number):
        Total duration of the video used to calculate displayed time.
      volume (string, number):
        Volume value passed to the underlying control and slots.
      volume_props (Anchor):
        Props passed down to the VVideoVolume component.
      update_playing (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VVideoControls.json))
      update_progress (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VVideoControls.json))
      update_volume (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VVideoControls.json))
      skip (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VVideoControls.json))
      click_fullscreen (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VVideoControls.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VVideoControls", children, **kwargs)
        self._attr_names += [
            "playing",
            "progress",
            "theme",
            "density",
            "elevation",
            "color",
            "variant",
            "floating",
            "fullscreen",
            ("track_color", "trackColor"),
            ("background_color", "backgroundColor"),
            ("hide_play", "hidePlay"),
            ("hide_volume", "hideVolume"),
            ("hide_fullscreen", "hideFullscreen"),
            ("split_time", "splitTime"),
            "pills",
            "detached",
            "duration",
            "volume",
            ("volume_props", "volumeProps"),
        ]
        self._event_names += [
            ("update_playing", "update:playing"),
            ("update_progress", "update:progress"),
            ("update_volume", "update:volume"),
            "skip",
            ("click_fullscreen", "click:fullscreen"),
        ]


class VVideoVolume(HtmlElement):
    """
    Vuetify's VVideoVolume component.
    See more `info and examples <https://vuetifyjs.com/api/v-video-volume>`_.

    Args:
      label (string):
        Text to display in tooltip and passed to `aria-label`.
      inline (boolean):
        Display slider next to the icon. VMenu won't be displayed on
        click. Recomended to pair with **sliderProps** to configure slider
        width.
      model_value (number):
        Volume value (0 ~ 100)
      direction ('horizontal', 'vertical'):
        Switch between horizontal and vertical slider.
      menu_props (unknown):
        Props passed to VMenu containing volume slider. Useful to adjust
        **location** and control menu alignment
      slider_props (enum):
        Selected props to customize volume slider.

        Enum values: [
          {  disabled: boolean  width: string, number  maxWidth: string,
          number  color: string  thumbSize: string, number  trackColor:
          string}
        ]
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VVideoVolume", children, **kwargs)
        self._attr_names += [
            "label",
            "inline",
            ("model_value", "modelValue"),
            "direction",
            ("menu_props", "menuProps"),
            ("slider_props", "sliderProps"),
        ]
        self._event_names += [
            "click",
            ("update_modelValue", "update:modelValue"),
        ]


class VVirtualScroll(HtmlElement):
    """
    Vuetify's VVirtualScroll component.
    See more `info and examples <https://vuetifyjs.com/api/v-virtual-scroll>`_.

    Args:
      height (string, number):
        Height of the component as a css value/
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component.
      width (string, number):
        Sets the width for the component.
      items (unknown[]):
        The array of items to display.
      item_height (string, number):
        Height in pixels of each item to display.
      item_key (SelectItemKey):
        Should point to a property with a unique value for each item,
        if not set then item index will be used as a key which may result
        in unnecessary re-renders.
      renderless (boolean):
        Disables default component rendering functionality. The parent
        node must be [a positioned element](https://developer.mozilla.org/en-US/docs/Web/CSS/position#types_of_positioning),
        e.g. using `position: relative;`
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VVirtualScroll", children, **kwargs)
        self._attr_names += [
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "items",
            ("item_height", "itemHeight"),
            ("item_key", "itemKey"),
            "renderless",
        ]
        self._event_names += []


class VWindow(HtmlElement):
    """
    Vuetify's VWindow component.
    See more `info and examples <https://vuetifyjs.com/api/v-window>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      reverse (boolean):
        Reverse the normal transition direction.
      disabled (boolean):
        Removes the ability to click or target the component.
      theme (string):
        Specify a theme for this component and all of its children.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      direction ('horizontal', 'vertical'):
        The transition direction when changing windows.
      continuous (boolean):
        If `true`, window will "wrap around" from the last item to the
        first, and from the first item to the last.
      next_icon (enum):
        Icon used for the "next" button if `show-arrows` is `true`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        Icon used for the "prev" button if `show-arrows` is `true`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      show_arrows (string, boolean):
        Display the "next" and "prev" buttons.
      touch (TouchHandlers):
        Provide a custom **left** and **right** function when swiped left or right.
      crossfade (boolean):
        Enables crossfade transition.
      transition_duration (number):
        Overrides transition duration.
      vertical_arrows (boolean, 'left', 'right'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VWindow.json))
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VWindow", children, **kwargs)
        self._attr_names += [
            "tag",
            "reverse",
            "disabled",
            "theme",
            ("selected_class", "selectedClass"),
            ("model_value", "modelValue"),
            "mandatory",
            "direction",
            "continuous",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            "touch",
            "crossfade",
            ("transition_duration", "transitionDuration"),
            ("vertical_arrows", "verticalArrows"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VWindowItem(HtmlElement):
    """
    Vuetify's VWindowItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-window-item>`_.

    Args:
      disabled (boolean):
        Prevents the item from becoming active when using the "next"
        and "prev" buttons or the `toggle` method.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      transition (string, boolean):
        The transition used when the component progressing through items.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.
      reverse_transition (string, boolean):
        Sets the reverse transition.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VWindowItem", children, **kwargs)
        self._attr_names += [
            "disabled",
            "value",
            "eager",
            "transition",
            ("reverse_transition", "reverseTransition"),
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]
