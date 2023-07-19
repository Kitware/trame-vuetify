##########################################################
# DO NOT EDIT: GENERATED FILE
# => instead run: $ROOT/vue-components/generate_python.py
##########################################################

from trame_client.widgets.core import AbstractElement, Template  # noqa
from trame_vuetify.module import vue3


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
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

    :param dataframe: A pandas dataframe
    :param options: Control which columns are sortable, filterable, grouped, aligned, etc. A dictionary where keys are the columns from the dataframe and values are Vuetify DataTableHeader objects. See more info |header_doc_link|.

    .. |header_doc_link| raw:: html

        <a href="https://vuetifyjs.com/en/api/v-data-table/#props-headers" target="_blank">here</a>

    >>> headers, rows = vuetify.dataframe_to_grid(dataframe)
    >>> VDataTable(
    ...     headers=("table_headers", headers),
    ...     items=("table_rows", rows))
    """
    headers = {}
    for col_name in dataframe.columns:
        headers[col_name] = {"text": col_name, "value": col_name}
        if options.get(col_name):
            headers[col_name].update(options.get(col_name))

    return list(headers.values()), dataframe.applymap(cast_to_serializable).to_dict(
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
    "bottom",
    "chip",
    "clear",
    "close",
    "colgroup",
    "column.data-table-expand",
    "column.data-table-select",
    "counter",
    "data-table-group",
    "data-table-select",
    "default",
    "details",
    "divider",
    "empty",
    "error",
    "expanded-row",
    "extension",
    "filter",
    "first",
    "footer",
    "footer.prepend",
    "group-header",
    "header",
    "headers",
    "icon",
    "image",
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
    "message",
    "next",
    "no-data",
    "opposite",
    "placeholder",
    "prepend",
    "prepend-inner",
    "prepend-item",
    "prev",
    "selection",
    "sources",
    "subheader",
    "subtitle",
    "tbody",
    "text",
    "tfoot",
    "thead",
    "thumb-label",
    "tick-label",
    "title",
    "top",
    "wrapper",
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
    "VContainer",
    "VCounter",
    "VDataIterator",
    "VDataTable",
    "VDataTableFooter",
    "VDataTableRow",
    "VDataTableRows",
    "VDataTableServer",
    "VDataTableVirtual",
    "VDateCard",
    "VDatePicker",
    "VDatePickerControls",
    "VDatePickerHeader",
    "VDatePickerMonth",
    "VDatePickerYears",
    "VDefaultsProvider",
    "VDialog",
    "VDialogBottomTransition",
    "VDialogTopTransition",
    "VDialogTransition",
    "VDivider",
    "VExpandTransition",
    "VExpandXTransition",
    "VExpansionPanel",
    "VExpansionPanelText",
    "VExpansionPanelTitle",
    "VExpansionPanels",
    "VFabTransition",
    "VFadeTransition",
    "VField",
    "VFieldLabel",
    "VFileInput",
    "VFooter",
    "VForm",
    "VHover",
    "VIcon",
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
    "VOverlay",
    "VPagination",
    "VParallax",
    "VPicker",
    "VPickerTitle",
    "VProgressCircular",
    "VProgressLinear",
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
    "VSpacer",
    "VSvgIcon",
    "VSwitch",
    "VSystemBar",
    "VTab",
    "VTable",
    "VTabs",
    "VTextField",
    "VTextarea",
    "VThemeProvider",
    "VTimeline",
    "VTimelineItem",
    "VToolbar",
    "VToolbarItems",
    "VToolbarTitle",
    "VTooltip",
    "VValidation",
    "VVirtualScroll",
    "VWindow",
    "VWindowItem",
    "dataframe_to_grid",
]


class VAlert(HtmlElement):
    """
      Vuetify's VAlert component. See more info and examples |VAlert_vuetify_link|.

      .. |VAlert_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-alert" target="_blank">here</a>


      :param title: Specify a title text for the component.
      :type string:
      :param text: Specify content text for the component.
      :type string:
      :param border: Adds a colored border to the component.
      :type boolean | 'top' | 'end' | 'bottom' | 'start':
      :param type: Create a specialized alert that uses a contextual color and has a pre-defined icon.
      :type 'success' | 'info' | 'warning' | 'error':
      :param border_color: Specifies the color of the border. Accepts any color value.
      :type string:
      :param closable: Adds a close icon that can hide the alert.
      :type boolean:
      :param close_icon: Change the default icon used for **closable** alerts.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param close_label: See description |VAlert_vuetify_link|.
      :type string:
      :param icon: See description |VAlert_vuetify_link|.
      :type | false
    | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type boolean:
      :param prominent: Displays a larger vertically centered icon to draw more attention.
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param elevation: See description |VAlert_vuetify_link|.
      :type string | number:
      :param location: Specifies the component's location. Can combine by using a space separated string
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param position: MISSING DESCRIPTION
      :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
      :param rounded: See description |VAlert_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VAlert_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':

      Events

      :param click_close: Emitted when close icon is clicked
      :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAlert", children, **kwargs)
        self._attr_names += [
            "title",
            "text",
            "border",
            "type",
            ("border_color", "borderColor"),
            "closable",
            ("close_icon", "closeIcon"),
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
    Vuetify's VAlertTitle component. See more info and examples |VAlertTitle_vuetify_link|.

    .. |VAlertTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-alert-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAlertTitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VApp(HtmlElement):
    """
    Vuetify's VApp component. See more info and examples |VApp_vuetify_link|.

    .. |VApp_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-app" target="_blank">here</a>


    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param full_height: Sets the component height to 100%
    :type boolean:
    :param overlaps: See description |VApp_vuetify_link|.
    :type string[]:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VApp", children, **kwargs)
        self._attr_names += [
            "theme",
            ("full_height", "fullHeight"),
            "overlaps",
        ]
        self._event_names += []


class VAppBar(HtmlElement):
    """
    Vuetify's VAppBar component. See more info and examples |VAppBar_vuetify_link|.

    .. |VAppBar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-app-bar" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string:
    :param flat: Removes the component's **box-shadow**.
    :type boolean:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'prominent' | 'comfortable' | 'compact':
    :param height: Designates a specific height for the toolbar. Overrides the heights imposed by other props, e.g. **prominent**, **dense**, **extended**, etc.
    :type string | number:
    :param elevation: See description |VAppBar_vuetify_link|.
    :type string | number:
    :param location: Aligns the component towards the top or bottom.
    :type 'top' | 'bottom':
    :param absolute: Applies position: absolute to the component.
    :type boolean:
    :param rounded: See description |VAppBar_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VAppBar_vuetify_link|.
    :type string:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param image: See description |VAppBar_vuetify_link|.
    :type string:
    :param scroll_behavior: Specify an action to take when the scroll position of **scroll-target** reaches **scroll-threshold**. Accepts any combination of hide, inverted, collapse, elevate, and fade-image. Multiple values can be used, separated by a space.
    :type string:
    :param collapse: Morphs the component into a collapsed state, reducing its maximum width.
    :type boolean:
    :param extended: Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop, and any of the other props that affect the height of the toolbar, e.g. **prominent**, **dense**, etc., **WITH THE EXCEPTION** of **height**.
    :type boolean:
    :param extension_height: Designate an explicit height for the `extension` slot.
    :type string | number:
    :param floating: Applies **display: inline-flex** to the component.
    :type boolean:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param scroll_target: The element to target for scrolling events. Uses `window` by default.
    :type string:
    :param scroll_threshold: The amount of scroll distance down before **scroll-behavior** activates.
    :type string | number:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
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
            "tag",
            "theme",
            "color",
            "name",
            "image",
            ("scroll_behavior", "scrollBehavior"),
            "collapse",
            "extended",
            ("extension_height", "extensionHeight"),
            "floating",
            "order",
            ("scroll_target", "scrollTarget"),
            ("scroll_threshold", "scrollThreshold"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VAppBarNavIcon(HtmlElement):
    """
      Vuetify's VAppBarNavIcon component. See more info and examples |VAppBarNavIcon_vuetify_link|.

      .. |VAppBarNavIcon_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-app-bar-nav-icon" target="_blank">here</a>


      :param symbol: See description |VAppBarNavIcon_vuetify_link|.
      :type any:
      :param text: Specify content text for the component.
      :type string:
      :param flat: Removes the button box shadow.
      :type boolean:
      :param border: Applies border styles to component.
      :type string | number | boolean:
      :param icon: See description |VAppBarNavIcon_vuetify_link|.
      :type | boolean
    | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param elevation: See description |VAppBarNavIcon_vuetify_link|.
      :type string | number:
      :param location: Specifies the component's location. Can combine by using a space separated string
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param position: MISSING DESCRIPTION
      :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
      :param rounded: See description |VAppBarNavIcon_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VAppBarNavIcon_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
      :type string | number:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component
      :type boolean:
      :param prepend_icon: See description |VAppBarNavIcon_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VAppBarNavIcon_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param block: Expands the button to 100% of available space.
      :type boolean:
      :param stacked: Displays the button as a flex-column.
      :type boolean:
      :param ripple: See description |VAppBarNavIcon_vuetify_link|.
      :type boolean | { class: string }:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param href: Designates the component as anchor and applies the **href** attribute.
      :type string:
      :param replace: See description |VAppBarNavIcon_vuetify_link|.
      :type boolean:
      :param exact: See description |VAppBarNavIcon_vuetify_link|.
      :type boolean:
      :param to: See description |VAppBarNavIcon_vuetify_link|.
      :type unknown:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAppBarNavIcon", children, **kwargs)
        self._attr_names += [
            "symbol",
            "text",
            "flat",
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
            "tag",
            "theme",
            "color",
            "variant",
            "value",
            "size",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "block",
            "stacked",
            "ripple",
            "disabled",
            ("selected_class", "selectedClass"),
            "loading",
            "href",
            "replace",
            "exact",
            "to",
        ]
        self._event_names += []


class VAppBarTitle(HtmlElement):
    """
    Vuetify's VAppBarTitle component. See more info and examples |VAppBarTitle_vuetify_link|.

    .. |VAppBarTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-app-bar-title" target="_blank">here</a>


    :param text: Specify content text for the component.
    :type string:
    :param tag: Specify a custom tag used on the root element.
    :type string:

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
        Vuetify's VAutocomplete component. See more info and examples |VAutocomplete_vuetify_link|.

        .. |VAutocomplete_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-autocomplete" target="_blank">here</a>


        :param flat: Removes elevation (shadow) added to element when using the **solo** or **solo-inverted** props
        :type boolean:
        :param type: Sets input type
        :type string:
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
        :type any:
        :param error: Puts the input in a manual error state
        :type boolean:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param reverse: Reverses the orientation
        :type boolean:
        :param rounded: Adds a border radius to the input
        :type string | number | boolean:
        :param theme: Specify a theme for this component and all of its children
        :type string:
        :param color: See description |VAutocomplete_vuetify_link|.
        :type string:
        :param variant: Applies a distinct style to the component
        :type | 'outlined'
      | 'plain'
      | 'underlined'
      | 'filled'
      | 'solo'
      | 'solo-inverted'
      | 'solo-filled':
        :param name: Sets the component's name attribute.
        :type string:
        :param id: Sets the DOM id on the component
        :type string:
        :param items: An array of strings or objects used for automatically generating children components
        :type any[]:
        :param active: Controls the **active** state of the item. This is typically used to highlight the component
        :type boolean:
        :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param append_icon: See description |VAutocomplete_vuetify_link|.
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param disabled: Removes the ability to click or target the input
        :type boolean:
        :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
        :type string | boolean:
        :param label: See description |VAutocomplete_vuetify_link|.
        :type string:
        :param auto_select_first: When searching, will always highlight the first option and select it on blur. `exact` will only highlight and select exact matches.
        :type boolean | 'exact':
        :param search: Text input used to filter items.
        :type string:
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'every' | 'some' | 'union' | 'intersection':
        :param no_filter: Do not apply filtering when searching. Useful when data is being filtered server side
        :type boolean:
        :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type { [string]: <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a> }:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param chips: See description |VAutocomplete_vuetify_link|.
        :type boolean:
        :param closable_chips: See description |VAutocomplete_vuetify_link|.
        :type boolean:
        :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
        :type boolean:
        :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
        :type boolean:
        :param hide_selected: See description |VAutocomplete_vuetify_link|.
        :type boolean:
        :param menu: Renders with the menu open by default
        :type boolean:
        :param menu_icon: Sets the the spin icon
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param menu_props: See description |VAutocomplete_vuetify_link|.
        :type unknown:
        :param transition: See description |VAutocomplete_vuetify_link|.
        :type string | boolean:
        :param multiple: See description |VAutocomplete_vuetify_link|.
        :type boolean:
        :param no_data_text: Text shown when no items are provided to the component
        :type string:
        :param open_on_clear: See description |VAutocomplete_vuetify_link|.
        :type boolean:
        :param value_comparator: Apply a custom comparison algorithm used for values
        :type (a: any, b: any) => boolean:
        :param item_title: Property on supplied `items` that contains its title
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param item_value: Property on supplied `items` that contains its value
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param item_children: Property on supplied `items` that contains its children
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**
        :type boolean:
        :param autofocus: Enables autofocus
        :type boolean:
        :param prefix: Displays prefix text
        :type string:
        :param placeholder: Sets the input’s placeholder text
        :type string:
        :param persistent_placeholder: Forces placeholder to always be visible
        :type boolean:
        :param persistent_counter: Forces counter to always be visible
        :type boolean:
        :param suffix: Displays suffix text
        :type string:
        :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center
        :type boolean:
        :param hint: See description |VAutocomplete_vuetify_link|.
        :type string:
        :param persistent_hint: See description |VAutocomplete_vuetify_link|.
        :type boolean:
        :param messages: Displays a list of messages or a single message if using a string
        :type string | string[]:
        :param direction: Changes the direction of the input
        :type 'horizontal' | 'vertical':
        :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
        :type string | string[]:
        :param max_errors: Control the maximum number of shown errors from validation.
        :type string | number:
        :param readonly: Puts input in readonly state
        :type boolean:
        :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
        :param validate_on: Change what type of event triggers validation to run.
        :type | 'lazy'
      | 'blur'
      | 'input'
      | 'submit'
      | 'blur lazy'
      | 'input lazy'
      | 'submit lazy'
      | 'lazy blur'
      | 'lazy input'
      | 'lazy submit':
        :param focused: Forces a focused state styling on the component.
        :type boolean:
        :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
        :type boolean | 'auto':
        :param bg_color: See description |VAutocomplete_vuetify_link|.
        :type string:
        :param clearable: Allows for the component to be cleared
        :type boolean:
        :param clear_icon: The icon used when the **clerable** prop is set to true
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param base_color: Sets the color of the input when it is not focused
        :type string:
        :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover)
        :type boolean:
        :param prepend_inner_icon: See description |VAutocomplete_vuetify_link|.
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param single_line: Label does not move on focus/dirty
        :type boolean:
        :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
        :type string | number | true:
        :param counter_value: Function returns the counter display text
        :type (value: any) => number:
        :param model_modifiers: **FOR INTERNAL USE ONLY**
        :type Record<string, boolean>:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes
        :param click_prepend: Emitted when prepended icon is clicked
        :param click_append: Emitted when append icon is clicked
        :param update_focused: Emitted when the input is focused or blurred
        :param click_clear: Emitted when clearable icon clicked
        :param click_appendInner: Emitted when appended inner icon is clicked
        :param click_prependInner: Emitted when prepended inner icon is clicked
        :param update_search: Event emitted when the search value changes
        :param update_menu: Event that is emitted when the component's menu state changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAutocomplete", children, **kwargs)
        self._attr_names += [
            "flat",
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "reverse",
            "rounded",
            "theme",
            "color",
            "variant",
            "name",
            "id",
            "items",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "disabled",
            "loading",
            "label",
            ("auto_select_first", "autoSelectFirst"),
            "search",
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
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "transition",
            "multiple",
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("value_comparator", "valueComparator"),
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            "autofocus",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("center_affix", "centerAffix"),
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
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            ("base_color", "baseColor"),
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "counter",
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
      Vuetify's VAvatar component. See more info and examples |VAvatar_vuetify_link|.

      .. |VAvatar_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-avatar" target="_blank">here</a>


      :param end: Applies margin at the start of the component.
      :type boolean:
      :param start: Applies margin at the end of the component.
      :type boolean:
      :param icon: See description |VAvatar_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param rounded: See description |VAvatar_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VAvatar_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
      :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
      :type string | number:
      :param image: See description |VAvatar_vuetify_link|.
      :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAvatar", children, **kwargs)
        self._attr_names += [
            "end",
            "start",
            "icon",
            "density",
            "rounded",
            "tag",
            "theme",
            "color",
            "variant",
            "size",
            "image",
        ]
        self._event_names += []


class VBadge(HtmlElement):
    """
      Vuetify's VBadge component. See more info and examples |VBadge_vuetify_link|.

      .. |VBadge_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-badge" target="_blank">here</a>


      :param icon: See description |VBadge_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type boolean:
      :param location: Specifies the component's location. Can combine by using a space separated string
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param rounded: See description |VBadge_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VBadge_vuetify_link|.
      :type string:
      :param floating: Elevates the badge above the slotted content.
      :type boolean:
      :param label: The **aria-label** used for the badge
      :type string:
      :param transition: See description |VBadge_vuetify_link|.
      :type string:
      :param bordered: Applies a **2px** by default and **1.5px** border around the badge when using the **dot** property.
      :type boolean:
      :param content: Text content to show in the badge.
      :type string | number:
      :param dot: Reduce the size of the badge and hide its contents.
      :type boolean:
      :param inline: Moves the badge to be inline with the wrapping element. Supports the usage of the **left** prop.
      :type boolean:
      :param max: Sets the maximum number allowed when using the **content** prop with a `number` like value. If the content number exceeds the maximum value, a `+` suffix is added.
      :type string | number:
      :param offset_x: Offset the badge on the x-axis.
      :type string | number:
      :param offset_y: Offset the badge on the y-axis.
      :type string | number:
      :param text_color: See description |VBadge_vuetify_link|.
      :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBadge", children, **kwargs)
        self._attr_names += [
            "icon",
            ("model_value", "modelValue"),
            "location",
            "rounded",
            "tag",
            "theme",
            "color",
            "floating",
            "label",
            "transition",
            "bordered",
            "content",
            "dot",
            "inline",
            "max",
            ("offset_x", "offsetX"),
            ("offset_y", "offsetY"),
            ("text_color", "textColor"),
        ]
        self._event_names += []


class VBanner(HtmlElement):
    """
      Vuetify's VBanner component. See more info and examples |VBanner_vuetify_link|.

      .. |VBanner_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-banner" target="_blank">here</a>


      :param text: Specify content text for the component.
      :type string:
      :param border: Applies border styles to component.
      :type string | number | boolean:
      :param icon: See description |VBanner_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param elevation: See description |VBanner_vuetify_link|.
      :type string | number:
      :param location: Specifies the component's location. Can combine by using a space separated string
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param position: MISSING DESCRIPTION
      :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
      :param sticky: See description |VBanner_vuetify_link|.
      :type boolean:
      :param rounded: See description |VBanner_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VBanner_vuetify_link|.
      :type string:
      :param stacked: Forces the banner actions onto a new line. This is only applicable when the banner is not **single-line** or using the **actions** slot.
      :type boolean:
      :param avatar: Designates a specific src image to pass to the thumbnail.
      :type string:
      :param lines: The amount of visible lines of text before it truncates.
      :type 'one' | 'two' | 'three':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBanner", children, **kwargs)
        self._attr_names += [
            "text",
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
            "sticky",
            "rounded",
            "tag",
            "theme",
            "color",
            "stacked",
            "avatar",
            "lines",
        ]
        self._event_names += []


class VBannerActions(HtmlElement):
    """
    Vuetify's VBannerActions component. See more info and examples |VBannerActions_vuetify_link|.

    .. |VBannerActions_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-banner-actions" target="_blank">here</a>


    :param density: Adjusts the vertical height used by the component.
    :type string:
    :param color: See description |VBannerActions_vuetify_link|.
    :type string:

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
    Vuetify's VBannerText component. See more info and examples |VBannerText_vuetify_link|.

    .. |VBannerText_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-banner-text" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBannerText", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VBottomNavigation(HtmlElement):
    """
    Vuetify's VBottomNavigation component. See more info and examples |VBottomNavigation_vuetify_link|.

    .. |VBottomNavigation_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-bottom-navigation" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param height: Sets the height for the component
    :type string | number:
    :param elevation: See description |VBottomNavigation_vuetify_link|.
    :type string | number:
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param rounded: See description |VBottomNavigation_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VBottomNavigation_vuetify_link|.
    :type string:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param bg_color: See description |VBottomNavigation_vuetify_link|.
    :type string:
    :param mode: Changes the orientation and active state styling of the component.
    :type string:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param grow: See description |VBottomNavigation_vuetify_link|.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBottomNavigation", children, **kwargs)
        self._attr_names += [
            "border",
            ("model_value", "modelValue"),
            "density",
            "height",
            "elevation",
            "absolute",
            "rounded",
            "tag",
            "theme",
            "color",
            "name",
            "order",
            "active",
            "disabled",
            ("selected_class", "selectedClass"),
            "multiple",
            ("bg_color", "bgColor"),
            "mode",
            "max",
            "grow",
            "mandatory",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VBottomSheet(HtmlElement):
    """
    Vuetify's VBottomSheet component. See more info and examples |VBottomSheet_vuetify_link|.

    .. |VBottomSheet_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-bottom-sheet" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param location: MISSING DESCRIPTION
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param absolute: Applies **position: absolute** to the content element.
    :type boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param z_index: The z-index used for the component
    :type string | number:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param activator: See description |VBottomSheet_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |VBottomSheet_vuetify_link|.
    :type any:
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :type boolean:
    :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
    :type boolean:
    :param scrim: Accepts true/false to enable background, and string to define color.
    :type string | boolean:
    :param activator_props: See description |VBottomSheet_vuetify_link|.
    :type {}:
    :param open_on_click: See description |VBottomSheet_vuetify_link|.
    :type boolean:
    :param open_on_hover: See description |VBottomSheet_vuetify_link|.
    :type boolean:
    :param open_on_focus: See description |VBottomSheet_vuetify_link|.
    :type boolean:
    :param close_on_content_click: Closes component when you click on its content
    :type boolean:
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :type string | number:
    :param location_strategy: A function used to specifies how the component should position relative to its activator
    :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param origin: See description |VBottomSheet_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
    :param offset: A single value that offsets content away from the target based upon what side it is on
    :type string | number | number[]:
    :param scroll_strategy: See description |VBottomSheet_vuetify_link|.
    :type 'close' | 'block' | 'none' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
    :param transition: See description |VBottomSheet_vuetify_link|.
    :type string | { component: Component }:
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :type string | boolean | Element:
    :param inset: Reduces the sheet content maximum width to 70%.
    :type boolean:
    :param fullscreen: Changes layout for fullscreen display.
    :type boolean:
    :param retain_focus: Tab focus will return to the first child of the dialog by default. Disable this when using external tools that require focus such as TinyMCE or vue-clipboard.
    :type boolean:
    :param scrollable: See description |VBottomSheet_vuetify_link|.
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBottomSheet", children, **kwargs)
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
            ("z_index", "zIndex"),
            "disabled",
            "eager",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            ("no_click_animation", "noClickAnimation"),
            "persistent",
            "scrim",
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
            "inset",
            "fullscreen",
            ("retain_focus", "retainFocus"),
            "scrollable",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VBreadcrumbs(HtmlElement):
    """
        Vuetify's VBreadcrumbs component. See more info and examples |VBreadcrumbs_vuetify_link|.

        .. |VBreadcrumbs_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-breadcrumbs" target="_blank">here</a>


        :param icon: See description |VBreadcrumbs_vuetify_link|.
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param rounded: See description |VBreadcrumbs_vuetify_link|.
        :type string | number | boolean:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param color: See description |VBreadcrumbs_vuetify_link|.
        :type string:
        :param items: An array of strings or objects used for automatically generating children components
        :type (
      | string
      | (Partial<LinkProps> & { title: string; disabled?: boolean })
    )[]:
        :param disabled: Removes the ability to click or target the component
        :type boolean:
        :param bg_color: See description |VBreadcrumbs_vuetify_link|.
        :type string:
        :param divider: Specifies the dividing character between items.
        :type string:
        :param active_class: The class applied to the component when it is in an active state
        :type string:
        :param active_color: The applied color when the component is in an active state
        :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBreadcrumbs", children, **kwargs)
        self._attr_names += [
            "icon",
            "density",
            "rounded",
            "tag",
            "color",
            "items",
            "disabled",
            ("bg_color", "bgColor"),
            "divider",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
        ]
        self._event_names += []


class VBreadcrumbsDivider(HtmlElement):
    """
    Vuetify's VBreadcrumbsDivider component. See more info and examples |VBreadcrumbsDivider_vuetify_link|.

    .. |VBreadcrumbsDivider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-breadcrumbs-divider" target="_blank">here</a>


    :param divider: Specifies the dividing character between items.
    :type string | number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBreadcrumbsDivider", children, **kwargs)
        self._attr_names += [
            "divider",
        ]
        self._event_names += []


class VBreadcrumbsItem(HtmlElement):
    """
    Vuetify's VBreadcrumbsItem component. See more info and examples |VBreadcrumbsItem_vuetify_link|.

    .. |VBreadcrumbsItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-breadcrumbs-item" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param color: See description |VBreadcrumbsItem_vuetify_link|.
    :type string:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VBreadcrumbsItem_vuetify_link|.
    :type boolean:
    :param exact: See description |VBreadcrumbsItem_vuetify_link|.
    :type boolean:
    :param to: See description |VBreadcrumbsItem_vuetify_link|.
    :type unknown:
    :param active_class: See description |VBreadcrumbsItem_vuetify_link|.
    :type string:
    :param active_color: The applied color when the component is in an active state
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBreadcrumbsItem", children, **kwargs)
        self._attr_names += [
            "title",
            "tag",
            "color",
            "active",
            "disabled",
            "href",
            "replace",
            "exact",
            "to",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
        ]
        self._event_names += []


class VBtn(HtmlElement):
    """
      Vuetify's VBtn component. See more info and examples |VBtn_vuetify_link|.

      .. |VBtn_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-btn" target="_blank">here</a>


      :param symbol: See description |VBtn_vuetify_link|.
      :type any:
      :param text: Specify content text for the component.
      :type string:
      :param flat: Removes the button box shadow.
      :type boolean:
      :param border: Applies border styles to component.
      :type string | number | boolean:
      :param icon: See description |VBtn_vuetify_link|.
      :type | boolean
    | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param elevation: See description |VBtn_vuetify_link|.
      :type string | number:
      :param location: Specifies the component's location. Can combine by using a space separated string
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param position: MISSING DESCRIPTION
      :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
      :param rounded: See description |VBtn_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VBtn_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
      :type string | number:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component
      :type boolean:
      :param prepend_icon: See description |VBtn_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VBtn_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param block: Expands the button to 100% of available space.
      :type boolean:
      :param stacked: Displays the button as a flex-column.
      :type boolean:
      :param ripple: See description |VBtn_vuetify_link|.
      :type boolean | { class: string }:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param href: Designates the component as anchor and applies the **href** attribute.
      :type string:
      :param replace: See description |VBtn_vuetify_link|.
      :type boolean:
      :param exact: See description |VBtn_vuetify_link|.
      :type boolean:
      :param to: See description |VBtn_vuetify_link|.
      :type unknown:

      Events

      :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtn", children, **kwargs)
        self._attr_names += [
            "symbol",
            "text",
            "flat",
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
            "tag",
            "theme",
            "color",
            "variant",
            "value",
            "size",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "block",
            "stacked",
            "ripple",
            "disabled",
            ("selected_class", "selectedClass"),
            "loading",
            "href",
            "replace",
            "exact",
            "to",
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VBtnGroup(HtmlElement):
    """
    Vuetify's VBtnGroup component. See more info and examples |VBtnGroup_vuetify_link|.

    .. |VBtnGroup_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-btn-group" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param elevation: See description |VBtnGroup_vuetify_link|.
    :type string | number:
    :param rounded: See description |VBtnGroup_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VBtnGroup_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
    :param divided: See description |VBtnGroup_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtnGroup", children, **kwargs)
        self._attr_names += [
            "border",
            "density",
            "elevation",
            "rounded",
            "tag",
            "theme",
            "color",
            "variant",
            "divided",
        ]
        self._event_names += []


class VBtnToggle(HtmlElement):
    """
    Vuetify's VBtnToggle component. See more info and examples |VBtnToggle_vuetify_link|.

    .. |VBtnToggle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-btn-toggle" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param elevation: See description |VBtnToggle_vuetify_link|.
    :type string | number:
    :param rounded: Round edge buttons
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VBtnToggle_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param divided: See description |VBtnToggle_vuetify_link|.
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtnToggle", children, **kwargs)
        self._attr_names += [
            "border",
            ("model_value", "modelValue"),
            "density",
            "elevation",
            "rounded",
            "tag",
            "theme",
            "color",
            "variant",
            "disabled",
            ("selected_class", "selectedClass"),
            "multiple",
            "max",
            "mandatory",
            "divided",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VCard(HtmlElement):
    """
      Vuetify's VCard component. See more info and examples |VCard_vuetify_link|.

      .. |VCard_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-card" target="_blank">here</a>


      :param title: Specify a title text for the component.
      :type string:
      :param text: Specify content text for the component.
      :type string:
      :param flat: Removes the card's elevation.
      :type boolean:
      :param border: Applies border styles to component.
      :type string | number | boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param elevation: See description |VCard_vuetify_link|.
      :type string | number:
      :param location: Specifies the component's location. Can combine by using a space separated string
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param position: MISSING DESCRIPTION
      :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
      :param rounded: See description |VCard_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VCard_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
      :param image: Apply a specific background image to the component.
      :type string:
      :param prepend_icon: See description |VCard_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VCard_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param ripple: See description |VCard_vuetify_link|.
      :type boolean | { class: string }:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param href: Designates the component as anchor and applies the **href** attribute.
      :type string:
      :param replace: See description |VCard_vuetify_link|.
      :type boolean:
      :param exact: See description |VCard_vuetify_link|.
      :type boolean:
      :param to: See description |VCard_vuetify_link|.
      :type unknown:
      :param link: Designates that the component is a link. This is automatic when using the href or to prop.
      :type boolean:
      :param subtitle: Specify a subtitle text for the component.
      :type string:
      :param append_avatar: See description |VCard_vuetify_link|.
      :type string:
      :param hover: See description |VCard_vuetify_link|.
      :type boolean:
      :param prepend_avatar: See description |VCard_vuetify_link|.
      :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCard", children, **kwargs)
        self._attr_names += [
            "title",
            "text",
            "flat",
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
            "tag",
            "theme",
            "color",
            "variant",
            "image",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "ripple",
            "disabled",
            "loading",
            "href",
            "replace",
            "exact",
            "to",
            "link",
            "subtitle",
            ("append_avatar", "appendAvatar"),
            "hover",
            ("prepend_avatar", "prependAvatar"),
        ]
        self._event_names += []


class VCardActions(HtmlElement):
    """
    Vuetify's VCardActions component. See more info and examples |VCardActions_vuetify_link|.

    .. |VCardActions_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-actions" target="_blank">here</a>



    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardActions", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VCardItem(HtmlElement):
    """
      Vuetify's VCardItem component. See more info and examples |VCardItem_vuetify_link|.

      .. |VCardItem_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-card-item" target="_blank">here</a>


      :param title: Specify a title text for the component.
      :type string:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param prepend_icon: See description |VCardItem_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VCardItem_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param subtitle: Specify a subtitle text for the component.
      :type string:
      :param append_avatar: See description |VCardItem_vuetify_link|.
      :type string:
      :param prepend_avatar: See description |VCardItem_vuetify_link|.
      :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardItem", children, **kwargs)
        self._attr_names += [
            "title",
            "density",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "subtitle",
            ("append_avatar", "appendAvatar"),
            ("prepend_avatar", "prependAvatar"),
        ]
        self._event_names += []


class VCardSubtitle(HtmlElement):
    """
    Vuetify's VCardSubtitle component. See more info and examples |VCardSubtitle_vuetify_link|.

    .. |VCardSubtitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-subtitle" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardSubtitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCardText(HtmlElement):
    """
    Vuetify's VCardText component. See more info and examples |VCardText_vuetify_link|.

    .. |VCardText_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-text" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardText", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCardTitle(HtmlElement):
    """
    Vuetify's VCardTitle component. See more info and examples |VCardTitle_vuetify_link|.

    .. |VCardTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardTitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCarousel(HtmlElement):
    """
      Vuetify's VCarousel component. See more info and examples |VCarousel_vuetify_link|.

      .. |VCarousel_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-carousel" target="_blank">here</a>


      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param height: Sets the height for the component
      :type string | number:
      :param reverse: Reverse the normal transition direction.
      :type boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VCarousel_vuetify_link|.
      :type string:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param direction: The transition direction when changing windows.
      :type 'horizontal' | 'vertical':
      :param mandatory: Forces at least one item to always be selected (if available).
      :type 'force':
      :param cycle: Determines if the carousel should cycle through images.
      :type boolean:
      :param delimiter_icon: Sets icon for carousel delimiter
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param hide_delimiters: Hides the carousel's bottom delimiters.
      :type boolean:
      :param hide_delimiter_background: Hides the bottom delimiter background.
      :type boolean:
      :param interval: The duration between image cycles. Requires the **cycle** prop.
      :type string | number:
      :param progress: Displays a carousel progress bar. Requires the **cycle** prop and **interval**.
      :type string | boolean:
      :param continuous: Determines whether carousel is continuous
      :type boolean:
      :param next_icon: The displayed icon for forcing pagination to the next item.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param prev_icon: The displayed icon for forcing pagination to the previous item.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param show_arrows: Displays arrows for next/previous navigation.
      :type string | boolean:
      :param touch: Provide a custom **left** and **right** function when swiped left or right.
      :type any:
      :param vertical_delimiters: Displays carousel delimiters vertically.
      :type boolean | 'left' | 'right':

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCarousel", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "height",
            "reverse",
            "tag",
            "theme",
            "color",
            "disabled",
            ("selected_class", "selectedClass"),
            "direction",
            "mandatory",
            "cycle",
            ("delimiter_icon", "delimiterIcon"),
            ("hide_delimiters", "hideDelimiters"),
            ("hide_delimiter_background", "hideDelimiterBackground"),
            "interval",
            "progress",
            "continuous",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            "touch",
            ("vertical_delimiters", "verticalDelimiters"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VCarouselItem(HtmlElement):
    """
      Vuetify's VCarouselItem component. See more info and examples |VCarouselItem_vuetify_link|.

      .. |VCarouselItem_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-carousel-item" target="_blank">here</a>


      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
      :type boolean:
      :param content_class: Apply a custom class to the internal content element.
      :type string:
      :param transition: See description |VCarouselItem_vuetify_link|.
      :type string | boolean:
      :param options: See description |VCarouselItem_vuetify_link|.
      :type { root: any; rootMargin: any; threshold: any }:
      :param inline: Display as an inline element instead of a block, also disables flex-grow.
      :type boolean:
      :param alt: Alternate text for screen readers. Leave empty for decorative images.
      :type string:
      :param cover: Resizes the background image to cover the entire container.
      :type boolean:
      :param gradient: See description |VCarouselItem_vuetify_link|.
      :type string:
      :param lazy_src: See description |VCarouselItem_vuetify_link|.
      :type string:
      :param sizes: See description |VCarouselItem_vuetify_link|.
      :type string:
      :param src: The image URL. This prop is mandatory.
      :type | string
    | { src: string; srcset: string; lazySrc: string; aspect: number }:
      :param srcset: See description |VCarouselItem_vuetify_link|.
      :type string:
      :param aspect_ratio: Sets a base aspect ratio, calculated as width/height. This will only set a **minimum** height, the component can still grow if it has a lot of content
      :type string | number:
      :param reverse_transition: Sets the reverse transition
      :type string | boolean:

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
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "eager",
            ("content_class", "contentClass"),
            "transition",
            "options",
            "inline",
            "alt",
            "cover",
            "gradient",
            ("lazy_src", "lazySrc"),
            "sizes",
            "src",
            "srcset",
            ("aspect_ratio", "aspectRatio"),
            ("reverse_transition", "reverseTransition"),
        ]
        self._event_names += []


class VCheckbox(HtmlElement):
    """
      Vuetify's VCheckbox component. See more info and examples |VCheckbox_vuetify_link|.

      .. |VCheckbox_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-checkbox" target="_blank">here</a>


      :param type: MISSING DESCRIPTION
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VCheckbox_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param id: MISSING DESCRIPTION
      :type string:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VCheckbox_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param ripple: See description |VCheckbox_vuetify_link|.
      :type boolean:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param label: See description |VCheckbox_vuetify_link|.
      :type string:
      :param multiple: Changes expected model to an array
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm used for values
      :type (a: any, b: any) => boolean:
      :param center_affix: MISSING DESCRIPTION
      :type boolean:
      :param hint: See description |VCheckbox_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VCheckbox_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: Changes the direction of the input
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':
      :param indeterminate: Sets an indeterminate state for the checkbox
      :type boolean:
      :param indeterminate_icon: The icon used when in an indeterminate state
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param true_value: Sets value for truthy state
      :type any:
      :param false_value: Sets value for falsy state
      :type any:
      :param defaults_target: MISSING DESCRIPTION
      :type string:
      :param false_icon: The icon used when inactive
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param true_icon: The icon used when active
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: Emitted when prepended icon is clicked
      :param click_append: Emitted when appended icon is clicked
      :param update_focused: Event that is emitted when the component's focus state changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCheckbox", children, **kwargs)
        self._attr_names += [
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "theme",
            "color",
            "name",
            "value",
            "id",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "ripple",
            "disabled",
            "label",
            "multiple",
            ("value_comparator", "valueComparator"),
            ("center_affix", "centerAffix"),
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
      Vuetify's VCheckboxBtn component. See more info and examples |VCheckboxBtn_vuetify_link|.

      .. |VCheckboxBtn_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-checkbox-btn" target="_blank">here</a>


      :param type: MISSING DESCRIPTION
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: MISSING DESCRIPTION
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VCheckboxBtn_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param id: MISSING DESCRIPTION
      :type string:
      :param ripple: See description |VCheckboxBtn_vuetify_link|.
      :type boolean:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param label: See description |VCheckboxBtn_vuetify_link|.
      :type string:
      :param multiple: MISSING DESCRIPTION
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm used for values
      :type (a: any, b: any) => boolean:
      :param readonly: MISSING DESCRIPTION
      :type boolean:
      :param inline: MISSING DESCRIPTION
      :type boolean:
      :param indeterminate: See description |VCheckboxBtn_vuetify_link|.
      :type boolean:
      :param indeterminate_icon: Icon used when the component is in an indeterminate state.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param true_value: Sets value for truthy state
      :type any:
      :param false_value: Sets value for falsy state
      :type any:
      :param defaults_target: MISSING DESCRIPTION
      :type string:
      :param false_icon: MISSING DESCRIPTION
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param true_icon: MISSING DESCRIPTION
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param update_indeterminate: Event that is emitted when the component's indeterminate state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCheckboxBtn", children, **kwargs)
        self._attr_names += [
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "theme",
            "color",
            "name",
            "value",
            "id",
            "ripple",
            "disabled",
            "label",
            "multiple",
            ("value_comparator", "valueComparator"),
            "readonly",
            "inline",
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
            ("update_indeterminate", "update:indeterminate"),
        ]


class VChip(HtmlElement):
    """
      Vuetify's VChip component. See more info and examples |VChip_vuetify_link|.

      .. |VChip_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-chip" target="_blank">here</a>


      :param text: Specify content text for the component.
      :type string:
      :param filter: Displays a selection icon when selected
      :type boolean:
      :param border: Applies border styles to component.
      :type string | number | boolean:
      :param closable: Adds remove button and then a chip can be closed
      :type boolean:
      :param close_icon: Change the default icon used for **close** chips
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param close_label: See description |VChip_vuetify_link|.
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param elevation: See description |VChip_vuetify_link|.
      :type string | number:
      :param rounded: See description |VChip_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VChip_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
      :param value: See description |VChip_vuetify_link|.
      :type any:
      :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
      :type string | number:
      :param prepend_icon: See description |VChip_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VChip_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param ripple: See description |VChip_vuetify_link|.
      :type boolean | { class: string }:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param href: Designates the component as anchor and applies the **href** attribute.
      :type string:
      :param replace: See description |VChip_vuetify_link|.
      :type boolean:
      :param exact: See description |VChip_vuetify_link|.
      :type boolean:
      :param to: See description |VChip_vuetify_link|.
      :type unknown:
      :param label: Applies a medium size border radius
      :type boolean:
      :param link: Designates that the component is a link. This is automatic when using the href or to prop.
      :type boolean:
      :param active_class: See description |VChip_vuetify_link|.
      :type string:
      :param append_avatar: See description |VChip_vuetify_link|.
      :type string:
      :param prepend_avatar: See description |VChip_vuetify_link|.
      :type string:
      :param draggable: Makes the chip draggable
      :type boolean:
      :param filter_icon: Change the default icon used for **filter** chips
      :type string:
      :param pill: Remove `v-avatar` padding
      :type boolean:

      Events

      :param click_close: Emitted when close icon is clicked
      :param update_modelValue: Event that is emitted when the component's model changes
      :param group_selected: Event that is emitted when an item is selected within a group.
      :param clickOnce: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VChip", children, **kwargs)
        self._attr_names += [
            "text",
            "filter",
            "border",
            "closable",
            ("close_icon", "closeIcon"),
            ("close_label", "closeLabel"),
            ("model_value", "modelValue"),
            "density",
            "elevation",
            "rounded",
            "tag",
            "theme",
            "color",
            "variant",
            "value",
            "size",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "ripple",
            "disabled",
            ("selected_class", "selectedClass"),
            "href",
            "replace",
            "exact",
            "to",
            "label",
            "link",
            ("active_class", "activeClass"),
            ("append_avatar", "appendAvatar"),
            ("prepend_avatar", "prependAvatar"),
            "draggable",
            ("filter_icon", "filterIcon"),
            "pill",
        ]
        self._event_names += [
            ("click_close", "click:close"),
            ("update_modelValue", "update:modelValue"),
            "click",
            ("group_selected", "group:selected"),
            "clickOnce",
        ]


class VChipGroup(HtmlElement):
    """
    Vuetify's VChipGroup component. See more info and examples |VChipGroup_vuetify_link|.

    .. |VChipGroup_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-chip-group" target="_blank">here</a>


    :param filter: Applies an checkmark icon in front of every chip for using it like a filter
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VChipGroup_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param column: Remove horizontal pagination and wrap items as needed
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VChipGroup", children, **kwargs)
        self._attr_names += [
            "filter",
            ("model_value", "modelValue"),
            "tag",
            "theme",
            "color",
            "variant",
            "disabled",
            ("selected_class", "selectedClass"),
            "multiple",
            ("value_comparator", "valueComparator"),
            "max",
            "mandatory",
            "column",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VClassIcon(HtmlElement):
    """
      Vuetify's VClassIcon component. See more info and examples |VClassIcon_vuetify_link|.

      .. |VClassIcon_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-class-icon" target="_blank">here</a>


      :param icon: See description |VClassIcon_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param tag: Specify a custom tag used on the root element
      :type string:

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
    Vuetify's VCode component. See more info and examples |VCode_vuetify_link|.

    .. |VCode_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-code" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCode", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCol(HtmlElement):
    """
    Vuetify's VCol component. See more info and examples |VCol_vuetify_link|.

    .. |VCol_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-col" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param order: See description |VCol_vuetify_link|.
    :type string | number:
    :param offset: Sets the default offset for the column.
    :type string | number:
    :param cols: Sets the default number of columns the component extends. Available options are: **1 -> 12** and **auto**.
    :type string | number | boolean:
    :param sm: Changes the number of columns on small and greater breakpoints.
    :type string | number | boolean:
    :param md: Changes the number of columns on medium and greater breakpoints.
    :type string | number | boolean:
    :param lg: Changes the number of columns on large and greater breakpoints.
    :type string | number | boolean:
    :param xl: Changes the number of columns on extra large and greater breakpoints.
    :type string | number | boolean:
    :param xxl: Changes the number of columns on extra extra large and greater breakpoints.
    :type string | number | boolean:
    :param offset_sm: Changes the offset of the component on small and greater breakpoints.
    :type string | number:
    :param offset_md: Changes the offset of the component on medium and greater breakpoints.
    :type string | number:
    :param offset_lg: Changes the offset of the component on large and greater breakpoints.
    :type string | number:
    :param offset_xl: Changes the offset of the component on extra large and greater breakpoints.
    :type string | number:
    :param offset_xxl: Changes the offset of the component on extra extra large and greater breakpoints.
    :type string | number:
    :param order_sm: Changes the order of the component on small and greater breakpoints.
    :type string | number:
    :param order_md: Changes the order of the component on medium and greater breakpoints.
    :type string | number:
    :param order_lg: Changes the order of the component on large and greater breakpoints.
    :type string | number:
    :param order_xl: Changes the order of the component on extra large and greater breakpoints.
    :type string | number:
    :param order_xxl: Changes the order of the component on extra extra large and greater breakpoints.
    :type string | number:
    :param align_self: See description |VCol_vuetify_link|.
    :type 'end' | 'start' | 'center' | 'auto' | 'baseline' | 'stretch':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCol", children, **kwargs)
        self._attr_names += [
            "tag",
            "order",
            "offset",
            "cols",
            "sm",
            "md",
            "lg",
            "xl",
            "xxl",
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
        Vuetify's VColorPicker component. See more info and examples |VColorPicker_vuetify_link|.

        .. |VColorPicker_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-color-picker" target="_blank">here</a>


        :param border: Applies border styles to component.
        :type string | number | boolean:
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
        :type string | Record<string, unknown>:
        :param width: Sets the width of the color picker
        :type string | number:
        :param elevation: See description |VColorPicker_vuetify_link|.
        :type string | number:
        :param position: MISSING DESCRIPTION
        :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
        :param rounded: See description |VColorPicker_vuetify_link|.
        :type string | number | boolean:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children
        :type string:
        :param color: See description |VColorPicker_vuetify_link|.
        :type string:
        :param disabled: Removes the ability to click or target the component
        :type boolean:
        :param mode: The current selected input type. Syncable with `v-model:mode`
        :type 'rgb' | 'rgba' | 'hsl' | 'hsla' | 'hex' | 'hexa':
        :param canvas_height: Height of canvas
        :type string | number:
        :param dot_size: Changes the size of the selection dot on the canvas
        :type string | number:
        :param hide_canvas: Hides canvas
        :type boolean:
        :param hide_sliders: Hides sliders
        :type boolean:
        :param hide_inputs: Hides inputs
        :type boolean:
        :param modes: Sets available input types
        :type ('rgb' | 'rgba' | 'hsl' | 'hsla' | 'hex' | 'hexa')[]:
        :param show_swatches: Displays color swatches
        :type boolean:
        :param swatches_max_height: Sets the maximum height of the swatches section
        :type string | number:
        :param swatches: Sets the available color swatches to select from. 2D array of rows and columns, accepts any color format the picker does
        :type (
      | string
      | number
      | {
          readonly h: number
          readonly s: number
          readonly v: number
          readonly a?: number
        }
      | {
          readonly r: number
          readonly g: number
          readonly b: number
          readonly a?: number
        }
      | {
          readonly h: number
          readonly s: number
          readonly l: number
          readonly a?: number
        }
    )[][]:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes
        :param update_mode: Selected mode
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VColorPicker", children, **kwargs)
        self._attr_names += [
            "border",
            ("model_value", "modelValue"),
            "width",
            "elevation",
            "position",
            "rounded",
            "tag",
            "theme",
            "color",
            "disabled",
            "mode",
            ("canvas_height", "canvasHeight"),
            ("dot_size", "dotSize"),
            ("hide_canvas", "hideCanvas"),
            ("hide_sliders", "hideSliders"),
            ("hide_inputs", "hideInputs"),
            "modes",
            ("show_swatches", "showSwatches"),
            ("swatches_max_height", "swatchesMaxHeight"),
            "swatches",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_mode", "update:mode"),
        ]


class VCombobox(HtmlElement):
    """
        Vuetify's VCombobox component. See more info and examples |VCombobox_vuetify_link|.

        .. |VCombobox_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-combobox" target="_blank">here</a>


        :param flat: Removes elevation (shadow) added to element when using the **solo** or **solo-inverted** props
        :type boolean:
        :param type: Sets input type
        :type string:
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
        :type any:
        :param error: Puts the input in a manual error state
        :type boolean:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param reverse: Reverses the orientation
        :type boolean:
        :param rounded: Adds a border radius to the input
        :type string | number | boolean:
        :param theme: Specify a theme for this component and all of its children
        :type string:
        :param color: See description |VCombobox_vuetify_link|.
        :type string:
        :param variant: Applies a distinct style to the component
        :type | 'outlined'
      | 'plain'
      | 'underlined'
      | 'filled'
      | 'solo'
      | 'solo-inverted'
      | 'solo-filled':
        :param name: Sets the component's name attribute.
        :type string:
        :param id: Sets the DOM id on the component
        :type string:
        :param items: An array of strings or objects used for automatically generating children components
        :type any[]:
        :param active: Controls the **active** state of the item. This is typically used to highlight the component
        :type boolean:
        :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param append_icon: See description |VCombobox_vuetify_link|.
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param disabled: Removes the ability to click or target the input
        :type boolean:
        :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
        :type string | boolean:
        :param label: See description |VCombobox_vuetify_link|.
        :type string:
        :param auto_select_first: When searching, will always highlight the first option and select it on blur. `exact` will only highlight and select exact matches.
        :type boolean | 'exact':
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'every' | 'some' | 'union' | 'intersection':
        :param no_filter: Disables all item filtering.
        :type boolean:
        :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type { [string]: <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a> }:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param chips: See description |VCombobox_vuetify_link|.
        :type boolean:
        :param closable_chips: See description |VCombobox_vuetify_link|.
        :type boolean:
        :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
        :type boolean:
        :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
        :type boolean:
        :param hide_selected: See description |VCombobox_vuetify_link|.
        :type boolean:
        :param menu: Renders with the menu open by default
        :type boolean:
        :param menu_icon: Sets the the spin icon
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param menu_props: See description |VCombobox_vuetify_link|.
        :type unknown:
        :param transition: See description |VCombobox_vuetify_link|.
        :type string | boolean:
        :param multiple: See description |VCombobox_vuetify_link|.
        :type boolean:
        :param no_data_text: Text shown when no items are provided to the component
        :type string:
        :param open_on_clear: See description |VCombobox_vuetify_link|.
        :type boolean:
        :param value_comparator: Apply a custom comparison algorithm used for values
        :type (a: any, b: any) => boolean:
        :param item_title: Property on supplied `items` that contains its title
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param item_value: Property on supplied `items` that contains its value
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param item_children: Property on supplied `items` that contains its children
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**
        :type boolean:
        :param autofocus: Enables autofocus
        :type boolean:
        :param prefix: Displays prefix text
        :type string:
        :param placeholder: Sets the input’s placeholder text
        :type string:
        :param persistent_placeholder: Forces placeholder to always be visible
        :type boolean:
        :param persistent_counter: Forces counter to always be visible
        :type boolean:
        :param suffix: Displays suffix text
        :type string:
        :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center
        :type boolean:
        :param hint: See description |VCombobox_vuetify_link|.
        :type string:
        :param persistent_hint: See description |VCombobox_vuetify_link|.
        :type boolean:
        :param messages: Displays a list of messages or a single message if using a string
        :type string | string[]:
        :param direction: Changes the direction of the input
        :type 'horizontal' | 'vertical':
        :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
        :type string | string[]:
        :param max_errors: Control the maximum number of shown errors from validation.
        :type string | number:
        :param readonly: Puts input in readonly state
        :type boolean:
        :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
        :param validate_on: Change what type of event triggers validation to run.
        :type | 'lazy'
      | 'blur'
      | 'input'
      | 'submit'
      | 'blur lazy'
      | 'input lazy'
      | 'submit lazy'
      | 'lazy blur'
      | 'lazy input'
      | 'lazy submit':
        :param focused: Forces a focused state styling on the component.
        :type boolean:
        :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
        :type boolean | 'auto':
        :param bg_color: See description |VCombobox_vuetify_link|.
        :type string:
        :param clearable: Allows for the component to be cleared
        :type boolean:
        :param clear_icon: The icon used when the **clerable** prop is set to true
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param base_color: Sets the color of the input when it is not focused
        :type string:
        :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover)
        :type boolean:
        :param prepend_inner_icon: See description |VCombobox_vuetify_link|.
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param single_line: Label does not move on focus/dirty
        :type boolean:
        :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
        :type string | number | true:
        :param counter_value: Function returns the counter display text
        :type (value: any) => number:
        :param model_modifiers: **FOR INTERNAL USE ONLY**
        :type Record<string, boolean>:
        :param delimiters: Accepts an array of strings that will trigger a new tag when typing. Does not replace the normal Tab and Enter keys.
        :type string[]:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes
        :param click_prepend: Emitted when prepended icon is clicked
        :param click_append: Emitted when append icon is clicked
        :param update_focused: Emitted when the input is focused or blurred
        :param click_clear: Emitted when clearable icon clicked
        :param click_appendInner: Emitted when appended inner icon is clicked
        :param click_prependInner: Emitted when prepended inner icon is clicked
        :param update_search: Event emitted when the search value changes
        :param update_menu: Event that is emitted when the component's menu state changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCombobox", children, **kwargs)
        self._attr_names += [
            "flat",
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "reverse",
            "rounded",
            "theme",
            "color",
            "variant",
            "name",
            "id",
            "items",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "disabled",
            "loading",
            "label",
            ("auto_select_first", "autoSelectFirst"),
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
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "transition",
            "multiple",
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("value_comparator", "valueComparator"),
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            "autofocus",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("center_affix", "centerAffix"),
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
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            ("base_color", "baseColor"),
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "counter",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
            "delimiters",
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
      Vuetify's VComponentIcon component. See more info and examples |VComponentIcon_vuetify_link|.

      .. |VComponentIcon_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-component-icon" target="_blank">here</a>


      :param icon: See description |VComponentIcon_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param tag: Specify a custom tag used on the root element
      :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VComponentIcon", children, **kwargs)
        self._attr_names += [
            "icon",
            "tag",
        ]
        self._event_names += []


class VContainer(HtmlElement):
    """
    Vuetify's VContainer component. See more info and examples |VContainer_vuetify_link|.

    .. |VContainer_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-container" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param fluid: Removes viewport maximum-width size breakpoints.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VContainer", children, **kwargs)
        self._attr_names += [
            "tag",
            "fluid",
        ]
        self._event_names += []


class VCounter(HtmlElement):
    """
    Vuetify's VCounter component. See more info and examples |VCounter_vuetify_link|.

    .. |VCounter_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-counter" target="_blank">here</a>


    :param value: Sets the current counter value.
    :type string | number:
    :param active: Determines whether the counter is visible or not.
    :type boolean:
    :param transition: See description |VCounter_vuetify_link|.
    :type string | { component: Component }:
    :param max: Sets the maximum allowed value.
    :type string | number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCounter", children, **kwargs)
        self._attr_names += [
            "value",
            "active",
            "transition",
            "max",
        ]
        self._event_names += []


class VDataIterator(HtmlElement):
    """
        Vuetify's VDataIterator component. See more info and examples |VDataIterator_vuetify_link|.

        .. |VDataIterator_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-data-iterator" target="_blank">here</a>


        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
        :type any[]:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param items: An array of strings or objects used for automatically generating children components
        :type any[]:
        :param loading: If `true` and no items are provided, then a loading text will be shown
        :type boolean:
        :param search: Text input used to filter items
        :type string:
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'every' | 'some' | 'union' | 'intersection':
        :param no_filter: Disables all item filtering.
        :type boolean:
        :param custom_filter: Function to filter items
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type { [string]: <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a> }:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param item_value: MISSING DESCRIPTION
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param return_object: MISSING DESCRIPTION
        :type boolean:
        :param item_selectable: MISSING DESCRIPTION
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param show_select: MISSING DESCRIPTION
        :type boolean:
        :param select_strategy: MISSING DESCRIPTION
        :type 'single' | 'page' | 'all':
        :param page: MISSING DESCRIPTION
        :type string | number:
        :param sort_by: Changes which item property (or properties) should be used for sort order. Can be used with `.sync` modifier
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L29-L29" target="_blank">SortItem</a>[]:
        :param multi_sort: If `true` then one can sort on multiple properties
        :type boolean:
        :param must_sort: If `true` then one can not disable sorting, it will always switch between ascending and descending
        :type boolean:
        :param custom_key_sort: MISSING DESCRIPTION
        :type Record<string, (a: any, b: any) => number>:
        :param items_per_page: Changes how many items per page should be visible. Can be used with `.sync` modifier. Setting this prop to `-1` will display all items on the page
        :type string | number:
        :param expand_on_click: MISSING DESCRIPTION
        :type boolean:
        :param show_expand: MISSING DESCRIPTION
        :type boolean:
        :param expanded: Array of expanded items. Can be used with `.sync` modifier
        :type string[]:
        :param group_by: Changes which item property should be used for grouping items. Currently only supports a single grouping in the format: `group` or `['group']`. When using an array, only the first element is considered. Can be used with `.sync` modifier
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L29-L29" target="_blank">SortItem</a>[]:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes
        :param update_groupBy: MISSING DESCRIPTION
        :param update_page: MISSING DESCRIPTION
        :param update_itemsPerPage: MISSING DESCRIPTION
        :param update_sortBy: MISSING DESCRIPTION
        :param update_options: MISSING DESCRIPTION
        :param update_expanded: The `.sync` event for `expanded` prop
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataIterator", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "tag",
            "items",
            "loading",
            "search",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            ("select_strategy", "selectStrategy"),
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
            ("update_groupBy", "update:groupBy"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_expanded", "update:expanded"),
        ]


class VDataTable(HtmlElement):
    """
        Vuetify's VDataTable component. See more info and examples |VDataTable_vuetify_link|.

        .. |VDataTable_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-data-table" target="_blank">here</a>


        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
        :type any[]:
        :param density: Adjusts the vertical height of the table rows
        :type 'default' | 'comfortable' | 'compact':
        :param height: Set an explicit height of table
        :type string | number:
        :param width: Sets the width for the component
        :type string | number:
        :param sticky: MISSING DESCRIPTION
        :type boolean:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children
        :type string:
        :param color: See description |VDataTable_vuetify_link|.
        :type string:
        :param items: An array of strings or objects used for automatically generating children components
        :type any[]:
        :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
        :type string | boolean:
        :param search: Text input used to filter items
        :type string:
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'every' | 'some' | 'union' | 'intersection':
        :param no_filter: Disables all item filtering.
        :type boolean:
        :param custom_filter: Function to filter items
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type { [string]: <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a> }:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
        :type boolean:
        :param no_data_text: Text shown when no items are provided to the component
        :type string:
        :param item_value: MISSING DESCRIPTION
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param return_object: MISSING DESCRIPTION
        :type boolean:
        :param hover: Adds a hover effects to a table rows
        :type boolean:
        :param next_icon: MISSING DESCRIPTION
        :type string:
        :param prev_icon: MISSING DESCRIPTION
        :type string:
        :param item_selectable: MISSING DESCRIPTION
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param show_select: Shows the select checkboxes in both the header and rows (if using default rows)
        :type boolean:
        :param select_strategy: MISSING DESCRIPTION
        :type 'single' | 'page' | 'all':
        :param page: The current displayed page number (1-indexed)
        :type string | number:
        :param sort_by: Changes which item property (or properties) should be used for sort order. Can be used with `.sync` modifier
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L29-L29" target="_blank">SortItem</a>[]:
        :param multi_sort: If `true` then one can sort on multiple properties
        :type boolean:
        :param must_sort: If `true` then one can not disable sorting, it will always switch between ascending and descending
        :type boolean:
        :param custom_key_sort: MISSING DESCRIPTION
        :type Record<string, (a: any, b: any) => number>:
        :param items_per_page: Changes how many items per page should be visible. Can be used with `.sync` modifier. Setting this prop to `-1` will display all items on the page
        :type string | number:
        :param expand_on_click: MISSING DESCRIPTION
        :type boolean:
        :param show_expand: Shows the expand toggle in default rows
        :type boolean:
        :param expanded: MISSING DESCRIPTION
        :type string[]:
        :param group_by: Changes which item property should be used for grouping items. Currently only supports a single grouping in the format: `group` or `['group']`. When using an array, only the first element is considered. Can be used with `.sync` modifier
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L29-L29" target="_blank">SortItem</a>[]:
        :param headers: An array of objects that each describe a header column. See the example below for a definition of all properties
        :type DeepReadonly<DataTableHeader[] | DataTableHeader[][]>:
        :param loading_text: MISSING DESCRIPTION
        :type string:
        :param row_height: MISSING DESCRIPTION
        :type number:
        :param sort_asc_icon: MISSING DESCRIPTION
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param sort_desc_icon: MISSING DESCRIPTION
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param fixed_header: Fixed header to top of table
        :type boolean:
        :param fixed_footer: See description |VDataTable_vuetify_link|.
        :type boolean:
        :param first_icon: MISSING DESCRIPTION
        :type string:
        :param last_icon: MISSING DESCRIPTION
        :type string:
        :param items_per_page_text: MISSING DESCRIPTION
        :type string:
        :param page_text: MISSING DESCRIPTION
        :type string:
        :param first_page_label: MISSING DESCRIPTION
        :type string:
        :param prev_page_label: MISSING DESCRIPTION
        :type string:
        :param next_page_label: MISSING DESCRIPTION
        :type string:
        :param last_page_label: MISSING DESCRIPTION
        :type string:
        :param items_per_page_options: MISSING DESCRIPTION
        :type { title: string; value: number }[]:
        :param show_current_page: MISSING DESCRIPTION
        :type boolean:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes
        :param update_groupBy: MISSING DESCRIPTION
        :param update_page: Emits when the **page** property of the **options** prop is updated
        :param update_itemsPerPage: MISSING DESCRIPTION
        :param update_sortBy: MISSING DESCRIPTION
        :param update_options: Emits when one of the **options** properties is updated
        :param update_expanded: MISSING DESCRIPTION
        :param click_row: Emits when a table row is clicked. This event provides 2 arguments: the first is the native click event, and the second is an object containing the corresponding item for that row. **NOTE:** will not emit when table rows are defined through a slot such as `item` or `body`.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTable", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            ("model_value", "modelValue"),
            "density",
            "height",
            "width",
            "sticky",
            "tag",
            "theme",
            "color",
            "items",
            "loading",
            "search",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            ("hide_no_data", "hideNoData"),
            ("no_data_text", "noDataText"),
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            "hover",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            ("select_strategy", "selectStrategy"),
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
            "headers",
            ("loading_text", "loadingText"),
            ("row_height", "rowHeight"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_header", "fixedHeader"),
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
            ("update_groupBy", "update:groupBy"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_expanded", "update:expanded"),
            ("click_row", "click:row"),
        ]


class VDataTableFooter(HtmlElement):
    """
    Vuetify's VDataTableFooter component. See more info and examples |VDataTableFooter_vuetify_link|.

    .. |VDataTableFooter_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-data-table-footer" target="_blank">here</a>



    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableFooter", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VDataTableRow(HtmlElement):
    """
    Vuetify's VDataTableRow component. See more info and examples |VDataTableRow_vuetify_link|.

    .. |VDataTableRow_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-data-table-row" target="_blank">here</a>


    :param item: MISSING DESCRIPTION
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/types.ts#L33-L39" target="_blank">DataTableItem</a>:
    :param index: MISSING DESCRIPTION
    :type Number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableRow", children, **kwargs)
        self._attr_names += [
            "item",
            "index",
        ]
        self._event_names += [
            "click",
        ]


class VDataTableRows(HtmlElement):
    """
    Vuetify's VDataTableRows component. See more info and examples |VDataTableRows_vuetify_link|.

    .. |VDataTableRows_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-data-table-rows" target="_blank">here</a>


    :param items: An array of strings or objects used for automatically generating children components
    :type (<a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/types.ts#L33-L39" target="_blank">DataTableItem</a> | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/composables/group.ts#L18-L25" target="_blank">Group</a>)[]:
    :param loading: MISSING DESCRIPTION
    :type string | boolean:
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :type boolean:
    :param no_data_text: Text shown when no items are provided to the component
    :type string:
    :param loading_text: MISSING DESCRIPTION
    :type string:
    :param row_height: MISSING DESCRIPTION
    :type number:

    Events

    :param click_row: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableRows", children, **kwargs)
        self._attr_names += [
            "items",
            "loading",
            ("hide_no_data", "hideNoData"),
            ("no_data_text", "noDataText"),
            ("loading_text", "loadingText"),
            ("row_height", "rowHeight"),
        ]
        self._event_names += [
            ("click_row", "click:row"),
        ]


class VDataTableServer(HtmlElement):
    """
      Vuetify's VDataTableServer component. See more info and examples |VDataTableServer_vuetify_link|.

      .. |VDataTableServer_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-data-table-server" target="_blank">here</a>


      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any[]:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Use the height prop to set the height of the table.
      :type string | number:
      :param width: Sets the width for the component
      :type string | number:
      :param sticky: MISSING DESCRIPTION
      :type boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VDataTableServer_vuetify_link|.
      :type string:
      :param items: An array of strings or objects used for automatically generating children components
      :type any[]:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param search: Text input used to filter items.
      :type string:
      :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
      :type boolean:
      :param no_data_text: Text shown when no items are provided to the component
      :type string:
      :param item_value: MISSING DESCRIPTION
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
      :param return_object: MISSING DESCRIPTION
      :type boolean:
      :param hover: Will add a hover effect to a table's row when the mouse is over it.
      :type boolean:
      :param next_icon: MISSING DESCRIPTION
      :type string:
      :param prev_icon: MISSING DESCRIPTION
      :type string:
      :param item_selectable: MISSING DESCRIPTION
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
      :param show_select: MISSING DESCRIPTION
      :type boolean:
      :param select_strategy: MISSING DESCRIPTION
      :type 'single' | 'page' | 'all':
      :param page: MISSING DESCRIPTION
      :type string | number:
      :param sort_by: MISSING DESCRIPTION
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L29-L29" target="_blank">SortItem</a>[]:
      :param multi_sort: MISSING DESCRIPTION
      :type boolean:
      :param must_sort: MISSING DESCRIPTION
      :type boolean:
      :param custom_key_sort: MISSING DESCRIPTION
      :type Record<string, (a: any, b: any) => number>:
      :param items_per_page: MISSING DESCRIPTION
      :type string | number:
      :param expand_on_click: MISSING DESCRIPTION
      :type boolean:
      :param show_expand: MISSING DESCRIPTION
      :type boolean:
      :param expanded: MISSING DESCRIPTION
      :type string[]:
      :param group_by: MISSING DESCRIPTION
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L29-L29" target="_blank">SortItem</a>[]:
      :param items_length: MISSING DESCRIPTION
      :type string | number:
      :param headers: MISSING DESCRIPTION
      :type DeepReadonly<DataTableHeader[] | DataTableHeader[][]>:
      :param loading_text: MISSING DESCRIPTION
      :type string:
      :param row_height: MISSING DESCRIPTION
      :type number:
      :param sort_asc_icon: MISSING DESCRIPTION
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param sort_desc_icon: MISSING DESCRIPTION
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param fixed_header: Use the fixed-header prop together with the height prop to fix the header to the top of the table.
      :type boolean:
      :param fixed_footer: See description |VDataTableServer_vuetify_link|.
      :type boolean:
      :param first_icon: MISSING DESCRIPTION
      :type string:
      :param last_icon: MISSING DESCRIPTION
      :type string:
      :param items_per_page_text: MISSING DESCRIPTION
      :type string:
      :param page_text: MISSING DESCRIPTION
      :type string:
      :param first_page_label: MISSING DESCRIPTION
      :type string:
      :param prev_page_label: MISSING DESCRIPTION
      :type string:
      :param next_page_label: MISSING DESCRIPTION
      :type string:
      :param last_page_label: MISSING DESCRIPTION
      :type string:
      :param items_per_page_options: MISSING DESCRIPTION
      :type { title: string; value: number }[]:
      :param show_current_page: MISSING DESCRIPTION
      :type boolean:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param update_groupBy: MISSING DESCRIPTION
      :param update_page: MISSING DESCRIPTION
      :param update_itemsPerPage: MISSING DESCRIPTION
      :param update_sortBy: MISSING DESCRIPTION
      :param update_options: MISSING DESCRIPTION
      :param update_expanded: MISSING DESCRIPTION
      :param click_row: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableServer", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "density",
            "height",
            "width",
            "sticky",
            "tag",
            "theme",
            "color",
            "items",
            "loading",
            "search",
            ("hide_no_data", "hideNoData"),
            ("no_data_text", "noDataText"),
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            "hover",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            ("select_strategy", "selectStrategy"),
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
            ("items_length", "itemsLength"),
            "headers",
            ("loading_text", "loadingText"),
            ("row_height", "rowHeight"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_header", "fixedHeader"),
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
            ("update_groupBy", "update:groupBy"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_expanded", "update:expanded"),
            ("click_row", "click:row"),
        ]


class VDataTableVirtual(HtmlElement):
    """
        Vuetify's VDataTableVirtual component. See more info and examples |VDataTableVirtual_vuetify_link|.

        .. |VDataTableVirtual_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-data-table-virtual" target="_blank">here</a>


        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
        :type any[]:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param height: Use the height prop to set the height of the table.
        :type string | number:
        :param width: Sets the width for the component
        :type string | number:
        :param sticky: MISSING DESCRIPTION
        :type boolean:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children
        :type string:
        :param color: See description |VDataTableVirtual_vuetify_link|.
        :type string:
        :param items: An array of strings or objects used for automatically generating children components
        :type any[]:
        :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
        :type string | boolean:
        :param search: Text input used to filter items.
        :type string:
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'every' | 'some' | 'union' | 'intersection':
        :param no_filter: Disables all item filtering.
        :type boolean:
        :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type { [string]: <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a> }:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
        :type boolean:
        :param no_data_text: Text shown when no items are provided to the component
        :type string:
        :param item_value: MISSING DESCRIPTION
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param return_object: MISSING DESCRIPTION
        :type boolean:
        :param hover: Will add a hover effect to a table's row when the mouse is over it.
        :type boolean:
        :param item_selectable: MISSING DESCRIPTION
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param show_select: MISSING DESCRIPTION
        :type boolean:
        :param select_strategy: MISSING DESCRIPTION
        :type 'single' | 'page' | 'all':
        :param sort_by: MISSING DESCRIPTION
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L29-L29" target="_blank">SortItem</a>[]:
        :param multi_sort: MISSING DESCRIPTION
        :type boolean:
        :param must_sort: MISSING DESCRIPTION
        :type boolean:
        :param custom_key_sort: MISSING DESCRIPTION
        :type Record<string, (a: any, b: any) => number>:
        :param expand_on_click: MISSING DESCRIPTION
        :type boolean:
        :param show_expand: MISSING DESCRIPTION
        :type boolean:
        :param expanded: MISSING DESCRIPTION
        :type string[]:
        :param group_by: MISSING DESCRIPTION
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L29-L29" target="_blank">SortItem</a>[]:
        :param headers: MISSING DESCRIPTION
        :type DeepReadonly<DataTableHeader[] | DataTableHeader[][]>:
        :param loading_text: MISSING DESCRIPTION
        :type string:
        :param row_height: MISSING DESCRIPTION
        :type number:
        :param sort_asc_icon: MISSING DESCRIPTION
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param sort_desc_icon: MISSING DESCRIPTION
        :type | string
      | (string | [string, number])[]
      | (new () => any)
      | FunctionalComponent:
        :param fixed_header: Use the fixed-header prop together with the height prop to fix the header to the top of the table.
        :type boolean:
        :param fixed_footer: See description |VDataTableVirtual_vuetify_link|.
        :type boolean:
        :param item_height: MISSING DESCRIPTION
        :type string | number:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes
        :param update_groupBy: MISSING DESCRIPTION
        :param update_sortBy: MISSING DESCRIPTION
        :param update_options: MISSING DESCRIPTION
        :param update_expanded: MISSING DESCRIPTION
        :param click_row: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableVirtual", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "density",
            "height",
            "width",
            "sticky",
            "tag",
            "theme",
            "color",
            "items",
            "loading",
            "search",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            ("hide_no_data", "hideNoData"),
            ("no_data_text", "noDataText"),
            ("item_value", "itemValue"),
            ("return_object", "returnObject"),
            "hover",
            ("item_selectable", "itemSelectable"),
            ("show_select", "showSelect"),
            ("select_strategy", "selectStrategy"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
            "headers",
            ("loading_text", "loadingText"),
            ("row_height", "rowHeight"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            ("item_height", "itemHeight"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_groupBy", "update:groupBy"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_expanded", "update:expanded"),
            ("click_row", "click:row"),
        ]


class VDateCard(HtmlElement):
    """
      Vuetify's VDateCard component. See more info and examples |VDateCard_vuetify_link|.

      .. |VDateCard_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-date-card" target="_blank">here</a>


      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any[]:
      :param height: Sets the height for the component
      :type string | number:
      :param color: See description |VDateCard_vuetify_link|.
      :type string:
      :param transition: See description |VDateCard_vuetify_link|.
      :type | string
    | {
        component: ComponentPublicInstanceConstructor<
          {
            $: ComponentInternalInstance
            $data: {}
            $props: {
              disabled?: boolean
              origin?: string
              mode?: string
              group?: boolean
              hideOnLeave?: boolean
              leaveAbsolute?: boolean
              style?: unknown
              class?: unknown
              'v-slot:default'?: false | (() => VNodeChild)
              $children?:
                | VNodeChild
                | (() => VNodeChild)
                | { default?: () => VNodeChild }
              'v-slots'?: { default?: false | (() => VNodeChild) }
              key?: string | number | symbol
              ref?: VNodeRef
              ref_for?: boolean
              ref_key?: string
              onVnodeBeforeMount?: VNodeMountHook | VNodeMountHook[]
              onVnodeMounted?: VNodeMountHook | VNodeMountHook[]
              onVnodeBeforeUpdate?: VNodeUpdateHook | VNodeUpdateHook[]
              onVnodeUpdated?: VNodeUpdateHook | VNodeUpdateHook[]
              onVnodeBeforeUnmount?: VNodeMountHook | VNodeMountHook[]
              onVnodeUnmounted?: VNodeMountHook | VNodeMountHook[]
            }
            $attrs: Data
            $refs: Data
            $slots: Readonly<{
              default?: () => VNode<
                RendererNode,
                RendererElement,
                { [key: string]: any }
              >[]
            }>
            $root: ComponentPublicInstance<
              {},
              {},
              {},
              {},
              {},
              {},
              {},
              {},
              false,
              ComponentOptionsBase<
                any,
                any,
                any,
                any,
                any,
                any,
                any,
                any,
                any,
                {},
                {},
                string,
                {}
              >,
              {},
              {}
            >
            $parent: ComponentPublicInstance<
              {},
              {},
              {},
              {},
              {},
              {},
              {},
              {},
              false,
              ComponentOptionsBase<
                any,
                any,
                any,
                any,
                any,
                any,
                any,
                any,
                any,
                {},
                {},
                string,
                {}
              >,
              {},
              {}
            >
            $emit: (event: string, ...args: any[]) => void
            $el: any
            $options: ComponentOptionsBase<
              {
                disabled: boolean
                origin: string
                mode: string
                group: boolean
                hideOnLeave: boolean
                leaveAbsolute: boolean
              } & {} & {
                $children?:
                  | VNodeChild
                  | (() => VNodeChild)
                  | { default?: () => VNodeChild }
                'v-slots'?: { default?: false | (() => VNodeChild) }
              } & { 'v-slot:default'?: false | (() => VNodeChild) },
              () => VNode<RendererNode, RendererElement, { [key: string]: any }>,
              unknown,
              {},
              {},
              ComponentOptionsMixin,
              ComponentOptionsMixin,
              Record<string, any>,
              string,
              {
                disabled: boolean
                origin: string
                mode: string
                group: boolean
                hideOnLeave: boolean
                leaveAbsolute: boolean
              },
              {},
              string,
              SlotsType<Partial<MakeSlots<{ default: never }>>>
            > &
              MergedComponentOptionsOverride
            $forceUpdate: () => void
            $nextTick: typeof nextTick
            $watch<T extends string | ((...args: any) => any)>(
              source: T,
              cb: T extends (...args: any) => infer R
                ? (args_0: R, args_1: R) => any
                : (...args: any) => any,
              options?: WatchOptions<boolean>,
            ): WatchStopHandle
          } & {
            disabled: boolean
            origin: string
            mode: string
            group: boolean
            hideOnLeave: boolean
            leaveAbsolute: boolean
          } & {} & {
            $children?:
              | VNodeChild
              | (() => VNodeChild)
              | { default?: () => VNodeChild }
            'v-slots'?: { default?: false | (() => VNodeChild) }
          } & {
            'v-slot:default'?: false | (() => VNodeChild)
          } & ShallowUnwrapRef<
              () => VNode<RendererNode, RendererElement, { [key: string]: any }>
            > &
            ExtractComputedReturns<{}> &
            ComponentCustomProperties & {},
          any,
          any,
          any,
          ComputedOptions,
          MethodOptions
        > &
          ComponentOptionsBase<
            {
              disabled: boolean
              origin: string
              mode: string
              group: boolean
              hideOnLeave: boolean
              leaveAbsolute: boolean
            } & {} & {
              $children?:
                | VNodeChild
                | (() => VNodeChild)
                | { default?: () => VNodeChild }
              'v-slots'?: { default?: false | (() => VNodeChild) }
            } & { 'v-slot:default'?: false | (() => VNodeChild) },
            () => VNode<RendererNode, RendererElement, { [key: string]: any }>,
            unknown,
            {},
            {},
            ComponentOptionsMixin,
            ComponentOptionsMixin,
            Record<string, any>,
            string,
            {
              disabled: boolean
              origin: string
              mode: string
              group: boolean
              hideOnLeave: boolean
              leaveAbsolute: boolean
            },
            {},
            string,
            SlotsType<Partial<MakeSlots<{ default: never }>>>
          > &
          VNodeProps &
          AllowedComponentProps &
          ComponentCustomProps & {
            filterProps: (props: T) => [Partial<Pick<T, U>>, Omit<T, U>]
          }
        leaveAbsolute: boolean
      }:
      :param multiple: MISSING DESCRIPTION
      :type boolean:
      :param max: MISSING DESCRIPTION
      :type number:
      :param next_icon: MISSING DESCRIPTION
      :type string:
      :param prev_icon: MISSING DESCRIPTION
      :type string:
      :param cancel_text: MISSING DESCRIPTION
      :type string:
      :param ok_text: MISSING DESCRIPTION
      :type string:
      :param input_mode: MISSING DESCRIPTION
      :type 'keyboard' | 'calendar':
      :param hide_actions: MISSING DESCRIPTION
      :type boolean:
      :param expand_icon: MISSING DESCRIPTION
      :type string:
      :param collapse_icon: MISSING DESCRIPTION
      :type string:
      :param range: MISSING DESCRIPTION
      :type string | boolean:
      :param display_date: MISSING DESCRIPTION
      :type any:
      :param view_mode: MISSING DESCRIPTION
      :type 'month' | 'year':
      :param format: MISSING DESCRIPTION
      :type string:
      :param show_adjacent_months: MISSING DESCRIPTION
      :type boolean:
      :param hide_weekdays: MISSING DESCRIPTION
      :type boolean:
      :param show_week: MISSING DESCRIPTION
      :type boolean:
      :param hover_date: MISSING DESCRIPTION
      :type any:
      :param side: MISSING DESCRIPTION
      :type string:
      :param min: MISSING DESCRIPTION
      :type number:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param save: MISSING DESCRIPTION
      :param cancel: MISSING DESCRIPTION
      :param update_displayDate: MISSING DESCRIPTION
      :param update_inputMode: MISSING DESCRIPTION
      :param update_viewMode: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDateCard", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "height",
            "color",
            "transition",
            "multiple",
            "max",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("cancel_text", "cancelText"),
            ("ok_text", "okText"),
            ("input_mode", "inputMode"),
            ("hide_actions", "hideActions"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "range",
            ("display_date", "displayDate"),
            ("view_mode", "viewMode"),
            "format",
            ("show_adjacent_months", "showAdjacentMonths"),
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
            ("hover_date", "hoverDate"),
            "side",
            "min",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "save",
            "cancel",
            ("update_displayDate", "update:displayDate"),
            ("update_inputMode", "update:inputMode"),
            ("update_viewMode", "update:viewMode"),
        ]


class VDatePicker(HtmlElement):
    """
    Vuetify's VDatePicker component. See more info and examples |VDatePicker_vuetify_link|.

    .. |VDatePicker_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any[]:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Width of the picker
    :type string | number:
    :param elevation: See description |VDatePicker_vuetify_link|.
    :type string | number:
    :param location: Specifies the component's location. Can combine by using a space separated string
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: MISSING DESCRIPTION
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VDatePicker_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VDatePicker_vuetify_link|.
    :type string:
    :param header: Text shown when no **display-date** is set.
    :type string:
    :param multiple: Allow the selection of multiple dates
    :type boolean:
    :param max: Maximum allowed date/month (ISO 8601 format)
    :type number:
    :param next_icon: Sets the icon for next month/year button
    :type string:
    :param prev_icon: Sets the icon for previous month/year button
    :type string:
    :param cancel_text: Text used for the Cancel button.
    :type string:
    :param ok_text: Text used for the Ok button.
    :type string:
    :param input_mode: Toggles between showing dates or inputs.
    :type 'keyboard' | 'calendar':
    :param hide_actions: Hide the picker actions
    :type boolean:
    :param expand_icon: Icon used for **view-mode** toggle.
    :type string:
    :param collapse_icon: MISSING DESCRIPTION
    :type string:
    :param range: Allow the selection of date range
    :type string | boolean:
    :param display_date: The date displayed in the picker header.
    :type any:
    :param view_mode: MISSING DESCRIPTION
    :type 'month' | 'year':
    :param format: Takes a date object and returns it in a specified format.
    :type string:
    :param show_adjacent_months: Toggles visibility of days from previous and next months
    :type boolean:
    :param hide_weekdays: MISSING DESCRIPTION
    :type boolean:
    :param show_week: Toggles visibility of the week numbers in the body of the calendar
    :type boolean:
    :param hover_date: MISSING DESCRIPTION
    :type any:
    :param side: MISSING DESCRIPTION
    :type string:
    :param min: Minimum allowed date/month (ISO 8601 format)
    :type number:
    :param calendar_icon: The icon shown in the header when in 'input' **input-mode**.
    :type string:
    :param keyboard_icon: MISSING DESCRIPTION
    :type string:
    :param input_text: MISSING DESCRIPTION
    :type string:
    :param landscape: MISSING DESCRIPTION
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_focused: Event that is emitted when the component's focus state changes
    :param update_displayDate: MISSING DESCRIPTION
    :param update_inputMode: MISSING DESCRIPTION
    :param update_viewMode: MISSING DESCRIPTION
    :param click_cancel: MISSING DESCRIPTION
    :param click_save: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePicker", children, **kwargs)
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
            "tag",
            "theme",
            "color",
            "header",
            "multiple",
            "max",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("cancel_text", "cancelText"),
            ("ok_text", "okText"),
            ("input_mode", "inputMode"),
            ("hide_actions", "hideActions"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "range",
            ("display_date", "displayDate"),
            ("view_mode", "viewMode"),
            "format",
            ("show_adjacent_months", "showAdjacentMonths"),
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
            ("hover_date", "hoverDate"),
            "side",
            "min",
            ("calendar_icon", "calendarIcon"),
            ("keyboard_icon", "keyboardIcon"),
            ("input_text", "inputText"),
            "landscape",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_focused", "update:focused"),
            ("update_displayDate", "update:displayDate"),
            ("update_inputMode", "update:inputMode"),
            ("update_viewMode", "update:viewMode"),
            ("click_cancel", "click:cancel"),
            ("click_save", "click:save"),
        ]


class VDatePickerControls(HtmlElement):
    """
    Vuetify's VDatePickerControls component. See more info and examples |VDatePickerControls_vuetify_link|.

    .. |VDatePickerControls_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker-controls" target="_blank">here</a>


    :param next_icon: MISSING DESCRIPTION
    :type string:
    :param prev_icon: MISSING DESCRIPTION
    :type string:
    :param expand_icon: MISSING DESCRIPTION
    :type string:
    :param collapse_icon: MISSING DESCRIPTION
    :type string:
    :param range: MISSING DESCRIPTION
    :type string | boolean:
    :param display_date: MISSING DESCRIPTION
    :type any:
    :param view_mode: MISSING DESCRIPTION
    :type 'month' | 'year':
    :param format: MISSING DESCRIPTION
    :type string:

    Events

    :param update_focused: Event that is emitted when the component's focus state changes
    :param update_displayDate: MISSING DESCRIPTION
    :param update_viewMode: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerControls", children, **kwargs)
        self._attr_names += [
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "range",
            ("display_date", "displayDate"),
            ("view_mode", "viewMode"),
            "format",
        ]
        self._event_names += [
            ("update_focused", "update:focused"),
            ("update_displayDate", "update:displayDate"),
            ("update_viewMode", "update:viewMode"),
        ]


class VDatePickerHeader(HtmlElement):
    """
    Vuetify's VDatePickerHeader component. See more info and examples |VDatePickerHeader_vuetify_link|.

    .. |VDatePickerHeader_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker-header" target="_blank">here</a>


    :param color: See description |VDatePickerHeader_vuetify_link|.
    :type string:
    :param header: MISSING DESCRIPTION
    :type string:
    :param append_icon: See description |VDatePickerHeader_vuetify_link|.
    :type string:
    :param transition: MISSING DESCRIPTION
    :type string:

    Events

    :param click_append: Emitted when appended icon is clicked
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerHeader", children, **kwargs)
        self._attr_names += [
            "color",
            "header",
            ("append_icon", "appendIcon"),
            "transition",
        ]
        self._event_names += [
            ("click_append", "click:append"),
        ]


class VDatePickerMonth(HtmlElement):
    """
    Vuetify's VDatePickerMonth component. See more info and examples |VDatePickerMonth_vuetify_link|.

    .. |VDatePickerMonth_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker-month" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any[]:
    :param color: See description |VDatePickerMonth_vuetify_link|.
    :type string:
    :param multiple: MISSING DESCRIPTION
    :type boolean:
    :param display_date: MISSING DESCRIPTION
    :type any:
    :param format: MISSING DESCRIPTION
    :type string:
    :param show_adjacent_months: MISSING DESCRIPTION
    :type boolean:
    :param hide_weekdays: MISSING DESCRIPTION
    :type boolean:
    :param show_week: MISSING DESCRIPTION
    :type boolean:
    :param hover_date: MISSING DESCRIPTION
    :type any:
    :param side: MISSING DESCRIPTION
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_focused: Event that is emitted when the component's focus state changes
    :param update_displayDate: MISSING DESCRIPTION
    :param update_hoverDate: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerMonth", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "color",
            "multiple",
            ("display_date", "displayDate"),
            "format",
            ("show_adjacent_months", "showAdjacentMonths"),
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
            ("hover_date", "hoverDate"),
            "side",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_focused", "update:focused"),
            ("update_displayDate", "update:displayDate"),
            ("update_hoverDate", "update:hoverDate"),
        ]


class VDatePickerYears(HtmlElement):
    """
    Vuetify's VDatePickerYears component. See more info and examples |VDatePickerYears_vuetify_link|.

    .. |VDatePickerYears_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker-years" target="_blank">here</a>


    :param height: Sets the height for the component
    :type string | number:
    :param color: See description |VDatePickerYears_vuetify_link|.
    :type string:
    :param max: MISSING DESCRIPTION
    :type number:
    :param display_date: MISSING DESCRIPTION
    :type any:
    :param min: MISSING DESCRIPTION
    :type number:

    Events

    :param update_displayDate: MISSING DESCRIPTION
    :param update_viewMode: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerYears", children, **kwargs)
        self._attr_names += [
            "height",
            "color",
            "max",
            ("display_date", "displayDate"),
            "min",
        ]
        self._event_names += [
            ("update_displayDate", "update:displayDate"),
            ("update_viewMode", "update:viewMode"),
        ]


class VDefaultsProvider(HtmlElement):
    """
        Vuetify's VDefaultsProvider component. See more info and examples |VDefaultsProvider_vuetify_link|.

        .. |VDefaultsProvider_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-defaults-provider" target="_blank">here</a>


        :param disabled: Turns off all calcuations of new default values for improved performance in situations where defaults propagation isn't necessary
        :type boolean:
        :param root: Force current defaults to match the application root defaults
        :type string | boolean:
        :param reset: Reset the default values up the nested chain by {n} amount
        :type string | number:
        :param scoped: Prevents the ability for default values to be inherited from parent components
        :type boolean:
        :param defaults: Specify new default prop values for components. Keep in mind that this will be merged with previously defined values
        :type {
      global: Record<string, unknown>
      [string]: Record<string, unknown>
    }:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDefaultsProvider", children, **kwargs)
        self._attr_names += [
            "disabled",
            "root",
            "reset",
            "scoped",
            "defaults",
        ]
        self._event_names += []


class VDialog(HtmlElement):
    """
    Vuetify's VDialog component. See more info and examples |VDialog_vuetify_link|.

    .. |VDialog_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param location: MISSING DESCRIPTION
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param absolute: Applies **position: absolute** to the content element.
    :type boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param z_index: The z-index used for the component
    :type string | number:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param activator: See description |VDialog_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |VDialog_vuetify_link|.
    :type any:
    :param no_click_animation: Disables the bounce effect when clicking outside of a `v-dialog`'s content when using the **persistent** prop.
    :type boolean:
    :param persistent: Clicking outside of the element or pressing **esc** key will not deactivate it.
    :type boolean:
    :param scrim: Accepts true/false to enable background, and string to define color.
    :type string | boolean:
    :param activator_props: See description |VDialog_vuetify_link|.
    :type {}:
    :param open_on_click: See description |VDialog_vuetify_link|.
    :type boolean:
    :param open_on_hover: Designates whether component should activate when its activator is hovered.
    :type boolean:
    :param open_on_focus: See description |VDialog_vuetify_link|.
    :type boolean:
    :param close_on_content_click: Closes component when you click on its content
    :type boolean:
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :type string | number:
    :param location_strategy: A function used to specifies how the component should position relative to its activator
    :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param origin: See description |VDialog_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
    :param offset: A single value that offsets content away from the target based upon what side it is on
    :type string | number | number[]:
    :param scroll_strategy: See description |VDialog_vuetify_link|.
    :type 'close' | 'block' | 'none' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
    :param transition: See description |VDialog_vuetify_link|.
    :type string | { component: Component }:
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :type string | boolean | Element:
    :param fullscreen: Changes layout for fullscreen display.
    :type boolean:
    :param retain_focus: Tab focus will return to the first child of the dialog by default. Disable this when using external tools that require focus such as TinyMCE or vue-clipboard.
    :type boolean:
    :param scrollable: See description |VDialog_vuetify_link|.
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
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
            ("z_index", "zIndex"),
            "disabled",
            "eager",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            ("no_click_animation", "noClickAnimation"),
            "persistent",
            "scrim",
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
        ]


class VDialogBottomTransition(HtmlElement):
    """
    Vuetify's VDialogBottomTransition component. See more info and examples |VDialogBottomTransition_vuetify_link|.

    .. |VDialogBottomTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog-bottom-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VDialogBottomTransition_vuetify_link|.
    :type string:
    :param mode: See description |VDialogBottomTransition_vuetify_link|.
    :type string:
    :param group: See description |VDialogBottomTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VDialogBottomTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialogBottomTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VDialogTopTransition(HtmlElement):
    """
    Vuetify's VDialogTopTransition component. See more info and examples |VDialogTopTransition_vuetify_link|.

    .. |VDialogTopTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog-top-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VDialogTopTransition_vuetify_link|.
    :type string:
    :param mode: See description |VDialogTopTransition_vuetify_link|.
    :type string:
    :param group: See description |VDialogTopTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VDialogTopTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialogTopTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VDialogTransition(HtmlElement):
    """
    Vuetify's VDialogTransition component. See more info and examples |VDialogTransition_vuetify_link|.

    .. |VDialogTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog-transition" target="_blank">here</a>


    :param target: See description |VDialogTransition_vuetify_link|.
    :type HTMLElement:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialogTransition", children, **kwargs)
        self._attr_names += [
            "target",
        ]
        self._event_names += []


class VDivider(HtmlElement):
    """
    Vuetify's VDivider component. See more info and examples |VDivider_vuetify_link|.

    .. |VDivider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-divider" target="_blank">here</a>


    :param length: Sets the dividers length. Default unit is px.
    :type string | number:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VDivider_vuetify_link|.
    :type string:
    :param vertical: Displays dividers vertically.
    :type boolean:
    :param inset: Adds indentation (72px) for **normal** dividers, reduces max height for **vertical**.
    :type boolean:
    :param thickness: Sets the dividers thickness. Default unit is px.
    :type string | number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDivider", children, **kwargs)
        self._attr_names += [
            "length",
            "theme",
            "color",
            "vertical",
            "inset",
            "thickness",
        ]
        self._event_names += []


class VExpandTransition(HtmlElement):
    """
    Vuetify's VExpandTransition component. See more info and examples |VExpandTransition_vuetify_link|.

    .. |VExpandTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expand-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param mode: See description |VExpandTransition_vuetify_link|.
    :type 'default' | 'in-out' | 'out-in':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpandTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
        ]
        self._event_names += []


class VExpandXTransition(HtmlElement):
    """
    Vuetify's VExpandXTransition component. See more info and examples |VExpandXTransition_vuetify_link|.

    .. |VExpandXTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expand-x-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param mode: See description |VExpandXTransition_vuetify_link|.
    :type 'default' | 'in-out' | 'out-in':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpandXTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "mode",
        ]
        self._event_names += []


class VExpansionPanel(HtmlElement):
    """
      Vuetify's VExpansionPanel component. See more info and examples |VExpansionPanel_vuetify_link|.

      .. |VExpansionPanel_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-expansion-panel" target="_blank">here</a>


      :param title: See description |VExpansionPanel_vuetify_link|.
      :type string:
      :param text: Specify content text for the component.
      :type string:
      :param elevation: See description |VExpansionPanel_vuetify_link|.
      :type string | number:
      :param rounded: See description |VExpansionPanel_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param color: See description |VExpansionPanel_vuetify_link|.
      :type string:
      :param value: Controls the opened/closed state of content
      :type any:
      :param ripple: See description |VExpansionPanel_vuetify_link|.
      :type boolean | { class: string }:
      :param disabled: Disables the expansion-panel content
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
      :type boolean:
      :param readonly: Makes the expansion-panel content read only.
      :type boolean:
      :param bg_color: See description |VExpansionPanel_vuetify_link|.
      :type string:
      :param hide_actions: See description |VExpansionPanel_vuetify_link|.
      :type boolean:
      :param expand_icon: See description |VExpansionPanel_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param collapse_icon: See description |VExpansionPanel_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:

      Events

      :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanel", children, **kwargs)
        self._attr_names += [
            "title",
            "text",
            "elevation",
            "rounded",
            "tag",
            "color",
            "value",
            "ripple",
            "disabled",
            ("selected_class", "selectedClass"),
            "eager",
            "readonly",
            ("bg_color", "bgColor"),
            ("hide_actions", "hideActions"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VExpansionPanelText(HtmlElement):
    """
    Vuetify's VExpansionPanelText component. See more info and examples |VExpansionPanelText_vuetify_link|.

    .. |VExpansionPanelText_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expansion-panel-text" target="_blank">here</a>


    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanelText", children, **kwargs)
        self._attr_names += [
            "eager",
        ]
        self._event_names += []


class VExpansionPanelTitle(HtmlElement):
    """
      Vuetify's VExpansionPanelTitle component. See more info and examples |VExpansionPanelTitle_vuetify_link|.

      .. |VExpansionPanelTitle_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-expansion-panel-title" target="_blank">here</a>


      :param color: See description |VExpansionPanelTitle_vuetify_link|.
      :type string:
      :param ripple: See description |VExpansionPanelTitle_vuetify_link|.
      :type boolean | { class: string }:
      :param readonly: See description |VExpansionPanelTitle_vuetify_link|.
      :type boolean:
      :param hide_actions: See description |VExpansionPanelTitle_vuetify_link|.
      :type boolean:
      :param expand_icon: See description |VExpansionPanelTitle_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param collapse_icon: See description |VExpansionPanelTitle_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanelTitle", children, **kwargs)
        self._attr_names += [
            "color",
            "ripple",
            "readonly",
            ("hide_actions", "hideActions"),
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
        ]
        self._event_names += []


class VExpansionPanels(HtmlElement):
    """
    Vuetify's VExpansionPanels component. See more info and examples |VExpansionPanels_vuetify_link|.

    .. |VExpansionPanels_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expansion-panels" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VExpansionPanels_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type 'default' | 'inset' | 'accordion' | 'popout':
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param readonly: Makes the entire expansion-panel read only.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanels", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "tag",
            "theme",
            "color",
            "variant",
            "disabled",
            ("selected_class", "selectedClass"),
            "multiple",
            "readonly",
            "max",
            "mandatory",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VFabTransition(HtmlElement):
    """
    Vuetify's VFabTransition component. See more info and examples |VFabTransition_vuetify_link|.

    .. |VFabTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-fab-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VFabTransition_vuetify_link|.
    :type string:
    :param mode: See description |VFabTransition_vuetify_link|.
    :type string:
    :param group: See description |VFabTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VFabTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFabTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VFadeTransition(HtmlElement):
    """
    Vuetify's VFadeTransition component. See more info and examples |VFadeTransition_vuetify_link|.

    .. |VFadeTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-fade-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VFadeTransition_vuetify_link|.
    :type string:
    :param mode: See description |VFadeTransition_vuetify_link|.
    :type string:
    :param group: See description |VFadeTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VFadeTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFadeTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VField(HtmlElement):
    """
      Vuetify's VField component. See more info and examples |VField_vuetify_link|.

      .. |VField_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-field" target="_blank">here</a>


      :param flat: MISSING DESCRIPTION
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type unknown:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param reverse: Reverses the orientation
      :type boolean:
      :param rounded: See description |VField_vuetify_link|.
      :type string | number | boolean:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VField_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type | 'outlined'
    | 'plain'
    | 'underlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled':
      :param id: Sets the DOM id on the component
      :type string:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component
      :type boolean:
      :param disabled: Removes the ability to click or target the input
      :type boolean:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param label: See description |VField_vuetify_link|.
      :type string:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center
      :type boolean:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param append_inner_icon: See description |VField_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param bg_color: See description |VField_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared
      :type boolean:
      :param clear_icon: The icon used when the **clerable** prop is set to true
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param base_color: Sets the color of the input when it is not focused
      :type string:
      :param dirty: Manually apply the dirty state styling
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover)
      :type boolean:
      :param prepend_inner_icon: See description |VField_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param single_line: Label does not move on focus/dirty
      :type boolean:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param update_focused: Emitted when the input is focused or blurred
      :param click_clear: Emitted when clearable icon clicked
      :param click_appendInner: Emitted when appended inner icon is clicked
      :param click_prependInner: Emitted when prepended inner icon is clicked
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VField", children, **kwargs)
        self._attr_names += [
            "flat",
            ("model_value", "modelValue"),
            "error",
            "reverse",
            "rounded",
            "theme",
            "color",
            "variant",
            "id",
            "active",
            "disabled",
            "loading",
            "label",
            ("center_affix", "centerAffix"),
            "focused",
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            ("base_color", "baseColor"),
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
    Vuetify's VFieldLabel component. See more info and examples |VFieldLabel_vuetify_link|.

    .. |VFieldLabel_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-field-label" target="_blank">here</a>


    :param floating: Elevates the label above the slotted content.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFieldLabel", children, **kwargs)
        self._attr_names += [
            "floating",
        ]
        self._event_names += []


class VFileInput(HtmlElement):
    """
      Vuetify's VFileInput component. See more info and examples |VFileInput_vuetify_link|.

      .. |VFileInput_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-file-input" target="_blank">here</a>


      :param flat: MISSING DESCRIPTION
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type File[]:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param reverse: Reverses the orientation
      :type boolean:
      :param rounded: See description |VFileInput_vuetify_link|.
      :type string | number | boolean:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VFileInput_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type | 'outlined'
    | 'plain'
    | 'underlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled':
      :param name: Sets the component's name attribute.
      :type string:
      :param id: Sets the DOM id on the component
      :type string:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component
      :type boolean:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VFileInput_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param disabled: Removes the ability to click or target the input
      :type boolean:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param label: See description |VFileInput_vuetify_link|.
      :type string:
      :param chips: Changes display of selections to chips
      :type boolean:
      :param multiple: Adds the **multiple** attribute to the input, allowing multiple file selections.
      :type boolean:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center
      :type boolean:
      :param hint: See description |VFileInput_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VFileInput_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: Changes the direction of the input
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':
      :param append_inner_icon: See description |VFileInput_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param bg_color: See description |VFileInput_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared
      :type boolean:
      :param clear_icon: The icon used when the **clerable** prop is set to true
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param base_color: Sets the color of the input when it is not focused
      :type string:
      :param dirty: Manually apply the dirty state styling
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover)
      :type boolean:
      :param prepend_inner_icon: See description |VFileInput_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param single_line: Label does not move on focus/dirty
      :type boolean:
      :param counter: See description |VFileInput_vuetify_link|.
      :type boolean:
      :param counter_size_string: See description |VFileInput_vuetify_link|.
      :type string:
      :param counter_string: See description |VFileInput_vuetify_link|.
      :type string:
      :param show_size: Sets the displayed size of selected file(s). When using **true** will default to _1000_ displaying (**kB, MB, GB**) while _1024_ will display (**KiB, MiB, GiB**).
      :type boolean | 1000 | 1024:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: Emitted when prepended icon is clicked
      :param click_append: Emitted when append icon is clicked
      :param update_focused: Emitted when the input is focused or blurred
      :param click_clear: Emitted when clearable icon clicked
      :param click_appendInner: Emitted when appended inner icon is clicked
      :param click_prependInner: Emitted when prepended inner icon is clicked
      :param click_control: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-file-input.json))
      :param mousedown_control: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFileInput", children, **kwargs)
        self._attr_names += [
            "flat",
            ("model_value", "modelValue"),
            "error",
            "density",
            "reverse",
            "rounded",
            "theme",
            "color",
            "variant",
            "name",
            "id",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "disabled",
            "loading",
            "label",
            "chips",
            "multiple",
            ("center_affix", "centerAffix"),
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
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            ("base_color", "baseColor"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "counter",
            ("counter_size_string", "counterSizeString"),
            ("counter_string", "counterString"),
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


class VFooter(HtmlElement):
    """
    Vuetify's VFooter component. See more info and examples |VFooter_vuetify_link|.

    .. |VFooter_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-footer" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param height: See description |VFooter_vuetify_link|.
    :type string | number:
    :param elevation: See description |VFooter_vuetify_link|.
    :type string | number:
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param rounded: See description |VFooter_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VFooter_vuetify_link|.
    :type string:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param app: Determines the position of the footer. If true, the footer would be given a fixed position at the bottom of the viewport. If false, the footer is set to the bottom of the page
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFooter", children, **kwargs)
        self._attr_names += [
            "border",
            "height",
            "elevation",
            "absolute",
            "rounded",
            "tag",
            "theme",
            "color",
            "name",
            "order",
            "app",
        ]
        self._event_names += []


class VForm(HtmlElement):
    """
      Vuetify's VForm component. See more info and examples |VForm_vuetify_link|.

      .. |VForm_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-form" target="_blank">here</a>


      :param model_value: The value representing the validity of the form. If the value is `null` then no validation has taken place yet, or the form has been reset. Otherwise the value will be a `boolean` that indicates if validation has passed or not.
      :type boolean:
      :param disabled: Puts all children inputs into a disabled state
      :type boolean:
      :param readonly: Puts all children inputs into a readonly state.
      :type boolean:
      :param validate_on: Changes the events in which validation occurs.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param fast_fail: Stop validation as soon as any rules fail.
      :type boolean:

      Events

      :param update_modelValue: Event emitted when the form's validity changes
      :param submit: Emitted when form is submitted
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VForm", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "disabled",
            "readonly",
            ("validate_on", "validateOn"),
            ("fast_fail", "fastFail"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "submit",
        ]


class VHover(HtmlElement):
    """
    Vuetify's VHover component. See more info and examples |VHover_vuetify_link|.

    .. |VHover_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-hover" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param disabled: Removes hover functionality
    :type boolean:
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :type string | number:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
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
      Vuetify's VIcon component. See more info and examples |VIcon_vuetify_link|.

      .. |VIcon_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-icon" target="_blank">here</a>


      :param end: Applies margin at the start of the component.
      :type boolean:
      :param start: Applies margin at the end of the component.
      :type boolean:
      :param icon: See description |VIcon_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VIcon_vuetify_link|.
      :type string:
      :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
      :type string | number:

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
            "size",
        ]
        self._event_names += []


class VImg(HtmlElement):
    """
      Vuetify's VImg component. See more info and examples |VImg_vuetify_link|.

      .. |VImg_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-img" target="_blank">here</a>


      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
      :type boolean:
      :param content_class: Apply a custom class to the internal content element.
      :type string:
      :param transition: See description |VImg_vuetify_link|.
      :type string:
      :param options: See description |VImg_vuetify_link|.
      :type { root: any; rootMargin: any; threshold: any }:
      :param inline: Display as an inline element instead of a block, also disables flex-grow.
      :type boolean:
      :param alt: Alternate text for screen readers. Leave empty for decorative images.
      :type string:
      :param cover: Resizes the background image to cover the entire container.
      :type boolean:
      :param gradient: See description |VImg_vuetify_link|.
      :type string:
      :param lazy_src: See description |VImg_vuetify_link|.
      :type string:
      :param sizes: See description |VImg_vuetify_link|.
      :type string:
      :param src: The image URL. This prop is mandatory.
      :type | string
    | { src: string; srcset: string; lazySrc: string; aspect: number }:
      :param srcset: See description |VImg_vuetify_link|.
      :type string:
      :param aspect_ratio: Calculated as `width/height`, so for a 1920x1080px image this will be `1.7778`. Will be calculated automatically if omitted.
      :type string | number:

      Events

      :param error: Emitted if the image fails to load
      :param loadstart: Emitted when the image starts to load
      :param load: Emitted when the image is loaded
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
            "eager",
            ("content_class", "contentClass"),
            "transition",
            "options",
            "inline",
            "alt",
            "cover",
            "gradient",
            ("lazy_src", "lazySrc"),
            "sizes",
            "src",
            "srcset",
            ("aspect_ratio", "aspectRatio"),
        ]
        self._event_names += [
            "error",
            "loadstart",
            "load",
        ]


class VInfiniteScroll(HtmlElement):
    """
    Vuetify's VInfiniteScroll component. See more info and examples |VInfiniteScroll_vuetify_link|.

    .. |VInfiniteScroll_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-infinite-scroll" target="_blank">here</a>


    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param color: See description |VInfiniteScroll_vuetify_link|.
    :type string:
    :param direction: Specifies if scroller is **vertical** or **horizontal**.
    :type 'horizontal' | 'vertical':
    :param mode: Specifies if content should load automatically when scrolling (**intersect**) or manually (**manual**).
    :type 'intersect' | 'manual':
    :param side: Specifies the side where new content should appear. Either the **start**, **end**, or **both** sides.
    :type 'end' | 'start' | 'both':
    :param margin: Value sent to the intersection observer. Will make the observer trigger earlier, by the margin (px) value supplied.
    :type string | number:
    :param load_more_text: Text shown in default load more button, when in manual mode.
    :type string:
    :param empty_text: Text shown when there is no more content to load.
    :type string:

    Events

    :param load: Emitted when reaching the start / end threshold, or if triggered when using manual mode.
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
            "direction",
            "mode",
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
      Vuetify's VInput component. See more info and examples |VInput_vuetify_link|.

      .. |VInput_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-input" target="_blank">here</a>


      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param name: Sets the component's name attribute.
      :type string:
      :param id: MISSING DESCRIPTION
      :type string:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VInput_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param label: See description |VInput_vuetify_link|.
      :type string:
      :param center_affix: MISSING DESCRIPTION
      :type boolean:
      :param hint: See description |VInput_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VInput_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: Changes the direction of the input
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: Emitted when prepended icon is clicked
      :param click_append: Emitted when appended icon is clicked
      :param update_focused: Event that is emitted when the component's focus state changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VInput", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "error",
            "density",
            "name",
            "id",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "disabled",
            "label",
            ("center_affix", "centerAffix"),
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
    Vuetify's VItem component. See more info and examples |VItem_vuetify_link|.

    .. |VItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-item" target="_blank">here</a>


    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:

    Events

    :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VItem", children, **kwargs)
        self._attr_names += [
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VItemGroup(HtmlElement):
    """
    Vuetify's VItemGroup component. See more info and examples |VItemGroup_vuetify_link|.

    .. |VItemGroup_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-item-group" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param selected_class: Configure the selected CSS class. This class will be available in `v-item` default scoped slot.
    :type string:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VItemGroup", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "tag",
            "theme",
            "disabled",
            ("selected_class", "selectedClass"),
            "multiple",
            "max",
            "mandatory",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VKbd(HtmlElement):
    """
    Vuetify's VKbd component. See more info and examples |VKbd_vuetify_link|.

    .. |VKbd_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-kbd" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VKbd", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VLabel(HtmlElement):
    """
    Vuetify's VLabel component. See more info and examples |VLabel_vuetify_link|.

    .. |VLabel_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-label" target="_blank">here</a>


    :param text: Specify content text for the component.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param clickable: See description |VLabel_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLabel", children, **kwargs)
        self._attr_names += [
            "text",
            "theme",
            "clickable",
        ]
        self._event_names += []


class VLayout(HtmlElement):
    """
    Vuetify's VLayout component. See more info and examples |VLayout_vuetify_link|.

    .. |VLayout_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-layout" target="_blank">here</a>


    :param full_height: Sets the component height to 100%
    :type boolean:
    :param overlaps: See description |VLayout_vuetify_link|.
    :type string[]:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLayout", children, **kwargs)
        self._attr_names += [
            ("full_height", "fullHeight"),
            "overlaps",
        ]
        self._event_names += []


class VLayoutItem(HtmlElement):
    """
    Vuetify's VLayoutItem component. See more info and examples |VLayoutItem_vuetify_link|.

    .. |VLayoutItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-layout-item" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param position: See description |VLayoutItem_vuetify_link|.
    :type 'top' | 'bottom' | 'left' | 'right':
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param size: See description |VLayoutItem_vuetify_link|.
    :type string | number:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:

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
    Vuetify's VLazy component. See more info and examples |VLazy_vuetify_link|.

    .. |VLazy_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-lazy" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param transition: See description |VLazy_vuetify_link|.
    :type string:
    :param options: See description |VLazy_vuetify_link|.
    :type { root: any; rootMargin: any; threshold: any }:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLazy", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "tag",
            "transition",
            "options",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VLigatureIcon(HtmlElement):
    """
      Vuetify's VLigatureIcon component. See more info and examples |VLigatureIcon_vuetify_link|.

      .. |VLigatureIcon_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-ligature-icon" target="_blank">here</a>


      :param icon: See description |VLigatureIcon_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param tag: Specify a custom tag used on the root element
      :type string:

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
        Vuetify's VList component. See more info and examples |VList_vuetify_link|.

        .. |VList_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-list" target="_blank">here</a>


        :param border: Applies border styles to component.
        :type string | number | boolean:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param height: Sets the height for the component.
        :type string | number:
        :param max_height: Sets the maximum height for the component.
        :type string | number:
        :param max_width: Sets the maximum width for the component.
        :type string | number:
        :param min_height: Sets the minimum height for the component.
        :type string | number:
        :param min_width: Sets the minimum width for the component.
        :type string | number:
        :param width: Sets the width for the component.
        :type string | number:
        :param elevation: See description |VList_vuetify_link|.
        :type string | number:
        :param rounded: See description |VList_vuetify_link|.
        :type string | number | boolean:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children
        :type string:
        :param color: See description |VList_vuetify_link|.
        :type string:
        :param variant: Applies a distinct style to the component
        :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
        :param items: An array of strings or objects used for automatically generating children components
        :type unknown[]:
        :param disabled: Puts all children inputs into a disabled state
        :type boolean:
        :param item_title: Property on supplied `items` that contains its title
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param item_value: Property on supplied `items` that contains its value
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param item_children: Property on supplied `items` that contains its children
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**
        :type boolean:
        :param bg_color: See description |VList_vuetify_link|.
        :type string:
        :param base_color: MISSING DESCRIPTION
        :type string:
        :param lines: See description |VList_vuetify_link|.
        :type false | 'one' | 'two' | 'three':
        :param mandatory: Forces at least one item to always be selected (if available).
        :type boolean:
        :param active_class: The class applied to the component when it is in an active state
        :type string:
        :param active_color: The applied color when the component is in an active state
        :type string:
        :param selected: An array containing the values of currently selected items. Can be two-way bound with `v-model:selected`.
        :type unknown[]:
        :param select_strategy: Affects how items with children behave when selected.
    - **leaf:** Only leaf nodes (items without children) can be selected.
    - **independent:** All nodes can be selected whether they have children or not.
    - **classic:** Selecting a parent node will cause all children to be selected, parent nodes will be displayed as selected if all their descendants are selected. Only leaf nodes will be added to the model.
        :type | 'single-leaf'
      | 'leaf'
      | 'independent'
      | 'single-independent'
      | 'classic'
      | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/selectStrategies.ts#L5-L12" target="_blank">SelectStrategyFn</a>:
        :param nav: See description |VList_vuetify_link|.
        :type boolean:
        :param open_strategy: Affects how items with children behave when expanded.
    - **multiple:** Any number of groups can be open at once.
    - **single:** Only one group at each level can be open, opening a group will cause others to close.
    - **list:** Multiple, but all other groups will close when an item is selected.
        :type | 'multiple'
      | 'single'
      | 'list'
      | { open: <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/openStrategies.ts#L1-L8" target="_blank">OpenStrategyFn</a>; select: <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/openStrategies.ts#L10-L18" target="_blank">OpenSelectStrategyFn</a> }:
        :param opened: An array containing the values of currently opened groups. Can be two-way bound with `v-model:opened`.
        :type unknown[]:
        :param item_type: See description |VList_vuetify_link|.
        :type string:

        Events

        :param update_selected: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-list.json))
        :param update_opened: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-list.json))
        :param click_open: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-list.json))
        :param click_select: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-list.json))
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
            "tag",
            "theme",
            "color",
            "variant",
            "items",
            "disabled",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("bg_color", "bgColor"),
            ("base_color", "baseColor"),
            "lines",
            "mandatory",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
            "selected",
            ("select_strategy", "selectStrategy"),
            "nav",
            ("open_strategy", "openStrategy"),
            "opened",
            ("item_type", "itemType"),
        ]
        self._event_names += [
            ("update_selected", "update:selected"),
            ("update_opened", "update:opened"),
            ("click_open", "click:open"),
            ("click_select", "click:select"),
        ]


class VListGroup(HtmlElement):
    """
      Vuetify's VListGroup component. See more info and examples |VListGroup_vuetify_link|.

      .. |VListGroup_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-list-group" target="_blank">here</a>


      :param title: See description |VListGroup_vuetify_link|.
      :type string:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param color: See description |VListGroup_vuetify_link|.
      :type string:
      :param value: Expands / Collapse the list-group
      :type any:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VListGroup_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param base_color: MISSING DESCRIPTION
      :type string:
      :param active_color: The applied color when the component is in an active state
      :type string:
      :param fluid: See description |VListGroup_vuetify_link|.
      :type boolean:
      :param expand_icon: See description |VListGroup_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param collapse_icon: See description |VListGroup_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param subgroup: See description |VListGroup_vuetify_link|.
      :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListGroup", children, **kwargs)
        self._attr_names += [
            "title",
            "tag",
            "color",
            "value",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            ("base_color", "baseColor"),
            ("active_color", "activeColor"),
            "fluid",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "subgroup",
        ]
        self._event_names += []


class VListImg(HtmlElement):
    """
    Vuetify's VListImg component. See more info and examples |VListImg_vuetify_link|.

    .. |VListImg_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-img" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListImg", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListItem(HtmlElement):
    """
      Vuetify's VListItem component. See more info and examples |VListItem_vuetify_link|.

      .. |VListItem_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-list-item" target="_blank">here</a>


      :param title: Generates a `v-list-item-title` component with the supplied value
      :type string | number | boolean:
      :param border: Applies border styles to component.
      :type string | number | boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param elevation: See description |VListItem_vuetify_link|.
      :type string | number:
      :param rounded: See description |VListItem_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VListItem_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
      :param value: The value used for selection.
      :type any:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component
      :type boolean:
      :param prepend_icon: See description |VListItem_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VListItem_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param ripple: See description |VListItem_vuetify_link|.
      :type boolean | { class: string }:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param href: Designates the component as anchor and applies the **href** attribute.
      :type string:
      :param replace: See description |VListItem_vuetify_link|.
      :type boolean:
      :param exact: See description |VListItem_vuetify_link|.
      :type boolean:
      :param to: See description |VListItem_vuetify_link|.
      :type unknown:
      :param base_color: MISSING DESCRIPTION
      :type string:
      :param link: Designates that the component is a link. This is automatic when using the href or to prop.
      :type boolean:
      :param lines: See description |VListItem_vuetify_link|.
      :type 'one' | 'two' | 'three':
      :param active_class: See description |VListItem_vuetify_link|.
      :type string:
      :param active_color: The applied color when the component is in an active state
      :type string:
      :param subtitle: Specify a subtitle text for the component.
      :type string | number | boolean:
      :param append_avatar: See description |VListItem_vuetify_link|.
      :type string:
      :param prepend_avatar: See description |VListItem_vuetify_link|.
      :type string:
      :param nav: See description |VListItem_vuetify_link|.
      :type boolean:

      Events

      :param clickOnce: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-list-item.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItem", children, **kwargs)
        self._attr_names += [
            "title",
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
            "tag",
            "theme",
            "color",
            "variant",
            "value",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "ripple",
            "disabled",
            "href",
            "replace",
            "exact",
            "to",
            ("base_color", "baseColor"),
            "link",
            "lines",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
            "subtitle",
            ("append_avatar", "appendAvatar"),
            ("prepend_avatar", "prependAvatar"),
            "nav",
        ]
        self._event_names += [
            "click",
            "clickOnce",
        ]


class VListItemAction(HtmlElement):
    """
    Vuetify's VListItemAction component. See more info and examples |VListItemAction_vuetify_link|.

    .. |VListItemAction_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-action" target="_blank">here</a>


    :param end: Applies margin at the start of the component.
    :type boolean:
    :param start: Applies margin at the end of the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:

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
    Vuetify's VListItemMedia component. See more info and examples |VListItemMedia_vuetify_link|.

    .. |VListItemMedia_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-media" target="_blank">here</a>


    :param end: Applies margin at the start of the component.
    :type boolean:
    :param start: Applies margin at the end of the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:

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
    Vuetify's VListItemSubtitle component. See more info and examples |VListItemSubtitle_vuetify_link|.

    .. |VListItemSubtitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-subtitle" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemSubtitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListItemTitle(HtmlElement):
    """
    Vuetify's VListItemTitle component. See more info and examples |VListItemTitle_vuetify_link|.

    .. |VListItemTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemTitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListSubheader(HtmlElement):
    """
    Vuetify's VListSubheader component. See more info and examples |VListSubheader_vuetify_link|.

    .. |VListSubheader_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-subheader" target="_blank">here</a>


    :param title: See description |VListSubheader_vuetify_link|.
    :type string:
    :param sticky: See description |VListSubheader_vuetify_link|.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param color: See description |VListSubheader_vuetify_link|.
    :type string:
    :param inset: See description |VListSubheader_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListSubheader", children, **kwargs)
        self._attr_names += [
            "title",
            "sticky",
            "tag",
            "color",
            "inset",
        ]
        self._event_names += []


class VLocaleProvider(HtmlElement):
    """
    Vuetify's VLocaleProvider component. See more info and examples |VLocaleProvider_vuetify_link|.

    .. |VLocaleProvider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-locale-provider" target="_blank">here</a>


    :param messages: See description |VLocaleProvider_vuetify_link|.
    :type Record<string, any>:
    :param locale: See description |VLocaleProvider_vuetify_link|.
    :type string:
    :param fallback_locale: See description |VLocaleProvider_vuetify_link|.
    :type string:
    :param rtl: See description |VLocaleProvider_vuetify_link|.
    :type boolean:

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
    Vuetify's VMain component. See more info and examples |VMain_vuetify_link|.

    .. |VMain_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-main" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param scrollable: See description |VMain_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMain", children, **kwargs)
        self._attr_names += [
            "tag",
            "scrollable",
        ]
        self._event_names += []


class VMenu(HtmlElement):
    """
    Vuetify's VMenu component. See more info and examples |VMenu_vuetify_link|.

    .. |VMenu_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-menu" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component. Use `auto` to use the activator width
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param location: MISSING DESCRIPTION
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param z_index: The z-index used for the component
    :type string | number:
    :param id: See description |VMenu_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param activator: See description |VMenu_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |VMenu_vuetify_link|.
    :type any:
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :type boolean:
    :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
    :type boolean:
    :param scrim: Accepts true/false to enable background, and string to define color.
    :type string | boolean:
    :param activator_props: See description |VMenu_vuetify_link|.
    :type {}:
    :param open_on_click: Designates whether menu should open on activator click
    :type boolean:
    :param open_on_hover: Designates whether menu should open on activator hover
    :type boolean:
    :param open_on_focus: See description |VMenu_vuetify_link|.
    :type boolean:
    :param close_on_content_click: Designates if menu should close when its content is clicked
    :type boolean:
    :param close_delay: Milliseconds to wait before closing component. Only works with the **open-on-hover** prop
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only works with the **open-on-hover** prop
    :type string | number:
    :param location_strategy: A function used to specifies how the component should position relative to its activator
    :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param origin: See description |VMenu_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
    :param offset: A single value that offsets content away from the target based upon what side it is on
    :type string | number | number[]:
    :param scroll_strategy: See description |VMenu_vuetify_link|.
    :type 'close' | 'block' | 'none' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
    :param transition: See description |VMenu_vuetify_link|.
    :type string | { component: Component }:
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default. Generally not recommended except as a last resort: the default positioning algorithm should handle most scenarios better than is possible without teleporting, and you may have unexpected behavior if the menu ends up as child of its activator.
    :type string | boolean | Element:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMenu", children, **kwargs)
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
            ("z_index", "zIndex"),
            "id",
            "disabled",
            "eager",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            ("no_click_animation", "noClickAnimation"),
            "persistent",
            "scrim",
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


class VMessages(HtmlElement):
    """
      Vuetify's VMessages component. See more info and examples |VMessages_vuetify_link|.

      .. |VMessages_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-messages" target="_blank">here</a>


      :param color: See description |VMessages_vuetify_link|.
      :type string:
      :param active: Determines whether the messages are visible or not
      :type boolean:
      :param transition: See description |VMessages_vuetify_link|.
      :type | string
    | { component: Component; leaveAbsolute: boolean; group: boolean }:
      :param messages: See description |VMessages_vuetify_link|.
      :type string | string[]:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMessages", children, **kwargs)
        self._attr_names += [
            "color",
            "active",
            "transition",
            "messages",
        ]
        self._event_names += []


class VNavigationDrawer(HtmlElement):
    """
    Vuetify's VNavigationDrawer component. See more info and examples |VNavigationDrawer_vuetify_link|.

    .. |VNavigationDrawer_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-navigation-drawer" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param width: Sets the width for the component
    :type string | number:
    :param elevation: See description |VNavigationDrawer_vuetify_link|.
    :type string | number:
    :param location: MISSING DESCRIPTION
    :type 'top' | 'end' | 'bottom' | 'start' | 'left' | 'right':
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param sticky: See description |VNavigationDrawer_vuetify_link|.
    :type boolean:
    :param rounded: See description |VNavigationDrawer_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VNavigationDrawer_vuetify_link|.
    :type string:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param image: Apply a specific background image to the component.
    :type string:
    :param floating: A floating drawer has no visible container (no border-right)
    :type boolean:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param scrim: See description |VNavigationDrawer_vuetify_link|.
    :type string | boolean:
    :param disable_resize_watcher: Will automatically open/close drawer when resized depending if mobile or desktop.
    :type boolean:
    :param disable_route_watcher: Disables opening of navigation drawer when route changes
    :type boolean:
    :param expand_on_hover: Collapses the drawer to a **mini-variant** until hovering with the mouse
    :type boolean:
    :param permanent: The drawer remains visible regardless of screen size
    :type boolean:
    :param rail: Sets the component width to the **rail-width** value.
    :type boolean:
    :param rail_width: Sets the width for the component when `rail` is enabled.
    :type string | number:
    :param temporary: A temporary drawer sits above its application and uses a scrim (overlay) to darken the background
    :type boolean:
    :param touchless: Disable mobile touch functionality
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_rail: Event that is emitted when the rail model changes
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
            "tag",
            "theme",
            "color",
            "name",
            "image",
            "floating",
            "order",
            "scrim",
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
    Vuetify's VNoSsr component. See more info and examples |VNoSsr_vuetify_link|.

    .. |VNoSsr_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-no-ssr" target="_blank">here</a>



    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VNoSsr", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VOverlay(HtmlElement):
    """
    Vuetify's VOverlay component. See more info and examples |VOverlay_vuetify_link|.

    .. |VOverlay_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-overlay" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param location: MISSING DESCRIPTION
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param absolute: Applies **position: absolute** to the content element.
    :type boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param z_index: The z-index used for the component
    :type string | number:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param activator: See description |VOverlay_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |VOverlay_vuetify_link|.
    :type any:
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :type boolean:
    :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
    :type boolean:
    :param scrim: Accepts true/false to enable background, and string to define color.
    :type string | boolean:
    :param activator_props: See description |VOverlay_vuetify_link|.
    :type {}:
    :param open_on_click: See description |VOverlay_vuetify_link|.
    :type boolean:
    :param open_on_hover: See description |VOverlay_vuetify_link|.
    :type boolean:
    :param open_on_focus: See description |VOverlay_vuetify_link|.
    :type boolean:
    :param close_on_content_click: Closes component when you click on its content
    :type boolean:
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :type string | number:
    :param location_strategy: A function used to specifies how the component should position relative to its activator
    :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param origin: See description |VOverlay_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
    :param offset: A single value that offsets content away from the target based upon what side it is on
    :type string | number | number[]:
    :param scroll_strategy: See description |VOverlay_vuetify_link|.
    :type 'close' | 'block' | 'none' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
    :param transition: See description |VOverlay_vuetify_link|.
    :type string:
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :type string | boolean | Element:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param click_outside: Event that fires when clicking outside an active overlay.
    :param afterLeave: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-overlay.json))
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
            ("z_index", "zIndex"),
            "disabled",
            "eager",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            ("no_click_animation", "noClickAnimation"),
            "persistent",
            "scrim",
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
            "afterLeave",
        ]


class VPagination(HtmlElement):
    """
      Vuetify's VPagination component. See more info and examples |VPagination_vuetify_link|.

      .. |VPagination_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-pagination" target="_blank">here</a>


      :param length: The number of pages
      :type string | number:
      :param border: Applies border styles to component.
      :type string | number | boolean:
      :param start: Specify the starting page
      :type string | number:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type number:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param elevation: See description |VPagination_vuetify_link|.
      :type string | number:
      :param rounded: See description |VPagination_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VPagination_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
      :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
      :type string | number:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param active_color: The applied color when the component is in an active state
      :type string:
      :param next_icon: The icon to use for the next button
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param prev_icon: The icon to use for the prev button
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param first_icon: The icon to use for the first button
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param last_icon: The icon to use for the last button
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param aria_label: Label for the root element
      :type string:
      :param total_visible: Specify the total visible pagination numbers
      :type string | number:
      :param page_aria_label: Label for each page button
      :type string:
      :param current_page_aria_label: Label for the currently selected page
      :type string:
      :param first_aria_label: Label for the go to first button
      :type string:
      :param previous_aria_label: Label for the previous button
      :type string:
      :param next_aria_label: Label for the next button
      :type string:
      :param last_aria_label: Label for the go to last button
      :type string:
      :param ellipsis: Text to show between page buttons when truncating the list
      :type string:
      :param show_first_last_page: Show buttons for going to first and last page
      :type boolean:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param next: Emitted when clicking on go to next button
      :param prev: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-pagination.json))
      :param first: Emitted when clicking on go to first button
      :param last: Emitted when clicking on go to last button
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
            "tag",
            "theme",
            "color",
            "variant",
            "size",
            "disabled",
            ("active_color", "activeColor"),
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
    Vuetify's VParallax component. See more info and examples |VParallax_vuetify_link|.

    .. |VParallax_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-parallax" target="_blank">here</a>


    :param scale: See description |VParallax_vuetify_link|.
    :type string | number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VParallax", children, **kwargs)
        self._attr_names += [
            "scale",
        ]
        self._event_names += []


class VPicker(HtmlElement):
    """
    Vuetify's VPicker component. See more info and examples |VPicker_vuetify_link|.

    .. |VPicker_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-picker" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param elevation: See description |VPicker_vuetify_link|.
    :type string | number:
    :param location: Specifies the component's location. Can combine by using a space separated string
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: MISSING DESCRIPTION
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VPicker_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param landscape: MISSING DESCRIPTION
    :type boolean:

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
            "tag",
            "theme",
            "landscape",
        ]
        self._event_names += []


class VPickerTitle(HtmlElement):
    """
    Vuetify's VPickerTitle component. See more info and examples |VPickerTitle_vuetify_link|.

    .. |VPickerTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-picker-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPickerTitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VProgressCircular(HtmlElement):
    """
    Vuetify's VProgressCircular component. See more info and examples |VProgressCircular_vuetify_link|.

    .. |VProgressCircular_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-progress-circular" target="_blank">here</a>


    :param model_value: The percentage value for current progress
    :type string | number:
    :param width: Sets the stroke of the circle in pixels
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VProgressCircular_vuetify_link|.
    :type string:
    :param size: Sets the diameter of the circle in pixels
    :type string | number:
    :param bg_color: See description |VProgressCircular_vuetify_link|.
    :type string:
    :param indeterminate: Constantly animates, use when loading progress is unknown. If set to the string `'disable-shrink'` it will use a simpler animation that does not run on the main thread.
    :type boolean | 'disable-shrink':
    :param rotate: Rotates the circle start point in degrees
    :type string | number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VProgressCircular", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "width",
            "tag",
            "theme",
            "color",
            "size",
            ("bg_color", "bgColor"),
            "indeterminate",
            "rotate",
        ]
        self._event_names += []


class VProgressLinear(HtmlElement):
    """
    Vuetify's VProgressLinear component. See more info and examples |VProgressLinear_vuetify_link|.

    .. |VProgressLinear_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-progress-linear" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type string | number:
    :param height: Sets the height for the component
    :type string | number:
    :param reverse: Displays reversed progress (right to left in LTR mode and left to right in RTL)
    :type boolean:
    :param location: Specifies the component's location. Can combine by using a space separated string
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param absolute: Applies position: absolute to the component
    :type boolean:
    :param rounded: See description |VProgressLinear_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VProgressLinear_vuetify_link|.
    :type string:
    :param active: Reduce the height to 0, hiding component
    :type boolean:
    :param bg_color: See description |VProgressLinear_vuetify_link|.
    :type string:
    :param max: Sets the maximum value the progress can reach
    :type string | number:
    :param indeterminate: Constantly animates, use when loading progress is unknown.
    :type boolean:
    :param clickable: Clicking on the progress track will automatically set the value
    :type boolean:
    :param bg_opacity: Background opacity, if null it defaults to 0.3 if background color is not specified or 1 otherwise
    :type string | number:
    :param buffer_value: The percentage value for the buffer
    :type string | number:
    :param stream: An alternative style for portraying loading that works in tandem with **buffer-value**
    :type boolean:
    :param striped: Adds a stripe background to the filled portion of the progress component
    :type boolean:
    :param rounded_bar: Applies a border radius to the progress bar
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VProgressLinear", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "height",
            "reverse",
            "location",
            "absolute",
            "rounded",
            "tag",
            "theme",
            "color",
            "active",
            ("bg_color", "bgColor"),
            "max",
            "indeterminate",
            "clickable",
            ("bg_opacity", "bgOpacity"),
            ("buffer_value", "bufferValue"),
            "stream",
            "striped",
            ("rounded_bar", "roundedBar"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VRadio(HtmlElement):
    """
      Vuetify's VRadio component. See more info and examples |VRadio_vuetify_link|.

      .. |VRadio_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-radio" target="_blank">here</a>


      :param type: MISSING DESCRIPTION
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: MISSING DESCRIPTION
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VRadio_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param id: MISSING DESCRIPTION
      :type string:
      :param ripple: See description |VRadio_vuetify_link|.
      :type boolean:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param label: See description |VRadio_vuetify_link|.
      :type string:
      :param multiple: MISSING DESCRIPTION
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm used for values
      :type (a: any, b: any) => boolean:
      :param readonly: MISSING DESCRIPTION
      :type boolean:
      :param inline: MISSING DESCRIPTION
      :type boolean:
      :param true_value: Sets value for truthy state
      :type any:
      :param false_value: Sets value for falsy state
      :type any:
      :param defaults_target: MISSING DESCRIPTION
      :type string:
      :param false_icon: The icon used when inactive
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param true_icon: The icon used when active
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:

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
            "value",
            "id",
            "ripple",
            "disabled",
            "label",
            "multiple",
            ("value_comparator", "valueComparator"),
            "readonly",
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
      Vuetify's VRadioGroup component. See more info and examples |VRadioGroup_vuetify_link|.

      .. |VRadioGroup_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-radio-group" target="_blank">here</a>


      :param type: See description |VRadioGroup_vuetify_link|.
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: See description |VRadioGroup_vuetify_link|.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VRadioGroup_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param id: MISSING DESCRIPTION
      :type string:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VRadioGroup_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param ripple: See description |VRadioGroup_vuetify_link|.
      :type boolean:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param label: See description |VRadioGroup_vuetify_link|.
      :type string:
      :param value_comparator: Apply a custom comparison algorithm used for values
      :type (a: any, b: any) => boolean:
      :param center_affix: MISSING DESCRIPTION
      :type boolean:
      :param hint: See description |VRadioGroup_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VRadioGroup_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: Changes the direction of the input
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':
      :param inline: Displays radio buttons in row
      :type boolean:
      :param defaults_target: MISSING DESCRIPTION
      :type string:
      :param false_icon: See description |VRadioGroup_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param true_icon: See description |VRadioGroup_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-radio-group.json))
      :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-radio-group.json))
      :param update_focused: Event that is emitted when the component's focus state changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRadioGroup", children, **kwargs)
        self._attr_names += [
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "height",
            "theme",
            "color",
            "name",
            "id",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "ripple",
            "disabled",
            "label",
            ("value_comparator", "valueComparator"),
            ("center_affix", "centerAffix"),
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
      Vuetify's VRangeSlider component. See more info and examples |VRangeSlider_vuetify_link|.

      .. |VRangeSlider_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-range-slider" target="_blank">here</a>


      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type number[]:
      :param error: See description |VRangeSlider_vuetify_link|.
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param reverse: See description |VRangeSlider_vuetify_link|.
      :type boolean:
      :param elevation: See description |VRangeSlider_vuetify_link|.
      :type string | number:
      :param rounded: See description |VRangeSlider_vuetify_link|.
      :type string | number | boolean:
      :param color: See description |VRangeSlider_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param id: MISSING DESCRIPTION
      :type string:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VRangeSlider_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param label: See description |VRangeSlider_vuetify_link|.
      :type string:
      :param center_affix: MISSING DESCRIPTION
      :type boolean:
      :param hint: See description |VRangeSlider_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VRangeSlider_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: See description |VRangeSlider_vuetify_link|.
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: See description |VRangeSlider_vuetify_link|.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':
      :param max: See description |VRangeSlider_vuetify_link|.
      :type string | number:
      :param min: See description |VRangeSlider_vuetify_link|.
      :type string | number:
      :param step: See description |VRangeSlider_vuetify_link|.
      :type string | number:
      :param thumb_color: See description |VRangeSlider_vuetify_link|.
      :type string:
      :param thumb_label: See description |VRangeSlider_vuetify_link|.
      :type boolean | 'always':
      :param thumb_size: See description |VRangeSlider_vuetify_link|.
      :type string | number:
      :param show_ticks: See description |VRangeSlider_vuetify_link|.
      :type boolean | 'always':
      :param ticks: See description |VRangeSlider_vuetify_link|.
      :type number[] | Record<number, string>:
      :param tick_size: See description |VRangeSlider_vuetify_link|.
      :type string | number:
      :param track_color: See description |VRangeSlider_vuetify_link|.
      :type string:
      :param track_fill_color: See description |VRangeSlider_vuetify_link|.
      :type string:
      :param track_size: See description |VRangeSlider_vuetify_link|.
      :type string | number:
      :param strict: See description |VRangeSlider_vuetify_link|.
      :type boolean:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-range-slider.json))
      :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-range-slider.json))
      :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-range-slider.json))
      :param end: MISSING DESCRIPTION
      :param start: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRangeSlider", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "error",
            "density",
            "reverse",
            "elevation",
            "rounded",
            "color",
            "name",
            "id",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "disabled",
            "label",
            ("center_affix", "centerAffix"),
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
      Vuetify's VRating component. See more info and examples |VRating_vuetify_link|.

      .. |VRating_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-rating" target="_blank">here</a>


      :param length: The amount of items to show
      :type string | number:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type string | number:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VRating_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
      :type string | number:
      :param ripple: See description |VRating_vuetify_link|.
      :type boolean:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param readonly: Removes all hover effects and pointer events
      :type boolean:
      :param clearable: Allows for the component to be cleared by clicking on the current value
      :type boolean:
      :param active_color: The applied color when the component is in an active state
      :type string:
      :param hover: Provides visual feedback when hovering over icons
      :type boolean:
      :param item_aria_label: See description |VRating_vuetify_link|.
      :type string:
      :param empty_icon: The icon displayed when empty
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param full_icon: The icon displayed when full
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param half_increments: Allows the selection of half increments
      :type boolean:
      :param item_label_position: Position of item labels. Accepts 'top' and 'bottom'.
      :type string:
      :param item_labels: Array of labels to display next to each item.
      :type string[]:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
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
            "size",
            "ripple",
            "disabled",
            "readonly",
            "clearable",
            ("active_color", "activeColor"),
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
    Vuetify's VResponsive component. See more info and examples |VResponsive_vuetify_link|.

    .. |VResponsive_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-responsive" target="_blank">here</a>


    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param content_class: Apply a custom class to the internal content element.
    :type string:
    :param inline: Display as an inline element instead of a block, also disables flex-grow.
    :type boolean:
    :param aspect_ratio: Sets a base aspect ratio, calculated as width/height. This will only set a **minimum** height, the component can still grow if it has a lot of content
    :type string | number:

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
      Vuetify's VRow component. See more info and examples |VRow_vuetify_link|.

      .. |VRow_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-row" target="_blank">here</a>


      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param align: See description |VRow_vuetify_link|.
      :type 'end' | 'start' | 'center' | 'baseline' | 'stretch':
      :param dense: Reduces the gutter between `v-col`s.
      :type boolean:
      :param no_gutters: Removes the gutter between `v-col`s.
      :type boolean:
      :param align_sm: Changes the **align-items** property on small and greater breakpoints.
      :type 'end' | 'start' | 'center' | 'baseline' | 'stretch':
      :param align_md: Changes the **align-items** property on medium and greater breakpoints.
      :type 'end' | 'start' | 'center' | 'baseline' | 'stretch':
      :param align_lg: Changes the **align-items** property on large and greater breakpoints.
      :type 'end' | 'start' | 'center' | 'baseline' | 'stretch':
      :param align_xl: Changes the **align-items** property on extra large and greater breakpoints.
      :type 'end' | 'start' | 'center' | 'baseline' | 'stretch':
      :param align_xxl: MISSING DESCRIPTION
      :type 'end' | 'start' | 'center' | 'baseline' | 'stretch':
      :param justify_sm: Changes the **justify-content** property on small and greater breakpoints.
      :type | 'end'
    | 'start'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify_md: Changes the **justify-content** property on medium and greater breakpoints.
      :type | 'end'
    | 'start'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify_lg: Changes the **justify-content** property on large and greater breakpoints.
      :type | 'end'
    | 'start'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify_xl: Changes the **justify-content** property on extra large and greater breakpoints.
      :type | 'end'
    | 'start'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify_xxl: MISSING DESCRIPTION
      :type | 'end'
    | 'start'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_sm: Changes the **align-content** property on small and greater breakpoints.
      :type | 'end'
    | 'start'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_md: Changes the **align-content** property on medium and greater breakpoints.
      :type | 'end'
    | 'start'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_lg: Changes the **align-content** property on large and greater breakpoints.
      :type | 'end'
    | 'start'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_xl: Changes the **align-content** property on extra large and greater breakpoints.
      :type | 'end'
    | 'start'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_xxl: MISSING DESCRIPTION
      :type | 'end'
    | 'start'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify: See description |VRow_vuetify_link|.
      :type | 'end'
    | 'start'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content: See description |VRow_vuetify_link|.
      :type | 'end'
    | 'start'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':

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
    Vuetify's VScaleTransition component. See more info and examples |VScaleTransition_vuetify_link|.

    .. |VScaleTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scale-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VScaleTransition_vuetify_link|.
    :type string:
    :param mode: See description |VScaleTransition_vuetify_link|.
    :type string:
    :param group: See description |VScaleTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VScaleTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScaleTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VScrollXReverseTransition(HtmlElement):
    """
    Vuetify's VScrollXReverseTransition component. See more info and examples |VScrollXReverseTransition_vuetify_link|.

    .. |VScrollXReverseTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-x-reverse-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VScrollXReverseTransition_vuetify_link|.
    :type string:
    :param mode: See description |VScrollXReverseTransition_vuetify_link|.
    :type string:
    :param group: See description |VScrollXReverseTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VScrollXReverseTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollXReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VScrollXTransition(HtmlElement):
    """
    Vuetify's VScrollXTransition component. See more info and examples |VScrollXTransition_vuetify_link|.

    .. |VScrollXTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-x-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VScrollXTransition_vuetify_link|.
    :type string:
    :param mode: See description |VScrollXTransition_vuetify_link|.
    :type string:
    :param group: See description |VScrollXTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VScrollXTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollXTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VScrollYReverseTransition(HtmlElement):
    """
    Vuetify's VScrollYReverseTransition component. See more info and examples |VScrollYReverseTransition_vuetify_link|.

    .. |VScrollYReverseTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-y-reverse-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VScrollYReverseTransition_vuetify_link|.
    :type string:
    :param mode: See description |VScrollYReverseTransition_vuetify_link|.
    :type string:
    :param group: See description |VScrollYReverseTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VScrollYReverseTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollYReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VScrollYTransition(HtmlElement):
    """
    Vuetify's VScrollYTransition component. See more info and examples |VScrollYTransition_vuetify_link|.

    .. |VScrollYTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-y-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VScrollYTransition_vuetify_link|.
    :type string:
    :param mode: See description |VScrollYTransition_vuetify_link|.
    :type string:
    :param group: See description |VScrollYTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VScrollYTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollYTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSelect(HtmlElement):
    """
      Vuetify's VSelect component. See more info and examples |VSelect_vuetify_link|.

      .. |VSelect_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-select" target="_blank">here</a>


      :param flat: Removes elevation (shadow) added to element when using the **solo** or **solo-inverted** props
      :type boolean:
      :param type: Sets input type
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param reverse: Reverses the orientation
      :type boolean:
      :param rounded: Adds a border radius to the input
      :type string | number | boolean:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VSelect_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type | 'outlined'
    | 'plain'
    | 'underlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled':
      :param name: Sets the component's name attribute.
      :type string:
      :param id: Sets the DOM id on the component
      :type string:
      :param items: Can be an array of objects or array of strings. When using objects, will look for a title, value and disabled keys. This can be changed using the **item-title**, **item-value** and **item-disabled** props.  Objects that have a **header** or **divider** property are considered special cases and generate a list header or divider; these items are not selectable.
      :type any[]:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component
      :type boolean:
      :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VSelect_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param disabled: Removes the ability to click or target the input
      :type boolean:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param label: See description |VSelect_vuetify_link|.
      :type string:
      :param chips: Changes display of selections to chips
      :type boolean:
      :param closable_chips: See description |VSelect_vuetify_link|.
      :type boolean:
      :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
      :type boolean:
      :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
      :type boolean:
      :param hide_selected: Do not display in the select menu items that are already selected
      :type boolean:
      :param menu: Renders with the menu open by default
      :type boolean:
      :param menu_icon: Sets the the spin icon
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param menu_props: See description |VSelect_vuetify_link|.
      :type unknown:
      :param transition: See description |VSelect_vuetify_link|.
      :type string | { component: Component }:
      :param multiple: Changes select to multiple. Accepts array for value
      :type boolean:
      :param no_data_text: Text shown when no items are provided to the component
      :type string:
      :param open_on_clear: When using the **clearable** prop, once cleared, the select menu will either open or stay open, depending on the current state
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm used for values
      :type (a: any, b: any) => boolean:
      :param item_title: Property on supplied `items` that contains its title
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
      :param item_value: See description |VSelect_vuetify_link|.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
      :param item_children: Property on supplied `items` that contains its children
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
      :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
      :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**
      :type boolean:
      :param autofocus: Enables autofocus
      :type boolean:
      :param prefix: Displays prefix text
      :type string:
      :param placeholder: Sets the input’s placeholder text
      :type string:
      :param persistent_placeholder: Forces placeholder to always be visible
      :type boolean:
      :param persistent_counter: Forces counter to always be visible
      :type boolean:
      :param suffix: Displays suffix text
      :type string:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center
      :type boolean:
      :param hint: See description |VSelect_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VSelect_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: Changes the direction of the input
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':
      :param bg_color: See description |VSelect_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared
      :type boolean:
      :param clear_icon: The icon used when the **clerable** prop is set to true
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param base_color: Sets the color of the input when it is not focused
      :type string:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover)
      :type boolean:
      :param prepend_inner_icon: See description |VSelect_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param single_line: Label does not move on focus/dirty
      :type boolean:
      :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
      :type string | number | true:
      :param counter_value: Function returns the counter display text
      :type (value: any) => number:
      :param model_modifiers: **FOR INTERNAL USE ONLY**
      :type Record<string, boolean>:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: Emitted when prepended icon is clicked
      :param click_append: Emitted when append icon is clicked
      :param update_focused: Emitted when the input is focused or blurred
      :param click_clear: Emitted when clearable icon clicked
      :param click_appendInner: Emitted when appended inner icon is clicked
      :param click_prependInner: Emitted when prepended inner icon is clicked
      :param update_menu: Event that is emitted when the component's menu state changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSelect", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            "flat",
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "reverse",
            "rounded",
            "theme",
            "color",
            "variant",
            "name",
            "id",
            "items",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "disabled",
            "loading",
            "label",
            "chips",
            ("closable_chips", "closableChips"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "transition",
            "multiple",
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("value_comparator", "valueComparator"),
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            "autofocus",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("center_affix", "centerAffix"),
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
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            ("base_color", "baseColor"),
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "counter",
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
      Vuetify's VSelectionControl component. See more info and examples |VSelectionControl_vuetify_link|.

      .. |VSelectionControl_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-selection-control" target="_blank">here</a>


      :param type: MISSING DESCRIPTION
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type unknown:
      :param error: MISSING DESCRIPTION
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VSelectionControl_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param id: MISSING DESCRIPTION
      :type string:
      :param ripple: See description |VSelectionControl_vuetify_link|.
      :type boolean:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param label: See description |VSelectionControl_vuetify_link|.
      :type string:
      :param multiple: MISSING DESCRIPTION
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm used for values
      :type (a: any, b: any) => boolean:
      :param readonly: MISSING DESCRIPTION
      :type boolean:
      :param inline: MISSING DESCRIPTION
      :type boolean:
      :param true_value: Sets value for truthy state
      :type any:
      :param false_value: Sets value for falsy state
      :type any:
      :param defaults_target: MISSING DESCRIPTION
      :type string:
      :param false_icon: MISSING DESCRIPTION
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param true_icon: MISSING DESCRIPTION
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
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
            "value",
            "id",
            "ripple",
            "disabled",
            "label",
            "multiple",
            ("value_comparator", "valueComparator"),
            "readonly",
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
      Vuetify's VSelectionControlGroup component. See more info and examples |VSelectionControlGroup_vuetify_link|.

      .. |VSelectionControlGroup_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-selection-control-group" target="_blank">here</a>


      :param type: Provides the default type for children selection controls.
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VSelectionControlGroup_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param id: Sets the DOM id on the component
      :type string:
      :param ripple: See description |VSelectionControlGroup_vuetify_link|.
      :type boolean:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param multiple: Changes select to multiple. Accepts array for value
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm used for values
      :type (a: any, b: any) => boolean:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param inline: Puts children inputs into a row.
      :type boolean:
      :param defaults_target: The target component to provide defaults values for.
      :type string:
      :param false_icon: The icon used when inactive
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param true_icon: The icon used when active
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
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
            "id",
            "ripple",
            "disabled",
            "multiple",
            ("value_comparator", "valueComparator"),
            "readonly",
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
    Vuetify's VSheet component. See more info and examples |VSheet_vuetify_link|.

    .. |VSheet_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-sheet" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param elevation: See description |VSheet_vuetify_link|.
    :type string | number:
    :param location: Specifies the component's location. Can combine by using a space separated string
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: MISSING DESCRIPTION
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VSheet_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VSheet_vuetify_link|.
    :type string:

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
            "tag",
            "theme",
            "color",
        ]
        self._event_names += []


class VSkeletonLoader(HtmlElement):
    """
    Vuetify's VSkeletonLoader component. See more info and examples |VSkeletonLoader_vuetify_link|.

    .. |VSkeletonLoader_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-skeleton-loader" target="_blank">here</a>


    :param type: A string delimited list of skeleton components to create such as `type="text@3"` or `type="card, list-item"`. Will recursively generate a corresponding skeleton from the provided string. Also supports short-hand for multiple elements such as **article@3** and **paragraph@2** which will generate 3 _article_ skeletons and 2 _paragraph_ skeletons. Please see below for a list of available pre-defined options.
    :type string | string[]:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param elevation: See description |VSkeletonLoader_vuetify_link|.
    :type string | number:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VSkeletonLoader_vuetify_link|.
    :type string:
    :param loading: Applies a loading animation with a on-hover loading cursor. A value of **false** will only work when there is content in the `default` slot.
    :type boolean:
    :param loading_text: MISSING DESCRIPTION
    :type string:
    :param boilerplate: Remove the loading animation from the skeleton
    :type boolean:

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
      Vuetify's VSlideGroup component. See more info and examples |VSlideGroup_vuetify_link|.

      .. |VSlideGroup_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-slide-group" target="_blank">here</a>


      :param symbol: See description |VSlideGroup_vuetify_link|.
      :type any:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param disabled: Puts all children components into a disabled state
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param multiple: Allows one to select mulitple items.
      :type boolean:
      :param direction: See description |VSlideGroup_vuetify_link|.
      :type 'horizontal' | 'vertical':
      :param max: Sets a maximum number of selections that can be made.
      :type number:
      :param mandatory: Forces at least one item to always be selected (if available).
      :type boolean | 'force':
      :param next_icon: The appended slot when arrows are shown
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param prev_icon: The prepended slot when arrows are shown
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param show_arrows: See description |VSlideGroup_vuetify_link|.
      :type string | boolean:
      :param center_active: Forces the selected component to be centered
      :type boolean:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideGroup", children, **kwargs)
        self._attr_names += [
            "symbol",
            ("model_value", "modelValue"),
            "tag",
            "disabled",
            ("selected_class", "selectedClass"),
            "multiple",
            "direction",
            "max",
            "mandatory",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            ("center_active", "centerActive"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSlideGroupItem(HtmlElement):
    """
    Vuetify's VSlideGroupItem component. See more info and examples |VSlideGroupItem_vuetify_link|.

    .. |VSlideGroupItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-group-item" target="_blank">here</a>


    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:

    Events

    :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideGroupItem", children, **kwargs)
        self._attr_names += [
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VSlideXReverseTransition(HtmlElement):
    """
    Vuetify's VSlideXReverseTransition component. See more info and examples |VSlideXReverseTransition_vuetify_link|.

    .. |VSlideXReverseTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-x-reverse-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VSlideXReverseTransition_vuetify_link|.
    :type string:
    :param mode: See description |VSlideXReverseTransition_vuetify_link|.
    :type string:
    :param group: See description |VSlideXReverseTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VSlideXReverseTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideXReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlideXTransition(HtmlElement):
    """
    Vuetify's VSlideXTransition component. See more info and examples |VSlideXTransition_vuetify_link|.

    .. |VSlideXTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-x-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VSlideXTransition_vuetify_link|.
    :type string:
    :param mode: See description |VSlideXTransition_vuetify_link|.
    :type string:
    :param group: See description |VSlideXTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VSlideXTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideXTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlideYReverseTransition(HtmlElement):
    """
    Vuetify's VSlideYReverseTransition component. See more info and examples |VSlideYReverseTransition_vuetify_link|.

    .. |VSlideYReverseTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-y-reverse-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VSlideYReverseTransition_vuetify_link|.
    :type string:
    :param mode: See description |VSlideYReverseTransition_vuetify_link|.
    :type string:
    :param group: See description |VSlideYReverseTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VSlideYReverseTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideYReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlideYTransition(HtmlElement):
    """
    Vuetify's VSlideYTransition component. See more info and examples |VSlideYTransition_vuetify_link|.

    .. |VSlideYTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-y-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param origin: See description |VSlideYTransition_vuetify_link|.
    :type string:
    :param mode: See description |VSlideYTransition_vuetify_link|.
    :type string:
    :param group: See description |VSlideYTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |VSlideYTransition_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideYTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "origin",
            "mode",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
        ]
        self._event_names += []


class VSlider(HtmlElement):
    """
      Vuetify's VSlider component. See more info and examples |VSlider_vuetify_link|.

      .. |VSlider_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-slider" target="_blank">here</a>


      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type string | number:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param reverse: See description |VSlider_vuetify_link|.
      :type boolean:
      :param elevation: See description |VSlider_vuetify_link|.
      :type string | number:
      :param rounded: See description |VSlider_vuetify_link|.
      :type string | number | boolean:
      :param color: See description |VSlider_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param id: MISSING DESCRIPTION
      :type string:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VSlider_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param label: See description |VSlider_vuetify_link|.
      :type string:
      :param center_affix: MISSING DESCRIPTION
      :type boolean:
      :param hint: See description |VSlider_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VSlider_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: See description |VSlider_vuetify_link|.
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':
      :param max: Sets the maximum allowed value
      :type string | number:
      :param min: Sets the minimum allowed value
      :type string | number:
      :param step: If greater than 0, sets step interval for ticks
      :type string | number:
      :param thumb_color: Sets the thumb and thumb label color
      :type string:
      :param thumb_label: Show thumb label. If `true` it shows label when using slider. If set to `'always'` it always shows label.
      :type boolean | 'always':
      :param thumb_size: Controls the size of the thumb label.
      :type string | number:
      :param show_ticks: See description |VSlider_vuetify_link|.
      :type boolean | 'always':
      :param ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
      :type number[] | Record<number, string>:
      :param tick_size: Controls the size of **ticks**
      :type string | number:
      :param track_color: Sets the track's color
      :type string:
      :param track_fill_color: Sets the track's fill color
      :type string:
      :param track_size: See description |VSlider_vuetify_link|.
      :type string | number:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-slider.json))
      :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-slider.json))
      :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-slider.json))
      :param end: Slider value emitted at the end of slider movement
      :param start: Slider value emitted at start of slider movement
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlider", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "error",
            "density",
            "reverse",
            "elevation",
            "rounded",
            "color",
            "name",
            "id",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "disabled",
            "label",
            ("center_affix", "centerAffix"),
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
    Vuetify's VSnackbar component. See more info and examples |VSnackbar_vuetify_link|.

    .. |VSnackbar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-snackbar" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param location: MISSING DESCRIPTION
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: MISSING DESCRIPTION
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param absolute: Applies **position: absolute** to the content element.
    :type boolean:
    :param rounded: See description |VSnackbar_vuetify_link|.
    :type string | number | boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VSnackbar_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
    :param z_index: The z-index used for the component
    :type string | number:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param activator: See description |VSnackbar_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |VSnackbar_vuetify_link|.
    :type any:
    :param activator_props: See description |VSnackbar_vuetify_link|.
    :type {}:
    :param open_on_click: See description |VSnackbar_vuetify_link|.
    :type boolean:
    :param open_on_hover: See description |VSnackbar_vuetify_link|.
    :type boolean:
    :param open_on_focus: See description |VSnackbar_vuetify_link|.
    :type boolean:
    :param close_on_content_click: Closes component when you click on its content
    :type boolean:
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :type string | number:
    :param location_strategy: A function used to specifies how the component should position relative to its activator
    :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param origin: See description |VSnackbar_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
    :param offset: A single value that offsets content away from the target based upon what side it is on
    :type string | number | number[]:
    :param transition: See description |VSnackbar_vuetify_link|.
    :type string:
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :type string | boolean | Element:
    :param vertical: Stacks snackbar content on top of the actions (button).
    :type boolean:
    :param multi_line: Gives the snackbar a larger minimum height.
    :type boolean:
    :param timeout: Time (in milliseconds) to wait until snackbar is automatically hidden.  Use `-1` to keep open indefinitely (`0` in version < 2.3 ). It is recommended for this number to be between `4000` and `10000`. Changes to this property will reset the timeout.
    :type string | number:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSnackbar", children, **kwargs)
        self._attr_names += [
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
            "theme",
            "color",
            "variant",
            ("z_index", "zIndex"),
            "disabled",
            "eager",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
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
            "timeout",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSpacer(HtmlElement):
    """
    Vuetify's VSpacer component. See more info and examples |VSpacer_vuetify_link|.

    .. |VSpacer_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-spacer" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSpacer", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VSvgIcon(HtmlElement):
    """
      Vuetify's VSvgIcon component. See more info and examples |VSvgIcon_vuetify_link|.

      .. |VSvgIcon_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-svg-icon" target="_blank">here</a>


      :param icon: See description |VSvgIcon_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param tag: Specify a custom tag used on the root element
      :type string:

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
      Vuetify's VSwitch component. See more info and examples |VSwitch_vuetify_link|.

      .. |VSwitch_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-switch" target="_blank">here</a>


      :param flat: Display component without elevation. Default elevation for thumb is 4dp, `flat` resets it
      :type boolean:
      :param type: MISSING DESCRIPTION
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VSwitch_vuetify_link|.
      :type string:
      :param name: Sets the component's name attribute.
      :type string:
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param id: MISSING DESCRIPTION
      :type string:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VSwitch_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param ripple: See description |VSwitch_vuetify_link|.
      :type boolean:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param loading: Displays circular progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - primary, secondary, success, info, warning, error) or a Boolean which uses the component color (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param label: See description |VSwitch_vuetify_link|.
      :type string:
      :param multiple: Changes expected model to an array
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm used for values
      :type (a: any, b: any) => boolean:
      :param center_affix: MISSING DESCRIPTION
      :type boolean:
      :param hint: See description |VSwitch_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VSwitch_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: Changes the direction of the input
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':
      :param inline: MISSING DESCRIPTION
      :type boolean:
      :param inset: Enlarge the `v-switch` track to encompass the thumb
      :type boolean:
      :param indeterminate: See description |VSwitch_vuetify_link|.
      :type boolean:
      :param true_value: Sets value for truthy state
      :type any:
      :param false_value: Sets value for falsy state
      :type any:
      :param defaults_target: MISSING DESCRIPTION
      :type string:
      :param false_icon: MISSING DESCRIPTION
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param true_icon: MISSING DESCRIPTION
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-switch.json))
      :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-switch.json))
      :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-switch.json))
      :param update_indeterminate: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-switch.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSwitch", children, **kwargs)
        self._attr_names += [
            "flat",
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "theme",
            "color",
            "name",
            "value",
            "id",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "ripple",
            "disabled",
            "loading",
            "label",
            "multiple",
            ("value_comparator", "valueComparator"),
            ("center_affix", "centerAffix"),
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
            "inline",
            "inset",
            "indeterminate",
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
            ("update_indeterminate", "update:indeterminate"),
        ]


class VSystemBar(HtmlElement):
    """
    Vuetify's VSystemBar component. See more info and examples |VSystemBar_vuetify_link|.

    .. |VSystemBar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-system-bar" target="_blank">here</a>


    :param height: Sets the height for the component.
    :type string | number:
    :param elevation: See description |VSystemBar_vuetify_link|.
    :type string | number:
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param rounded: See description |VSystemBar_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VSystemBar_vuetify_link|.
    :type string:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param window: Increases the system bar height to 32px (24px default).
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSystemBar", children, **kwargs)
        self._attr_names += [
            "height",
            "elevation",
            "absolute",
            "rounded",
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
      Vuetify's VTab component. See more info and examples |VTab_vuetify_link|.

      .. |VTab_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-tab" target="_blank">here</a>


      :param text: Specify content text for the component.
      :type string:
      :param border: Applies border styles to component.
      :type string | number | boolean:
      :param icon: See description |VTab_vuetify_link|.
      :type | boolean
    | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param elevation: See description |VTab_vuetify_link|.
      :type string | number:
      :param fixed: Forces component to take up all available space up to their maximum width (300px), and centers it.
      :type boolean:
      :param rounded: See description |VTab_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VTab_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
      :type string | number:
      :param prepend_icon: See description |VTab_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VTab_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param stacked: Displays the tab as a flex-column.
      :type boolean:
      :param ripple: See description |VTab_vuetify_link|.
      :type boolean | { class: string }:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param href: Designates the component as anchor and applies the **href** attribute.
      :type string:
      :param replace: See description |VTab_vuetify_link|.
      :type boolean:
      :param exact: See description |VTab_vuetify_link|.
      :type boolean:
      :param to: See description |VTab_vuetify_link|.
      :type unknown:
      :param direction: Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
      :type 'horizontal' | 'vertical':
      :param slider_color: See description |VTab_vuetify_link|.
      :type string:
      :param hide_slider: Hides the active tab slider component (no exit or enter animation).
      :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTab", children, **kwargs)
        self._attr_names += [
            "text",
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
            "fixed",
            "rounded",
            "tag",
            "theme",
            "color",
            "variant",
            "value",
            "size",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "stacked",
            "ripple",
            "disabled",
            ("selected_class", "selectedClass"),
            "loading",
            "href",
            "replace",
            "exact",
            "to",
            "direction",
            ("slider_color", "sliderColor"),
            ("hide_slider", "hideSlider"),
        ]
        self._event_names += []


class VTable(HtmlElement):
    """
    Vuetify's VTable component. See more info and examples |VTable_vuetify_link|.

    .. |VTable_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-table" target="_blank">here</a>


    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param height: Use the height prop to set the height of the table.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param hover: Will add a hover effect to a table's row when the mouse is over it.
    :type boolean:
    :param fixed_header: Use the fixed-header prop together with the height prop to fix the header to the top of the table.
    :type boolean:
    :param fixed_footer: See description |VTable_vuetify_link|.
    :type boolean:

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
      Vuetify's VTabs component. See more info and examples |VTabs_vuetify_link|.

      .. |VTabs_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-tabs" target="_blank">here</a>


      :param symbol: See description |VTabs_vuetify_link|.
      :type any:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Sets the height of the tabs bar
      :type string | number:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param color: See description |VTabs_vuetify_link|.
      :type string:
      :param items: The items to display in the component. This can be an array of strings or objects with a property `title`
      :type (string | Record<string, any>)[]:
      :param stacked: Apply the stacked prop to all children v-tab components.
      :type boolean:
      :param disabled: Puts all children components into a disabled state
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param multiple: Allows one to select mulitple items.
      :type boolean:
      :param direction: Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
      :type 'horizontal' | 'vertical':
      :param bg_color: See description |VTabs_vuetify_link|.
      :type string:
      :param max: Sets a maximum number of selections that can be made.
      :type number:
      :param grow: Force `v-tab`'s to take up all available space
      :type boolean:
      :param mandatory: Forces at least one item to always be selected (if available).
      :type boolean | 'force':
      :param next_icon: Right pagination icon
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param prev_icon: Left pagination icon
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param show_arrows: Show pagination arrows if the tab items overflow their container. For mobile devices, arrows will only display when using this prop.
      :type string | boolean:
      :param center_active: Forces the selected tab to be centered
      :type boolean:
      :param slider_color: Changes the background color of an auto-generated `v-tabs-slider`
      :type string:
      :param hide_slider: Hide's the generated `v-tabs-slider`
      :type boolean:
      :param align_tabs: See description |VTabs_vuetify_link|.
      :type 'title' | 'end' | 'start' | 'center':
      :param fixed_tabs: `v-tabs-item` min-width 160px, max-width 360px
      :type boolean:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
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
            "items",
            "stacked",
            "disabled",
            ("selected_class", "selectedClass"),
            "multiple",
            "direction",
            ("bg_color", "bgColor"),
            "max",
            "grow",
            "mandatory",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            ("center_active", "centerActive"),
            ("slider_color", "sliderColor"),
            ("hide_slider", "hideSlider"),
            ("align_tabs", "alignTabs"),
            ("fixed_tabs", "fixedTabs"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTextField(HtmlElement):
    """
      Vuetify's VTextField component. See more info and examples |VTextField_vuetify_link|.

      .. |VTextField_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-text-field" target="_blank">here</a>


      :param flat: Removes elevation (shadow) added to element when using the **solo** or **solo-inverted** props
      :type boolean:
      :param type: Sets input type
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param reverse: Reverses the input orientation
      :type boolean:
      :param rounded: Adds a border radius to the input
      :type string | number | boolean:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VTextField_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type | 'outlined'
    | 'plain'
    | 'underlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled':
      :param name: Sets the component's name attribute.
      :type string:
      :param id: Sets the DOM id on the component
      :type string:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component
      :type boolean:
      :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VTextField_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param disabled: Removes the ability to click or target the input
      :type boolean:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param label: See description |VTextField_vuetify_link|.
      :type string:
      :param autofocus: Enables autofocus
      :type boolean:
      :param prefix: Displays prefix text
      :type string:
      :param placeholder: Sets the input’s placeholder text
      :type string:
      :param persistent_placeholder: Forces placeholder to always be visible
      :type boolean:
      :param persistent_counter: Forces counter to always be visible
      :type boolean:
      :param suffix: Displays suffix text
      :type string:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center
      :type boolean:
      :param hint: See description |VTextField_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VTextField_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: Changes the direction of the input
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':
      :param append_inner_icon: See description |VTextField_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param bg_color: See description |VTextField_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared
      :type boolean:
      :param clear_icon: Applied when using **clearable** and the input is dirty
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param base_color: Sets the color of the input when it is not focused
      :type string:
      :param dirty: Manually apply the dirty state styling
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover)
      :type boolean:
      :param prepend_inner_icon: Prepends an icon inside the component's input, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param single_line: Label does not move on focus/dirty
      :type boolean:
      :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
      :type string | number | true:
      :param counter_value: Function returns the counter display text
      :type (value: any) => number:
      :param model_modifiers: **FOR INTERNAL USE ONLY**
      :type Record<string, boolean>:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: Emitted when prepended icon is clicked
      :param click_append: Emitted when append icon is clicked
      :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-text-field.json))
      :param click_clear: Emitted when clearable icon clicked
      :param click_appendInner: Emitted when appended inner icon is clicked
      :param click_prependInner: Emitted when prepended inner icon is clicked
      :param click_control: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-text-field.json))
      :param mousedown_control: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTextField", children, **kwargs)
        self._attr_names += [
            "flat",
            "type",
            ("model_value", "modelValue"),
            "error",
            "density",
            "reverse",
            "rounded",
            "theme",
            "color",
            "variant",
            "name",
            "id",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "disabled",
            "loading",
            "label",
            "autofocus",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("center_affix", "centerAffix"),
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
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            ("base_color", "baseColor"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "counter",
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
      Vuetify's VTextarea component. See more info and examples |VTextarea_vuetify_link|.

      .. |VTextarea_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-textarea" target="_blank">here</a>


      :param flat: MISSING DESCRIPTION
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param reverse: Reverses the orientation
      :type boolean:
      :param rounded: See description |VTextarea_vuetify_link|.
      :type string | number | boolean:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param color: See description |VTextarea_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component
      :type | 'outlined'
    | 'plain'
    | 'underlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled':
      :param name: Sets the component's name attribute.
      :type string:
      :param id: Sets the DOM id on the component
      :type string:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component
      :type boolean:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param append_icon: See description |VTextarea_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param disabled: Removes the ability to click or target the input
      :type boolean:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
      :type string | boolean:
      :param label: See description |VTextarea_vuetify_link|.
      :type string:
      :param autofocus: See description |VTextarea_vuetify_link|.
      :type boolean:
      :param prefix: See description |VTextarea_vuetify_link|.
      :type string:
      :param placeholder: See description |VTextarea_vuetify_link|.
      :type string:
      :param persistent_placeholder: See description |VTextarea_vuetify_link|.
      :type boolean:
      :param persistent_counter: Forces counter to always be visible
      :type boolean:
      :param suffix: See description |VTextarea_vuetify_link|.
      :type string:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center
      :type boolean:
      :param hint: See description |VTextarea_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VTextarea_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string
      :type string | string[]:
      :param direction: Changes the direction of the input
      :type 'horizontal' | 'vertical':
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
      :type boolean | 'auto':
      :param append_inner_icon: See description |VTextarea_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param bg_color: See description |VTextarea_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared
      :type boolean:
      :param clear_icon: The icon used when the **clerable** prop is set to true
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param base_color: Sets the color of the input when it is not focused
      :type string:
      :param dirty: Manually apply the dirty state styling
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover)
      :type boolean:
      :param prepend_inner_icon: See description |VTextarea_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param single_line: Label does not move on focus/dirty
      :type boolean:
      :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
      :type string | number | true:
      :param counter_value: MISSING DESCRIPTION
      :type (value: any) => number:
      :param model_modifiers: **FOR INTERNAL USE ONLY**
      :type Record<string, boolean>:
      :param auto_grow: Automatically grow the textarea depending on amount of text
      :type boolean:
      :param no_resize: Remove resize handle
      :type boolean:
      :param rows: Default row count
      :type string | number:
      :param max_rows: See description |VTextarea_vuetify_link|.
      :type string | number:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-textarea.json))
      :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-textarea.json))
      :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-textarea.json))
      :param click_clear: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-textarea.json))
      :param click_appendInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-textarea.json))
      :param click_prependInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-textarea.json))
      :param click_control: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/master/packages/api-generator/src/locale/en/v-textarea.json))
      :param mousedown_control: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTextarea", children, **kwargs)
        self._attr_names += [
            "flat",
            ("model_value", "modelValue"),
            "error",
            "density",
            "reverse",
            "rounded",
            "theme",
            "color",
            "variant",
            "name",
            "id",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "disabled",
            "loading",
            "label",
            "autofocus",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("center_affix", "centerAffix"),
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
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            ("base_color", "baseColor"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "counter",
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
    Vuetify's VThemeProvider component. See more info and examples |VThemeProvider_vuetify_link|.

    .. |VThemeProvider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-theme-provider" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param with_background: See description |VThemeProvider_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VThemeProvider", children, **kwargs)
        self._attr_names += [
            "tag",
            "theme",
            ("with_background", "withBackground"),
        ]
        self._event_names += []


class VTimeline(HtmlElement):
    """
    Vuetify's VTimeline component. See more info and examples |VTimeline_vuetify_link|.

    .. |VTimeline_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-timeline" target="_blank">here</a>


    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param direction: Display timeline in a **vertical** or **horizontal** direction
    :type 'horizontal' | 'vertical':
    :param align: See description |VTimeline_vuetify_link|.
    :type 'start' | 'center':
    :param side: See description |VTimeline_vuetify_link|.
    :type 'end' | 'start':
    :param justify: See description |VTimeline_vuetify_link|.
    :type string:
    :param line_inset: See description |VTimeline_vuetify_link|.
    :type string | number:
    :param line_thickness: See description |VTimeline_vuetify_link|.
    :type string | number:
    :param line_color: See description |VTimeline_vuetify_link|.
    :type string:
    :param truncate_line: Truncate timeline directly at the **start** or **end** of the line, or on **both** ends
    :type 'end' | 'start' | 'both':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimeline", children, **kwargs)
        self._attr_names += [
            "density",
            "tag",
            "theme",
            "direction",
            "align",
            "side",
            "justify",
            ("line_inset", "lineInset"),
            ("line_thickness", "lineThickness"),
            ("line_color", "lineColor"),
            ("truncate_line", "truncateLine"),
        ]
        self._event_names += []


class VTimelineItem(HtmlElement):
    """
      Vuetify's VTimelineItem component. See more info and examples |VTimelineItem_vuetify_link|.

      .. |VTimelineItem_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-timeline-item" target="_blank">here</a>


      :param icon: See description |VTimelineItem_vuetify_link|.
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'compact':
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param elevation: See description |VTimelineItem_vuetify_link|.
      :type string | number:
      :param rounded: See description |VTimelineItem_vuetify_link|.
      :type string | number | boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param size: Size of the item dot
      :type string | number:
      :param line_inset: See description |VTimelineItem_vuetify_link|.
      :type string | number:
      :param dot_color: See description |VTimelineItem_vuetify_link|.
      :type string:
      :param fill_dot: Remove outer border of item dot, making the color fill the entire dot
      :type boolean:
      :param hide_dot: Hide the timeline item dot
      :type boolean:
      :param hide_opposite: Hide opposite content if it exists
      :type boolean:
      :param icon_color: Color of the icon
      :type string:

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
            "tag",
            "size",
            ("line_inset", "lineInset"),
            ("dot_color", "dotColor"),
            ("fill_dot", "fillDot"),
            ("hide_dot", "hideDot"),
            ("hide_opposite", "hideOpposite"),
            ("icon_color", "iconColor"),
        ]
        self._event_names += []


class VToolbar(HtmlElement):
    """
    Vuetify's VToolbar component. See more info and examples |VToolbar_vuetify_link|.

    .. |VToolbar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-toolbar" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string:
    :param flat: Removes the toolbar's box-shadow.
    :type boolean:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'prominent' | 'comfortable' | 'compact':
    :param height: Designates a specific height for the toolbar. Overrides the heights imposed by other props, e.g. **prominent**, **dense**, **extended**, etc.
    :type string | number:
    :param elevation: See description |VToolbar_vuetify_link|.
    :type string | number:
    :param absolute: Applies position: absolute to the component.
    :type boolean:
    :param rounded: See description |VToolbar_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |VToolbar_vuetify_link|.
    :type string:
    :param image: See description |VToolbar_vuetify_link|.
    :type string:
    :param collapse: Puts the toolbar into a collapsed state reducing its maximum width.
    :type boolean:
    :param extended: Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop, and any of the other props that affect the height of the toolbar, e.g. **prominent**, **dense**, etc., **WITH THE EXCEPTION** of **height**.
    :type boolean:
    :param extension_height: Specify an explicit height for the `extension` slot.
    :type string | number:
    :param floating: Applies **display: inline-flex** to the component.
    :type boolean:

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
    Vuetify's VToolbarItems component. See more info and examples |VToolbarItems_vuetify_link|.

    .. |VToolbarItems_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-toolbar-items" target="_blank">here</a>


    :param color: See description |VToolbarItems_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':

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
    Vuetify's VToolbarTitle component. See more info and examples |VToolbarTitle_vuetify_link|.

    .. |VToolbarTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-toolbar-title" target="_blank">here</a>


    :param text: Specify content text for the component.
    :type string:
    :param tag: Specify a custom tag used on the root element.
    :type string:

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
    Vuetify's VTooltip component. See more info and examples |VTooltip_vuetify_link|.

    .. |VTooltip_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-tooltip" target="_blank">here</a>


    :param text: Specify content text for the component.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param location: MISSING DESCRIPTION
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param z_index: The z-index used for the component
    :type string | number:
    :param id: See description |VTooltip_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param activator: See description |VTooltip_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |VTooltip_vuetify_link|.
    :type any:
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :type boolean:
    :param scrim: Accepts true/false to enable background, and string to define color.
    :type string | boolean:
    :param activator_props: See description |VTooltip_vuetify_link|.
    :type {}:
    :param open_on_click: Designates whether the tooltip should open on activator click
    :type boolean:
    :param open_on_hover: Designates whether the tooltip should open on activator hover
    :type boolean:
    :param open_on_focus: See description |VTooltip_vuetify_link|.
    :type boolean:
    :param close_on_content_click: Closes component when you click on its content
    :type boolean:
    :param close_delay: Delay (in ms) after which menu closes (when open-on-hover prop is set to true)
    :type string | number:
    :param open_delay: Delay (in ms) after which tooltip opens (when `open-on-hover` prop is set to **true**)
    :type string | number:
    :param location_strategy: A function used to specifies how the component should position relative to its activator
    :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param origin: See description |VTooltip_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
    :param offset: A single value that offsets content away from the target based upon what side it is on
    :type string | number | number[]:
    :param scroll_strategy: See description |VTooltip_vuetify_link|.
    :type 'close' | 'block' | 'none' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
    :param transition: See description |VTooltip_vuetify_link|.
    :type string | boolean:
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :type string | boolean | Element:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
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
            ("z_index", "zIndex"),
            "id",
            "disabled",
            "eager",
            "activator",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            ("no_click_animation", "noClickAnimation"),
            "scrim",
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


class VValidation(HtmlElement):
    """
      Vuetify's VValidation component. See more info and examples |VValidation_vuetify_link|.

      .. |VValidation_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-validation" target="_blank">here</a>


      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param error: Puts the input in a manual error state
      :type boolean:
      :param name: Sets the component's name attribute.
      :type string:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param label: See description |VValidation_vuetify_link|.
      :type string:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'lazy'
    | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
      :param update_focused: Event that is emitted when the component's focus state changes
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


class VVirtualScroll(HtmlElement):
    """
    Vuetify's VVirtualScroll component. See more info and examples |VVirtualScroll_vuetify_link|.

    .. |VVirtualScroll_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-virtual-scroll" target="_blank">here</a>


    :param height: Height of the component as a css value
    :type string | number:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param items: The array of items to display
    :type unknown[]:
    :param item_height: Height in pixels of each item to display. When using **dynamic-item-height** this should be an average initial size.
    :type string | number:
    :param renderless: MISSING DESCRIPTION
    :type boolean:

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
            "renderless",
        ]
        self._event_names += []


class VWindow(HtmlElement):
    """
      Vuetify's VWindow component. See more info and examples |VWindow_vuetify_link|.

      .. |VWindow_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-window" target="_blank">here</a>


      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
      :type any:
      :param reverse: Reverse the normal transition direction.
      :type boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children
      :type string:
      :param disabled: Removes the ability to click or target the component
      :type boolean:
      :param selected_class: Configure the active CSS class applied when an item is selected.
      :type string:
      :param direction: The transition direction when changing windows.
      :type 'horizontal' | 'vertical':
      :param mandatory: Forces at least one item to always be selected (if available).
      :type 'force':
      :param continuous: If `true`, window will "wrap around" from the last item to the first, and from the first item to the last
      :type boolean:
      :param next_icon: Icon used for the "next" button if `show-arrows` is `true`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param prev_icon: Icon used for the "prev" button if `show-arrows` is `true`
      :type | string
    | (string | [string, number])[]
    | (new () => any)
    | FunctionalComponent:
      :param show_arrows: Display the "next" and "prev" buttons
      :type string | boolean:
      :param touch: Provide a custom **left** and **right** function when swiped left or right.
      :type any:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VWindow", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "reverse",
            "tag",
            "theme",
            "disabled",
            ("selected_class", "selectedClass"),
            "direction",
            "mandatory",
            "continuous",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            "touch",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VWindowItem(HtmlElement):
    """
    Vuetify's VWindowItem component. See more info and examples |VWindowItem_vuetify_link|.

    .. |VWindowItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-window-item" target="_blank">here</a>


    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param transition: See description |VWindowItem_vuetify_link|.
    :type string | boolean:
    :param reverse_transition: Sets the reverse transition
    :type string | boolean:

    Events

    :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VWindowItem", children, **kwargs)
        self._attr_names += [
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "eager",
            "transition",
            ("reverse_transition", "reverseTransition"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]
