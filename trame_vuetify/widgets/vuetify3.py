##########################################################
# DO NOT EDIT: GENERATED FILE
# => instead run: $ROOT/vue-components/generate_python.py
##########################################################

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
    "chip",
    "clear",
    "close",
    "colgroup",
    "content",
    "counter",
    "data-table-group",
    "data-table-select",
    "day",
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
    "item",
    "item-label",
    "item.data-table-expand",
    "item.data-table-select",
    "label",
    "last",
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
    "VCalendarDay",
    "VCalendarHeader",
    "VCalendarInterval",
    "VCalendarIntervalEvent",
    "VCalendarMonthDay",
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
      full_height (boolean):
        Sets the component height to 100%.
      overlaps (string[]):
        **FOR INTERNAL USE ONLY**
      theme (string):
        Specify a theme for this component and all of its children.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VApp", children, **kwargs)
        self._attr_names += [
            ("full_height", "fullHeight"),
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
      extended (boolean):
        Use this prop to increase the height of the toolbar _without_
        using the `extension` slot for adding content. May be used in
        conjunction with the **extension-height** prop, and any of the
        other props that affect the height of the toolbar, e.g. **prominent**,
        **dense**, etc., **WITH THE EXCEPTION** of **height**.
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
      theme (string):
        Specify a theme for this component and all of its children.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
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
      ripple (boolean, { class: string }):
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
      disabled (boolean):
        Removes the ability to click or target the component.
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
            "theme",
            "size",
            "value",
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
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "disabled",
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
      close_text (string):
        Text set to the inputs `aria-label` and `title` when input menu is closed.
      open_text (string):
        Text set to the inputs **aria-label** and **title** when input menu is open.
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
      disabled (boolean):
        Removes the ability to click or target the input.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      items (any[]):
        Can be an array of objects or strings. By default objects should
        have **title** and **value** properties, and can optionally have
        a **props** property containing any [VListItem props](/api/v-list-item/#props).
        Keys to use for these can be changed with the **item-title**,
        **item-value**, and **item-props** props.
      item_title (SelectItemKey<any>):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey<any>):
        Property on supplied `items` that contains its value.
      item_children (SelectItemKey):
        This property currently has **no effect**.
      item_props (SelectItemKey<any>):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator ((a: any, b: any) => boolean):
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
      id (string):
        Sets the DOM id on the component.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      no_data_text (string):
        Text shown when no items are provided to the component.
      open_on_clear (boolean):
        Open's the menu whenever the clear icon is clicked.
      item_color (string):
        Sets color of selected items.
      autofocus (boolean):
        Enables autofocus.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      prefix (string):
        Displays prefix text.
      placeholder (string):
        Sets the input’s placeholder text.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      role (string):
        The role attribute applied to the input.
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
        Makes prepend/append icons full opacity when the field is focused.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outnside the component's input, uses
        the same syntax as `v-icon`.

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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
            ("close_text", "closeText"),
            ("open_text", "openText"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            ("list_props", "listProps"),
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "disabled",
            "multiple",
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "id",
            "transition",
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("item_color", "itemColor"),
            "autofocus",
            "counter",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            "role",
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
      theme (string):
        Specify a theme for this component and all of its children.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      text (string):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      start (boolean):
        Applies margin at the end of the component.
      end (boolean):
        Applies margin at the start of the component.
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
            "theme",
            "size",
            "text",
            "border",
            "density",
            "start",
            "end",
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
      theme (string):
        Specify a theme for this component and all of its children.
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
      max (string, number):
        Sets the maximum number allowed when using the **content** prop
        with a `number` like value. If the content number exceeds the
        maximum value, a `+` suffix is added.
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
            "theme",
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
            "max",
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
            "theme",
            "stacked",
            "text",
            "border",
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
      height (string, number):
        Sets the height for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      disabled (boolean):
        Puts all children components into a disabled state.
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
      max (number):
        Sets a maximum number of selections that can be made.
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
      multiple (boolean):
        Allows one to select multiple items.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_active (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VBottomNavigation.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBottomNavigation", children, **kwargs)
        self._attr_names += [
            "tag",
            "name",
            "mode",
            "theme",
            "active",
            ("base_color", "baseColor"),
            "border",
            "density",
            "height",
            "elevation",
            "disabled",
            ("selected_class", "selectedClass"),
            "absolute",
            "rounded",
            "tile",
            "color",
            "max",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "grow",
            "order",
            "multiple",
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
      theme (string):
        Specify a theme for this component and all of its children.
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
      disabled (boolean):
        Removes the ability to click or target the component.
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
          { component: Component }
        ]
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      inset (boolean):
        Reduces the sheet content maximum width to 70%.
      fullscreen (boolean):
        Changes layout for fullscreen display.
      retain_focus (boolean):
        Tab focus will return to the first child of the dialog by default.
        Disable this when using external tools that require focus such
        as TinyMCE or vue-clipboard.
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
        Sets the overlay opacity.
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
        A single value that offsets content away from the target based
        upon what side it is on.
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
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
            "theme",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "disabled",
            "location",
            "absolute",
            ("model_value", "modelValue"),
            "transition",
            "activator",
            "inset",
            "fullscreen",
            ("retain_focus", "retainFocus"),
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
            ("scroll_strategy", "scrollStrategy"),
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
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      divider (string):
        Specifies the dividing character between items.
      active_color (string):
        The applied color when the component is in an active state.
      active_class (string):
        The class applied to the component when it is in an active state.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      disabled (boolean):
        Removes the ability to click or target the component.
      items (enum):
        An array of strings or objects used for automatically generating
        children components.

        Enum values: [
          (, string, (Partial<LinkProps> & { title: string; disabled: boolean }))[]
        ]
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBreadcrumbs", children, **kwargs)
        self._attr_names += [
            "icon",
            "density",
            "rounded",
            "tile",
            "tag",
            "color",
            "divider",
            ("active_color", "activeColor"),
            ("active_class", "activeClass"),
            ("bg_color", "bgColor"),
            "disabled",
            "items",
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
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      active_color (string):
        The applied color when the component is in an active state.
      disabled (boolean):
        Removes the ability to click or target the component.
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
            "active",
            ("active_color", "activeColor"),
            "disabled",
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
      text (string, number, boolean):
        Specify content text for the component.
      flat (boolean):
        Removes the button box shadow. This is different than using the 'flat' variant.
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/)
        component. The button will become _round_.

        Enum values: [
          boolean, string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
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
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        The applied color when the component is in an active state.
      disabled (boolean):
        Removes the ability to click or target the component.
      slim (boolean):
        Reduces padding to 0 8px.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      block (boolean):
        Expands the button to 100% of available space.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
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
      readonly (boolean):
        Puts the button in a readonly state. Cannot be clicked or navigated
        to by keyboard.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      stacked (boolean):
        Displays the button as a flex-column.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtn", children, **kwargs)
        self._attr_names += [
            "symbol",
            "text",
            "flat",
            "replace",
            "border",
            "icon",
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
            "exact",
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            "disabled",
            "slim",
            "value",
            "block",
            "size",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "readonly",
            "active",
            "loading",
            "href",
            "to",
            "stacked",
            "ripple",
            ("selected_class", "selectedClass"),
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
        ]
        self._event_names += []


class VBtnToggle(HtmlElement):
    """
    Vuetify's VBtnToggle component.
    See more `info and examples <https://vuetifyjs.com/api/v-btn-toggle>`_.

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
      disabled (boolean):
        Puts all children components into a disabled state.
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
      max (number):
        Sets a maximum number of selections that can be made.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      multiple (boolean):
        Allows one to select multiple items.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      divided (boolean):
        Add dividers between children [v-btn](/components/buttons) components.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtnToggle", children, **kwargs)
        self._attr_names += [
            "tag",
            "theme",
            ("base_color", "baseColor"),
            "border",
            "density",
            "elevation",
            "disabled",
            ("selected_class", "selectedClass"),
            "rounded",
            "tile",
            "color",
            "variant",
            "max",
            ("model_value", "modelValue"),
            "multiple",
            "mandatory",
            "divided",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VCalendar(HtmlElement):
    """
    Vuetify's VCalendar component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar>`_.

    Args:
      title (string):
        Specify a title text for the component.
      text (string):
        Specify content text for the component.
      model_value (unknown[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      disabled (boolean):
        Removes the ability to click or target the component.
      hide_header (boolean):
        Determines whether the header is hidden in the calendar view.
      hide_week_number (boolean):
        Toggles the display of week numbers in a calendar view.
      month (string, number):
        Specifies the month for the calendar view.
      show_adjacent_months (boolean):
        Shows or hides days from adjacent months.
      year (string, number):
        Specifies the year for the calendar view.
      weekdays ((0, 1, 2, 4, 5, 6, 3)[]):
        Specifies which days of the week to display.
      weeks_in_month ('static', 'dynamic'):
        A dynamic number of weeks in a month will grow and shrink depending
        on how many days are in the month. A static number always shows
        7 weeks.
      first_day_of_week (string, number):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/calendar.json))
      allowed_dates (unknown[], js_fn):
        Determines which dates are selectable.
      display_value (unknown):
        The value that determines the month to show. This is different
        from modelValue, which determines the selected value.
      max (unknown):
        Maximum date or value that can be selected.
      min (unknown):
        Minimum date or value that can be selected.
      hide_day_header (boolean):
        Determines whether the day header is visible in the calendar day view.
      intervals (number):
        Total number of intervals in a day view.
      day (unknown):
        Represents the specific day associated with the interval.
      day_index (number):
        Index of the day this interval is a part of, in a week or month view.
      events (any[]):
        Array of events specific to this interval.
      interval_divisions (number):
        Number of subdivisions within this interval.
      interval_duration (number):
        Duration of this specific interval in minutes.
      interval_height (number):
        Height of the interval in pixels in the calendar view.
      interval_format (string, Function):
        Formatting rule for displaying the interval, as a string or function.
      interval_start (number):
        Starting time for this specific interval.
      next_icon (string):
        The icon to use for the next button.
      prev_icon (string):
        The icon to use for the prev button.
      view_mode ('month', 'day', 'week'):
        The current view mode of the calendar.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      next (event):
        Emitted when moving to the next time period.
      prev (event):
        Emitted when moving to the previous time period.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendar", children, **kwargs)
        self._attr_names += [
            "title",
            "text",
            ("model_value", "modelValue"),
            "disabled",
            ("hide_header", "hideHeader"),
            ("hide_week_number", "hideWeekNumber"),
            "month",
            ("show_adjacent_months", "showAdjacentMonths"),
            "year",
            "weekdays",
            ("weeks_in_month", "weeksInMonth"),
            ("first_day_of_week", "firstDayOfWeek"),
            ("allowed_dates", "allowedDates"),
            ("display_value", "displayValue"),
            "max",
            "min",
            ("hide_day_header", "hideDayHeader"),
            "intervals",
            "day",
            ("day_index", "dayIndex"),
            "events",
            ("interval_divisions", "intervalDivisions"),
            ("interval_duration", "intervalDuration"),
            ("interval_height", "intervalHeight"),
            ("interval_format", "intervalFormat"),
            ("interval_start", "intervalStart"),
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("view_mode", "viewMode"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "next",
            "prev",
        ]


class VCalendarDay(HtmlElement):
    """
    Vuetify's VCalendarDay component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar-day>`_.

    Args:
      hide_day_header (boolean):
        Determines whether the day header is visible in the calendar day view.
      intervals (number):
        Specifies the total number of time intervals for the day in the calendar view.
      day (unknown):
        Represents the specific day associated with the interval.
      day_index (number):
        Index of the day this interval is a part of, in a week or month view.
      events (any[]):
        Array of events specific to this interval.
      interval_divisions (number):
        Number of subdivisions within this interval.
      interval_duration (number):
        Duration of this specific interval in minutes.
      interval_height (number):
        Height of the interval in pixels in the calendar view.
      interval_format (string, Function):
        Formatting rule for displaying the interval, as a string or function.
      interval_start (number):
        Starting time for this specific interval.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendarDay", children, **kwargs)
        self._attr_names += [
            ("hide_day_header", "hideDayHeader"),
            "intervals",
            "day",
            ("day_index", "dayIndex"),
            "events",
            ("interval_divisions", "intervalDivisions"),
            ("interval_duration", "intervalDuration"),
            ("interval_height", "intervalHeight"),
            ("interval_format", "intervalFormat"),
            ("interval_start", "intervalStart"),
        ]
        self._event_names += []


class VCalendarHeader(HtmlElement):
    """
    Vuetify's VCalendarHeader component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar-header>`_.

    Args:
      title (string):
        Specify a title text for the component.
      text (string):
        Specify content text for the component.
      next_icon (string):
        The icon to use for the next button.
      prev_icon (string):
        The icon to use for the prev button.
      view_mode ('day', 'month', 'week'):
        The current view mode of the calendar.
      click_next (event):
        Event emitted when clicking the next button.
      click_prev (event):
        Event emitted when clicking the prev button.
      click_toToday (event):
        Event emitted when clicking the today button.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendarHeader", children, **kwargs)
        self._attr_names += [
            "title",
            "text",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("view_mode", "viewMode"),
        ]
        self._event_names += [
            ("click_next", "click:next"),
            ("click_prev", "click:prev"),
            ("click_toToday", "click:toToday"),
        ]


class VCalendarInterval(HtmlElement):
    """
    Vuetify's VCalendarInterval component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar-interval>`_.

    Args:
      day (unknown):
        Represents the specific day associated with the interval.
      day_index (number):
        Index of the day this interval is a part of, in a week or month view.
      events (any[]):
        Array of events specific to this interval.
      interval_divisions (number):
        Number of subdivisions within this interval.
      interval_duration (number):
        Duration of this specific interval in minutes.
      interval_height (number):
        Height of the interval in pixels in the calendar view.
      interval_format (string, Function):
        Formatting rule for displaying the interval, as a string or function.
      interval_start (number):
        Starting time for this specific interval.
      index (number):
        Index or position of the interval in the day view.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendarInterval", children, **kwargs)
        self._attr_names += [
            "day",
            ("day_index", "dayIndex"),
            "events",
            ("interval_divisions", "intervalDivisions"),
            ("interval_duration", "intervalDuration"),
            ("interval_height", "intervalHeight"),
            ("interval_format", "intervalFormat"),
            ("interval_start", "intervalStart"),
            "index",
        ]
        self._event_names += []


class VCalendarIntervalEvent(HtmlElement):
    """
    Vuetify's VCalendarIntervalEvent component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar-interval-event>`_.

    Args:
      interval_divisions (number):
        Number of subdivisions within the interval for this event.
      interval_duration (number):
        Duration of the interval in which this event occurs, in minutes.
      interval_height (number):
        Height of the interval in the calendar view, in pixels.
      all_day (boolean):
        Indicates whether the event spans the entire day.
      interval (unknown):
        The specific time interval this event is associated with.
      event (unknown):
        The event object associated with this calendar interval.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendarIntervalEvent", children, **kwargs)
        self._attr_names += [
            ("interval_divisions", "intervalDivisions"),
            ("interval_duration", "intervalDuration"),
            ("interval_height", "intervalHeight"),
            ("all_day", "allDay"),
            "interval",
            "event",
        ]
        self._event_names += []


class VCalendarMonthDay(HtmlElement):
    """
    Vuetify's VCalendarMonthDay component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar-month-day>`_.

    Args:
      title (string, number):
        Specify a title text for the component.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      day (unknown):
        Represents the specific day in the month view of the calendar.
      events (any[]):
        Array of events associated with this specific day.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendarMonthDay", children, **kwargs)
        self._attr_names += [
            "title",
            "active",
            "disabled",
            "color",
            "day",
            "events",
        ]
        self._event_names += []


class VCard(HtmlElement):
    """
    Vuetify's VCard component.
    See more `info and examples <https://vuetifyjs.com/api/v-card>`_.

    Args:
      title (string, number, boolean):
        Specify a title text for the component.
      text (string, number, boolean):
        Specify content text for the component.
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
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      image (string):
        Apply a specific background image to the component.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      subtitle (string, number, boolean):
        Specify a subtitle text for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      append_icon (enum):
        Creates a [v-icon](/api/v-icon/) component after default content
        in the **append** slot.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prepend_icon (enum):
        Prepends a [v-icon](/components/icons/) component to the header.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
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
            "title",
            "text",
            "flat",
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
            "location",
            "position",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            "image",
            "exact",
            "subtitle",
            "disabled",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "loading",
            "href",
            "to",
            "ripple",
            ("append_avatar", "appendAvatar"),
            "hover",
            ("prepend_avatar", "prependAvatar"),
        ]
        self._event_names += []


class VCardActions(HtmlElement):
    """
    Vuetify's VCardActions component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-actions>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardActions", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VCardItem(HtmlElement):
    """
    Vuetify's VCardItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-item>`_.

    Args:
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
      theme (string):
        Specify a theme for this component and all of its children.
      height (string, number):
        Sets the height for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
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
      interval (string, number):
        The duration between image cycles. Requires the **cycle** prop.
      cycle (boolean):
        Determines if the carousel should cycle through images.
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
      show_arrows (string, boolean):
        Displays arrows for next/previous navigation.
      touch (TouchHandlers):
        Provide a custom **left** and **right** function when swiped left or right.
      direction ('horizontal', 'vertical'):
        The transition direction when changing windows.
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
            "theme",
            "height",
            "disabled",
            ("selected_class", "selectedClass"),
            "color",
            ("model_value", "modelValue"),
            "mandatory",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            "interval",
            "cycle",
            ("delimiter_icon", "delimiterIcon"),
            ("hide_delimiters", "hideDelimiters"),
            ("hide_delimiter_background", "hideDelimiterBackground"),
            "continuous",
            ("show_arrows", "showArrows"),
            "touch",
            "direction",
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
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Prevents the item from becoming active when using the "next"
        and "prev" buttons or the `toggle` method.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      content_class (any):
        Apply a custom class to the internal content element.
      transition (string, boolean):
        The transition to use when switching from `lazy-src` to `src`.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.
      options (IntersectionObserverInit):
        Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
        constructor.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      alt (string):
        Alternate text for screen readers. Leave empty for decorative images.
      cover (boolean):
        Resizes the background image to cover the entire container.
      draggable (boolean, 'true', 'false'):
        Controls the `draggable` behavior of the image. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable).
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
      src (enum):
        The image URL. This prop is mandatory.

        Enum values: [
          string, { src: string; srcset: string; lazySrc: string; aspect: number }
        ]
      srcset (string):
        A set of alternate images to use based on device size. [Read
        more...](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset).
      aspect_ratio (string, number):
        Calculated as `width/height`, so for a 1920x1080px image this
        will be `1.7778`. Will be calculated automatically if omitted.
      inline (boolean):
        Display as an inline element instead of a block, also disables flex-grow.
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
            "eager",
            "disabled",
            "value",
            ("content_class", "contentClass"),
            "transition",
            "options",
            ("selected_class", "selectedClass"),
            "alt",
            "cover",
            "draggable",
            "gradient",
            ("lazy_src", "lazySrc"),
            "sizes",
            "src",
            "srcset",
            ("aspect_ratio", "aspectRatio"),
            "inline",
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
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      disabled (boolean):
        Removes the ability to click or target the component.
      multiple (boolean):
        Changes expected model to an array.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      id (string):
        Sets the DOM id on the component.
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
        Makes prepend/append icons full opacity when the input is focused.
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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      indeterminate (boolean):
        Sets an indeterminate state for the checkbox.
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
            ("model_value", "modelValue"),
            "error",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "color",
            "name",
            "label",
            ("base_color", "baseColor"),
            "disabled",
            "multiple",
            "value",
            ("value_comparator", "valueComparator"),
            "id",
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
            "ripple",
            "indeterminate",
            ("indeterminate_icon", "indeterminateIcon"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
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
      theme (string):
        Specify a theme for this component and all of its children.
      id (string):
        Sets the DOM id on the component.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      base_color (string):
        Sets the color of the input when it is not focused.
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      disabled (boolean):
        Removes the ability to click or target the component.
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
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      indeterminate (boolean):
        Puts the control in an indeterminate state. Used with the [indeterminate-icon](#props-indeterminate-icon)
        property.
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
      value_comparator ((a: any, b: any) => boolean):
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
            "theme",
            "id",
            "value",
            ("base_color", "baseColor"),
            "readonly",
            "ripple",
            "density",
            "disabled",
            "color",
            "inline",
            ("model_value", "modelValue"),
            "multiple",
            "indeterminate",
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
      theme (string):
        Specify a theme for this component and all of its children.
      size (string, number):
        Sets the height, padding and the font size of the component.
        Accepts only predefined options: **x-small**, **small**, **default**,
        **large**, and **x-large**.
      value (any):
        The value used when a child of a [v-chip-group](/components/chip-groups).
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
      ripple (boolean, { class: string }):
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
      disabled (boolean):
        Removes the ability to click or target the component.
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
      draggable (boolean):
        Makes the chip draggable.
      filter_icon (enum):
        Change the default icon used for **filter** chips.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      pill (boolean):
        Remove `v-avatar` padding.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_close (event):
        Emitted when close icon is clicked.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VChip", children, **kwargs)
        self._attr_names += [
            "filter",
            "replace",
            "link",
            "tag",
            "label",
            "theme",
            "size",
            "value",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "ripple",
            "text",
            "border",
            "density",
            "elevation",
            "disabled",
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
            "draggable",
            ("filter_icon", "filterIcon"),
            "pill",
        ]
        self._event_names += [
            "click",
            ("update_modelValue", "update:modelValue"),
            ("click_close", "click:close"),
            ("group_selected", "group:selected"),
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
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
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
      base_color (string):
        Sets the color of component when not focused. Recommended with
        `color` or `filter` to properly highlight selected items.
      disabled (boolean):
        Puts all children components into a disabled state.
      multiple (boolean):
        Allows one to select multiple items.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      direction ('horizontal', 'vertical'):
        Switch between horizontal and vertical modes.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      max (number):
        Sets a maximum number of selections that can be made.
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
      column (boolean):
        Remove horizontal pagination and wrap items as needed.
      center_active (boolean):
        Forces the selected chip to be centered.
      show_arrows (string, boolean):
        Force the display of the pagination arrows.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Sets the designated mobile breakpoint for the component.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VChipGroup", children, **kwargs)
        self._attr_names += [
            "symbol",
            "filter",
            ("model_value", "modelValue"),
            "tag",
            "theme",
            "color",
            "variant",
            ("base_color", "baseColor"),
            "disabled",
            "multiple",
            "mandatory",
            ("value_comparator", "valueComparator"),
            "direction",
            ("selected_class", "selectedClass"),
            "max",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            "column",
            ("center_active", "centerActive"),
            ("show_arrows", "showArrows"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VClassIcon(HtmlElement):
    """
    Vuetify's VClassIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-class-icon>`_.

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
        super().__init__("VClassIcon", children, **kwargs)
        self._attr_names += [
            "icon",
            "tag",
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


class VColorPicker(HtmlElement):
    """
    Vuetify's VColorPicker component.
    See more `info and examples <https://vuetifyjs.com/api/v-color-picker>`_.

    Args:
      title (string):
        Specify a title text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      model_value (string, Record<string, unknown>):
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
        Sets the width of the color picker.
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
      disabled (boolean):
        Removes the ability to click or target the component.
      mode ('rgb', 'rgba', 'hsl', 'hsla', 'hex', 'hexa'):
        The current selected input type. Syncable with `v-model:mode`.
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
      divided (boolean):
        Adds a divider between the header and controls.
      landscape (boolean):
        Puts the picker into landscape mode.
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
            "title",
            "border",
            ("model_value", "modelValue"),
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
            "disabled",
            "mode",
            ("hide_header", "hideHeader"),
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
      theme (string):
        Specify a theme for this component and all of its children.
      items (any[]):
        Can be an array of objects or strings. By default objects should
        have **title** and **value** properties, and can optionally have
        a **props** property containing any [VListItem props](/api/v-list-item/#props).
        Keys to use for these can be changed with the **item-title**,
        **item-value**, and **item-props** props.
      id (string):
        Sets the DOM id on the component.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the outnside the component's input, uses
        the same syntax as `v-icon`.

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
      width (string, number):
        Sets the width for the component.
      disabled (boolean):
        Removes the ability to click or target the input.
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
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
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
      close_text (string):
        Text set to the inputs `aria-label` and `title` when input menu is closed.
      open_text (string):
        Text set to the inputs **aria-label** and **title** when input menu is open.
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
      item_title (SelectItemKey<any>):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey<any>):
        Property on supplied `items` that contains its value.
      item_children (SelectItemKey):
        This property currently has **no effect**.
      item_props (SelectItemKey<any>):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
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
      autofocus (boolean):
        Enables autofocus.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      placeholder (string):
        Sets the input’s placeholder text.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
            "theme",
            "items",
            "id",
            "active",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "disabled",
            "loading",
            "rounded",
            "tile",
            "color",
            "variant",
            ("model_value", "modelValue"),
            "transition",
            ("bg_color", "bgColor"),
            "multiple",
            "eager",
            "prefix",
            "role",
            "direction",
            ("value_comparator", "valueComparator"),
            ("auto_select_first", "autoSelectFirst"),
            ("clear_on_select", "clearOnSelect"),
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            "chips",
            ("closable_chips", "closableChips"),
            ("close_text", "closeText"),
            ("open_text", "openText"),
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            ("list_props", "listProps"),
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("item_color", "itemColor"),
            "autofocus",
            "counter",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            "focused",
            ("hide_details", "hideDetails"),
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
        Represents the commited v-model value
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
      max (string, number):
        Sets the maximum allowed value.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCounter", children, **kwargs)
        self._attr_names += [
            "disabled",
            "value",
            "transition",
            "active",
            "max",
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
      value_comparator ((a: any, b: any) => boolean):
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
      sort_by (SortItem):
        Changes which item property (or properties) should be used for
        sort order. Can be used with `.sync` modifier.
      multi_sort (boolean):
        If `true` then one can sort on multiple properties.
      must_sort (boolean):
        If `true` then one can not disable sorting, it will always switch
        between ascending and descending.
      custom_key_sort (unknown):
        Function used on specific keys within the item object. `customSort`
        is skipped for columns with `customKeySort` specified.
      items_per_page (string, number):
        Changes how many items per page should be visible. Can be used
        with `.sync` modifier. Setting this prop to `-1` will display
        all items on the page.
      expand_on_click (boolean):
        Expands item when the row is clicked.
      show_expand (boolean):
        Shows the expand icon.
      expanded (string[]):
        Array of expanded items. Can be used with `.sync` modifier.
      group_by (SortItem):
        Changes which item property should be used for grouping items.
        Currently only supports a single grouping in the format: `group`
        or `['group']`. When using an array, only the first element is
        considered. Can be used with `.sync` modifier.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      update_expanded (event):
        The `.sync` event for `expanded` prop.
      update_groupBy (event):
        The `.sync` event for `groupBy` prop.
      update_page (event):
        The `.sync` event for `page` prop.
      update_itemsPerPage (event):
        The `.sync` event for `itemsPerPage` prop.
      update_sortBy (event):
        The `.sync` event for `sortBy` prop.
      update_options (event):
        The `.sync` event for `options` prop.
      update_currentItems (event):
        The `.sync` event for `currentItems` prop.
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
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
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
      select_strategy ('single', 'page', 'all'):
        Defines the strategy of selecting items in the list. Possible
        values are: 'single' (only one item can be selected at a time),
        'page' ('Select all' button will select only items on the current
        page), 'all' ('Select all' button will select all items in the
        list).
      items (any[]):
        An array of strings or objects used for automatically generating
        children components.
      item_value (SelectItemKey<any>):
        Property on supplied `items` that contains its value.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      no_data_text (string):
        Text shown when no items are provided to the component.
      loading (string, boolean):
        Displays `loading` slot if set to `true`
      next_icon (enum):
        Next icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        Previous icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hover (boolean):
        Adds a hover effects to a table rows.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      item_selectable (SelectItemKey<any>):
        Property on supplied `items` that indicates whether the item is selectable.
      show_select (boolean):
        Shows the select checkboxes in both the header and rows (if using default rows).
      page (string, number):
        The current displayed page number (1-indexed).
      sort_by (SortItem):
        Changes which item property (or properties) should be used for
        sort order. Can be used with `.sync` modifier.
      multi_sort (boolean):
        If `true` then one can sort on multiple properties.
      must_sort (boolean):
        If `true` then one can not disable sorting, it will always switch
        between ascending and descending.
      custom_key_sort (unknown):
        Function used on specific keys within the item object. `customSort`
        is skipped for columns with `customKeySort` specified.
      items_per_page (string, number):
        Changes how many items per page should be visible. Can be used
        with `.sync` modifier. Setting this prop to `-1` will display
        all items on the page.
      expand_on_click (boolean):
        Expands item when the row is clicked.
      show_expand (boolean):
        Shows the expand toggle in default rows.
      expanded (string[]):
        Whether the item is expanded or not.
      group_by (SortItem):
        Changes which item property should be used for grouping items.
        Currently only supports a single grouping in the format: `group`
        or `['group']`. When using an array, only the first element is
        considered. Can be used with `.sync` modifier.
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
                 'item', 'value', 'index', 'column', js_fn
        ]
      disable_sort (boolean):
        Disables sorting completely.
      headers (enum):
        An array of objects that each describe a header column. See the
        example below for a definition of all properties.

        Enum values: [
          {  readonly key?:, (string & {}), 'data-table-group', 'data-table-select',
          'data-table-expand', undefined  readonly value?: SelectItemKey<any>
           readonly title?: string, undefined  readonly fixed?: boolean,
          undefined  readonly align?: 'end', 'start', 'center', undefined
           readonly width?: string, number, undefined  readonly minWidth?:
          string, number, undefined  readonly maxWidth?: string, number,
          undefined  readonly nowrap?: boolean, undefined  readonly headerProps?:
          { readonly [x: string]: any }, undefined  readonly cellProps?:,
          { readonly [x: string]: any }, HeaderCellPropsFunction, undefined
           readonly sortable?: boolean, undefined  readonly sort?: DataTableCompareFunction<any>,
          undefined  readonly sortRaw?: DataTableCompareFunction<any>,
          undefined  readonly filter?: FilterFunction, undefined  readonly
          children?: readonly any[], undefined}[]
        ]
      loading_text (string):
        Text shown when the data is loading.
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
        Hides the default footer. This has no effect on `v-data-table-virtual`.
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
        Emits when the **expanded** property of the **options** prop is updated.
      update_groupBy (event):
        Emits when the **group-by** property of the **options** property is updated.
      update_page (event):
        Emits when the **page** property of the **options** prop is updated.
      update_itemsPerPage (event):
        Emits when the **items-per-page** property of the **options** prop is updated.
      update_sortBy (event):
        Emits when the **sortBy** property of the **options** prop is updated.
      update_options (event):
        Emits when one of the **options** properties is updated.
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
            ("select_strategy", "selectStrategy"),
            "items",
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            ("no_data_text", "noDataText"),
            "loading",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            "hover",
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            "page",
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
            ("row_props", "rowProps"),
            ("hide_default_body", "hideDefaultBody"),
            ("hide_default_footer", "hideDefaultFooter"),
            ("hide_default_header", "hideDefaultHeader"),
            ("fixed_header", "fixedHeader"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_footer", "fixedFooter"),
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
      next_icon (enum):
        Next icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        Previous icon.

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
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
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
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      sticky (boolean):
        Deprecated, use `fixed-header` instead.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      disable_sort (boolean):
        Toggles rendering of sort button.
      fixed_header (boolean):
        Sticks the header to the top of the table.
      multi_sort (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableHeaders.json))
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
      header_props (unknown):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableHeaders.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableHeaders", children, **kwargs)
        self._attr_names += [
            "loading",
            "sticky",
            "color",
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("disable_sort", "disableSort"),
            ("fixed_header", "fixedHeader"),
            ("multi_sort", "multiSort"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("header_props", "headerProps"),
        ]
        self._event_names += []


class VDataTableRow(HtmlElement):
    """
    Vuetify's VDataTableRow component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table-row>`_.

    Args:
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      item (unknown):
        Data (key, index and column values) of the displayed item.
      cell_props (enum):
        Props to be applied to the cell.

        Enum values: [
          Record<string, any>, ((      data: Pick<        ItemKeySlot<unknown>,
                 'value', 'item', 'index', 'internalItem', js_fn
        ]
      index (number):
        Row index.
      contextmenu (event):
        The event emitted when the user clicks the context menu button.
      dblclick (event):
        The event emitted when the user double clicks the row.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableRow", children, **kwargs)
        self._attr_names += [
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "item",
            ("cell_props", "cellProps"),
            "index",
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
      items (DataTableItem):
        An array of strings or objects used for automatically generating
        children components.
      loading (string, boolean):
        Displays `loading` slot if set to `true`
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      no_data_text (string):
        Text shown when no items are provided to the component.
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
            "items",
            "loading",
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("hide_no_data", "hideNoData"),
            ("no_data_text", "noDataText"),
            ("cell_props", "cellProps"),
            ("loading_text", "loadingText"),
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
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      items (any[]):
        An array of strings or objects used for automatically generating
        children components.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Use the height prop to set the height of the table.
      width (string, number):
        Sets the width for the component.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      sticky (boolean):
        Deprecated, use `fixed-header` instead.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      next_icon (enum):
        Next icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        Previous icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hover (boolean):
        Will add a hover effect to a table's row when the mouse is over it.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      select_strategy ('single', 'page', 'all'):
        Defines the strategy of selecting items in the list. Possible
        values are: 'single' (only one item can be selected at a time),
        'page' ('Select all' button will select only items on the current
        page), 'all' ('Select all' button will select all items in the
        list).
      item_value (SelectItemKey<any>):
        Property on supplied `items` that contains its value.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      no_data_text (string):
        Text shown when no items are provided to the component.
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
      headers (enum):
        An array of objects that each describe a header column.

        Enum values: [
          {  readonly key?:, (string & {}), 'data-table-expand', 'data-table-select',
          'data-table-group', undefined  readonly value?: SelectItemKey<Record<string,
          any>>  readonly title?: string, undefined  readonly fixed?: boolean,
          undefined  readonly align?: 'start', 'end', 'center', undefined
           readonly width?: string, number, undefined  readonly minWidth?:
          string, number, undefined  readonly maxWidth?: string, number,
          undefined  readonly nowrap?: boolean, undefined  readonly headerProps?:
          { readonly [x: string]: any }, undefined  readonly cellProps?:,
          HeaderCellPropsFunction, { readonly [x: string]: any }, undefined
           readonly sortable?: boolean, undefined  readonly sort?: DataTableCompareFunction<any>,
          undefined  readonly sortRaw?: DataTableCompareFunction<any>,
          undefined  readonly filter?: FilterFunction, undefined  readonly
          children?:, readonly {        readonly key?:, (string & {}),
          'data-table-expand', 'data-table-select', 'data-table-group',
          undefined        readonly value?: SelectItemKey<Record<string,
          any>>        readonly title?: string, undefined        readonly
          fixed?: boolean, undefined        readonly align?: 'start', 'end',
          'center', undefined        readonly width?: string, number, undefined
                 readonly minWidth?: string, number, undefined        readonly
          maxWidth?: string, number, undefined        readonly nowrap?:
          boolean, undefined        readonly headerProps?: { readonly [x:
          string]: any }, undefined        readonly cellProps?:, HeaderCellPropsFunction,
          { readonly [x: string]: any }, undefined        readonly sortable?:
          boolean, undefined        readonly sort?: DataTableCompareFunction<any>,
          undefined        readonly sortRaw?: DataTableCompareFunction<any>,
          undefined        readonly filter?: FilterFunction, undefined
                 readonly children?: readonly any[], undefined      }[],
          undefined}[]
        ]
      disable_sort (boolean):
        Toggles rendering of sort button.
      fixed_header (boolean):
        Use the fixed-header prop together with the height prop to fix
        the header to the top of the table.
      multi_sort (boolean):
        Allows sorting by multiple columns.
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
      sort_by (SortItem):
        Array of column keys and sort orders that determines the sort
        order of the table.
      page (string, number):
        The current displayed page number (1-indexed).
      expanded (string[]):
        Whether the item is expanded or not.
      expand_on_click (boolean):
        Expands item when the row is clicked.
      loading_text (string):
        Text shown when the data is loading.
      row_props (enum):
        An object of additional props to be passed to each `<tr>` in
        the table body. Also accepts a function that will be called for
        each row.

        Enum values: [
          Record<string, any>, ((      data: Pick<ItemKeySlot<any>, 'item', 'index', js_fn
        ]
      group_by (SortItem):
        Defines the grouping of the table items.
      items_length (string, number):
        Number of all items.
      items_per_page (string, number):
        The number of items to display on each page.
      hide_default_body (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/DataTable.json))
      hide_default_footer (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/DataTable.json))
      hide_default_header (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/DataTable.json))
      show_expand (boolean):
        Shows the expand icon.
      item_selectable (SelectItemKey<any>):
        Property on supplied `items` that indicates whether the item is selectable.
      show_select (boolean):
        Shows the column with checkboxes for selecting items in the list.
      must_sort (boolean):
        Forces sorting on the column(s).
      custom_key_sort (unknown):
        Function used on specific keys within the item object. `customSort`
        is skipped for columns with `customKeySort` specified.
      fixed_footer (boolean):
        Use the fixed-footer prop together with the height prop to fix
        the footer to the bottom of the table.
      update_modelValue (event):
        Emits when the component's model changes.
      update_expanded (event):
        Emits when the **expanded** property of the **options** prop is updated.
      update_page (event):
        Emits when the **page** property of the **options** prop is updated.
      update_itemsPerPage (event):
        Emits when the **items-per-page** property of the **options** prop is updated.
      update_sortBy (event):
        Emits when the **sort-by** property of the **options** prop is updated.
      update_options (event):
        Emits when one of the **options** properties is updated.
      update_groupBy (event):
        Emits when the **group-by** property of the **options** property is updated.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableServer", children, **kwargs)
        self._attr_names += [
            "search",
            "tag",
            "theme",
            "items",
            "density",
            "height",
            "width",
            "loading",
            "sticky",
            "color",
            ("model_value", "modelValue"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            "hover",
            ("value_comparator", "valueComparator"),
            ("hide_no_data", "hideNoData"),
            ("select_strategy", "selectStrategy"),
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            ("no_data_text", "noDataText"),
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
            "headers",
            ("disable_sort", "disableSort"),
            ("fixed_header", "fixedHeader"),
            ("multi_sort", "multiSort"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("header_props", "headerProps"),
            ("cell_props", "cellProps"),
            ("sort_by", "sortBy"),
            "page",
            "expanded",
            ("expand_on_click", "expandOnClick"),
            ("loading_text", "loadingText"),
            ("row_props", "rowProps"),
            ("group_by", "groupBy"),
            ("items_length", "itemsLength"),
            ("items_per_page", "itemsPerPage"),
            ("hide_default_body", "hideDefaultBody"),
            ("hide_default_footer", "hideDefaultFooter"),
            ("hide_default_header", "hideDefaultHeader"),
            ("show_expand", "showExpand"),
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            ("fixed_footer", "fixedFooter"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_expanded", "update:expanded"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_groupBy", "update:groupBy"),
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
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
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
      select_strategy ('single', 'page', 'all'):
        Defines the strategy of selecting items in the list. Possible
        values are: 'single' (only one item can be selected at a time),
        'page' ('Select all' button will select only items on the current
        page), 'all' ('Select all' button will select all items in the
        list).
      items (any[]):
        An array of strings or objects used for automatically generating
        children components.
      item_value (SelectItemKey<any>):
        Property on supplied `items` that contains its value.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      no_data_text (string):
        Text shown when no items are provided to the component.
      loading (string, boolean):
        Displays `loading` slot if set to `true`
      hover (boolean):
        Will add a hover effect to a table's row when the mouse is over it.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      item_selectable (SelectItemKey<any>):
        Property on supplied `items` that indicates whether the item is selectable.
      show_select (boolean):
        Shows the column with checkboxes for selecting items in the list.
      sort_by (SortItem):
        Array of column keys and sort orders that determines the sort
        order of the table.
      multi_sort (boolean):
        Allows sorting by multiple columns.
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
        Whether the item is expanded or not.
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
                 'item', 'value', 'index', 'column', js_fn
        ]
      disable_sort (boolean):
        Toggles rendering of sort button.
      headers (enum):
        An array of objects that each describe a header column.

        Enum values: [
          {  readonly key?:, (string & {}), 'data-table-group', 'data-table-select',
          'data-table-expand', undefined  readonly value?: SelectItemKey<Record<string,
          any>>  readonly title?: string, undefined  readonly fixed?: boolean,
          undefined  readonly align?: 'end', 'start', 'center', undefined
           readonly width?: string, number, undefined  readonly minWidth?:
          string, number, undefined  readonly maxWidth?: string, number,
          undefined  readonly nowrap?: boolean, undefined  readonly headerProps?:
          { readonly [x: string]: any }, undefined  readonly cellProps?:,
          { readonly [x: string]: any }, HeaderCellPropsFunction, undefined
           readonly sortable?: boolean, undefined  readonly sort?: DataTableCompareFunction<any>,
          undefined  readonly sortRaw?: DataTableCompareFunction<any>,
          undefined  readonly filter?: FilterFunction, undefined  readonly
          children?:, readonly {        readonly key?:, (string & {}),
          'data-table-group', 'data-table-select', 'data-table-expand',
          undefined        readonly value?: SelectItemKey<Record<string,
          any>>        readonly title?: string, undefined        readonly
          fixed?: boolean, undefined        readonly align?: 'end', 'start',
          'center', undefined        readonly width?: string, number, undefined
                 readonly minWidth?: string, number, undefined        readonly
          maxWidth?: string, number, undefined        readonly nowrap?:
          boolean, undefined        readonly headerProps?: { readonly [x:
          string]: any }, undefined        readonly cellProps?:, { readonly
          [x: string]: any }, HeaderCellPropsFunction, undefined
           readonly sortable?: boolean, undefined        readonly sort?:
          DataTableCompareFunction<any>, undefined        readonly sortRaw?:
          DataTableCompareFunction<any>, undefined        readonly filter?:
          FilterFunction, undefined        readonly children?: readonly
          any[], undefined      }[], undefined}[]
        ]
      loading_text (string):
        Text shown when the data is loading.
      row_props (enum):
        An object of additional props to be passed to each `<tr>` in
        the table body. Also accepts a function that will be called for
        each row.

        Enum values: [
          Record<string, any>, ((      data: Pick<ItemKeySlot<any>, 'item', 'index', js_fn
        ]
      hide_default_body (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/DataTable.json))
      hide_default_footer (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/DataTable.json))
      hide_default_header (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/DataTable.json))
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
      item_height (string, number):
        Height in pixels of each item to display.
      item_key (SelectItemKey):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/virtual.json))
      update_modelValue (event):
        Emits when the component's model changes.
      update_expanded (event):
        Emits when the **expanded** property of the **options** prop is updated.
      update_groupBy (event):
        Emits when the **group-by** property of the **options** property is updated.
      update_sortBy (event):
        Emits when the **sort-by** property of the **options** prop is updated.
      update_options (event):
        Emits when one of the **options** properties is updated.
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
            ("select_strategy", "selectStrategy"),
            "items",
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            ("no_data_text", "noDataText"),
            "loading",
            "hover",
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
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
            ("row_props", "rowProps"),
            ("hide_default_body", "hideDefaultBody"),
            ("hide_default_footer", "hideDefaultFooter"),
            ("hide_default_header", "hideDefaultHeader"),
            ("fixed_header", "fixedHeader"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_footer", "fixedFooter"),
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
      model_value (any):
        Represents the commited v-model value
      error (boolean):
        Puts the input in a manual error state.
      reverse (boolean):
        Reverses the orientation.
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
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDateInput.json))
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
      disabled (boolean):
        Removes the ability to click or target the input.
      multiple (number, boolean, (string & {}), 'range'):
        Allow the selection of multiple dates. The **range** value selects
        all dates between two selections.
      id (string):
        Sets the DOM id on the component.
      transition (string):
        The transition used when changing months into the future
      autofocus (boolean):
        Enables autofocus.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      prefix (string):
        Displays prefix text.
      placeholder (string):
        Sets the input’s placeholder text.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      role (string):
        The role attribute applied to the input.
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
        Makes prepend/append icons full opacity when the field is focused.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outnside the component's input, uses
        the same syntax as `v-icon`.

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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
      hide_header (boolean):
        Hide the picker header.
      month (string, number):
        Sets the month.
      show_adjacent_months (boolean):
        Toggles visibility of days from previous and next months.
      year (number):
        Sets the year.
      weekdays ((0, 1, 2, 4, 5, 6, 3)[]):
        Array of weekdays.
      weeks_in_month ('static', 'dynamic'):
        A dynamic number of weeks in a month will grow and shrink depending
        on how many days are in the month. A static number always shows
        7 weeks.
      first_day_of_week (string, number):
        Sets the first day of the week, starting with 0 for Sunday.
      allowed_dates (unknown[], js_fn):
        Restricts which dates can be selected.
      max (unknown):
        Maximum allowed date/month (ISO 8601 format).
      min (unknown):
        Minimum allowed date/month (ISO 8601 format).
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
      view_mode ('month', 'year', 'months'):
        Sets the view mode of the date picker.
      reverse_transition (string):
        The transition used when changing months into the past
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      divided (boolean):
        Adds a divider between the header and controls.
      landscape (boolean):
        Puts the picker into landscape mode.
      cancel_text (string):
        Text for the cancel button
      ok_text (string):
        Text for the ok button
      hide_actions (boolean):
        Hide the Cancel and OK buttons, and automatically update the
        value when a date is selected.
      display_format (string, Function):
        The format of the date that is displayed in the input. Can use
        any format [here](/features/dates/#format-options) or a custom
        function.
      header_color (string):
        Allows you to set a different color for the header when used
        in conjunction with the `color` prop.
      control_height (string, number):
        Sets the height of the controls.
      mode_icon (enum):
        Icon used for the mode button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      hide_weekdays (boolean):
        Hides the weekdays.
      show_week (boolean):
        Toggles visibility of the week numbers in the body of the calendar.
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
            "name",
            "header",
            "label",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "disabled",
            "multiple",
            "id",
            "transition",
            "autofocus",
            "counter",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            "role",
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
            ("hide_header", "hideHeader"),
            "month",
            ("show_adjacent_months", "showAdjacentMonths"),
            "year",
            "weekdays",
            ("weeks_in_month", "weeksInMonth"),
            ("first_day_of_week", "firstDayOfWeek"),
            ("allowed_dates", "allowedDates"),
            "max",
            "min",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("view_mode", "viewMode"),
            ("reverse_transition", "reverseTransition"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "divided",
            "landscape",
            ("cancel_text", "cancelText"),
            ("ok_text", "okText"),
            ("hide_actions", "hideActions"),
            ("display_format", "displayFormat"),
            ("header_color", "headerColor"),
            ("control_height", "controlHeight"),
            ("mode_icon", "modeIcon"),
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
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
      disabled (boolean):
        Removes the ability to click or target the component.
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
      max (unknown):
        Maximum allowed date/month (ISO 8601 format).
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
      multiple (number, boolean, (string & {}), 'range'):
        Allow the selection of multiple dates. The **range** value selects
        all dates between two selections.
      divided (boolean):
        Adds a divider between the header and controls.
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
      view_mode ('month', 'months', 'year'):
        Determines which picker in the date or month picker is being
        displayed. Allowed values: `'month'`, `'months'`, `'year'`.
      month (string, number):
        Sets the month.
      header_color (string):
        Allows you to set a different color for the header when used
        in conjunction with the `color` prop.
      control_height (string, number):
        Sets the height of the controls.
      mode_icon (enum):
        Icon displayed next to the current month and year, toggles year
        selection when clicked.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      year (number):
        Sets the year.
      hide_weekdays (boolean):
        Hides the weekdays.
      show_week (boolean):
        Toggles visibility of the week numbers in the body of the calendar.
      reverse_transition (string):
        The transition used when changing months into the past
      show_adjacent_months (boolean):
        Toggles visibility of days from previous and next months.
      weekdays ((0, 1, 2, 3, 4, 5, 6)[]):
        Array of weekdays.
      weeks_in_month ('static', 'dynamic'):
        A dynamic number of weeks in a month will grow and shrink depending
        on how many days are in the month. A static number always shows
        7 weeks.
      first_day_of_week (string, number):
        Sets the first day of the week, starting with 0 for Sunday.
      allowed_dates (unknown[], js_fn):
        Restricts which dates can be selected.
      min (unknown):
        Minimum allowed date/month (ISO 8601 format).
      landscape (boolean):
        Changes the picker to landscape mode.
      hide_header (boolean):
        Hides the header.
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
            "theme",
            "active",
            "text",
            "border",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "disabled",
            "location",
            "position",
            "rounded",
            "tile",
            "color",
            "max",
            ("model_value", "modelValue"),
            "transition",
            ("bg_color", "bgColor"),
            "multiple",
            "divided",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("view_mode", "viewMode"),
            "month",
            ("header_color", "headerColor"),
            ("control_height", "controlHeight"),
            ("mode_icon", "modeIcon"),
            "year",
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
            ("reverse_transition", "reverseTransition"),
            ("show_adjacent_months", "showAdjacentMonths"),
            "weekdays",
            ("weeks_in_month", "weeksInMonth"),
            ("first_day_of_week", "firstDayOfWeek"),
            ("allowed_dates", "allowedDates"),
            "min",
            "landscape",
            ("hide_header", "hideHeader"),
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
      active (string, string[]):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      text (string):
        Specify content text for the component.
      disabled (string, boolean, string[]):
        Removes the ability to click or target the component.
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
      view_mode ('month', 'months', 'year'):
        Sets the view mode of the date picker.
      control_height (string, number):
        Sets the height of the controls.
      mode_icon (enum):
        Icon used for the mode button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      click_next (event):
        Event fired when clicking the next button.
      click_prev (event):
        Event fired when clicking the previous button.
      click_year (event):
        Event fired when clicking the date text.
      click_month (event):
        Event fired when clicking on the month.
      click_text (event):
        Event fired when clicking the year.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerControls", children, **kwargs)
        self._attr_names += [
            "active",
            "text",
            "disabled",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("view_mode", "viewMode"),
            ("control_height", "controlHeight"),
            ("mode_icon", "modeIcon"),
        ]
        self._event_names += [
            ("click_next", "click:next"),
            ("click_prev", "click:prev"),
            ("click_year", "click:year"),
            ("click_month", "click:month"),
            ("click_text", "click:text"),
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
      model_value (unknown[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      disabled (boolean):
        Removes the ability to click or target the component.
      multiple (number, boolean, (string & {}), 'range'):
        Sets the multiple of the month.
      transition (string):
        The transition used when changing months into the future
      month (string, number):
        Sets the month.
      show_adjacent_months (boolean):
        Show adjacent months.
      year (string, number):
        Sets the year.
      weekdays ((0, 1, 2, 4, 5, 6, 3)[]):
        Sets the weekdays of the month.
      weeks_in_month ('static', 'dynamic'):
        A dynamic number of weeks in a month will grow and shrink depending
        on how many days are in the month. A static number always shows
        7 weeks.
      first_day_of_week (string, number):
        Sets the first day of the week, starting with 0 for Sunday.
      allowed_dates (unknown[], js_fn):
        Sets the allowed dates of the month.
      max (unknown):
        Sets the maximum date of the month.
      min (unknown):
        Sets the minimum date of the month.
      reverse_transition (string):
        The transition used when changing months into the past
      hide_weekdays (boolean):
        Hide the days of the week letters.
      show_week (boolean):
        Show the week number.
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
            ("model_value", "modelValue"),
            "color",
            "disabled",
            "multiple",
            "transition",
            "month",
            ("show_adjacent_months", "showAdjacentMonths"),
            "year",
            "weekdays",
            ("weeks_in_month", "weeksInMonth"),
            ("first_day_of_week", "firstDayOfWeek"),
            ("allowed_dates", "allowedDates"),
            "max",
            "min",
            ("reverse_transition", "reverseTransition"),
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
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
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      max (unknown):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerMonths.json))
      model_value (number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      year (number):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerMonths.json))
      min (unknown):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerMonths.json))
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerMonths", children, **kwargs)
        self._attr_names += [
            "height",
            "color",
            "max",
            ("model_value", "modelValue"),
            "year",
            "min",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VDatePickerYears(HtmlElement):
    """
    Vuetify's VDatePickerYears component.
    See more `info and examples <https://vuetifyjs.com/api/v-date-picker-years>`_.

    Args:
      model_value (number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      height (string, number):
        Sets the height for the component.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      max (unknown):
        Sets the maximum date of the month.
      min (unknown):
        Sets the minimum date of the month.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerYears", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "height",
            "color",
            "max",
            "min",
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
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Removes the ability to click or target the component.
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
        Sets the overlay opacity.
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
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        A single value that offsets content away from the target based
        upon what side it is on.
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          { component: Component }
        ]
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default.
      fullscreen (boolean):
        Changes layout for fullscreen display.
      retain_focus (boolean):
        Tab focus will return to the first child of the dialog by default.
        Disable this when using external tools that require focus such
        as TinyMCE or vue-clipboard.
      scrollable (boolean):
        When set to true, expects a `v-card` and a `v-card-text` component
        with a designated height. For more information, check out the
        [scrollable example](/components/dialogs#scrollable).
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
            "eager",
            "disabled",
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
            ("scroll_strategy", "scrollStrategy"),
            "transition",
            "attach",
            "fullscreen",
            ("retain_focus", "retainFocus"),
            "scrollable",
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
      inset (boolean):
        Adds indentation (72px) for **normal** dividers, reduces max
        height for **vertical**.
      opacity (string, number):
        Sets the component's opacity value
      vertical (boolean):
        Displays dividers vertically.
      thickness (string, number):
        Sets the dividers thickness. Default unit is px.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDivider", children, **kwargs)
        self._attr_names += [
            "length",
            "theme",
            "color",
            "inset",
            "opacity",
            "vertical",
            "thickness",
        ]
        self._event_names += []


class VEmptyState(HtmlElement):
    """
    Vuetify's VEmptyState component.
    See more `info and examples <https://vuetifyjs.com/api/v-empty-state>`_.

    Args:
      title (string):
        Specify a title text for the component.
      theme (string):
        Specify a theme for this component and all of its children.
      size (string, number):
        The size used to control the dimensions of the media element
        inside the component. Can be specified as a number or a string
        (e.g., '50%', '100px').
      text (string):
        Specify content text for the component.
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
            "theme",
            "size",
            "text",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
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
      disabled (boolean):
        Removes the ability to click or target the component.
      mode ('default', 'in-out', 'out-in'):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpandTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "group",
        ]
        self._event_names += []


class VExpandXTransition(HtmlElement):
    """
    Vuetify's VExpandXTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-expand-x-transition>`_.

    Args:
      disabled (boolean):
        Removes the ability to click or target the component.
      mode ('default', 'in-out', 'out-in'):
        Sets the transition mode (does not apply to transition-group).
        You can find more information on the Vue documentation [for transition
        modes](https://vuejs.org/api/built-in-components.html#transition).
      group (boolean):
        Creates a `transition-group` component. You can find more information
        in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpandXTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
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
      value (any):
        Controls the opened/closed state of content.
      readonly (boolean):
        Makes the expansion panel content read only.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      text (string):
        Specify content text for the component.
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
      disabled (boolean):
        Disables the expansion-panel content.
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
            "value",
            "readonly",
            "ripple",
            "text",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "disabled",
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
      readonly (boolean):
        Makes the expansion panel content read only.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      hide_actions (boolean):
        Hide the expand icon in the content title.
      focusable (boolean):
        Makes the expansion panel headers focusable.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanelTitle", children, **kwargs)
        self._attr_names += [
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "static",
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "readonly",
            "ripple",
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
      theme (string):
        Specify a theme for this component and all of its children.
      readonly (boolean):
        Makes the entire expansion panel read only.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      disabled (boolean):
        Puts all children components into a disabled state.
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
      max (number):
        Sets a maximum number of selections that can be made.
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      multiple (boolean):
        Allows one to select multiple items.
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
            "theme",
            "readonly",
            "ripple",
            "elevation",
            "disabled",
            ("selected_class", "selectedClass"),
            "static",
            "rounded",
            "tile",
            "color",
            "variant",
            "max",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "multiple",
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
      text (string, number, boolean):
        Specify content text for the component.
      flat (boolean):
        Removes the button box shadow. This is different than using the 'flat' variant.
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/)
        component. The button will become _round_.

        Enum values: [
          boolean, string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      model_value (boolean):
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
        Sets the width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location (Anchor):
        The location of the fab relative to the layout. Only works when using **app**.
      position ('fixed', 'static', 'relative', 'absolute', 'sticky'):
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
      name (string):
        Assign a specific name for layout registration.
      extended (boolean):
        An alternate style for the FAB that expects text.
      order (string, number):
        Adjust the order of the component in relation to its registration order.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        The applied color when the component is in an active state.
      disabled (boolean):
        Removes the ability to click or target the component.
      slim (boolean):
        Reduces padding to 0 8px.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      offset (boolean):
        Translates the Fab up or down, depending on if location is set
        to **top** or **bottom**.
      block (boolean):
        Expands the button to 100% of available space.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
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
      readonly (boolean):
        Puts the button in a readonly state. Cannot be clicked or navigated
        to by keyboard.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      stacked (boolean):
        Displays the button as a flex-column.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      app (boolean):
        If true, attaches to the closest layout and positions according
        to the value of **location**.
      appear (boolean):
        Used to control the animation of the FAB.
      layout (boolean):
        If true, will effect layout dimensions based on size and position.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFab", children, **kwargs)
        self._attr_names += [
            "symbol",
            "text",
            "flat",
            "replace",
            "border",
            "icon",
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
            "absolute",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            "name",
            "extended",
            "order",
            "exact",
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            "disabled",
            "slim",
            "value",
            "offset",
            "block",
            "transition",
            "size",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "readonly",
            "active",
            "loading",
            "href",
            "to",
            "stacked",
            "ripple",
            ("selected_class", "selectedClass"),
            "app",
            "appear",
            "layout",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VFabTransition(HtmlElement):
    """
    Vuetify's VFabTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-fab-transition>`_.

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
        super().__init__("VFabTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
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
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      theme (string):
        Specify a theme for this component and all of its children.
      id (string):
        Sets the DOM id on the component.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      base_color (string):
        Sets the color of the input when it is not focused.
      disabled (boolean):
        Removes the ability to click or target the input.
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
        Makes prepend/append icons full opacity when the field is focused.
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
            "label",
            "theme",
            "id",
            "active",
            ("base_color", "baseColor"),
            "disabled",
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
      model_value (File, File[]):
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
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      name (string):
        Sets the component's name attribute.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      chips (boolean):
        Changes display of selections to chips.
      base_color (string):
        Sets the color of the input when it is not focused.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      disabled (boolean):
        Removes the ability to click or target the input.
      multiple (boolean):
        Adds the **multiple** attribute to the input, allowing multiple file selections.
      id (string):
        Sets the DOM id on the component.
      counter (boolean):
        Displays the number of selected files.
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
        Makes prepend/append icons full opacity when the field is focused.
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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
        super().__init__("VFileInput", children, **kwargs)
        self._attr_names += [
            "flat",
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
            "label",
            "chips",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "disabled",
            "multiple",
            "id",
            "counter",
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
            ("counter_size_string", "counterSizeString"),
            ("counter_string", "counterString"),
            ("hide_input", "hideInput"),
            ("show_size", "showSize"),
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
      theme (string):
        Specify a theme for this component and all of its children.
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
      disabled (boolean):
        Removes the ability to click or target the component.
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
      multiple (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUpload.json))
      opacity (string, number):
        Sets the component's opacity value
      scrim (string, boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUpload.json))
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
      browse_text (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUpload.json))
      divider_text (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUpload.json))
      hide_browse (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUpload.json))
      show_size (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUpload.json))
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFileUpload", children, **kwargs)
        self._attr_names += [
            "length",
            "tag",
            "name",
            "title",
            "theme",
            "border",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "disabled",
            "location",
            "position",
            "rounded",
            "tile",
            "color",
            "icon",
            ("model_value", "modelValue"),
            "multiple",
            "opacity",
            "scrim",
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "subtitle",
            "clearable",
            "thickness",
            ("browse_text", "browseText"),
            ("divider_text", "dividerText"),
            ("hide_browse", "hideBrowse"),
            ("show_size", "showSize"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VFileUploadItem(HtmlElement):
    """
    Vuetify's VFileUploadItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-file-upload-item>`_.

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
      theme (string):
        Specify a theme for this component and all of its children.
      value (any):
        The value used for selection. Obtained from [`v-list`](/api/v-list)'s
        `v-model:selected` when the item is selected.
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
      slim (boolean):
        Reduces horizontal spacing for badges, icons, tooltips, and avatars
        to create a more compact visual representation.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
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
      disabled (boolean):
        Removes the ability to click or target the component.
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
      clearable (boolean):
        Allows for the component to be cleared.
      show_size (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUploadItem.json))
      file (File):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUploadItem.json))
      file_icon (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUploadItem.json))
      click_remove (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VFileUploadItem.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFileUploadItem", children, **kwargs)
        self._attr_names += [
            "replace",
            "link",
            "tag",
            "nav",
            "title",
            "theme",
            "value",
            "active",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "slim",
            "ripple",
            "border",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "disabled",
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
            "clearable",
            ("show_size", "showSize"),
            "file",
            ("file_icon", "fileIcon"),
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
      theme (string):
        Specify a theme for this component and all of its children.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      height (string, number):
        Sets the height for the component.
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
            "theme",
            "border",
            "height",
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
      readonly (boolean):
        Puts all children inputs into a readonly state.
      disabled (boolean):
        Puts all children inputs into a disabled state.
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
            "readonly",
            "disabled",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("fast_fail", "fastFail"),
        ]
        self._event_names += [
            "submit",
            ("update_modelValue", "update:modelValue"),
        ]


class VHover(HtmlElement):
    """
    Vuetify's VHover component.
    See more `info and examples <https://vuetifyjs.com/api/v-hover>`_.

    Args:
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      disabled (boolean):
        Removes hover functionality.
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
            ("model_value", "modelValue"),
            "disabled",
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
      opacity (string, number):
        Sets the component's opacity value
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
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
            "opacity",
            "size",
        ]
        self._event_names += []


class VIconBtn(HtmlElement):
    """
    Vuetify's VIconBtn component.
    See more `info and examples <https://vuetifyjs.com/api/v-icon-btn>`_.

    Args:
      text (string, number, boolean):
        Specify content text for the component.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      height (string, number):
        Sets the height for the component.
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
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      active_color (string):
        The applied color when the component is in an active state.
      disabled (boolean):
        Removes the ability to click or target the component.
      opacity (string, number):
        Sets the component's opacity value
      size (string, number):
        Sets the height and width of the component.
      icon_color (string):
        Explicit color applied to the icon.
      readonly (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VIconBtn.json))
      active (boolean):
        When undefined (default), the component utilizes its default
        variant, otherwise it will use the activeVariant if active is
        true, or the baseVariant if active is false.
      loading (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VIconBtn.json))
      sizes (enum):
        An array of tuples that define the button sizes for each named size.

        Enum values: [
          ['default', 'small', 'x-small', 'large', 'x-large', number][]
        ]
      base_variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        When active is a boolean, this variant is used when active is false.
      hide_overlay (boolean):
        Hides overlay from being displayed when active or focused.
      icon_size (string, number):
        The specific size of the icon, can use named sizes.
      icon_sizes (enum):
        An array of tuples that define the icon sizes for each named size.

        Enum values: [
          ['default', 'small', 'x-small', 'large', 'x-large', number][]
        ]
      rotate (string, number):
        The rotation of the icon in degrees.
      active_icon (enum):
        When active is a boolean, this icon is used when active is true.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      active_variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        When active is a boolean, this variant is used when active is true.
      update_active (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VIconBtn.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VIconBtn", children, **kwargs)
        self._attr_names += [
            "text",
            "border",
            "icon",
            "height",
            "width",
            "elevation",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            ("active_color", "activeColor"),
            "disabled",
            "opacity",
            "size",
            ("icon_color", "iconColor"),
            "readonly",
            "active",
            "loading",
            "sizes",
            ("base_variant", "baseVariant"),
            ("hide_overlay", "hideOverlay"),
            ("icon_size", "iconSize"),
            ("icon_sizes", "iconSizes"),
            "rotate",
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
      inline (boolean):
        Display as an inline element instead of a block, also disables flex-grow.
      transition (enum):
        The transition to use when switching from `lazy-src` to `src`.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component })
        ]
      content_class (any):
        Apply a custom class to the internal content element.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      draggable (boolean, 'true', 'false'):
        Controls the `draggable` behavior of the image. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable).
      options (IntersectionObserverInit):
        Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
        constructor.
      alt (string):
        Alternate text for screen readers. Leave empty for decorative images.
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
      src (enum):
        The image URL. This prop is mandatory.

        Enum values: [
          string, { src: string; srcset: string; lazySrc: string; aspect: number }
        ]
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
            "inline",
            "transition",
            ("content_class", "contentClass"),
            "eager",
            "draggable",
            "options",
            "alt",
            "cover",
            "gradient",
            ("lazy_src", "lazySrc"),
            "sizes",
            "src",
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
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      mode ('intersect', 'manual'):
        Specifies if content should load automatically when scrolling
        (**intersect**) or manually (**manual**).
      direction ('horizontal', 'vertical'):
        Specifies if scroller is **vertical** or **horizontal**.
      side ('end', 'start', 'both'):
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
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "tag",
            "color",
            "mode",
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
      name (string):
        Sets the component's name attribute.
      error (boolean):
        Puts the input in a manual error state.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      theme (string):
        Specify a theme for this component and all of its children.
      id (string):
        Sets the DOM id on the component.
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
      width (string, number):
        Sets the width for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
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
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the input is focused.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
            "name",
            "error",
            "label",
            "theme",
            "id",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "disabled",
            "color",
            ("model_value", "modelValue"),
            "direction",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
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
      multiple (boolean):
        Allows one to select multiple items.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      selected_class (string):
        Configure the selected CSS class. This class will be available
        in `v-item` default scoped slot.
      max (number):
        Sets a maximum number of selections that can be made.
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
            "multiple",
            "mandatory",
            ("selected_class", "selectedClass"),
            "max",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VKbd(HtmlElement):
    """
    Vuetify's VKbd component.
    See more `info and examples <https://vuetifyjs.com/api/v-kbd>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VKbd", children, **kwargs)
        self._attr_names += [
            "tag",
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
      full_height (boolean):
        Sets the component height to 100%.
      overlaps (string[]):
        **FOR INTERNAL USE ONLY**
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
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLayout", children, **kwargs)
        self._attr_names += [
            ("full_height", "fullHeight"),
            "overlaps",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
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
      order (string, number):
        Adjust the order of the component in relation to its registration order.
      size (string, number):
        Sets the height and width of the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLayoutItem", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "position",
            "absolute",
            "name",
            "order",
            "size",
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
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
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
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      activated (any):
        Array of ids of activated nodes.
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        The applied color when the component is in an active state.
      active_class (string):
        The class applied to the component when it is in an active state.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      disabled (boolean):
        Puts all children inputs into a disabled state.
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
      lines (false, 'one', 'two', 'three'):
        Designates a **minimum-height** for all children `v-list-item`
        components. This prop uses [line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp)
        and is not supported in all browsers.
      slim (boolean):
        Reduces horizontal spacing for badges, icons, tooltips, and avatars
        within slim list items to create a more compact visual representation.
      nav (boolean):
        An alternative styling that reduces `v-list-item` width and rounds
        the corners. Typically used with **[v-navigation-drawer](/components/navigation-drawers)**.
      activatable (boolean):
        Designates whether the list items are activatable.
      selectable (boolean):
        Designates whether the list items are selectable.
      opened (unknown):
        An array containing the values of currently opened groups. Can
        be two-way bound with `v-model:opened`.
      selected (unknown):
        An array containing the values of currently selected items. Can
        be two-way bound with `v-model:selected`.
      mandatory (boolean):
        Forces at least one item to always be selected (if available).
      active_strategy (ActiveStrategy):
        Affects how items with children behave when activated. - **leaf:**
        Only leaf nodes (items without children) can be activated. -
        **independent:** All nodes can be activated whether they have
        children or not. - **classic:** Activating a parent node will
        cause all children to be activated.
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
      item_type (string):
        Designates the key on the supplied items that is used for determining
        the nodes type.
      items (any[]):
        Can be an array of objects or strings. By default objects should
        have a **title** property, and can optionally have a **props**
        property containing any [VListItem props](/api/v-list-item/#props),
        a **value** property to allow selection, and a **children** property
        containing more item objects. Keys to use for these can be changed
        with the **item-title**, **item-value**, **item-props**, and
        **item-children** props.
      item_title (SelectItemKey<any>):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey<any>):
        Property on supplied `items` that contains its value.
      item_children (SelectItemKey<any>):
        Property on supplied `items` that contains its children.
      item_props (SelectItemKey<any>):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
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
            "activated",
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            ("active_class", "activeClass"),
            ("bg_color", "bgColor"),
            "disabled",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "lines",
            "slim",
            "nav",
            "activatable",
            "selectable",
            "opened",
            "selected",
            "mandatory",
            ("active_strategy", "activeStrategy"),
            ("select_strategy", "selectStrategy"),
            ("open_strategy", "openStrategy"),
            ("item_type", "itemType"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
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
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      title (string):
        Specify a title text for the component.
      value (any):
        Expands / Collapse the list-group.
      active_color (string):
        The applied color when the component is in an active state.
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
      fluid (boolean):
        Removes the left padding assigned for action icons from group items.
      subgroup (boolean):
        Designate the component as nested list group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListGroup", children, **kwargs)
        self._attr_names += [
            "tag",
            "title",
            "value",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "fluid",
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
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      subtitle (string, number, boolean):
        Specify a subtitle text for the component.
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        The applied color when the component is in an active state.
      active_class (string):
        The class applied to the component when it matches the current
        route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class)
        on the [vue-router](https://router.vuejs.org/) documentation.
      disabled (boolean):
        Removes the ability to click or target the component.
      lines (false, 'one', 'two', 'three'):
        The line declaration specifies the minimum height of the item
        and can also be controlled from v-list with the same prop.
      slim (boolean):
        Reduces horizontal spacing for badges, icons, tooltips, and avatars
        to create a more compact visual representation.
      nav (boolean):
        Reduces the width v-list-item takes up as well as adding a border radius.
      value (any):
        The value used for selection. Obtained from [`v-list`](/api/v-list)'s
        `v-model:selected` when the item is selected.
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
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      append_avatar (string):
        Appends a [v-avatar](/components/avatars/) component after default
        content in the **append** slot.
      prepend_avatar (string):
        Prepends a [v-avatar](/components/avatars/) component in the
        **prepend** slot before default content.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItem", children, **kwargs)
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
            "exact",
            "subtitle",
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            ("active_class", "activeClass"),
            "disabled",
            "lines",
            "slim",
            "nav",
            "value",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "active",
            "href",
            "to",
            "ripple",
            ("append_avatar", "appendAvatar"),
            ("prepend_avatar", "prependAvatar"),
        ]
        self._event_names += [
            "click",
        ]


class VListItemAction(HtmlElement):
    """
    Vuetify's VListItemAction component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-action>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      start (boolean):
        Applies margin at the end of the component.
      end (boolean):
        Applies margin at the start of the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemAction", children, **kwargs)
        self._attr_names += [
            "tag",
            "start",
            "end",
        ]
        self._event_names += []


class VListItemMedia(HtmlElement):
    """
    Vuetify's VListItemMedia component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-media>`_.

    Args:
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      start (boolean):
        Applies margin at the end of the component.
      end (boolean):
        Applies margin at the start of the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemMedia", children, **kwargs)
        self._attr_names += [
            "tag",
            "start",
            "end",
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
      scrollable (boolean):
        Specify a custom scrollable function.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMain", children, **kwargs)
        self._attr_names += [
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "tag",
            "scrollable",
        ]
        self._event_names += []


class VMenu(HtmlElement):
    """
    Vuetify's VMenu component.
    See more `info and examples <https://vuetifyjs.com/api/v-menu>`_.

    Args:
      theme (string):
        Specify a theme for this component and all of its children.
      id (string):
        The unique identifier of the component.
      height (string, number):
        Sets the height for the component.
      max_height (string, number):
        Sets the maximum height for the component.
      max_width (string, number):
        Sets the maximum width for the component.
      min_height (string, number):
        Sets the minimum height for the component.
      min_width (string, number):
        Sets the minimum width for the component. Use `auto` to use the activator width.
      width (string, number):
        Sets the width for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
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
          { component: Component }
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
        Sets the overlay opacity.
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
        A single value that offsets content away from the target based
        upon what side it is on.
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
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
            "theme",
            "id",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "disabled",
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
            ("scroll_strategy", "scrollStrategy"),
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
      active (boolean):
        Determines whether the messages are visible or not.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMessages", children, **kwargs)
        self._attr_names += [
            "color",
            "transition",
            "messages",
            "active",
        ]
        self._event_names += []


class VNavigationDrawer(HtmlElement):
    """
    Vuetify's VNavigationDrawer component.
    See more `info and examples <https://vuetifyjs.com/api/v-navigation-drawer>`_.

    Args:
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      model_value (boolean):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      width (string, number):
        Sets the width for the component.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      location ('top', 'end', 'bottom', 'start', 'left', 'right'):
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
        Apply a specific background image to the component.
      floating (boolean):
        A floating drawer has no visible container (no border-right).
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
      disable_resize_watcher (boolean):
        Prevents the automatic opening or closing of the drawer when
        resized, based on whether the device is mobile or desktop.
      disable_route_watcher (boolean):
        Disables opening of navigation drawer when route changes.
      expand_on_hover (boolean):
        Collapses the drawer to a **mini-variant** until hovering with the mouse.
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
            "border",
            ("model_value", "modelValue"),
            "width",
            "elevation",
            "location",
            "absolute",
            "sticky",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "name",
            "image",
            "floating",
            "order",
            "persistent",
            "scrim",
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
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
      theme (string):
        Specify a theme for this component and all of its children.
      id (string):
        Sets the DOM id on the component.
      active (boolean):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      base_color (string):
        Sets the color of the input when it is not focused.
      prepend_icon (enum):
        Prepends an icon to the outnside the component's input, uses
        the same syntax as `v-icon`.

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
      width (string, number):
        Sets the width for the component.
      disabled (boolean):
        Removes the ability to click or target the input.
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
      max (number):
        Specifies the maximum allowable value for the input.
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
      prefix (string):
        Displays prefix text.
      role (string):
        The role attribute applied to the input.
      direction ('horizontal', 'vertical'):
        Changes the direction of the input.
      autofocus (boolean):
        Enables autofocus.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      placeholder (string):
        Sets the input’s placeholder text.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      center_affix (boolean):
        Vertically align **appendInner**, **prependInner**, **clearIcon**
        and **label** in the center.
      glow (boolean):
        Makes prepend/append icons full opacity when the field is focused.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Displays hint text below the input when focused. Force this always
        open with the [persistent-hint](#props-persistent-hint) property.
      persistent_hint (boolean):
        Forces [hint](#props-hint) to always be visible.
      messages (string, string[]):
        Displays a list of messages or a single message if using a string.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
      min (number):
        Specifies the minimum allowable value for the input.
      control_variant ('split', 'default', 'hidden', 'stacked'):
        The color of the control. It defaults to the value of `variant` prop.
      hide_input (boolean):
        Hide the input field.
      step (number):
        Defines the interval between allowed values when the user increments
        or decrements the input
      precision (number):
        Enforces strict precision. It is expected to be an integer value
        in range between `0` and `15`, or null for unrestricted.
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
            "theme",
            "id",
            "active",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "disabled",
            "loading",
            "rounded",
            "tile",
            "color",
            "variant",
            "max",
            ("model_value", "modelValue"),
            ("bg_color", "bgColor"),
            "inset",
            "prefix",
            "role",
            "direction",
            "autofocus",
            "counter",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("center_affix", "centerAffix"),
            "glow",
            ("icon_color", "iconColor"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "rules",
            ("validate_on", "validateOn"),
            "focused",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
            "min",
            ("control_variant", "controlVariant"),
            ("hide_input", "hideInput"),
            "step",
            "precision",
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
      disabled (boolean):
        Removes the ability to click or target the input.
      autofocus (boolean):
        Automatically focuses the first input on page load
      placeholder (string):
        Sets the input’s placeholder text.
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
            "label",
            "divider",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "disabled",
            "autofocus",
            "placeholder",
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
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Removes the ability to click or target the component.
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
        Sets the overlay opacity.
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
        A single value that offsets content away from the target based
        upon what side it is on.
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
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
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VOverlay.json))
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
            "eager",
            "disabled",
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
            ("scroll_strategy", "scrollStrategy"),
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
      active_color (string):
        The applied color when the component is in an active state.
      disabled (boolean):
        Removes the ability to click or target the component.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      next_icon (enum):
        The icon to use for the next button.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        The icon to use for the prev button.

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
      aria_label (string):
        Label for the root element.
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
            ("active_color", "activeColor"),
            "disabled",
            "size",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("first_icon", "firstIcon"),
            ("last_icon", "lastIcon"),
            ("aria_label", "ariaLabel"),
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
      hide_header (boolean):
        Hide the picker header.
      divided (boolean):
        Adds a divider between the header and controls.
      landscape (boolean):
        Puts the picker into landscape mode.
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
            ("hide_header", "hideHeader"),
            "divided",
            "landscape",
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


class VProgressCircular(HtmlElement):
    """
    Vuetify's VProgressCircular component.
    See more `info and examples <https://vuetifyjs.com/api/v-progress-circular>`_.

    Args:
      model_value (string, number):
        The percentage value for current progress.
      width (string, number):
        Sets the stroke of the circle in pixels.
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
      size (string, number):
        Sets the diameter of the circle in pixels.
      indeterminate (boolean, 'disable-shrink'):
        Constantly animates, use when loading progress is unknown. If
        set to the string `'disable-shrink'` it will use a simpler animation
        that does not run on the main thread.
      rotate (string, number):
        Rotates the circle start point in degrees.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VProgressCircular", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "width",
            "tag",
            "theme",
            "color",
            ("bg_color", "bgColor"),
            "size",
            "indeterminate",
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
      max (string, number):
        Sets the maximum value the progress can reach.
      indeterminate (boolean):
        Constantly animates, use when loading progress is unknown.
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
      stream (boolean):
        An alternative style for portraying loading that works in tandem
        with **buffer-value**.
      striped (boolean):
        Adds a stripe background to the filled portion of the progress component.
      rounded_bar (boolean):
        Applies a border radius to the progress bar.
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
            ("bg_color", "bgColor"),
            "opacity",
            "active",
            "max",
            "indeterminate",
            ("bg_opacity", "bgOpacity"),
            ("buffer_value", "bufferValue"),
            ("buffer_color", "bufferColor"),
            ("buffer_opacity", "bufferOpacity"),
            "clickable",
            "stream",
            "striped",
            ("rounded_bar", "roundedBar"),
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
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VPullToRefresh.json))
      load (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VPullToRefresh.json))
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
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      disabled (boolean):
        Removes the ability to click or target the component.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      id (string):
        Sets the DOM id on the component.
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string }):
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
            "label",
            ("base_color", "baseColor"),
            "disabled",
            "multiple",
            "value",
            ("value_comparator", "valueComparator"),
            "id",
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
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      height (string, number):
        Sets the height for the component.
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
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      disabled (boolean):
        Removes the ability to click or target the component.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      id (string):
        Sets the DOM id on the component.
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
        Makes prepend/append icons full opacity when the input is focused.
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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      inline (boolean):
        Displays radio buttons in row.
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
            ("model_value", "modelValue"),
            "error",
            "density",
            "height",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "color",
            "name",
            "label",
            ("base_color", "baseColor"),
            "disabled",
            ("value_comparator", "valueComparator"),
            "id",
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
            "ripple",
            "inline",
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
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
      model_value ((string, number)[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      reverse (boolean):
        Reverses the slider direction.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
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
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      name (string):
        Sets the component's name attribute.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      disabled (boolean):
        Removes the ability to click or target the component.
      id (string):
        Sets the DOM id on the component.
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
        Makes prepend/append icons full opacity when the input is focused.
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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
      ripple (boolean):
        Applies the [v-ripple](/directives/ripple) directive.
      max (string, number):
        Sets the maximum allowed value.
      min (string, number):
        Sets the minimum allowed value.
      step (string, number):
        If greater than 0, sets step interval for ticks.
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
      end (event):
        Slider value emitted at the end of slider movement.
      start (event):
        Slider value emitted at start of slider movement.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRangeSlider", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "error",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "rounded",
            "tile",
            "theme",
            "color",
            "name",
            "label",
            ("base_color", "baseColor"),
            "disabled",
            "id",
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
            "ripple",
            "max",
            "min",
            "step",
            ("thumb_color", "thumbColor"),
            ("thumb_label", "thumbLabel"),
            ("thumb_size", "thumbSize"),
            ("show_ticks", "showTicks"),
            "ticks",
            ("tick_size", "tickSize"),
            ("track_color", "trackColor"),
            ("track_fill_color", "trackFillColor"),
            ("track_size", "trackSize"),
            "strict",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            "end",
            "start",
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
      active_color (string):
        The applied color when the component is in an active state.
      disabled (boolean):
        Removes the ability to click or target the component.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      readonly (boolean):
        Removes all hover effects and pointer events.
      clearable (boolean):
        Allows for the component to be cleared by clicking on the current value.
      ripple (boolean):
        Applies the [v-ripple](/directives/ripple) directive.
      hover (boolean):
        Provides visual feedback when hovering over icons.
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
            ("active_color", "activeColor"),
            "disabled",
            "size",
            "readonly",
            "clearable",
            "ripple",
            "hover",
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
      aspect_ratio (string, number):
        Sets a base aspect ratio, calculated as width/height. This will
        only set a **minimum** height, the component can still grow if
        it has a lot of content.
      inline (boolean):
        Display as an inline element instead of a block, also disables flex-grow.
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
            ("aspect_ratio", "aspectRatio"),
            "inline",
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
        super().__init__("VScaleTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
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
        super().__init__("VScrollXTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
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
        super().__init__("VScrollYTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
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
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      chips (boolean):
        Changes display of selections to chips.
      closable_chips (boolean):
        Enables the [closable](/api/v-chip/#props-closable) prop on all
        [v-chip](/components/chips/) components.
      close_text (string):
        Text set to the inputs `aria-label` and `title` when input menu is closed.
      open_text (string):
        Text set to the inputs **aria-label** and **title** when input menu is open.
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
      disabled (boolean):
        Removes the ability to click or target the input.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      items (any[]):
        Can be an array of objects or strings. By default objects should
        have **title** and **value** properties, and can optionally have
        a **props** property containing any [VListItem props](/api/v-list-item/#props).
        Keys to use for these can be changed with the **item-title**,
        **item-value**, and **item-props** props.
      item_title (SelectItemKey<any>):
        Property on supplied `items` that contains its title.
      item_value (SelectItemKey<any>):
        Set property of **items**'s value - **must be primitive**. Dot
        notation is supported. **Note:** This is currently not supported
        with `v-combobox` [GitHub Issue](https://github.com/vuetifyjs/vuetify/issues/5479).
      item_children (SelectItemKey):
        This property currently has **no effect**.
      item_props (SelectItemKey<any>):
        Props object that will be applied to each item component. `true`
        will treat the original object as raw props and pass it directly
        to the component.
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**.
      value_comparator ((a: any, b: any) => boolean):
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
      id (string):
        Sets the DOM id on the component.
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
      autofocus (boolean):
        Enables autofocus.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      prefix (string):
        Displays prefix text.
      placeholder (string):
        Sets the input’s placeholder text.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      role (string):
        The role attribute applied to the input.
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
        Makes prepend/append icons full opacity when the field is focused.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outnside the component's input, uses
        the same syntax as `v-icon`.

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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
            "label",
            "chips",
            ("closable_chips", "closableChips"),
            ("close_text", "closeText"),
            ("open_text", "openText"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            ("list_props", "listProps"),
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "disabled",
            "multiple",
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "id",
            "transition",
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("item_color", "itemColor"),
            "autofocus",
            "counter",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            "role",
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
      model_value (unknown):
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
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      disabled (boolean):
        Removes the ability to click or target the component.
      multiple (boolean):
        Changes select to multiple. Accepts array for value.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      id (string):
        Sets the DOM id on the component.
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string }):
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
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSelectionControl", children, **kwargs)
        self._attr_names += [
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "theme",
            "color",
            "name",
            "label",
            ("base_color", "baseColor"),
            "disabled",
            "multiple",
            "value",
            ("value_comparator", "valueComparator"),
            "id",
            "readonly",
            "ripple",
            "inline",
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
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
      model_value (unknown):
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
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      id (string):
        Sets the DOM id on the component.
      readonly (boolean):
        Puts input in readonly state.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      inline (boolean):
        Puts children inputs into a row.
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
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSelectionControlGroup", children, **kwargs)
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
            ("value_comparator", "valueComparator"),
            "id",
            "readonly",
            "ripple",
            "inline",
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSheet(HtmlElement):
    """
    Vuetify's VSheet component.
    See more `info and examples <https://vuetifyjs.com/api/v-sheet>`_.

    Args:
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
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSheet", children, **kwargs)
        self._attr_names += [
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
          'text', (string & {}), 'image', 'chip', 'subtitle', 'divider',
          'button', 'actions', 'article', 'table', 'avatar', 'heading',
          'sentences', 'paragraph', 'ossein', 'card', 'card-avatar', 'date-picker',
          'date-picker-options', 'date-picker-days', 'list-item', 'list-item-avatar',
          'list-item-two-line', 'list-item-avatar-two-line', 'list-item-three-line',
          'list-item-avatar-three-line', 'table-heading', 'table-thead',
          'table-tbody', 'table-row-divider', 'table-row', 'table-tfoot',
          (, 'text', (string & {}), 'image', 'chip', 'subtitle', 'divider',
          'button', 'actions', 'article', 'table', 'avatar', 'heading',
          'sentences', 'paragraph', 'ossein', 'card', 'card-avatar', 'date-picker',
          'date-picker-options', 'date-picker-days', 'list-item', 'list-item-avatar',
          'list-item-two-line', 'list-item-avatar-two-line', 'list-item-three-line',
          'list-item-avatar-three-line', 'table-heading', 'table-thead',
          'table-tbody', 'table-row-divider', 'table-row', 'table-tfoot'
             )[]
        ]
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
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      loading (boolean):
        Applies a loading animation with a on-hover loading cursor. A
        value of **false** will only work when there is content in the
        `default` slot.
      loading_text (string):
        aria-label for the element in a loading state.
      boilerplate (boolean):
        Remove the loading animation from the skeleton.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSkeletonLoader", children, **kwargs)
        self._attr_names += [
            "type",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "theme",
            "color",
            "loading",
            ("loading_text", "loadingText"),
            "boilerplate",
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
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      disabled (boolean):
        Puts all children components into a disabled state.
      multiple (boolean):
        Allows one to select multiple items.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      direction ('horizontal', 'vertical'):
        Switch between horizontal and vertical modes.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      max (number):
        Sets a maximum number of selections that can be made.
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
      center_active (boolean):
        Forces the selected component to be centered.
      show_arrows (string, boolean):
        Change when the overflow arrow indicators are shown. By **default**,
        arrows *always* display on Desktop when the container is overflowing.
        When the container overflows on mobile, arrows are not shown
        by default. A **show-arrows** value of `true` allows these arrows
        to show on Mobile if the container overflowing. A value of `desktop`
        *always* displays arrows on Desktop while a value of `mobile`
        always displays arrows on Mobile. A value of `always` always
        displays arrows on Desktop *and* Mobile. Find more information
        on how to customize breakpoint thresholds on the [breakpoints
        page](/customizing/breakpoints).
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Sets the designated mobile breakpoint for the component.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideGroup", children, **kwargs)
        self._attr_names += [
            "symbol",
            ("model_value", "modelValue"),
            "tag",
            "disabled",
            "multiple",
            "mandatory",
            "direction",
            ("selected_class", "selectedClass"),
            "max",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("center_active", "centerActive"),
            ("show_arrows", "showArrows"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
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
        super().__init__("VSlideXReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlideXTransition(HtmlElement):
    """
    Vuetify's VSlideXTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-x-transition>`_.

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
        super().__init__("VSlideXTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlideYReverseTransition(HtmlElement):
    """
    Vuetify's VSlideYReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-y-reverse-transition>`_.

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
        super().__init__("VSlideYReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlideYTransition(HtmlElement):
    """
    Vuetify's VSlideYTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-y-transition>`_.

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
        super().__init__("VSlideYTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
            "origin",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlider(HtmlElement):
    """
    Vuetify's VSlider component.
    See more `info and examples <https://vuetifyjs.com/api/v-slider>`_.

    Args:
      model_value (string, number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      error (boolean):
        Puts the input in a manual error state.
      reverse (boolean):
        Reverses the slider direction.
      density ('default', 'comfortable', 'compact'):
        Adjusts the vertical height used by the component.
      max_width (string, number):
        Sets the maximum width for the component.
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
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      name (string):
        Sets the component's name attribute.
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      disabled (boolean):
        Removes the ability to click or target the component.
      id (string):
        Sets the DOM id on the component.
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
        Makes prepend/append icons full opacity when the input is focused.
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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
      ripple (boolean):
        Applies the [v-ripple](/directives/ripple) directive.
      max (string, number):
        Sets the maximum allowed value.
      min (string, number):
        Sets the minimum allowed value.
      step (string, number):
        If greater than 0, sets step interval for ticks.
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
      update_modelValue (event):
        Event that is emitted when the component's model changes.
      click_prepend (event):
        Emitted when prepended icon is clicked.
      click_append (event):
        Emitted when appended icon is clicked.
      update_focused (event):
        Event that is emitted when the component's focus state changes.
      end (event):
        Slider value emitted at the end of slider movement.
      start (event):
        Slider value emitted at start of slider movement.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlider", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "error",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "rounded",
            "tile",
            "theme",
            "color",
            "name",
            "label",
            ("base_color", "baseColor"),
            "disabled",
            "id",
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
            "ripple",
            "max",
            "min",
            "step",
            ("thumb_color", "thumbColor"),
            ("thumb_label", "thumbLabel"),
            ("thumb_size", "thumbSize"),
            ("show_ticks", "showTicks"),
            "ticks",
            ("tick_size", "tickSize"),
            ("track_color", "trackColor"),
            ("track_fill_color", "trackFillColor"),
            ("track_size", "trackSize"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            "end",
            "start",
        ]


class VSnackbar(HtmlElement):
    """
    Vuetify's VSnackbar component.
    See more `info and examples <https://vuetifyjs.com/api/v-snackbar>`_.

    Args:
      text (string):
        Specify content text for the component.
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
      position ('fixed', 'static', 'relative', 'absolute', 'sticky'):
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
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Removes the ability to click or target the component.
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
        Sets the overlay opacity.
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
        A single value that offsets content away from the target based
        upon what side it is on.
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
      vertical (boolean):
        Stacks snackbar content on top of the actions (button).
      multi_line (boolean):
        Gives the snackbar a larger minimum height.
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
            "text",
            ("model_value", "modelValue"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "location",
            "position",
            "absolute",
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            "eager",
            "disabled",
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
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            "transition",
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
      text (string):
        Specify content text for the component.
      closable (string, boolean):
        Adds a dismiss button that closes the active snackbar.
      model_value (Anchor):
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
      position ('fixed', 'static', 'relative', 'absolute', 'sticky'):
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
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      close_text (string):
        The text used in the close button when using the **closable** prop.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Removes the ability to click or target the component.
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
        Sets the overlay opacity.
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
        A single value that offsets content away from the target based
        upon what side it is on.
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
      vertical (boolean):
        Stacks snackbar content on top of the actions (button).
      multi_line (boolean):
        Gives the snackbar a larger minimum height.
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
            "text",
            "closable",
            ("model_value", "modelValue"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "location",
            "position",
            "absolute",
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            ("close_text", "closeText"),
            "eager",
            "disabled",
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
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            "transition",
            "attach",
            "vertical",
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
      model_value ((string, number, { value: number })[]):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      fill (boolean):
        Using the **fill** property allows you to better customize the
        look and feel of your sparkline.
      height (string, number):
        Height of the SVG trendline or bars.
      width (string, number):
        Width of the SVG trendline or bars.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      item_value (string):
        The value of the item.
      id (string):
        The id of the component.
      max (string, number):
        The maximum value of the sparkline.
      min (string, number):
        The minimum value of the sparkline.
      gradient (string[]):
        An array of colors to use as a linear-gradient.
      labels ((string, number, { value: number })[]):
        An array of string labels that correspond to the same index as
        its data counterpart.
      auto_line_width (boolean):
        Automatically expand bars to use space efficiently.
      auto_draw (boolean):
        Trace the length of the line when first rendered.
      auto_draw_duration (string, number):
        Amount of time (in ms) to run the trace animation.
      auto_draw_easing (string):
        The easing function to use for the trace animation.
      gradient_direction ('top', 'bottom', 'left', 'right'):
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
            ("model_value", "modelValue"),
            "fill",
            "height",
            "width",
            "color",
            ("item_value", "itemValue"),
            "id",
            "max",
            "min",
            "gradient",
            "labels",
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
      theme (string):
        Specify a theme for this component and all of its children.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Removes the ability to click or target the component.
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      id (string):
        The unique identifier of the component.
      submenu (boolean):
        Opens with right arrow and closes on left instead of up/down.
        Implies `location="end"`. Directions are reversed for RTL.
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
        Sets the overlay opacity.
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
        Opens speed-dial on hover.
      open_on_focus (boolean):
        Activate the component when the activator is focused.
      close_on_content_click (boolean):
        Closes component when you click on its content.
      close_delay (string, number):
        Milliseconds to wait before closing component. Only works with
        the **open-on-hover** prop.
      open_delay (string, number):
        Milliseconds to wait before opening component. Only works with
        the **open-on-hover** prop.
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        A single value that offsets content away from the target based
        upon what side it is on.
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
      transition (enum):
        Sets the component transition. Can be one of the [built in](/styles/transitions/)
        or custom transition.

        Enum values: [
          string, boolean, (TransitionProps & { component: Component }),
          { component: Component }
        ]
      attach (string, boolean, Element):
        Specifies which DOM element the overlay content should teleport
        to. Can be a direct element reference, querySelector string,
        or `true` to disable teleporting. Uses `body` by default.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSpeedDial", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "location",
            "theme",
            "eager",
            "disabled",
            "activator",
            "id",
            "submenu",
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
            ("scroll_strategy", "scrollStrategy"),
            "transition",
            "attach",
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
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      model_value (any):
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
      disabled (boolean):
        Puts all children components into a disabled state.
      multiple (boolean):
        Allows one to select multiple items.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      items ((string, Record<string, any>)[]):
        An array of strings or objects used for automatically generating
        children components.
      item_title (string):
        Property on supplied `items` that contains its title.
      item_value (string):
        Property on supplied `items` that contains its value.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      max (number):
        Sets a maximum number of selections that can be made.
      mobile (boolean):
        Forces the stepper into a mobile state, removing labels from stepper items.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      hide_actions (boolean):
        Hide actions bar (prev and next buttons).
      alt_labels (boolean):
        Places the labels beneath the step.
      complete_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/Stepper.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      edit_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/Stepper.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      editable (boolean):
        Marks step as editable.
      error_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/Stepper.json))

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
            "border",
            ("model_value", "modelValue"),
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
            "disabled",
            "multiple",
            "mandatory",
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("selected_class", "selectedClass"),
            "max",
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
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
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      disabled (boolean, 'next', 'prev'):
        Removes the ability to click or target the component.
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
            "color",
            "disabled",
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
      title (string):
        Specify a title text for the component.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      error (boolean):
        Puts the stepper item in a manual error state.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      subtitle (string):
        Specify a subtitle text for the component.
      disabled (boolean):
        Removes the ability to click or target the component.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
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
            "title",
            "icon",
            "error",
            "color",
            "subtitle",
            "disabled",
            "value",
            "rules",
            "ripple",
            ("selected_class", "selectedClass"),
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
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      elevation (string, number):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the [elevation page](/styles/elevation).
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes the border-radius.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('default', 'accordion', 'inset', 'popout'):
        Applies a distinct style to the component.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      disabled (boolean):
        Puts all children components into a disabled state.
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
      multiple (boolean):
        Allows one to select multiple items.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      items ((string, Record<string, any>)[]):
        An array of strings or objects used for automatically generating
        children components.
      item_title (string):
        Property on supplied `items` that contains its title.
      item_value (string):
        Property on supplied `items` that contains its value.
      readonly (boolean):
        Makes the entire expansion panel read only.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      max (number):
        Sets a maximum number of selections that can be made.
      mobile (boolean):
        Forces the stepper into a mobile state, removing labels from stepper items.
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Overrides the display configuration default screen size that
        the component should be considered in mobile.
      hide_actions (boolean):
        Hide the expand icon in the content title.
      focusable (boolean):
        Makes the expansion-panel headers focusable.
      alt_labels (boolean):
        Places the labels beneath the step.
      complete_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/Stepper.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      edit_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/Stepper.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      editable (boolean):
        Marks step as editable.
      error_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/Stepper.json))

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
            ("model_value", "modelValue"),
            "elevation",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            "eager",
            ("bg_color", "bgColor"),
            "disabled",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "multiple",
            "mandatory",
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            "readonly",
            "ripple",
            ("selected_class", "selectedClass"),
            "max",
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
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
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      disabled (boolean, 'next', 'prev'):
        Removes the ability to click or target the component.
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
            "color",
            "disabled",
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
      title (string):
        Specify a title text for the component.
      text (string):
        Specify content text for the component.
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/) component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      error (boolean):
        Puts the stepper item in a manual error state.
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
      static (boolean):
        Remove title size expansion when selected.
      rounded (string, number, boolean):
        Designates the **border-radius** applied to the component. This
        can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**,
        **circle**, and **shaped**. Find more information on available
        border radius classes on the [Border Radius page](/styles/border-radius).
      tile (boolean):
        Removes any applied **border-radius** from the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      subtitle (string):
        Specify a subtitle text for the component.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      disabled (boolean):
        Disables the expansion-panel content.
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
      value (any):
        Controls the opened/closed state of content.
      readonly (boolean):
        Makes the expansion panel content read only.
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
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
            "title",
            "text",
            "icon",
            "error",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "static",
            "rounded",
            "tile",
            "tag",
            "color",
            "eager",
            "subtitle",
            ("bg_color", "bgColor"),
            "disabled",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "value",
            "readonly",
            "rules",
            "ripple",
            ("selected_class", "selectedClass"),
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
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      reverse (boolean):
        Reverse the normal transition direction.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      disabled (boolean):
        Removes the ability to click or target the component.
      direction ('horizontal', 'vertical'):
        The transition direction when changing windows.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperWindow", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "reverse",
            "tag",
            "theme",
            "disabled",
            "direction",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VStepperWindowItem(HtmlElement):
    """
    Vuetify's VStepperWindowItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-window-item>`_.

    Args:
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Prevents the item from becoming active when using the "next"
        and "prev" buttons or the `toggle` method.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      transition (string, boolean):
        The transition used when the component progressing through items.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      reverse_transition (string, boolean):
        Sets the reverse transition.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperWindowItem", children, **kwargs)
        self._attr_names += [
            "eager",
            "disabled",
            "value",
            "transition",
            ("selected_class", "selectedClass"),
            ("reverse_transition", "reverseTransition"),
        ]
        self._event_names += []


class VSvgIcon(HtmlElement):
    """
    Vuetify's VSvgIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-svg-icon>`_.

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
        super().__init__("VSvgIcon", children, **kwargs)
        self._attr_names += [
            "icon",
            "tag",
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
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      base_color (string):
        Sets the color of the input when it is not focused.
      disabled (boolean):
        Removes the ability to click or target the component.
      multiple (boolean):
        Changes expected model to an array.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      id (string):
        Sets the DOM id on the component.
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
        Makes prepend/append icons full opacity when the input is focused.
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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
      loading (string, boolean):
        Displays circular progress bar. Can either be a String which
        specifies which color is applied to the progress bar (any material
        color or theme color - primary, secondary, success, info, warning,
        error) or a Boolean which uses the component color (set by color
        prop - if it's supported by the component) or the primary color.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      inline (boolean):
        Puts children inputs into a row.
      indeterminate (boolean):
        Sets an indeterminate state for the switch.
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
      inset (boolean):
        Enlarge the `v-switch` track to encompass the thumb.
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
            ("model_value", "modelValue"),
            "error",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "color",
            "name",
            "label",
            ("base_color", "baseColor"),
            "disabled",
            "multiple",
            "value",
            ("value_comparator", "valueComparator"),
            "id",
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
            "loading",
            "ripple",
            "inline",
            "indeterminate",
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "inset",
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
      height (string, number):
        Sets the height for the component.
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
      order (string, number):
        Adjust the order of the component in relation to its registration order.
      window (boolean):
        Increases the system bar height to 32px (24px default).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSystemBar", children, **kwargs)
        self._attr_names += [
            "height",
            "elevation",
            "absolute",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "name",
            "order",
            "window",
        ]
        self._event_names += []


class VTab(HtmlElement):
    """
    Vuetify's VTab component.
    See more `info and examples <https://vuetifyjs.com/api/v-tab>`_.

    Args:
      text (string, number, boolean):
        Specify content text for the component.
      replace (boolean):
        Setting **replace** prop will call `router.replace()` instead
        of `router.push()` when clicked, so the navigation will not leave
        a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace)
        prop on the vue-router documentation.
      fixed (boolean):
        Forces component to take up all available space up to their maximum
        width (300px), and centers it.
      border (string, number, boolean):
        Applies utility border classes to the component. To use it, you
        need to omit the `border-` prefix, (for example use `border-sm`
        as `border="sm"`).  Find a list of the built-in border classes
        on the [borders page](/styles/borders).
      icon (enum):
        Apply a specific icon using the [v-icon](/components/icons/)
        component. The button will become _round_.

        Enum values: [
          boolean, string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
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
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
        Applies a distinct style to the component.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact)
        on the vue-router documentation.
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        The applied color when the component is in an active state.
      disabled (boolean):
        Removes the ability to click or target the component.
      slim (boolean):
        Reduces padding to 0 8px.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
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
      direction ('horizontal', 'vertical'):
        Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
      readonly (boolean):
        Puts the button in a readonly state. Cannot be clicked or navigated
        to by keyboard.
      loading (string, boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color.
      href (string):
        Designates the component as anchor and applies the **href** attribute.
      to (enum):
        Denotes the target route of the link. You can find more information
        about the [**to** prop](https://router.vuejs.org/api/#to) on
        the vue-router documentation.

        Enum values: [
          string, RouteLocationAsRelativeGeneric, RouteLocationAsPathGeneric
        ]
      stacked (boolean):
        Displays the tab as a flex-column.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      slider_color (string):
        Applies specified color to the slider when active on that component
        - supports utility colors (for example `success` or `purple`)
        or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list
        of built-in classes on the [colors page](/styles/colors#material-colors).
      hide_slider (boolean):
        Hides the active tab slider component (no exit or enter animation).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTab", children, **kwargs)
        self._attr_names += [
            "text",
            "replace",
            "fixed",
            "border",
            "icon",
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
            "exact",
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            "disabled",
            "slim",
            "value",
            "size",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "direction",
            "readonly",
            "loading",
            "href",
            "to",
            "stacked",
            "ripple",
            ("selected_class", "selectedClass"),
            ("slider_color", "sliderColor"),
            ("hide_slider", "hideSlider"),
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
      hover (boolean):
        Will add a hover effect to a table's row when the mouse is over it.
      fixed_header (boolean):
        Use the fixed-header prop together with the height prop to fix
        the header to the top of the table.
      fixed_footer (boolean):
        Use the fixed-footer prop together with the height prop to fix
        the footer to the bottom of the table.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTable", children, **kwargs)
        self._attr_names += [
            "density",
            "height",
            "tag",
            "theme",
            "hover",
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
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
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      disabled (boolean):
        Puts all children components into a disabled state.
      multiple (boolean):
        Allows one to select multiple items.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
      items (unknown[]):
        The items to display in the component. This can be an array of
        strings or objects with a property `text`.
      direction ('horizontal', 'vertical'):
        Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
      stacked (boolean):
        Apply the stacked prop to all children v-tab components.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      max (number):
        Sets a maximum number of selections that can be made.
      next_icon (enum):
        Right pagination icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      prev_icon (enum):
        Left pagination icon.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      center_active (boolean):
        Forces the selected tab to be centered.
      show_arrows (string, boolean):
        Show pagination arrows if the tab items overflow their container.
        For mobile devices, arrows will only display when using this
        prop.
      mobile (boolean):
        Determines the display mode of the component. If true, the component
        will be displayed in mobile mode. If false, the component will
        be displayed in desktop mode. If null, will be based on the current
        mobile-breakpoint
      mobile_breakpoint (number, 'xs', 'sm', 'md', 'lg', 'xl', 'xxl'):
        Sets the designated mobile breakpoint for the component.
      slider_color (string):
        Changes the background color of an auto-generated `v-tabs-slider`.
      hide_slider (boolean):
        Hide's the generated `v-tabs-slider`.
      align_tabs ('title', 'end', 'start', 'center'):
        Aligns the tabs to the `start`, `center`, or `end` of container.
        Also accepts `title` to align with the `v-toolbar-title` component.
      fixed_tabs (boolean):
        `v-tabs-item` min-width 160px, max-width 360px.
      grow (boolean):
        Force `v-tab`'s to take up all available space.
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
            ("bg_color", "bgColor"),
            "disabled",
            "multiple",
            "mandatory",
            "items",
            "direction",
            "stacked",
            ("selected_class", "selectedClass"),
            "max",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("center_active", "centerActive"),
            ("show_arrows", "showArrows"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("slider_color", "sliderColor"),
            ("hide_slider", "hideSlider"),
            ("align_tabs", "alignTabs"),
            ("fixed_tabs", "fixedTabs"),
            "grow",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTabsWindow(HtmlElement):
    """
    Vuetify's VTabsWindow component.
    See more `info and examples <https://vuetifyjs.com/api/v-tabs-window>`_.

    Args:
      model_value (any):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      reverse (boolean):
        Reverse the normal transition direction.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      theme (string):
        Specify a theme for this component and all of its children.
      disabled (boolean):
        Removes the ability to click or target the component.
      direction ('horizontal', 'vertical'):
        The transition direction when changing windows.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTabsWindow", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "reverse",
            "tag",
            "theme",
            "disabled",
            "direction",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTabsWindowItem(HtmlElement):
    """
    Vuetify's VTabsWindowItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-tabs-window-item>`_.

    Args:
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Prevents the item from becoming active when using the "next"
        and "prev" buttons or the `toggle` method.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      transition (string, boolean):
        The transition used when the component progressing through items.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      reverse_transition (string, boolean):
        Sets the reverse transition.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTabsWindowItem", children, **kwargs)
        self._attr_names += [
            "eager",
            "disabled",
            "value",
            "transition",
            ("selected_class", "selectedClass"),
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
      disabled (boolean):
        Removes the ability to click or target the input.
      id (string):
        Sets the DOM id on the component.
      autofocus (boolean):
        Enables autofocus.
      counter (string, number, boolean):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      prefix (string):
        Displays prefix text.
      placeholder (string):
        Sets the input’s placeholder text.
      persistent_placeholder (boolean):
        Forces placeholder to always be visible.
      persistent_counter (boolean):
        Forces counter to always be visible.
      suffix (string):
        Displays suffix text.
      role (string):
        The role attribute applied to the input.
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
        Makes prepend/append icons full opacity when the field is focused.
      icon_color (string, boolean):
        Sets the color of the prepend/append icons.
      prepend_icon (enum):
        Prepends an icon to the outnside the component's input, uses
        the same syntax as `v-icon`.

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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
            "label",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "disabled",
            "id",
            "autofocus",
            "counter",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            "role",
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
        Applies a distinct style to the component.

        Enum values: [
          'outlined', 'plain', 'underlined', 'filled', 'solo', 'solo-inverted',
          'solo-filled'
        ]
      name (string):
        Sets the component's name attribute.
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
      disabled (boolean):
        Removes the ability to click or target the input.
      id (string):
        Sets the DOM id on the component.
      autofocus (boolean):
        The element should be focused as soon as the page loads.
      counter (string, number, true):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      prefix (string):
        Displays prefix text.
      placeholder (string):
        Sets the input's placeholder text.
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
        Makes prepend/append icons full opacity when the field is focused.
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
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTextarea", children, **kwargs)
        self._attr_names += [
            "flat",
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
            "label",
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "disabled",
            "id",
            "autofocus",
            "counter",
            "prefix",
            "placeholder",
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
        Use the current value of `$vuetify.theme.dark` as opposed to the provided one.
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
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      disabled (boolean):
        Removes the ability to click or target the component.
      readonly (boolean):
        Puts picker in readonly state.
      hide_header (boolean):
        Hide the picker header.
      max (string):
        Maximum allowed time.
      min (string):
        Minimum allowed time.
      view_mode ('hour', 'minute', 'second'):
        The current view mode of thep picker.`
      divided (boolean):
        Adds a divider between the header and controls.
      scrollable (boolean):
        Allows changing hour/minute with mouse scroll.
      ampm_in_title (boolean):
        Place AM/PM switch in title, not near the clock.
      format ('ampm', '24hr'):
        Defines the format of a time displayed in picker. Available options
        are `ampm` and `24hr`.
      use_seconds (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePicker.json))
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
            "disabled",
            "readonly",
            ("hide_header", "hideHeader"),
            "max",
            "min",
            ("view_mode", "viewMode"),
            "divided",
            "scrollable",
            ("ampm_in_title", "ampmInTitle"),
            "format",
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
      model_value (number):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      disabled (boolean):
        Removes the ability to click or target the component.
      readonly (boolean):
        When true, the picker is in a read-only state, and users cannot
        modify the selected time.
      max (number):
        Defines the maximum time value that can be selected.
      min (number):
        Defines the minimum time value that can be selected.
      scrollable (boolean):
        Allows the time selection to be scrollable, enhancing user experience
        for devices with scroll inputs.
      step (number):
        Defines the increments between selectable times, such as a step
        of 1 for every minute or a larger step for every 5 or 15 minutes.
      rotate (number):
        Controls rotation, specifying the degree of rotation for the clock hands.
      format (Function):
        Specifies the format of the displayed time, either 12-hour or
        24-hour, depending on the component's setup.
      ampm (boolean):
        Displays time in a 12-hour format.
      displayed_value (any):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerClock.json))
      double (boolean):
        If set, this probably indicates a double rotation or a mode where
        more than one set of values (like hours and minutes) is displayed
        on the clock at the same time.
      allowed_values ((value: number) => boolean):
        Restricts which hours can be selected.
      input (event):
        The updated bound model.
      change (event):
        The event that is triggered when the selected time is changed.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimePickerClock", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "color",
            "disabled",
            "readonly",
            "max",
            "min",
            "scrollable",
            "step",
            "rotate",
            "format",
            "ampm",
            ("displayed_value", "displayedValue"),
            "double",
            ("allowed_values", "allowedValues"),
        ]
        self._event_names += [
            "input",
            "change",
        ]


class VTimePickerControls(HtmlElement):
    """
    Vuetify's VTimePickerControls component.
    See more `info and examples <https://vuetifyjs.com/api/v-time-picker-controls>`_.

    Args:
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      disabled (boolean):
        Removes the ability to click or target the component.
      value (number):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      readonly (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      view_mode ('hour', 'minute', 'second'):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      ampm_in_title (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      ampm (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      hour (number):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      minute (number):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      second (number):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      use_seconds (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      ampm_readonly (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      period (string):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      update_period (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
      update_viewMode (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimePickerControls", children, **kwargs)
        self._attr_names += [
            "color",
            "disabled",
            "value",
            "readonly",
            ("view_mode", "viewMode"),
            ("ampm_in_title", "ampmInTitle"),
            "ampm",
            "hour",
            "minute",
            "second",
            ("use_seconds", "useSeconds"),
            ("ampm_readonly", "ampmReadonly"),
            "period",
        ]
        self._event_names += [
            ("update_period", "update:period"),
            ("update_viewMode", "update:viewMode"),
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
      size (string, number):
        Sets the height and width of the component. Default unit is px.
        Can also use the following predefined sizes: **x-small**, **small**,
        **default**, **large**, and **x-large**.
      icon_color (string):
        Color of the icon.
      direction ('horizontal', 'vertical'):
        Display timeline in a **vertical** or **horizontal** direction.
      align ('start', 'center'):
        Places the timeline dot at the top or center of the timeline item.
      side ('end', 'start'):
        Display all timeline items on one side of the timeline, either
        **start** or **end**.
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
            "size",
            ("icon_color", "iconColor"),
            "direction",
            "align",
            "side",
            "justify",
            ("line_thickness", "lineThickness"),
            ("line_color", "lineColor"),
            ("dot_color", "dotColor"),
            ("fill_dot", "fillDot"),
            ("hide_opposite", "hideOpposite"),
            ("line_inset", "lineInset"),
            ("truncate_line", "truncateLine"),
        ]
        self._event_names += []


class VTimelineItem(HtmlElement):
    """
    Vuetify's VTimelineItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-timeline-item>`_.

    Args:
      icon (enum):
        Apply a specific icon to the inside dot using the [v-icon](/components/icons/)
        component.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      density ('default', 'compact'):
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
      size (string, number):
        Size of the item dot
      icon_color (string):
        Color of the icon.
      side ('end', 'start'):
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
            "icon",
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
            "size",
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
      extended (boolean):
        Use this prop to increase the height of the toolbar _without_
        using the `extension` slot for adding content. May be used in
        conjunction with the **extension-height** prop, and any of the
        other props that affect the height of the toolbar, e.g. **prominent**,
        **dense**, etc., **WITH THE EXCEPTION** of **height**.
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
      variant ('text', 'flat', 'elevated', 'tonal', 'outlined', 'plain'):
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
      text (string):
        Specify content text for the component.
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
      theme (string):
        Specify a theme for this component and all of its children.
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Removes the ability to click or target the component.
      activator (Element, (string & {}), 'parent', ComponentPublicInstance):
        Explicitly sets the overlay's activator.
      id (string):
        HTML id attribute of the tooltip overlay. If not set, a globally
        unique id will be used.
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
        Sets the overlay opacity.
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
      location_strategy (LocationStrategyFunction):
        A function used to specifies how the component should position
        relative to its activator.
      origin (Anchor):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
      offset (string, number, number[]):
        A single value that offsets content away from the target based
        upon what side it is on.
      scroll_strategy (ScrollStrategyFunction):
        Strategy used when the component is activate and user scrolls.
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
      interactive (boolean):
        When true, the tooltip will respond to pointer events, allowing
        you to copy text from it.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTooltip", children, **kwargs)
        self._attr_names += [
            "text",
            ("model_value", "modelValue"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "location",
            "theme",
            "eager",
            "disabled",
            "activator",
            "id",
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
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            ("scroll_strategy", "scrollStrategy"),
            "transition",
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
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        The applied color when the component is in an active state.
      active_class (string):
        The class applied to the component when it is in an active state.
      bg_color (string):
        Applies specified color to the control's background. Used on
        components that also support the **color** prop. - supports utility
        colors (for example `success` or `purple`) or css color (`#033`
        or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on
        the [colors page](/styles/colors#material-colors).
      disabled (boolean):
        Disables selection for all nodes.
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
      active_strategy (ActiveStrategy):
        Affects how items with children behave when activated. - **leaf:**
        Only leaf nodes (items without children) can be activated. -
        **independent:** All nodes can be activated whether they have
        children or not. - **classic:** Activating a parent node will
        cause all children to be activated.
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
      return_object (boolean):
        When `true` will make `v-model`, `active.sync` and `open.sync`
        return the complete object instead of just the key.
      value_comparator ((a: any, b: any) => boolean):
        Apply a custom comparison algorithm to compare **model-value**
        and values contains in the **items** prop.
      open_on_click (boolean):
        When `true` will cause nodes to be opened by clicking anywhere
        on it, instead of only opening by clicking on expand icon. When
        using this prop with `activatable` you will be unable to mark
        nodes with children as active.
      indeterminate_icon (enum):
        Icon used when node is in an indeterminate state. Only visible
        when `selectable` is `true`.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      false_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTreeviewChildren.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      true_icon (enum):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTreeviewChildren.json))

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      fluid (boolean):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTreeview.json))
      open_all (boolean):
        When `true` will cause all branch nodes to be opened when component is mounted.
      loading_icon (string):
        Icon used when node is in a loading state.
      selected_color (string):
        The color of the selection checkbox.
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
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            ("active_class", "activeClass"),
            ("bg_color", "bgColor"),
            "disabled",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "lines",
            "slim",
            "activatable",
            "selectable",
            "opened",
            "selected",
            "mandatory",
            ("active_strategy", "activeStrategy"),
            ("select_strategy", "selectStrategy"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            ("open_on_click", "openOnClick"),
            ("indeterminate_icon", "indeterminateIcon"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "fluid",
            ("open_all", "openAll"),
            ("loading_icon", "loadingIcon"),
            ("selected_color", "selectedColor"),
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
      title (string):
        Specify a title text for the component.
      tag (string, js_fn, FunctionalComponent):
        Specify a custom tag used on the root element.
      color (string):
        Applies specified color to the control - supports utility colors
        (for example `success` or `purple`) or css color (`#033` or `rgba(255,
        0, 0, 0.5)`). Find a list of built-in classes on the [colors
        page](/styles/colors#material-colors).
      base_color (string):
        Sets the color of component when not focused.
      active_color (string):
        The applied color when the component is in an active state.
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
      value (any):
        Expands / Collapse the list-group.
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
        Removes viewport maximum-width size breakpoints.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTreeviewGroup", children, **kwargs)
        self._attr_names += [
            "title",
            "tag",
            "color",
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "value",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
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
      theme (string):
        Specify a theme for this component and all of its children.
      value (any):
        The value used for selection. Obtained from [`v-list`](/api/v-list)'s
        `v-model:selected` when the item is selected.
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
      slim (boolean):
        Reduces the vertical padding or height of the v-treeview-item,
        making it more compact.
      ripple (boolean, { class: string }):
        Applies the [v-ripple](/directives/ripple) directive.
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
      disabled (boolean):
        Removes the ability to click or target the component.
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
      toggle_icon (enum):
        Allows customization of the icon used to toggle the expansion
        and collapse of treeview branches.

        Enum values: [
          string, (string, [string, number])[], js_fn, FunctionalComponent
        ]
      toggleExpand (event):
        MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTreeviewItem.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTreeviewItem", children, **kwargs)
        self._attr_names += [
            "replace",
            "link",
            "tag",
            "nav",
            "title",
            "theme",
            "value",
            "active",
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "slim",
            "ripple",
            "border",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "disabled",
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
            ("toggle_icon", "toggleIcon"),
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
      label (string):
        Sets the text of the [v-label](/api/v-label/) or [v-field-label](/api/v-field-label/)
        component.
      disabled (boolean):
        Removes the ability to click or target the component.
      error_messages (string, string[]):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation.
      max_errors (string, number):
        Control the maximum number of shown errors from validation.
      readonly (boolean):
        Puts input in readonly state.
      rules (ValidationRule):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`.
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
            "label",
            "disabled",
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
      theme (string):
        Specify a theme for this component and all of its children.
      disabled (boolean):
        Removes the ability to click or target the component.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      model_value (unknown):
        The v-model value of the component. If component supports the
        **multiple** prop, this defaults to an empty array.
      mandatory (boolean, 'force'):
        Forces at least one item to always be selected (if available).
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
      continuous (boolean):
        If `true`, window will "wrap around" from the last item to the
        first, and from the first item to the last.
      show_arrows (string, boolean):
        Display the "next" and "prev" buttons.
      touch (TouchHandlers):
        Provide a custom **left** and **right** function when swiped left or right.
      direction ('horizontal', 'vertical'):
        The transition direction when changing windows.
      update_modelValue (event):
        Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VWindow", children, **kwargs)
        self._attr_names += [
            "tag",
            "reverse",
            "theme",
            "disabled",
            ("selected_class", "selectedClass"),
            ("model_value", "modelValue"),
            "mandatory",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            "continuous",
            ("show_arrows", "showArrows"),
            "touch",
            "direction",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VWindowItem(HtmlElement):
    """
    Vuetify's VWindowItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-window-item>`_.

    Args:
      eager (boolean):
        Forces the component's content to render when it mounts. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      disabled (boolean):
        Prevents the item from becoming active when using the "next"
        and "prev" buttons or the `toggle` method.
      value (any):
        The value used when the component is selected in a group. If
        not provided, a unique ID will be used.
      transition (string, boolean):
        The transition used when the component progressing through items.
        Can be one of the [built in](/styles/transitions/) or custom
        transition.
      selected_class (string):
        Configure the active CSS class applied when an item is selected.
      reverse_transition (string, boolean):
        Sets the reverse transition.
      group_selected (event):
        Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VWindowItem", children, **kwargs)
        self._attr_names += [
            "eager",
            "disabled",
            "value",
            "transition",
            ("selected_class", "selectedClass"),
            ("reverse_transition", "reverseTransition"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]
