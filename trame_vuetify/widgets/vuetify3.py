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
    "body.append",
    "body.prepend",
    "bottom",
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
    Vuetify's VAlert component. See more info and examples |VAlert_vuetify_link|.

    .. |VAlert_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-alert" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param border: Adds a colored border to the component.
    :type boolean | 'top' | 'end' | 'bottom' | 'start':
    :param border_color: Specifies the color of the border. Accepts any color value.
    :type string:
    :param closable: Adds a close icon that can hide the alert.
    :type boolean:
    :param close_icon: Change the default icon used for **closable** alerts.
    :type any:
    :param type: Create a specialized alert that uses a contextual color and has a pre-defined icon.
    :type 'success' | 'info' | 'warning' | 'error':
    :param close_label: See description |VAlert_vuetify_link|.
    :type string:
    :param icon: See description |VAlert_vuetify_link|.
    :type any:
    :param model_value: Controls whether the component is visible or hidden.
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
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VAlert_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes the component's border-radius.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VAlert_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':

    Events

    :param click_close: Emitted when close icon is clicked.
    :param update_modelValue: Event that is emitted when the component's model changes.
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
    Vuetify's VAlertTitle component. See more info and examples |VAlertTitle_vuetify_link|.

    .. |VAlertTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-alert-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
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


    :param full_height: Sets the component height to 100%.
    :type boolean:
    :param overlaps: **FOR INTERNAL USE ONLY**
    :type string[]:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

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
      Vuetify's VAppBar component. See more info and examples |VAppBar_vuetify_link|.

      .. |VAppBar_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-app-bar" target="_blank">here</a>


      :param image: See description |VAppBar_vuetify_link|.
      :type string:
      :param title: Specify a title text for the component.
      :type string:
      :param flat: Removes the component's **box-shadow**.
      :type boolean:
      :param collapse: Morphs the component into a collapsed state, reducing its maximum width.
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type boolean:
      :param location: Aligns the component towards the top or bottom.
      :type 'top' | 'bottom':
      :param absolute: Applies position: absolute to the component.
      :type boolean:
      :param color: See description |VAppBar_vuetify_link|.
      :type string:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'prominent' | 'comfortable' | 'compact':
      :param extended: Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop, and any of the other props that affect the height of the toolbar, e.g. **prominent**, **dense**, etc., **WITH THE EXCEPTION** of **height**.
      :type boolean:
      :param extension_height: Designate an explicit height for the `extension` slot.
      :type string | number:
      :param floating: Applies **display: inline-flex** to the component.
      :type boolean:
      :param height: Designates a specific height for the toolbar. Overrides the heights imposed by other props, e.g. **prominent**, **dense**, **extended**, etc.
      :type string | number:
      :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
      :type string | number | boolean:
      :param elevation: See description |VAppBar_vuetify_link|.
      :type string | number:
      :param rounded: See description |VAppBar_vuetify_link|.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param tag: Specify a custom tag used on the root element.
      :type string:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param name: Assign a specific name for layout registration.
      :type string:
      :param order: Adjust the order of the component in relation to its registration order.
      :type string | number:
      :param scroll_target: The element to target for scrolling events. Uses `window` by default.
      :type string:
      :param scroll_threshold: The amount of scroll distance down before **scroll-behavior** activates.
      :type string | number:
      :param scroll_behavior: Specify an action to take when the scroll position of **scroll-target** reaches **scroll-threshold**. Accepts any combination of hide, inverted, collapse, elevate, and fade-image. Multiple values can be used, separated by a space.
      :type | (string & {})
    | 'hide'
    | 'inverted'
    | 'collapse'
    | 'elevate'
    | 'fade-image':

      Events

      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAppBar", children, **kwargs)
        self._attr_names += [
            "image",
            "title",
            "flat",
            "collapse",
            ("model_value", "modelValue"),
            "location",
            "absolute",
            "color",
            "density",
            "extended",
            ("extension_height", "extensionHeight"),
            "floating",
            "height",
            "border",
            "elevation",
            "rounded",
            "tile",
            "tag",
            "theme",
            "name",
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
    Vuetify's VAppBarNavIcon component. See more info and examples |VAppBarNavIcon_vuetify_link|.

    .. |VAppBarNavIcon_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-app-bar-nav-icon" target="_blank">here</a>


    :param symbol: See description |VAppBarNavIcon_vuetify_link|.
    :type any:
    :param flat: Removes the button box shadow. This is different than using the 'flat' variant.
    :type boolean:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type boolean:
    :param base_color: Sets the color of component when not focused.
    :type string:
    :param prepend_icon: See description |VAppBarNavIcon_vuetify_link|.
    :type any:
    :param append_icon: See description |VAppBarNavIcon_vuetify_link|.
    :type any:
    :param block: Expands the button to 100% of available space.
    :type boolean:
    :param readonly: Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.
    :type boolean:
    :param slim: Reduces padding to 0 8px.
    :type boolean:
    :param stacked: Displays the button as a flex-column.
    :type boolean:
    :param ripple: See description |VAppBarNavIcon_vuetify_link|.
    :type boolean | { class: string }:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param text: Specify content text for the component.
    :type string:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param elevation: See description |VAppBarNavIcon_vuetify_link|.
    :type string | number:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :type string | boolean:
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VAppBarNavIcon_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VAppBarNavIcon_vuetify_link|.
    :type boolean:
    :param exact: See description |VAppBarNavIcon_vuetify_link|.
    :type boolean:
    :param to: See description |VAppBarNavIcon_vuetify_link|.
    :type RouteLocationRaw:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VAppBarNavIcon_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'text' | 'elevated' | 'tonal' | 'outlined' | 'plain':
    :param icon: See description |VAppBarNavIcon_vuetify_link|.
    :type any:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAppBarNavIcon", children, **kwargs)
        self._attr_names += [
            "symbol",
            "flat",
            "active",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "block",
            "readonly",
            "slim",
            "stacked",
            "ripple",
            "value",
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
            "replace",
            "exact",
            "to",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
            "icon",
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


        :param label: See description |VAutocomplete_vuetify_link|.
        :type string:
        :param auto_select_first: When searching, will always highlight the first option and select it on blur. `exact` will only highlight and select exact matches.
        :type boolean | 'exact':
        :param clear_on_select: Reset the search text when a selection is made while using the **multiple** prop.
        :type boolean:
        :param search: Text input used to filter items.
        :type string:
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'some' | 'every' | 'union' | 'intersection':
        :param no_filter: Do not apply filtering when searching. Useful when data is being filtered server side.
        :type boolean:
        :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param reverse: Reverses the orientation.
        :type boolean:
        :param flat: Removes box shadow when using a variant with elevation.
        :type boolean:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type unknown:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param chips: Changes display of selections to chips.
        :type boolean:
        :param closable_chips: See description |VAutocomplete_vuetify_link|.
        :type boolean:
        :param close_text: Text set to to the inputs `aria-label` and `title` when input menu is closed.
        :type string:
        :param type: Sets input type.
        :type string:
        :param open_text: Text set to to the inputs **aria-label** and **title** when input menu is open.
        :type string:
        :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
        :type boolean:
        :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
        :type boolean:
        :param hide_selected: Do not display in the select menu items that are already selected.
        :type boolean:
        :param list_props: See description |VAutocomplete_vuetify_link|.
        :type unknown:
        :param base_color: Sets the color of the input when it is not focused.
        :type string:
        :param bg_color: See description |VAutocomplete_vuetify_link|.
        :type string:
        :param disabled: Removes the ability to click or target the input.
        :type boolean:
        :param multiple: Changes select to multiple. Accepts array for value.
        :type boolean:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param max_width: Sets the maximum width for the component.
        :type string | number:
        :param min_width: Sets the minimum width for the component.
        :type string | number:
        :param width: Sets the width for the component.
        :type string | number:
        :param items: See description |VAutocomplete_vuetify_link|.
        :type any[]:
        :param item_title: Property on supplied `items` that contains its title.
        :type SelectItemKey<any>:
        :param item_value: Property on supplied `items` that contains its value.
        :type SelectItemKey<any>:
        :param item_children: This property currently has **no effect**.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L73-L77" target="_blank">SelectItemKey</a>:
        :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
        :type SelectItemKey<any>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
        :type boolean:
        :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
        :type (a: any, b: any) => boolean:
        :param rounded: Adds a border radius to the input.
        :type string | number | boolean:
        :param tile: Removes any applied **border-radius** from the component.
        :type boolean:
        :param theme: Specify a theme for this component and all of its children.
        :type string:
        :param color: See description |VAutocomplete_vuetify_link|.
        :type string:
        :param variant: Applies a distinct style to the component.
        :type | 'outlined'
      | 'plain'
      | 'underlined'
      | 'filled'
      | 'solo'
      | 'solo-inverted'
      | 'solo-filled':
        :param name: Sets the component's name attribute.
        :type string:
        :param menu: Renders with the menu open by default.
        :type boolean:
        :param menu_icon: Sets the the spin icon.
        :type any:
        :param menu_props: See description |VAutocomplete_vuetify_link|.
        :type unknown:
        :param id: Sets the DOM id on the component.
        :type string:
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
        :type any:
        :param transition: See description |VAutocomplete_vuetify_link|.
        :type string | boolean | (TransitionProps & { component: Component }):
        :param no_data_text: Text shown when no items are provided to the component.
        :type string:
        :param open_on_clear: Open's the menu whenever the clear icon is clicked.
        :type boolean:
        :param item_color: Sets color of selected items.
        :type string:
        :param autofocus: Enables autofocus.
        :type boolean:
        :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
        :type string | number | boolean:
        :param prefix: Displays prefix text.
        :type string:
        :param placeholder: Sets the input’s placeholder text.
        :type string:
        :param persistent_placeholder: Forces placeholder to always be visible.
        :type boolean:
        :param persistent_counter: Forces counter to always be visible.
        :type boolean:
        :param suffix: Displays suffix text.
        :type string:
        :param role: The role attribute applied to the input.
        :type string:
        :param append_icon: See description |VAutocomplete_vuetify_link|.
        :type any:
        :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
        :type boolean:
        :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`.
        :type any:
        :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
        :type boolean:
        :param hint: See description |VAutocomplete_vuetify_link|.
        :type string:
        :param persistent_hint: See description |VAutocomplete_vuetify_link|.
        :type boolean:
        :param messages: Displays a list of messages or a single message if using a string.
        :type string | string[]:
        :param direction: Changes the direction of the input.
        :type 'horizontal' | 'vertical':
        :param error: Puts the input in a manual error state.
        :type boolean:
        :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
        :type string | string[]:
        :param max_errors: Control the maximum number of shown errors from validation.
        :type string | number:
        :param readonly: Puts input in readonly state.
        :type boolean:
        :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
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
        :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
        :type boolean | 'auto':
        :param clearable: Allows for the component to be cleared.
        :type boolean:
        :param clear_icon: The icon used when the **clearable** prop is set to true.
        :type any:
        :param active: Controls the **active** state of the item. This is typically used to highlight the component.
        :type boolean:
        :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
        :type boolean:
        :param prepend_inner_icon: See description |VAutocomplete_vuetify_link|.
        :type any:
        :param single_line: Label does not move on focus/dirty.
        :type boolean:
        :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
        :type string | boolean:
        :param counter_value: Function returns the counter display text.
        :type number | ((value: any) => number):
        :param model_modifiers: **FOR INTERNAL USE ONLY**
        :type unknown:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes.
        :param click_prepend: Emitted when prepended icon is clicked.
        :param click_append: Emitted when append icon is clicked.
        :param update_focused: Emitted when the input is focused or blurred
        :param click_clear: Emitted when clearable icon clicked.
        :param click_appendInner: Emitted when appended inner icon is clicked.
        :param click_prependInner: Emitted when prepended inner icon is clicked.
        :param update_search: Event emitted when the search value changes.
        :param update_menu: Event that is emitted when the component's menu state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAutocomplete", children, **kwargs)
        self._attr_names += [
            "label",
            ("auto_select_first", "autoSelectFirst"),
            ("clear_on_select", "clearOnSelect"),
            "search",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            "reverse",
            "flat",
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            "chips",
            ("closable_chips", "closableChips"),
            ("close_text", "closeText"),
            "type",
            ("open_text", "openText"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            ("list_props", "listProps"),
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "disabled",
            "multiple",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            "name",
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "id",
            ("model_value", "modelValue"),
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
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "error",
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
    Vuetify's VAvatar component. See more info and examples |VAvatar_vuetify_link|.

    .. |VAvatar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-avatar" target="_blank">here</a>


    :param start: Applies margin at the end of the component.
    :type boolean:
    :param end: Applies margin at the start of the component.
    :type boolean:
    :param icon: See description |VAvatar_vuetify_link|.
    :type any:
    :param image: See description |VAvatar_vuetify_link|.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param rounded: See description |VAvatar_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VAvatar_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'text' | 'elevated' | 'tonal' | 'outlined' | 'plain':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VAvatar", children, **kwargs)
        self._attr_names += [
            "start",
            "end",
            "icon",
            "image",
            "text",
            "density",
            "rounded",
            "tile",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
        ]
        self._event_names += []


class VBadge(HtmlElement):
    """
    Vuetify's VBadge component. See more info and examples |VBadge_vuetify_link|.

    .. |VBadge_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-badge" target="_blank">here</a>


    :param bordered: Applies a **2px** by default and **1.5px** border around the badge when using the **dot** property.
    :type boolean:
    :param color: See description |VBadge_vuetify_link|.
    :type string:
    :param content: Text content to show in the badge.
    :type string | number:
    :param dot: Reduce the size of the badge and hide its contents.
    :type boolean:
    :param floating: Elevates the badge above the slotted content.
    :type boolean:
    :param icon: See description |VBadge_vuetify_link|.
    :type any:
    :param inline: Moves the badge to be inline with the wrapping element. Supports the usage of the **left** prop.
    :type boolean:
    :param label: The **aria-label** used for the badge.
    :type string:
    :param max: Sets the maximum number allowed when using the **content** prop with a `number` like value. If the content number exceeds the maximum value, a `+` suffix is added.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type boolean:
    :param offset_x: Offset the badge on the x-axis.
    :type string | number:
    :param offset_y: Offset the badge on the y-axis.
    :type string | number:
    :param text_color: See description |VBadge_vuetify_link|.
    :type string:
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param rounded: See description |VBadge_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param transition: See description |VBadge_vuetify_link|.
    :type string | boolean | (TransitionProps & { component: Component }):

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBadge", children, **kwargs)
        self._attr_names += [
            "bordered",
            "color",
            "content",
            "dot",
            "floating",
            "icon",
            "inline",
            "label",
            "max",
            ("model_value", "modelValue"),
            ("offset_x", "offsetX"),
            ("offset_y", "offsetY"),
            ("text_color", "textColor"),
            "location",
            "rounded",
            "tile",
            "tag",
            "theme",
            "transition",
        ]
        self._event_names += []


class VBanner(HtmlElement):
    """
    Vuetify's VBanner component. See more info and examples |VBanner_vuetify_link|.

    .. |VBanner_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-banner" target="_blank">here</a>


    :param text: Specify content text for the component.
    :type string:
    :param avatar: Designates a specific src image to pass to the thumbnail.
    :type string:
    :param bg_color: See description |VBanner_vuetify_link|.
    :type string:
    :param color: See description |VBanner_vuetify_link|.
    :type string:
    :param icon: See description |VBanner_vuetify_link|.
    :type any:
    :param stacked: Forces the banner actions onto a new line. This is not applicable when the banner has `lines="one"`.
    :type boolean:
    :param sticky: See description |VBanner_vuetify_link|.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param mobile: Applies the mobile banner styles.
    :type boolean:
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
    :param elevation: See description |VBanner_vuetify_link|.
    :type string | number:
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'sticky' | 'static' | 'relative' | 'fixed' | 'absolute':
    :param rounded: See description |VBanner_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param lines: The amount of visible lines of text before it truncates.
    :type 'one' | 'two' | 'three':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBanner", children, **kwargs)
        self._attr_names += [
            "text",
            "avatar",
            ("bg_color", "bgColor"),
            "color",
            "icon",
            "stacked",
            "sticky",
            "border",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "elevation",
            "location",
            "position",
            "rounded",
            "tile",
            "tag",
            "theme",
            "lines",
        ]
        self._event_names += []


class VBannerActions(HtmlElement):
    """
    Vuetify's VBannerActions component. See more info and examples |VBannerActions_vuetify_link|.

    .. |VBannerActions_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-banner-actions" target="_blank">here</a>


    :param color: See description |VBannerActions_vuetify_link|.
    :type string:
    :param density: Adjusts the vertical height used by the component.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBannerActions", children, **kwargs)
        self._attr_names += [
            "color",
            "density",
        ]
        self._event_names += []


class VBannerText(HtmlElement):
    """
    Vuetify's VBannerText component. See more info and examples |VBannerText_vuetify_link|.

    .. |VBannerText_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-banner-text" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
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


    :param base_color: Sets the color of component when not focused.
    :type string:
    :param bg_color: See description |VBottomNavigation_vuetify_link|.
    :type string:
    :param color: See description |VBottomNavigation_vuetify_link|.
    :type string:
    :param grow: See description |VBottomNavigation_vuetify_link|.
    :type boolean:
    :param mode: Changes the orientation and active state styling of the component.
    :type string:
    :param height: Sets the height for the component.
    :type string | number:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
    :type string | number | boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param elevation: See description |VBottomNavigation_vuetify_link|.
    :type string | number:
    :param rounded: See description |VBottomNavigation_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param multiple: Allows one to select multiple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param disabled: Puts all children components into a disabled state.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    :param update_active: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VBottomNavigation.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBottomNavigation", children, **kwargs)
        self._attr_names += [
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "color",
            "grow",
            "mode",
            "height",
            "active",
            "border",
            "density",
            "elevation",
            "rounded",
            "tile",
            "name",
            "order",
            "absolute",
            "tag",
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
            "theme",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_active", "update:active"),
        ]


class VBottomSheet(HtmlElement):
    """
      Vuetify's VBottomSheet component. See more info and examples |VBottomSheet_vuetify_link|.

      .. |VBottomSheet_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-bottom-sheet" target="_blank">here</a>


      :param activator: Explicitly sets the overlay's activator.
      :type Element | 'parent' | (string & {}) | ComponentPublicInstance:
      :param inset: Reduces the sheet content maximum width to 70%.
      :type boolean:
      :param fullscreen: Changes layout for fullscreen display.
      :type boolean:
      :param retain_focus: Tab focus will return to the first child of the dialog by default. Disable this when using external tools that require focus such as TinyMCE or vue-clipboard.
      :type boolean:
      :param scrollable: See description |VBottomSheet_vuetify_link|.
      :type boolean:
      :param absolute: Applies **position: absolute** to the content element.
      :type boolean:
      :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
      :type boolean:
      :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
      :type boolean:
      :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
      :type any:
      :param content_props: Apply custom properties to the content.
      :type any:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param opacity: Sets the overlay opacity.
      :type string | number:
      :param no_click_animation: Disables the bounce effect when clicking outside of a `v-dialog`'s content when using the **persistent** prop.
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type boolean:
      :param persistent: Clicking outside of the element or pressing **esc** key will not deactivate it.
      :type boolean:
      :param scrim: Accepts true/false to enable background, and string to define color.
      :type string | boolean:
      :param z_index: The z-index used for the component.
      :type string | number:
      :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
      :type | Element
    | 'parent'
    | 'cursor'
    | (string & {})
    | ComponentPublicInstance
    | [number, number]:
      :param activator_props: Apply custom properties to the activator.
      :type unknown:
      :param open_on_click: Activate the component when the activator is clicked.
      :type boolean:
      :param open_on_hover: Activate the component when the activator is hovered.
      :type boolean:
      :param open_on_focus: Activate the component when the activator is focused.
      :type boolean:
      :param close_on_content_click: Closes component when you click on its content.
      :type boolean:
      :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
      :type string | number:
      :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
      :type string | number:
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
      :param location_strategy: A function used to specifies how the component should position relative to its activator.
      :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
      :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param origin: See description |VBottomSheet_vuetify_link|.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
      :param offset: A single value that offsets content away from the target based upon what side it is on.
      :type string | number | number[]:
      :param scroll_strategy: Strategy used when the component is activate and user scrolls.
      :type 'none' | 'close' | 'block' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param transition: See description |VBottomSheet_vuetify_link|.
      :type | { component: Component }
    | string
    | boolean
    | (TransitionProps & { component: Component }):
      :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
      :type string | boolean | Element:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBottomSheet", children, **kwargs)
        self._attr_names += [
            "activator",
            "inset",
            "fullscreen",
            ("retain_focus", "retainFocus"),
            "scrollable",
            "absolute",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
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
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "eager",
            ("location_strategy", "locationStrategy"),
            "location",
            "origin",
            "offset",
            ("scroll_strategy", "scrollStrategy"),
            "theme",
            "transition",
            "attach",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VBreadcrumbs(HtmlElement):
    """
        Vuetify's VBreadcrumbs component. See more info and examples |VBreadcrumbs_vuetify_link|.

        .. |VBreadcrumbs_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-breadcrumbs" target="_blank">here</a>


        :param divider: Specifies the dividing character between items.
        :type string:
        :param active_class: The class applied to the component when it is in an active state.
        :type string:
        :param active_color: The applied color when the component is in an active state.
        :type string:
        :param bg_color: See description |VBreadcrumbs_vuetify_link|.
        :type string:
        :param color: See description |VBreadcrumbs_vuetify_link|.
        :type string:
        :param disabled: Removes the ability to click or target the component.
        :type boolean:
        :param icon: See description |VBreadcrumbs_vuetify_link|.
        :type any:
        :param items: An array of strings or objects used for automatically generating children components.
        :type (
      | string
      | (Partial<LinkProps> & { title: string; disabled: boolean })
    )[]:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param rounded: See description |VBreadcrumbs_vuetify_link|.
        :type string | number | boolean:
        :param tile: Removes any applied **border-radius** from the component.
        :type boolean:
        :param tag: Specify a custom tag used on the root element.
        :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBreadcrumbs", children, **kwargs)
        self._attr_names += [
            "divider",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
            ("bg_color", "bgColor"),
            "color",
            "disabled",
            "icon",
            "items",
            "density",
            "rounded",
            "tile",
            "tag",
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


    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type boolean:
    :param active_class: See description |VBreadcrumbsItem_vuetify_link|.
    :type string:
    :param active_color: The applied color when the component is in an active state.
    :type string:
    :param color: See description |VBreadcrumbsItem_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param title: Specify a title text for the component.
    :type string:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VBreadcrumbsItem_vuetify_link|.
    :type boolean:
    :param exact: See description |VBreadcrumbsItem_vuetify_link|.
    :type boolean:
    :param to: See description |VBreadcrumbsItem_vuetify_link|.
    :type RouteLocationRaw:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBreadcrumbsItem", children, **kwargs)
        self._attr_names += [
            "active",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
            "color",
            "disabled",
            "title",
            "href",
            "replace",
            "exact",
            "to",
            "tag",
        ]
        self._event_names += []


class VBtn(HtmlElement):
    """
    Vuetify's VBtn component. See more info and examples |VBtn_vuetify_link|.

    .. |VBtn_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-btn" target="_blank">here</a>


    :param symbol: See description |VBtn_vuetify_link|.
    :type any:
    :param flat: Removes the button box shadow. This is different than using the 'flat' variant.
    :type boolean:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type boolean:
    :param base_color: Sets the color of component when not focused.
    :type string:
    :param prepend_icon: See description |VBtn_vuetify_link|.
    :type any:
    :param append_icon: See description |VBtn_vuetify_link|.
    :type any:
    :param block: Expands the button to 100% of available space.
    :type boolean:
    :param readonly: Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.
    :type boolean:
    :param slim: Reduces padding to 0 8px.
    :type boolean:
    :param stacked: Displays the button as a flex-column.
    :type boolean:
    :param ripple: See description |VBtn_vuetify_link|.
    :type boolean | { class: string }:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param text: Specify content text for the component.
    :type string:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param elevation: See description |VBtn_vuetify_link|.
    :type string | number:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :type string | boolean:
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VBtn_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VBtn_vuetify_link|.
    :type boolean:
    :param exact: See description |VBtn_vuetify_link|.
    :type boolean:
    :param to: See description |VBtn_vuetify_link|.
    :type RouteLocationRaw:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VBtn_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'text' | 'elevated' | 'tonal' | 'outlined' | 'plain':
    :param icon: See description |VBtn_vuetify_link|.
    :type any:

    Events

    :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtn", children, **kwargs)
        self._attr_names += [
            "symbol",
            "flat",
            "active",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "block",
            "readonly",
            "slim",
            "stacked",
            "ripple",
            "value",
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
            "replace",
            "exact",
            "to",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
            "icon",
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VBtnGroup(HtmlElement):
    """
    Vuetify's VBtnGroup component. See more info and examples |VBtnGroup_vuetify_link|.

    .. |VBtnGroup_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-btn-group" target="_blank">here</a>


    :param base_color: Sets the color of component when not focused.
    :type string:
    :param divided: See description |VBtnGroup_vuetify_link|.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
    :type string | number | boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param elevation: See description |VBtnGroup_vuetify_link|.
    :type string | number:
    :param rounded: See description |VBtnGroup_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VBtnGroup_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'elevated' | 'tonal' | 'outlined' | 'text' | 'plain':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtnGroup", children, **kwargs)
        self._attr_names += [
            ("base_color", "baseColor"),
            "divided",
            "border",
            "density",
            "elevation",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
        ]
        self._event_names += []


class VBtnToggle(HtmlElement):
    """
    Vuetify's VBtnToggle component. See more info and examples |VBtnToggle_vuetify_link|.

    .. |VBtnToggle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-btn-toggle" target="_blank">here</a>


    :param base_color: Sets the color of component when not focused.
    :type string:
    :param divided: See description |VBtnToggle_vuetify_link|.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
    :type string | number | boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param elevation: See description |VBtnToggle_vuetify_link|.
    :type string | number:
    :param rounded: Round edge buttons.
    :type string | number | boolean:
    :param tile: Removes the component's border-radius.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VBtnToggle_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'elevated' | 'tonal' | 'outlined' | 'text' | 'plain':
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param multiple: Allows one to select multiple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param disabled: Puts all children components into a disabled state.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VBtnToggle", children, **kwargs)
        self._attr_names += [
            ("base_color", "baseColor"),
            "divided",
            "border",
            "density",
            "elevation",
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VCalendar(HtmlElement):
    """
    Vuetify's VCalendar component. See more info and examples |VCalendar_vuetify_link|.

    .. |VCalendar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-calendar" target="_blank">here</a>


    :param hide_header: Determines whether the header is hidden in the calendar view.
    :type boolean:
    :param hide_week_number: Toggles the display of week numbers in a calendar view.
    :type boolean:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param month: Specifies the month for the calendar view.
    :type string | number:
    :param show_adjacent_months: Shows or hides days from adjacent months.
    :type boolean:
    :param year: Specifies the year for the calendar view.
    :type string | number:
    :param weekdays: Specifies which days of the week to display.
    :type number[]:
    :param weeks_in_month: A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.
    :type 'dynamic' | 'static':
    :param allowed_dates: Determines which dates are selectable.
    :type unknown[] | ((date: unknown) => boolean):
    :param display_value: Value to display for the component, possibly a formatted date.
    :type unknown:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown[]:
    :param max: Maximum date or value that can be selected.
    :type unknown:
    :param min: Minimum date or value that can be selected.
    :type unknown:
    :param hide_day_header: Determines whether the day header is visible in the calendar day view.
    :type boolean:
    :param intervals: Total number of intervals in a day view.
    :type number:
    :param day: Represents the specific day associated with the interval.
    :type unknown:
    :param day_index: Index of the day this interval is a part of, in a week or month view.
    :type number:
    :param events: Array of events specific to this interval.
    :type any[]:
    :param interval_divisions: Number of subdivisions within this interval.
    :type number:
    :param interval_duration: Duration of this specific interval in minutes.
    :type number:
    :param interval_height: Height of the interval in pixels in the calendar view.
    :type number:
    :param interval_format: Formatting rule for displaying the interval, as a string or function.
    :type string | Function:
    :param interval_start: Starting time for this specific interval.
    :type number:
    :param next_icon: The icon to use for the next button.
    :type string:
    :param prev_icon: The icon to use for the prev button.
    :type string:
    :param title: Specify a title text for the component.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param view_mode: The current view mode of the calendar.
    :type 'month' | 'day' | 'week':

    Events

    :param next: Emitted when moving to the next time period.
    :param prev: Emitted when moving to the previous time period.
    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendar", children, **kwargs)
        self._attr_names += [
            ("hide_header", "hideHeader"),
            ("hide_week_number", "hideWeekNumber"),
            "disabled",
            "month",
            ("show_adjacent_months", "showAdjacentMonths"),
            "year",
            "weekdays",
            ("weeks_in_month", "weeksInMonth"),
            ("allowed_dates", "allowedDates"),
            ("display_value", "displayValue"),
            ("model_value", "modelValue"),
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
            "title",
            "text",
            ("view_mode", "viewMode"),
        ]
        self._event_names += [
            "next",
            "prev",
            ("update_modelValue", "update:modelValue"),
        ]


class VCalendarDay(HtmlElement):
    """
    Vuetify's VCalendarDay component. See more info and examples |VCalendarDay_vuetify_link|.

    .. |VCalendarDay_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-calendar-day" target="_blank">here</a>


    :param hide_day_header: Determines whether the day header is visible in the calendar day view.
    :type boolean:
    :param intervals: Specifies the total number of time intervals for the day in the calendar view.
    :type number:
    :param day: Represents the specific day associated with the interval.
    :type unknown:
    :param day_index: Index of the day this interval is a part of, in a week or month view.
    :type number:
    :param events: Array of events specific to this interval.
    :type any[]:
    :param interval_divisions: Number of subdivisions within this interval.
    :type number:
    :param interval_duration: Duration of this specific interval in minutes.
    :type number:
    :param interval_height: Height of the interval in pixels in the calendar view.
    :type number:
    :param interval_format: Formatting rule for displaying the interval, as a string or function.
    :type string | Function:
    :param interval_start: Starting time for this specific interval.
    :type number:

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
    Vuetify's VCalendarHeader component. See more info and examples |VCalendarHeader_vuetify_link|.

    .. |VCalendarHeader_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-calendar-header" target="_blank">here</a>


    :param next_icon: The icon to use for the next button.
    :type string:
    :param prev_icon: The icon to use for the prev button.
    :type string:
    :param title: Specify a title text for the component.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param view_mode: The current view mode of the calendar.
    :type 'month' | 'week' | 'day':

    Events

    :param click_next: Event emitted when clicking the next button.
    :param click_prev: Event emitted when clicking the prev button.
    :param click_toToday: Event emitted when clicking the today button.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendarHeader", children, **kwargs)
        self._attr_names += [
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            "title",
            "text",
            ("view_mode", "viewMode"),
        ]
        self._event_names += [
            ("click_next", "click:next"),
            ("click_prev", "click:prev"),
            ("click_toToday", "click:toToday"),
        ]


class VCalendarInterval(HtmlElement):
    """
    Vuetify's VCalendarInterval component. See more info and examples |VCalendarInterval_vuetify_link|.

    .. |VCalendarInterval_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-calendar-interval" target="_blank">here</a>


    :param index: Index or position of the interval in the day view.
    :type number:
    :param day: Represents the specific day associated with the interval.
    :type unknown:
    :param day_index: Index of the day this interval is a part of, in a week or month view.
    :type number:
    :param events: Array of events specific to this interval.
    :type any[]:
    :param interval_divisions: Number of subdivisions within this interval.
    :type number:
    :param interval_duration: Duration of this specific interval in minutes.
    :type number:
    :param interval_height: Height of the interval in pixels in the calendar view.
    :type number:
    :param interval_format: Formatting rule for displaying the interval, as a string or function.
    :type string | Function:
    :param interval_start: Starting time for this specific interval.
    :type number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendarInterval", children, **kwargs)
        self._attr_names += [
            "index",
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


class VCalendarIntervalEvent(HtmlElement):
    """
    Vuetify's VCalendarIntervalEvent component. See more info and examples |VCalendarIntervalEvent_vuetify_link|.

    .. |VCalendarIntervalEvent_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-calendar-interval-event" target="_blank">here</a>


    :param all_day: Indicates whether the event spans the entire day.
    :type boolean:
    :param interval: The specific time interval this event is associated with.
    :type unknown:
    :param interval_divisions: Number of subdivisions within the interval for this event.
    :type number:
    :param interval_duration: Duration of the interval in which this event occurs, in minutes.
    :type number:
    :param interval_height: Height of the interval in the calendar view, in pixels.
    :type number:
    :param event: The event object associated with this calendar interval.
    :type unknown:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendarIntervalEvent", children, **kwargs)
        self._attr_names += [
            ("all_day", "allDay"),
            "interval",
            ("interval_divisions", "intervalDivisions"),
            ("interval_duration", "intervalDuration"),
            ("interval_height", "intervalHeight"),
            "event",
        ]
        self._event_names += []


class VCalendarMonthDay(HtmlElement):
    """
    Vuetify's VCalendarMonthDay component. See more info and examples |VCalendarMonthDay_vuetify_link|.

    .. |VCalendarMonthDay_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-calendar-month-day" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string | number:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type boolean:
    :param color: See description |VCalendarMonthDay_vuetify_link|.
    :type string:
    :param day: Represents the specific day in the month view of the calendar.
    :type unknown:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param events: Array of events associated with this specific day.
    :type any[]:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCalendarMonthDay", children, **kwargs)
        self._attr_names += [
            "title",
            "active",
            "color",
            "day",
            "disabled",
            "events",
        ]
        self._event_names += []


class VCard(HtmlElement):
    """
    Vuetify's VCard component. See more info and examples |VCard_vuetify_link|.

    .. |VCard_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string | number:
    :param subtitle: Specify a subtitle text for the component.
    :type string | number:
    :param text: Specify content text for the component.
    :type string | number:
    :param image: Apply a specific background image to the component.
    :type string:
    :param flat: Removes the card's elevation.
    :type boolean:
    :param append_avatar: See description |VCard_vuetify_link|.
    :type string:
    :param append_icon: See description |VCard_vuetify_link|.
    :type any:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param hover: See description |VCard_vuetify_link|.
    :type boolean:
    :param link: Designates that the component is a link. This is automatic when using the href or to prop.
    :type boolean:
    :param prepend_avatar: See description |VCard_vuetify_link|.
    :type string:
    :param prepend_icon: See description |VCard_vuetify_link|.
    :type any:
    :param ripple: See description |VCard_vuetify_link|.
    :type boolean | { class: string }:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :type string | boolean:
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VCard_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VCard_vuetify_link|.
    :type boolean:
    :param exact: See description |VCard_vuetify_link|.
    :type boolean:
    :param to: See description |VCard_vuetify_link|.
    :type RouteLocationRaw:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VCard_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCard", children, **kwargs)
        self._attr_names += [
            "title",
            "subtitle",
            "text",
            "image",
            "flat",
            ("append_avatar", "appendAvatar"),
            ("append_icon", "appendIcon"),
            "disabled",
            "hover",
            "link",
            ("prepend_avatar", "prependAvatar"),
            ("prepend_icon", "prependIcon"),
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
            "loading",
            "location",
            "position",
            "rounded",
            "tile",
            "href",
            "replace",
            "exact",
            "to",
            "tag",
            "theme",
            "color",
            "variant",
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
    :type string | number:
    :param subtitle: Specify a subtitle text for the component.
    :type string | number:
    :param append_avatar: See description |VCardItem_vuetify_link|.
    :type string:
    :param append_icon: See description |VCardItem_vuetify_link|.
    :type any:
    :param prepend_avatar: See description |VCardItem_vuetify_link|.
    :type string:
    :param prepend_icon: See description |VCardItem_vuetify_link|.
    :type any:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardItem", children, **kwargs)
        self._attr_names += [
            "title",
            "subtitle",
            ("append_avatar", "appendAvatar"),
            ("append_icon", "appendIcon"),
            ("prepend_avatar", "prependAvatar"),
            ("prepend_icon", "prependIcon"),
            "density",
        ]
        self._event_names += []


class VCardSubtitle(HtmlElement):
    """
    Vuetify's VCardSubtitle component. See more info and examples |VCardSubtitle_vuetify_link|.

    .. |VCardSubtitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-subtitle" target="_blank">here</a>


    :param opacity: Sets the component's opacity value
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardSubtitle", children, **kwargs)
        self._attr_names += [
            "opacity",
            "tag",
        ]
        self._event_names += []


class VCardText(HtmlElement):
    """
    Vuetify's VCardText component. See more info and examples |VCardText_vuetify_link|.

    .. |VCardText_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-text" target="_blank">here</a>


    :param opacity: Sets the component's opacity value
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCardText", children, **kwargs)
        self._attr_names += [
            "opacity",
            "tag",
        ]
        self._event_names += []


class VCardTitle(HtmlElement):
    """
    Vuetify's VCardTitle component. See more info and examples |VCardTitle_vuetify_link|.

    .. |VCardTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
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


    :param color: See description |VCarousel_vuetify_link|.
    :type string:
    :param cycle: Determines if the carousel should cycle through images.
    :type boolean:
    :param delimiter_icon: Sets icon for carousel delimiter.
    :type any:
    :param height: Sets the height for the component.
    :type string | number:
    :param hide_delimiters: Hides the carousel's bottom delimiters.
    :type boolean:
    :param hide_delimiter_background: Hides the bottom delimiter background.
    :type boolean:
    :param interval: The duration between image cycles. Requires the **cycle** prop.
    :type string | number:
    :param progress: Displays a carousel progress bar. Requires the **cycle** prop and **interval**.
    :type string | boolean:
    :param continuous: Determines whether carousel is continuous.
    :type boolean:
    :param next_icon: The displayed icon for forcing pagination to the next item.
    :type any:
    :param prev_icon: The displayed icon for forcing pagination to the previous item.
    :type any:
    :param reverse: Reverse the normal transition direction.
    :type boolean:
    :param show_arrows: Displays arrows for next/previous navigation.
    :type string | boolean:
    :param touch: Provide a custom **left** and **right** function when swiped left or right.
    :type boolean | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/directives/touch/index.ts#L9-L17" target="_blank">TouchHandlers</a>:
    :param direction: The transition direction when changing windows.
    :type 'horizontal' | 'vertical':
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param vertical_delimiters: Displays carousel delimiters vertically.
    :type boolean | 'left' | 'right':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCarousel", children, **kwargs)
        self._attr_names += [
            "color",
            "cycle",
            ("delimiter_icon", "delimiterIcon"),
            "height",
            ("hide_delimiters", "hideDelimiters"),
            ("hide_delimiter_background", "hideDelimiterBackground"),
            "interval",
            "progress",
            "continuous",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            "reverse",
            ("show_arrows", "showArrows"),
            "touch",
            "direction",
            ("model_value", "modelValue"),
            "disabled",
            ("selected_class", "selectedClass"),
            "mandatory",
            "tag",
            "theme",
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


        :param alt: Alternate text for screen readers. Leave empty for decorative images.
        :type string:
        :param cover: Resizes the background image to cover the entire container.
        :type boolean:
        :param color: See description |VCarouselItem_vuetify_link|.
        :type string:
        :param draggable: See description |VCarouselItem_vuetify_link|.
        :type boolean | 'true' | 'false':
        :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
        :type boolean:
        :param gradient: See description |VCarouselItem_vuetify_link|.
        :type string:
        :param lazy_src: Something to show while waiting for the main image to load, typically a small base64-encoded thumbnail. Has a slight blur filter applied.
    NOTE: This prop has no effect unless either `height` or `aspect-ratio` are provided.
        :type string:
        :param options: See description |VCarouselItem_vuetify_link|.
        :type IntersectionObserverInit:
        :param sizes: See description |VCarouselItem_vuetify_link|.
        :type string:
        :param src: The image URL. This prop is mandatory.
        :type | string
      | { src: string; srcset: string; lazySrc: string; aspect: number }:
        :param srcset: See description |VCarouselItem_vuetify_link|.
        :type string:
        :param position: See description |VCarouselItem_vuetify_link|.
        :type string:
        :param aspect_ratio: Calculated as `width/height`, so for a 1920x1080px image this will be `1.7778`. Will be calculated automatically if omitted.
        :type string | number:
        :param content_class: Apply a custom class to the internal content element.
        :type any:
        :param inline: Display as an inline element instead of a block, also disables flex-grow.
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
        :param rounded: See description |VCarouselItem_vuetify_link|.
        :type string | number | boolean:
        :param tile: Removes any applied **border-radius** from the component.
        :type boolean:
        :param transition: See description |VCarouselItem_vuetify_link|.
        :type string | boolean:
        :param crossorigin: See description |VCarouselItem_vuetify_link|.
        :type '' | 'anonymous' | 'use-credentials':
        :param referrerpolicy: See description |VCarouselItem_vuetify_link|.
        :type | 'no-referrer'
      | 'no-referrer-when-downgrade'
      | 'origin'
      | 'origin-when-cross-origin'
      | 'same-origin'
      | 'strict-origin'
      | 'strict-origin-when-cross-origin'
      | 'unsafe-url':
        :param reverse_transition: Sets the reverse transition.
        :type string | boolean:
        :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
        :type any:
        :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.
        :type boolean:
        :param selected_class: Configure the active CSS class applied when an item is selected.
        :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCarouselItem", children, **kwargs)
        self._attr_names += [
            "alt",
            "cover",
            "color",
            "draggable",
            "eager",
            "gradient",
            ("lazy_src", "lazySrc"),
            "options",
            "sizes",
            "src",
            "srcset",
            "position",
            ("aspect_ratio", "aspectRatio"),
            ("content_class", "contentClass"),
            "inline",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "rounded",
            "tile",
            "transition",
            "crossorigin",
            "referrerpolicy",
            ("reverse_transition", "reverseTransition"),
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += []


class VCheckbox(HtmlElement):
    """
      Vuetify's VCheckbox component. See more info and examples |VCheckbox_vuetify_link|.

      .. |VCheckbox_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-checkbox" target="_blank">here</a>


      :param label: See description |VCheckbox_vuetify_link|.
      :type string:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VCheckbox_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param type: Provides the default type for children selection controls.
      :type string:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VCheckbox_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VCheckbox_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type unknown:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'input'
    | 'blur'
    | 'submit'
    | 'input lazy'
    | 'blur lazy'
    | 'submit lazy'
    | 'lazy input'
    | 'lazy blur'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param indeterminate: Sets an indeterminate state for the checkbox.
      :type boolean:
      :param indeterminate_icon: The icon used when in an indeterminate state.
      :type any:
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param true_value: Sets value for truthy state.
      :type any:
      :param false_value: Sets value for falsy state.
      :type any:
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param color: See description |VCheckbox_vuetify_link|.
      :type string:
      :param defaults_target: The target component to provide defaults values for.
      :type string:
      :param false_icon: The icon used when inactive.
      :type any:
      :param true_icon: The icon used when active.
      :type any:
      :param ripple: See description |VCheckbox_vuetify_link|.
      :type boolean | { class: string }:
      :param multiple: Changes expected model to an array.
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
      :type (a: any, b: any) => boolean:

      Events

      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when appended icon is clicked.
      :param update_focused: Event that is emitted when the component's focus state changes.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCheckbox", children, **kwargs)
        self._attr_names += [
            "label",
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            "type",
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            "indeterminate",
            ("indeterminate_icon", "indeterminateIcon"),
            ("base_color", "baseColor"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            ("defaults_target", "defaultsTarget"),
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "multiple",
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("update_modelValue", "update:modelValue"),
        ]


class VCheckboxBtn(HtmlElement):
    """
    Vuetify's VCheckboxBtn component. See more info and examples |VCheckboxBtn_vuetify_link|.

    .. |VCheckboxBtn_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-checkbox-btn" target="_blank">here</a>


    :param label: See description |VCheckboxBtn_vuetify_link|.
    :type string:
    :param indeterminate: See description |VCheckboxBtn_vuetify_link|.
    :type boolean:
    :param indeterminate_icon: Icon used when the component is in an indeterminate state.
    :type any:
    :param type: Provides the default type for children selection controls.
    :type string:
    :param base_color: Sets the color of the input when it is not focused.
    :type string:
    :param true_value: Sets value for truthy state.
    :type any:
    :param false_value: Sets value for falsy state.
    :type any:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param color: See description |VCheckboxBtn_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param defaults_target: The target component to provide defaults values for.
    :type string:
    :param error: Puts the input in a manual error state.
    :type boolean:
    :param id: Sets the DOM id on the component.
    :type string:
    :param inline: Puts children inputs into a row.
    :type boolean:
    :param false_icon: The icon used when inactive.
    :type any:
    :param true_icon: The icon used when active.
    :type any:
    :param ripple: See description |VCheckboxBtn_vuetify_link|.
    :type boolean | { class: string }:
    :param multiple: Changes select to multiple. Accepts array for value.
    :type boolean:
    :param name: Sets the component's name attribute.
    :type string:
    :param readonly: Puts input in readonly state.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :type (a: any, b: any) => boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    :param update_indeterminate: Event that is emitted when the component's indeterminate state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCheckboxBtn", children, **kwargs)
        self._attr_names += [
            "label",
            "indeterminate",
            ("indeterminate_icon", "indeterminateIcon"),
            "type",
            ("base_color", "baseColor"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            "disabled",
            ("defaults_target", "defaultsTarget"),
            "error",
            "id",
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "multiple",
            "name",
            "readonly",
            ("model_value", "modelValue"),
            ("value_comparator", "valueComparator"),
            "density",
            "theme",
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


    :param label: Applies a medium size border radius.
    :type boolean:
    :param filter: Displays a selection icon when selected.
    :type boolean:
    :param active_class: See description |VChip_vuetify_link|.
    :type string:
    :param append_avatar: See description |VChip_vuetify_link|.
    :type string:
    :param append_icon: See description |VChip_vuetify_link|.
    :type any:
    :param closable: Adds remove button and then a chip can be closed.
    :type boolean:
    :param close_icon: Change the default icon used for **close** chips.
    :type any:
    :param close_label: See description |VChip_vuetify_link|.
    :type string:
    :param draggable: Makes the chip draggable.
    :type boolean:
    :param filter_icon: Change the default icon used for **filter** chips.
    :type string:
    :param link: Designates that the component is a link. This is automatic when using the href or to prop.
    :type boolean:
    :param pill: Remove `v-avatar` padding.
    :type boolean:
    :param prepend_avatar: See description |VChip_vuetify_link|.
    :type string:
    :param prepend_icon: See description |VChip_vuetify_link|.
    :type any:
    :param ripple: See description |VChip_vuetify_link|.
    :type boolean | { class: string }:
    :param value: See description |VChip_vuetify_link|.
    :type any:
    :param text: Specify content text for the component.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
    :type string | number | boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param elevation: See description |VChip_vuetify_link|.
    :type string | number:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param rounded: See description |VChip_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VChip_vuetify_link|.
    :type boolean:
    :param exact: See description |VChip_vuetify_link|.
    :type boolean:
    :param to: See description |VChip_vuetify_link|.
    :type RouteLocationRaw:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VChip_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'text' | 'elevated' | 'tonal' | 'outlined' | 'plain':

    Events

    :param clickOnce: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VChip.json))
    :param click_close: Emitted when close icon is clicked.
    :param update_modelValue: Event that is emitted when the component's model changes.
    :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VChip", children, **kwargs)
        self._attr_names += [
            "label",
            "filter",
            ("active_class", "activeClass"),
            ("append_avatar", "appendAvatar"),
            ("append_icon", "appendIcon"),
            "closable",
            ("close_icon", "closeIcon"),
            ("close_label", "closeLabel"),
            "draggable",
            ("filter_icon", "filterIcon"),
            "link",
            "pill",
            ("prepend_avatar", "prependAvatar"),
            ("prepend_icon", "prependIcon"),
            "ripple",
            "value",
            "text",
            ("model_value", "modelValue"),
            "border",
            "density",
            "elevation",
            "disabled",
            ("selected_class", "selectedClass"),
            "rounded",
            "tile",
            "href",
            "replace",
            "exact",
            "to",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
        ]
        self._event_names += [
            "click",
            "clickOnce",
            ("click_close", "click:close"),
            ("update_modelValue", "update:modelValue"),
            ("group_selected", "group:selected"),
        ]


class VChipGroup(HtmlElement):
    """
    Vuetify's VChipGroup component. See more info and examples |VChipGroup_vuetify_link|.

    .. |VChipGroup_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-chip-group" target="_blank">here</a>


    :param symbol: See description |VChipGroup_vuetify_link|.
    :type any:
    :param column: Remove horizontal pagination and wrap items as needed.
    :type boolean:
    :param filter: Applies an checkmark icon in front of every chip for using it like a filter.
    :type boolean:
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :type (a: any, b: any) => boolean:
    :param center_active: Forces the selected chip to be centered.
    :type boolean:
    :param direction: Switch between horizontal and vertical modes.
    :type 'horizontal' | 'vertical':
    :param next_icon: Specify the icon to use for the next icon.
    :type any:
    :param prev_icon: Specify the icon to use for the prev icon.
    :type any:
    :param show_arrows: Force the display of the pagination arrows.
    :type string | boolean:
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :type boolean:
    :param mobile_breakpoint: Sets the designated mobile breakpoint for the component.
    :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param multiple: Allows one to select multiple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param disabled: Puts all children components into a disabled state.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VChipGroup_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'elevated' | 'tonal' | 'outlined' | 'text' | 'plain':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VChipGroup", children, **kwargs)
        self._attr_names += [
            "symbol",
            "column",
            "filter",
            ("value_comparator", "valueComparator"),
            ("center_active", "centerActive"),
            "direction",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "tag",
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
            "theme",
            "color",
            "variant",
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
    :type any:
    :param tag: Specify a custom tag used on the root element.
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


    :param tag: Specify a custom tag used on the root element.
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
    :param offset: Sets the default offset for the column.
    :type string | number:
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
    :param order: See description |VCol_vuetify_link|.
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
    :type 'auto' | 'start' | 'end' | 'center' | 'baseline' | 'stretch':
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCol", children, **kwargs)
        self._attr_names += [
            "cols",
            "sm",
            "md",
            "lg",
            "xl",
            "xxl",
            "offset",
            ("offset_sm", "offsetSm"),
            ("offset_md", "offsetMd"),
            ("offset_lg", "offsetLg"),
            ("offset_xl", "offsetXl"),
            ("offset_xxl", "offsetXxl"),
            "order",
            ("order_sm", "orderSm"),
            ("order_md", "orderMd"),
            ("order_lg", "orderLg"),
            ("order_xl", "orderXl"),
            ("order_xxl", "orderXxl"),
            ("align_self", "alignSelf"),
            "tag",
        ]
        self._event_names += []


class VColorPicker(HtmlElement):
    """
        Vuetify's VColorPicker component. See more info and examples |VColorPicker_vuetify_link|.

        .. |VColorPicker_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-color-picker" target="_blank">here</a>


        :param canvas_height: Height of canvas.
        :type string | number:
        :param disabled: Removes the ability to click or target the component.
        :type boolean:
        :param dot_size: Changes the size of the selection dot on the canvas.
        :type string | number:
        :param hide_canvas: Hides canvas.
        :type boolean:
        :param hide_sliders: Hides sliders.
        :type boolean:
        :param hide_inputs: Hides inputs.
        :type boolean:
        :param mode: The current selected input type. Syncable with `v-model:mode`.
        :type 'rgb' | 'rgba' | 'hsl' | 'hsla' | 'hex' | 'hexa':
        :param modes: Sets available input types.
        :type ('rgb' | 'rgba' | 'hsl' | 'hsla' | 'hex' | 'hexa')[]:
        :param show_swatches: Displays color swatches.
        :type boolean:
        :param swatches_max_height: Sets the maximum height of the swatches section.
        :type string | number:
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
        :type string | Record<string, unknown>:
        :param color: See description |VColorPicker_vuetify_link|.
        :type string:
        :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
        :type string | number | boolean:
        :param width: Sets the width of the color picker.
        :type string | number:
        :param elevation: See description |VColorPicker_vuetify_link|.
        :type string | number:
        :param position: Sets the position for the component.
        :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
        :param rounded: See description |VColorPicker_vuetify_link|.
        :type string | number | boolean:
        :param tile: Removes any applied **border-radius** from the component.
        :type boolean:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children.
        :type string:
        :param swatches: Sets the available color swatches to select from. 2D array of rows and columns, accepts any color format the picker does.
        :type (
      | string
      | number
      | {
          readonly h: number
          readonly s: number
          readonly v: number
          readonly a?: number | undefined
        }
      | {
          readonly r: number
          readonly g: number
          readonly b: number
          readonly a?: number | undefined
        }
      | {
          readonly h: number
          readonly s: number
          readonly l: number
          readonly a?: number | undefined
        }
    )[][]:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes.
        :param update_mode: Selected mode.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VColorPicker", children, **kwargs)
        self._attr_names += [
            ("canvas_height", "canvasHeight"),
            "disabled",
            ("dot_size", "dotSize"),
            ("hide_canvas", "hideCanvas"),
            ("hide_sliders", "hideSliders"),
            ("hide_inputs", "hideInputs"),
            "mode",
            "modes",
            ("show_swatches", "showSwatches"),
            ("swatches_max_height", "swatchesMaxHeight"),
            ("model_value", "modelValue"),
            "color",
            "border",
            "width",
            "elevation",
            "position",
            "rounded",
            "tile",
            "tag",
            "theme",
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


        :param label: See description |VCombobox_vuetify_link|.
        :type string:
        :param auto_select_first: When searching, will always highlight the first option and select it on blur. `exact` will only highlight and select exact matches.
        :type boolean | 'exact':
        :param clear_on_select: Reset the search text when a selection is made while using the **multiple** prop.
        :type boolean:
        :param type: Sets input type.
        :type string:
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'some' | 'every' | 'union' | 'intersection':
        :param no_filter: Disables all item filtering.
        :type boolean:
        :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param reverse: Reverses the orientation.
        :type boolean:
        :param flat: Removes box shadow when using a variant with elevation.
        :type boolean:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type unknown:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param chips: Changes display of selections to chips.
        :type boolean:
        :param closable_chips: See description |VCombobox_vuetify_link|.
        :type boolean:
        :param close_text: Text set to to the inputs `aria-label` and `title` when input menu is closed.
        :type string:
        :param open_text: Text set to to the inputs **aria-label** and **title** when input menu is open.
        :type string:
        :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
        :type boolean:
        :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
        :type boolean:
        :param hide_selected: Do not display in the select menu items that are already selected.
        :type boolean:
        :param list_props: See description |VCombobox_vuetify_link|.
        :type unknown:
        :param base_color: Sets the color of the input when it is not focused.
        :type string:
        :param bg_color: See description |VCombobox_vuetify_link|.
        :type string:
        :param disabled: Removes the ability to click or target the input.
        :type boolean:
        :param multiple: Changes select to multiple. Accepts array for value.
        :type boolean:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param max_width: Sets the maximum width for the component.
        :type string | number:
        :param min_width: Sets the minimum width for the component.
        :type string | number:
        :param width: Sets the width for the component.
        :type string | number:
        :param items: See description |VCombobox_vuetify_link|.
        :type any[]:
        :param item_title: Property on supplied `items` that contains its title.
        :type SelectItemKey<any>:
        :param item_value: Property on supplied `items` that contains its value.
        :type SelectItemKey<any>:
        :param item_children: This property currently has **no effect**.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L73-L77" target="_blank">SelectItemKey</a>:
        :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
        :type SelectItemKey<any>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
        :type boolean:
        :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
        :type (a: any, b: any) => boolean:
        :param rounded: Adds a border radius to the input.
        :type string | number | boolean:
        :param tile: Removes any applied **border-radius** from the component.
        :type boolean:
        :param theme: Specify a theme for this component and all of its children.
        :type string:
        :param color: See description |VCombobox_vuetify_link|.
        :type string:
        :param variant: Applies a distinct style to the component.
        :type | 'outlined'
      | 'plain'
      | 'underlined'
      | 'filled'
      | 'solo'
      | 'solo-inverted'
      | 'solo-filled':
        :param name: Sets the component's name attribute.
        :type string:
        :param menu: Renders with the menu open by default.
        :type boolean:
        :param menu_icon: Sets the the spin icon.
        :type any:
        :param menu_props: See description |VCombobox_vuetify_link|.
        :type unknown:
        :param id: Sets the DOM id on the component.
        :type string:
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
        :type any:
        :param transition: See description |VCombobox_vuetify_link|.
        :type string | boolean | (TransitionProps & { component: Component }):
        :param no_data_text: Text shown when no items are provided to the component.
        :type string:
        :param open_on_clear: Open's the menu whenever the clear icon is clicked.
        :type boolean:
        :param item_color: Sets color of selected items.
        :type string:
        :param autofocus: Enables autofocus.
        :type boolean:
        :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
        :type string | number | boolean:
        :param prefix: Displays prefix text.
        :type string:
        :param placeholder: Sets the input’s placeholder text.
        :type string:
        :param persistent_placeholder: Forces placeholder to always be visible.
        :type boolean:
        :param persistent_counter: Forces counter to always be visible.
        :type boolean:
        :param suffix: Displays suffix text.
        :type string:
        :param role: The role attribute applied to the input.
        :type string:
        :param append_icon: See description |VCombobox_vuetify_link|.
        :type any:
        :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
        :type boolean:
        :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`.
        :type any:
        :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
        :type boolean:
        :param hint: See description |VCombobox_vuetify_link|.
        :type string:
        :param persistent_hint: See description |VCombobox_vuetify_link|.
        :type boolean:
        :param messages: Displays a list of messages or a single message if using a string.
        :type string | string[]:
        :param direction: Changes the direction of the input.
        :type 'horizontal' | 'vertical':
        :param error: Puts the input in a manual error state.
        :type boolean:
        :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
        :type string | string[]:
        :param max_errors: Control the maximum number of shown errors from validation.
        :type string | number:
        :param readonly: Puts input in readonly state.
        :type boolean:
        :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
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
        :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
        :type boolean | 'auto':
        :param clearable: Allows for the component to be cleared.
        :type boolean:
        :param clear_icon: The icon used when the **clearable** prop is set to true.
        :type any:
        :param active: Controls the **active** state of the item. This is typically used to highlight the component.
        :type boolean:
        :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
        :type boolean:
        :param prepend_inner_icon: See description |VCombobox_vuetify_link|.
        :type any:
        :param single_line: Label does not move on focus/dirty.
        :type boolean:
        :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
        :type string | boolean:
        :param counter_value: Function returns the counter display text.
        :type number | ((value: any) => number):
        :param model_modifiers: **FOR INTERNAL USE ONLY**
        :type unknown:
        :param delimiters: Accepts an array of strings that will trigger a new tag when typing. Does not replace the normal Tab and Enter keys.
        :type string[]:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes.
        :param click_prepend: Emitted when prepended icon is clicked.
        :param click_append: Emitted when append icon is clicked.
        :param update_focused: Emitted when the input is focused or blurred
        :param click_clear: Emitted when clearable icon clicked.
        :param click_appendInner: Emitted when appended inner icon is clicked.
        :param click_prependInner: Emitted when prepended inner icon is clicked.
        :param update_search: Event emitted when the search value changes.
        :param update_menu: Event that is emitted when the component's menu state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCombobox", children, **kwargs)
        self._attr_names += [
            "label",
            ("auto_select_first", "autoSelectFirst"),
            ("clear_on_select", "clearOnSelect"),
            "type",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            "reverse",
            "flat",
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
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            "name",
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "id",
            ("model_value", "modelValue"),
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
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "error",
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
    :type any:
    :param tag: Specify a custom tag used on the root element.
    :type string:

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
    Vuetify's VConfirmEdit component. See more info and examples |VConfirmEdit_vuetify_link|.

    .. |VConfirmEdit_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-confirm-edit" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param color: See description |VConfirmEdit_vuetify_link|.
    :type string:
    :param cancel_text: Text for the cancel button
    :type string:
    :param ok_text: Text for the ok button
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    :param save: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VConfirmEdit.json))
    :param cancel: The event emitted when the user clicks the Cancel button
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VConfirmEdit", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "color",
            ("cancel_text", "cancelText"),
            ("ok_text", "okText"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "save",
            "cancel",
        ]


class VContainer(HtmlElement):
    """
    Vuetify's VContainer component. See more info and examples |VContainer_vuetify_link|.

    .. |VContainer_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-container" target="_blank">here</a>


    :param fluid: Removes viewport maximum-width size breakpoints.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VContainer", children, **kwargs)
        self._attr_names += [
            "fluid",
            "tag",
        ]
        self._event_names += []


class VCounter(HtmlElement):
    """
      Vuetify's VCounter component. See more info and examples |VCounter_vuetify_link|.

      .. |VCounter_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-counter" target="_blank">here</a>


      :param active: Determines whether the counter is visible or not.
      :type boolean:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param max: Sets the maximum allowed value.
      :type string | number:
      :param value: Sets the current counter value.
      :type string | number:
      :param transition: See description |VCounter_vuetify_link|.
      :type | { component: Component }
    | string
    | boolean
    | (TransitionProps & { component: Component }):

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VCounter", children, **kwargs)
        self._attr_names += [
            "active",
            "disabled",
            "max",
            "value",
            "transition",
        ]
        self._event_names += []


class VDataIterator(HtmlElement):
    """
        Vuetify's VDataIterator component. See more info and examples |VDataIterator_vuetify_link|.

        .. |VDataIterator_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-data-iterator" target="_blank">here</a>


        :param search: Text input used to filter items.
        :type string:
        :param loading: If `true` and no items are provided, then a loading text will be shown.
        :type boolean:
        :param items: An array of strings or objects used for automatically generating children components.
        :type unknown[]:
        :param item_value: Property on supplied `items` that contains its value.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L73-L77" target="_blank">SelectItemKey</a>:
        :param item_selectable: Property on supplied `items` that contains the boolean value indicating if the item is selectable.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L73-L77" target="_blank">SelectItemKey</a>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
        :type boolean:
        :param show_select: Shows the column with checkboxes for selecting items in the list.
        :type boolean:
        :param select_strategy: Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).
        :type 'single' | 'page' | 'all':
        :param page: The current displayed page number (1-indexed).
        :type string | number:
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
        :type any[]:
        :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
        :type (a: any, b: any) => boolean:
        :param sort_by: Changes which item property (or properties) should be used for sort order. Can be used with `.sync` modifier.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/composables/sort.ts#L30-L30" target="_blank">SortItem</a>[]:
        :param multi_sort: If `true` then one can sort on multiple properties.
        :type boolean:
        :param must_sort: If `true` then one can not disable sorting, it will always switch between ascending and descending.
        :type boolean:
        :param custom_key_sort: Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified.
        :type unknown:
        :param items_per_page: Changes how many items per page should be visible. Can be used with `.sync` modifier. Setting this prop to `-1` will display all items on the page.
        :type string | number:
        :param expand_on_click: Expands item when the row is clicked.
        :type boolean:
        :param show_expand: Shows the expand icon.
        :type boolean:
        :param expanded: Array of expanded items. Can be used with `.sync` modifier.
        :type string[]:
        :param group_by: Changes which item property should be used for grouping items. Currently only supports a single grouping in the format: `group` or `['group']`. When using an array, only the first element is considered. Can be used with `.sync` modifier.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/composables/sort.ts#L30-L30" target="_blank">SortItem</a>[]:
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'every' | 'some' | 'union' | 'intersection':
        :param no_filter: Disables all item filtering.
        :type boolean:
        :param custom_filter: Function to filter items.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type unknown:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param transition: See description |VDataIterator_vuetify_link|.
        :type | { component: Component; hideOnLeave: boolean }
      | string
      | boolean
      | (TransitionProps & { component: Component }):

        Events

        :param update_modelValue: Event that is emitted when the component's model changes.
        :param update_expanded: The `.sync` event for `expanded` prop.
        :param update_groupBy: The `.sync` event for `groupBy` prop.
        :param update_page: The `.sync` event for `page` prop.
        :param update_itemsPerPage: The `.sync` event for `itemsPerPage` prop.
        :param update_sortBy: The `.sync` event for `sortBy` prop.
        :param update_options: The `.sync` event for `options` prop.
        :param update_currentItems: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataIterator.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataIterator", children, **kwargs)
        self._attr_names += [
            "search",
            "loading",
            "items",
            ("item_value", "itemValue"),
            ("item_selectable", "itemSelectable"),
            ("return_object", "returnObject"),
            ("show_select", "showSelect"),
            ("select_strategy", "selectStrategy"),
            "page",
            ("model_value", "modelValue"),
            ("value_comparator", "valueComparator"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            ("items_per_page", "itemsPerPage"),
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            "tag",
            "transition",
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
        Vuetify's VDataTable component. See more info and examples |VDataTable_vuetify_link|.

        .. |VDataTable_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-data-table" target="_blank">here</a>


        :param width: Sets the width for the component.
        :type string | number:
        :param header_props: See description |VDataTable_vuetify_link|.
        :type unknown:
        :param cell_props: An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.
        :type | Record<string, any>
      | ((
          data: Pick<
            ItemKeySlot<any>,
            'value' | 'item' | 'index' | 'internalItem' | 'column'
          >,
        ) => Record<string, any>):
        :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
        :type boolean:
        :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
        :type string | boolean:
        :param headers: An array of objects that each describe a header column. See the example below for a definition of all properties.
        :type {
      readonly key?:
        | 'data-table-group'
        | 'data-table-select'
        | 'data-table-expand'
        | (string & {})
        | undefined
      readonly value?: SelectItemKey<any>
      readonly title?: string | undefined
      readonly fixed?: boolean | undefined
      readonly align?: 'start' | 'end' | 'center' | undefined
      readonly width?: string | number | undefined
      readonly minWidth?: string | undefined
      readonly maxWidth?: string | undefined
      readonly nowrap?: boolean | undefined
      readonly headerProps?: { readonly [x: string]: any } | undefined
      readonly cellProps?:
        | { readonly [x: string]: any }
        | ((
            data: Pick<
              ItemKeySlot<any>,
              'value' | 'item' | 'index' | 'internalItem'
            >,
          ) => Record<string, any>)
        | undefined
      readonly sortable?: boolean | undefined
      readonly sort?: DataTableCompareFunction<any> | undefined
      readonly sortRaw?: DataTableCompareFunction<any> | undefined
      readonly filter?: FilterFunction | undefined
      readonly mobile?: boolean | undefined
      readonly children?: readonly any[] | undefined
    }[]:
        :param page: The current displayed page number (1-indexed).
        :type string | number:
        :param items_per_page: Changes how many items per page should be visible. Can be used with `.sync` modifier. Setting this prop to `-1` will display all items on the page.
        :type string | number:
        :param loading_text: Text shown when the data is loading.
        :type string:
        :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
        :type boolean:
        :param items: An array of strings or objects used for automatically generating children components.
        :type any[]:
        :param no_data_text: Text shown when no items are provided to the component.
        :type string:
        :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
        :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
        :param row_props: An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.
        :type | Record<string, any>
      | ((
          data: Pick<ItemKeySlot<any>, 'item' | 'index' | 'internalItem'>,
        ) => Record<string, any>):
        :param hide_default_body: Hides the default body.
        :type boolean:
        :param hide_default_footer: Hides the default footer. This has no effect on `v-data-table-virtual`.
        :type boolean:
        :param hide_default_header: Hides the default header.
        :type boolean:
        :param search: Text input used to filter items.
        :type string:
        :param expand_on_click: Expands item when the row is clicked.
        :type boolean:
        :param show_expand: Shows the expand toggle in default rows.
        :type boolean:
        :param expanded: Whether the item is expanded or not.
        :type string[]:
        :param group_by: Changes which item property should be used for grouping items. Currently only supports a single grouping in the format: `group` or `['group']`. When using an array, only the first element is considered. Can be used with `.sync` modifier.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/composables/sort.ts#L30-L30" target="_blank">SortItem</a>[]:
        :param item_value: Property on supplied `items` that contains its value.
        :type SelectItemKey<any>:
        :param item_selectable: Property on supplied `items` that indicates whether the item is selectable.
        :type SelectItemKey<any>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
        :type boolean:
        :param show_select: Shows the select checkboxes in both the header and rows (if using default rows).
        :type boolean:
        :param select_strategy: Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).
        :type 'page' | 'single' | 'all':
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
        :type unknown:
        :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
        :type (a: any, b: any) => boolean:
        :param sort_by: Changes which item property (or properties) should be used for sort order. Can be used with `.sync` modifier.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/composables/sort.ts#L30-L30" target="_blank">SortItem</a>[]:
        :param multi_sort: If `true` then one can sort on multiple properties.
        :type boolean:
        :param must_sort: If `true` then one can not disable sorting, it will always switch between ascending and descending.
        :type boolean:
        :param custom_key_sort: Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified.
        :type unknown:
        :param color: See description |VDataTable_vuetify_link|.
        :type string:
        :param sticky: Sticks the header to the top of the table.
        :type boolean:
        :param disable_sort: Disables sorting completely.
        :type boolean:
        :param sort_asc_icon: Icon used for ascending sort button.
        :type any:
        :param sort_desc_icon: Icon used for descending sort button.
        :type any:
        :param fixed_header: Fixed header to top of table.
        :type boolean:
        :param fixed_footer: Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.
        :type boolean:
        :param height: Set an explicit height of table.
        :type string | number:
        :param hover: Adds a hover effects to a table rows.
        :type boolean:
        :param density: Adjusts the vertical height of the table rows.
        :type 'default' | 'comfortable' | 'compact':
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children.
        :type string:
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'every' | 'some' | 'union' | 'intersection':
        :param no_filter: Disables all item filtering.
        :type boolean:
        :param custom_filter: Function to filter items.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type unknown:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param prev_icon: Previous icon.
        :type string:
        :param next_icon: Next icon.
        :type string:
        :param first_icon: First icon.
        :type string:
        :param last_icon: Last icon.
        :type string:
        :param items_per_page_text: Text for items-per-page dropdown.
        :type string:
        :param page_text: Label for page number.
        :type string:
        :param first_page_label: Label for first page.
        :type string:
        :param prev_page_label: Label for previous page.
        :type string:
        :param next_page_label: Label for next page.
        :type string:
        :param last_page_label: Label for last page.
        :type string:
        :param items_per_page_options: Array of options to show in the items-per-page dropdown.
        :type (number | { title: string; value: number })[]:
        :param show_current_page: Show current page number between prev/next icons.
        :type boolean:

        Events

        :param update_expanded: Emits when the **expanded** property of the **options** prop is updated.
        :param update_modelValue: Emits when the component's model changes.
        :param update_page: Emits when the **page** property of the **options** prop is updated.
        :param update_itemsPerPage: Emits when the **items-per-page** property of the **options** prop is updated.
        :param update_sortBy: Emits when the **sortBy** property of the **options** prop is updated.
        :param update_options: Emits when one of the **options** properties is updated.
        :param update_groupBy: Emits when the **group-by** property of the **options** property is updated.
        :param update_currentItems: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTable.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTable", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            "width",
            ("header_props", "headerProps"),
            ("cell_props", "cellProps"),
            "mobile",
            "loading",
            "headers",
            "page",
            ("items_per_page", "itemsPerPage"),
            ("loading_text", "loadingText"),
            ("hide_no_data", "hideNoData"),
            "items",
            ("no_data_text", "noDataText"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("row_props", "rowProps"),
            ("hide_default_body", "hideDefaultBody"),
            ("hide_default_footer", "hideDefaultFooter"),
            ("hide_default_header", "hideDefaultHeader"),
            "search",
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
            ("item_value", "itemValue"),
            ("item_selectable", "itemSelectable"),
            ("return_object", "returnObject"),
            ("show_select", "showSelect"),
            ("select_strategy", "selectStrategy"),
            ("model_value", "modelValue"),
            ("value_comparator", "valueComparator"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            "color",
            "sticky",
            ("disable_sort", "disableSort"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            "height",
            "hover",
            "density",
            "tag",
            "theme",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
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
            ("update_expanded", "update:expanded"),
            ("update_modelValue", "update:modelValue"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_groupBy", "update:groupBy"),
            ("update_currentItems", "update:currentItems"),
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


class VDataTableHeaders(HtmlElement):
    """
    Vuetify's VDataTableHeaders component. See more info and examples |VDataTableHeaders_vuetify_link|.

    .. |VDataTableHeaders_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-data-table-headers" target="_blank">here</a>


    :param color: See description |VDataTableHeaders_vuetify_link|.
    :type string:
    :param sticky: Sticks the header to the top of the table.
    :type boolean:
    :param disable_sort: Toggles rendering of sort button.
    :type boolean:
    :param multi_sort: See description |VDataTableHeaders_vuetify_link|.
    :type boolean:
    :param sort_asc_icon: Icon used for ascending sort button.
    :type any:
    :param sort_desc_icon: Icon used for descending sort button.
    :type any:
    :param header_props: See description |VDataTableHeaders_vuetify_link|.
    :type unknown:
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :type boolean:
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :type string | boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableHeaders", children, **kwargs)
        self._attr_names += [
            "color",
            "sticky",
            ("disable_sort", "disableSort"),
            ("multi_sort", "multiSort"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("header_props", "headerProps"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "loading",
        ]
        self._event_names += []


class VDataTableRow(HtmlElement):
    """
      Vuetify's VDataTableRow component. See more info and examples |VDataTableRow_vuetify_link|.

      .. |VDataTableRow_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-data-table-row" target="_blank">here</a>


      :param cell_props: See description |VDataTableRow_vuetify_link|.
      :type | Record<string, any>
    | ((
        data: Pick<
          ItemKeySlot<unknown>,
          'value' | 'index' | 'item' | 'internalItem' | 'column'
        >,
      ) => Record<string, any>):
      :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
      :type boolean:
      :param index: Row index.
      :type number:
      :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
      :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
      :param item: Data (key, index and column values) of the displayed item.
      :type unknown:

      Events

      :param contextmenu: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))
      :param dblclick: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDataTableRow.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableRow", children, **kwargs)
        self._attr_names += [
            ("cell_props", "cellProps"),
            "mobile",
            "index",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "item",
        ]
        self._event_names += [
            "click",
            "contextmenu",
            "dblclick",
        ]


class VDataTableRows(HtmlElement):
    """
      Vuetify's VDataTableRows component. See more info and examples |VDataTableRows_vuetify_link|.

      .. |VDataTableRows_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-data-table-rows" target="_blank">here</a>


      :param cell_props: An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.
      :type | Record<string, any>
    | ((
        data: Pick<
          ItemKeySlot<any>,
          'value' | 'item' | 'index' | 'internalItem' | 'column'
        >,
      ) => Record<string, any>):
      :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
      :type boolean:
      :param loading: Displays `loading` slot if set to `true`
      :type string | boolean:
      :param loading_text: Text shown when the data is loading.
      :type string:
      :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
      :type boolean:
      :param items: An array of strings or objects used for automatically generating children components.
      :type (<a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/types.ts#L48-L54" target="_blank">DataTableItem</a> | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/composables/group.ts#L18-L25" target="_blank">Group</a>)[]:
      :param no_data_text: Text shown when no items are provided to the component.
      :type string:
      :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
      :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
      :param row_props: An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.
      :type | Record<string, any>
    | ((
        data: Pick<ItemKeySlot<any>, 'item' | 'index' | 'internalItem'>,
      ) => Record<string, any>):

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableRows", children, **kwargs)
        self._attr_names += [
            ("cell_props", "cellProps"),
            "mobile",
            "loading",
            ("loading_text", "loadingText"),
            ("hide_no_data", "hideNoData"),
            "items",
            ("no_data_text", "noDataText"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("row_props", "rowProps"),
        ]
        self._event_names += []


class VDataTableServer(HtmlElement):
    """
        Vuetify's VDataTableServer component. See more info and examples |VDataTableServer_vuetify_link|.

        .. |VDataTableServer_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-data-table-server" target="_blank">here</a>


        :param width: Sets the width for the component.
        :type string | number:
        :param header_props: See description |VDataTableServer_vuetify_link|.
        :type unknown:
        :param cell_props: An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.
        :type | Record<string, any>
      | ((
          data: Pick<
            ItemKeySlot<any>,
            'value' | 'item' | 'index' | 'internalItem' | 'column'
          >,
        ) => Record<string, any>):
        :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
        :type boolean:
        :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
        :type string | boolean:
        :param headers: An array of objects that each describe a header column.
        :type {
      readonly key?:
        | 'data-table-group'
        | 'data-table-select'
        | 'data-table-expand'
        | (string & {})
        | undefined
      readonly value?: SelectItemKey<Record<string, any>>
      readonly title?: string | undefined
      readonly fixed?: boolean | undefined
      readonly align?: 'start' | 'end' | 'center' | undefined
      readonly width?: string | number | undefined
      readonly minWidth?: string | undefined
      readonly maxWidth?: string | undefined
      readonly nowrap?: boolean | undefined
      readonly headerProps?: { readonly [x: string]: any } | undefined
      readonly cellProps?:
        | { readonly [x: string]: any }
        | ((
            data: Pick<
              ItemKeySlot<any>,
              'value' | 'item' | 'index' | 'internalItem'
            >,
          ) => Record<string, any>)
        | undefined
      readonly sortable?: boolean | undefined
      readonly sort?: DataTableCompareFunction<any> | undefined
      readonly sortRaw?: DataTableCompareFunction<any> | undefined
      readonly filter?: FilterFunction | undefined
      readonly mobile?: boolean | undefined
      readonly children?:
        | readonly {
            readonly key?:
              | 'data-table-group'
              | 'data-table-select'
              | 'data-table-expand'
              | (string & {})
              | undefined
            readonly value?: SelectItemKey<Record<string, any>>
            readonly title?: string | undefined
            readonly fixed?: boolean | undefined
            readonly align?: 'start' | 'end' | 'center' | undefined
            readonly width?: string | number | undefined
            readonly minWidth?: string | undefined
            readonly maxWidth?: string | undefined
            readonly nowrap?: boolean | undefined
            readonly headerProps?: { readonly [x: string]: any } | undefined
            readonly cellProps?:
              | { readonly [x: string]: any }
              | ((
                  data: Pick<
                    ItemKeySlot<any>,
                    'value' | 'item' | 'index' | 'internalItem'
                  >,
                ) => Record<string, any>)
              | undefined
            readonly sortable?: boolean | undefined
            readonly sort?: DataTableCompareFunction<any> | undefined
            readonly sortRaw?: DataTableCompareFunction<any> | undefined
            readonly filter?: FilterFunction | undefined
            readonly mobile?: boolean | undefined
            readonly children?: readonly any[] | undefined
          }[]
        | undefined
    }[]:
        :param items_length: Number of all items.
        :type string | number:
        :param page: The current displayed page number (1-indexed).
        :type string | number:
        :param items_per_page: The number of items to display on each page.
        :type string | number:
        :param loading_text: Text shown when the data is loading.
        :type string:
        :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
        :type boolean:
        :param items: An array of strings or objects used for automatically generating children components.
        :type any[]:
        :param no_data_text: Text shown when no items are provided to the component.
        :type string:
        :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
        :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
        :param row_props: An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.
        :type | Record<string, any>
      | ((
          data: Pick<ItemKeySlot<any>, 'item' | 'index' | 'internalItem'>,
        ) => Record<string, any>):
        :param hide_default_body: See description |VDataTableServer_vuetify_link|.
        :type boolean:
        :param hide_default_footer: See description |VDataTableServer_vuetify_link|.
        :type boolean:
        :param hide_default_header: See description |VDataTableServer_vuetify_link|.
        :type boolean:
        :param search: Text input used to filter items.
        :type string:
        :param expand_on_click: Expands item when the row is clicked.
        :type boolean:
        :param show_expand: Shows the expand icon.
        :type boolean:
        :param expanded: Whether the item is expanded or not.
        :type string[]:
        :param group_by: Defines the grouping of the table items.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/composables/sort.ts#L30-L30" target="_blank">SortItem</a>[]:
        :param item_value: Property on supplied `items` that contains its value.
        :type SelectItemKey<any>:
        :param item_selectable: Property on supplied `items` that indicates whether the item is selectable.
        :type SelectItemKey<any>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
        :type boolean:
        :param show_select: Shows the column with checkboxes for selecting items in the list.
        :type boolean:
        :param select_strategy: Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).
        :type 'page' | 'single' | 'all':
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
        :type unknown:
        :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
        :type (a: any, b: any) => boolean:
        :param sort_by: Array of column keys and sort orders that determines the sort order of the table.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/composables/sort.ts#L30-L30" target="_blank">SortItem</a>[]:
        :param multi_sort: Allows sorting by multiple columns.
        :type boolean:
        :param must_sort: Forces sorting on the column(s).
        :type boolean:
        :param custom_key_sort: Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified.
        :type unknown:
        :param color: See description |VDataTableServer_vuetify_link|.
        :type string:
        :param sticky: Sticks the header to the top of the table.
        :type boolean:
        :param disable_sort: Toggles rendering of sort button.
        :type boolean:
        :param sort_asc_icon: Icon used for ascending sort button.
        :type any:
        :param sort_desc_icon: Icon used for descending sort button.
        :type any:
        :param fixed_header: Use the fixed-header prop together with the height prop to fix the header to the top of the table.
        :type boolean:
        :param fixed_footer: Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.
        :type boolean:
        :param height: Use the height prop to set the height of the table.
        :type string | number:
        :param hover: Will add a hover effect to a table's row when the mouse is over it.
        :type boolean:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children.
        :type string:
        :param prev_icon: Previous icon.
        :type string:
        :param next_icon: Next icon.
        :type string:
        :param first_icon: First icon.
        :type string:
        :param last_icon: Last icon.
        :type string:
        :param items_per_page_text: Text for items-per-page dropdown.
        :type string:
        :param page_text: Label for page number.
        :type string:
        :param first_page_label: Label for first page.
        :type string:
        :param prev_page_label: Label for previous page.
        :type string:
        :param next_page_label: Label for next page.
        :type string:
        :param last_page_label: Label for last page.
        :type string:
        :param items_per_page_options: Array of options to show in the items-per-page dropdown.
        :type (number | { title: string; value: number })[]:
        :param show_current_page: Show current page number between prev/next icons.
        :type boolean:

        Events

        :param update_expanded: Emits when the **expanded** property of the **options** prop is updated.
        :param update_modelValue: Emits when the component's model changes.
        :param update_page: Emits when the **page** property of the **options** prop is updated.
        :param update_itemsPerPage: Emits when the **items-per-page** property of the **options** prop is updated.
        :param update_sortBy: Emits when the **sort-by** property of the **options** prop is updated.
        :param update_options: Emits when one of the **options** properties is updated.
        :param update_groupBy: Emits when the **group-by** property of the **options** property is updated.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableServer", children, **kwargs)
        self._attr_names += [
            "width",
            ("header_props", "headerProps"),
            ("cell_props", "cellProps"),
            "mobile",
            "loading",
            "headers",
            ("items_length", "itemsLength"),
            "page",
            ("items_per_page", "itemsPerPage"),
            ("loading_text", "loadingText"),
            ("hide_no_data", "hideNoData"),
            "items",
            ("no_data_text", "noDataText"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("row_props", "rowProps"),
            ("hide_default_body", "hideDefaultBody"),
            ("hide_default_footer", "hideDefaultFooter"),
            ("hide_default_header", "hideDefaultHeader"),
            "search",
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
            ("item_value", "itemValue"),
            ("item_selectable", "itemSelectable"),
            ("return_object", "returnObject"),
            ("show_select", "showSelect"),
            ("select_strategy", "selectStrategy"),
            ("model_value", "modelValue"),
            ("value_comparator", "valueComparator"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            "color",
            "sticky",
            ("disable_sort", "disableSort"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            "height",
            "hover",
            "density",
            "tag",
            "theme",
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
            ("update_expanded", "update:expanded"),
            ("update_modelValue", "update:modelValue"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_groupBy", "update:groupBy"),
        ]


class VDataTableVirtual(HtmlElement):
    """
        Vuetify's VDataTableVirtual component. See more info and examples |VDataTableVirtual_vuetify_link|.

        .. |VDataTableVirtual_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-data-table-virtual" target="_blank">here</a>


        :param width: Sets the width for the component.
        :type string | number:
        :param header_props: See description |VDataTableVirtual_vuetify_link|.
        :type unknown:
        :param cell_props: An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.
        :type | Record<string, any>
      | ((
          data: Pick<
            ItemKeySlot<any>,
            'value' | 'item' | 'index' | 'internalItem' | 'column'
          >,
        ) => Record<string, any>):
        :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
        :type boolean:
        :param headers: An array of objects that each describe a header column.
        :type {
      readonly key?:
        | 'data-table-group'
        | 'data-table-select'
        | 'data-table-expand'
        | (string & {})
        | undefined
      readonly value?: SelectItemKey<Record<string, any>>
      readonly title?: string | undefined
      readonly fixed?: boolean | undefined
      readonly align?: 'start' | 'end' | 'center' | undefined
      readonly width?: string | number | undefined
      readonly minWidth?: string | undefined
      readonly maxWidth?: string | undefined
      readonly nowrap?: boolean | undefined
      readonly headerProps?: { readonly [x: string]: any } | undefined
      readonly cellProps?:
        | { readonly [x: string]: any }
        | ((
            data: Pick<
              ItemKeySlot<any>,
              'value' | 'item' | 'index' | 'internalItem'
            >,
          ) => Record<string, any>)
        | undefined
      readonly sortable?: boolean | undefined
      readonly sort?: DataTableCompareFunction<any> | undefined
      readonly sortRaw?: DataTableCompareFunction<any> | undefined
      readonly filter?: FilterFunction | undefined
      readonly mobile?: boolean | undefined
      readonly children?:
        | readonly {
            readonly key?:
              | 'data-table-group'
              | 'data-table-select'
              | 'data-table-expand'
              | (string & {})
              | undefined
            readonly value?: SelectItemKey<Record<string, any>>
            readonly title?: string | undefined
            readonly fixed?: boolean | undefined
            readonly align?: 'start' | 'end' | 'center' | undefined
            readonly width?: string | number | undefined
            readonly minWidth?: string | undefined
            readonly maxWidth?: string | undefined
            readonly nowrap?: boolean | undefined
            readonly headerProps?: { readonly [x: string]: any } | undefined
            readonly cellProps?:
              | { readonly [x: string]: any }
              | ((
                  data: Pick<
                    ItemKeySlot<any>,
                    'value' | 'item' | 'index' | 'internalItem'
                  >,
                ) => Record<string, any>)
              | undefined
            readonly sortable?: boolean | undefined
            readonly sort?: DataTableCompareFunction<any> | undefined
            readonly sortRaw?: DataTableCompareFunction<any> | undefined
            readonly filter?: FilterFunction | undefined
            readonly mobile?: boolean | undefined
            readonly children?: readonly any[] | undefined
          }[]
        | undefined
    }[]:
        :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
        :type string | boolean:
        :param loading_text: Text shown when the data is loading.
        :type string:
        :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
        :type boolean:
        :param items: An array of strings or objects used for automatically generating children components.
        :type any[]:
        :param no_data_text: Text shown when no items are provided to the component.
        :type string:
        :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
        :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
        :param row_props: An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.
        :type | Record<string, any>
      | ((
          data: Pick<ItemKeySlot<any>, 'item' | 'index' | 'internalItem'>,
        ) => Record<string, any>):
        :param hide_default_body: See description |VDataTableVirtual_vuetify_link|.
        :type boolean:
        :param hide_default_footer: See description |VDataTableVirtual_vuetify_link|.
        :type boolean:
        :param hide_default_header: See description |VDataTableVirtual_vuetify_link|.
        :type boolean:
        :param search: Text input used to filter items.
        :type string:
        :param expand_on_click: Expands item when the row is clicked.
        :type boolean:
        :param show_expand: Shows the expand icon.
        :type boolean:
        :param expanded: Whether the item is expanded or not.
        :type string[]:
        :param group_by: Defines the grouping of the table items.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/composables/sort.ts#L30-L30" target="_blank">SortItem</a>[]:
        :param item_value: Property on supplied `items` that contains its value.
        :type SelectItemKey<any>:
        :param item_selectable: Property on supplied `items` that indicates whether the item is selectable.
        :type SelectItemKey<any>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
        :type boolean:
        :param show_select: Shows the column with checkboxes for selecting items in the list.
        :type boolean:
        :param select_strategy: Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).
        :type 'single' | 'page' | 'all':
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
        :type unknown:
        :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
        :type (a: any, b: any) => boolean:
        :param sort_by: Array of column keys and sort orders that determines the sort order of the table.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VDataTable/composables/sort.ts#L30-L30" target="_blank">SortItem</a>[]:
        :param multi_sort: Allows sorting by multiple columns.
        :type boolean:
        :param must_sort: Forces sorting on the column(s).
        :type boolean:
        :param custom_key_sort: Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified.
        :type unknown:
        :param color: See description |VDataTableVirtual_vuetify_link|.
        :type string:
        :param sticky: Sticks the header to the top of the table.
        :type boolean:
        :param disable_sort: Toggles rendering of sort button.
        :type boolean:
        :param sort_asc_icon: Icon used for ascending sort button.
        :type any:
        :param sort_desc_icon: Icon used for descending sort button.
        :type any:
        :param fixed_header: Use the fixed-header prop together with the height prop to fix the header to the top of the table.
        :type boolean:
        :param fixed_footer: Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.
        :type boolean:
        :param height: Use the height prop to set the height of the table.
        :type string | number:
        :param hover: Will add a hover effect to a table's row when the mouse is over it.
        :type boolean:
        :param density: Adjusts the vertical height used by the component.
        :type 'default' | 'comfortable' | 'compact':
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children.
        :type string:
        :param item_height: Height in pixels of each item to display.
        :type string | number:
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
        :type unknown:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:

        Events

        :param update_expanded: Emits when the **expanded** property of the **options** prop is updated.
        :param update_modelValue: Emits when the component's model changes.
        :param update_sortBy: Emits when the **sort-by** property of the **options** prop is updated.
        :param update_options: Emits when one of the **options** properties is updated.
        :param update_groupBy: Emits when the **group-by** property of the **options** property is updated.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDataTableVirtual", children, **kwargs)
        self._attr_names += [
            "width",
            ("header_props", "headerProps"),
            ("cell_props", "cellProps"),
            "mobile",
            "headers",
            "loading",
            ("loading_text", "loadingText"),
            ("hide_no_data", "hideNoData"),
            "items",
            ("no_data_text", "noDataText"),
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("row_props", "rowProps"),
            ("hide_default_body", "hideDefaultBody"),
            ("hide_default_footer", "hideDefaultFooter"),
            ("hide_default_header", "hideDefaultHeader"),
            "search",
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
            ("item_value", "itemValue"),
            ("item_selectable", "itemSelectable"),
            ("return_object", "returnObject"),
            ("show_select", "showSelect"),
            ("select_strategy", "selectStrategy"),
            ("model_value", "modelValue"),
            ("value_comparator", "valueComparator"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("custom_key_sort", "customKeySort"),
            "color",
            "sticky",
            ("disable_sort", "disableSort"),
            ("sort_asc_icon", "sortAscIcon"),
            ("sort_desc_icon", "sortDescIcon"),
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            "height",
            "hover",
            "density",
            "tag",
            "theme",
            ("item_height", "itemHeight"),
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
        ]
        self._event_names += [
            ("update_expanded", "update:expanded"),
            ("update_modelValue", "update:modelValue"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_groupBy", "update:groupBy"),
        ]


class VDateInput(HtmlElement):
    """
      Vuetify's VDateInput component. See more info and examples |VDateInput_vuetify_link|.

      .. |VDateInput_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-date-input" target="_blank">here</a>


      :param flat: Removes box shadow when using a variant with elevation.
      :type boolean:
      :param hide_actions: See description |VDateInput_vuetify_link|.
      :type boolean:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param reverse: Reverses the orientation.
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type any:
      :param color: See description |VDateInput_vuetify_link|.
      :type string:
      :param cancel_text: Text for the cancel button
      :type string:
      :param type: Determines the type of the picker - `date` for date picker, `month` for month picker.
      :type string:
      :param ok_text: Text for the ok button
      :type string:
      :param autofocus: Enables autofocus.
      :type boolean:
      :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
      :type string | number | boolean:
      :param prefix: Displays prefix text.
      :type string:
      :param placeholder: Sets the input’s placeholder text.
      :type string:
      :param persistent_placeholder: Forces placeholder to always be visible.
      :type boolean:
      :param persistent_counter: Forces counter to always be visible.
      :type boolean:
      :param suffix: Displays suffix text.
      :type string:
      :param role: The role attribute applied to the input.
      :type string:
      :param text: Specify content text for the component.
      :type string:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VDateInput_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VDateInput_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VDateInput_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param height: Sets the height of the input.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Width of the picker.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the input.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param label: See description |VDateInput_vuetify_link|.
      :type string:
      :param readonly: Makes the picker readonly (doesn't allow to select new date).
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param append_inner_icon: See description |VDateInput_vuetify_link|.
      :type any:
      :param bg_color: See description |VDateInput_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared.
      :type boolean:
      :param clear_icon: The icon used when the **clearable** prop is set to true.
      :type any:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component.
      :type boolean:
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param dirty: Manually apply the dirty state styling.
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
      :type boolean:
      :param prepend_inner_icon: See description |VDateInput_vuetify_link|.
      :type any:
      :param single_line: Label does not move on focus/dirty.
      :type boolean:
      :param variant: Applies a distinct style to the component.
      :type | 'underlined'
    | 'outlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled'
    | 'plain':
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
      :type string | boolean:
      :param rounded: Adds a border radius to the input.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param counter_value: Function returns the counter display text.
      :type number | ((value: any) => number):
      :param model_modifiers: **FOR INTERNAL USE ONLY**
      :type unknown:
      :param header: Text shown when no **display-date** is set.
      :type string:
      :param next_icon: Sets the icon for next month/year button.
      :type string:
      :param prev_icon: Sets the icon for previous month/year button.
      :type string:
      :param mode_icon: Icon displayed next to the current month and year, toggles year selection when clicked.
      :type string:
      :param view_mode: Determines which picker in the date or month picker is being displayed. Allowed values: `'month'`, `'months'`, `'year'`.
      :type 'month' | 'months' | 'year':
      :param month: The current month number to show
      :type string | number:
      :param year: The current year number to show
      :type number:
      :param hide_weekdays: Hide the days of the week letters.
      :type boolean:
      :param show_week: Toggles visibility of the week numbers in the body of the calendar.
      :type boolean:
      :param transition: The transition used when changing months into the future
      :type string:
      :param reverse_transition: The transition used when changing months into the past
      :type string:
      :param show_adjacent_months: Toggles visibility of days from previous and next months.
      :type boolean:
      :param weekdays: An array of weekdays to display.
      :type number[]:
      :param weeks_in_month: A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.
      :type 'dynamic' | 'static':
      :param allowed_dates: Restricts which dates can be selected.
      :type unknown[] | ((date: unknown) => boolean):
      :param display_value: The value that determines the month to show. This is different from modelValue, which determines the selected value.
      :type unknown:
      :param max: Maximum allowed date/month (ISO 8601 format).
      :type unknown:
      :param min: Minimum allowed date/month (ISO 8601 format).
      :type unknown:
      :param multiple: Allow the selection of multiple dates. The **range** value selects all dates between two selections.
      :type number | boolean | (string & {}) | 'range':
      :param landscape: Puts the picker into landscape mode.
      :type boolean:
      :param title: Specify a title text for the component.
      :type string:
      :param hide_header: Hide the picker header.
      :type boolean:
      :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
      :type string | number | boolean:
      :param elevation: See description |VDateInput_vuetify_link|.
      :type string | number:
      :param location: Specifies the component's location. Can combine by using a space separated string.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param position: Sets the position for the component.
      :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
      :param tag: Specify a custom tag used on the root element.
      :type string:

      Events

      :param update_focused: Emitted when the input is focused or blurred
      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when append icon is clicked.
      :param click_clear: Emitted when clearable icon clicked.
      :param click_appendInner: Emitted when appended inner icon is clicked.
      :param click_prependInner: Emitted when prepended inner icon is clicked.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDateInput", children, **kwargs)
        self._attr_names += [
            "flat",
            ("hide_actions", "hideActions"),
            "focused",
            "reverse",
            ("model_value", "modelValue"),
            "color",
            ("cancel_text", "cancelText"),
            "type",
            ("ok_text", "okText"),
            "autofocus",
            "counter",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            "role",
            "text",
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "label",
            "readonly",
            "rules",
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            ("base_color", "baseColor"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "loading",
            "rounded",
            "tile",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
            "header",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("mode_icon", "modeIcon"),
            ("view_mode", "viewMode"),
            "month",
            "year",
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
            "transition",
            ("reverse_transition", "reverseTransition"),
            ("show_adjacent_months", "showAdjacentMonths"),
            "weekdays",
            ("weeks_in_month", "weeksInMonth"),
            ("allowed_dates", "allowedDates"),
            ("display_value", "displayValue"),
            "max",
            "min",
            "multiple",
            "landscape",
            "title",
            ("hide_header", "hideHeader"),
            "border",
            "elevation",
            "location",
            "position",
            "tag",
        ]
        self._event_names += [
            ("update_focused", "update:focused"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_modelValue", "update:modelValue"),
        ]


class VDatePicker(HtmlElement):
    """
    Vuetify's VDatePicker component. See more info and examples |VDatePicker_vuetify_link|.

    .. |VDatePicker_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker" target="_blank">here</a>


    :param header: Text shown when no **display-date** is set.
    :type string:
    :param title: Specify a title text for the component.
    :type string:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type string | string[]:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param next_icon: Sets the icon for next month/year button.
    :type string:
    :param prev_icon: Sets the icon for previous month/year button.
    :type string:
    :param mode_icon: Icon displayed next to the current month and year, toggles year selection when clicked.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param view_mode: Determines which picker in the date or month picker is being displayed. Allowed values: `'month'`, `'months'`, `'year'`.
    :type 'month' | 'months' | 'year':
    :param month: The current month number to show
    :type string | number:
    :param year: The current year number to show
    :type number:
    :param color: See description |VDatePicker_vuetify_link|.
    :type string:
    :param hide_weekdays: Hide the days of the week letters.
    :type boolean:
    :param show_week: Toggles visibility of the week numbers in the body of the calendar.
    :type boolean:
    :param transition: The transition used when changing months into the future
    :type string:
    :param reverse_transition: The transition used when changing months into the past
    :type string:
    :param show_adjacent_months: Toggles visibility of days from previous and next months.
    :type boolean:
    :param weekdays: An array of weekdays to display.
    :type number[]:
    :param weeks_in_month: A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.
    :type 'dynamic' | 'static':
    :param allowed_dates: Restricts which dates can be selected.
    :type unknown[] | ((date: unknown) => boolean):
    :param display_value: The value that determines the month to show. This is different from modelValue, which determines the selected value.
    :type unknown:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param max: Maximum allowed date/month (ISO 8601 format).
    :type unknown:
    :param min: Minimum allowed date/month (ISO 8601 format).
    :type unknown:
    :param multiple: Allow the selection of multiple dates. The **range** value selects all dates between two selections.
    :type number | boolean | (string & {}) | 'range':
    :param height: Sets the height for the component.
    :type string | number:
    :param bg_color: See description |VDatePicker_vuetify_link|.
    :type string:
    :param landscape: Puts the picker into landscape mode.
    :type boolean:
    :param hide_header: Hide the picker header.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
    :type string | number | boolean:
    :param max_height: Sets the maximum height for the component.
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Width of the picker.
    :type string | number:
    :param elevation: See description |VDatePicker_vuetify_link|.
    :type string | number:
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VDatePicker_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    :param update_month: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePicker.json))
    :param update_year: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePicker.json))
    :param update_viewMode: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePicker.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePicker", children, **kwargs)
        self._attr_names += [
            "header",
            "title",
            "active",
            "disabled",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("mode_icon", "modeIcon"),
            "text",
            ("view_mode", "viewMode"),
            "month",
            "year",
            "color",
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
            "transition",
            ("reverse_transition", "reverseTransition"),
            ("show_adjacent_months", "showAdjacentMonths"),
            "weekdays",
            ("weeks_in_month", "weeksInMonth"),
            ("allowed_dates", "allowedDates"),
            ("display_value", "displayValue"),
            ("model_value", "modelValue"),
            "max",
            "min",
            "multiple",
            "height",
            ("bg_color", "bgColor"),
            "landscape",
            ("hide_header", "hideHeader"),
            "border",
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
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_month", "update:month"),
            ("update_year", "update:year"),
            ("update_viewMode", "update:viewMode"),
        ]


class VDatePickerControls(HtmlElement):
    """
    Vuetify's VDatePickerControls component. See more info and examples |VDatePickerControls_vuetify_link|.

    .. |VDatePickerControls_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker-controls" target="_blank">here</a>


    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type string | string[]:
    :param disabled: Removes the ability to click or target the component.
    :type string | boolean | string[]:
    :param next_icon: See description |VDatePickerControls_vuetify_link|.
    :type string:
    :param prev_icon: See description |VDatePickerControls_vuetify_link|.
    :type string:
    :param mode_icon: See description |VDatePickerControls_vuetify_link|.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param view_mode: See description |VDatePickerControls_vuetify_link|.
    :type 'month' | 'months' | 'year':

    Events

    :param click_year: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
    :param click_month: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
    :param click_prev: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
    :param click_next: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
    :param click_text: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerControls.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerControls", children, **kwargs)
        self._attr_names += [
            "active",
            "disabled",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("mode_icon", "modeIcon"),
            "text",
            ("view_mode", "viewMode"),
        ]
        self._event_names += [
            ("click_year", "click:year"),
            ("click_month", "click:month"),
            ("click_prev", "click:prev"),
            ("click_next", "click:next"),
            ("click_text", "click:text"),
        ]


class VDatePickerHeader(HtmlElement):
    """
    Vuetify's VDatePickerHeader component. See more info and examples |VDatePickerHeader_vuetify_link|.

    .. |VDatePickerHeader_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker-header" target="_blank">here</a>


    :param append_icon: See description |VDatePickerHeader_vuetify_link|.
    :type string:
    :param color: See description |VDatePickerHeader_vuetify_link|.
    :type string:
    :param header: See description |VDatePickerHeader_vuetify_link|.
    :type string:
    :param transition: See description |VDatePickerHeader_vuetify_link|.
    :type string:

    Events

    :param click_append: Emitted when appended icon is clicked.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerHeader", children, **kwargs)
        self._attr_names += [
            ("append_icon", "appendIcon"),
            "color",
            "header",
            "transition",
        ]
        self._event_names += [
            "click",
            ("click_append", "click:append"),
        ]


class VDatePickerMonth(HtmlElement):
    """
    Vuetify's VDatePickerMonth component. See more info and examples |VDatePickerMonth_vuetify_link|.

    .. |VDatePickerMonth_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker-month" target="_blank">here</a>


    :param color: See description |VDatePickerMonth_vuetify_link|.
    :type string:
    :param hide_weekdays: Hide the days of the week letters.
    :type boolean:
    :param show_week: See description |VDatePickerMonth_vuetify_link|.
    :type boolean:
    :param transition: The transition used when changing months into the future
    :type string:
    :param reverse_transition: The transition used when changing months into the past
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param month: The current month number to show
    :type string | number:
    :param show_adjacent_months: See description |VDatePickerMonth_vuetify_link|.
    :type boolean:
    :param year: The current year number to show
    :type string | number:
    :param weekdays: An array of weekdays to display.
    :type number[]:
    :param weeks_in_month: A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.
    :type 'dynamic' | 'static':
    :param allowed_dates: See description |VDatePickerMonth_vuetify_link|.
    :type unknown[] | ((date: unknown) => boolean):
    :param display_value: The value that determines the month to show. This is different from modelValue, which determines the selected value.
    :type unknown:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown[]:
    :param max: See description |VDatePickerMonth_vuetify_link|.
    :type unknown:
    :param min: See description |VDatePickerMonth_vuetify_link|.
    :type unknown:
    :param multiple: See description |VDatePickerMonth_vuetify_link|.
    :type number | boolean | 'range' | (string & {}):

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    :param update_month: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerMonth.json))
    :param update_year: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VDatePickerMonth.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerMonth", children, **kwargs)
        self._attr_names += [
            "color",
            ("hide_weekdays", "hideWeekdays"),
            ("show_week", "showWeek"),
            "transition",
            ("reverse_transition", "reverseTransition"),
            "disabled",
            "month",
            ("show_adjacent_months", "showAdjacentMonths"),
            "year",
            "weekdays",
            ("weeks_in_month", "weeksInMonth"),
            ("allowed_dates", "allowedDates"),
            ("display_value", "displayValue"),
            ("model_value", "modelValue"),
            "max",
            "min",
            "multiple",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_month", "update:month"),
            ("update_year", "update:year"),
        ]


class VDatePickerMonths(HtmlElement):
    """
    Vuetify's VDatePickerMonths component. See more info and examples |VDatePickerMonths_vuetify_link|.

    .. |VDatePickerMonths_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker-months" target="_blank">here</a>


    :param color: See description |VDatePickerMonths_vuetify_link|.
    :type string:
    :param height: Sets the height for the component.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type number:
    :param year: See description |VDatePickerMonths_vuetify_link|.
    :type number:
    :param min: See description |VDatePickerMonths_vuetify_link|.
    :type unknown:
    :param max: See description |VDatePickerMonths_vuetify_link|.
    :type unknown:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerMonths", children, **kwargs)
        self._attr_names += [
            "color",
            "height",
            ("model_value", "modelValue"),
            "year",
            "min",
            "max",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VDatePickerYears(HtmlElement):
    """
    Vuetify's VDatePickerYears component. See more info and examples |VDatePickerYears_vuetify_link|.

    .. |VDatePickerYears_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-date-picker-years" target="_blank">here</a>


    :param color: See description |VDatePickerYears_vuetify_link|.
    :type string:
    :param height: Sets the height for the component.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type number:
    :param min: See description |VDatePickerYears_vuetify_link|.
    :type unknown:
    :param max: See description |VDatePickerYears_vuetify_link|.
    :type unknown:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDatePickerYears", children, **kwargs)
        self._attr_names += [
            "color",
            "height",
            ("model_value", "modelValue"),
            "min",
            "max",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VDefaultsProvider(HtmlElement):
    """
        Vuetify's VDefaultsProvider component. See more info and examples |VDefaultsProvider_vuetify_link|.

        .. |VDefaultsProvider_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-defaults-provider" target="_blank">here</a>


        :param disabled: Turns off all calculations of new default values for improved performance in situations where defaults propagation isn't necessary.
        :type boolean:
        :param reset: Reset the default values up the nested chain by {n} amount.
        :type string | number:
        :param root: Force current defaults to match the application root defaults.
        :type string | boolean:
        :param scoped: Prevents the ability for default values to be inherited from parent components.
        :type boolean:
        :param defaults: Specify new default prop values for components. Keep in mind that this will be merged with previously defined values.
        :type {
      global: Record<string, unknown>
      [string]: Record<string, unknown>
    }:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDefaultsProvider", children, **kwargs)
        self._attr_names += [
            "disabled",
            "reset",
            "root",
            "scoped",
            "defaults",
        ]
        self._event_names += []


class VDialog(HtmlElement):
    """
      Vuetify's VDialog component. See more info and examples |VDialog_vuetify_link|.

      .. |VDialog_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-dialog" target="_blank">here</a>


      :param activator: Explicitly sets the overlay's activator.
      :type Element | 'parent' | (string & {}) | ComponentPublicInstance:
      :param fullscreen: Changes layout for fullscreen display.
      :type boolean:
      :param retain_focus: Tab focus will return to the first child of the dialog by default. Disable this when using external tools that require focus such as TinyMCE or vue-clipboard.
      :type boolean:
      :param scrollable: See description |VDialog_vuetify_link|.
      :type boolean:
      :param absolute: Applies **position: absolute** to the content element.
      :type boolean:
      :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
      :type boolean:
      :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
      :type boolean:
      :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
      :type any:
      :param content_props: Apply custom properties to the content.
      :type any:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param opacity: Sets the overlay opacity.
      :type string | number:
      :param no_click_animation: Disables the bounce effect when clicking outside of a `v-dialog`'s content when using the **persistent** prop.
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type boolean:
      :param persistent: Clicking outside of the element or pressing **esc** key will not deactivate it.
      :type boolean:
      :param scrim: Accepts true/false to enable background, and string to define color.
      :type string | boolean:
      :param z_index: The z-index used for the component.
      :type string | number:
      :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
      :type | Element
    | 'parent'
    | 'cursor'
    | (string & {})
    | ComponentPublicInstance
    | [number, number]:
      :param activator_props: Apply custom properties to the activator.
      :type unknown:
      :param open_on_click: Activate the component when the activator is clicked.
      :type boolean:
      :param open_on_hover: Designates whether component should activate when its activator is hovered.
      :type boolean:
      :param open_on_focus: Activate the component when the activator is focused.
      :type boolean:
      :param close_on_content_click: Closes component when you click on its content.
      :type boolean:
      :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
      :type string | number:
      :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
      :type string | number:
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
      :param location_strategy: A function used to specifies how the component should position relative to its activator.
      :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
      :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param origin: See description |VDialog_vuetify_link|.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
      :param offset: A single value that offsets content away from the target based upon what side it is on.
      :type string | number | number[]:
      :param scroll_strategy: Strategy used when the component is activate and user scrolls.
      :type 'none' | 'close' | 'block' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param transition: See description |VDialog_vuetify_link|.
      :type | { component: Component }
    | string
    | boolean
    | (TransitionProps & { component: Component }):
      :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
      :type string | boolean | Element:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes.
      :param afterLeave: Event that fires after the overlay has finished transitioning out.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialog", children, **kwargs)
        self._attr_names += [
            "activator",
            "fullscreen",
            ("retain_focus", "retainFocus"),
            "scrollable",
            "absolute",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
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
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "eager",
            ("location_strategy", "locationStrategy"),
            "location",
            "origin",
            "offset",
            ("scroll_strategy", "scrollStrategy"),
            "theme",
            "transition",
            "attach",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "afterLeave",
        ]


class VDialogBottomTransition(HtmlElement):
    """
    Vuetify's VDialogBottomTransition component. See more info and examples |VDialogBottomTransition_vuetify_link|.

    .. |VDialogBottomTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog-bottom-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VDialogBottomTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VDialogBottomTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VDialogBottomTransition_vuetify_link|.
    :type string:
    :param origin: See description |VDialogBottomTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialogBottomTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VDialogTopTransition(HtmlElement):
    """
    Vuetify's VDialogTopTransition component. See more info and examples |VDialogTopTransition_vuetify_link|.

    .. |VDialogTopTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog-top-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VDialogTopTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VDialogTopTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VDialogTopTransition_vuetify_link|.
    :type string:
    :param origin: See description |VDialogTopTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDialogTopTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VDialogTransition(HtmlElement):
    """
    Vuetify's VDialogTransition component. See more info and examples |VDialogTransition_vuetify_link|.

    .. |VDialogTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog-transition" target="_blank">here</a>


    :param target: See description |VDialogTransition_vuetify_link|.
    :type HTMLElement | [number, number]:

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
    :param color: See description |VDivider_vuetify_link|.
    :type string:
    :param inset: Adds indentation (72px) for **normal** dividers, reduces max height for **vertical**.
    :type boolean:
    :param opacity: Sets the component's opacity value
    :type string | number:
    :param thickness: Sets the dividers thickness. Default unit is px.
    :type string | number:
    :param vertical: Displays dividers vertically.
    :type boolean:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VDivider", children, **kwargs)
        self._attr_names += [
            "length",
            "color",
            "inset",
            "opacity",
            "thickness",
            "vertical",
            "theme",
        ]
        self._event_names += []


class VEmptyState(HtmlElement):
    """
    Vuetify's VEmptyState component. See more info and examples |VEmptyState_vuetify_link|.

    .. |VEmptyState_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-empty-state" target="_blank">here</a>


    :param headline: A large headline often used for 404 pages.
    :type string:
    :param title: Specify a title text for the component.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param action_text: The text used for the action button.
    :type string:
    :param bg_color: See description |VEmptyState_vuetify_link|.
    :type string:
    :param color: See description |VEmptyState_vuetify_link|.
    :type string:
    :param icon: See description |VEmptyState_vuetify_link|.
    :type any:
    :param image: See description |VEmptyState_vuetify_link|.
    :type string:
    :param justify: Control the justification of the text.
    :type 'start' | 'center' | 'end':
    :param text_width: Sets the width of the text container.
    :type string | number:
    :param href: The URL the action button links to.
    :type string:
    :param to: The URL the action button links to.
    :type string:
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
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param click_action: Event emitted when the action button is clicked.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VEmptyState", children, **kwargs)
        self._attr_names += [
            "headline",
            "title",
            "text",
            ("action_text", "actionText"),
            ("bg_color", "bgColor"),
            "color",
            "icon",
            "image",
            "justify",
            ("text_width", "textWidth"),
            "href",
            "to",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "size",
            "theme",
        ]
        self._event_names += [
            ("click_action", "click:action"),
        ]


class VExpandTransition(HtmlElement):
    """
    Vuetify's VExpandTransition component. See more info and examples |VExpandTransition_vuetify_link|.

    .. |VExpandTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expand-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VExpandTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VExpandTransition_vuetify_link|.
    :type 'default' | 'in-out' | 'out-in':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpandTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            "mode",
        ]
        self._event_names += []


class VExpandXTransition(HtmlElement):
    """
    Vuetify's VExpandXTransition component. See more info and examples |VExpandXTransition_vuetify_link|.

    .. |VExpandXTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expand-x-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VExpandXTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VExpandXTransition_vuetify_link|.
    :type 'default' | 'in-out' | 'out-in':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpandXTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            "mode",
        ]
        self._event_names += []


class VExpansionPanel(HtmlElement):
    """
    Vuetify's VExpansionPanel component. See more info and examples |VExpansionPanel_vuetify_link|.

    .. |VExpansionPanel_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expansion-panel" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param bg_color: See description |VExpansionPanel_vuetify_link|.
    :type string:
    :param elevation: See description |VExpansionPanel_vuetify_link|.
    :type string | number:
    :param value: Controls the opened/closed state of content.
    :type any:
    :param disabled: Disables the expansion-panel content.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param rounded: See description |VExpansionPanel_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param color: See description |VExpansionPanel_vuetify_link|.
    :type string:
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :type any:
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :type any:
    :param hide_actions: Hide the expand icon in the content title.
    :type boolean:
    :param focusable: See description |VExpansionPanel_vuetify_link|.
    :type boolean:
    :param static: Remove title size expansion when selected.
    :type boolean:
    :param ripple: See description |VExpansionPanel_vuetify_link|.
    :type boolean | { class: string }:
    :param readonly: Makes the expansion-panel content read only.
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:

    Events

    :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanel", children, **kwargs)
        self._attr_names += [
            "title",
            "text",
            ("bg_color", "bgColor"),
            "elevation",
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "rounded",
            "tile",
            "tag",
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("hide_actions", "hideActions"),
            "focusable",
            "static",
            "ripple",
            "readonly",
            "eager",
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
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :type any:
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :type any:
    :param hide_actions: Hide the expand icon in the content title.
    :type boolean:
    :param focusable: See description |VExpansionPanelTitle_vuetify_link|.
    :type boolean:
    :param static: Remove title size expansion when selected.
    :type boolean:
    :param ripple: See description |VExpansionPanelTitle_vuetify_link|.
    :type boolean | { class: string }:
    :param readonly: See description |VExpansionPanelTitle_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanelTitle", children, **kwargs)
        self._attr_names += [
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("hide_actions", "hideActions"),
            "focusable",
            "static",
            "ripple",
            "readonly",
        ]
        self._event_names += []


class VExpansionPanels(HtmlElement):
    """
    Vuetify's VExpansionPanels component. See more info and examples |VExpansionPanels_vuetify_link|.

    .. |VExpansionPanels_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expansion-panels" target="_blank">here</a>


    :param flat: Removes the expansion-panel's elevation and borders.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type any:
    :param multiple: Allows one to select multiple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param disabled: Puts all children components into a disabled state.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param title: Specify a title text for the component.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param bg_color: See description |VExpansionPanels_vuetify_link|.
    :type string:
    :param elevation: See description |VExpansionPanels_vuetify_link|.
    :type string | number:
    :param value: Controls the opened/closed state of content in the expansion-panel. Corresponds to a zero-based index of the currently opened content. If the `multiple` prop (previously `expand` in 1.5.x) is used then it is an array of numbers where each entry corresponds to the index of the opened content.  The index order is not relevant.
    :type any:
    :param rounded: See description |VExpansionPanels_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes the border-radius.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param color: See description |VExpansionPanels_vuetify_link|.
    :type string:
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :type any:
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :type any:
    :param hide_actions: Hide the expand icon in the content title.
    :type boolean:
    :param focusable: Makes the expansion-panel headers focusable.
    :type boolean:
    :param static: Remove title size expansion when selected.
    :type boolean:
    :param ripple: See description |VExpansionPanels_vuetify_link|.
    :type boolean | { class: string }:
    :param readonly: Makes the entire expansion-panel read only.
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'default' | 'accordion' | 'inset' | 'popout':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VExpansionPanels", children, **kwargs)
        self._attr_names += [
            "flat",
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
            "title",
            "text",
            ("bg_color", "bgColor"),
            "elevation",
            "value",
            "rounded",
            "tile",
            "tag",
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("hide_actions", "hideActions"),
            "focusable",
            "static",
            "ripple",
            "readonly",
            "eager",
            "theme",
            "variant",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VFab(HtmlElement):
    """
    Vuetify's VFab component. See more info and examples |VFab_vuetify_link|.

    .. |VFab_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-fab" target="_blank">here</a>


    :param symbol: See description |VFab_vuetify_link|.
    :type any:
    :param flat: Removes the button box shadow. This is different than using the 'flat' variant.
    :type boolean:
    :param app: If true, attaches to the closest layout and positions according to the value of **location**.
    :type boolean:
    :param appear: Used to control the animation of the FAB.
    :type boolean:
    :param extended: An alternate style for the FAB that expects text.
    :type boolean:
    :param layout: If true, will effect layout dimensions based on size and position.
    :type boolean:
    :param location: The location of the fab relative to the layout. Only works when using **app**.
    :type 'start' | 'end' | 'left' | 'right' | 'top' | 'bottom':
    :param offset: Translates the Fab up or down, depending on if location is set to **top** or **bottom**.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type boolean:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type boolean:
    :param base_color: Sets the color of component when not focused.
    :type string:
    :param prepend_icon: See description |VFab_vuetify_link|.
    :type any:
    :param append_icon: See description |VFab_vuetify_link|.
    :type any:
    :param block: Expands the button to 100% of available space.
    :type boolean:
    :param readonly: Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.
    :type boolean:
    :param slim: Reduces padding to 0 8px.
    :type boolean:
    :param stacked: Displays the button as a flex-column.
    :type boolean:
    :param ripple: See description |VFab_vuetify_link|.
    :type boolean | { class: string }:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param text: Specify content text for the component.
    :type string:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param elevation: See description |VFab_vuetify_link|.
    :type string | number:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :type string | boolean:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param rounded: See description |VFab_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VFab_vuetify_link|.
    :type boolean:
    :param exact: See description |VFab_vuetify_link|.
    :type boolean:
    :param to: See description |VFab_vuetify_link|.
    :type RouteLocationRaw:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VFab_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'text' | 'elevated' | 'tonal' | 'outlined' | 'plain':
    :param icon: See description |VFab_vuetify_link|.
    :type any:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param transition: See description |VFab_vuetify_link|.
    :type string | boolean | (TransitionProps & { component: Component }):

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFab", children, **kwargs)
        self._attr_names += [
            "symbol",
            "flat",
            "app",
            "appear",
            "extended",
            "layout",
            "location",
            "offset",
            ("model_value", "modelValue"),
            "active",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "block",
            "readonly",
            "slim",
            "stacked",
            "ripple",
            "value",
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
            "position",
            "absolute",
            "rounded",
            "tile",
            "href",
            "replace",
            "exact",
            "to",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
            "icon",
            "name",
            "order",
            "transition",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VFabTransition(HtmlElement):
    """
    Vuetify's VFabTransition component. See more info and examples |VFabTransition_vuetify_link|.

    .. |VFabTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-fab-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VFabTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VFabTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VFabTransition_vuetify_link|.
    :type string:
    :param origin: See description |VFabTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFabTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VFadeTransition(HtmlElement):
    """
    Vuetify's VFadeTransition component. See more info and examples |VFadeTransition_vuetify_link|.

    .. |VFadeTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-fade-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VFadeTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VFadeTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VFadeTransition_vuetify_link|.
    :type string:
    :param origin: See description |VFadeTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFadeTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VField(HtmlElement):
    """
      Vuetify's VField component. See more info and examples |VField_vuetify_link|.

      .. |VField_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-field" target="_blank">here</a>


      :param label: See description |VField_vuetify_link|.
      :type string:
      :param id: Sets the DOM id on the component.
      :type string:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param reverse: Reverses the orientation.
      :type boolean:
      :param flat: Removes box shadow when using a variant with elevation.
      :type boolean:
      :param append_inner_icon: See description |VField_vuetify_link|.
      :type any:
      :param bg_color: See description |VField_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared.
      :type boolean:
      :param clear_icon: The icon used when the **clearable** prop is set to true.
      :type any:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component.
      :type boolean:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param color: See description |VField_vuetify_link|.
      :type string:
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param dirty: Manually apply the dirty state styling.
      :type boolean:
      :param disabled: Removes the ability to click or target the input.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
      :type boolean:
      :param prepend_inner_icon: See description |VField_vuetify_link|.
      :type any:
      :param single_line: Label does not move on focus/dirty.
      :type boolean:
      :param variant: Applies a distinct style to the component.
      :type | 'underlined'
    | 'outlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled'
    | 'plain':
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
      :type string | boolean:
      :param rounded: See description |VField_vuetify_link|.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type unknown:

      Events

      :param update_focused: Emitted when the input is focused or blurred
      :param click_clear: Emitted when clearable icon clicked.
      :param click_appendInner: Emitted when appended inner icon is clicked.
      :param click_prependInner: Emitted when prepended inner icon is clicked.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VField", children, **kwargs)
        self._attr_names += [
            "label",
            "id",
            "focused",
            "reverse",
            "flat",
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            ("center_affix", "centerAffix"),
            "color",
            ("base_color", "baseColor"),
            "dirty",
            "disabled",
            "error",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "loading",
            "rounded",
            "tile",
            "theme",
            ("model_value", "modelValue"),
        ]
        self._event_names += [
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_modelValue", "update:modelValue"),
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


      :param label: See description |VFileInput_vuetify_link|.
      :type string:
      :param counter: Displays the number of selected files.
      :type boolean:
      :param flat: Removes box shadow when using a variant with elevation.
      :type boolean:
      :param chips: Changes display of selections to chips.
      :type boolean:
      :param counter_size_string: See description |VFileInput_vuetify_link|.
      :type string:
      :param counter_string: See description |VFileInput_vuetify_link|.
      :type string:
      :param hide_input: Display the icon only without the input (file names).
      :type boolean:
      :param multiple: Adds the **multiple** attribute to the input, allowing multiple file selections.
      :type boolean:
      :param show_size: Sets the displayed size of selected file(s). When using **true** will default to _1000_ displaying (**kB, MB, GB**) while _1024_ will display (**KiB, MiB, GiB**).
      :type boolean | 1000 | 1024:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VFileInput_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VFileInput_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VFileInput_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param reverse: Reverses the orientation.
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the input.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type File | File[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param append_inner_icon: See description |VFileInput_vuetify_link|.
      :type any:
      :param bg_color: See description |VFileInput_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared.
      :type boolean:
      :param clear_icon: The icon used when the **clearable** prop is set to true.
      :type any:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component.
      :type boolean:
      :param color: See description |VFileInput_vuetify_link|.
      :type string:
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param dirty: Manually apply the dirty state styling.
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
      :type boolean:
      :param prepend_inner_icon: See description |VFileInput_vuetify_link|.
      :type any:
      :param single_line: Label does not move on focus/dirty.
      :type boolean:
      :param variant: Applies a distinct style to the component.
      :type | 'underlined'
    | 'outlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled'
    | 'plain':
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
      :type string | boolean:
      :param rounded: See description |VFileInput_vuetify_link|.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:

      Events

      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when append icon is clicked.
      :param update_focused: Emitted when the input is focused or blurred
      :param click_clear: Emitted when clearable icon clicked.
      :param click_appendInner: Emitted when appended inner icon is clicked.
      :param click_prependInner: Emitted when prepended inner icon is clicked.
      :param click_control: Emitted when the main input is clicked.
      :param mousedown_control: Event that is emitted when using mousedown on the main control area.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFileInput", children, **kwargs)
        self._attr_names += [
            "label",
            "counter",
            "flat",
            "chips",
            ("counter_size_string", "counterSizeString"),
            ("counter_string", "counterString"),
            ("hide_input", "hideInput"),
            "multiple",
            ("show_size", "showSize"),
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "color",
            ("base_color", "baseColor"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "loading",
            "rounded",
            "tile",
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("click_control", "click:control"),
            ("mousedown_control", "mousedown:control"),
            ("update_modelValue", "update:modelValue"),
        ]


class VFooter(HtmlElement):
    """
    Vuetify's VFooter component. See more info and examples |VFooter_vuetify_link|.

    .. |VFooter_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-footer" target="_blank">here</a>


    :param app: Determines the position of the footer. If true, the footer would be given a fixed position at the bottom of the viewport. If false, the footer is set to the bottom of the page.
    :type boolean:
    :param color: See description |VFooter_vuetify_link|.
    :type string:
    :param height: Sets the height for the component.
    :type string | number:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
    :type string | number | boolean:
    :param elevation: See description |VFooter_vuetify_link|.
    :type string | number:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param rounded: See description |VFooter_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VFooter", children, **kwargs)
        self._attr_names += [
            "app",
            "color",
            "height",
            "border",
            "elevation",
            "name",
            "order",
            "absolute",
            "rounded",
            "tile",
            "tag",
            "theme",
        ]
        self._event_names += []


class VForm(HtmlElement):
    """
      Vuetify's VForm component. See more info and examples |VForm_vuetify_link|.

      .. |VForm_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-form" target="_blank">here</a>


      :param model_value: The value representing the validity of the form. If the value is `null` then no validation has taken place yet, or the form has been reset. Otherwise the value will be a `boolean` that indicates if validation has passed or not.
      :type boolean:
      :param disabled: Puts all children inputs into a disabled state.
      :type boolean:
      :param fast_fail: Stop validation as soon as any rules fail.
      :type boolean:
      :param readonly: Puts all children inputs into a readonly state.
      :type boolean:
      :param validate_on: Changes the events in which validation occurs.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':

      Events

      :param update_modelValue: Event emitted when the form's validity changes.
      :param submit: Emitted when form is submitted.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VForm", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "disabled",
            ("fast_fail", "fastFail"),
            "readonly",
            ("validate_on", "validateOn"),
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


    :param disabled: Removes hover functionality.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type boolean:
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :type string | number:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
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
    Vuetify's VIcon component. See more info and examples |VIcon_vuetify_link|.

    .. |VIcon_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-icon" target="_blank">here</a>


    :param color: See description |VIcon_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param start: Applies margin at the end of the component.
    :type boolean:
    :param end: Applies margin at the start of the component.
    :type boolean:
    :param icon: See description |VIcon_vuetify_link|.
    :type any:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VIcon", children, **kwargs)
        self._attr_names += [
            "color",
            "disabled",
            "start",
            "end",
            "icon",
            "size",
            "tag",
            "theme",
        ]
        self._event_names += []


class VImg(HtmlElement):
    """
        Vuetify's VImg component. See more info and examples |VImg_vuetify_link|.

        .. |VImg_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-img" target="_blank">here</a>


        :param alt: Alternate text for screen readers. Leave empty for decorative images.
        :type string:
        :param cover: Resizes the background image to cover the entire container.
        :type boolean:
        :param color: See description |VImg_vuetify_link|.
        :type string:
        :param draggable: See description |VImg_vuetify_link|.
        :type boolean | 'true' | 'false':
        :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
        :type boolean:
        :param gradient: See description |VImg_vuetify_link|.
        :type string:
        :param lazy_src: Something to show while waiting for the main image to load, typically a small base64-encoded thumbnail. Has a slight blur filter applied.
    NOTE: This prop has no effect unless either `height` or `aspect-ratio` are provided.
        :type string:
        :param options: See description |VImg_vuetify_link|.
        :type IntersectionObserverInit:
        :param sizes: See description |VImg_vuetify_link|.
        :type string:
        :param src: The image URL. This prop is mandatory.
        :type | string
      | { src: string; srcset: string; lazySrc: string; aspect: number }:
        :param srcset: See description |VImg_vuetify_link|.
        :type string:
        :param position: See description |VImg_vuetify_link|.
        :type string:
        :param aspect_ratio: Calculated as `width/height`, so for a 1920x1080px image this will be `1.7778`. Will be calculated automatically if omitted.
        :type string | number:
        :param content_class: Apply a custom class to the internal content element.
        :type any:
        :param inline: Display as an inline element instead of a block, also disables flex-grow.
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
        :param rounded: See description |VImg_vuetify_link|.
        :type string | number | boolean:
        :param tile: Removes any applied **border-radius** from the component.
        :type boolean:
        :param transition: See description |VImg_vuetify_link|.
        :type string | boolean | (TransitionProps & { component: Component }):
        :param crossorigin: See description |VImg_vuetify_link|.
        :type '' | 'anonymous' | 'use-credentials':
        :param referrerpolicy: See description |VImg_vuetify_link|.
        :type | 'no-referrer'
      | 'no-referrer-when-downgrade'
      | 'origin'
      | 'origin-when-cross-origin'
      | 'same-origin'
      | 'strict-origin'
      | 'strict-origin-when-cross-origin'
      | 'unsafe-url':

        Events

        :param error: Emitted if the image fails to load.
        :param loadstart: Emitted when the image starts to load.
        :param load: Emitted when the image is loaded.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VImg", children, **kwargs)
        self._attr_names += [
            "alt",
            "cover",
            "color",
            "draggable",
            "eager",
            "gradient",
            ("lazy_src", "lazySrc"),
            "options",
            "sizes",
            "src",
            "srcset",
            "position",
            ("aspect_ratio", "aspectRatio"),
            ("content_class", "contentClass"),
            "inline",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "rounded",
            "tile",
            "transition",
            "crossorigin",
            "referrerpolicy",
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


    :param color: See description |VInfiniteScroll_vuetify_link|.
    :type string:
    :param direction: Specifies if scroller is **vertical** or **horizontal**.
    :type 'vertical' | 'horizontal':
    :param side: Specifies the side where new content should appear. Either the **start**, **end**, or **both** sides.
    :type 'start' | 'end' | 'both':
    :param mode: Specifies if content should load automatically when scrolling (**intersect**) or manually (**manual**).
    :type 'intersect' | 'manual':
    :param margin: Value sent to the intersection observer. Will make the observer trigger earlier, by the margin (px) value supplied.
    :type string | number:
    :param load_more_text: Text shown in default load more button, when in manual mode.
    :type string:
    :param empty_text: Text shown when there is no more content to load.
    :type string:
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

    Events

    :param load: Emitted when reaching the start / end threshold, or if triggered when using manual mode.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VInfiniteScroll", children, **kwargs)
        self._attr_names += [
            "color",
            "direction",
            "side",
            "mode",
            "margin",
            ("load_more_text", "loadMoreText"),
            ("empty_text", "emptyText"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "tag",
        ]
        self._event_names += [
            "load",
        ]


class VInput(HtmlElement):
    """
      Vuetify's VInput component. See more info and examples |VInput_vuetify_link|.

      .. |VInput_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-input" target="_blank">here</a>


      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VInput_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VInput_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VInput_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param label: See description |VInput_vuetify_link|.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type unknown:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':

      Events

      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when appended icon is clicked.
      :param update_focused: Event that is emitted when the component's focus state changes.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VInput", children, **kwargs)
        self._attr_names += [
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "label",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("update_modelValue", "update:modelValue"),
        ]


class VItem(HtmlElement):
    """
    Vuetify's VItem component. See more info and examples |VItem_vuetify_link|.

    .. |VItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-item" target="_blank">here</a>


    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Removes the ability to click or target the component.
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


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param multiple: Allows one to select multiple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the selected CSS class. This class will be available in `v-item` default scoped slot.
    :type string:
    :param disabled: Puts all children components into a disabled state.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VItemGroup", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
            "tag",
            "theme",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VKbd(HtmlElement):
    """
    Vuetify's VKbd component. See more info and examples |VKbd_vuetify_link|.

    .. |VKbd_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-kbd" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
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
    :param theme: Specify a theme for this component and all of its children.
    :type string:

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
    Vuetify's VLayout component. See more info and examples |VLayout_vuetify_link|.

    .. |VLayout_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-layout" target="_blank">here</a>


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
    :param full_height: Sets the component height to 100%.
    :type boolean:
    :param overlaps: **FOR INTERNAL USE ONLY**
    :type string[]:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLayout", children, **kwargs)
        self._attr_names += [
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            ("full_height", "fullHeight"),
            "overlaps",
        ]
        self._event_names += []


class VLayoutItem(HtmlElement):
    """
    Vuetify's VLayoutItem component. See more info and examples |VLayoutItem_vuetify_link|.

    .. |VLayoutItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-layout-item" target="_blank">here</a>


    :param position: See description |VLayoutItem_vuetify_link|.
    :type 'top' | 'right' | 'bottom' | 'left':
    :param size: Sets the height and width of the component.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type boolean:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLayoutItem", children, **kwargs)
        self._attr_names += [
            "position",
            "size",
            ("model_value", "modelValue"),
            "name",
            "order",
            "absolute",
        ]
        self._event_names += []


class VLazy(HtmlElement):
    """
    Vuetify's VLazy component. See more info and examples |VLazy_vuetify_link|.

    .. |VLazy_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-lazy" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type boolean:
    :param options: See description |VLazy_vuetify_link|.
    :type IntersectionObserverInit:
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
    :type string | boolean | (TransitionProps & { component: Component }):

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLazy", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "options",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "tag",
            "transition",
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
    :type any:
    :param tag: Specify a custom tag used on the root element.
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


        :param base_color: Sets the color of component when not focused.
        :type string:
        :param active_color: The applied color when the component is in an active state.
        :type string:
        :param active_class: The class applied to the component when it is in an active state.
        :type string:
        :param bg_color: See description |VList_vuetify_link|.
        :type string:
        :param disabled: Puts all children inputs into a disabled state.
        :type boolean:
        :param expand_icon: See description |VList_vuetify_link|.
        :type string:
        :param collapse_icon: See description |VList_vuetify_link|.
        :type string:
        :param lines: See description |VList_vuetify_link|.
        :type false | 'one' | 'two' | 'three':
        :param slim: Reduces horizontal spacing for badges, icons, tooltips, and avatars within slim list items to create a more compact visual representation.
        :type boolean:
        :param nav: See description |VList_vuetify_link|.
        :type boolean:
        :param activatable: See description |VList_vuetify_link|.
        :type boolean:
        :param selectable: See description |VList_vuetify_link|.
        :type boolean:
        :param opened: An array containing the values of currently opened groups. Can be two-way bound with `v-model:opened`.
        :type unknown:
        :param activated: Array of ids of activated nodes.
        :type any:
        :param selected: An array containing the values of currently selected items. Can be two-way bound with `v-model:selected`.
        :type unknown:
        :param mandatory: Forces at least one item to always be selected (if available).
        :type boolean:
        :param active_strategy: Affects how items with children behave when activated.
    - **leaf:** Only leaf nodes (items without children) can be activated.
    - **independent:** All nodes can be activated whether they have children or not.
    - **classic:** Activating a parent node will cause all children to be activated.
        :type | 'single-leaf'
      | 'leaf'
      | 'independent'
      | 'single-independent'
      | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/activeStrategies.ts#L27-L31" target="_blank">ActiveStrategy</a>
      | ((mandatory: boolean) => <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/activeStrategies.ts#L27-L31" target="_blank">ActiveStrategy</a>):
        :param select_strategy: Affects how items with children behave when selected.
    - **leaf:** Only leaf nodes (items without children) can be selected.
    - **independent:** All nodes can be selected whether they have children or not.
    - **classic:** Selecting a parent node will cause all children to be selected, parent nodes will be displayed as selected if all their descendants are selected. Only leaf nodes will be added to the model.
        :type | 'single-leaf'
      | 'leaf'
      | 'independent'
      | 'single-independent'
      | 'classic'
      | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/selectStrategies.ts#L26-L30" target="_blank">SelectStrategy</a>
      | ((mandatory: boolean) => <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/selectStrategies.ts#L26-L30" target="_blank">SelectStrategy</a>):
        :param open_strategy: Affects how items with children behave when expanded.
    - **multiple:** Any number of groups can be open at once.
    - **single:** Only one group at each level can be open, opening a group will cause others to close.
    - **list:** Multiple, but all other groups will close when an item is selected.
        :type 'single' | 'multiple' | 'list' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/openStrategies.ts#L20-L23" target="_blank">OpenStrategy</a>:
        :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
        :param item_type: Designates the key on the supplied items that is used for determining the nodes type.
        :type string:
        :param items: See description |VList_vuetify_link|.
        :type any[]:
        :param item_title: Property on supplied `items` that contains its title.
        :type SelectItemKey<any>:
        :param item_value: Property on supplied `items` that contains its value.
        :type SelectItemKey<any>:
        :param item_children: Property on supplied `items` that contains its children.
        :type SelectItemKey<any>:
        :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
        :type SelectItemKey<any>:
        :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
        :type boolean:
        :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
        :type (a: any, b: any) => boolean:
        :param rounded: See description |VList_vuetify_link|.
        :type string | number | boolean:
        :param tile: Removes any applied **border-radius** from the component.
        :type boolean:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children.
        :type string:
        :param color: See description |VList_vuetify_link|.
        :type string:
        :param variant: Applies a distinct style to the component.
        :type 'flat' | 'elevated' | 'tonal' | 'outlined' | 'text' | 'plain':

        Events

        :param click_open: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VList.json))
        :param click_select: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VList.json))
        :param update_selected: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VList.json))
        :param update_opened: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VList.json))
        :param update_activated: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VList.json))
        :param click_activate: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VList.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VList", children, **kwargs)
        self._attr_names += [
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
            "activated",
            "selected",
            "mandatory",
            ("active_strategy", "activeStrategy"),
            ("select_strategy", "selectStrategy"),
            ("open_strategy", "openStrategy"),
            "border",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            ("item_type", "itemType"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
        ]
        self._event_names += [
            ("click_open", "click:open"),
            ("click_select", "click:select"),
            ("update_selected", "update:selected"),
            ("update_opened", "update:opened"),
            ("update_activated", "update:activated"),
            ("click_activate", "click:activate"),
        ]


class VListGroup(HtmlElement):
    """
    Vuetify's VListGroup component. See more info and examples |VListGroup_vuetify_link|.

    .. |VListGroup_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-group" target="_blank">here</a>


    :param active_color: The applied color when the component is in an active state.
    :type string:
    :param base_color: Sets the color of component when not focused.
    :type string:
    :param color: See description |VListGroup_vuetify_link|.
    :type string:
    :param collapse_icon: Icon to display when the list item is expanded.
    :type any:
    :param expand_icon: Icon to display when the list item is collapsed.
    :type any:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :type any:
    :param append_icon: See description |VListGroup_vuetify_link|.
    :type any:
    :param fluid: See description |VListGroup_vuetify_link|.
    :type boolean:
    :param subgroup: Designate the component as nested list group.
    :type boolean:
    :param title: Specify a title text for the component.
    :type string:
    :param value: Expands / Collapse the list-group.
    :type any:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListGroup", children, **kwargs)
        self._attr_names += [
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            "color",
            ("collapse_icon", "collapseIcon"),
            ("expand_icon", "expandIcon"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "fluid",
            "subgroup",
            "title",
            "value",
            "tag",
        ]
        self._event_names += []


class VListImg(HtmlElement):
    """
    Vuetify's VListImg component. See more info and examples |VListImg_vuetify_link|.

    .. |VListImg_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-img" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
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


    :param title: See description |VListItem_vuetify_link|.
    :type string | number:
    :param subtitle: Specify a subtitle text for the component.
    :type string | number:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type boolean:
    :param active_class: See description |VListItem_vuetify_link|.
    :type string:
    :param active_color: The applied color when the component is in an active state.
    :type string:
    :param append_avatar: See description |VListItem_vuetify_link|.
    :type string:
    :param append_icon: See description |VListItem_vuetify_link|.
    :type any:
    :param base_color: Sets the color of component when not focused.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param link: Designates that the component is a link. This is automatic when using the href or to prop.
    :type boolean:
    :param nav: See description |VListItem_vuetify_link|.
    :type boolean:
    :param prepend_avatar: See description |VListItem_vuetify_link|.
    :type string:
    :param prepend_icon: See description |VListItem_vuetify_link|.
    :type any:
    :param ripple: See description |VListItem_vuetify_link|.
    :type boolean | { class: string }:
    :param value: The value used for selection.
    :type any:
    :param slim: See description |VListItem_vuetify_link|.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VListItem_vuetify_link|.
    :type boolean:
    :param exact: See description |VListItem_vuetify_link|.
    :type boolean:
    :param to: See description |VListItem_vuetify_link|.
    :type RouteLocationRaw:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VListItem_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'elevated' | 'tonal' | 'outlined' | 'text' | 'plain':
    :param lines: See description |VListItem_vuetify_link|.
    :type false | 'one' | 'two' | 'three':

    Events

    :param clickOnce: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VListItem.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItem", children, **kwargs)
        self._attr_names += [
            "title",
            "subtitle",
            "active",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
            ("append_avatar", "appendAvatar"),
            ("append_icon", "appendIcon"),
            ("base_color", "baseColor"),
            "disabled",
            "link",
            "nav",
            ("prepend_avatar", "prependAvatar"),
            ("prepend_icon", "prependIcon"),
            "ripple",
            "value",
            "slim",
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
            "href",
            "replace",
            "exact",
            "to",
            "tag",
            "theme",
            "color",
            "variant",
            "lines",
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


    :param start: Applies margin at the end of the component.
    :type boolean:
    :param end: Applies margin at the start of the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemAction", children, **kwargs)
        self._attr_names += [
            "start",
            "end",
            "tag",
        ]
        self._event_names += []


class VListItemMedia(HtmlElement):
    """
    Vuetify's VListItemMedia component. See more info and examples |VListItemMedia_vuetify_link|.

    .. |VListItemMedia_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-media" target="_blank">here</a>


    :param start: Applies margin at the end of the component.
    :type boolean:
    :param end: Applies margin at the start of the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemMedia", children, **kwargs)
        self._attr_names += [
            "start",
            "end",
            "tag",
        ]
        self._event_names += []


class VListItemSubtitle(HtmlElement):
    """
    Vuetify's VListItemSubtitle component. See more info and examples |VListItemSubtitle_vuetify_link|.

    .. |VListItemSubtitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-subtitle" target="_blank">here</a>


    :param opacity: Sets the component's opacity value
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListItemSubtitle", children, **kwargs)
        self._attr_names += [
            "opacity",
            "tag",
        ]
        self._event_names += []


class VListItemTitle(HtmlElement):
    """
    Vuetify's VListItemTitle component. See more info and examples |VListItemTitle_vuetify_link|.

    .. |VListItemTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
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


    :param color: See description |VListSubheader_vuetify_link|.
    :type string:
    :param inset: See description |VListSubheader_vuetify_link|.
    :type boolean:
    :param sticky: See description |VListSubheader_vuetify_link|.
    :type boolean:
    :param title: Specify a title text for the component.
    :type string:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VListSubheader", children, **kwargs)
        self._attr_names += [
            "color",
            "inset",
            "sticky",
            "title",
            "tag",
        ]
        self._event_names += []


class VLocaleProvider(HtmlElement):
    """
    Vuetify's VLocaleProvider component. See more info and examples |VLocaleProvider_vuetify_link|.

    .. |VLocaleProvider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-locale-provider" target="_blank">here</a>


    :param locale: See description |VLocaleProvider_vuetify_link|.
    :type string:
    :param fallback_locale: See description |VLocaleProvider_vuetify_link|.
    :type string:
    :param messages: Displays a list of messages or a single message if using a string.
    :type unknown:
    :param rtl: See description |VLocaleProvider_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VLocaleProvider", children, **kwargs)
        self._attr_names += [
            "locale",
            ("fallback_locale", "fallbackLocale"),
            "messages",
            "rtl",
        ]
        self._event_names += []


class VMain(HtmlElement):
    """
    Vuetify's VMain component. See more info and examples |VMain_vuetify_link|.

    .. |VMain_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-main" target="_blank">here</a>


    :param scrollable: See description |VMain_vuetify_link|.
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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMain", children, **kwargs)
        self._attr_names += [
            "scrollable",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "tag",
        ]
        self._event_names += []


class VMenu(HtmlElement):
    """
      Vuetify's VMenu component. See more info and examples |VMenu_vuetify_link|.

      .. |VMenu_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-menu" target="_blank">here</a>


      :param activator: Explicitly sets the overlay's activator.
      :type Element | 'parent' | (string & {}) | ComponentPublicInstance:
      :param id: The unique identifier of the component.
      :type string:
      :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
      :type boolean:
      :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
      :type boolean:
      :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
      :type any:
      :param content_props: Apply custom properties to the content.
      :type any:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param opacity: Sets the overlay opacity.
      :type string | number:
      :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type boolean:
      :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
      :type boolean:
      :param scrim: Accepts true/false to enable background, and string to define color.
      :type string | boolean:
      :param z_index: The z-index used for the component.
      :type string | number:
      :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
      :type | Element
    | 'parent'
    | 'cursor'
    | (string & {})
    | ComponentPublicInstance
    | [number, number]:
      :param activator_props: Apply custom properties to the activator.
      :type unknown:
      :param open_on_click: Designates whether menu should open on activator click.
      :type boolean:
      :param open_on_hover: Designates whether menu should open on activator hover.
      :type boolean:
      :param open_on_focus: Activate the component when the activator is focused.
      :type boolean:
      :param close_on_content_click: Designates if menu should close when its content is clicked.
      :type boolean:
      :param close_delay: Milliseconds to wait before closing component. Only works with the **open-on-hover** prop.
      :type string | number:
      :param open_delay: Milliseconds to wait before opening component. Only works with the **open-on-hover** prop.
      :type string | number:
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component. Use `auto` to use the activator width.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
      :type boolean:
      :param location_strategy: A function used to specifies how the component should position relative to its activator.
      :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
      :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param origin: See description |VMenu_vuetify_link|.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
      :param offset: A single value that offsets content away from the target based upon what side it is on.
      :type string | number | number[]:
      :param scroll_strategy: Strategy used when the component is activate and user scrolls.
      :type 'none' | 'close' | 'block' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param transition: See description |VMenu_vuetify_link|.
      :type | { component: Component }
    | string
    | boolean
    | (TransitionProps & { component: Component }):
      :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default. Generally not recommended except as a last resort: the default positioning algorithm should handle most scenarios better than is possible without teleporting, and you may have unexpected behavior if the menu ends up as child of its activator.
      :type string | boolean | Element:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMenu", children, **kwargs)
        self._attr_names += [
            "activator",
            "id",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
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
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "eager",
            ("location_strategy", "locationStrategy"),
            "location",
            "origin",
            "offset",
            ("scroll_strategy", "scrollStrategy"),
            "theme",
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


      :param active: Determines whether the messages are visible or not.
      :type boolean:
      :param color: See description |VMessages_vuetify_link|.
      :type string:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param transition: See description |VMessages_vuetify_link|.
      :type | { component: Component; leaveAbsolute: boolean; group: boolean }
    | string
    | boolean
    | (TransitionProps & { component: Component }):

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VMessages", children, **kwargs)
        self._attr_names += [
            "active",
            "color",
            "messages",
            "transition",
        ]
        self._event_names += []


class VNavigationDrawer(HtmlElement):
    """
    Vuetify's VNavigationDrawer component. See more info and examples |VNavigationDrawer_vuetify_link|.

    .. |VNavigationDrawer_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-navigation-drawer" target="_blank">here</a>


    :param image: Apply a specific background image to the component.
    :type string:
    :param color: See description |VNavigationDrawer_vuetify_link|.
    :type string:
    :param disable_resize_watcher: Prevents the automatic opening or closing of the drawer when resized, based on whether the device is mobile or desktop.
    :type boolean:
    :param disable_route_watcher: Disables opening of navigation drawer when route changes.
    :type boolean:
    :param expand_on_hover: Collapses the drawer to a **mini-variant** until hovering with the mouse.
    :type boolean:
    :param floating: A floating drawer has no visible container (no border-right).
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type boolean:
    :param permanent: The drawer remains visible regardless of screen size.
    :type boolean:
    :param rail: Sets the component width to the **rail-width** value.
    :type boolean:
    :param rail_width: Sets the width for the component when `rail` is enabled.
    :type string | number:
    :param scrim: Determines whether an overlay is used when a **temporary** drawer is open. Accepts true/false to enable background, and string to define color.
    :type string | boolean:
    :param temporary: A temporary drawer sits above its application and uses a scrim (overlay) to darken the background.
    :type boolean:
    :param persistent: Clicking outside or pressing **esc** key will not dismiss the dialog.
    :type boolean:
    :param touchless: Disable mobile touch functionality.
    :type boolean:
    :param width: Sets the width for the component.
    :type string | number:
    :param location: Controls the edge of the screen the drawer is attached to.
    :type 'start' | 'end' | 'left' | 'right' | 'top' | 'bottom':
    :param sticky: See description |VNavigationDrawer_vuetify_link|.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
    :type string | number | boolean:
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :type string | number:
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :type boolean:
    :param mobile_breakpoint: Sets the designated mobile breakpoint for the component. This will apply alternate styles for mobile devices such as the `temporary` prop, or activate the `bottom` prop when the breakpoint value is met. Setting the value to `0` will disable this functionality.
    :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
    :param elevation: See description |VNavigationDrawer_vuetify_link|.
    :type string | number:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param rounded: See description |VNavigationDrawer_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    :param update_rail: Event that is emitted when the rail model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VNavigationDrawer", children, **kwargs)
        self._attr_names += [
            "image",
            "color",
            ("disable_resize_watcher", "disableResizeWatcher"),
            ("disable_route_watcher", "disableRouteWatcher"),
            ("expand_on_hover", "expandOnHover"),
            "floating",
            ("model_value", "modelValue"),
            "permanent",
            "rail",
            ("rail_width", "railWidth"),
            "scrim",
            "temporary",
            "persistent",
            "touchless",
            "width",
            "location",
            "sticky",
            "border",
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "elevation",
            "name",
            "order",
            "absolute",
            "rounded",
            "tile",
            "tag",
            "theme",
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


class VNumberInput(HtmlElement):
    """
      Vuetify's VNumberInput component. See more info and examples |VNumberInput_vuetify_link|.

      .. |VNumberInput_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-number-input" target="_blank">here</a>


      :param label: See description |VNumberInput_vuetify_link|.
      :type string:
      :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
      :type string | number | boolean:
      :param flat: Removes box shadow when using a variant with elevation.
      :type boolean:
      :param control_variant: See description |VNumberInput_vuetify_link|.
      :type 'default' | 'stacked' | 'split':
      :param inset: See description |VNumberInput_vuetify_link|.
      :type boolean:
      :param hide_input: See description |VNumberInput_vuetify_link|.
      :type boolean:
      :param min: See description |VNumberInput_vuetify_link|.
      :type number:
      :param type: Sets input type.
      :type string:
      :param max: See description |VNumberInput_vuetify_link|.
      :type number:
      :param step: See description |VNumberInput_vuetify_link|.
      :type number:
      :param autofocus: Enables autofocus.
      :type boolean:
      :param prefix: Displays prefix text.
      :type string:
      :param placeholder: Sets the input’s placeholder text.
      :type string:
      :param persistent_placeholder: Forces placeholder to always be visible.
      :type boolean:
      :param persistent_counter: Forces counter to always be visible.
      :type boolean:
      :param suffix: Displays suffix text.
      :type string:
      :param role: The role attribute applied to the input.
      :type string:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VNumberInput_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VNumberInput_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VNumberInput_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param reverse: Reverses the orientation.
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the input.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type any:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param bg_color: See description |VNumberInput_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared.
      :type boolean:
      :param clear_icon: The icon used when the **clearable** prop is set to true.
      :type any:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component.
      :type boolean:
      :param color: See description |VNumberInput_vuetify_link|.
      :type string:
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param dirty: Manually apply the dirty state styling.
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
      :type boolean:
      :param single_line: Label does not move on focus/dirty.
      :type boolean:
      :param variant: Applies a distinct style to the component.
      :type | 'underlined'
    | 'outlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled'
    | 'plain':
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
      :type string | boolean:
      :param rounded: Adds a border radius to the input.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param counter_value: Function returns the counter display text.
      :type number | ((value: any) => number):
      :param model_modifiers: **FOR INTERNAL USE ONLY**
      :type unknown:

      Events

      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when append icon is clicked.
      :param update_focused: Emitted when the input is focused or blurred
      :param click_clear: Emitted when clearable icon clicked.
      :param click_appendInner: Emitted when appended inner icon is clicked.
      :param click_prependInner: Emitted when prepended inner icon is clicked.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VNumberInput", children, **kwargs)
        self._attr_names += [
            "label",
            "counter",
            "flat",
            ("control_variant", "controlVariant"),
            "inset",
            ("hide_input", "hideInput"),
            "min",
            "type",
            "max",
            "step",
            "autofocus",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            "role",
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "color",
            ("base_color", "baseColor"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("single_line", "singleLine"),
            "variant",
            "loading",
            "rounded",
            "tile",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_modelValue", "update:modelValue"),
        ]


class VOtpInput(HtmlElement):
    """
      Vuetify's VOtpInput component. See more info and examples |VOtpInput_vuetify_link|.

      .. |VOtpInput_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-otp-input" target="_blank">here</a>


      :param length: The OTP field's length.
      :type string | number:
      :param autofocus: Automatically focuses the first input on page load
      :type boolean:
      :param divider: Specifies the dividing character between items.
      :type string:
      :param focus_all: Puts all inputs into a focus state when any are focused
      :type boolean:
      :param label: See description |VOtpInput_vuetify_link|.
      :type string:
      :param type: Supported types: `text`, `password`, `number`.
      :type 'number' | 'text' | 'password':
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type string | number:
      :param placeholder: Sets the input’s placeholder text.
      :type string:
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
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param bg_color: See description |VOtpInput_vuetify_link|.
      :type string:
      :param color: See description |VOtpInput_vuetify_link|.
      :type string:
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param disabled: Removes the ability to click or target the input.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param variant: Applies a distinct style to the component.
      :type | 'underlined'
    | 'outlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled'
    | 'plain':
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
      :type string | boolean:
      :param rounded: See description |VOtpInput_vuetify_link|.
      :type string | number | boolean:
      :param theme: Specify a theme for this component and all of its children.
      :type string:

      Events

      :param update_focused: Emitted when the input is focused or blurred
      :param finish: Emitted when the input is filled completely and cursor is blurred.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VOtpInput", children, **kwargs)
        self._attr_names += [
            "length",
            "autofocus",
            "divider",
            ("focus_all", "focusAll"),
            "label",
            "type",
            ("model_value", "modelValue"),
            "placeholder",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "focused",
            ("bg_color", "bgColor"),
            "color",
            ("base_color", "baseColor"),
            "disabled",
            "error",
            "variant",
            "loading",
            "rounded",
            "theme",
        ]
        self._event_names += [
            ("update_focused", "update:focused"),
            "finish",
            ("update_modelValue", "update:modelValue"),
        ]


class VOverlay(HtmlElement):
    """
      Vuetify's VOverlay component. See more info and examples |VOverlay_vuetify_link|.

      .. |VOverlay_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-overlay" target="_blank">here</a>


      :param activator: Explicitly sets the overlay's activator.
      :type Element | 'parent' | (string & {}) | ComponentPublicInstance:
      :param absolute: Applies **position: absolute** to the content element.
      :type boolean:
      :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
      :type boolean:
      :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
      :type boolean:
      :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
      :type any:
      :param content_props: Apply custom properties to the content.
      :type any:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param opacity: Sets the overlay opacity.
      :type string | number:
      :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type boolean:
      :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
      :type boolean:
      :param scrim: Accepts true/false to enable background, and string to define color.
      :type string | boolean:
      :param z_index: The z-index used for the component.
      :type string | number:
      :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
      :type | Element
    | 'parent'
    | 'cursor'
    | (string & {})
    | ComponentPublicInstance
    | [number, number]:
      :param activator_props: Apply custom properties to the activator.
      :type unknown:
      :param open_on_click: Activate the component when the activator is clicked.
      :type boolean:
      :param open_on_hover: Activate the component when the activator is hovered.
      :type boolean:
      :param open_on_focus: Activate the component when the activator is focused.
      :type boolean:
      :param close_on_content_click: Closes component when you click on its content.
      :type boolean:
      :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
      :type string | number:
      :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
      :type string | number:
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
      :param location_strategy: A function used to specifies how the component should position relative to its activator.
      :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
      :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param origin: See description |VOverlay_vuetify_link|.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
      :param offset: A single value that offsets content away from the target based upon what side it is on.
      :type string | number | number[]:
      :param scroll_strategy: Strategy used when the component is activate and user scrolls.
      :type 'none' | 'close' | 'block' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param transition: See description |VOverlay_vuetify_link|.
      :type string | boolean | (TransitionProps & { component: Component }):
      :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
      :type string | boolean | Element:

      Events

      :param click_outside: Event that fires when clicking outside an active overlay.
      :param update_modelValue: Event that is emitted when the component's model changes.
      :param afterEnter: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VOverlay.json))
      :param afterLeave: Event that fires after the overlay has finished transitioning out.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VOverlay", children, **kwargs)
        self._attr_names += [
            "activator",
            "absolute",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
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
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "eager",
            ("location_strategy", "locationStrategy"),
            "location",
            "origin",
            "offset",
            ("scroll_strategy", "scrollStrategy"),
            "theme",
            "transition",
            "attach",
        ]
        self._event_names += [
            ("click_outside", "click:outside"),
            ("update_modelValue", "update:modelValue"),
            "afterEnter",
            "afterLeave",
        ]


class VPagination(HtmlElement):
    """
    Vuetify's VPagination component. See more info and examples |VPagination_vuetify_link|.

    .. |VPagination_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-pagination" target="_blank">here</a>


    :param length: The number of pages.
    :type string | number:
    :param active_color: The applied color when the component is in an active state.
    :type string:
    :param start: Specify the starting page.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type number:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param total_visible: Specify the total visible pagination numbers.
    :type string | number:
    :param first_icon: The icon to use for the first button.
    :type any:
    :param prev_icon: The icon to use for the prev button.
    :type any:
    :param next_icon: The icon to use for the next button.
    :type any:
    :param last_icon: The icon to use for the last button.
    :type any:
    :param aria_label: Label for the root element.
    :type string:
    :param page_aria_label: Label for each page button.
    :type string:
    :param current_page_aria_label: Label for the currently selected page.
    :type string:
    :param first_aria_label: Label for the go to first button.
    :type string:
    :param previous_aria_label: Label for the previous button.
    :type string:
    :param next_aria_label: Label for the next button.
    :type string:
    :param last_aria_label: Label for the go to last button.
    :type string:
    :param ellipsis: Text to show between page buttons when truncating the list.
    :type string:
    :param show_first_last_page: Show buttons for going to first and last page.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
    :type string | number | boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param elevation: See description |VPagination_vuetify_link|.
    :type string | number:
    :param rounded: See description |VPagination_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VPagination_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'elevated' | 'tonal' | 'outlined' | 'text' | 'plain':

    Events

    :param first: Emitted when clicking on go to first button.
    :param prev: Emitted when clicking on go to previous button.
    :param next: Emitted when clicking on go to next button.
    :param last: Emitted when clicking on go to last button.
    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPagination", children, **kwargs)
        self._attr_names += [
            "length",
            ("active_color", "activeColor"),
            "start",
            ("model_value", "modelValue"),
            "disabled",
            ("total_visible", "totalVisible"),
            ("first_icon", "firstIcon"),
            ("prev_icon", "prevIcon"),
            ("next_icon", "nextIcon"),
            ("last_icon", "lastIcon"),
            ("aria_label", "ariaLabel"),
            ("page_aria_label", "pageAriaLabel"),
            ("current_page_aria_label", "currentPageAriaLabel"),
            ("first_aria_label", "firstAriaLabel"),
            ("previous_aria_label", "previousAriaLabel"),
            ("next_aria_label", "nextAriaLabel"),
            ("last_aria_label", "lastAriaLabel"),
            "ellipsis",
            ("show_first_last_page", "showFirstLastPage"),
            "border",
            "density",
            "elevation",
            "rounded",
            "tile",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
        ]
        self._event_names += [
            "first",
            "prev",
            "next",
            "last",
            ("update_modelValue", "update:modelValue"),
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
    :param bg_color: See description |VPicker_vuetify_link|.
    :type string:
    :param landscape: Puts the picker into landscape mode.
    :type boolean:
    :param hide_header: Hide the picker header.
    :type boolean:
    :param color: See description |VPicker_vuetify_link|.
    :type string:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VPicker_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPicker", children, **kwargs)
        self._attr_names += [
            "title",
            ("bg_color", "bgColor"),
            "landscape",
            ("hide_header", "hideHeader"),
            "color",
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
        ]
        self._event_names += []


class VPickerTitle(HtmlElement):
    """
    Vuetify's VPickerTitle component. See more info and examples |VPickerTitle_vuetify_link|.

    .. |VPickerTitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-picker-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
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


    :param bg_color: See description |VProgressCircular_vuetify_link|.
    :type string:
    :param color: See description |VProgressCircular_vuetify_link|.
    :type string:
    :param model_value: The percentage value for current progress.
    :type string | number:
    :param rotate: Rotates the circle start point in degrees.
    :type string | number:
    :param width: Sets the stroke of the circle in pixels.
    :type string | number:
    :param size: Sets the diameter of the circle in pixels.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param indeterminate: Constantly animates, use when loading progress is unknown. If set to the string `'disable-shrink'` it will use a simpler animation that does not run on the main thread.
    :type boolean | 'disable-shrink':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VProgressCircular", children, **kwargs)
        self._attr_names += [
            ("bg_color", "bgColor"),
            "color",
            ("model_value", "modelValue"),
            "rotate",
            "width",
            "size",
            "tag",
            "theme",
            "indeterminate",
        ]
        self._event_names += []


class VProgressLinear(HtmlElement):
    """
    Vuetify's VProgressLinear component. See more info and examples |VProgressLinear_vuetify_link|.

    .. |VProgressLinear_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-progress-linear" target="_blank">here</a>


    :param absolute: Applies position: absolute to the component.
    :type boolean:
    :param active: Reduce the height to 0, hiding component.
    :type boolean:
    :param bg_color: See description |VProgressLinear_vuetify_link|.
    :type string:
    :param bg_opacity: Background opacity, if null it defaults to 0.3 if background color is not specified or 1 otherwise.
    :type string | number:
    :param buffer_value: The percentage value for the buffer.
    :type string | number:
    :param buffer_color: Sets the color of the buffer bar.
    :type string:
    :param buffer_opacity: Set the opacity of the buffer bar.
    :type string | number:
    :param clickable: Clicking on the progress track will automatically set the value.
    :type boolean:
    :param color: See description |VProgressLinear_vuetify_link|.
    :type string:
    :param height: Sets the height for the component.
    :type string | number:
    :param indeterminate: Constantly animates, use when loading progress is unknown.
    :type boolean:
    :param max: Sets the maximum value the progress can reach.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type string | number:
    :param opacity: Set the opacity of the progress bar.
    :type string | number:
    :param reverse: Displays reversed progress (right to left in LTR mode and left to right in RTL).
    :type boolean:
    :param stream: An alternative style for portraying loading that works in tandem with **buffer-value**.
    :type boolean:
    :param striped: Adds a stripe background to the filled portion of the progress component.
    :type boolean:
    :param rounded_bar: Applies a border radius to the progress bar.
    :type boolean:
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param rounded: See description |VProgressLinear_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VProgressLinear", children, **kwargs)
        self._attr_names += [
            "absolute",
            "active",
            ("bg_color", "bgColor"),
            ("bg_opacity", "bgOpacity"),
            ("buffer_value", "bufferValue"),
            ("buffer_color", "bufferColor"),
            ("buffer_opacity", "bufferOpacity"),
            "clickable",
            "color",
            "height",
            "indeterminate",
            "max",
            ("model_value", "modelValue"),
            "opacity",
            "reverse",
            "stream",
            "striped",
            ("rounded_bar", "roundedBar"),
            "location",
            "rounded",
            "tile",
            "tag",
            "theme",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VPullToRefresh(HtmlElement):
    """
    Vuetify's VPullToRefresh component. See more info and examples |VPullToRefresh_vuetify_link|.

    .. |VPullToRefresh_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-pull-to-refresh" target="_blank">here</a>


    :param pull_down_threshold: See description |VPullToRefresh_vuetify_link|.
    :type number:

    Events

    :param load: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VPullToRefresh.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VPullToRefresh", children, **kwargs)
        self._attr_names += [
            ("pull_down_threshold", "pullDownThreshold"),
        ]
        self._event_names += [
            "load",
        ]


class VRadio(HtmlElement):
    """
    Vuetify's VRadio component. See more info and examples |VRadio_vuetify_link|.

    .. |VRadio_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-radio" target="_blank">here</a>


    :param label: See description |VRadio_vuetify_link|.
    :type string:
    :param base_color: Sets the color of the input when it is not focused.
    :type string:
    :param true_value: Sets value for truthy state.
    :type any:
    :param false_value: Sets value for falsy state.
    :type any:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param color: See description |VRadio_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param defaults_target: The target component to provide defaults values for.
    :type string:
    :param error: Puts the input in a manual error state.
    :type boolean:
    :param id: Sets the DOM id on the component.
    :type string:
    :param inline: Puts children inputs into a row.
    :type boolean:
    :param false_icon: The icon used when inactive.
    :type any:
    :param true_icon: The icon used when active.
    :type any:
    :param ripple: See description |VRadio_vuetify_link|.
    :type boolean | { class: string }:
    :param multiple: Changes select to multiple. Accepts array for value.
    :type boolean:
    :param name: Sets the component's name attribute.
    :type string:
    :param readonly: Puts input in readonly state.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type any:
    :param type: Provides the default type for children selection controls.
    :type string:
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :type (a: any, b: any) => boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRadio", children, **kwargs)
        self._attr_names += [
            "label",
            ("base_color", "baseColor"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            "disabled",
            ("defaults_target", "defaultsTarget"),
            "error",
            "id",
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "multiple",
            "name",
            "readonly",
            ("model_value", "modelValue"),
            "type",
            ("value_comparator", "valueComparator"),
            "density",
            "theme",
        ]
        self._event_names += []


class VRadioGroup(HtmlElement):
    """
      Vuetify's VRadioGroup component. See more info and examples |VRadioGroup_vuetify_link|.

      .. |VRadioGroup_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-radio-group" target="_blank">here</a>


      :param label: See description |VRadioGroup_vuetify_link|.
      :type string:
      :param height: Sets the height of the input.
      :type string | number:
      :param type: Provides the default type for children selection controls.
      :type string:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VRadioGroup_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VRadioGroup_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VRadioGroup_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type unknown:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param color: See description |VRadioGroup_vuetify_link|.
      :type string:
      :param defaults_target: The target component to provide defaults values for.
      :type string:
      :param inline: Displays radio buttons in row.
      :type boolean:
      :param false_icon: The icon used when inactive.
      :type any:
      :param true_icon: The icon used when active.
      :type any:
      :param ripple: See description |VRadioGroup_vuetify_link|.
      :type boolean | { class: string }:
      :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
      :type (a: any, b: any) => boolean:

      Events

      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when appended icon is clicked.
      :param update_focused: Event that is emitted when the component's focus state changes.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRadioGroup", children, **kwargs)
        self._attr_names += [
            "label",
            "height",
            "type",
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            "color",
            ("defaults_target", "defaultsTarget"),
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("update_modelValue", "update:modelValue"),
        ]


class VRangeSlider(HtmlElement):
    """
      Vuetify's VRangeSlider component. See more info and examples |VRangeSlider_vuetify_link|.

      .. |VRangeSlider_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-range-slider" target="_blank">here</a>


      :param label: See description |VRangeSlider_vuetify_link|.
      :type string:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param reverse: Reverses the slider direction.
      :type boolean:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VRangeSlider_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VRangeSlider_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VRangeSlider_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type (string | number)[]:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param max: Sets the maximum allowed value.
      :type string | number:
      :param min: Sets the minimum allowed value.
      :type string | number:
      :param step: If greater than 0, sets step interval for ticks.
      :type string | number:
      :param thumb_color: Sets the thumb and thumb label color.
      :type string:
      :param thumb_label: Show thumb label. If `true` it shows label when using slider. If set to `'always'` it always shows label.
      :type boolean | 'always':
      :param thumb_size: Controls the size of the thumb label.
      :type string | number:
      :param show_ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
      :type boolean | 'always':
      :param ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
      :type number[] | Record<number, string>:
      :param tick_size: Controls the size of **ticks**
      :type string | number:
      :param color: See description |VRangeSlider_vuetify_link|.
      :type string:
      :param track_color: Sets the track's color
      :type string:
      :param track_fill_color: Sets the track's fill color
      :type string:
      :param track_size: Sets the track's size (height).
      :type string | number:
      :param rounded: See description |VRangeSlider_vuetify_link|.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param elevation: See description |VRangeSlider_vuetify_link|.
      :type string | number:
      :param ripple: See description |VRangeSlider_vuetify_link|.
      :type boolean:
      :param strict: Disallows dragging the ending thumb past the starting thumb and vice versa.
      :type boolean:

      Events

      :param update_focused: Event that is emitted when the component's focus state changes.
      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when appended icon is clicked.
      :param update_modelValue: Event that is emitted when the component's model changes.
      :param end: Slider value emitted at the end of slider movement.
      :param start: Slider value emitted at start of slider movement.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRangeSlider", children, **kwargs)
        self._attr_names += [
            "label",
            "focused",
            "reverse",
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
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
            "color",
            ("track_color", "trackColor"),
            ("track_fill_color", "trackFillColor"),
            ("track_size", "trackSize"),
            "rounded",
            "tile",
            "elevation",
            "ripple",
            "strict",
        ]
        self._event_names += [
            ("update_focused", "update:focused"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_modelValue", "update:modelValue"),
            "end",
            "start",
        ]


class VRating(HtmlElement):
    """
    Vuetify's VRating component. See more info and examples |VRating_vuetify_link|.

    .. |VRating_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-rating" target="_blank">here</a>


    :param length: The amount of items to show.
    :type string | number:
    :param name: Sets the component's name attribute.
    :type string:
    :param item_aria_label: See description |VRating_vuetify_link|.
    :type string:
    :param active_color: The applied color when the component is in an active state.
    :type string:
    :param color: See description |VRating_vuetify_link|.
    :type string:
    :param clearable: Allows for the component to be cleared by clicking on the current value.
    :type boolean:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param empty_icon: The icon displayed when empty.
    :type any:
    :param full_icon: The icon displayed when full.
    :type any:
    :param half_increments: Allows the selection of half increments.
    :type boolean:
    :param hover: Provides visual feedback when hovering over icons.
    :type boolean:
    :param readonly: Removes all hover effects and pointer events.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type string | number:
    :param item_label_position: Position of item labels. Accepts 'top' and 'bottom'.
    :type string:
    :param ripple: See description |VRating_vuetify_link|.
    :type boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param item_labels: Array of labels to display next to each item..
    :type string[]:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRating", children, **kwargs)
        self._attr_names += [
            "length",
            "name",
            ("item_aria_label", "itemAriaLabel"),
            ("active_color", "activeColor"),
            "color",
            "clearable",
            "disabled",
            ("empty_icon", "emptyIcon"),
            ("full_icon", "fullIcon"),
            ("half_increments", "halfIncrements"),
            "hover",
            "readonly",
            ("model_value", "modelValue"),
            ("item_label_position", "itemLabelPosition"),
            "ripple",
            "density",
            "size",
            "tag",
            "theme",
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


    :param aspect_ratio: Sets a base aspect ratio, calculated as width/height. This will only set a **minimum** height, the component can still grow if it has a lot of content.
    :type string | number:
    :param content_class: Apply a custom class to the internal content element.
    :type any:
    :param inline: Display as an inline element instead of a block, also disables flex-grow.
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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VResponsive", children, **kwargs)
        self._attr_names += [
            ("aspect_ratio", "aspectRatio"),
            ("content_class", "contentClass"),
            "inline",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
        ]
        self._event_names += []


class VRow(HtmlElement):
    """
      Vuetify's VRow component. See more info and examples |VRow_vuetify_link|.

      .. |VRow_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-row" target="_blank">here</a>


      :param dense: Reduces the gutter between `v-col`s.
      :type boolean:
      :param no_gutters: Removes the gutter between `v-col`s.
      :type boolean:
      :param align: See description |VRow_vuetify_link|.
      :type 'start' | 'end' | 'center' | 'baseline' | 'stretch':
      :param align_sm: Changes the **align-items** property on small and greater breakpoints.
      :type 'start' | 'end' | 'center' | 'baseline' | 'stretch':
      :param align_md: Changes the **align-items** property on medium and greater breakpoints.
      :type 'start' | 'end' | 'center' | 'baseline' | 'stretch':
      :param align_lg: Changes the **align-items** property on large and greater breakpoints.
      :type 'start' | 'end' | 'center' | 'baseline' | 'stretch':
      :param align_xl: Changes the **align-items** property on extra large and greater breakpoints.
      :type 'start' | 'end' | 'center' | 'baseline' | 'stretch':
      :param align_xxl: Changes the **align-items** property on extra extra large and greater breakpoints.
      :type 'start' | 'end' | 'center' | 'baseline' | 'stretch':
      :param justify_sm: Changes the **justify-content** property on small and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify_md: Changes the **justify-content** property on medium and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify_lg: Changes the **justify-content** property on large and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify_xl: Changes the **justify-content** property on extra large and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify_xxl: Changes the **justify-content** property on extra extra large and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_sm: Changes the **align-content** property on small and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_md: Changes the **align-content** property on medium and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_lg: Changes the **align-content** property on large and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_xl: Changes the **align-content** property on extra large and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content_xxl: Changes the **align-content** property on extra extra large and greater breakpoints.
      :type | 'start'
    | 'end'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param justify: See description |VRow_vuetify_link|.
      :type | 'start'
    | 'end'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param align_content: See description |VRow_vuetify_link|.
      :type | 'start'
    | 'end'
    | 'center'
    | 'stretch'
    | 'space-between'
    | 'space-around'
    | 'space-evenly':
      :param tag: Specify a custom tag used on the root element.
      :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VRow", children, **kwargs)
        self._attr_names += [
            "dense",
            ("no_gutters", "noGutters"),
            "align",
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
            "tag",
        ]
        self._event_names += []


class VScaleTransition(HtmlElement):
    """
    Vuetify's VScaleTransition component. See more info and examples |VScaleTransition_vuetify_link|.

    .. |VScaleTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scale-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VScaleTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VScaleTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VScaleTransition_vuetify_link|.
    :type string:
    :param origin: See description |VScaleTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScaleTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollXReverseTransition(HtmlElement):
    """
    Vuetify's VScrollXReverseTransition component. See more info and examples |VScrollXReverseTransition_vuetify_link|.

    .. |VScrollXReverseTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-x-reverse-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VScrollXReverseTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VScrollXReverseTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VScrollXReverseTransition_vuetify_link|.
    :type string:
    :param origin: See description |VScrollXReverseTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollXReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollXTransition(HtmlElement):
    """
    Vuetify's VScrollXTransition component. See more info and examples |VScrollXTransition_vuetify_link|.

    .. |VScrollXTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-x-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VScrollXTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VScrollXTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VScrollXTransition_vuetify_link|.
    :type string:
    :param origin: See description |VScrollXTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollXTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollYReverseTransition(HtmlElement):
    """
    Vuetify's VScrollYReverseTransition component. See more info and examples |VScrollYReverseTransition_vuetify_link|.

    .. |VScrollYReverseTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-y-reverse-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VScrollYReverseTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VScrollYReverseTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VScrollYReverseTransition_vuetify_link|.
    :type string:
    :param origin: See description |VScrollYReverseTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollYReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollYTransition(HtmlElement):
    """
    Vuetify's VScrollYTransition component. See more info and examples |VScrollYTransition_vuetify_link|.

    .. |VScrollYTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-y-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VScrollYTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VScrollYTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VScrollYTransition_vuetify_link|.
    :type string:
    :param origin: See description |VScrollYTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VScrollYTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VSelect(HtmlElement):
    """
      Vuetify's VSelect component. See more info and examples |VSelect_vuetify_link|.

      .. |VSelect_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-select" target="_blank">here</a>


      :param label: See description |VSelect_vuetify_link|.
      :type string:
      :param chips: Changes display of selections to chips.
      :type boolean:
      :param closable_chips: See description |VSelect_vuetify_link|.
      :type boolean:
      :param close_text: Text set to to the inputs `aria-label` and `title` when input menu is closed.
      :type string:
      :param type: Sets input type.
      :type string:
      :param open_text: Text set to to the inputs **aria-label** and **title** when input menu is open.
      :type string:
      :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
      :type boolean:
      :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
      :type boolean:
      :param hide_selected: Do not display in the select menu items that are already selected.
      :type boolean:
      :param list_props: See description |VSelect_vuetify_link|.
      :type unknown:
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param bg_color: See description |VSelect_vuetify_link|.
      :type string:
      :param disabled: Removes the ability to click or target the input.
      :type boolean:
      :param multiple: Changes select to multiple. Accepts array for value.
      :type boolean:
      :param reverse: Reverses the orientation.
      :type boolean:
      :param flat: Removes box shadow when using a variant with elevation.
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width of the select's `v-menu` content.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param items: See description |VSelect_vuetify_link|.
      :type any[]:
      :param item_title: Property on supplied `items` that contains its title.
      :type SelectItemKey<any>:
      :param item_value: See description |VSelect_vuetify_link|.
      :type SelectItemKey<any>:
      :param item_children: This property currently has **no effect**.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L73-L77" target="_blank">SelectItemKey</a>:
      :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
      :type SelectItemKey<any>:
      :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
      :type (a: any, b: any) => boolean:
      :param rounded: Adds a border radius to the input.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param color: See description |VSelect_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component.
      :type | 'outlined'
    | 'plain'
    | 'underlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled':
      :param name: Sets the component's name attribute.
      :type string:
      :param menu: Renders with the menu open by default.
      :type boolean:
      :param menu_icon: Sets the the spin icon.
      :type any:
      :param menu_props: See description |VSelect_vuetify_link|.
      :type unknown:
      :param id: Sets the DOM id on the component.
      :type string:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type any:
      :param transition: See description |VSelect_vuetify_link|.
      :type | string
    | boolean
    | (TransitionProps & { component: Component })
    | { component: Component }:
      :param no_data_text: Text shown when no items are provided to the component.
      :type string:
      :param open_on_clear: When using the **clearable** prop, once cleared, the select menu will either open or stay open, depending on the current state.
      :type boolean:
      :param item_color: Sets color of selected items.
      :type string:
      :param autofocus: Enables autofocus.
      :type boolean:
      :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
      :type string | number | boolean:
      :param prefix: Displays prefix text.
      :type string:
      :param placeholder: Sets the input’s placeholder text.
      :type string:
      :param persistent_placeholder: Forces placeholder to always be visible.
      :type boolean:
      :param persistent_counter: Forces counter to always be visible.
      :type boolean:
      :param suffix: Displays suffix text.
      :type string:
      :param role: The role attribute applied to the input.
      :type string:
      :param append_icon: See description |VSelect_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VSelect_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VSelect_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
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
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param clearable: Allows for the component to be cleared.
      :type boolean:
      :param clear_icon: The icon used when the **clearable** prop is set to true.
      :type any:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component.
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
      :type boolean:
      :param prepend_inner_icon: See description |VSelect_vuetify_link|.
      :type any:
      :param single_line: Label does not move on focus/dirty.
      :type boolean:
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
      :type string | boolean:
      :param counter_value: Function returns the counter display text.
      :type number | ((value: any) => number):
      :param model_modifiers: **FOR INTERNAL USE ONLY**
      :type unknown:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes.
      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when append icon is clicked.
      :param update_focused: Emitted when the input is focused or blurred
      :param click_clear: Emitted when clearable icon clicked.
      :param click_appendInner: Emitted when appended inner icon is clicked.
      :param click_prependInner: Emitted when prepended inner icon is clicked.
      :param update_menu: Event that is emitted when the component's menu state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSelect", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            "label",
            "chips",
            ("closable_chips", "closableChips"),
            ("close_text", "closeText"),
            "type",
            ("open_text", "openText"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            ("list_props", "listProps"),
            ("base_color", "baseColor"),
            ("bg_color", "bgColor"),
            "disabled",
            "multiple",
            "reverse",
            "flat",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "rounded",
            "tile",
            "theme",
            "color",
            "variant",
            "name",
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "id",
            ("model_value", "modelValue"),
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
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "error",
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
    Vuetify's VSelectionControl component. See more info and examples |VSelectionControl_vuetify_link|.

    .. |VSelectionControl_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-selection-control" target="_blank">here</a>


    :param label: See description |VSelectionControl_vuetify_link|.
    :type string:
    :param base_color: Sets the color of the input when it is not focused.
    :type string:
    :param true_value: Sets value for truthy state.
    :type any:
    :param false_value: Sets value for falsy state.
    :type any:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param color: See description |VSelectionControl_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param defaults_target: The target component to provide defaults values for.
    :type string:
    :param error: Puts the input in a manual error state.
    :type boolean:
    :param id: Sets the DOM id on the component.
    :type string:
    :param inline: Puts children inputs into a row.
    :type boolean:
    :param false_icon: The icon used when inactive.
    :type any:
    :param true_icon: The icon used when active.
    :type any:
    :param ripple: See description |VSelectionControl_vuetify_link|.
    :type boolean | { class: string }:
    :param multiple: Changes select to multiple. Accepts array for value.
    :type boolean:
    :param name: Sets the component's name attribute.
    :type string:
    :param readonly: Puts input in readonly state.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param type: Provides the default type for children selection controls.
    :type string:
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :type (a: any, b: any) => boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSelectionControl", children, **kwargs)
        self._attr_names += [
            "label",
            ("base_color", "baseColor"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            "disabled",
            ("defaults_target", "defaultsTarget"),
            "error",
            "id",
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "multiple",
            "name",
            "readonly",
            ("model_value", "modelValue"),
            "type",
            ("value_comparator", "valueComparator"),
            "density",
            "theme",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSelectionControlGroup(HtmlElement):
    """
    Vuetify's VSelectionControlGroup component. See more info and examples |VSelectionControlGroup_vuetify_link|.

    .. |VSelectionControlGroup_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-selection-control-group" target="_blank">here</a>


    :param color: See description |VSelectionControlGroup_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param defaults_target: The target component to provide defaults values for.
    :type string:
    :param error: Puts the input in a manual error state.
    :type boolean:
    :param id: Sets the DOM id on the component.
    :type string:
    :param inline: Puts children inputs into a row.
    :type boolean:
    :param false_icon: The icon used when inactive.
    :type any:
    :param true_icon: The icon used when active.
    :type any:
    :param ripple: See description |VSelectionControlGroup_vuetify_link|.
    :type boolean | { class: string }:
    :param multiple: Changes select to multiple. Accepts array for value.
    :type boolean:
    :param name: Sets the component's name attribute.
    :type string:
    :param readonly: Puts input in readonly state.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param type: Provides the default type for children selection controls.
    :type string:
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :type (a: any, b: any) => boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSelectionControlGroup", children, **kwargs)
        self._attr_names += [
            "color",
            "disabled",
            ("defaults_target", "defaultsTarget"),
            "error",
            "id",
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "multiple",
            "name",
            "readonly",
            ("model_value", "modelValue"),
            "type",
            ("value_comparator", "valueComparator"),
            "density",
            "theme",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSheet(HtmlElement):
    """
    Vuetify's VSheet component. See more info and examples |VSheet_vuetify_link|.

    .. |VSheet_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-sheet" target="_blank">here</a>


    :param color: See description |VSheet_vuetify_link|.
    :type string:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VSheet_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSheet", children, **kwargs)
        self._attr_names += [
            "color",
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
        ]
        self._event_names += []


class VSkeletonLoader(HtmlElement):
    """
      Vuetify's VSkeletonLoader component. See more info and examples |VSkeletonLoader_vuetify_link|.

      .. |VSkeletonLoader_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-skeleton-loader" target="_blank">here</a>


      :param boilerplate: Remove the loading animation from the skeleton.
      :type boolean:
      :param color: See description |VSkeletonLoader_vuetify_link|.
      :type string:
      :param loading: Applies a loading animation with a on-hover loading cursor. A value of **false** will only work when there is content in the `default` slot.
      :type boolean:
      :param loading_text: See description |VSkeletonLoader_vuetify_link|.
      :type string:
      :param type: A string delimited list of skeleton components to create such as `type="text@3"` or `type="card, list-item"`. Will recursively generate a corresponding skeleton from the provided string. Also supports short-hand for multiple elements such as **article@3** and **paragraph@2** which will generate 3 _article_ skeletons and 2 _paragraph_ skeletons. Please see below for a list of available pre-defined options.
      :type | 'avatar'
    | 'button'
    | 'chip'
    | 'divider'
    | 'heading'
    | 'image'
    | 'text'
    | 'sentences'
    | 'paragraph'
    | 'ossein'
    | 'actions'
    | 'article'
    | 'card'
    | 'card-avatar'
    | 'date-picker'
    | 'date-picker-options'
    | 'date-picker-days'
    | 'list-item'
    | 'list-item-avatar'
    | 'list-item-two-line'
    | 'list-item-avatar-two-line'
    | 'list-item-three-line'
    | 'list-item-avatar-three-line'
    | 'subtitle'
    | 'table'
    | 'table-heading'
    | 'table-thead'
    | 'table-tbody'
    | 'table-row-divider'
    | 'table-row'
    | 'table-tfoot'
    | (string & {})
    | (
        | 'avatar'
        | 'button'
        | 'chip'
        | 'divider'
        | 'heading'
        | 'image'
        | 'text'
        | 'sentences'
        | 'paragraph'
        | 'ossein'
        | 'actions'
        | 'article'
        | 'card'
        | 'card-avatar'
        | 'date-picker'
        | 'date-picker-options'
        | 'date-picker-days'
        | 'list-item'
        | 'list-item-avatar'
        | 'list-item-two-line'
        | 'list-item-avatar-two-line'
        | 'list-item-three-line'
        | 'list-item-avatar-three-line'
        | 'subtitle'
        | 'table'
        | 'table-heading'
        | 'table-thead'
        | 'table-tbody'
        | 'table-row-divider'
        | 'table-row'
        | 'table-tfoot'
        | (string & {})
      )[]:
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
      :param theme: Specify a theme for this component and all of its children.
      :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSkeletonLoader", children, **kwargs)
        self._attr_names += [
            "boilerplate",
            "color",
            "loading",
            ("loading_text", "loadingText"),
            "type",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "theme",
        ]
        self._event_names += []


class VSlideGroup(HtmlElement):
    """
    Vuetify's VSlideGroup component. See more info and examples |VSlideGroup_vuetify_link|.

    .. |VSlideGroup_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-group" target="_blank">here</a>


    :param symbol: See description |VSlideGroup_vuetify_link|.
    :type any:
    :param center_active: Forces the selected component to be centered.
    :type boolean:
    :param direction: Switch between horizontal and vertical modes.
    :type 'horizontal' | 'vertical':
    :param next_icon: The appended slot when arrows are shown.
    :type any:
    :param prev_icon: The prepended slot when arrows are shown.
    :type any:
    :param show_arrows: See description |VSlideGroup_vuetify_link|.
    :type string | boolean:
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :type boolean:
    :param mobile_breakpoint: Sets the designated mobile breakpoint for the component.
    :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param multiple: Allows one to select multiple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param disabled: Puts all children components into a disabled state.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideGroup", children, **kwargs)
        self._attr_names += [
            "symbol",
            ("center_active", "centerActive"),
            "direction",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "tag",
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
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
    :param disabled: Removes the ability to click or target the component.
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


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VSlideXReverseTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VSlideXReverseTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VSlideXReverseTransition_vuetify_link|.
    :type string:
    :param origin: See description |VSlideXReverseTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideXReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideXTransition(HtmlElement):
    """
    Vuetify's VSlideXTransition component. See more info and examples |VSlideXTransition_vuetify_link|.

    .. |VSlideXTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-x-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VSlideXTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VSlideXTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VSlideXTransition_vuetify_link|.
    :type string:
    :param origin: See description |VSlideXTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideXTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideYReverseTransition(HtmlElement):
    """
    Vuetify's VSlideYReverseTransition component. See more info and examples |VSlideYReverseTransition_vuetify_link|.

    .. |VSlideYReverseTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-y-reverse-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VSlideYReverseTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VSlideYReverseTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VSlideYReverseTransition_vuetify_link|.
    :type string:
    :param origin: See description |VSlideYReverseTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideYReverseTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideYTransition(HtmlElement):
    """
    Vuetify's VSlideYTransition component. See more info and examples |VSlideYTransition_vuetify_link|.

    .. |VSlideYTransition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-y-transition" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param group: See description |VSlideYTransition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :type boolean:
    :param leave_absolute: See description |VSlideYTransition_vuetify_link|.
    :type boolean:
    :param mode: See description |VSlideYTransition_vuetify_link|.
    :type string:
    :param origin: See description |VSlideYTransition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlideYTransition", children, **kwargs)
        self._attr_names += [
            "disabled",
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlider(HtmlElement):
    """
      Vuetify's VSlider component. See more info and examples |VSlider_vuetify_link|.

      .. |VSlider_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-slider" target="_blank">here</a>


      :param label: See description |VSlider_vuetify_link|.
      :type string:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param reverse: Reverses the slider direction.
      :type boolean:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param max: Sets the maximum allowed value.
      :type string | number:
      :param min: Sets the minimum allowed value.
      :type string | number:
      :param step: If greater than 0, sets step interval for ticks.
      :type string | number:
      :param thumb_color: Sets the thumb and thumb label color.
      :type string:
      :param thumb_label: Show thumb label. If `true` it shows label when using slider. If set to `'always'` it always shows label.
      :type boolean | 'always':
      :param thumb_size: Controls the size of the thumb label.
      :type string | number:
      :param show_ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
      :type boolean | 'always':
      :param ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
      :type number[] | Record<number, string>:
      :param tick_size: Controls the size of **ticks**
      :type string | number:
      :param color: See description |VSlider_vuetify_link|.
      :type string:
      :param track_color: Sets the track's color
      :type string:
      :param track_fill_color: Sets the track's fill color
      :type string:
      :param track_size: Sets the track's size (height).
      :type string | number:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param rounded: See description |VSlider_vuetify_link|.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param elevation: See description |VSlider_vuetify_link|.
      :type string | number:
      :param ripple: See description |VSlider_vuetify_link|.
      :type boolean:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VSlider_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VSlider_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VSlider_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type string | number:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':

      Events

      :param update_focused: Event that is emitted when the component's focus state changes.
      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when appended icon is clicked.
      :param update_modelValue: Event that is emitted when the component's model changes.
      :param start: Slider value emitted at start of slider movement.
      :param end: Slider value emitted at the end of slider movement.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSlider", children, **kwargs)
        self._attr_names += [
            "label",
            "focused",
            "reverse",
            "disabled",
            "error",
            "readonly",
            "max",
            "min",
            "step",
            ("thumb_color", "thumbColor"),
            ("thumb_label", "thumbLabel"),
            ("thumb_size", "thumbSize"),
            ("show_ticks", "showTicks"),
            "ticks",
            ("tick_size", "tickSize"),
            "color",
            ("track_color", "trackColor"),
            ("track_fill_color", "trackFillColor"),
            ("track_size", "trackSize"),
            "direction",
            "rounded",
            "tile",
            "elevation",
            "ripple",
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            ("hide_details", "hideDetails"),
        ]
        self._event_names += [
            ("update_focused", "update:focused"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_modelValue", "update:modelValue"),
            "start",
            "end",
        ]


class VSnackbar(HtmlElement):
    """
      Vuetify's VSnackbar component. See more info and examples |VSnackbar_vuetify_link|.

      .. |VSnackbar_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-snackbar" target="_blank">here</a>


      :param activator: Explicitly sets the overlay's activator.
      :type Element | 'parent' | (string & {}) | ComponentPublicInstance:
      :param text: Specify content text for the component.
      :type string:
      :param multi_line: Gives the snackbar a larger minimum height.
      :type boolean:
      :param timer: Display a progress bar that counts down until the snackbar closes. Pass a string to set a custom color, otherwise uses `info`.
      :type string | boolean:
      :param timeout: Time (in milliseconds) to wait until snackbar is automatically hidden.  Use `-1` to keep open indefinitely (`0` in version < 2.3 ). It is recommended for this number to be between `4000` and `10000`. Changes to this property will reset the timeout.
      :type string | number:
      :param vertical: Stacks snackbar content on top of the actions (button).
      :type boolean:
      :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param position: Sets the position for the component.
      :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
      :param absolute: Applies **position: absolute** to the content element.
      :type boolean:
      :param rounded: See description |VSnackbar_vuetify_link|.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param color: See description |VSnackbar_vuetify_link|.
      :type string:
      :param variant: Applies a distinct style to the component.
      :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
      :type boolean:
      :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
      :type boolean:
      :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
      :type any:
      :param content_props: Apply custom properties to the content.
      :type any:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param opacity: Sets the overlay opacity.
      :type string | number:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type boolean:
      :param z_index: The z-index used for the component.
      :type string | number:
      :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
      :type | Element
    | 'parent'
    | 'cursor'
    | (string & {})
    | ComponentPublicInstance
    | [number, number]:
      :param activator_props: Apply custom properties to the activator.
      :type unknown:
      :param open_on_click: Activate the component when the activator is clicked.
      :type boolean:
      :param open_on_hover: Activate the component when the activator is hovered.
      :type boolean:
      :param open_on_focus: Activate the component when the activator is focused.
      :type boolean:
      :param close_on_content_click: Closes component when you click on its content.
      :type boolean:
      :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
      :type string | number:
      :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
      :type string | number:
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
      :param location_strategy: A function used to specifies how the component should position relative to its activator.
      :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
      :param origin: See description |VSnackbar_vuetify_link|.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
      :param offset: A single value that offsets content away from the target based upon what side it is on.
      :type string | number | number[]:
      :param transition: See description |VSnackbar_vuetify_link|.
      :type string | boolean | (TransitionProps & { component: Component }):
      :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
      :type string | boolean | Element:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSnackbar", children, **kwargs)
        self._attr_names += [
            "activator",
            "text",
            ("multi_line", "multiLine"),
            "timer",
            "timeout",
            "vertical",
            "location",
            "position",
            "absolute",
            "rounded",
            "tile",
            "color",
            "variant",
            "theme",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            "opacity",
            ("model_value", "modelValue"),
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "eager",
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            "transition",
            "attach",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSnackbarQueue(HtmlElement):
    """
        Vuetify's VSnackbarQueue component. See more info and examples |VSnackbarQueue_vuetify_link|.

        .. |VSnackbarQueue_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-snackbar-queue" target="_blank">here</a>


        :param activator: Explicitly sets the overlay's activator.
        :type Element | 'parent' | (string & {}) | ComponentPublicInstance:
        :param text: Specify content text for the component.
        :type string:
        :param multi_line: Gives the snackbar a larger minimum height.
        :type boolean:
        :param timer: Display a progress bar that counts down until the snackbar closes. Pass a string to set a custom color, otherwise uses `info`.
        :type string | boolean:
        :param timeout: Time (in milliseconds) to wait until snackbar is automatically hidden.  Use `-1` to keep open indefinitely (`0` in version < 2.3 ). It is recommended for this number to be between `4000` and `10000`. Changes to this property will reset the timeout.
        :type string | number:
        :param vertical: Stacks snackbar content on top of the actions (button).
        :type boolean:
        :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
        :param position: Sets the position for the component.
        :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
        :param absolute: Applies **position: absolute** to the content element.
        :type boolean:
        :param rounded: See description |VSnackbarQueue_vuetify_link|.
        :type string | number | boolean:
        :param tile: Removes any applied **border-radius** from the component.
        :type boolean:
        :param color: See description |VSnackbarQueue_vuetify_link|.
        :type string:
        :param variant: Applies a distinct style to the component.
        :type 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain':
        :param theme: Specify a theme for this component and all of its children.
        :type string:
        :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
        :type boolean:
        :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
        :type boolean:
        :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
        :type any:
        :param content_props: Apply custom properties to the content.
        :type any:
        :param disabled: Removes the ability to click or target the component.
        :type boolean:
        :param opacity: Sets the overlay opacity.
        :type string | number:
        :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
        :type (
      | string
      | {
          text: string
          multiLine: boolean
          timer: string | boolean
          timeout: string | number
          vertical: boolean
          location: <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>
          position: 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky'
          absolute: boolean
          rounded: string | number | boolean
          tile: boolean
          color: string
          variant: 'text' | 'flat' | 'elevated' | 'tonal' | 'outlined' | 'plain'
          theme: string
          closeOnBack: boolean
          contained: boolean
          contentClass: any
          contentProps: any
          disabled: boolean
          opacity: string | number
          zIndex: string | number
          target:
            | Element
            | 'parent'
            | 'cursor'
            | (string & {})
            | ComponentPublicInstance
            | [number, number]
          closeOnContentClick: boolean
          style: StyleValue
          class: any
          height: string | number
          maxHeight: string | number
          maxWidth: string | number
          minHeight: string | number
          minWidth: string | number
          width: string | number
          eager: boolean
          locationStrategy: 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>
          origin: <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap'
          offset: string | number | number[]
          transition:
            | string
            | boolean
            | (TransitionProps & { component: Component })
          attach: string | boolean | Element
          'v-slots': {
            activator:
              | false
              | ((arg: {
                  isActive: boolean
                  props: Record<string, any>
                }) => VNodeChild)
            default: false | (() => VNodeChild)
            actions: false | ((arg: { isActive: Ref<boolean> }) => VNodeChild)
            text: false | (() => VNodeChild)
          }
          'v-slot:default': false | (() => VNodeChild)
          'v-slot:activator':
            | false
            | ((arg: {
                isActive: boolean
                props: Record<string, any>
              }) => VNodeChild)
          key: string | number | symbol
          ref: VNodeRef
          ref_for: boolean
          ref_key: string
          onVnodeBeforeMount: VNodeMountHook | VNodeMountHook[]
          onVnodeMounted: VNodeMountHook | VNodeMountHook[]
          onVnodeBeforeUpdate: VNodeUpdateHook | VNodeUpdateHook[]
          onVnodeUpdated: VNodeUpdateHook | VNodeUpdateHook[]
          onVnodeBeforeUnmount: VNodeMountHook | VNodeMountHook[]
          onVnodeUnmounted: VNodeMountHook | VNodeMountHook[]
          'v-slot:actions':
            | false
            | ((arg: { isActive: Ref<boolean> }) => VNodeChild)
          'v-slot:text': false | (() => VNodeChild)
        }
    )[]:
        :param z_index: The z-index used for the component.
        :type string | number:
        :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
        :type | Element
      | 'parent'
      | 'cursor'
      | (string & {})
      | ComponentPublicInstance
      | [number, number]:
        :param activator_props: Apply custom properties to the activator.
        :type unknown:
        :param open_on_click: Activate the component when the activator is clicked.
        :type boolean:
        :param open_on_hover: Activate the component when the activator is hovered.
        :type boolean:
        :param open_on_focus: Activate the component when the activator is focused.
        :type boolean:
        :param close_on_content_click: Closes component when you click on its content.
        :type boolean:
        :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
        :type string | number:
        :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
        :type string | number:
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
        :param location_strategy: A function used to specifies how the component should position relative to its activator.
        :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
        :param origin: See description |VSnackbarQueue_vuetify_link|.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
        :param offset: A single value that offsets content away from the target based upon what side it is on.
        :type string | number | number[]:
        :param transition: See description |VSnackbarQueue_vuetify_link|.
        :type string | boolean | (TransitionProps & { component: Component }):
        :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
        :type string | boolean | Element:
        :param closable: Adds a dismiss button that closes the active snackbar.
        :type string | boolean:
        :param close_text: The text used in the close button when using the **closable** prop.
        :type string:

        Events

        :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSnackbarQueue", children, **kwargs)
        self._attr_names += [
            "activator",
            "text",
            ("multi_line", "multiLine"),
            "timer",
            "timeout",
            "vertical",
            "location",
            "position",
            "absolute",
            "rounded",
            "tile",
            "color",
            "variant",
            "theme",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            "opacity",
            ("model_value", "modelValue"),
            ("z_index", "zIndex"),
            "target",
            ("activator_props", "activatorProps"),
            ("open_on_click", "openOnClick"),
            ("open_on_hover", "openOnHover"),
            ("open_on_focus", "openOnFocus"),
            ("close_on_content_click", "closeOnContentClick"),
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "eager",
            ("location_strategy", "locationStrategy"),
            "origin",
            "offset",
            "transition",
            "attach",
            "closable",
            ("close_text", "closeText"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSpacer(HtmlElement):
    """
    Vuetify's VSpacer component. See more info and examples |VSpacer_vuetify_link|.

    .. |VSpacer_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-spacer" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSpacer", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VSparkline(HtmlElement):
    """
    Vuetify's VSparkline component. See more info and examples |VSparkline_vuetify_link|.

    .. |VSparkline_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-sparkline" target="_blank">here</a>


    :param type: Choose between a trendline or bars.
    :type 'trend' | 'bar':
    :param auto_line_width: Automatically expand bars to use space efficiently.
    :type boolean:
    :param auto_draw: Trace the length of the line when first rendered.
    :type boolean:
    :param auto_draw_duration: Amount of time (in ms) to run the trace animation.
    :type string | number:
    :param auto_draw_easing: The easing function to use for the trace animation.
    :type string:
    :param color: See description |VSparkline_vuetify_link|.
    :type string:
    :param gradient: An array of colors to use as a linear-gradient.
    :type string[]:
    :param gradient_direction: The direction the gradient should run.
    :type 'top' | 'bottom' | 'left' | 'right':
    :param height: Height of the SVG trendline or bars.
    :type string | number:
    :param labels: An array of string labels that correspond to the same index as its data counterpart.
    :type (number | { value: number })[]:
    :param label_size: The label font size.
    :type string | number:
    :param line_width: The thickness of the line, in px.
    :type string | number:
    :param id: See description |VSparkline_vuetify_link|.
    :type string:
    :param item_value: See description |VSparkline_vuetify_link|.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type (number | { value: number })[]:
    :param min: See description |VSparkline_vuetify_link|.
    :type string | number:
    :param max: See description |VSparkline_vuetify_link|.
    :type string | number:
    :param padding: Low `smooth` or high `line-width` values may result in cropping, increase padding to compensate.
    :type string | number:
    :param show_labels: Show labels below each data point.
    :type boolean:
    :param smooth: Number of px to use as a corner radius. `true` defaults to 8, `false` is 0.
    :type boolean:
    :param width: Width of the SVG trendline or bars.
    :type string | number:
    :param fill: Using the **fill** property allows you to better customize the look and feel of your sparkline.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSparkline", children, **kwargs)
        self._attr_names += [
            "type",
            ("auto_line_width", "autoLineWidth"),
            ("auto_draw", "autoDraw"),
            ("auto_draw_duration", "autoDrawDuration"),
            ("auto_draw_easing", "autoDrawEasing"),
            "color",
            "gradient",
            ("gradient_direction", "gradientDirection"),
            "height",
            "labels",
            ("label_size", "labelSize"),
            ("line_width", "lineWidth"),
            "id",
            ("item_value", "itemValue"),
            ("model_value", "modelValue"),
            "min",
            "max",
            "padding",
            ("show_labels", "showLabels"),
            "smooth",
            "width",
            "fill",
        ]
        self._event_names += []


class VSpeedDial(HtmlElement):
    """
      Vuetify's VSpeedDial component. See more info and examples |VSpeedDial_vuetify_link|.

      .. |VSpeedDial_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-speed-dial" target="_blank">here</a>


      :param activator: Explicitly sets the overlay's activator.
      :type (string & {}) | Element | 'parent' | ComponentPublicInstance:
      :param id: The unique identifier of the component.
      :type string:
      :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
      :type boolean:
      :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
      :type boolean:
      :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
      :type any:
      :param content_props: Apply custom properties to the content.
      :type any:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param opacity: Sets the overlay opacity.
      :type string | number:
      :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type boolean:
      :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
      :type boolean:
      :param scrim: Accepts true/false to enable background, and string to define color.
      :type string | boolean:
      :param z_index: The z-index used for the component.
      :type string | number:
      :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
      :type | (string & {})
    | Element
    | 'parent'
    | 'cursor'
    | ComponentPublicInstance
    | [number, number]:
      :param activator_props: Apply custom properties to the activator.
      :type unknown:
      :param open_on_click: Activate the component when the activator is clicked.
      :type boolean:
      :param open_on_hover: Opens speed-dial on hover.
      :type boolean:
      :param open_on_focus: Activate the component when the activator is focused.
      :type boolean:
      :param close_on_content_click: Closes component when you click on its content.
      :type boolean:
      :param close_delay: Milliseconds to wait before closing component. Only works with the **open-on-hover** prop.
      :type string | number:
      :param open_delay: Milliseconds to wait before opening component. Only works with the **open-on-hover** prop.
      :type string | number:
      :param height: Sets the height for the component.
      :type string | number:
      :param max_height: Sets the maximum height for the component.
      :type string | number:
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_height: Sets the minimum height for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component. Use `auto` to use the activator width.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
      :type boolean:
      :param location_strategy: A function used to specifies how the component should position relative to its activator.
      :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
      :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param origin: See description |VSpeedDial_vuetify_link|.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
      :param offset: A single value that offsets content away from the target based upon what side it is on.
      :type string | number | number[]:
      :param scroll_strategy: Strategy used when the component is activate and user scrolls.
      :type 'none' | 'close' | 'block' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param transition: See description |VSpeedDial_vuetify_link|.
      :type | { component: Component }
    | string
    | boolean
    | (TransitionProps & { component: Component }):
      :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default. Generally not recommended except as a last resort: the default positioning algorithm should handle most scenarios better than is possible without teleporting, and you may have unexpected behavior if the menu ends up as child of its activator.
      :type string | boolean | Element:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSpeedDial", children, **kwargs)
        self._attr_names += [
            "activator",
            "id",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
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
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "eager",
            ("location_strategy", "locationStrategy"),
            "location",
            "origin",
            "offset",
            ("scroll_strategy", "scrollStrategy"),
            "theme",
            "transition",
            "attach",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VStepper(HtmlElement):
    """
    Vuetify's VStepper component. See more info and examples |VStepper_vuetify_link|.

    .. |VStepper_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-stepper" target="_blank">here</a>


    :param flat: Removes the stepper's elevation.
    :type boolean:
    :param alt_labels: Places the labels beneath the step.
    :type boolean:
    :param bg_color: See description |VStepper_vuetify_link|.
    :type string:
    :param complete_icon: See description |VStepper_vuetify_link|.
    :type string:
    :param edit_icon: See description |VStepper_vuetify_link|.
    :type string:
    :param editable: Marks step as editable.
    :type boolean:
    :param error_icon: See description |VStepper_vuetify_link|.
    :type string:
    :param hide_actions: Hide actions bar (prev and next buttons).
    :type boolean:
    :param items: An array of strings or objects used for automatically generating children components.
    :type (string | Record<string, any>)[]:
    :param item_title: Property on supplied `items` that contains its title.
    :type string:
    :param item_value: Property on supplied `items` that contains its value.
    :type string:
    :param non_linear: Allow user to jump to any step.
    :type boolean:
    :param mobile: Forces the stepper into a mobile state, removing labels from stepper items.
    :type boolean:
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type any:
    :param multiple: Allows one to select multiple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param disabled: Puts all children components into a disabled state.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param color: See description |VStepper_vuetify_link|.
    :type string:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param elevation: See description |VStepper_vuetify_link|.
    :type string | number:
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VStepper_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param prev_text: The text used for the Prev button.
    :type string:
    :param next_text: The text used for the Next button.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepper", children, **kwargs)
        self._attr_names += [
            "flat",
            ("alt_labels", "altLabels"),
            ("bg_color", "bgColor"),
            ("complete_icon", "completeIcon"),
            ("edit_icon", "editIcon"),
            "editable",
            ("error_icon", "errorIcon"),
            ("hide_actions", "hideActions"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("non_linear", "nonLinear"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
            "color",
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
            ("prev_text", "prevText"),
            ("next_text", "nextText"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VStepperActions(HtmlElement):
    """
    Vuetify's VStepperActions component. See more info and examples |VStepperActions_vuetify_link|.

    .. |VStepperActions_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-stepper-actions" target="_blank">here</a>


    :param color: See description |VStepperActions_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean | 'prev' | 'next':
    :param prev_text: The text used for the Prev button.
    :type string:
    :param next_text: The text used for the Next button.
    :type string:

    Events

    :param click_prev: Event emitted when clicking the prev button.
    :param click_next: Event emitted when clicking the next button.
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
    Vuetify's VStepperHeader component. See more info and examples |VStepperHeader_vuetify_link|.

    .. |VStepperHeader_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-stepper-header" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperHeader", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VStepperItem(HtmlElement):
    """
    Vuetify's VStepperItem component. See more info and examples |VStepperItem_vuetify_link|.

    .. |VStepperItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-stepper-item" target="_blank">here</a>


    :param icon: See description |VStepperItem_vuetify_link|.
    :type string:
    :param title: Specify a title text for the component.
    :type string:
    :param subtitle: Specify a subtitle text for the component.
    :type string:
    :param color: See description |VStepperItem_vuetify_link|.
    :type string:
    :param complete: Marks step as complete.
    :type boolean:
    :param complete_icon: Icon to display when step is marked as completed.
    :type string:
    :param editable: Marks step as editable.
    :type boolean:
    :param edit_icon: Icon to display when step is editable.
    :type string:
    :param error: Puts the stepper item in a manual error state.
    :type boolean:
    :param error_icon: Icon to display when step has an error.
    :type string:
    :param ripple: See description |VStepperItem_vuetify_link|.
    :type boolean | { class: string }:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VStepper/VStepperItem.tsx#L42-L42" target="_blank">ValidationRule</a>[]:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:

    Events

    :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperItem", children, **kwargs)
        self._attr_names += [
            "icon",
            "title",
            "subtitle",
            "color",
            "complete",
            ("complete_icon", "completeIcon"),
            "editable",
            ("edit_icon", "editIcon"),
            "error",
            ("error_icon", "errorIcon"),
            "ripple",
            "value",
            "rules",
            "disabled",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VStepperVertical(HtmlElement):
    """
    Vuetify's VStepperVertical component. See more info and examples |VStepperVertical_vuetify_link|.

    .. |VStepperVertical_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-stepper-vertical" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string:
    :param flat: Removes the expansion-panel's elevation and borders.
    :type boolean:
    :param prev_text: The text used for the Prev button.
    :type string:
    :param next_text: The text used for the Next button.
    :type string:
    :param alt_labels: Places the labels beneath the step.
    :type boolean:
    :param bg_color: See description |VStepperVertical_vuetify_link|.
    :type string:
    :param complete_icon: See description |VStepperVertical_vuetify_link|.
    :type string:
    :param edit_icon: See description |VStepperVertical_vuetify_link|.
    :type string:
    :param editable: Marks step as editable.
    :type boolean:
    :param error_icon: See description |VStepperVertical_vuetify_link|.
    :type string:
    :param hide_actions: Hide actions bar (prev and next buttons).
    :type boolean:
    :param items: An array of strings or objects used for automatically generating children components.
    :type (string | Record<string, any>)[]:
    :param item_title: Property on supplied `items` that contains its title.
    :type string:
    :param item_value: Property on supplied `items` that contains its value.
    :type string:
    :param value: Controls the opened/closed state of content.
    :type any:
    :param non_linear: Allow user to jump to any step.
    :type boolean:
    :param mobile: Forces the stepper into a mobile state, removing labels from stepper items.
    :type boolean:
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type any:
    :param multiple: Allows one to select multiple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param disabled: Disables the expansion-panel content.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param text: Specify content text for the component.
    :type string:
    :param elevation: See description |VStepperVertical_vuetify_link|.
    :type string | number:
    :param rounded: See description |VStepperVertical_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes the border-radius.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param color: See description |VStepperVertical_vuetify_link|.
    :type string:
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :type any:
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :type any:
    :param focusable: Makes the expansion-panel headers focusable.
    :type boolean:
    :param ripple: See description |VStepperVertical_vuetify_link|.
    :type boolean | { class: string }:
    :param readonly: Makes the expansion-panel content read only.
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'default' | 'accordion' | 'inset' | 'popout':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperVertical", children, **kwargs)
        self._attr_names += [
            "title",
            "flat",
            ("prev_text", "prevText"),
            ("next_text", "nextText"),
            ("alt_labels", "altLabels"),
            ("bg_color", "bgColor"),
            ("complete_icon", "completeIcon"),
            ("edit_icon", "editIcon"),
            "editable",
            ("error_icon", "errorIcon"),
            ("hide_actions", "hideActions"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            "value",
            ("non_linear", "nonLinear"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
            "text",
            "elevation",
            "rounded",
            "tile",
            "tag",
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "focusable",
            "ripple",
            "readonly",
            "eager",
            "theme",
            "variant",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VStepperVerticalActions(HtmlElement):
    """
    Vuetify's VStepperVerticalActions component. See more info and examples |VStepperVerticalActions_vuetify_link|.

    .. |VStepperVerticalActions_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-stepper-vertical-actions" target="_blank">here</a>


    :param color: See description |VStepperVerticalActions_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean | 'prev' | 'next':
    :param prev_text: The text used for the Prev button.
    :type string:
    :param next_text: The text used for the Next button.
    :type string:

    Events

    :param click_prev: Event emitted when clicking the prev button.
    :param click_next: Event emitted when clicking the next button.
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
    Vuetify's VStepperVerticalItem component. See more info and examples |VStepperVerticalItem_vuetify_link|.

    .. |VStepperVerticalItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-stepper-vertical-item" target="_blank">here</a>


    :param icon: See description |VStepperVerticalItem_vuetify_link|.
    :type string:
    :param subtitle: Specify a subtitle text for the component.
    :type string:
    :param title: Specify a title text for the component.
    :type string:
    :param text: Specify content text for the component.
    :type string:
    :param hide_actions: Hide the expand icon in the content title.
    :type boolean:
    :param color: See description |VStepperVerticalItem_vuetify_link|.
    :type string:
    :param complete: Marks step as complete.
    :type boolean:
    :param complete_icon: Icon to display when step is marked as completed.
    :type string:
    :param editable: Marks step as editable.
    :type boolean:
    :param edit_icon: Icon to display when step is editable.
    :type string:
    :param error: Puts the stepper item in a manual error state.
    :type boolean:
    :param error_icon: Icon to display when step has an error.
    :type string:
    :param ripple: See description |VStepperVerticalItem_vuetify_link|.
    :type boolean | { class: string }:
    :param value: Controls the opened/closed state of content.
    :type any:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VStepper/VStepperItem.tsx#L42-L42" target="_blank">ValidationRule</a>[]:
    :param bg_color: See description |VStepperVerticalItem_vuetify_link|.
    :type string:
    :param elevation: See description |VStepperVerticalItem_vuetify_link|.
    :type string | number:
    :param disabled: Disables the expansion-panel content.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param rounded: See description |VStepperVerticalItem_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :type any:
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :type any:
    :param focusable: See description |VStepperVerticalItem_vuetify_link|.
    :type boolean:
    :param static: Remove title size expansion when selected.
    :type boolean:
    :param readonly: Makes the expansion-panel content read only.
    :type boolean:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:

    Events

    :param click_next: Event emitted when clicking the next button
    :param click_prev: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VStepperVerticalItem.json))
    :param click_finish: Event emitted when clicking the finish button
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperVerticalItem", children, **kwargs)
        self._attr_names += [
            "icon",
            "subtitle",
            "title",
            "text",
            ("hide_actions", "hideActions"),
            "color",
            "complete",
            ("complete_icon", "completeIcon"),
            "editable",
            ("edit_icon", "editIcon"),
            "error",
            ("error_icon", "errorIcon"),
            "ripple",
            "value",
            "rules",
            ("bg_color", "bgColor"),
            "elevation",
            "disabled",
            ("selected_class", "selectedClass"),
            "rounded",
            "tile",
            "tag",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            "focusable",
            "static",
            "readonly",
            "eager",
        ]
        self._event_names += [
            ("click_next", "click:next"),
            ("click_prev", "click:prev"),
            ("click_finish", "click:finish"),
        ]


class VStepperWindow(HtmlElement):
    """
    Vuetify's VStepperWindow component. See more info and examples |VStepperWindow_vuetify_link|.

    .. |VStepperWindow_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-stepper-window" target="_blank">here</a>


    :param reverse: Reverse the normal transition direction.
    :type boolean:
    :param direction: The transition direction when changing windows.
    :type 'horizontal' | 'vertical':
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type any:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperWindow", children, **kwargs)
        self._attr_names += [
            "reverse",
            "direction",
            ("model_value", "modelValue"),
            "disabled",
            ("selected_class", "selectedClass"),
            "tag",
            "theme",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VStepperWindowItem(HtmlElement):
    """
    Vuetify's VStepperWindowItem component. See more info and examples |VStepperWindowItem_vuetify_link|.

    .. |VStepperWindowItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-stepper-window-item" target="_blank">here</a>


    :param reverse_transition: Sets the reverse transition.
    :type string | boolean:
    :param transition: See description |VStepperWindowItem_vuetify_link|.
    :type string | boolean:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VStepperWindowItem", children, **kwargs)
        self._attr_names += [
            ("reverse_transition", "reverseTransition"),
            "transition",
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "eager",
        ]
        self._event_names += []


class VSvgIcon(HtmlElement):
    """
    Vuetify's VSvgIcon component. See more info and examples |VSvgIcon_vuetify_link|.

    .. |VSvgIcon_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-svg-icon" target="_blank">here</a>


    :param icon: See description |VSvgIcon_vuetify_link|.
    :type any:
    :param tag: Specify a custom tag used on the root element.
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


      :param label: See description |VSwitch_vuetify_link|.
      :type string:
      :param indeterminate: Sets an indeterminate state for the switch.
      :type boolean:
      :param inset: Enlarge the `v-switch` track to encompass the thumb.
      :type boolean:
      :param flat: Display component without elevation. Default elevation for thumb is 4dp, `flat` resets it.
      :type boolean:
      :param loading: Displays circular progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - primary, secondary, success, info, warning, error) or a Boolean which uses the component color (set by color prop - if it's supported by the component) or the primary color.
      :type string | boolean:
      :param type: Provides the default type for children selection controls.
      :type string:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VSwitch_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VSwitch_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VSwitch_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type unknown:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'input'
    | 'blur'
    | 'submit'
    | 'input lazy'
    | 'blur lazy'
    | 'submit lazy'
    | 'lazy input'
    | 'lazy blur'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param true_value: Sets value for truthy state.
      :type any:
      :param false_value: Sets value for falsy state.
      :type any:
      :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
      :type any:
      :param color: See description |VSwitch_vuetify_link|.
      :type string:
      :param defaults_target: The target component to provide defaults values for.
      :type string:
      :param inline: Puts children inputs into a row.
      :type boolean:
      :param false_icon: The icon used when inactive.
      :type any:
      :param true_icon: The icon used when active.
      :type any:
      :param ripple: See description |VSwitch_vuetify_link|.
      :type boolean | { class: string }:
      :param multiple: Changes expected model to an array.
      :type boolean:
      :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
      :type (a: any, b: any) => boolean:

      Events

      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when appended icon is clicked.
      :param update_focused: Event that is emitted when the component's focus state changes.
      :param update_modelValue: Event that is emitted when the component's model changes.
      :param update_indeterminate: Event that is emitted when the component's indeterminate state changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSwitch", children, **kwargs)
        self._attr_names += [
            "label",
            "indeterminate",
            "inset",
            "flat",
            "loading",
            "type",
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("base_color", "baseColor"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            ("defaults_target", "defaultsTarget"),
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "multiple",
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("update_modelValue", "update:modelValue"),
            ("update_indeterminate", "update:indeterminate"),
        ]


class VSystemBar(HtmlElement):
    """
    Vuetify's VSystemBar component. See more info and examples |VSystemBar_vuetify_link|.

    .. |VSystemBar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-system-bar" target="_blank">here</a>


    :param color: See description |VSystemBar_vuetify_link|.
    :type string:
    :param height: Sets the height for the component.
    :type string | number:
    :param window: Increases the system bar height to 32px (24px default).
    :type boolean:
    :param elevation: See description |VSystemBar_vuetify_link|.
    :type string | number:
    :param name: Assign a specific name for layout registration.
    :type string:
    :param order: Adjust the order of the component in relation to its registration order.
    :type string | number:
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param rounded: See description |VSystemBar_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VSystemBar", children, **kwargs)
        self._attr_names += [
            "color",
            "height",
            "window",
            "elevation",
            "name",
            "order",
            "absolute",
            "rounded",
            "tile",
            "tag",
            "theme",
        ]
        self._event_names += []


class VTab(HtmlElement):
    """
    Vuetify's VTab component. See more info and examples |VTab_vuetify_link|.

    .. |VTab_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-tab" target="_blank">here</a>


    :param fixed: Forces component to take up all available space up to their maximum width (300px), and centers it.
    :type boolean:
    :param slider_color: See description |VTab_vuetify_link|.
    :type string:
    :param hide_slider: Hides the active tab slider component (no exit or enter animation).
    :type boolean:
    :param direction: Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
    :type 'horizontal' | 'vertical':
    :param base_color: Sets the color of component when not focused.
    :type string:
    :param prepend_icon: See description |VTab_vuetify_link|.
    :type any:
    :param append_icon: See description |VTab_vuetify_link|.
    :type any:
    :param readonly: Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.
    :type boolean:
    :param slim: Reduces padding to 0 8px.
    :type boolean:
    :param stacked: Displays the tab as a flex-column.
    :type boolean:
    :param ripple: See description |VTab_vuetify_link|.
    :type boolean | { class: string }:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param text: Specify content text for the component.
    :type string:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param elevation: See description |VTab_vuetify_link|.
    :type string | number:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :type string | boolean:
    :param rounded: See description |VTab_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VTab_vuetify_link|.
    :type boolean:
    :param exact: See description |VTab_vuetify_link|.
    :type boolean:
    :param to: See description |VTab_vuetify_link|.
    :type RouteLocationRaw:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VTab_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'text' | 'elevated' | 'tonal' | 'outlined' | 'plain':
    :param icon: See description |VTab_vuetify_link|.
    :type any:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTab", children, **kwargs)
        self._attr_names += [
            "fixed",
            ("slider_color", "sliderColor"),
            ("hide_slider", "hideSlider"),
            "direction",
            ("base_color", "baseColor"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "readonly",
            "slim",
            "stacked",
            "ripple",
            "value",
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
            "rounded",
            "tile",
            "href",
            "replace",
            "exact",
            "to",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
            "icon",
        ]
        self._event_names += []


class VTable(HtmlElement):
    """
    Vuetify's VTable component. See more info and examples |VTable_vuetify_link|.

    .. |VTable_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-table" target="_blank">here</a>


    :param fixed_header: Use the fixed-header prop together with the height prop to fix the header to the top of the table.
    :type boolean:
    :param fixed_footer: Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.
    :type boolean:
    :param height: Use the height prop to set the height of the table.
    :type string | number:
    :param hover: Will add a hover effect to a table's row when the mouse is over it.
    :type boolean:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTable", children, **kwargs)
        self._attr_names += [
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            "height",
            "hover",
            "density",
            "tag",
            "theme",
        ]
        self._event_names += []


class VTabs(HtmlElement):
    """
    Vuetify's VTabs component. See more info and examples |VTabs_vuetify_link|.

    .. |VTabs_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-tabs" target="_blank">here</a>


    :param symbol: See description |VTabs_vuetify_link|.
    :type any:
    :param align_tabs: Aligns the tabs to the `start`, `center`, or `end` of container. Also accepts `title` to align with the `v-toolbar-title` component.
    :type 'start' | 'title' | 'center' | 'end':
    :param color: See description |VTabs_vuetify_link|.
    :type string:
    :param fixed_tabs: `v-tabs-item` min-width 160px, max-width 360px.
    :type boolean:
    :param items: The items to display in the component. This can be an array of strings or objects with a property `text`.
    :type (string | number | Record<string, any>)[]:
    :param stacked: Apply the stacked prop to all children v-tab components.
    :type boolean:
    :param bg_color: See description |VTabs_vuetify_link|.
    :type string:
    :param grow: Force `v-tab`'s to take up all available space.
    :type boolean:
    :param height: Sets the height of the tabs bar.
    :type string | number:
    :param hide_slider: Hide's the generated `v-tabs-slider`.
    :type boolean:
    :param slider_color: Changes the background color of an auto-generated `v-tabs-slider`.
    :type string:
    :param center_active: Forces the selected tab to be centered.
    :type boolean:
    :param direction: Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
    :type 'horizontal' | 'vertical':
    :param next_icon: Right pagination icon.
    :type any:
    :param prev_icon: Left pagination icon.
    :type any:
    :param show_arrows: Show pagination arrows if the tab items overflow their container. For mobile devices, arrows will only display when using this prop.
    :type string | boolean:
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :type boolean:
    :param mobile_breakpoint: Sets the designated mobile breakpoint for the component.
    :type number | 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl':
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type any:
    :param multiple: Allows one to select multiple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param disabled: Puts all children components into a disabled state.
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'comfortable' | 'compact':

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTabs", children, **kwargs)
        self._attr_names += [
            "symbol",
            ("align_tabs", "alignTabs"),
            "color",
            ("fixed_tabs", "fixedTabs"),
            "items",
            "stacked",
            ("bg_color", "bgColor"),
            "grow",
            "height",
            ("hide_slider", "hideSlider"),
            ("slider_color", "sliderColor"),
            ("center_active", "centerActive"),
            "direction",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            "mobile",
            ("mobile_breakpoint", "mobileBreakpoint"),
            "tag",
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
            "density",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTabsWindow(HtmlElement):
    """
    Vuetify's VTabsWindow component. See more info and examples |VTabsWindow_vuetify_link|.

    .. |VTabsWindow_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-tabs-window" target="_blank">here</a>


    :param reverse: Reverse the normal transition direction.
    :type boolean:
    :param direction: The transition direction when changing windows.
    :type 'horizontal' | 'vertical':
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type any:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTabsWindow", children, **kwargs)
        self._attr_names += [
            "reverse",
            "direction",
            ("model_value", "modelValue"),
            "disabled",
            ("selected_class", "selectedClass"),
            "tag",
            "theme",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTabsWindowItem(HtmlElement):
    """
    Vuetify's VTabsWindowItem component. See more info and examples |VTabsWindowItem_vuetify_link|.

    .. |VTabsWindowItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-tabs-window-item" target="_blank">here</a>


    :param reverse_transition: Sets the reverse transition.
    :type string | boolean:
    :param transition: See description |VTabsWindowItem_vuetify_link|.
    :type string | boolean:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTabsWindowItem", children, **kwargs)
        self._attr_names += [
            ("reverse_transition", "reverseTransition"),
            "transition",
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "eager",
        ]
        self._event_names += []


class VTextField(HtmlElement):
    """
      Vuetify's VTextField component. See more info and examples |VTextField_vuetify_link|.

      .. |VTextField_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-text-field" target="_blank">here</a>


      :param label: See description |VTextField_vuetify_link|.
      :type string:
      :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
      :type string | number | boolean:
      :param flat: Removes elevation (shadow) added to element when using the **solo** or **solo-inverted** props.
      :type boolean:
      :param autofocus: Enables autofocus.
      :type boolean:
      :param prefix: Displays prefix text.
      :type string:
      :param placeholder: Sets the input’s placeholder text.
      :type string:
      :param persistent_placeholder: Forces placeholder to always be visible.
      :type boolean:
      :param persistent_counter: Forces counter to always be visible.
      :type boolean:
      :param suffix: Displays suffix text.
      :type string:
      :param role: The role attribute applied to the input.
      :type string:
      :param type: Sets input type.
      :type string:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VTextField_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VTextField_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VTextField_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param reverse: Reverses the input orientation.
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the input.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type any:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param append_inner_icon: See description |VTextField_vuetify_link|.
      :type any:
      :param bg_color: See description |VTextField_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared.
      :type boolean:
      :param clear_icon: Applied when using **clearable** and the input is dirty.
      :type any:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component.
      :type boolean:
      :param color: See description |VTextField_vuetify_link|.
      :type string:
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param dirty: Manually apply the dirty state styling.
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
      :type boolean:
      :param prepend_inner_icon: Prepends an icon inside the component's input, uses the same syntax as `v-icon`.
      :type any:
      :param single_line: Label does not move on focus/dirty.
      :type boolean:
      :param variant: Applies a distinct style to the component.
      :type | 'underlined'
    | 'outlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled'
    | 'plain':
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
      :type string | boolean:
      :param rounded: Adds a border radius to the input.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param counter_value: Function returns the counter display text.
      :type number | ((value: any) => number):
      :param model_modifiers: **FOR INTERNAL USE ONLY**
      :type unknown:

      Events

      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when append icon is clicked.
      :param update_focused: Emitted when the input is focused or blurred
      :param click_clear: Emitted when clearable icon clicked.
      :param click_appendInner: Emitted when appended inner icon is clicked.
      :param click_prependInner: Emitted when prepended inner icon is clicked.
      :param click_control: Emitted when the main input is clicked.
      :param mousedown_control: Event that is emitted when using mousedown on the main control area.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTextField", children, **kwargs)
        self._attr_names += [
            "label",
            "counter",
            "flat",
            "autofocus",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            "role",
            "type",
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "color",
            ("base_color", "baseColor"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "loading",
            "rounded",
            "tile",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("click_control", "click:control"),
            ("mousedown_control", "mousedown:control"),
            ("update_modelValue", "update:modelValue"),
        ]


class VTextarea(HtmlElement):
    """
      Vuetify's VTextarea component. See more info and examples |VTextarea_vuetify_link|.

      .. |VTextarea_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-textarea" target="_blank">here</a>


      :param label: See description |VTextarea_vuetify_link|.
      :type string:
      :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
      :type string | number | true:
      :param flat: Removes box shadow when using a variant with elevation.
      :type boolean:
      :param auto_grow: Automatically grow the textarea depending on amount of text.
      :type boolean:
      :param autofocus: See description |VTextarea_vuetify_link|.
      :type boolean:
      :param prefix: Displays prefix text.
      :type string:
      :param placeholder: Sets the input's placeholder text.
      :type string:
      :param persistent_placeholder: Forces placeholder to always be visible.
      :type boolean:
      :param persistent_counter: Forces counter to always be visible.
      :type boolean:
      :param no_resize: Remove resize handle.
      :type boolean:
      :param rows: Default row count.
      :type string | number:
      :param max_rows: Specifies the maximum number of row count
      :type string | number:
      :param suffix: Displays suffix text.
      :type string:
      :param id: Sets the DOM id on the component.
      :type string:
      :param append_icon: See description |VTextarea_vuetify_link|.
      :type any:
      :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
      :type boolean:
      :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
      :type any:
      :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
      :type boolean:
      :param hint: See description |VTextarea_vuetify_link|.
      :type string:
      :param persistent_hint: See description |VTextarea_vuetify_link|.
      :type boolean:
      :param messages: Displays a list of messages or a single message if using a string.
      :type string | string[]:
      :param direction: Changes the direction of the input.
      :type 'horizontal' | 'vertical':
      :param reverse: Reverses the orientation.
      :type boolean:
      :param density: Adjusts the vertical height used by the component.
      :type 'default' | 'comfortable' | 'compact':
      :param max_width: Sets the maximum width for the component.
      :type string | number:
      :param min_width: Sets the minimum width for the component.
      :type string | number:
      :param width: Sets the width for the component.
      :type string | number:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param disabled: Removes the ability to click or target the input.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type any:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:
      :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
      :type boolean | 'auto':
      :param append_inner_icon: See description |VTextarea_vuetify_link|.
      :type any:
      :param bg_color: See description |VTextarea_vuetify_link|.
      :type string:
      :param clearable: Allows for the component to be cleared.
      :type boolean:
      :param clear_icon: The icon used when the **clearable** prop is set to true.
      :type any:
      :param active: Controls the **active** state of the item. This is typically used to highlight the component.
      :type boolean:
      :param color: See description |VTextarea_vuetify_link|.
      :type string:
      :param base_color: Sets the color of the input when it is not focused.
      :type string:
      :param dirty: Manually apply the dirty state styling.
      :type boolean:
      :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
      :type boolean:
      :param prepend_inner_icon: See description |VTextarea_vuetify_link|.
      :type any:
      :param single_line: Label does not move on focus/dirty.
      :type boolean:
      :param variant: Applies a distinct style to the component.
      :type | 'underlined'
    | 'outlined'
    | 'filled'
    | 'solo'
    | 'solo-inverted'
    | 'solo-filled'
    | 'plain':
      :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
      :type string | boolean:
      :param rounded: See description |VTextarea_vuetify_link|.
      :type string | number | boolean:
      :param tile: Removes any applied **border-radius** from the component.
      :type boolean:
      :param counter_value: Display the input length but do not provide any validation.
      :type (value: any) => number:
      :param model_modifiers: **FOR INTERNAL USE ONLY**
      :type unknown:

      Events

      :param click_prepend: Emitted when prepended icon is clicked.
      :param click_append: Emitted when append icon is clicked.
      :param update_focused: Emitted when the input is focused or blurred
      :param click_clear: Emitted when clearable icon clicked.
      :param click_appendInner: Emitted when appended inner icon is clicked.
      :param click_prependInner: Emitted when prepended inner icon is clicked.
      :param click_control: Emitted when the main input is clicked.
      :param mousedown_control: Event that is emitted when using mousedown on the main control area.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTextarea", children, **kwargs)
        self._attr_names += [
            "label",
            "counter",
            "flat",
            ("auto_grow", "autoGrow"),
            "autofocus",
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            ("no_resize", "noResize"),
            "rows",
            ("max_rows", "maxRows"),
            "suffix",
            "id",
            ("append_icon", "appendIcon"),
            ("center_affix", "centerAffix"),
            ("prepend_icon", "prependIcon"),
            ("hide_spin_buttons", "hideSpinButtons"),
            "hint",
            ("persistent_hint", "persistentHint"),
            "messages",
            "direction",
            "reverse",
            "density",
            ("max_width", "maxWidth"),
            ("min_width", "minWidth"),
            "width",
            "theme",
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "color",
            ("base_color", "baseColor"),
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "loading",
            "rounded",
            "tile",
            ("counter_value", "counterValue"),
            ("model_modifiers", "modelModifiers"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("click_control", "click:control"),
            ("mousedown_control", "mousedown:control"),
            ("update_modelValue", "update:modelValue"),
        ]


class VThemeProvider(HtmlElement):
    """
    Vuetify's VThemeProvider component. See more info and examples |VThemeProvider_vuetify_link|.

    .. |VThemeProvider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-theme-provider" target="_blank">here</a>


    :param with_background: See description |VThemeProvider_vuetify_link|.
    :type boolean:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VThemeProvider", children, **kwargs)
        self._attr_names += [
            ("with_background", "withBackground"),
            "theme",
            "tag",
        ]
        self._event_names += []


class VTimePicker(HtmlElement):
    """
    Vuetify's VTimePicker component. See more info and examples |VTimePicker_vuetify_link|.

    .. |VTimePicker_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-time-picker" target="_blank">here</a>


    :param title: Specify a title text for the component.
    :type string:
    :param ampm_in_title: Place AM/PM switch in title, not near the clock.
    :type boolean:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param format: Defines the format of a time displayed in picker. Available options are `ampm` and `24hr`.
    :type 'ampm' | '24hr':
    :param max: Maximum allowed time.
    :type string:
    :param min: Minimum allowed time.
    :type string:
    :param readonly: Puts picker in readonly state.
    :type boolean:
    :param scrollable: Allows changing hour/minute with mouse scroll.
    :type boolean:
    :param use_seconds: See description |VTimePicker_vuetify_link|.
    :type boolean:
    :param bg_color: See description |VTimePicker_vuetify_link|.
    :type string:
    :param hide_header: Hide the picker header.
    :type boolean:
    :param color: See description |VTimePicker_vuetify_link|.
    :type string:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param width: Width of the picker.
    :type string | number:
    :param elevation: See description |VTimePicker_vuetify_link|.
    :type string | number:
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
    :param position: Sets the position for the component.
    :type 'static' | 'relative' | 'fixed' | 'absolute' | 'sticky':
    :param rounded: See description |VTimePicker_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param allowed_hours: Restricts which hours can be selected.
    :type ((val: number) => boolean) | number[]:
    :param allowed_minutes: Restricts which minutes can be selected.
    :type ((val: number) => boolean) | number[]:
    :param allowed_seconds: Restricts which seconds can be selected.
    :type ((val: number) => boolean) | number[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type any:

    Events

    :param update_hour: Emitted when user selects the hour.
    :param update_minute: Emitted when user selects the minute.
    :param update_period: Emitted when user clicks the AM/PM button.
    :param update_second: Emitted when user selects the second.
    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimePicker", children, **kwargs)
        self._attr_names += [
            "title",
            ("ampm_in_title", "ampmInTitle"),
            "disabled",
            "format",
            "max",
            "min",
            "readonly",
            "scrollable",
            ("use_seconds", "useSeconds"),
            ("bg_color", "bgColor"),
            ("hide_header", "hideHeader"),
            "color",
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
            ("allowed_hours", "allowedHours"),
            ("allowed_minutes", "allowedMinutes"),
            ("allowed_seconds", "allowedSeconds"),
            ("model_value", "modelValue"),
        ]
        self._event_names += [
            ("update_hour", "update:hour"),
            ("update_minute", "update:minute"),
            ("update_period", "update:period"),
            ("update_second", "update:second"),
            ("update_modelValue", "update:modelValue"),
        ]


class VTimePickerClock(HtmlElement):
    """
    Vuetify's VTimePickerClock component. See more info and examples |VTimePickerClock_vuetify_link|.

    .. |VTimePickerClock_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-time-picker-clock" target="_blank">here</a>


    :param ampm: See description |VTimePickerClock_vuetify_link|.
    :type boolean:
    :param color: See description |VTimePickerClock_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param displayed_value: See description |VTimePickerClock_vuetify_link|.
    :type any:
    :param double: See description |VTimePickerClock_vuetify_link|.
    :type boolean:
    :param format: See description |VTimePickerClock_vuetify_link|.
    :type Function:
    :param max: See description |VTimePickerClock_vuetify_link|.
    :type number:
    :param min: See description |VTimePickerClock_vuetify_link|.
    :type number:
    :param scrollable: See description |VTimePickerClock_vuetify_link|.
    :type boolean:
    :param readonly: See description |VTimePickerClock_vuetify_link|.
    :type boolean:
    :param rotate: See description |VTimePickerClock_vuetify_link|.
    :type number:
    :param step: See description |VTimePickerClock_vuetify_link|.
    :type number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type number:
    :param allowed_values: See description |VTimePickerClock_vuetify_link|.
    :type (value: number) => boolean:

    Events

    :param change: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerClock.json))
    :param input: The updated bound model.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimePickerClock", children, **kwargs)
        self._attr_names += [
            "ampm",
            "color",
            "disabled",
            ("displayed_value", "displayedValue"),
            "double",
            "format",
            "max",
            "min",
            "scrollable",
            "readonly",
            "rotate",
            "step",
            ("model_value", "modelValue"),
            ("allowed_values", "allowedValues"),
        ]
        self._event_names += [
            "change",
            "input",
        ]


class VTimePickerControls(HtmlElement):
    """
    Vuetify's VTimePickerControls component. See more info and examples |VTimePickerControls_vuetify_link|.

    .. |VTimePickerControls_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-time-picker-controls" target="_blank">here</a>


    :param ampm: See description |VTimePickerControls_vuetify_link|.
    :type boolean:
    :param ampm_readonly: See description |VTimePickerControls_vuetify_link|.
    :type boolean:
    :param color: See description |VTimePickerControls_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param hour: See description |VTimePickerControls_vuetify_link|.
    :type number:
    :param minute: See description |VTimePickerControls_vuetify_link|.
    :type number:
    :param second: See description |VTimePickerControls_vuetify_link|.
    :type number:
    :param period: See description |VTimePickerControls_vuetify_link|.
    :type string:
    :param readonly: See description |VTimePickerControls_vuetify_link|.
    :type boolean:
    :param use_seconds: See description |VTimePickerControls_vuetify_link|.
    :type boolean:
    :param selecting: See description |VTimePickerControls_vuetify_link|.
    :type number:
    :param value: See description |VTimePickerControls_vuetify_link|.
    :type number:

    Events

    :param update_period: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
    :param update_selecting: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTimePickerControls.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimePickerControls", children, **kwargs)
        self._attr_names += [
            "ampm",
            ("ampm_readonly", "ampmReadonly"),
            "color",
            "disabled",
            "hour",
            "minute",
            "second",
            "period",
            "readonly",
            ("use_seconds", "useSeconds"),
            "selecting",
            "value",
        ]
        self._event_names += [
            ("update_period", "update:period"),
            ("update_selecting", "update:selecting"),
        ]


class VTimeline(HtmlElement):
    """
    Vuetify's VTimeline component. See more info and examples |VTimeline_vuetify_link|.

    .. |VTimeline_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-timeline" target="_blank">here</a>


    :param justify: Places timeline line at the center or automatically on the left or right side.
    :type string:
    :param line_thickness: Thickness of the timeline line.
    :type string | number:
    :param line_color: Color of the timeline line.
    :type string:
    :param dot_color: Color of the item dot.
    :type string:
    :param fill_dot: Remove outer border of item dot, making the color fill the entire dot.
    :type boolean:
    :param hide_opposite: Hide opposite content if it exists.
    :type boolean:
    :param icon_color: Color of the icon.
    :type string:
    :param line_inset: Specifies the distance between the line and the dot of timeline items.
    :type string | number:
    :param size: Size of the item dot
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'compact' | 'comfortable':
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param align: Places the timeline dot at the top or center of the timeline item.
    :type 'center' | 'start':
    :param direction: Display timeline in a **vertical** or **horizontal** direction.
    :type 'vertical' | 'horizontal':
    :param side: Display all timeline items on one side of the timeline, either **before** or **after**.
    :type 'start' | 'end':
    :param truncate_line: Truncate timeline directly at the **start** or **end** of the line, or on **both** ends.
    :type 'start' | 'end' | 'both':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimeline", children, **kwargs)
        self._attr_names += [
            "justify",
            ("line_thickness", "lineThickness"),
            ("line_color", "lineColor"),
            ("dot_color", "dotColor"),
            ("fill_dot", "fillDot"),
            ("hide_opposite", "hideOpposite"),
            ("icon_color", "iconColor"),
            ("line_inset", "lineInset"),
            "size",
            "tag",
            "density",
            "theme",
            "align",
            "direction",
            "side",
            ("truncate_line", "truncateLine"),
        ]
        self._event_names += []


class VTimelineItem(HtmlElement):
    """
    Vuetify's VTimelineItem component. See more info and examples |VTimelineItem_vuetify_link|.

    .. |VTimelineItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-timeline-item" target="_blank">here</a>


    :param icon: See description |VTimelineItem_vuetify_link|.
    :type any:
    :param dot_color: Color of the item dot.
    :type string:
    :param fill_dot: Remove outer border of item dot, making the color fill the entire dot.
    :type boolean:
    :param hide_dot: Hide the timeline item dot.
    :type boolean:
    :param hide_opposite: Hide opposite content if it exists.
    :type boolean:
    :param icon_color: Color of the icon.
    :type string:
    :param line_inset: Specifies the distance between the line and the dot of the item.
    :type string | number:
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
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param size: Size of the item dot
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'compact':

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTimelineItem", children, **kwargs)
        self._attr_names += [
            "icon",
            ("dot_color", "dotColor"),
            ("fill_dot", "fillDot"),
            ("hide_dot", "hideDot"),
            ("hide_opposite", "hideOpposite"),
            ("icon_color", "iconColor"),
            ("line_inset", "lineInset"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "rounded",
            "tile",
            "size",
            "tag",
            "density",
        ]
        self._event_names += []


class VToolbar(HtmlElement):
    """
    Vuetify's VToolbar component. See more info and examples |VToolbar_vuetify_link|.

    .. |VToolbar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-toolbar" target="_blank">here</a>


    :param image: See description |VToolbar_vuetify_link|.
    :type string:
    :param title: Specify a title text for the component.
    :type string:
    :param flat: Removes the toolbar's box-shadow.
    :type boolean:
    :param absolute: Applies position: absolute to the component.
    :type boolean:
    :param collapse: Puts the toolbar into a collapsed state reducing its maximum width.
    :type boolean:
    :param color: See description |VToolbar_vuetify_link|.
    :type string:
    :param density: Adjusts the vertical height used by the component.
    :type 'default' | 'prominent' | 'comfortable' | 'compact':
    :param extended: Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop, and any of the other props that affect the height of the toolbar, e.g. **prominent**, **dense**, etc., **WITH THE EXCEPTION** of **height**.
    :type boolean:
    :param extension_height: Specify an explicit height for the `extension` slot.
    :type string | number:
    :param floating: Applies **display: inline-flex** to the component.
    :type boolean:
    :param height: Designates a specific height for the toolbar. Overrides the heights imposed by other props, e.g. **prominent**, **dense**, **extended**, etc.
    :type string | number:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
    :type string | number | boolean:
    :param elevation: See description |VToolbar_vuetify_link|.
    :type string | number:
    :param rounded: See description |VToolbar_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VToolbar", children, **kwargs)
        self._attr_names += [
            "image",
            "title",
            "flat",
            "absolute",
            "collapse",
            "color",
            "density",
            "extended",
            ("extension_height", "extensionHeight"),
            "floating",
            "height",
            "border",
            "elevation",
            "rounded",
            "tile",
            "tag",
            "theme",
        ]
        self._event_names += []


class VToolbarItems(HtmlElement):
    """
    Vuetify's VToolbarItems component. See more info and examples |VToolbarItems_vuetify_link|.

    .. |VToolbarItems_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-toolbar-items" target="_blank">here</a>


    :param color: See description |VToolbarItems_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'elevated' | 'tonal' | 'outlined' | 'text' | 'plain':

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


      :param activator: Explicitly sets the overlay's activator.
      :type Element | 'parent' | (string & {}) | ComponentPublicInstance:
      :param id: HTML id attribute of the tooltip overlay. If not set, a globally unique id will be used.
      :type string:
      :param text: Specify content text for the component.
      :type string:
      :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
      :type boolean:
      :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
      :type boolean:
      :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
      :type any:
      :param content_props: Apply custom properties to the content.
      :type any:
      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param opacity: Sets the overlay opacity.
      :type string | number:
      :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
      :type boolean:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type boolean:
      :param scrim: Accepts true/false to enable background, and string to define color.
      :type string | boolean:
      :param z_index: The z-index used for the component.
      :type string | number:
      :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
      :type | Element
    | 'parent'
    | 'cursor'
    | (string & {})
    | ComponentPublicInstance
    | [number, number]:
      :param activator_props: Apply custom properties to the activator.
      :type unknown:
      :param open_on_click: Designates whether the tooltip should open on activator click.
      :type boolean:
      :param open_on_hover: Designates whether the tooltip should open on activator hover.
      :type boolean:
      :param open_on_focus: Activate the component when the activator is focused.
      :type boolean:
      :param close_on_content_click: Closes component when you click on its content.
      :type boolean:
      :param close_delay: Delay (in ms) after which menu closes (when open-on-hover prop is set to true).
      :type string | number:
      :param open_delay: Delay (in ms) after which tooltip opens (when `open-on-hover` prop is set to **true**).
      :type string | number:
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
      :param location_strategy: A function used to specifies how the component should position relative to its activator.
      :type 'static' | 'connected' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
      :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a>:
      :param origin: See description |VTooltip_vuetify_link|.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/anchor.ts#L8-L14" target="_blank">Anchor</a> | 'auto' | 'overlap':
      :param offset: A single value that offsets content away from the target based upon what side it is on.
      :type string | number | number[]:
      :param scroll_strategy: Strategy used when the component is activate and user scrolls.
      :type 'none' | 'close' | 'block' | 'reposition' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
      :param theme: Specify a theme for this component and all of its children.
      :type string:
      :param transition: See description |VTooltip_vuetify_link|.
      :type string | boolean | (TransitionProps & { component: Component }):
      :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
      :type string | boolean | Element:

      Events

      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTooltip", children, **kwargs)
        self._attr_names += [
            "activator",
            "id",
            "text",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            "opacity",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
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
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "eager",
            ("location_strategy", "locationStrategy"),
            "location",
            "origin",
            "offset",
            ("scroll_strategy", "scrollStrategy"),
            "theme",
            "transition",
            "attach",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTreeview(HtmlElement):
    """
        Vuetify's VTreeview component. See more info and examples |VTreeview_vuetify_link|.

        .. |VTreeview_vuetify_link| raw:: html

            <a href="https://vuetifyjs.com/api/v-treeview" target="_blank">here</a>


        :param open_all: When `true` will cause all branch nodes to be opened when component is mounted.
        :type boolean:
        :param search: The search model for filtering results.
        :type string:
        :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
        :type 'some' | 'every' | 'union' | 'intersection':
        :param no_filter: Disables all item filtering.
        :type boolean:
        :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/filter.ts#L19-L19" target="_blank">FilterFunction</a>:
        :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
        :type unknown:
        :param filter_keys: Array of specific keys to filter on the item.
        :type string | string[]:
        :param loading_icon: Icon used when node is in a loading state.
        :type string:
        :param selectable: Will render a checkbox next to each node allowing them to be selected.
        :type boolean:
        :param load_children: A function used when dynamically loading children. If this prop is set, then the supplied function will be run if expanding an item that has a `item-children` property that is an empty array. Supports returning a Promise.
        :type (item: unknown) => Promise<void>:
        :param items: An array of items used to build the treeview.
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
      | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/selectStrategies.ts#L26-L30" target="_blank">SelectStrategy</a>
      | ((mandatory: boolean) => <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/selectStrategies.ts#L26-L30" target="_blank">SelectStrategy</a>):
        :param base_color: Sets the color of component when not focused.
        :type string:
        :param active_color: The applied color when the component is in an active state.
        :type string:
        :param active_class: The class applied to the component when it is in an active state.
        :type string:
        :param bg_color: See description |VTreeview_vuetify_link|.
        :type string:
        :param disabled: Disables selection for all nodes.
        :type boolean:
        :param expand_icon: Icon used to indicate that a node can be expanded.
        :type string:
        :param collapse_icon: See description |VTreeview_vuetify_link|.
        :type string:
        :param lines: See description |VTreeview_vuetify_link|.
        :type false | 'one' | 'two' | 'three':
        :param slim: Reduces horizontal spacing for badges, icons, tooltips, and avatars within slim list items to create a more compact visual representation.
        :type boolean:
        :param activatable: Allows user to mark a node as active by clicking on it.
        :type boolean:
        :param opened: An array containing the values of currently opened groups. Can be two-way bound with `v-model:opened`.
        :type any:
        :param activated: Array of ids of activated nodes.
        :type any:
        :param selected: An array containing the values of currently selected items. Can be two-way bound with `v-model:selected`.
        :type any:
        :param mandatory: Forces at least one item to always be selected (if available).
        :type boolean:
        :param active_strategy: Affects how items with children behave when activated.
    - **leaf:** Only leaf nodes (items without children) can be activated.
    - **independent:** All nodes can be activated whether they have children or not.
    - **classic:** Activating a parent node will cause all children to be activated.
        :type | 'single-leaf'
      | 'leaf'
      | 'independent'
      | 'single-independent'
      | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/activeStrategies.ts#L27-L31" target="_blank">ActiveStrategy</a>
      | ((mandatory: boolean) => <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/activeStrategies.ts#L27-L31" target="_blank">ActiveStrategy</a>):
        :param open_strategy: Affects how items with children behave when expanded.
    - **multiple:** Any number of groups can be open at once.
    - **single:** Only one group at each level can be open, opening a group will cause others to close.
    - **list:** Multiple, but all other groups will close when an item is selected.
        :type 'single' | 'multiple' | 'list' | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/nested/openStrategies.ts#L20-L23" target="_blank">OpenStrategy</a>:
        :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
        :param elevation: See description |VTreeview_vuetify_link|.
        :type string | number:
        :param item_type: Designates the key on the supplied items that is used for determining the nodes type.
        :type string:
        :param item_title: Property on supplied `items` that contains its title.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L73-L77" target="_blank">SelectItemKey</a>:
        :param item_value: Property on supplied `items` that contains its value.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L73-L77" target="_blank">SelectItemKey</a>:
        :param item_children: Property on supplied `items` that contains its children.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L73-L77" target="_blank">SelectItemKey</a>:
        :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
        :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/util/helpers.ts#L73-L77" target="_blank">SelectItemKey</a>:
        :param return_object: When `true` will make `v-model`, `active.sync` and `open.sync` return the complete object instead of just the key.
        :type boolean:
        :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
        :type (a: any, b: any) => boolean:
        :param rounded: Provides an alternative active style for `v-treeview` node. Only visible when `activatable` is `true` and should not be used in conjunction with the `shaped` prop.
        :type string | number | boolean:
        :param tile: Removes any applied **border-radius** from the component.
        :type boolean:
        :param tag: Specify a custom tag used on the root element.
        :type string:
        :param theme: Specify a theme for this component and all of its children.
        :type string:
        :param color: See description |VTreeview_vuetify_link|.
        :type string:
        :param variant: Applies a distinct style to the component.
        :type 'flat' | 'elevated' | 'tonal' | 'outlined' | 'text' | 'plain':

        Events

        :param click_open: Emits the item when it is clicked to open.
        :param click_select: Emits the item when it is clicked to select.
        :param update_opened: Emits the array of open items when this value changes.
        :param update_activated: Emits the array of active items when this value changes.
        :param update_selected: Emits the array of selected items when this value changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTreeview", children, **kwargs)
        self._attr_names += [
            ("open_all", "openAll"),
            "search",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            ("loading_icon", "loadingIcon"),
            "selectable",
            ("load_children", "loadChildren"),
            "items",
            ("select_strategy", "selectStrategy"),
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
            "opened",
            "activated",
            "selected",
            "mandatory",
            ("active_strategy", "activeStrategy"),
            ("open_strategy", "openStrategy"),
            "border",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            ("item_type", "itemType"),
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            ("value_comparator", "valueComparator"),
            "rounded",
            "tile",
            "tag",
            "theme",
            "color",
            "variant",
        ]
        self._event_names += [
            ("click_open", "click:open"),
            ("click_select", "click:select"),
            ("update_opened", "update:opened"),
            ("update_activated", "update:activated"),
            ("update_selected", "update:selected"),
        ]


class VTreeviewGroup(HtmlElement):
    """
    Vuetify's VTreeviewGroup component. See more info and examples |VTreeviewGroup_vuetify_link|.

    .. |VTreeviewGroup_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-treeview-group" target="_blank">here</a>


    :param active_color: The applied color when the component is in an active state.
    :type string:
    :param base_color: Sets the color of component when not focused.
    :type string:
    :param color: See description |VTreeviewGroup_vuetify_link|.
    :type string:
    :param collapse_icon: Icon to display when the list item is expanded.
    :type any:
    :param expand_icon: Icon to display when the list item is collapsed.
    :type any:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :type any:
    :param append_icon: See description |VTreeviewGroup_vuetify_link|.
    :type any:
    :param fluid: See description |VTreeviewGroup_vuetify_link|.
    :type boolean:
    :param title: Specify a title text for the component.
    :type string:
    :param value: Expands / Collapse the list-group.
    :type any:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTreeviewGroup", children, **kwargs)
        self._attr_names += [
            ("active_color", "activeColor"),
            ("base_color", "baseColor"),
            "color",
            ("collapse_icon", "collapseIcon"),
            ("expand_icon", "expandIcon"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "fluid",
            "title",
            "value",
            "tag",
        ]
        self._event_names += []


class VTreeviewItem(HtmlElement):
    """
    Vuetify's VTreeviewItem component. See more info and examples |VTreeviewItem_vuetify_link|.

    .. |VTreeviewItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-treeview-item" target="_blank">here</a>


    :param title: See description |VTreeviewItem_vuetify_link|.
    :type string | number:
    :param subtitle: Specify a subtitle text for the component.
    :type string | number:
    :param loading: See description |VTreeviewItem_vuetify_link|.
    :type boolean:
    :param toggle_icon: See description |VTreeviewItem_vuetify_link|.
    :type any:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :type boolean:
    :param active_class: See description |VTreeviewItem_vuetify_link|.
    :type string:
    :param active_color: The applied color when the component is in an active state.
    :type string:
    :param append_avatar: See description |VTreeviewItem_vuetify_link|.
    :type string:
    :param append_icon: See description |VTreeviewItem_vuetify_link|.
    :type any:
    :param base_color: Sets the color of component when not focused.
    :type string:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param link: Designates that the component is a link. This is automatic when using the href or to prop.
    :type boolean:
    :param nav: See description |VTreeviewItem_vuetify_link|.
    :type boolean:
    :param prepend_avatar: See description |VTreeviewItem_vuetify_link|.
    :type string:
    :param prepend_icon: See description |VTreeviewItem_vuetify_link|.
    :type any:
    :param ripple: See description |VTreeviewItem_vuetify_link|.
    :type boolean | { class: string }:
    :param value: The value used for selection.
    :type any:
    :param slim: See description |VTreeviewItem_vuetify_link|.
    :type boolean:
    :param border: Designates the **border-radius** applied to the component. This can be **xs**, **sm**, **md**, **lg**, **xl**.
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
    :param elevation: See description |VTreeviewItem_vuetify_link|.
    :type string | number:
    :param rounded: See description |VTreeviewItem_vuetify_link|.
    :type string | number | boolean:
    :param tile: Removes any applied **border-radius** from the component.
    :type boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |VTreeviewItem_vuetify_link|.
    :type boolean:
    :param exact: See description |VTreeviewItem_vuetify_link|.
    :type boolean:
    :param to: See description |VTreeviewItem_vuetify_link|.
    :type RouteLocationRaw:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:
    :param color: See description |VTreeviewItem_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component.
    :type 'flat' | 'elevated' | 'tonal' | 'outlined' | 'text' | 'plain':
    :param lines: See description |VTreeviewItem_vuetify_link|.
    :type false | 'one' | 'two' | 'three':

    Events

    :param clickOnce: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree//packages/api-generator/src/locale/en/VTreeviewItem.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VTreeviewItem", children, **kwargs)
        self._attr_names += [
            "title",
            "subtitle",
            "loading",
            ("toggle_icon", "toggleIcon"),
            "active",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
            ("append_avatar", "appendAvatar"),
            ("append_icon", "appendIcon"),
            ("base_color", "baseColor"),
            "disabled",
            "link",
            "nav",
            ("prepend_avatar", "prependAvatar"),
            ("prepend_icon", "prependIcon"),
            "ripple",
            "value",
            "slim",
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
            "href",
            "replace",
            "exact",
            "to",
            "tag",
            "theme",
            "color",
            "variant",
            "lines",
        ]
        self._event_names += [
            "click",
            "clickOnce",
        ]


class VValidation(HtmlElement):
    """
      Vuetify's VValidation component. See more info and examples |VValidation_vuetify_link|.

      .. |VValidation_vuetify_link| raw:: html

          <a href="https://vuetifyjs.com/api/v-validation" target="_blank">here</a>


      :param disabled: Removes the ability to click or target the component.
      :type boolean:
      :param error: Puts the input in a manual error state.
      :type boolean:
      :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
      :type string | string[]:
      :param max_errors: Control the maximum number of shown errors from validation.
      :type string | number:
      :param name: Sets the component's name attribute.
      :type string:
      :param label: See description |VValidation_vuetify_link|.
      :type string:
      :param readonly: Puts input in readonly state.
      :type boolean:
      :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
      :type <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
      :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
      :type unknown:
      :param validate_on: Change what type of event triggers validation to run.
      :type | 'blur'
    | 'input'
    | 'submit'
    | 'blur lazy'
    | 'input lazy'
    | 'submit lazy'
    | 'lazy blur'
    | 'lazy input'
    | 'lazy submit'
    | 'lazy':
      :param validation_value: The value used when applying validation rules.
      :type any:
      :param focused: Forces a focused state styling on the component.
      :type boolean:

      Events

      :param update_focused: Event that is emitted when the component's focus state changes.
      :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VValidation", children, **kwargs)
        self._attr_names += [
            "disabled",
            "error",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "label",
            "readonly",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            "focused",
        ]
        self._event_names += [
            ("update_focused", "update:focused"),
            ("update_modelValue", "update:modelValue"),
        ]


class VVirtualScroll(HtmlElement):
    """
    Vuetify's VVirtualScroll component. See more info and examples |VVirtualScroll_vuetify_link|.

    .. |VVirtualScroll_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-virtual-scroll" target="_blank">here</a>


    :param items: The array of items to display.
    :type unknown[]:
    :param renderless: Disables default component rendering functionality.
    :type boolean:
    :param item_height: Height in pixels of each item to display.
    :type string | number:
    :param height: Height of the component as a css value/
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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VVirtualScroll", children, **kwargs)
        self._attr_names += [
            "items",
            "renderless",
            ("item_height", "itemHeight"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
        ]
        self._event_names += []


class VWindow(HtmlElement):
    """
    Vuetify's VWindow component. See more info and examples |VWindow_vuetify_link|.

    .. |VWindow_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-window" target="_blank">here</a>


    :param continuous: If `true`, window will "wrap around" from the last item to the first, and from the first item to the last.
    :type boolean:
    :param next_icon: Icon used for the "next" button if `show-arrows` is `true`.
    :type any:
    :param prev_icon: Icon used for the "prev" button if `show-arrows` is `true`.
    :type any:
    :param reverse: Reverse the normal transition direction.
    :type boolean:
    :param show_arrows: Display the "next" and "prev" buttons.
    :type string | boolean:
    :param touch: Provide a custom **left** and **right** function when swiped left or right.
    :type boolean | <a href="https://github.com/vuetifyjs/vuetify/blob/master/packages/vuetify/src/directives/touch/index.ts#L9-L17" target="_blank">TouchHandlers</a>:
    :param direction: The transition direction when changing windows.
    :type 'horizontal' | 'vertical':
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :type unknown:
    :param disabled: Removes the ability to click or target the component.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | 'force':
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VWindow", children, **kwargs)
        self._attr_names += [
            "continuous",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            "reverse",
            ("show_arrows", "showArrows"),
            "touch",
            "direction",
            ("model_value", "modelValue"),
            "disabled",
            ("selected_class", "selectedClass"),
            "mandatory",
            "tag",
            "theme",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VWindowItem(HtmlElement):
    """
    Vuetify's VWindowItem component. See more info and examples |VWindowItem_vuetify_link|.

    .. |VWindowItem_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-window-item" target="_blank">here</a>


    :param reverse_transition: Sets the reverse transition.
    :type string | boolean:
    :param transition: See description |VWindowItem_vuetify_link|.
    :type string | boolean:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.
    :type boolean:
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :type string:
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:

    Events

    :param group_selected: Event that is emitted when an item is selected within a group.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("VWindowItem", children, **kwargs)
        self._attr_names += [
            ("reverse_transition", "reverseTransition"),
            "transition",
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "eager",
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]
