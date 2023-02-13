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
    "chip",
    "clear",
    "default",
    "details",
    "divider",
    "extension",
    "header",
    "image",
    "input",
    "item",
    "item-label",
    "label",
    "loader",
    "next",
    "no-data",
    "prepend",
    "prepend-inner",
    "prepend-item",
    "prev",
    "selection",
    "subheader",
    "subtitle",
    "text",
    "title",
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
    "VDataTable",
    "VDataTableRow",
    "VDataTableRows",
    "VDataTableServer",
    "VDataTableVirtual",
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


class VApp(HtmlElement):
    """
    Vuetify's v-app component. See more info and examples |v-app_vuetify_link|.

    .. |v-app_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-app" target="_blank">here</a>


    :param full_height: Sets the component height to 100%
    :type boolean:
    :param overlaps: See description |v-app_vuetify_link|.
    :type string[]:
    :param theme: Specify a theme for this component and all of its children
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-app", children, **kwargs)
        self._attr_names += [
            ("full_height", "fullHeight"),
            "overlaps",
            "theme",
        ]
        self._event_names += []


class VAppBar(HtmlElement):
    """
    Vuetify's v-app-bar component. See more info and examples |v-app-bar_vuetify_link|.

    .. |v-app-bar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-app-bar" target="_blank">here</a>


    :param image: The `src` used for `v-img`. For additional customization options, use the **image** slot.
    :type string:
    :param title: See description |v-app-bar_vuetify_link|.
    :type string:
    :param flat: Removes the component's **box-shadow**.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param location: See description |v-app-bar_vuetify_link|.
    :type "top" | "bottom":
    :param absolute: Applies position: absolute to the component.
    :type boolean:
    :param collapse: Morphs the component into a collapsed state, reducing its maximum width.
    :type boolean:
    :param color: See description |v-app-bar_vuetify_link|.
    :type string:
    :param density: See description |v-app-bar_vuetify_link|.
    :type "default" | "prominent" | "comfortable" | "compact":
    :param extended: Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop, and any of the other props that affect the height of the toolbar, e.g. **prominent**, **dense**, etc., **WITH THE EXCEPTION** of **height**.
    :type boolean:
    :param extension_height: Designate an explicit height for the `extension` slot.
    :type string | number:
    :param floating: Applies **display: inline-flex** to the component.
    :type boolean:
    :param height: See description |v-app-bar_vuetify_link|.
    :type string | number:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param elevation: See description |v-app-bar_vuetify_link|.
    :type string | number:
    :param rounded: See description |v-app-bar_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param name: See description |v-app-bar_vuetify_link|.
    :type string:
    :param order: See description |v-app-bar_vuetify_link|.
    :type string | number:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-app-bar", children, **kwargs)
        self._attr_names += [
            "image",
            "title",
            "flat",
            ("model_value", "modelValue"),
            "location",
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
            "tag",
            "theme",
            "name",
            "order",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VAppBarNavIcon(HtmlElement):
    """
    Vuetify's v-app-bar-nav-icon component. See more info and examples |v-app-bar-nav-icon_vuetify_link|.

    .. |v-app-bar-nav-icon_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-app-bar-nav-icon" target="_blank">here</a>


    :param icon: See description |v-app-bar-nav-icon_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-app-bar-nav-icon", children, **kwargs)
        self._attr_names += [
            "icon",
        ]
        self._event_names += []


class VAppBarTitle(HtmlElement):
    """
    Vuetify's v-app-bar-title component. See more info and examples |v-app-bar-title_vuetify_link|.

    .. |v-app-bar-title_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-app-bar-title" target="_blank">here</a>



    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-app-bar-title", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VAlert(HtmlElement):
    """
    Vuetify's v-alert component. See more info and examples |v-alert_vuetify_link|.

    .. |v-alert_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-alert" target="_blank">here</a>


    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param type: Specify a **success**, **info**, **warning** or **error** alert. Uses the contextual color and has a pre-defined icon.
    :type "success" | "info" | "warning" | "error":
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
    :param elevation: See description |v-alert_vuetify_link|.
    :type string | number:
    :param location: See description |v-alert_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param position: Specifies the type of positioning method used for an element. Available options are: **static**, **relative**, **fixed**, **absolute**, and **sticky**.
    :type "static" | "relative" | "fixed" | "absolute" | "sticky":
    :param rounded: See description |v-alert_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-alert_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":
    :param text: Specify subtitle/body text for the alert.
    :type string:
    :param border: Puts a border on the alert. Accepts **top** \| **end** \| **bottom** \| **start**.
    :type boolean | "top" | "end" | "bottom" | "start":
    :param border_color: Specifies the color of the border. Accepts any color value.
    :type string:
    :param closable: Adds a close icon that can hide the alert.
    :type boolean:
    :param close_icon: Change the default icon used for **closable** alerts.
    :type string | (new () => any) | FunctionalComponent:
    :param close_label: See description |v-alert_vuetify_link|.
    :type string:
    :param icon: Designates a specific icon.
    :type false | string | (new () => any) | FunctionalComponent:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param prominent: Displays a larger vertically centered icon to draw more attention.
    :type boolean:
    :param title: Specify title text for the alert.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-alert", children, **kwargs)
        self._attr_names += [
            "density",
            "type",
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
            "text",
            "border",
            ("border_color", "borderColor"),
            "closable",
            ("close_icon", "closeIcon"),
            ("close_label", "closeLabel"),
            "icon",
            ("model_value", "modelValue"),
            "prominent",
            "title",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VAlertTitle(HtmlElement):
    """
    Vuetify's v-alert-title component. See more info and examples |v-alert-title_vuetify_link|.

    .. |v-alert-title_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-alert-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-alert-title", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VAutocomplete(HtmlElement):
    """
    Vuetify's v-autocomplete component. See more info and examples |v-autocomplete_vuetify_link|.

    .. |v-autocomplete_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-autocomplete" target="_blank">here</a>


    :param label: See description |v-autocomplete_vuetify_link|.
    :type string:
    :param type: Sets input type
    :type string:
    :param search: See description |v-autocomplete_vuetify_link|.
    :type string:
    :param filter_mode: See description |v-autocomplete_vuetify_link|.
    :type "every" | "some" | "union" | "intersection":
    :param no_filter: Do not apply filtering when searching. Useful when data is being filtered server side
    :type boolean:
    :param custom_filter: See description |v-autocomplete_vuetify_link|.
    :type (value: string, query: string, item: any) => number | boolean | [number, number] | [number, number][]:
    :param custom_key_filter: See description |v-autocomplete_vuetify_link|.
    :type {  }:
    :param reverse: See description |v-autocomplete_vuetify_link|.
    :type boolean:
    :param filter_keys: See description |v-autocomplete_vuetify_link|.
    :type string | string[]:
    :param chips: Changes display of selections to chips
    :type boolean:
    :param closable_chips: See description |v-autocomplete_vuetify_link|.
    :type boolean:
    :param eager: Will force the components content to render on mounted. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :type boolean:
    :param hide_selected: Do not display in the select menu items that are already selected
    :type boolean:
    :param menu: See description |v-autocomplete_vuetify_link|.
    :type boolean:
    :param menu_icon: See description |v-autocomplete_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param menu_props: See description |v-autocomplete_vuetify_link|.
    :type unknown:
    :param id: See description |v-autocomplete_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the input
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param transition: See description |v-autocomplete_vuetify_link|.
    :type string | boolean:
    :param name: See description |v-autocomplete_vuetify_link|.
    :type string:
    :param multiple: Changes select to multiple. Accepts array for value
    :type boolean:
    :param no_data_text: Text shown when no items are provided to the component
    :type string:
    :param open_on_clear: When using the **clearable** prop, once cleared, the select menu will either open or stay open, depending on the current state
    :type boolean:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param items: Can be an array of objects or array of strings. When using objects, will look for a title, value and disabled keys. This can be changed using the **item-title**, **item-value** and **item-disabled** props.  Objects that have a **header** or **divider** property are considered special cases and generate a list header or divider; these items are not selectable.
    :type unknown[]:
    :param item_title: See description |v-autocomplete_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_value: See description |v-autocomplete_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_children: See description |v-autocomplete_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_props: See description |v-autocomplete_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**
    :type boolean:
    :param autofocus: Enables autofocus
    :type boolean:
    :param hint: See description |v-autocomplete_vuetify_link|.
    :type string:
    :param persistent_hint: See description |v-autocomplete_vuetify_link|.
    :type boolean:
    :param prefix: Displays prefix text
    :type string:
    :param placeholder: Sets the input’s placeholder text
    :type string:
    :param persistent_placeholder: Forces placeholder to always be visible
    :type boolean:
    :param persistent_counter: See description |v-autocomplete_vuetify_link|.
    :type boolean:
    :param suffix: Displays suffix text
    :type string:
    :param append_icon: Appends an icon to the outside the component's input, uses same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-autocomplete_vuetify_link|.
    :type string | string[]:
    :param direction: See description |v-autocomplete_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param error: See description |v-autocomplete_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-autocomplete_vuetify_link|.
    :type string | number:
    :param readonly: Puts input in readonly state
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param validate_on: See description |v-autocomplete_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param bg_color: See description |v-autocomplete_vuetify_link|.
    :type string:
    :param clearable: Allows for the component to be cleared
    :type boolean:
    :param clear_icon: See description |v-autocomplete_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param color: See description |v-autocomplete_vuetify_link|.
    :type string:
    :param persistent_clear: See description |v-autocomplete_vuetify_link|.
    :type boolean:
    :param prepend_inner_icon: See description |v-autocomplete_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param single_line: Label does not move on focus/dirty
    :type boolean:
    :param variant: Applies a distinct style to the component
    :type "underlined" | "outlined" | "filled" | "solo" | "plain":
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
    :type string | boolean:
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :type string | number | true:
    :param counter_value: See description |v-autocomplete_vuetify_link|.
    :type (value: any) => number:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-autocomplete.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-autocomplete.json))
    :param click_clear: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-autocomplete.json))
    :param click_appendInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-autocomplete.json))
    :param click_prependInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-autocomplete.json))
    :param update_search: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-autocomplete.json))
    :param update_menu: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-autocomplete.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-autocomplete", children, **kwargs)
        self._attr_names += [
            "label",
            "type",
            "search",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            "reverse",
            ("filter_keys", "filterKeys"),
            "chips",
            ("closable_chips", "closableChips"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "id",
            "disabled",
            ("model_value", "modelValue"),
            "theme",
            "transition",
            "name",
            "multiple",
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("value_comparator", "valueComparator"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            "autofocus",
            "hint",
            ("persistent_hint", "persistentHint"),
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "direction",
            "density",
            "error",
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
            "active",
            "color",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "loading",
            "counter",
            ("counter_value", "counterValue"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_search", "update:search"),
            ("update_menu", "update:menu"),
        ]


class VAvatar(HtmlElement):
    """
    Vuetify's v-avatar component. See more info and examples |v-avatar_vuetify_link|.

    .. |v-avatar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-avatar" target="_blank">here</a>


    :param start: See description |v-avatar_vuetify_link|.
    :type boolean:
    :param end: See description |v-avatar_vuetify_link|.
    :type boolean:
    :param icon: See description |v-avatar_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param image: See description |v-avatar_vuetify_link|.
    :type string:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param rounded: See description |v-avatar_vuetify_link|.
    :type string | number | boolean:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-avatar_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "elevated" | "flat" | "tonal" | "outlined" | "text" | "plain":

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-avatar", children, **kwargs)
        self._attr_names += [
            "start",
            "end",
            "icon",
            "image",
            "density",
            "rounded",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
        ]
        self._event_names += []


class VBadge(HtmlElement):
    """
    Vuetify's v-badge component. See more info and examples |v-badge_vuetify_link|.

    .. |v-badge_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-badge" target="_blank">here</a>


    :param location: Changes the location of the badge. Possible values are **top**, **bottom**, **start**, **end**, **top start**, **top end**, **bottom start**, **bottom end**.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param rounded: See description |v-badge_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param transition: See description |v-badge_vuetify_link|.
    :type string:
    :param bordered: Applies a **2px** by default and **1.5px** border around the badge when using the **dot** property.
    :type boolean:
    :param color: See description |v-badge_vuetify_link|.
    :type string:
    :param content: Text content to show in the badge.
    :type string | number:
    :param dot: Reduce the size of the badge and hide its contents.
    :type boolean:
    :param floating: See description |v-badge_vuetify_link|.
    :type boolean:
    :param icon: Designates a specific icon to render in the badge.
    :type string | (new () => any) | FunctionalComponent:
    :param inline: Moves the badge to be inline with the wrapping element. Supports the usage of the **left** prop.
    :type boolean:
    :param label: The **aria-label** used for the badge
    :type string:
    :param max: Sets the maximum number allowed when using the **content** prop with a `number` like value. If the content number exceeds the maximum value, a `+` suffix is added.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param offset_x: Offset the badge on the x-axis.
    :type string | number:
    :param offset_y: Offset the badge on the y-axis.
    :type string | number:
    :param text_color: See description |v-badge_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-badge", children, **kwargs)
        self._attr_names += [
            "location",
            "rounded",
            "tag",
            "theme",
            "transition",
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
        ]
        self._event_names += []


class VBanner(HtmlElement):
    """
    Vuetify's v-banner component. See more info and examples |v-banner_vuetify_link|.

    .. |v-banner_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-banner" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
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
    :param elevation: See description |v-banner_vuetify_link|.
    :type string | number:
    :param location: See description |v-banner_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param position: Specifies the type of positioning method used for an element. Available options are: **static**, **relative**, **fixed**, **absolute**, and **sticky**.
    :type "static" | "relative" | "fixed" | "absolute" | "sticky":
    :param sticky: See description |v-banner_vuetify_link|.
    :type boolean:
    :param rounded: See description |v-banner_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param avatar: Designates a specific src image to pass to the thumbnail.
    :type string:
    :param color: See description |v-banner_vuetify_link|.
    :type string:
    :param icon: Designates a specific icon.
    :type string | (new () => any) | FunctionalComponent:
    :param stacked: See description |v-banner_vuetify_link|.
    :type boolean:
    :param text: See description |v-banner_vuetify_link|.
    :type string:
    :param lines: See description |v-banner_vuetify_link|.
    :type "one" | "two" | "three":

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-banner", children, **kwargs)
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
            "location",
            "position",
            "sticky",
            "rounded",
            "tag",
            "theme",
            "avatar",
            "color",
            "icon",
            "stacked",
            "text",
            "lines",
        ]
        self._event_names += []


class VBannerActions(HtmlElement):
    """
    Vuetify's v-banner-actions component. See more info and examples |v-banner-actions_vuetify_link|.

    .. |v-banner-actions_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-banner-actions" target="_blank">here</a>


    :param color: See description |v-banner-actions_vuetify_link|.
    :type string:
    :param density: See description |v-banner-actions_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-banner-actions", children, **kwargs)
        self._attr_names += [
            "color",
            "density",
        ]
        self._event_names += []


class VBannerText(HtmlElement):
    """
    Vuetify's v-banner-text component. See more info and examples |v-banner-text_vuetify_link|.

    .. |v-banner-text_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-banner-text" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-banner-text", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VBottomNavigation(HtmlElement):
    """
    Vuetify's v-bottom-navigation component. See more info and examples |v-bottom-navigation_vuetify_link|.

    .. |v-bottom-navigation_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-bottom-navigation" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param elevation: See description |v-bottom-navigation_vuetify_link|.
    :type string | number:
    :param rounded: See description |v-bottom-navigation_vuetify_link|.
    :type string | number | boolean:
    :param name: See description |v-bottom-navigation_vuetify_link|.
    :type string:
    :param order: See description |v-bottom-navigation_vuetify_link|.
    :type string | number:
    :param absolute: See description |v-bottom-navigation_vuetify_link|.
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the selected CSS class.
    :type string:
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | "force":
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param bg_color: See description |v-bottom-navigation_vuetify_link|.
    :type string:
    :param color: See description |v-bottom-navigation_vuetify_link|.
    :type string:
    :param grow: See description |v-bottom-navigation_vuetify_link|.
    :type boolean:
    :param mode: Changes the orientation and active state styling of the component. Available options are **horizontal** and **shift**.
    :type string:
    :param height: See description |v-bottom-navigation_vuetify_link|.
    :type string | number:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-bottom-navigation", children, **kwargs)
        self._attr_names += [
            "border",
            "density",
            "elevation",
            "rounded",
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
            ("bg_color", "bgColor"),
            "color",
            "grow",
            "mode",
            "height",
            "active",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VBreadcrumbs(HtmlElement):
    """
    Vuetify's v-breadcrumbs component. See more info and examples |v-breadcrumbs_vuetify_link|.

    .. |v-breadcrumbs_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-breadcrumbs" target="_blank">here</a>


    :param divider: Specifies the dividing character between items.
    :type string:
    :param active_class: The class applied to the component when it is in an active state
    :type string:
    :param active_color: See description |v-breadcrumbs_vuetify_link|.
    :type string:
    :param bg_color: See description |v-breadcrumbs_vuetify_link|.
    :type string:
    :param color: See description |v-breadcrumbs_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param icon: See description |v-breadcrumbs_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param items: An array of strings or objects used for automatically generating children components
    :type unknown[]:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param rounded: See description |v-breadcrumbs_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-breadcrumbs", children, **kwargs)
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
            "tag",
        ]
        self._event_names += []


class VBreadcrumbsItem(HtmlElement):
    """
    Vuetify's v-breadcrumbs-item component. See more info and examples |v-breadcrumbs-item_vuetify_link|.

    .. |v-breadcrumbs-item_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-breadcrumbs-item" target="_blank">here</a>


    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |v-breadcrumbs-item_vuetify_link|.
    :type boolean:
    :param exact: See description |v-breadcrumbs-item_vuetify_link|.
    :type boolean:
    :param to: See description |v-breadcrumbs-item_vuetify_link|.
    :type unknown:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param active_class: See description |v-breadcrumbs-item_vuetify_link|.
    :type string:
    :param active_color: See description |v-breadcrumbs-item_vuetify_link|.
    :type string:
    :param color: See description |v-breadcrumbs-item_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param title: See description |v-breadcrumbs-item_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-breadcrumbs-item", children, **kwargs)
        self._attr_names += [
            "href",
            "replace",
            "exact",
            "to",
            "tag",
            "active",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
            "color",
            "disabled",
            "title",
        ]
        self._event_names += []


class VBreadcrumbsDivider(HtmlElement):
    """
    Vuetify's v-breadcrumbs-divider component. See more info and examples |v-breadcrumbs-divider_vuetify_link|.

    .. |v-breadcrumbs-divider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-breadcrumbs-divider" target="_blank">here</a>



    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-breadcrumbs-divider", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VBtn(HtmlElement):
    """
    Vuetify's v-btn component. See more info and examples |v-btn_vuetify_link|.

    .. |v-btn_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-btn" target="_blank">here</a>


    :param symbol: See description |v-btn_vuetify_link|.
    :type any:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param flat: Removes the button box shadow.
    :type boolean:
    :param rounded: See description |v-btn_vuetify_link|.
    :type string | number | boolean:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
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
    :param elevation: See description |v-btn_vuetify_link|.
    :type string | number:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param selected_class: Configure the active CSS class applied when the item is selected.
    :type string:
    :param loading: See description |v-btn_vuetify_link|.
    :type string | boolean:
    :param location: See description |v-btn_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param position: Specifies the type of positioning method used for an element. Available options are: **static**, **relative**, **fixed**, **absolute**, and **sticky**.
    :type "static" | "relative" | "fixed" | "absolute" | "sticky":
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |v-btn_vuetify_link|.
    :type boolean:
    :param exact: See description |v-btn_vuetify_link|.
    :type boolean:
    :param to: See description |v-btn_vuetify_link|.
    :type unknown:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-btn_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param prepend_icon: See description |v-btn_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param append_icon: See description |v-btn_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param block: Expands the button to 100% of available space.
    :type boolean:
    :param stacked: Displays the button as a flex-column.
    :type boolean:
    :param ripple: See description |v-btn_vuetify_link|.
    :type boolean:
    :param icon: Designates the button as icon. Button will become _round_ and applies the **text** prop.
    :type boolean | string | (new () => any) | FunctionalComponent:

    Events

    :param group_selected: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-btn.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-btn", children, **kwargs)
        self._attr_names += [
            "symbol",
            "border",
            "flat",
            "rounded",
            "density",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "elevation",
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "loading",
            "location",
            "position",
            "href",
            "replace",
            "exact",
            "to",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
            "active",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "block",
            "stacked",
            "ripple",
            "icon",
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VBtnGroup(HtmlElement):
    """
    Vuetify's v-btn-group component. See more info and examples |v-btn-group_vuetify_link|.

    .. |v-btn-group_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-btn-group" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param elevation: See description |v-btn-group_vuetify_link|.
    :type string | number:
    :param rounded: See description |v-btn-group_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-btn-group_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":
    :param divided: See description |v-btn-group_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-btn-group", children, **kwargs)
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
    Vuetify's v-btn-toggle component. See more info and examples |v-btn-toggle_vuetify_link|.

    .. |v-btn-toggle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-btn-toggle" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the selected CSS class.
    :type string:
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | "force":

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-btn-toggle", children, **kwargs)
        self._attr_names += [
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


class VCard(HtmlElement):
    """
    Vuetify's v-card component. See more info and examples |v-card_vuetify_link|.

    .. |v-card_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card" target="_blank">here</a>


    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param flat: Removes the card's elevation.
    :type boolean:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
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
    :param elevation: See description |v-card_vuetify_link|.
    :type string | number:
    :param loading: See description |v-card_vuetify_link|.
    :type string | boolean:
    :param location: See description |v-card_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param position: Specifies the type of positioning method used for an element. Available options are: **static**, **relative**, **fixed**, **absolute**, and **sticky**.
    :type "static" | "relative" | "fixed" | "absolute" | "sticky":
    :param rounded: See description |v-card_vuetify_link|.
    :type string | number | boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |v-card_vuetify_link|.
    :type boolean:
    :param exact: See description |v-card_vuetify_link|.
    :type boolean:
    :param to: See description |v-card_vuetify_link|.
    :type unknown:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param color: See description |v-card_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":
    :param text: Generates a `v-card-text` component with the supplied value
    :type string:
    :param link: See description |v-card_vuetify_link|.
    :type boolean:
    :param append_avatar: See description |v-card_vuetify_link|.
    :type string:
    :param append_icon: See description |v-card_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param hover: See description |v-card_vuetify_link|.
    :type boolean:
    :param image: See description |v-card_vuetify_link|.
    :type string:
    :param prepend_avatar: See description |v-card_vuetify_link|.
    :type string:
    :param prepend_icon: See description |v-card_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param ripple: See description |v-card_vuetify_link|.
    :type boolean:
    :param subtitle: Generates a `v-card-subtitle` component with the supplied value
    :type string:
    :param title: Generates a `v-card-title` component with the supplied value
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card", children, **kwargs)
        self._attr_names += [
            "theme",
            "border",
            "flat",
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
            "href",
            "replace",
            "exact",
            "to",
            "tag",
            "color",
            "variant",
            "text",
            "link",
            ("append_avatar", "appendAvatar"),
            ("append_icon", "appendIcon"),
            "disabled",
            "hover",
            "image",
            ("prepend_avatar", "prependAvatar"),
            ("prepend_icon", "prependIcon"),
            "ripple",
            "subtitle",
            "title",
        ]
        self._event_names += []


class VCardActions(HtmlElement):
    """
    Vuetify's v-card-actions component. See more info and examples |v-card-actions_vuetify_link|.

    .. |v-card-actions_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-actions" target="_blank">here</a>



    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card-actions", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VCardItem(HtmlElement):
    """
    Vuetify's v-card-item component. See more info and examples |v-card-item_vuetify_link|.

    .. |v-card-item_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-item" target="_blank">here</a>


    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param append_avatar: See description |v-card-item_vuetify_link|.
    :type string:
    :param append_icon: See description |v-card-item_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_avatar: See description |v-card-item_vuetify_link|.
    :type string:
    :param prepend_icon: See description |v-card-item_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param subtitle: MISSING DESCRIPTION
    :type string:
    :param title: MISSING DESCRIPTION
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card-item", children, **kwargs)
        self._attr_names += [
            "density",
            ("append_avatar", "appendAvatar"),
            ("append_icon", "appendIcon"),
            ("prepend_avatar", "prependAvatar"),
            ("prepend_icon", "prependIcon"),
            "subtitle",
            "title",
        ]
        self._event_names += []


class VCardSubtitle(HtmlElement):
    """
    Vuetify's v-card-subtitle component. See more info and examples |v-card-subtitle_vuetify_link|.

    .. |v-card-subtitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-subtitle" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card-subtitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCardText(HtmlElement):
    """
    Vuetify's v-card-text component. See more info and examples |v-card-text_vuetify_link|.

    .. |v-card-text_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-text" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card-text", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCardTitle(HtmlElement):
    """
    Vuetify's v-card-title component. See more info and examples |v-card-title_vuetify_link|.

    .. |v-card-title_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-card-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card-title", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCarousel(HtmlElement):
    """
    Vuetify's v-carousel component. See more info and examples |v-carousel_vuetify_link|.

    .. |v-carousel_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-carousel" target="_blank">here</a>


    :param color: See description |v-carousel_vuetify_link|.
    :type string:
    :param cycle: Determines if the carousel should cycle through images.
    :type boolean:
    :param delimiter_icon: Sets icon for carousel delimiter
    :type string | (new () => any) | FunctionalComponent:
    :param height: See description |v-carousel_vuetify_link|.
    :type string | number:
    :param hide_delimiters: Hides the carousel's bottom delimiters.
    :type boolean:
    :param hide_delimiter_background: Hides the bottom delimiter background.
    :type boolean:
    :param interval: The duration between image cycles. Requires the **cycle** prop.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param progress: Displays a carousel progress bar. Requires the **cycle** prop and **interval**.
    :type string | boolean:
    :param show_arrows: Displays arrows for next/previous navigation.
    :type string | boolean:
    :param vertical_delimiters: Displays carousel delimiters vertically.
    :type boolean | "left" | "right":

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-carousel", children, **kwargs)
        self._attr_names += [
            "color",
            "cycle",
            ("delimiter_icon", "delimiterIcon"),
            "height",
            ("hide_delimiters", "hideDelimiters"),
            ("hide_delimiter_background", "hideDelimiterBackground"),
            "interval",
            ("model_value", "modelValue"),
            "progress",
            ("show_arrows", "showArrows"),
            ("vertical_delimiters", "verticalDelimiters"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VCarouselItem(HtmlElement):
    """
    Vuetify's v-carousel-item component. See more info and examples |v-carousel-item_vuetify_link|.

    .. |v-carousel-item_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-carousel-item" target="_blank">here</a>


    :param value: See description |v-carousel-item_vuetify_link|.
    :type any:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-carousel-item", children, **kwargs)
        self._attr_names += [
            "value",
        ]
        self._event_names += []


class VCheckbox(HtmlElement):
    """
    Vuetify's v-checkbox component. See more info and examples |v-checkbox_vuetify_link|.

    .. |v-checkbox_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-checkbox" target="_blank">here</a>


    :param id: See description |v-checkbox_vuetify_link|.
    :type string:
    :param append_icon: Appends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-checkbox_vuetify_link|.
    :type string | string[]:
    :param type: See description |v-checkbox_vuetify_link|.
    :type string:
    :param direction: See description |v-checkbox_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: See description |v-checkbox_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-checkbox_vuetify_link|.
    :type string | number:
    :param name: Sets the component's name attribute
    :type string:
    :param label: See description |v-checkbox_vuetify_link|.
    :type string:
    :param readonly: See description |v-checkbox_vuetify_link|.
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param validate_on: See description |v-checkbox_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-checkbox_vuetify_link|.
    :type any:
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param indeterminate: Sets an indeterminate state for the checkbox
    :type boolean:
    :param indeterminate_icon: The icon used when in an indeterminate state
    :type string | (new () => any) | FunctionalComponent:
    :param true_value: See description |v-checkbox_vuetify_link|.
    :type any:
    :param false_value: See description |v-checkbox_vuetify_link|.
    :type any:
    :param value: The input's value
    :type any:
    :param color: See description |v-checkbox_vuetify_link|.
    :type string:
    :param inline: See description |v-checkbox_vuetify_link|.
    :type boolean:
    :param false_icon: The icon used when inactive
    :type string | (new () => any) | FunctionalComponent:
    :param true_icon: The icon used when active
    :type string | (new () => any) | FunctionalComponent:
    :param ripple: See description |v-checkbox_vuetify_link|.
    :type boolean:
    :param multiple: Changes expected model to an array
    :type boolean:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:

    Events

    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-checkbox.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-checkbox.json))
    :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-checkbox.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-checkbox", children, **kwargs)
        self._attr_names += [
            "id",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "type",
            "direction",
            "density",
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
            "indeterminate",
            ("indeterminate_icon", "indeterminateIcon"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "multiple",
            ("value_comparator", "valueComparator"),
            "theme",
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
        ]


class VCheckboxBtn(HtmlElement):
    """
    Vuetify's v-checkbox-btn component. See more info and examples |v-checkbox-btn_vuetify_link|.

    .. |v-checkbox-btn_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-checkbox-btn" target="_blank">here</a>


    :param indeterminate: See description |v-checkbox-btn_vuetify_link|.
    :type boolean:
    :param indeterminate_icon: See description |v-checkbox-btn_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param type: See description |v-checkbox-btn_vuetify_link|.
    :type string:
    :param label: See description |v-checkbox-btn_vuetify_link|.
    :type string:
    :param true_value: See description |v-checkbox-btn_vuetify_link|.
    :type any:
    :param false_value: See description |v-checkbox-btn_vuetify_link|.
    :type any:
    :param value: See description |v-checkbox-btn_vuetify_link|.
    :type any:
    :param color: See description |v-checkbox-btn_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: See description |v-checkbox-btn_vuetify_link|.
    :type boolean:
    :param id: See description |v-checkbox-btn_vuetify_link|.
    :type string:
    :param inline: See description |v-checkbox-btn_vuetify_link|.
    :type boolean:
    :param false_icon: See description |v-checkbox-btn_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param true_icon: See description |v-checkbox-btn_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param ripple: See description |v-checkbox-btn_vuetify_link|.
    :type boolean:
    :param multiple: See description |v-checkbox-btn_vuetify_link|.
    :type boolean:
    :param name: See description |v-checkbox-btn_vuetify_link|.
    :type string:
    :param readonly: See description |v-checkbox-btn_vuetify_link|.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_indeterminate: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-checkbox-btn.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-checkbox-btn", children, **kwargs)
        self._attr_names += [
            "indeterminate",
            ("indeterminate_icon", "indeterminateIcon"),
            "type",
            "label",
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            "disabled",
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
            "theme",
            "density",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_indeterminate", "update:indeterminate"),
        ]


class VChip(HtmlElement):
    """
    Vuetify's v-chip component. See more info and examples |v-chip_vuetify_link|.

    .. |v-chip_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-chip" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param filter: Displays a selection icon when selected
    :type boolean:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param elevation: See description |v-chip_vuetify_link|.
    :type string | number:
    :param value: See description |v-chip_vuetify_link|.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param selected_class: Configure the active CSS class applied when the item is selected.
    :type string:
    :param rounded: See description |v-chip_vuetify_link|.
    :type string | number | boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |v-chip_vuetify_link|.
    :type boolean:
    :param exact: See description |v-chip_vuetify_link|.
    :type boolean:
    :param to: See description |v-chip_vuetify_link|.
    :type unknown:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-chip_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":
    :param text: See description |v-chip_vuetify_link|.
    :type string:
    :param link: Explicitly define the chip as a link
    :type boolean:
    :param active_class: See description |v-chip_vuetify_link|.
    :type string:
    :param append_avatar: See description |v-chip_vuetify_link|.
    :type string:
    :param append_icon: See description |v-chip_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param closable: Adds remove button and then a chip can be closed
    :type boolean:
    :param close_icon: Change the default icon used for **close** chips
    :type string | (new () => any) | FunctionalComponent:
    :param close_label: See description |v-chip_vuetify_link|.
    :type string:
    :param draggable: Makes the chip draggable
    :type boolean:
    :param filter_icon: Change the default icon used for **filter** chips
    :type string:
    :param label: Applies a medium size border radius
    :type boolean:
    :param pill: Remove `v-avatar` padding
    :type boolean:
    :param prepend_avatar: See description |v-chip_vuetify_link|.
    :type string:
    :param prepend_icon: See description |v-chip_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param ripple: Applies the v-ripple directive
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:

    Events

    :param click_close: Emitted when close icon is clicked
    :param update_modelValue: Event that is emitted when the component's model changes
    :param group_selected: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-chip.json))
    :param clickOnce: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-chip", children, **kwargs)
        self._attr_names += [
            "border",
            "filter",
            "density",
            "elevation",
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "rounded",
            "href",
            "replace",
            "exact",
            "to",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
            "text",
            "link",
            ("active_class", "activeClass"),
            ("append_avatar", "appendAvatar"),
            ("append_icon", "appendIcon"),
            "closable",
            ("close_icon", "closeIcon"),
            ("close_label", "closeLabel"),
            "draggable",
            ("filter_icon", "filterIcon"),
            "label",
            "pill",
            ("prepend_avatar", "prependAvatar"),
            ("prepend_icon", "prependIcon"),
            "ripple",
            ("model_value", "modelValue"),
        ]
        self._event_names += [
            ("click_close", "click:close"),
            ("update_modelValue", "update:modelValue"),
            ("group_selected", "group:selected"),
            "click",
            "clickOnce",
        ]


class VChipGroup(HtmlElement):
    """
    Vuetify's v-chip-group component. See more info and examples |v-chip-group_vuetify_link|.

    .. |v-chip-group_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-chip-group" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the selected CSS class.
    :type string:
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | "force":
    :param filter: Applies an checkmark icon in front of every chip for using it like a filter
    :type boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-chip-group_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":
    :param column: Remove horizontal pagination and wrap items as needed
    :type boolean:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-chip-group", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
            "filter",
            "tag",
            "theme",
            "color",
            "variant",
            "column",
            ("value_comparator", "valueComparator"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VCode(HtmlElement):
    """
    Vuetify's v-code component. See more info and examples |v-code_vuetify_link|.

    .. |v-code_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-code" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-code", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VColorPicker(HtmlElement):
    """
    Vuetify's v-color-picker component. See more info and examples |v-color-picker_vuetify_link|.

    .. |v-color-picker_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-color-picker" target="_blank">here</a>


    :param elevation: See description |v-color-picker_vuetify_link|.
    :type string | number:
    :param rounded: See description |v-color-picker_vuetify_link|.
    :type string | number | boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param canvas_height: Height of canvas
    :type string | number:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param dot_size: Changes the size of the selection dot on the canvas
    :type string | number:
    :param hide_canvas: Hides canvas
    :type boolean:
    :param hide_sliders: Hides sliders
    :type boolean:
    :param hide_inputs: Hides inputs
    :type boolean:
    :param mode: Sets mode of inputs. Available modes are 'rgba', 'hsla', and 'hexa'. Can be synced with the `.sync` modifier.
    :type string:
    :param modes: See description |v-color-picker_vuetify_link|.
    :type string[]:
    :param show_swatches: Displays color swatches
    :type boolean:
    :param swatches_max_height: Sets the maximum height of the swatches section
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type string | Record<string, unknown>:
    :param width: Sets the width of the color picker
    :type string | number:
    :param swatches: Sets the available color swatches to select from - This prop only accepts rgba hex strings
    :type string[][]:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_mode: Selected mode
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-color-picker", children, **kwargs)
        self._attr_names += [
            "elevation",
            "rounded",
            "theme",
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
            "width",
            "swatches",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_mode", "update:mode"),
        ]


class VCombobox(HtmlElement):
    """
    Vuetify's v-combobox component. See more info and examples |v-combobox_vuetify_link|.

    .. |v-combobox_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-combobox" target="_blank">here</a>


    :param label: See description |v-combobox_vuetify_link|.
    :type string:
    :param type: Sets input type
    :type string:
    :param filter_mode: See description |v-combobox_vuetify_link|.
    :type "every" | "some" | "union" | "intersection":
    :param no_filter: See description |v-combobox_vuetify_link|.
    :type boolean:
    :param custom_filter: See description |v-combobox_vuetify_link|.
    :type (value: string, query: string, item: any) => number | boolean | [number, number] | [number, number][]:
    :param custom_key_filter: See description |v-combobox_vuetify_link|.
    :type {  }:
    :param reverse: See description |v-combobox_vuetify_link|.
    :type boolean:
    :param filter_keys: See description |v-combobox_vuetify_link|.
    :type string | string[]:
    :param chips: Changes display of selections to chips
    :type boolean:
    :param closable_chips: See description |v-combobox_vuetify_link|.
    :type boolean:
    :param eager: Will force the components content to render on mounted. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param hide_no_data: See description |v-combobox_vuetify_link|.
    :type boolean:
    :param hide_selected: Do not display in the select menu items that are already selected
    :type boolean:
    :param menu: See description |v-combobox_vuetify_link|.
    :type boolean:
    :param menu_icon: See description |v-combobox_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param menu_props: See description |v-combobox_vuetify_link|.
    :type unknown:
    :param id: See description |v-combobox_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the input
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param transition: See description |v-combobox_vuetify_link|.
    :type string | boolean:
    :param name: See description |v-combobox_vuetify_link|.
    :type string:
    :param multiple: Changes select to multiple. Accepts array for value
    :type boolean:
    :param no_data_text: Text shown when no items are provided to the component
    :type string:
    :param open_on_clear: When using the **clearable** prop, once cleared, the select menu will either open or stay open, depending on the current state
    :type boolean:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param items: Can be an array of objects or array of strings. When using objects, will look for a title, value and disabled keys. This can be changed using the **item-title**, **item-value** and **item-disabled** props.  Objects that have a **header** or **divider** property are considered special cases and generate a list header or divider; these items are not selectable.
    :type unknown[]:
    :param item_title: See description |v-combobox_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_value: See description |v-combobox_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_children: See description |v-combobox_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_props: See description |v-combobox_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**
    :type boolean:
    :param autofocus: Enables autofocus
    :type boolean:
    :param hint: See description |v-combobox_vuetify_link|.
    :type string:
    :param persistent_hint: See description |v-combobox_vuetify_link|.
    :type boolean:
    :param prefix: Displays prefix text
    :type string:
    :param placeholder: Sets the input’s placeholder text
    :type string:
    :param persistent_placeholder: Forces placeholder to always be visible
    :type boolean:
    :param persistent_counter: See description |v-combobox_vuetify_link|.
    :type boolean:
    :param suffix: Displays suffix text
    :type string:
    :param append_icon: Appends an icon to the outside the component's input, uses same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-combobox_vuetify_link|.
    :type string | string[]:
    :param direction: See description |v-combobox_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param error: See description |v-combobox_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-combobox_vuetify_link|.
    :type string | number:
    :param readonly: Puts input in readonly state
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param validate_on: See description |v-combobox_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param bg_color: See description |v-combobox_vuetify_link|.
    :type string:
    :param clearable: Allows for the component to be cleared
    :type boolean:
    :param clear_icon: See description |v-combobox_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param color: See description |v-combobox_vuetify_link|.
    :type string:
    :param persistent_clear: See description |v-combobox_vuetify_link|.
    :type boolean:
    :param prepend_inner_icon: See description |v-combobox_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param single_line: Label does not move on focus/dirty
    :type boolean:
    :param variant: Applies a distinct style to the component
    :type "underlined" | "outlined" | "filled" | "solo" | "plain":
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
    :type string | boolean:
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :type string | number | true:
    :param counter_value: See description |v-combobox_vuetify_link|.
    :type (value: any) => number:
    :param delimiters: Accepts an array of strings that will trigger a new tag when typing. Does not replace the normal Tab and Enter keys.
    :type string[]:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-combobox.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-combobox.json))
    :param click_clear: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-combobox.json))
    :param click_appendInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-combobox.json))
    :param click_prependInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-combobox.json))
    :param update_search: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-combobox.json))
    :param update_menu: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-combobox.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-combobox", children, **kwargs)
        self._attr_names += [
            "label",
            "type",
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            "reverse",
            ("filter_keys", "filterKeys"),
            "chips",
            ("closable_chips", "closableChips"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "id",
            "disabled",
            ("model_value", "modelValue"),
            "theme",
            "transition",
            "name",
            "multiple",
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("value_comparator", "valueComparator"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            "autofocus",
            "hint",
            ("persistent_hint", "persistentHint"),
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "direction",
            "density",
            "error",
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
            "active",
            "color",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "loading",
            "counter",
            ("counter_value", "counterValue"),
            "delimiters",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_search", "update:search"),
            ("update_menu", "update:menu"),
        ]


class VCounter(HtmlElement):
    """
    Vuetify's v-counter component. See more info and examples |v-counter_vuetify_link|.

    .. |v-counter_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-counter" target="_blank">here</a>


    :param transition: See description |v-counter_vuetify_link|.
    :type string | { component: DefineComponent<{ group: BooleanConstructor; hideOnLeave: BooleanConstructor; leaveAbsolute: BooleanConstructor; mode: { type: StringConstructor; default: string; }; origin: { type: StringConstructor; default: string; }; }, () => VNode<RendererNode, RendererElement, { [key: string]: any; }>, unknown, {}, {}, ComponentOptionsMixin, ComponentOptionsMixin, {}, string, PublicProps, Readonly<ExtractPropTypes<{ group: BooleanConstructor; hideOnLeave: BooleanConstructor; leaveAbsolute: BooleanConstructor; mode: { type: StringConstructor; default: string; }; origin: { type: StringConstructor; default: string; }; }>>, { group: boolean; hideOnLeave: boolean; leaveAbsolute: boolean; mode: string; origin: string; }> }:
    :param value: See description |v-counter_vuetify_link|.
    :type string | number:
    :param active: Determines whether the counter is visible or not
    :type boolean:
    :param max: See description |v-counter_vuetify_link|.
    :type string | number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-counter", children, **kwargs)
        self._attr_names += [
            "transition",
            "value",
            "active",
            "max",
        ]
        self._event_names += []


class VDefaultsProvider(HtmlElement):
    """
    Vuetify's v-defaults-provider component. See more info and examples |v-defaults-provider_vuetify_link|.

    .. |v-defaults-provider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-defaults-provider" target="_blank">here</a>


    :param reset: See description |v-defaults-provider_vuetify_link|.
    :type string | number:
    :param root: See description |v-defaults-provider_vuetify_link|.
    :type boolean:
    :param scoped: See description |v-defaults-provider_vuetify_link|.
    :type boolean:
    :param defaults: Specify new default prop values for components. Keep in mind that this will be merged with previously defined values
    :type { global: Record<string, unknown> }:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-defaults-provider", children, **kwargs)
        self._attr_names += [
            "reset",
            "root",
            "scoped",
            "defaults",
        ]
        self._event_names += []


class VDialog(HtmlElement):
    """
    Vuetify's v-dialog component. See more info and examples |v-dialog_vuetify_link|.

    .. |v-dialog_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog" target="_blank">here</a>


    :param activator: See description |v-dialog_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param fullscreen: Changes layout for fullscreen display.
    :type boolean:
    :param scrollable: See description |v-dialog_vuetify_link|.
    :type boolean:
    :param retain_focus: Tab focus will return to the first child of the dialog by default. Disable this when using external tools that require focus such as TinyMCE or vue-clipboard.
    :type boolean:
    :param absolute: Applies **position: absolute** to the content element.
    :type boolean:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |v-dialog_vuetify_link|.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param no_click_animation: Disables the bounce effect when clicking outside of a `v-dialog`'s content when using the **persistent** prop.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param persistent: Clicking outside of the element or pressing **esc** key will not deactivate it.
    :type boolean:
    :param scrim: See description |v-dialog_vuetify_link|.
    :type string | boolean:
    :param z_index: The z-index used for the component
    :type string | number:
    :param activator_props: See description |v-dialog_vuetify_link|.
    :type {  }:
    :param open_on_click: See description |v-dialog_vuetify_link|.
    :type boolean:
    :param open_on_hover: Designates whether component should activate when its activator is hovered.
    :type boolean:
    :param open_on_focus: See description |v-dialog_vuetify_link|.
    :type boolean:
    :param close_on_content_click: See description |v-dialog_vuetify_link|.
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
    :param eager: See description |v-dialog_vuetify_link|.
    :type boolean:
    :param location_strategy: See description |v-dialog_vuetify_link|.
    :type "static" | "connected" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param location: Aligns the component towards the `top`, `bottom`, `right`, `left`, can be combined like for example `top right`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param origin: See description |v-dialog_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a> | "auto" | "overlap":
    :param offset: See description |v-dialog_vuetify_link|.
    :type string | number | number[]:
    :param scroll_strategy: See description |v-dialog_vuetify_link|.
    :type "none" | "close" | "block" | "reposition" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param transition: See description |v-dialog_vuetify_link|.
    :type string | { component: DefineComponent<{ target: PropType<HTMLElement>; }, () => JSX.Element, unknown, {}, {}, ComponentOptionsMixin, ComponentOptionsMixin, {}, string, PublicProps, Readonly<ExtractPropTypes<{ target: PropType<HTMLElement>; }>>, {}> }:
    :param attach: Specifies which DOM element that this component should detach to. String can be any valid querySelector and Object can be any valid Node. This attachs to the root `v-app` component by default
    :type string | boolean | Element:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-dialog", children, **kwargs)
        self._attr_names += [
            "activator",
            "fullscreen",
            "scrollable",
            ("retain_focus", "retainFocus"),
            "absolute",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
            "persistent",
            "scrim",
            ("z_index", "zIndex"),
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


class VDivider(HtmlElement):
    """
    Vuetify's v-divider component. See more info and examples |v-divider_vuetify_link|.

    .. |v-divider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-divider" target="_blank">here</a>


    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param length: Sets the dividers length. Default unit is px.
    :type string | number:
    :param color: See description |v-divider_vuetify_link|.
    :type string:
    :param inset: Adds indentation (72px) for **normal** dividers, reduces max height for **vertical**.
    :type boolean:
    :param thickness: Sets the dividers thickness. Default unit is px.
    :type string | number:
    :param vertical: Displays dividers vertically.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-divider", children, **kwargs)
        self._attr_names += [
            "theme",
            "length",
            "color",
            "inset",
            "thickness",
            "vertical",
        ]
        self._event_names += []


class VExpansionPanels(HtmlElement):
    """
    Vuetify's v-expansion-panels component. See more info and examples |v-expansion-panels_vuetify_link|.

    .. |v-expansion-panels_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expansion-panels" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the selected CSS class.
    :type string:
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | "force":
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-expansion-panels_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "default" | "accordion" | "inset" | "popout":
    :param readonly: Makes the entire expansion-panel read only.
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expansion-panels", children, **kwargs)
        self._attr_names += [
            ("model_value", "modelValue"),
            "multiple",
            "max",
            ("selected_class", "selectedClass"),
            "disabled",
            "mandatory",
            "tag",
            "theme",
            "color",
            "variant",
            "readonly",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VExpansionPanel(HtmlElement):
    """
    Vuetify's v-expansion-panel component. See more info and examples |v-expansion-panel_vuetify_link|.

    .. |v-expansion-panel_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expansion-panel" target="_blank">here</a>


    :param elevation: See description |v-expansion-panel_vuetify_link|.
    :type string | number:
    :param value: Controls the opened/closed state of content
    :type any:
    :param disabled: Disables the expansion-panel content
    :type boolean:
    :param selected_class: Configure the active CSS class applied when the item is selected.
    :type string:
    :param eager: See description |v-expansion-panel_vuetify_link|.
    :type boolean:
    :param rounded: See description |v-expansion-panel_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param color: See description |v-expansion-panel_vuetify_link|.
    :type string:
    :param expand_icon: See description |v-expansion-panel_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param collapse_icon: See description |v-expansion-panel_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param hide_actions: See description |v-expansion-panel_vuetify_link|.
    :type boolean:
    :param ripple: See description |v-expansion-panel_vuetify_link|.
    :type boolean | Record<string, any>:
    :param readonly: Makes the expansion-panel content read only.
    :type boolean:
    :param title: See description |v-expansion-panel_vuetify_link|.
    :type string:
    :param text: See description |v-expansion-panel_vuetify_link|.
    :type string:
    :param bg_color: See description |v-expansion-panel_vuetify_link|.
    :type string:

    Events

    :param group_selected: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-expansion-panel.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expansion-panel", children, **kwargs)
        self._attr_names += [
            "elevation",
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "eager",
            "rounded",
            "tag",
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("hide_actions", "hideActions"),
            "ripple",
            "readonly",
            "title",
            "text",
            ("bg_color", "bgColor"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VExpansionPanelText(HtmlElement):
    """
    Vuetify's v-expansion-panel-text component. See more info and examples |v-expansion-panel-text_vuetify_link|.

    .. |v-expansion-panel-text_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expansion-panel-text" target="_blank">here</a>


    :param eager: See description |v-expansion-panel-text_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expansion-panel-text", children, **kwargs)
        self._attr_names += [
            "eager",
        ]
        self._event_names += []


class VExpansionPanelTitle(HtmlElement):
    """
    Vuetify's v-expansion-panel-title component. See more info and examples |v-expansion-panel-title_vuetify_link|.

    .. |v-expansion-panel-title_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expansion-panel-title" target="_blank">here</a>


    :param color: See description |v-expansion-panel-title_vuetify_link|.
    :type string:
    :param expand_icon: See description |v-expansion-panel-title_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param collapse_icon: See description |v-expansion-panel-title_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param hide_actions: See description |v-expansion-panel-title_vuetify_link|.
    :type boolean:
    :param ripple: See description |v-expansion-panel-title_vuetify_link|.
    :type boolean | Record<string, any>:
    :param readonly: See description |v-expansion-panel-title_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expansion-panel-title", children, **kwargs)
        self._attr_names += [
            "color",
            ("expand_icon", "expandIcon"),
            ("collapse_icon", "collapseIcon"),
            ("hide_actions", "hideActions"),
            "ripple",
            "readonly",
        ]
        self._event_names += []


class VField(HtmlElement):
    """
    Vuetify's v-field component. See more info and examples |v-field_vuetify_link|.

    .. |v-field_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-field" target="_blank">here</a>


    :param label: See description |v-field_vuetify_link|.
    :type string:
    :param id: See description |v-field_vuetify_link|.
    :type string:
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param append_inner_icon: See description |v-field_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param bg_color: See description |v-field_vuetify_link|.
    :type string:
    :param clearable: Allows for the component to be cleared
    :type boolean:
    :param clear_icon: See description |v-field_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param color: See description |v-field_vuetify_link|.
    :type string:
    :param dirty: Manually apply the dirty state styling
    :type boolean:
    :param disabled: Removes the ability to click or target the input
    :type boolean:
    :param error: See description |v-field_vuetify_link|.
    :type boolean:
    :param persistent_clear: See description |v-field_vuetify_link|.
    :type boolean:
    :param prepend_inner_icon: See description |v-field_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param reverse: See description |v-field_vuetify_link|.
    :type boolean:
    :param single_line: Label does not move on focus/dirty
    :type boolean:
    :param variant: Applies a distinct style to the component
    :type "underlined" | "outlined" | "filled" | "solo" | "plain":
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param loading: See description |v-field_vuetify_link|.
    :type string | boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type unknown:

    Events

    :param click_clear: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-field.json))
    :param click_appendInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-field.json))
    :param click_prependInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-field.json))
    :param update_modelValue: Event that is emitted when the component's model changes
    :param click_control: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-field.json))
    :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-field.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-field", children, **kwargs)
        self._attr_names += [
            "label",
            "id",
            "focused",
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "color",
            "dirty",
            "disabled",
            "error",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            "reverse",
            ("single_line", "singleLine"),
            "variant",
            "theme",
            "loading",
            ("model_value", "modelValue"),
        ]
        self._event_names += [
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_modelValue", "update:modelValue"),
            ("click_control", "click:control"),
            ("update_focused", "update:focused"),
        ]


class VFieldLabel(HtmlElement):
    """
    Vuetify's v-field-label component. See more info and examples |v-field-label_vuetify_link|.

    .. |v-field-label_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-field-label" target="_blank">here</a>


    :param floating: See description |v-field-label_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-field-label", children, **kwargs)
        self._attr_names += [
            "floating",
        ]
        self._event_names += []


class VFileInput(HtmlElement):
    """
    Vuetify's v-file-input component. See more info and examples |v-file-input_vuetify_link|.

    .. |v-file-input_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-file-input" target="_blank">here</a>


    :param id: See description |v-file-input_vuetify_link|.
    :type string:
    :param append_icon: Appends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-file-input_vuetify_link|.
    :type string | string[]:
    :param direction: See description |v-file-input_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param disabled: Removes the ability to click or target the input
    :type boolean:
    :param error: See description |v-file-input_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-file-input_vuetify_link|.
    :type string | number:
    :param name: See description |v-file-input_vuetify_link|.
    :type string:
    :param label: See description |v-file-input_vuetify_link|.
    :type string:
    :param readonly: Puts input in readonly state
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type File[]:
    :param validate_on: See description |v-file-input_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-file-input_vuetify_link|.
    :type any:
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param reverse: See description |v-file-input_vuetify_link|.
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param append_inner_icon: See description |v-file-input_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param bg_color: See description |v-file-input_vuetify_link|.
    :type string:
    :param clearable: Allows for the component to be cleared
    :type boolean:
    :param clear_icon: See description |v-file-input_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param color: See description |v-file-input_vuetify_link|.
    :type string:
    :param dirty: Manually apply the dirty state styling
    :type boolean:
    :param persistent_clear: See description |v-file-input_vuetify_link|.
    :type boolean:
    :param prepend_inner_icon: See description |v-file-input_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param single_line: Label does not move on focus/dirty
    :type boolean:
    :param variant: Applies a distinct style to the component
    :type "underlined" | "outlined" | "filled" | "solo" | "plain":
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
    :type string | boolean:
    :param chips: Changes display of selections to chips
    :type boolean:
    :param counter: See description |v-file-input_vuetify_link|.
    :type boolean:
    :param counter_size_string: See description |v-file-input_vuetify_link|.
    :type string:
    :param counter_string: See description |v-file-input_vuetify_link|.
    :type string:
    :param multiple: Adds the **multiple** attribute to the input, allowing multiple file selections.
    :type boolean:
    :param hint: See description |v-file-input_vuetify_link|.
    :type string:
    :param persistent_hint: See description |v-file-input_vuetify_link|.
    :type boolean:
    :param placeholder: See description |v-file-input_vuetify_link|.
    :type string:
    :param show_size: Sets the displayed size of selected file(s). When using **true** will default to _1000_ displaying (**kB, MB, GB**) while _1024_ will display (**KiB, MiB, GiB**).
    :type boolean | 1000 | 1024:

    Events

    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-file-input.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-file-input.json))
    :param click_clear: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-file-input.json))
    :param click_appendInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-file-input.json))
    :param click_prependInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-file-input.json))
    :param click_control: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-file-input.json))
    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-file-input", children, **kwargs)
        self._attr_names += [
            "id",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "direction",
            "density",
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
            "reverse",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "color",
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "theme",
            "loading",
            "chips",
            "counter",
            ("counter_size_string", "counterSizeString"),
            ("counter_string", "counterString"),
            "multiple",
            "hint",
            ("persistent_hint", "persistentHint"),
            "placeholder",
            ("show_size", "showSize"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("click_control", "click:control"),
            ("update_modelValue", "update:modelValue"),
        ]


class VFooter(HtmlElement):
    """
    Vuetify's v-footer component. See more info and examples |v-footer_vuetify_link|.

    .. |v-footer_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-footer" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param elevation: See description |v-footer_vuetify_link|.
    :type string | number:
    :param name: See description |v-footer_vuetify_link|.
    :type string:
    :param order: See description |v-footer_vuetify_link|.
    :type string | number:
    :param absolute: See description |v-footer_vuetify_link|.
    :type boolean:
    :param rounded: See description |v-footer_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param app: See description |v-footer_vuetify_link|.
    :type boolean:
    :param color: See description |v-footer_vuetify_link|.
    :type string:
    :param height: See description |v-footer_vuetify_link|.
    :type string | number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-footer", children, **kwargs)
        self._attr_names += [
            "border",
            "elevation",
            "name",
            "order",
            "absolute",
            "rounded",
            "tag",
            "theme",
            "app",
            "color",
            "height",
        ]
        self._event_names += []


class VForm(HtmlElement):
    """
    Vuetify's v-form component. See more info and examples |v-form_vuetify_link|.

    .. |v-form_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-form" target="_blank">here</a>


    :param disabled: Puts all children inputs into a disabled state
    :type boolean:
    :param fast_fail: Stop validation as soon as any rules fail.
    :type boolean:
    :param readonly: Puts all children inputs into a readonly state.
    :type boolean:
    :param model_value: The value representing the validity of the form. If the value is `null` then no validation has taken place yet, or the form has been reset. Otherwise the value will be a `boolean` that indicates if validation has passed or not.
    :type boolean:
    :param validate_on: Changes the events in which validation occurs.
    :type "blur" | "input" | "submit":

    Events

    :param submit: Emitted when form is submitted
    :param update_modelValue: Event emitted when the form's validity changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-form", children, **kwargs)
        self._attr_names += [
            "disabled",
            ("fast_fail", "fastFail"),
            "readonly",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
        ]
        self._event_names += [
            "submit",
            ("update_modelValue", "update:modelValue"),
        ]


class VContainer(HtmlElement):
    """
    Vuetify's v-container component. See more info and examples |v-container_vuetify_link|.

    .. |v-container_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-container" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param fluid: Removes viewport maximum-width size breakpoints.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-container", children, **kwargs)
        self._attr_names += [
            "tag",
            "fluid",
        ]
        self._event_names += []


class VCol(HtmlElement):
    """
    Vuetify's v-col component. See more info and examples |v-col_vuetify_link|.

    .. |v-col_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-col" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param cols: Sets the default number of columns the component extends. Available options are: **1 -> 12** and **auto**.
    :type string | number | boolean:
    :param offset: Sets the default offset for the column.
    :type string | number:
    :param order: See description |v-col_vuetify_link|.
    :type string | number:
    :param align_self: See description |v-col_vuetify_link|.
    :type "auto" | "start" | "end" | "center" | "baseline" | "stretch":

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-col", children, **kwargs)
        self._attr_names += [
            "tag",
            "cols",
            "offset",
            "order",
            ("align_self", "alignSelf"),
        ]
        self._event_names += []


class VRow(HtmlElement):
    """
    Vuetify's v-row component. See more info and examples |v-row_vuetify_link|.

    .. |v-row_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-row" target="_blank">here</a>


    :param align: See description |v-row_vuetify_link|.
    :type "start" | "end" | "center" | "baseline" | "stretch":
    :param justify: See description |v-row_vuetify_link|.
    :type "start" | "end" | "center" | "stretch" | "space-between" | "space-around" | "space-evenly":
    :param align_content: See description |v-row_vuetify_link|.
    :type "start" | "end" | "center" | "stretch" | "space-between" | "space-around" | "space-evenly":
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param dense: Reduces the gutter between `v-col`s.
    :type boolean:
    :param no_gutters: Removes the gutter between `v-col`s.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-row", children, **kwargs)
        self._attr_names += [
            "align",
            "justify",
            ("align_content", "alignContent"),
            "tag",
            "dense",
            ("no_gutters", "noGutters"),
        ]
        self._event_names += []


class VSpacer(HtmlElement):
    """
    Vuetify's v-spacer component. See more info and examples |v-spacer_vuetify_link|.

    .. |v-spacer_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-spacer" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-spacer", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VHover(HtmlElement):
    """
    Vuetify's v-hover component. See more info and examples |v-hover_vuetify_link|.

    .. |v-hover_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-hover" target="_blank">here</a>


    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :type string | number:
    :param disabled: Removes hover functionality
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-hover", children, **kwargs)
        self._attr_names += [
            ("close_delay", "closeDelay"),
            ("open_delay", "openDelay"),
            "disabled",
            ("model_value", "modelValue"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VIcon(HtmlElement):
    """
    Vuetify's v-icon component. See more info and examples |v-icon_vuetify_link|.

    .. |v-icon_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-icon" target="_blank">here</a>


    :param color: See description |v-icon_vuetify_link|.
    :type string:
    :param start: See description |v-icon_vuetify_link|.
    :type boolean:
    :param end: See description |v-icon_vuetify_link|.
    :type boolean:
    :param icon: Designates a specific icon.
    :type string | (new () => any) | FunctionalComponent:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-icon", children, **kwargs)
        self._attr_names += [
            "color",
            "start",
            "end",
            "icon",
            "size",
            "tag",
            "theme",
        ]
        self._event_names += []


class VComponentIcon(HtmlElement):
    """
    Vuetify's v-component-icon component. See more info and examples |v-component-icon_vuetify_link|.

    .. |v-component-icon_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-component-icon" target="_blank">here</a>


    :param icon: MISSING DESCRIPTION
    :type string | (new () => any) | FunctionalComponent:
    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-component-icon", children, **kwargs)
        self._attr_names += [
            "icon",
            "tag",
        ]
        self._event_names += []


class VSvgIcon(HtmlElement):
    """
    Vuetify's v-svg-icon component. See more info and examples |v-svg-icon_vuetify_link|.

    .. |v-svg-icon_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-svg-icon" target="_blank">here</a>


    :param icon: MISSING DESCRIPTION
    :type string | (new () => any) | FunctionalComponent:
    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-svg-icon", children, **kwargs)
        self._attr_names += [
            "icon",
            "tag",
        ]
        self._event_names += []


class VLigatureIcon(HtmlElement):
    """
    Vuetify's v-ligature-icon component. See more info and examples |v-ligature-icon_vuetify_link|.

    .. |v-ligature-icon_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-ligature-icon" target="_blank">here</a>


    :param icon: MISSING DESCRIPTION
    :type string | (new () => any) | FunctionalComponent:
    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-ligature-icon", children, **kwargs)
        self._attr_names += [
            "icon",
            "tag",
        ]
        self._event_names += []


class VClassIcon(HtmlElement):
    """
    Vuetify's v-class-icon component. See more info and examples |v-class-icon_vuetify_link|.

    .. |v-class-icon_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-class-icon" target="_blank">here</a>


    :param icon: MISSING DESCRIPTION
    :type string | (new () => any) | FunctionalComponent:
    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-class-icon", children, **kwargs)
        self._attr_names += [
            "icon",
            "tag",
        ]
        self._event_names += []


class VImg(HtmlElement):
    """
    Vuetify's v-img component. See more info and examples |v-img_vuetify_link|.

    .. |v-img_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-img" target="_blank">here</a>


    :param transition: The transition to use when switching from `lazy-src` to `src`.
    :type string:
    :param aspect_ratio: Calculated as `width/height`, so for a 1920x1080px image this will be `1.7778`. Will be calculated automatically if omitted.
    :type string | number:
    :param alt: Alternate text for screen readers. Leave empty for decorative images.
    :type string:
    :param cover: Resizes the background image to cover the entire container.
    :type boolean:
    :param eager: Will force the components content to render on mounted. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param gradient: See description |v-img_vuetify_link|.
    :type string:
    :param lazy_src: See description |v-img_vuetify_link|.
    :type string:
    :param options: See description |v-img_vuetify_link|.
    :type { root: any; rootMargin: any; threshold: any }:
    :param sizes: See description |v-img_vuetify_link|.
    :type string:
    :param src: The image URL. This prop is mandatory.
    :type string | { src: string; srcset: string; lazySrc: string; aspect: number }:
    :param srcset: See description |v-img_vuetify_link|.
    :type string:
    :param width: See description |v-img_vuetify_link|.
    :type string | number:

    Events

    :param loadstart: Emitted when the image starts to load
    :param load: Emitted when the image is loaded
    :param error: Emitted if the image fails to load
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-img", children, **kwargs)
        self._attr_names += [
            "transition",
            ("aspect_ratio", "aspectRatio"),
            "alt",
            "cover",
            "eager",
            "gradient",
            ("lazy_src", "lazySrc"),
            "options",
            "sizes",
            "src",
            "srcset",
            "width",
        ]
        self._event_names += [
            "loadstart",
            "load",
            "error",
        ]


class VInput(HtmlElement):
    """
    Vuetify's v-input component. See more info and examples |v-input_vuetify_link|.

    .. |v-input_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-input" target="_blank">here</a>


    :param id: See description |v-input_vuetify_link|.
    :type string:
    :param append_icon: Appends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-input_vuetify_link|.
    :type string | string[]:
    :param direction: See description |v-input_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: Puts the input in a manual error state
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-input_vuetify_link|.
    :type string | number:
    :param name: See description |v-input_vuetify_link|.
    :type string:
    :param label: See description |v-input_vuetify_link|.
    :type string:
    :param readonly: Puts input in readonly state
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param validate_on: See description |v-input_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-input_vuetify_link|.
    :type any:
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":

    Events

    :param click_prepend: Emitted when prepended icon is clicked
    :param click_append: Emitted when appended icon is clicked
    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-input", children, **kwargs)
        self._attr_names += [
            "id",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "direction",
            "density",
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
            ("update_modelValue", "update:modelValue"),
        ]


class VItemGroup(HtmlElement):
    """
    Vuetify's v-item-group component. See more info and examples |v-item-group_vuetify_link|.

    .. |v-item-group_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-item-group" target="_blank">here</a>


    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the selected CSS class. This class will be available in `v-item` default scoped slot.
    :type string:
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | "force":
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-item-group", children, **kwargs)
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


class VItem(HtmlElement):
    """
    Vuetify's v-item component. See more info and examples |v-item_vuetify_link|.

    .. |v-item_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-item" target="_blank">here</a>


    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param selected_class: Configure the active CSS class applied when the item is selected.
    :type string:

    Events

    :param group_selected: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-item.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-item", children, **kwargs)
        self._attr_names += [
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VKbd(HtmlElement):
    """
    Vuetify's v-kbd component. See more info and examples |v-kbd_vuetify_link|.

    .. |v-kbd_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-kbd" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-kbd", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VLabel(HtmlElement):
    """
    Vuetify's v-label component. See more info and examples |v-label_vuetify_link|.

    .. |v-label_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-label" target="_blank">here</a>


    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param text: Specify the displayed label text
    :type string:
    :param clickable: See description |v-label_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-label", children, **kwargs)
        self._attr_names += [
            "theme",
            "text",
            "clickable",
        ]
        self._event_names += []


class VLayout(HtmlElement):
    """
    Vuetify's v-layout component. See more info and examples |v-layout_vuetify_link|.

    .. |v-layout_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-layout" target="_blank">here</a>


    :param full_height: Sets the component height to 100%
    :type boolean:
    :param overlaps: See description |v-layout_vuetify_link|.
    :type string[]:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-layout", children, **kwargs)
        self._attr_names += [
            ("full_height", "fullHeight"),
            "overlaps",
        ]
        self._event_names += []


class VLayoutItem(HtmlElement):
    """
    Vuetify's v-layout-item component. See more info and examples |v-layout-item_vuetify_link|.

    .. |v-layout-item_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-layout-item" target="_blank">here</a>


    :param name: See description |v-layout-item_vuetify_link|.
    :type string:
    :param order: See description |v-layout-item_vuetify_link|.
    :type string | number:
    :param absolute: See description |v-layout-item_vuetify_link|.
    :type boolean:
    :param position: See description |v-layout-item_vuetify_link|.
    :type "top" | "right" | "bottom" | "left":
    :param size: See description |v-layout-item_vuetify_link|.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-layout-item", children, **kwargs)
        self._attr_names += [
            "name",
            "order",
            "absolute",
            "position",
            "size",
            ("model_value", "modelValue"),
        ]
        self._event_names += []


class VLazy(HtmlElement):
    """
    Vuetify's v-lazy component. See more info and examples |v-lazy_vuetify_link|.

    .. |v-lazy_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-lazy" target="_blank">here</a>


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
    :param transition: See description |v-lazy_vuetify_link|.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param options: See description |v-lazy_vuetify_link|.
    :type { root: any; rootMargin: any; threshold: any }:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-lazy", children, **kwargs)
        self._attr_names += [
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            "tag",
            "transition",
            ("model_value", "modelValue"),
            "options",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VList(HtmlElement):
    """
    Vuetify's v-list component. See more info and examples |v-list_vuetify_link|.

    .. |v-list_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list" target="_blank">here</a>


    :param active_color: See description |v-list_vuetify_link|.
    :type string:
    :param active_class: The class applied to the component when it is in an active state
    :type string:
    :param bg_color: See description |v-list_vuetify_link|.
    :type string:
    :param disabled: Puts all children inputs into a disabled state
    :type boolean:
    :param nav: See description |v-list_vuetify_link|.
    :type boolean:
    :param lines: See description |v-list_vuetify_link|.
    :type false | "one" | "two" | "three":
    :param mandatory: See description |v-list_vuetify_link|.
    :type boolean:
    :param select_strategy: See description |v-list_vuetify_link|.
    :type "single-leaf" | "leaf" | "independent" | "single-independent" | "classic" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/nested/selectStrategies.ts#L2-L9" target="_blank">SelectStrategyFn</a>:
    :param open_strategy: See description |v-list_vuetify_link|.
    :type "single" | "multiple" | "list" | { open: <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/nested/openStrategies.ts#L1-L8" target="_blank">OpenStrategyFn</a>; select: <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/nested/openStrategies.ts#L10-L18" target="_blank">OpenSelectStrategyFn</a> }:
    :param opened: See description |v-list_vuetify_link|.
    :type unknown[]:
    :param selected: See description |v-list_vuetify_link|.
    :type unknown[]:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
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
    :param elevation: See description |v-list_vuetify_link|.
    :type string | number:
    :param item_type: See description |v-list_vuetify_link|.
    :type string:
    :param items: An array of strings or objects used for automatically generating children components
    :type unknown[]:
    :param item_title: See description |v-list_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_value: See description |v-list_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_children: See description |v-list_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_props: See description |v-list_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param return_object: See description |v-list_vuetify_link|.
    :type boolean:
    :param rounded: See description |v-list_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-list_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":

    Events

    :param update_selected: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-list.json))
    :param update_opened: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-list.json))
    :param click_open: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-list.json))
    :param click_select: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-list.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list", children, **kwargs)
        self._attr_names += [
            ("active_color", "activeColor"),
            ("active_class", "activeClass"),
            ("bg_color", "bgColor"),
            "disabled",
            "nav",
            "lines",
            "mandatory",
            ("select_strategy", "selectStrategy"),
            ("open_strategy", "openStrategy"),
            "opened",
            "selected",
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
            "rounded",
            "tag",
            "theme",
            "color",
            "variant",
        ]
        self._event_names += [
            ("update_selected", "update:selected"),
            ("update_opened", "update:opened"),
            ("click_open", "click:open"),
            ("click_select", "click:select"),
        ]


class VListGroup(HtmlElement):
    """
    Vuetify's v-list-group component. See more info and examples |v-list-group_vuetify_link|.

    .. |v-list-group_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-group" target="_blank">here</a>


    :param title: See description |v-list-group_vuetify_link|.
    :type string:
    :param active_color: See description |v-list-group_vuetify_link|.
    :type string:
    :param color: See description |v-list-group_vuetify_link|.
    :type string:
    :param collapse_icon: See description |v-list-group_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param expand_icon: See description |v-list-group_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param append_icon: Appends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param fluid: See description |v-list-group_vuetify_link|.
    :type boolean:
    :param subgroup: See description |v-list-group_vuetify_link|.
    :type boolean:
    :param value: Expands / Collapse the list-group
    :type any:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param items: See description |v-list-group_vuetify_link|.
    :type InternalListItem[]:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-group", children, **kwargs)
        self._attr_names += [
            "title",
            ("active_color", "activeColor"),
            "color",
            ("collapse_icon", "collapseIcon"),
            ("expand_icon", "expandIcon"),
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "fluid",
            "subgroup",
            "value",
            "tag",
            "items",
        ]
        self._event_names += []


class VListImg(HtmlElement):
    """
    Vuetify's v-list-img component. See more info and examples |v-list-img_vuetify_link|.

    .. |v-list-img_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-img" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-img", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListItem(HtmlElement):
    """
    Vuetify's v-list-item component. See more info and examples |v-list-item_vuetify_link|.

    .. |v-list-item_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item" target="_blank">here</a>


    :param title: Generates a `v-list-item-title` component with the supplied value
    :type string | number | boolean:
    :param subtitle: Generates a `v-list-item-subtitle` component with the supplied value
    :type string | number | boolean:
    :param active_class: See description |v-list-item_vuetify_link|.
    :type string:
    :param active_color: The applied color when a `v-list-item` is in an active state
    :type string:
    :param append_avatar: See description |v-list-item_vuetify_link|.
    :type string:
    :param append_icon: See description |v-list-item_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param nav: See description |v-list-item_vuetify_link|.
    :type boolean:
    :param prepend_avatar: See description |v-list-item_vuetify_link|.
    :type string:
    :param prepend_icon: See description |v-list-item_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param value: The value used for selection.
    :type any:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param link: See description |v-list-item_vuetify_link|.
    :type boolean:
    :param ripple: MISSING DESCRIPTION
    :type boolean:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
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
    :param elevation: See description |v-list-item_vuetify_link|.
    :type string | number:
    :param rounded: See description |v-list-item_vuetify_link|.
    :type string | number | boolean:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |v-list-item_vuetify_link|.
    :type boolean:
    :param exact: See description |v-list-item_vuetify_link|.
    :type boolean:
    :param to: See description |v-list-item_vuetify_link|.
    :type unknown:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-list-item_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":
    :param lines: See description |v-list-item_vuetify_link|.
    :type "one" | "two" | "three":

    Events

    :param clickOnce: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-list-item.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item", children, **kwargs)
        self._attr_names += [
            "title",
            "subtitle",
            ("active_class", "activeClass"),
            ("active_color", "activeColor"),
            ("append_avatar", "appendAvatar"),
            ("append_icon", "appendIcon"),
            "disabled",
            "nav",
            ("prepend_avatar", "prependAvatar"),
            ("prepend_icon", "prependIcon"),
            "value",
            "active",
            "link",
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
            "rounded",
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
    Vuetify's v-list-item-action component. See more info and examples |v-list-item-action_vuetify_link|.

    .. |v-list-item-action_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-action" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param start: See description |v-list-item-action_vuetify_link|.
    :type boolean:
    :param end: See description |v-list-item-action_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-action", children, **kwargs)
        self._attr_names += [
            "tag",
            "start",
            "end",
        ]
        self._event_names += []


class VListItemMedia(HtmlElement):
    """
    Vuetify's v-list-item-media component. See more info and examples |v-list-item-media_vuetify_link|.

    .. |v-list-item-media_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-media" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param start: See description |v-list-item-media_vuetify_link|.
    :type boolean:
    :param end: See description |v-list-item-media_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-media", children, **kwargs)
        self._attr_names += [
            "tag",
            "start",
            "end",
        ]
        self._event_names += []


class VListItemSubtitle(HtmlElement):
    """
    Vuetify's v-list-item-subtitle component. See more info and examples |v-list-item-subtitle_vuetify_link|.

    .. |v-list-item-subtitle_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-subtitle" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-subtitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListItemTitle(HtmlElement):
    """
    Vuetify's v-list-item-title component. See more info and examples |v-list-item-title_vuetify_link|.

    .. |v-list-item-title_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-item-title" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-title", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListSubheader(HtmlElement):
    """
    Vuetify's v-list-subheader component. See more info and examples |v-list-subheader_vuetify_link|.

    .. |v-list-subheader_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-list-subheader" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param color: See description |v-list-subheader_vuetify_link|.
    :type string:
    :param inset: See description |v-list-subheader_vuetify_link|.
    :type boolean:
    :param sticky: See description |v-list-subheader_vuetify_link|.
    :type boolean:
    :param title: See description |v-list-subheader_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-subheader", children, **kwargs)
        self._attr_names += [
            "tag",
            "color",
            "inset",
            "sticky",
            "title",
        ]
        self._event_names += []


class VLocaleProvider(HtmlElement):
    """
    Vuetify's v-locale-provider component. See more info and examples |v-locale-provider_vuetify_link|.

    .. |v-locale-provider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-locale-provider" target="_blank">here</a>


    :param locale: See description |v-locale-provider_vuetify_link|.
    :type string:
    :param fallback_locale: See description |v-locale-provider_vuetify_link|.
    :type string:
    :param messages: See description |v-locale-provider_vuetify_link|.
    :type Record<string, any>:
    :param rtl: See description |v-locale-provider_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-locale-provider", children, **kwargs)
        self._attr_names += [
            "locale",
            ("fallback_locale", "fallbackLocale"),
            "messages",
            "rtl",
        ]
        self._event_names += []


class VMain(HtmlElement):
    """
    Vuetify's v-main component. See more info and examples |v-main_vuetify_link|.

    .. |v-main_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-main" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param scrollable: See description |v-main_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-main", children, **kwargs)
        self._attr_names += [
            "tag",
            "scrollable",
        ]
        self._event_names += []


class VMenu(HtmlElement):
    """
    Vuetify's v-menu component. See more info and examples |v-menu_vuetify_link|.

    .. |v-menu_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-menu" target="_blank">here</a>


    :param activator: See description |v-menu_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param id: See description |v-menu_vuetify_link|.
    :type string:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |v-menu_vuetify_link|.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param no_click_animation: See description |v-menu_vuetify_link|.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param persistent: See description |v-menu_vuetify_link|.
    :type boolean:
    :param scrim: See description |v-menu_vuetify_link|.
    :type string | boolean:
    :param z_index: The z-index used for the component
    :type string | number:
    :param activator_props: See description |v-menu_vuetify_link|.
    :type {  }:
    :param open_on_click: Designates whether menu should open on activator click
    :type boolean:
    :param open_on_hover: Designates whether menu should open on activator hover
    :type boolean:
    :param open_on_focus: See description |v-menu_vuetify_link|.
    :type boolean:
    :param close_on_content_click: Designates if menu should close when its content is clicked
    :type boolean:
    :param close_delay: Milliseconds to wait before closing component. Only works with the **open-on-hover** prop
    :type string | number:
    :param open_delay: Milliseconds to wait before opening component. Only works with the **open-on-hover** prop
    :type string | number:
    :param height: Sets the height for the component.
    :type string | number:
    :param max_height: Sets the max height of the menu content
    :type string | number:
    :param max_width: Sets the maximum width for the component.
    :type string | number:
    :param min_height: Sets the minimum height for the component.
    :type string | number:
    :param min_width: Sets the minimum width for the component.
    :type string | number:
    :param width: Sets the width for the component.
    :type string | number:
    :param eager: See description |v-menu_vuetify_link|.
    :type boolean:
    :param location_strategy: See description |v-menu_vuetify_link|.
    :type "static" | "connected" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param location: Aligns the component towards the `top`, `bottom`, `right`, `left`, can be combined like for example `top right`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param origin: See description |v-menu_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a> | "auto" | "overlap":
    :param offset: See description |v-menu_vuetify_link|.
    :type string | number | number[]:
    :param scroll_strategy: See description |v-menu_vuetify_link|.
    :type "none" | "close" | "block" | "reposition" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param transition: See description |v-menu_vuetify_link|.
    :type string | { component: DefineComponent<{ target: PropType<HTMLElement>; }, () => JSX.Element, unknown, {}, {}, ComponentOptionsMixin, ComponentOptionsMixin, {}, string, PublicProps, Readonly<ExtractPropTypes<{ target: PropType<HTMLElement>; }>>, {}> }:
    :param attach: Specifies which DOM element that this component should detach to. String can be any valid querySelector and Object can be any valid Node. This attachs to the root `v-app` component by default
    :type string | boolean | Element:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-menu", children, **kwargs)
        self._attr_names += [
            "activator",
            "id",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
            "persistent",
            "scrim",
            ("z_index", "zIndex"),
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
    Vuetify's v-messages component. See more info and examples |v-messages_vuetify_link|.

    .. |v-messages_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-messages" target="_blank">here</a>


    :param transition: See description |v-messages_vuetify_link|.
    :type string | { component: DefineComponent<{ group: BooleanConstructor; hideOnLeave: BooleanConstructor; leaveAbsolute: BooleanConstructor; mode: { type: StringConstructor; default: string; }; origin: { type: StringConstructor; default: string; }; }, () => VNode<RendererNode, RendererElement, { [key: string]: any; }>, unknown, {}, {}, ComponentOptionsMixin, ComponentOptionsMixin, {}, string, PublicProps, Readonly<ExtractPropTypes<{ group: BooleanConstructor; hideOnLeave: BooleanConstructor; leaveAbsolute: BooleanConstructor; mode: { type: StringConstructor; default: string; }; origin: { type: StringConstructor; default: string; }; }>>, { group: boolean; hideOnLeave: boolean; leaveAbsolute: boolean; mode: string; origin: string; }>; leaveAbsolute: boolean; group: boolean }:
    :param active: Determines whether the messages are visible or not
    :type boolean:
    :param color: See description |v-messages_vuetify_link|.
    :type string:
    :param messages: See description |v-messages_vuetify_link|.
    :type string | string[]:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-messages", children, **kwargs)
        self._attr_names += [
            "transition",
            "active",
            "color",
            "messages",
        ]
        self._event_names += []


class VNavigationDrawer(HtmlElement):
    """
    Vuetify's v-navigation-drawer component. See more info and examples |v-navigation-drawer_vuetify_link|.

    .. |v-navigation-drawer_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-navigation-drawer" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param elevation: See description |v-navigation-drawer_vuetify_link|.
    :type string | number:
    :param name: See description |v-navigation-drawer_vuetify_link|.
    :type string:
    :param order: See description |v-navigation-drawer_vuetify_link|.
    :type string | number:
    :param absolute: See description |v-navigation-drawer_vuetify_link|.
    :type boolean:
    :param rounded: See description |v-navigation-drawer_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-navigation-drawer_vuetify_link|.
    :type string:
    :param disable_resize_watcher: Will automatically open/close drawer when resized depending if mobile or desktop.
    :type boolean:
    :param disable_route_watcher: Disables opening of navigation drawer when route changes
    :type boolean:
    :param expand_on_hover: Collapses the drawer to a **mini-variant** until hovering with the mouse
    :type boolean:
    :param floating: A floating drawer has no visible container (no border-right)
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param permanent: The drawer remains visible regardless of screen size
    :type boolean:
    :param rail: See description |v-navigation-drawer_vuetify_link|.
    :type boolean:
    :param rail_width: See description |v-navigation-drawer_vuetify_link|.
    :type string | number:
    :param scrim: See description |v-navigation-drawer_vuetify_link|.
    :type string | boolean:
    :param image: See description |v-navigation-drawer_vuetify_link|.
    :type string:
    :param temporary: A temporary drawer sits above its application and uses a scrim (overlay) to darken the background
    :type boolean:
    :param touchless: Disable mobile touch functionality
    :type boolean:
    :param width: See description |v-navigation-drawer_vuetify_link|.
    :type string | number:
    :param location: See description |v-navigation-drawer_vuetify_link|.
    :type "start" | "end" | "left" | "right" | "top" | "bottom":
    :param sticky: See description |v-navigation-drawer_vuetify_link|.
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_rail: Event that is emitted when the rail model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-navigation-drawer", children, **kwargs)
        self._attr_names += [
            "border",
            "elevation",
            "name",
            "order",
            "absolute",
            "rounded",
            "tag",
            "theme",
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
            "image",
            "temporary",
            "touchless",
            "width",
            "location",
            "sticky",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_rail", "update:rail"),
        ]


class VNoSsr(HtmlElement):
    """
    Vuetify's v-no-ssr component. See more info and examples |v-no-ssr_vuetify_link|.

    .. |v-no-ssr_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-no-ssr" target="_blank">here</a>



    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-no-ssr", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VOverlay(HtmlElement):
    """
    Vuetify's v-overlay component. See more info and examples |v-overlay_vuetify_link|.

    .. |v-overlay_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-overlay" target="_blank">here</a>


    :param activator: See description |v-overlay_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param absolute: Applies **position: absolute** to the content element.
    :type boolean:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |v-overlay_vuetify_link|.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param no_click_animation: See description |v-overlay_vuetify_link|.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param persistent: See description |v-overlay_vuetify_link|.
    :type boolean:
    :param scrim: See description |v-overlay_vuetify_link|.
    :type string | boolean:
    :param z_index: The z-index used for the component
    :type string | number:
    :param activator_props: See description |v-overlay_vuetify_link|.
    :type {  }:
    :param open_on_click: See description |v-overlay_vuetify_link|.
    :type boolean:
    :param open_on_hover: See description |v-overlay_vuetify_link|.
    :type boolean:
    :param open_on_focus: See description |v-overlay_vuetify_link|.
    :type boolean:
    :param close_on_content_click: See description |v-overlay_vuetify_link|.
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
    :param eager: See description |v-overlay_vuetify_link|.
    :type boolean:
    :param location_strategy: See description |v-overlay_vuetify_link|.
    :type "static" | "connected" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param location: Aligns the component towards the `top`, `bottom`, `right`, `left`, can be combined like for example `top right`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param origin: See description |v-overlay_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a> | "auto" | "overlap":
    :param offset: See description |v-overlay_vuetify_link|.
    :type string | number | number[]:
    :param scroll_strategy: See description |v-overlay_vuetify_link|.
    :type "none" | "close" | "block" | "reposition" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param transition: See description |v-overlay_vuetify_link|.
    :type string:
    :param attach: Specifies which DOM element that this component should detach to. String can be any valid querySelector and Object can be any valid Node. This attachs to the root `v-app` component by default
    :type string | boolean | Element:

    Events

    :param click_outside: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-overlay.json))
    :param update_modelValue: Event that is emitted when the component's model changes
    :param afterLeave: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-overlay.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-overlay", children, **kwargs)
        self._attr_names += [
            "activator",
            "absolute",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
            "persistent",
            "scrim",
            ("z_index", "zIndex"),
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
            "afterLeave",
        ]


class VPagination(HtmlElement):
    """
    Vuetify's v-pagination component. See more info and examples |v-pagination_vuetify_link|.

    .. |v-pagination_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-pagination" target="_blank">here</a>


    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param length: The number of pages
    :type string | number:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param elevation: See description |v-pagination_vuetify_link|.
    :type string | number:
    :param rounded: See description |v-pagination_vuetify_link|.
    :type string | number | boolean:
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-pagination_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":
    :param active_color: See description |v-pagination_vuetify_link|.
    :type string:
    :param start: Specify the starting page
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type number:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param total_visible: Specify the total visible pagination numbers
    :type string | number:
    :param first_icon: The icon to use for the first button
    :type string | (new () => any) | FunctionalComponent:
    :param prev_icon: The icon to use for the prev button
    :type string | (new () => any) | FunctionalComponent:
    :param next_icon: The icon to use for the next button
    :type string | (new () => any) | FunctionalComponent:
    :param last_icon: The icon to use for the last button
    :type string | (new () => any) | FunctionalComponent:
    :param aria_label: Label for the root element
    :type string:
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
    :param first: Emitted when clicking on go to first button
    :param prev: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-pagination.json))
    :param next: Emitted when clicking on go to next button
    :param last: Emitted when clicking on go to last button
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-pagination", children, **kwargs)
        self._attr_names += [
            "border",
            "length",
            "density",
            "elevation",
            "rounded",
            "size",
            "tag",
            "theme",
            "color",
            "variant",
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
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            "first",
            "prev",
            "next",
            "last",
        ]


class VParallax(HtmlElement):
    """
    Vuetify's v-parallax component. See more info and examples |v-parallax_vuetify_link|.

    .. |v-parallax_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-parallax" target="_blank">here</a>


    :param scale: See description |v-parallax_vuetify_link|.
    :type string | number:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-parallax", children, **kwargs)
        self._attr_names += [
            "scale",
        ]
        self._event_names += []


class VProgressCircular(HtmlElement):
    """
    Vuetify's v-progress-circular component. See more info and examples |v-progress-circular_vuetify_link|.

    .. |v-progress-circular_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-progress-circular" target="_blank">here</a>


    :param size: Sets the diameter of the circle in pixels
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param bg_color: See description |v-progress-circular_vuetify_link|.
    :type string:
    :param color: See description |v-progress-circular_vuetify_link|.
    :type string:
    :param model_value: The percentage value for current progress
    :type string | number:
    :param rotate: Rotates the circle start point in degrees
    :type string | number:
    :param width: Sets the stroke of the circle in pixels
    :type string | number:
    :param indeterminate: Constantly animates, use when loading progress is unknown. If set to the string `'disable-shrink'` it will use a simpler animation that does not run on the main thread.
    :type boolean | "disable-shrink":

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-progress-circular", children, **kwargs)
        self._attr_names += [
            "size",
            "tag",
            "theme",
            ("bg_color", "bgColor"),
            "color",
            ("model_value", "modelValue"),
            "rotate",
            "width",
            "indeterminate",
        ]
        self._event_names += []


class VProgressLinear(HtmlElement):
    """
    Vuetify's v-progress-linear component. See more info and examples |v-progress-linear_vuetify_link|.

    .. |v-progress-linear_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-progress-linear" target="_blank">here</a>


    :param location: See description |v-progress-linear_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param reverse: Displays reversed progress (right to left in LTR mode and left to right in RTL)
    :type boolean:
    :param rounded: See description |v-progress-linear_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param absolute: Applies position: absolute to the component
    :type boolean:
    :param active: Reduce the height to 0, hiding component
    :type boolean:
    :param bg_color: See description |v-progress-linear_vuetify_link|.
    :type string:
    :param bg_opacity: Background opacity, if null it defaults to 0.3 if background color is not specified or 1 otherwise
    :type string | number:
    :param buffer_value: The percentage value for the buffer
    :type string | number:
    :param clickable: See description |v-progress-linear_vuetify_link|.
    :type boolean:
    :param color: See description |v-progress-linear_vuetify_link|.
    :type string:
    :param height: See description |v-progress-linear_vuetify_link|.
    :type string | number:
    :param indeterminate: Constantly animates, use when loading progress is unknown.
    :type boolean:
    :param max: See description |v-progress-linear_vuetify_link|.
    :type string | number:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type string | number:
    :param stream: An alternative style for portraying loading that works in tandem with **buffer-value**
    :type boolean:
    :param striped: Adds a stripe background to the filled portion of the progress component
    :type boolean:
    :param rounded_bar: See description |v-progress-linear_vuetify_link|.
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-progress-linear", children, **kwargs)
        self._attr_names += [
            "location",
            "reverse",
            "rounded",
            "tag",
            "theme",
            "absolute",
            "active",
            ("bg_color", "bgColor"),
            ("bg_opacity", "bgOpacity"),
            ("buffer_value", "bufferValue"),
            "clickable",
            "color",
            "height",
            "indeterminate",
            "max",
            ("model_value", "modelValue"),
            "stream",
            "striped",
            ("rounded_bar", "roundedBar"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VRadio(HtmlElement):
    """
    Vuetify's v-radio component. See more info and examples |v-radio_vuetify_link|.

    .. |v-radio_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-radio" target="_blank">here</a>


    :param label: See description |v-radio_vuetify_link|.
    :type string:
    :param true_value: See description |v-radio_vuetify_link|.
    :type any:
    :param false_value: See description |v-radio_vuetify_link|.
    :type any:
    :param value: See description |v-radio_vuetify_link|.
    :type any:
    :param color: See description |v-radio_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: See description |v-radio_vuetify_link|.
    :type boolean:
    :param id: See description |v-radio_vuetify_link|.
    :type string:
    :param inline: See description |v-radio_vuetify_link|.
    :type boolean:
    :param false_icon: The icon used when inactive
    :type string | (new () => any) | FunctionalComponent:
    :param true_icon: The icon used when active
    :type string | (new () => any) | FunctionalComponent:
    :param ripple: See description |v-radio_vuetify_link|.
    :type boolean:
    :param type: See description |v-radio_vuetify_link|.
    :type string:
    :param multiple: See description |v-radio_vuetify_link|.
    :type boolean:
    :param name: Sets the component's name attribute
    :type string:
    :param readonly: See description |v-radio_vuetify_link|.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-radio", children, **kwargs)
        self._attr_names += [
            "label",
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            "disabled",
            "error",
            "id",
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "type",
            "multiple",
            "name",
            "readonly",
            ("model_value", "modelValue"),
            ("value_comparator", "valueComparator"),
            "theme",
            "density",
        ]
        self._event_names += []


class VRadioGroup(HtmlElement):
    """
    Vuetify's v-radio-group component. See more info and examples |v-radio-group_vuetify_link|.

    .. |v-radio-group_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-radio-group" target="_blank">here</a>


    :param id: See description |v-radio-group_vuetify_link|.
    :type string:
    :param append_icon: Appends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-radio-group_vuetify_link|.
    :type string | string[]:
    :param type: See description |v-radio-group_vuetify_link|.
    :type string:
    :param direction: See description |v-radio-group_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: See description |v-radio-group_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-radio-group_vuetify_link|.
    :type string | number:
    :param name: Sets the component's name attribute
    :type string:
    :param label: See description |v-radio-group_vuetify_link|.
    :type string:
    :param readonly: See description |v-radio-group_vuetify_link|.
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param validate_on: See description |v-radio-group_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-radio-group_vuetify_link|.
    :type any:
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param color: See description |v-radio-group_vuetify_link|.
    :type string:
    :param inline: Displays radio buttons in row
    :type boolean:
    :param false_icon: See description |v-radio-group_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param true_icon: See description |v-radio-group_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param ripple: See description |v-radio-group_vuetify_link|.
    :type boolean:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param height: See description |v-radio-group_vuetify_link|.
    :type string | number:

    Events

    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-radio-group.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-radio-group.json))
    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-radio-group", children, **kwargs)
        self._attr_names += [
            "id",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "type",
            "direction",
            "density",
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
            "color",
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            ("value_comparator", "valueComparator"),
            "theme",
            "height",
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_modelValue", "update:modelValue"),
        ]


class VRangeSlider(HtmlElement):
    """
    Vuetify's v-range-slider component. See more info and examples |v-range-slider_vuetify_link|.

    .. |v-range-slider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-range-slider" target="_blank">here</a>


    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param id: See description |v-range-slider_vuetify_link|.
    :type string:
    :param append_icon: Appends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-range-slider_vuetify_link|.
    :type string | string[]:
    :param direction: See description |v-range-slider_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: See description |v-range-slider_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-range-slider_vuetify_link|.
    :type string | number:
    :param name: See description |v-range-slider_vuetify_link|.
    :type string:
    :param label: See description |v-range-slider_vuetify_link|.
    :type string:
    :param readonly: See description |v-range-slider_vuetify_link|.
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type number[]:
    :param validate_on: See description |v-range-slider_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-range-slider_vuetify_link|.
    :type any:
    :param reverse: See description |v-range-slider_vuetify_link|.
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param max: See description |v-range-slider_vuetify_link|.
    :type string | number:
    :param min: See description |v-range-slider_vuetify_link|.
    :type string | number:
    :param step: See description |v-range-slider_vuetify_link|.
    :type string | number:
    :param thumb_color: See description |v-range-slider_vuetify_link|.
    :type string:
    :param thumb_label: See description |v-range-slider_vuetify_link|.
    :type boolean | "always":
    :param thumb_size: See description |v-range-slider_vuetify_link|.
    :type string | number:
    :param show_ticks: See description |v-range-slider_vuetify_link|.
    :type boolean | "always":
    :param ticks: See description |v-range-slider_vuetify_link|.
    :type number[] | Record<number, string>:
    :param tick_size: See description |v-range-slider_vuetify_link|.
    :type string | number:
    :param color: See description |v-range-slider_vuetify_link|.
    :type string:
    :param track_color: See description |v-range-slider_vuetify_link|.
    :type string:
    :param track_fill_color: See description |v-range-slider_vuetify_link|.
    :type string:
    :param track_size: See description |v-range-slider_vuetify_link|.
    :type string | number:
    :param rounded: See description |v-range-slider_vuetify_link|.
    :type string | number | boolean:
    :param elevation: See description |v-range-slider_vuetify_link|.
    :type string | number:
    :param strict: See description |v-range-slider_vuetify_link|.
    :type boolean:

    Events

    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-range-slider.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-range-slider.json))
    :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-range-slider.json))
    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-range-slider", children, **kwargs)
        self._attr_names += [
            "focused",
            "id",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "direction",
            "density",
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
            "reverse",
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
            "elevation",
            "strict",
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("update_modelValue", "update:modelValue"),
        ]


class VRating(HtmlElement):
    """
    Vuetify's v-rating component. See more info and examples |v-rating_vuetify_link|.

    .. |v-rating_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-rating" target="_blank">here</a>


    :param length: The amount of items to show
    :type string | number:
    :param name: See description |v-rating_vuetify_link|.
    :type string:
    :param active_color: See description |v-rating_vuetify_link|.
    :type string:
    :param color: See description |v-rating_vuetify_link|.
    :type string:
    :param clearable: Allows for the component to be cleared by clicking on the current value
    :type boolean:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param half_increments: Allows the selection of half increments
    :type boolean:
    :param hover: Provides visual feedback when hovering over icons
    :type boolean:
    :param readonly: Removes all hover effects and pointer events
    :type boolean:
    :param ripple: See description |v-rating_vuetify_link|.
    :type boolean:
    :param item_aria_label: See description |v-rating_vuetify_link|.
    :type string:
    :param empty_icon: The icon displayed when empty
    :type string | (new () => any) | FunctionalComponent:
    :param full_icon: The icon displayed when full
    :type string | (new () => any) | FunctionalComponent:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type string | number:
    :param item_label_position: Position of item labels. Accepts 'top' and 'bottom'.
    :type string:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param item_labels: Array of labels to display next to each item.
    :type string[]:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-rating", children, **kwargs)
        self._attr_names += [
            "length",
            "name",
            ("active_color", "activeColor"),
            "color",
            "clearable",
            "disabled",
            ("half_increments", "halfIncrements"),
            "hover",
            "readonly",
            "ripple",
            ("item_aria_label", "itemAriaLabel"),
            ("empty_icon", "emptyIcon"),
            ("full_icon", "fullIcon"),
            ("model_value", "modelValue"),
            ("item_label_position", "itemLabelPosition"),
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
    Vuetify's v-responsive component. See more info and examples |v-responsive_vuetify_link|.

    .. |v-responsive_vuetify_link| raw:: html

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
    :param aspect_ratio: Sets a base aspect ratio, calculated as width/height. This will only set a **minimum** height, the component can still grow if it has a lot of content
    :type string | number:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-responsive", children, **kwargs)
        self._attr_names += [
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            ("aspect_ratio", "aspectRatio"),
            ("content_class", "contentClass"),
        ]
        self._event_names += []


class VSelect(HtmlElement):
    """
    Vuetify's v-select component. See more info and examples |v-select_vuetify_link|.

    .. |v-select_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-select" target="_blank">here</a>


    :param label: See description |v-select_vuetify_link|.
    :type string:
    :param type: Sets input type
    :type string:
    :param chips: Changes display of selections to chips
    :type boolean:
    :param closable_chips: See description |v-select_vuetify_link|.
    :type boolean:
    :param eager: Will force the components content to render on mounted. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :type boolean:
    :param hide_no_data: See description |v-select_vuetify_link|.
    :type boolean:
    :param hide_selected: Do not display in the select menu items that are already selected
    :type boolean:
    :param menu: See description |v-select_vuetify_link|.
    :type boolean:
    :param menu_icon: See description |v-select_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param menu_props: See description |v-select_vuetify_link|.
    :type unknown:
    :param id: See description |v-select_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the input
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param reverse: See description |v-select_vuetify_link|.
    :type boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param transition: See description |v-select_vuetify_link|.
    :type string | { component: DefineComponent<{ target: PropType<HTMLElement>; }, () => JSX.Element, unknown, {}, {}, ComponentOptionsMixin, ComponentOptionsMixin, {}, string, PublicProps, Readonly<ExtractPropTypes<{ target: PropType<HTMLElement>; }>>, {}> }:
    :param name: See description |v-select_vuetify_link|.
    :type string:
    :param multiple: Changes select to multiple. Accepts array for value
    :type boolean:
    :param no_data_text: Text shown when no items are provided to the component
    :type string:
    :param open_on_clear: When using the **clearable** prop, once cleared, the select menu will either open or stay open, depending on the current state
    :type boolean:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param items: Can be an array of objects or array of strings. When using objects, will look for a title, value and disabled keys. This can be changed using the **item-title**, **item-value** and **item-disabled** props.  Objects that have a **header** or **divider** property are considered special cases and generate a list header or divider; these items are not selectable.
    :type unknown[]:
    :param item_title: See description |v-select_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_value: See description |v-select_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_children: See description |v-select_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_props: See description |v-select_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**
    :type boolean:
    :param autofocus: Enables autofocus
    :type boolean:
    :param hint: See description |v-select_vuetify_link|.
    :type string:
    :param persistent_hint: See description |v-select_vuetify_link|.
    :type boolean:
    :param prefix: Displays prefix text
    :type string:
    :param placeholder: Sets the input’s placeholder text
    :type string:
    :param persistent_placeholder: Forces placeholder to always be visible
    :type boolean:
    :param persistent_counter: See description |v-select_vuetify_link|.
    :type boolean:
    :param suffix: Displays suffix text
    :type string:
    :param append_icon: Appends an icon to the outside the component's input, uses same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-select_vuetify_link|.
    :type string | string[]:
    :param direction: See description |v-select_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param error: See description |v-select_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-select_vuetify_link|.
    :type string | number:
    :param readonly: Puts input in readonly state
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param validate_on: See description |v-select_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param bg_color: See description |v-select_vuetify_link|.
    :type string:
    :param clearable: Allows for the component to be cleared
    :type boolean:
    :param clear_icon: See description |v-select_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param color: See description |v-select_vuetify_link|.
    :type string:
    :param persistent_clear: See description |v-select_vuetify_link|.
    :type boolean:
    :param prepend_inner_icon: See description |v-select_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param single_line: Label does not move on focus/dirty
    :type boolean:
    :param variant: Applies a distinct style to the component
    :type "underlined" | "outlined" | "filled" | "solo" | "plain":
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
    :type string | boolean:
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :type string | number | true:
    :param counter_value: See description |v-select_vuetify_link|.
    :type (value: any) => number:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-select.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-select.json))
    :param click_clear: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-select.json))
    :param click_appendInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-select.json))
    :param click_prependInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-select.json))
    :param update_menu: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-select.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-select", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            "label",
            "type",
            "chips",
            ("closable_chips", "closableChips"),
            "eager",
            ("hide_no_data", "hideNoData"),
            ("hide_selected", "hideSelected"),
            "menu",
            ("menu_icon", "menuIcon"),
            ("menu_props", "menuProps"),
            "id",
            "disabled",
            ("model_value", "modelValue"),
            "reverse",
            "theme",
            "transition",
            "name",
            "multiple",
            ("no_data_text", "noDataText"),
            ("open_on_clear", "openOnClear"),
            ("value_comparator", "valueComparator"),
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            "autofocus",
            "hint",
            ("persistent_hint", "persistentHint"),
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "direction",
            "density",
            "error",
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
            "active",
            "color",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "loading",
            "counter",
            ("counter_value", "counterValue"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("update_menu", "update:menu"),
        ]


class VSelectionControl(HtmlElement):
    """
    Vuetify's v-selection-control component. See more info and examples |v-selection-control_vuetify_link|.

    .. |v-selection-control_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-selection-control" target="_blank">here</a>


    :param type: See description |v-selection-control_vuetify_link|.
    :type string:
    :param label: See description |v-selection-control_vuetify_link|.
    :type string:
    :param true_value: See description |v-selection-control_vuetify_link|.
    :type any:
    :param false_value: See description |v-selection-control_vuetify_link|.
    :type any:
    :param value: See description |v-selection-control_vuetify_link|.
    :type any:
    :param color: See description |v-selection-control_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: See description |v-selection-control_vuetify_link|.
    :type boolean:
    :param id: See description |v-selection-control_vuetify_link|.
    :type string:
    :param inline: See description |v-selection-control_vuetify_link|.
    :type boolean:
    :param false_icon: See description |v-selection-control_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param true_icon: See description |v-selection-control_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param ripple: See description |v-selection-control_vuetify_link|.
    :type boolean:
    :param multiple: See description |v-selection-control_vuetify_link|.
    :type boolean:
    :param name: See description |v-selection-control_vuetify_link|.
    :type string:
    :param readonly: See description |v-selection-control_vuetify_link|.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type unknown:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-selection-control", children, **kwargs)
        self._attr_names += [
            "type",
            "label",
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            "disabled",
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
            "theme",
            "density",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSelectionControlGroup(HtmlElement):
    """
    Vuetify's v-selection-control-group component. See more info and examples |v-selection-control-group_vuetify_link|.

    .. |v-selection-control-group_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-selection-control-group" target="_blank">here</a>


    :param color: See description |v-selection-control-group_vuetify_link|.
    :type string:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: See description |v-selection-control-group_vuetify_link|.
    :type boolean:
    :param id: See description |v-selection-control-group_vuetify_link|.
    :type string:
    :param inline: See description |v-selection-control-group_vuetify_link|.
    :type boolean:
    :param false_icon: See description |v-selection-control-group_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param true_icon: See description |v-selection-control-group_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param ripple: See description |v-selection-control-group_vuetify_link|.
    :type boolean:
    :param type: See description |v-selection-control-group_vuetify_link|.
    :type string:
    :param multiple: See description |v-selection-control-group_vuetify_link|.
    :type boolean:
    :param name: See description |v-selection-control-group_vuetify_link|.
    :type string:
    :param readonly: See description |v-selection-control-group_vuetify_link|.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param defaults_target: See description |v-selection-control-group_vuetify_link|.
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-selection-control-group", children, **kwargs)
        self._attr_names += [
            "color",
            "disabled",
            "error",
            "id",
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "type",
            "multiple",
            "name",
            "readonly",
            ("model_value", "modelValue"),
            ("value_comparator", "valueComparator"),
            "theme",
            "density",
            ("defaults_target", "defaultsTarget"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VSheet(HtmlElement):
    """
    Vuetify's v-sheet component. See more info and examples |v-sheet_vuetify_link|.

    .. |v-sheet_vuetify_link| raw:: html

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
    :param elevation: See description |v-sheet_vuetify_link|.
    :type string | number:
    :param location: See description |v-sheet_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param position: Specifies the type of positioning method used for an element. Available options are: **static**, **relative**, **fixed**, **absolute**, and **sticky**.
    :type "static" | "relative" | "fixed" | "absolute" | "sticky":
    :param rounded: See description |v-sheet_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-sheet_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-sheet", children, **kwargs)
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


class VSlideGroup(HtmlElement):
    """
    Vuetify's v-slide-group component. See more info and examples |v-slide-group_vuetify_link|.

    .. |v-slide-group_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-group" target="_blank">here</a>


    :param symbol: See description |v-slide-group_vuetify_link|.
    :type any:
    :param center_active: Forces the selected component to be centered
    :type boolean:
    :param direction: See description |v-slide-group_vuetify_link|.
    :type string:
    :param next_icon: The appended slot when arrows are shown
    :type string | (new () => any) | FunctionalComponent:
    :param prev_icon: The prepended slot when arrows are shown
    :type string | (new () => any) | FunctionalComponent:
    :param show_arrows: See description |v-slide-group_vuetify_link|.
    :type string | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param multiple: Allows one to select mulitple items.
    :type boolean:
    :param max: Sets a maximum number of selections that can be made.
    :type number:
    :param selected_class: Configure the selected CSS class.
    :type string:
    :param disabled: Puts all children components into a disabled state
    :type boolean:
    :param mandatory: Forces at least one item to always be selected (if available).
    :type boolean | "force":

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-group", children, **kwargs)
        self._attr_names += [
            "symbol",
            ("center_active", "centerActive"),
            "direction",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
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
    Vuetify's v-slide-group-item component. See more info and examples |v-slide-group-item_vuetify_link|.

    .. |v-slide-group-item_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-group-item" target="_blank">here</a>


    :param selected_class: Configure the active CSS class applied when the item is selected.
    :type string:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:

    Events

    :param group_selected: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-slide-group-item.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-group-item", children, **kwargs)
        self._attr_names += [
            ("selected_class", "selectedClass"),
            "value",
            "disabled",
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VSlider(HtmlElement):
    """
    Vuetify's v-slider component. See more info and examples |v-slider_vuetify_link|.

    .. |v-slider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slider" target="_blank">here</a>


    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: Puts the input in a manual error state
    :type boolean:
    :param readonly: Puts input in readonly state
    :type boolean:
    :param max: Sets the maximum allowed value
    :type string | number:
    :param min: Sets the minimum allowed value
    :type string | number:
    :param step: If greater than 0, sets step interval for ticks
    :type string | number:
    :param thumb_color: Sets the thumb and thumb label color
    :type string:
    :param thumb_label: Show thumb label. If `true` it shows label when using slider. If set to `'always'` it always shows label.
    :type boolean | "always":
    :param thumb_size: Controls the size of the thumb label.
    :type string | number:
    :param show_ticks: See description |v-slider_vuetify_link|.
    :type boolean | "always":
    :param ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
    :type number[] | Record<number, string>:
    :param tick_size: Controls the size of **ticks**
    :type string | number:
    :param color: See description |v-slider_vuetify_link|.
    :type string:
    :param track_color: Sets the track's color
    :type string:
    :param track_fill_color: Sets the track's fill color
    :type string:
    :param track_size: See description |v-slider_vuetify_link|.
    :type string | number:
    :param direction: See description |v-slider_vuetify_link|.
    :type "horizontal" | "vertical":
    :param reverse: See description |v-slider_vuetify_link|.
    :type boolean:
    :param rounded: See description |v-slider_vuetify_link|.
    :type string | number | boolean:
    :param elevation: See description |v-slider_vuetify_link|.
    :type string | number:
    :param id: See description |v-slider_vuetify_link|.
    :type string:
    :param append_icon: Appends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: Displays a list of messages or message if using a string
    :type string | string[]:
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-slider_vuetify_link|.
    :type string | number:
    :param name: See description |v-slider_vuetify_link|.
    :type string:
    :param label: See description |v-slider_vuetify_link|.
    :type string:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type string | number:
    :param validate_on: See description |v-slider_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-slider_vuetify_link|.
    :type any:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":

    Events

    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-slider.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-slider.json))
    :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-slider.json))
    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slider", children, **kwargs)
        self._attr_names += [
            "focused",
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
            "reverse",
            "rounded",
            "elevation",
            "id",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "density",
            ("error_messages", "errorMessages"),
            ("max_errors", "maxErrors"),
            "name",
            "label",
            "rules",
            ("model_value", "modelValue"),
            ("validate_on", "validateOn"),
            ("validation_value", "validationValue"),
            ("hide_details", "hideDetails"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("update_focused", "update:focused"),
            ("update_modelValue", "update:modelValue"),
        ]


class VSnackbar(HtmlElement):
    """
    Vuetify's v-snackbar component. See more info and examples |v-snackbar_vuetify_link|.

    .. |v-snackbar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-snackbar" target="_blank">here</a>


    :param activator: See description |v-snackbar_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param multi_line: Gives the snackbar a larger minimum height.
    :type boolean:
    :param vertical: Stacks snackbar content on top of the actions (button).
    :type boolean:
    :param timeout: Time (in milliseconds) to wait until snackbar is automatically hidden.  Use `-1` to keep open indefinitely (`0` in version < 2.3 ). It is recommended for this number to be between `4000` and `10000`. Changes to this property will reset the timeout.
    :type string | number:
    :param location: Aligns the component towards the `top`, `bottom`, `right`, `left`, can be combined like for example `top right`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param position: Specifies the type of positioning method used for an element. Available options are: **static**, **relative**, **fixed**, **absolute**, and **sticky**.
    :type "static" | "relative" | "fixed" | "absolute" | "sticky":
    :param absolute: Applies **position: absolute** to the component.
    :type boolean:
    :param rounded: See description |v-snackbar_vuetify_link|.
    :type string | number | boolean:
    :param color: See description |v-snackbar_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type "flat" | "elevated" | "tonal" | "outlined" | "text" | "plain":
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |v-snackbar_vuetify_link|.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param z_index: The z-index used for the component
    :type string | number:
    :param activator_props: See description |v-snackbar_vuetify_link|.
    :type {  }:
    :param open_on_click: See description |v-snackbar_vuetify_link|.
    :type boolean:
    :param open_on_hover: See description |v-snackbar_vuetify_link|.
    :type boolean:
    :param open_on_focus: See description |v-snackbar_vuetify_link|.
    :type boolean:
    :param close_on_content_click: See description |v-snackbar_vuetify_link|.
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
    :param eager: See description |v-snackbar_vuetify_link|.
    :type boolean:
    :param location_strategy: See description |v-snackbar_vuetify_link|.
    :type "static" | "connected" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param origin: See description |v-snackbar_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a> | "auto" | "overlap":
    :param offset: See description |v-snackbar_vuetify_link|.
    :type string | number | number[]:
    :param transition: See description |v-snackbar_vuetify_link|.
    :type string:
    :param attach: Specifies which DOM element that this component should detach to. String can be any valid querySelector and Object can be any valid Node. This attachs to the root `v-app` component by default
    :type string | boolean | Element:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-snackbar", children, **kwargs)
        self._attr_names += [
            "activator",
            ("multi_line", "multiLine"),
            "vertical",
            "timeout",
            "location",
            "position",
            "absolute",
            "rounded",
            "color",
            "variant",
            "theme",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            ("model_value", "modelValue"),
            ("z_index", "zIndex"),
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


class VSwitch(HtmlElement):
    """
    Vuetify's v-switch component. See more info and examples |v-switch_vuetify_link|.

    .. |v-switch_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-switch" target="_blank">here</a>


    :param id: See description |v-switch_vuetify_link|.
    :type string:
    :param append_icon: Appends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-switch_vuetify_link|.
    :type string | string[]:
    :param type: See description |v-switch_vuetify_link|.
    :type string:
    :param direction: See description |v-switch_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: See description |v-switch_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-switch_vuetify_link|.
    :type string | number:
    :param name: See description |v-switch_vuetify_link|.
    :type string:
    :param label: See description |v-switch_vuetify_link|.
    :type string:
    :param readonly: See description |v-switch_vuetify_link|.
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param validate_on: See description |v-switch_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-switch_vuetify_link|.
    :type any:
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param flat: Display component without elevation. Default elevation for thumb is 4dp, `flat` resets it
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param true_value: See description |v-switch_vuetify_link|.
    :type any:
    :param false_value: See description |v-switch_vuetify_link|.
    :type any:
    :param value: The input's value
    :type any:
    :param color: See description |v-switch_vuetify_link|.
    :type string:
    :param inline: See description |v-switch_vuetify_link|.
    :type boolean:
    :param false_icon: See description |v-switch_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param true_icon: See description |v-switch_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param ripple: See description |v-switch_vuetify_link|.
    :type boolean:
    :param multiple: Changes expected model to an array
    :type boolean:
    :param value_comparator: Apply a custom comparison algorithm used for values
    :type (a: any, b: any) => boolean:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param indeterminate: See description |v-switch_vuetify_link|.
    :type boolean:
    :param inset: Enlarge the `v-switch` track to encompass the thumb
    :type boolean:
    :param loading: Displays circular progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - primary, secondary, success, info, warning, error) or a Boolean which uses the component color (set by color prop - if it's supported by the component) or the primary color
    :type string | boolean:

    Events

    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-switch.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-switch.json))
    :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-switch.json))
    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_indeterminate: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-switch.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-switch", children, **kwargs)
        self._attr_names += [
            "id",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "type",
            "direction",
            "density",
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
            "flat",
            ("hide_details", "hideDetails"),
            ("true_value", "trueValue"),
            ("false_value", "falseValue"),
            "value",
            "color",
            "inline",
            ("false_icon", "falseIcon"),
            ("true_icon", "trueIcon"),
            "ripple",
            "multiple",
            ("value_comparator", "valueComparator"),
            "theme",
            "indeterminate",
            "inset",
            "loading",
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
    Vuetify's v-system-bar component. See more info and examples |v-system-bar_vuetify_link|.

    .. |v-system-bar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-system-bar" target="_blank">here</a>


    :param elevation: See description |v-system-bar_vuetify_link|.
    :type string | number:
    :param name: See description |v-system-bar_vuetify_link|.
    :type string:
    :param order: See description |v-system-bar_vuetify_link|.
    :type string | number:
    :param absolute: See description |v-system-bar_vuetify_link|.
    :type boolean:
    :param rounded: See description |v-system-bar_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param color: See description |v-system-bar_vuetify_link|.
    :type string:
    :param height: Sets the height for the component.
    :type string | number:
    :param window: Increases the system bar height to 32px (24px default).
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-system-bar", children, **kwargs)
        self._attr_names += [
            "elevation",
            "name",
            "order",
            "absolute",
            "rounded",
            "tag",
            "theme",
            "color",
            "height",
            "window",
        ]
        self._event_names += []


class VTabs(HtmlElement):
    """
    Vuetify's v-tabs component. See more info and examples |v-tabs_vuetify_link|.

    .. |v-tabs_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-tabs" target="_blank">here</a>


    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param align_tabs: See description |v-tabs_vuetify_link|.
    :type "start" | "title" | "center" | "end":
    :param color: See description |v-tabs_vuetify_link|.
    :type string:
    :param direction: Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
    :type "horizontal" | "vertical":
    :param fixed_tabs: `v-tabs-item` min-width 160px, max-width 360px
    :type boolean:
    :param items: The items to display in the component. This can be an array of strings or objects with a property `title`
    :type (string | Record<string, any>)[]:
    :param stacked: See description |v-tabs_vuetify_link|.
    :type boolean:
    :param bg_color: See description |v-tabs_vuetify_link|.
    :type string:
    :param grow: Force `v-tab`'s to take up all available space
    :type boolean:
    :param height: Sets the height of the tabs bar
    :type string | number:
    :param hide_slider: Hide's the generated `v-tabs-slider`
    :type boolean:
    :param slider_color: Changes the background color of an auto-generated `v-tabs-slider`
    :type string:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param mandatory: See description |v-tabs_vuetify_link|.
    :type boolean | "force":

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tabs", children, **kwargs)
        self._attr_names += [
            "density",
            "tag",
            ("align_tabs", "alignTabs"),
            "color",
            "direction",
            ("fixed_tabs", "fixedTabs"),
            "items",
            "stacked",
            ("bg_color", "bgColor"),
            "grow",
            "height",
            ("hide_slider", "hideSlider"),
            ("slider_color", "sliderColor"),
            ("model_value", "modelValue"),
            "mandatory",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
        ]


class VTab(HtmlElement):
    """
    Vuetify's v-tab component. See more info and examples |v-tab_vuetify_link|.

    .. |v-tab_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-tab" target="_blank">here</a>


    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param href: Designates the component as anchor and applies the **href** attribute.
    :type string:
    :param replace: See description |v-tab_vuetify_link|.
    :type boolean:
    :param exact: See description |v-tab_vuetify_link|.
    :type boolean:
    :param to: See description |v-tab_vuetify_link|.
    :type unknown:
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param selected_class: Configure the active CSS class applied when the item is selected.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param fixed: See description |v-tab_vuetify_link|.
    :type boolean:
    :param prepend_icon: See description |v-tab_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param append_icon: See description |v-tab_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param stacked: See description |v-tab_vuetify_link|.
    :type boolean:
    :param title: See description |v-tab_vuetify_link|.
    :type string:
    :param ripple: See description |v-tab_vuetify_link|.
    :type boolean:
    :param color: See description |v-tab_vuetify_link|.
    :type string:
    :param slider_color: See description |v-tab_vuetify_link|.
    :type string:
    :param hide_slider: See description |v-tab_vuetify_link|.
    :type boolean:
    :param direction: See description |v-tab_vuetify_link|.
    :type "horizontal" | "vertical":
    :param icon: See description |v-tab_vuetify_link|.
    :type boolean | string | (new () => any) | FunctionalComponent:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tab", children, **kwargs)
        self._attr_names += [
            "tag",
            "href",
            "replace",
            "exact",
            "to",
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "theme",
            "fixed",
            ("prepend_icon", "prependIcon"),
            ("append_icon", "appendIcon"),
            "stacked",
            "title",
            "ripple",
            "color",
            ("slider_color", "sliderColor"),
            ("hide_slider", "hideSlider"),
            "direction",
            "icon",
        ]
        self._event_names += []


class VTable(HtmlElement):
    """
    Vuetify's v-table component. See more info and examples |v-table_vuetify_link|.

    .. |v-table_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-table" target="_blank">here</a>


    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param fixed_header: See description |v-table_vuetify_link|.
    :type boolean:
    :param fixed_footer: See description |v-table_vuetify_link|.
    :type boolean:
    :param height: See description |v-table_vuetify_link|.
    :type string | number:
    :param hover: See description |v-table_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-table", children, **kwargs)
        self._attr_names += [
            "density",
            "tag",
            "theme",
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            "height",
            "hover",
        ]
        self._event_names += []


class VTextarea(HtmlElement):
    """
    Vuetify's v-textarea component. See more info and examples |v-textarea_vuetify_link|.

    .. |v-textarea_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-textarea" target="_blank">here</a>


    :param id: See description |v-textarea_vuetify_link|.
    :type string:
    :param append_icon: Appends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-textarea_vuetify_link|.
    :type string | string[]:
    :param direction: See description |v-textarea_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param disabled: Removes the ability to click or target the input
    :type boolean:
    :param error: See description |v-textarea_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-textarea_vuetify_link|.
    :type string | number:
    :param name: See description |v-textarea_vuetify_link|.
    :type string:
    :param label: See description |v-textarea_vuetify_link|.
    :type string:
    :param readonly: Puts input in readonly state
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param validate_on: See description |v-textarea_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-textarea_vuetify_link|.
    :type any:
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param reverse: See description |v-textarea_vuetify_link|.
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param append_inner_icon: See description |v-textarea_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param bg_color: See description |v-textarea_vuetify_link|.
    :type string:
    :param clearable: Allows for the component to be cleared
    :type boolean:
    :param clear_icon: See description |v-textarea_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param color: See description |v-textarea_vuetify_link|.
    :type string:
    :param dirty: Manually apply the dirty state styling
    :type boolean:
    :param persistent_clear: See description |v-textarea_vuetify_link|.
    :type boolean:
    :param prepend_inner_icon: See description |v-textarea_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param single_line: Label does not move on focus/dirty
    :type boolean:
    :param variant: Applies a distinct style to the component
    :type "underlined" | "outlined" | "filled" | "solo" | "plain":
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
    :type string | boolean:
    :param auto_grow: Automatically grow the textarea depending on amount of text
    :type boolean:
    :param autofocus: See description |v-textarea_vuetify_link|.
    :type boolean:
    :param hint: See description |v-textarea_vuetify_link|.
    :type string:
    :param persistent_hint: See description |v-textarea_vuetify_link|.
    :type boolean:
    :param prefix: See description |v-textarea_vuetify_link|.
    :type string:
    :param placeholder: See description |v-textarea_vuetify_link|.
    :type string:
    :param persistent_placeholder: See description |v-textarea_vuetify_link|.
    :type boolean:
    :param persistent_counter: See description |v-textarea_vuetify_link|.
    :type boolean:
    :param no_resize: Remove resize handle
    :type boolean:
    :param rows: Default row count
    :type string | number:
    :param max_rows: See description |v-textarea_vuetify_link|.
    :type string | number:
    :param suffix: See description |v-textarea_vuetify_link|.
    :type string:
    :param counter: See description |v-textarea_vuetify_link|.
    :type string | number | true:
    :param counter_value: See description |v-textarea_vuetify_link|.
    :type (value: any) => number:

    Events

    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-textarea.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-textarea.json))
    :param click_clear: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-textarea.json))
    :param click_appendInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-textarea.json))
    :param click_prependInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-textarea.json))
    :param click_control: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-textarea.json))
    :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-textarea.json))
    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-textarea", children, **kwargs)
        self._attr_names += [
            "id",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "direction",
            "density",
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
            "reverse",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "color",
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "theme",
            "loading",
            ("auto_grow", "autoGrow"),
            "autofocus",
            "hint",
            ("persistent_hint", "persistentHint"),
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            ("no_resize", "noResize"),
            "rows",
            ("max_rows", "maxRows"),
            "suffix",
            "counter",
            ("counter_value", "counterValue"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("click_control", "click:control"),
            ("update_focused", "update:focused"),
            ("update_modelValue", "update:modelValue"),
        ]


class VTextField(HtmlElement):
    """
    Vuetify's v-text-field component. See more info and examples |v-text-field_vuetify_link|.

    .. |v-text-field_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-text-field" target="_blank">here</a>


    :param label: See description |v-text-field_vuetify_link|.
    :type string:
    :param type: Sets input type
    :type string:
    :param autofocus: Enables autofocus
    :type boolean:
    :param hint: See description |v-text-field_vuetify_link|.
    :type string:
    :param persistent_hint: See description |v-text-field_vuetify_link|.
    :type boolean:
    :param prefix: Displays prefix text
    :type string:
    :param placeholder: Sets the input’s placeholder text
    :type string:
    :param persistent_placeholder: Forces placeholder to always be visible
    :type boolean:
    :param persistent_counter: See description |v-text-field_vuetify_link|.
    :type boolean:
    :param suffix: Displays suffix text
    :type string:
    :param id: See description |v-text-field_vuetify_link|.
    :type string:
    :param append_icon: Appends an icon to the outside the component's input, uses same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param prepend_icon: Prepends an icon to the outnside the component's input, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param messages: See description |v-text-field_vuetify_link|.
    :type string | string[]:
    :param direction: See description |v-text-field_vuetify_link|.
    :type "horizontal" | "vertical":
    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param disabled: Removes the ability to click or target the input
    :type boolean:
    :param error: See description |v-text-field_vuetify_link|.
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-text-field_vuetify_link|.
    :type string | number:
    :param name: See description |v-text-field_vuetify_link|.
    :type string:
    :param readonly: Puts input in readonly state
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param validate_on: See description |v-text-field_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-text-field_vuetify_link|.
    :type any:
    :param focused: Forces a focused state styling on the component.
    :type boolean:
    :param reverse: Reverses the input orientation
    :type boolean:
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display
    :type boolean | "auto":
    :param append_inner_icon: See description |v-text-field_vuetify_link|.
    :type string | (new () => any) | FunctionalComponent:
    :param bg_color: See description |v-text-field_vuetify_link|.
    :type string:
    :param clearable: Allows for the component to be cleared
    :type boolean:
    :param clear_icon: Applied when using **clearable** and the input is dirty
    :type string | (new () => any) | FunctionalComponent:
    :param active: Controls the **active** state of the item. This is typically used to highlight the component
    :type boolean:
    :param color: See description |v-text-field_vuetify_link|.
    :type string:
    :param dirty: Manually apply the dirty state styling
    :type boolean:
    :param persistent_clear: See description |v-text-field_vuetify_link|.
    :type boolean:
    :param prepend_inner_icon: Prepends an icon inside the component's input, uses the same syntax as `v-icon`
    :type string | (new () => any) | FunctionalComponent:
    :param single_line: Label does not move on focus/dirty
    :type boolean:
    :param variant: Applies a distinct style to the component
    :type "underlined" | "outlined" | "filled" | "solo" | "plain":
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color
    :type string | boolean:
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :type string | number | true:
    :param counter_value: See description |v-text-field_vuetify_link|.
    :type (value: any) => number:

    Events

    :param click_prepend: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-text-field.json))
    :param click_append: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-text-field.json))
    :param click_clear: Emitted when clearable icon clicked
    :param click_appendInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-text-field.json))
    :param click_prependInner: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-text-field.json))
    :param click_control: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-text-field.json))
    :param click_input: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-text-field.json))
    :param update_focused: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-text-field.json))
    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-text-field", children, **kwargs)
        self._attr_names += [
            "label",
            "type",
            "autofocus",
            "hint",
            ("persistent_hint", "persistentHint"),
            "prefix",
            "placeholder",
            ("persistent_placeholder", "persistentPlaceholder"),
            ("persistent_counter", "persistentCounter"),
            "suffix",
            "id",
            ("append_icon", "appendIcon"),
            ("prepend_icon", "prependIcon"),
            "messages",
            "direction",
            "density",
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
            "reverse",
            ("hide_details", "hideDetails"),
            ("append_inner_icon", "appendInnerIcon"),
            ("bg_color", "bgColor"),
            "clearable",
            ("clear_icon", "clearIcon"),
            "active",
            "color",
            "dirty",
            ("persistent_clear", "persistentClear"),
            ("prepend_inner_icon", "prependInnerIcon"),
            ("single_line", "singleLine"),
            "variant",
            "theme",
            "loading",
            "counter",
            ("counter_value", "counterValue"),
        ]
        self._event_names += [
            ("click_prepend", "click:prepend"),
            ("click_append", "click:append"),
            ("click_clear", "click:clear"),
            ("click_appendInner", "click:appendInner"),
            ("click_prependInner", "click:prependInner"),
            ("click_control", "click:control"),
            ("click_input", "click:input"),
            ("update_focused", "update:focused"),
            ("update_modelValue", "update:modelValue"),
        ]


class VThemeProvider(HtmlElement):
    """
    Vuetify's v-theme-provider component. See more info and examples |v-theme-provider_vuetify_link|.

    .. |v-theme-provider_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-theme-provider" target="_blank">here</a>


    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param with_background: See description |v-theme-provider_vuetify_link|.
    :type boolean:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-theme-provider", children, **kwargs)
        self._attr_names += [
            "theme",
            "tag",
            ("with_background", "withBackground"),
        ]
        self._event_names += []


class VTimeline(HtmlElement):
    """
    Vuetify's v-timeline component. See more info and examples |v-timeline_vuetify_link|.

    .. |v-timeline_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-timeline" target="_blank">here</a>


    :param density: Adjusts vertical spacing within the component. Available options are: **default**, **comfortable**, and **compact**.
    :type "default" | "comfortable" | "compact":
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param justify: See description |v-timeline_vuetify_link|.
    :type string:
    :param line_inset: See description |v-timeline_vuetify_link|.
    :type string | number:
    :param line_thickness: See description |v-timeline_vuetify_link|.
    :type string | number:
    :param line_color: See description |v-timeline_vuetify_link|.
    :type string:
    :param align: See description |v-timeline_vuetify_link|.
    :type "center" | "start":
    :param direction: Display timeline in a **vertical** or **horizontal** direction
    :type "vertical" | "horizontal":
    :param side: See description |v-timeline_vuetify_link|.
    :type "start" | "end":
    :param truncate_line: Truncate timeline directly at the **start** or **end** of the line, or on **both** ends
    :type "start" | "end" | "both":

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-timeline", children, **kwargs)
        self._attr_names += [
            "density",
            "tag",
            "theme",
            "justify",
            ("line_inset", "lineInset"),
            ("line_thickness", "lineThickness"),
            ("line_color", "lineColor"),
            "align",
            "direction",
            "side",
            ("truncate_line", "truncateLine"),
        ]
        self._event_names += []


class VTimelineItem(HtmlElement):
    """
    Vuetify's v-timeline-item component. See more info and examples |v-timeline-item_vuetify_link|.

    .. |v-timeline-item_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-timeline-item" target="_blank">here</a>


    :param rounded: See description |v-timeline-item_vuetify_link|.
    :type string | number | boolean:
    :param elevation: See description |v-timeline-item_vuetify_link|.
    :type string | number:
    :param size: Size of the item dot
    :type string | number:
    :param tag: Specify a custom tag used on the root element.
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
    :param dot_color: See description |v-timeline-item_vuetify_link|.
    :type string:
    :param fill_dot: Remove outer border of item dot, making the color fill the entire dot
    :type boolean:
    :param hide_dot: Hide the timeline item dot
    :type boolean:
    :param hide_opposite: Hide opposite content if it exists
    :type boolean:
    :param icon: Specify icon to display inside dot
    :type string | (new () => any) | FunctionalComponent:
    :param icon_color: Color of the icon
    :type string:
    :param line_inset: See description |v-timeline-item_vuetify_link|.
    :type string | number:
    :param density: See description |v-timeline-item_vuetify_link|.
    :type "default" | "compact":

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-timeline-item", children, **kwargs)
        self._attr_names += [
            "rounded",
            "elevation",
            "size",
            "tag",
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
            ("dot_color", "dotColor"),
            ("fill_dot", "fillDot"),
            ("hide_dot", "hideDot"),
            ("hide_opposite", "hideOpposite"),
            "icon",
            ("icon_color", "iconColor"),
            ("line_inset", "lineInset"),
            "density",
        ]
        self._event_names += []


class VToolbar(HtmlElement):
    """
    Vuetify's v-toolbar component. See more info and examples |v-toolbar_vuetify_link|.

    .. |v-toolbar_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-toolbar" target="_blank">here</a>


    :param image: See description |v-toolbar_vuetify_link|.
    :type string:
    :param title: See description |v-toolbar_vuetify_link|.
    :type string:
    :param flat: Removes the toolbar's box-shadow.
    :type boolean:
    :param absolute: Applies position: absolute to the component.
    :type boolean:
    :param collapse: Puts the toolbar into a collapsed state reducing its maximum width.
    :type boolean:
    :param color: See description |v-toolbar_vuetify_link|.
    :type string:
    :param density: See description |v-toolbar_vuetify_link|.
    :type "default" | "prominent" | "comfortable" | "compact":
    :param extended: Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop, and any of the other props that affect the height of the toolbar, e.g. **prominent**, **dense**, etc., **WITH THE EXCEPTION** of **height**.
    :type boolean:
    :param extension_height: Specify an explicit height for the `extension` slot.
    :type string | number:
    :param floating: Applies **display: inline-flex** to the component.
    :type boolean:
    :param height: Designates a specific height for the toolbar. Overrides the heights imposed by other props, e.g. **prominent**, **dense**, **extended**, etc.
    :type string | number:
    :param border: Applies border styles to component.
    :type string | number | boolean:
    :param elevation: See description |v-toolbar_vuetify_link|.
    :type string | number:
    :param rounded: See description |v-toolbar_vuetify_link|.
    :type string | number | boolean:
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-toolbar", children, **kwargs)
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
            "tag",
            "theme",
        ]
        self._event_names += []


class VToolbarTitle(HtmlElement):
    """
    Vuetify's v-toolbar-title component. See more info and examples |v-toolbar-title_vuetify_link|.

    .. |v-toolbar-title_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-toolbar-title" target="_blank">here</a>


    :param text: See description |v-toolbar-title_vuetify_link|.
    :type string:
    :param tag: Specify a custom tag used on the root element.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-toolbar-title", children, **kwargs)
        self._attr_names += [
            "text",
            "tag",
        ]
        self._event_names += []


class VToolbarItems(HtmlElement):
    """
    Vuetify's v-toolbar-items component. See more info and examples |v-toolbar-items_vuetify_link|.

    .. |v-toolbar-items_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-toolbar-items" target="_blank">here</a>


    :param color: See description |v-toolbar-items_vuetify_link|.
    :type string:
    :param variant: Applies a distinct style to the component
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-toolbar-items", children, **kwargs)
        self._attr_names += [
            "color",
            "variant",
        ]
        self._event_names += []


class VTooltip(HtmlElement):
    """
    Vuetify's v-tooltip component. See more info and examples |v-tooltip_vuetify_link|.

    .. |v-tooltip_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-tooltip" target="_blank">here</a>


    :param activator: See description |v-tooltip_vuetify_link|.
    :type string | Element | ComponentPublicInstance:
    :param id: See description |v-tooltip_vuetify_link|.
    :type string:
    :param text: See description |v-tooltip_vuetify_link|.
    :type string:
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :type boolean:
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`.
    :type boolean:
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component
    :type any:
    :param content_props: See description |v-tooltip_vuetify_link|.
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param no_click_animation: See description |v-tooltip_vuetify_link|.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type boolean:
    :param scrim: See description |v-tooltip_vuetify_link|.
    :type string | boolean:
    :param z_index: The z-index used for the component
    :type string | number:
    :param activator_props: See description |v-tooltip_vuetify_link|.
    :type {  }:
    :param open_on_click: Designates whether the tooltip should open on activator click
    :type boolean:
    :param open_on_hover: Designates whether the tooltip should open on activator hover
    :type boolean:
    :param open_on_focus: See description |v-tooltip_vuetify_link|.
    :type boolean:
    :param close_on_content_click: See description |v-tooltip_vuetify_link|.
    :type boolean:
    :param close_delay: Delay (in ms) after which menu closes (when open-on-hover prop is set to true)
    :type string | number:
    :param open_delay: Delay (in ms) after which tooltip opens (when `open-on-hover` prop is set to **true**)
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
    :param location_strategy: See description |v-tooltip_vuetify_link|.
    :type "static" | "connected" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/components/VOverlay/locationStrategies.ts#L36-L40" target="_blank">LocationStrategyFn</a>:
    :param location: Aligns the component towards the `top`, `bottom`, `right`, `left`, can be combined like for example `top right`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a>:
    :param origin: See description |v-tooltip_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/anchor.ts#L7-L13" target="_blank">Anchor</a> | "auto" | "overlap":
    :param offset: See description |v-tooltip_vuetify_link|.
    :type string | number | number[]:
    :param scroll_strategy: See description |v-tooltip_vuetify_link|.
    :type "none" | "close" | "block" | "reposition" | <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/components/VOverlay/scrollStrategies.ts#L17-L17" target="_blank">ScrollStrategyFn</a>:
    :param theme: Specify a theme for this component and all of its children
    :type string:
    :param transition: See description |v-tooltip_vuetify_link|.
    :type string | boolean:
    :param attach: Specifies which DOM element that this component should detach to. String can be any valid querySelector and Object can be any valid Node. This attachs to the root `v-app` component by default
    :type string | boolean | Element:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tooltip", children, **kwargs)
        self._attr_names += [
            "activator",
            "id",
            "text",
            ("close_on_back", "closeOnBack"),
            "contained",
            ("content_class", "contentClass"),
            ("content_props", "contentProps"),
            "disabled",
            ("no_click_animation", "noClickAnimation"),
            ("model_value", "modelValue"),
            "scrim",
            ("z_index", "zIndex"),
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


class VValidation(HtmlElement):
    """
    Vuetify's v-validation component. See more info and examples |v-validation_vuetify_link|.

    .. |v-validation_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-validation" target="_blank">here</a>


    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param error: Puts the input in a manual error state
    :type boolean:
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation
    :type string | string[]:
    :param max_errors: See description |v-validation_vuetify_link|.
    :type string | number:
    :param name: See description |v-validation_vuetify_link|.
    :type string:
    :param label: See description |v-validation_vuetify_link|.
    :type string:
    :param readonly: Puts input in readonly state
    :type boolean:
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/composables/validation.ts#L16-L20" target="_blank">ValidationRule</a>[]:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param validate_on: See description |v-validation_vuetify_link|.
    :type "blur" | "input" | "submit":
    :param validation_value: See description |v-validation_vuetify_link|.
    :type any:
    :param focused: Forces a focused state styling on the component.
    :type boolean:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-validation", children, **kwargs)
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
            ("update_modelValue", "update:modelValue"),
        ]


class VWindow(HtmlElement):
    """
    Vuetify's v-window component. See more info and examples |v-window_vuetify_link|.

    .. |v-window_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-window" target="_blank">here</a>


    :param continuous: If `true`, window will "wrap around" from the last item to the first, and from the first item to the last
    :type boolean:
    :param reverse: Reverse the normal transition direction.
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any:
    :param disabled: Removes the ability to click or target the component
    :type boolean:
    :param next_icon: Icon used for the "next" button if `show-arrows` is `true`
    :type string | (new () => any) | FunctionalComponent:
    :param prev_icon: Icon used for the "prev" button if `show-arrows` is `true`
    :type string | (new () => any) | FunctionalComponent:
    :param show_arrows: Display the "next" and "prev" buttons
    :type string | boolean:
    :param touch: Provide a custom **left** and **right** function when swiped left or right.
    :type any:
    :param direction: See description |v-window_vuetify_link|.
    :type string:
    :param selected_class: See description |v-window_vuetify_link|.
    :type string:
    :param mandatory: See description |v-window_vuetify_link|.
    :type "force":
    :param tag: Specify a custom tag used on the root element.
    :type string:
    :param theme: Specify a theme for this component and all of its children
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-window", children, **kwargs)
        self._attr_names += [
            "continuous",
            "reverse",
            ("model_value", "modelValue"),
            "disabled",
            ("next_icon", "nextIcon"),
            ("prev_icon", "prevIcon"),
            ("show_arrows", "showArrows"),
            "touch",
            "direction",
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
    Vuetify's v-window-item component. See more info and examples |v-window-item_vuetify_link|.

    .. |v-window-item_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-window-item" target="_blank">here</a>


    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :type any:
    :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method
    :type boolean:
    :param selected_class: Configure the active CSS class applied when the item is selected.
    :type string:
    :param eager: See description |v-window-item_vuetify_link|.
    :type boolean:
    :param reverse_transition: Sets the reverse transition
    :type string | boolean:
    :param transition: See description |v-window-item_vuetify_link|.
    :type string | boolean:

    Events

    :param group_selected: MISSING DESCRIPTION ([edit in github](https://github.com/vuetifyjs/vuetify/tree/next/packages/api-generator/src/locale/en/v-window-item.json))
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-window-item", children, **kwargs)
        self._attr_names += [
            "value",
            "disabled",
            ("selected_class", "selectedClass"),
            "eager",
            ("reverse_transition", "reverseTransition"),
            "transition",
        ]
        self._event_names += [
            ("group_selected", "group:selected"),
        ]


class VDialogTransition(HtmlElement):
    """
    Vuetify's v-dialog-transition component. See more info and examples |v-dialog-transition_vuetify_link|.

    .. |v-dialog-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog-transition" target="_blank">here</a>


    :param target: See description |v-dialog-transition_vuetify_link|.
    :type HTMLElement:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-dialog-transition", children, **kwargs)
        self._attr_names += [
            "target",
        ]
        self._event_names += []


class VFabTransition(HtmlElement):
    """
    Vuetify's v-fab-transition component. See more info and examples |v-fab-transition_vuetify_link|.

    .. |v-fab-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-fab-transition" target="_blank">here</a>


    :param group: See description |v-fab-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-fab-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-fab-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-fab-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-fab-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VDialogBottomTransition(HtmlElement):
    """
    Vuetify's v-dialog-bottom-transition component. See more info and examples |v-dialog-bottom-transition_vuetify_link|.

    .. |v-dialog-bottom-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog-bottom-transition" target="_blank">here</a>


    :param group: See description |v-dialog-bottom-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-dialog-bottom-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-dialog-bottom-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-dialog-bottom-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-dialog-bottom-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VDialogTopTransition(HtmlElement):
    """
    Vuetify's v-dialog-top-transition component. See more info and examples |v-dialog-top-transition_vuetify_link|.

    .. |v-dialog-top-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-dialog-top-transition" target="_blank">here</a>


    :param group: See description |v-dialog-top-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-dialog-top-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-dialog-top-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-dialog-top-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-dialog-top-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VFadeTransition(HtmlElement):
    """
    Vuetify's v-fade-transition component. See more info and examples |v-fade-transition_vuetify_link|.

    .. |v-fade-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-fade-transition" target="_blank">here</a>


    :param group: See description |v-fade-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-fade-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-fade-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-fade-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-fade-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VScaleTransition(HtmlElement):
    """
    Vuetify's v-scale-transition component. See more info and examples |v-scale-transition_vuetify_link|.

    .. |v-scale-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scale-transition" target="_blank">here</a>


    :param group: See description |v-scale-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-scale-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-scale-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-scale-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scale-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollXTransition(HtmlElement):
    """
    Vuetify's v-scroll-x-transition component. See more info and examples |v-scroll-x-transition_vuetify_link|.

    .. |v-scroll-x-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-x-transition" target="_blank">here</a>


    :param group: See description |v-scroll-x-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-scroll-x-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-scroll-x-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-scroll-x-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scroll-x-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollXReverseTransition(HtmlElement):
    """
    Vuetify's v-scroll-x-reverse-transition component. See more info and examples |v-scroll-x-reverse-transition_vuetify_link|.

    .. |v-scroll-x-reverse-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-x-reverse-transition" target="_blank">here</a>


    :param group: See description |v-scroll-x-reverse-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-scroll-x-reverse-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-scroll-x-reverse-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-scroll-x-reverse-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scroll-x-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollYTransition(HtmlElement):
    """
    Vuetify's v-scroll-y-transition component. See more info and examples |v-scroll-y-transition_vuetify_link|.

    .. |v-scroll-y-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-y-transition" target="_blank">here</a>


    :param group: See description |v-scroll-y-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-scroll-y-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-scroll-y-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-scroll-y-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scroll-y-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollYReverseTransition(HtmlElement):
    """
    Vuetify's v-scroll-y-reverse-transition component. See more info and examples |v-scroll-y-reverse-transition_vuetify_link|.

    .. |v-scroll-y-reverse-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-scroll-y-reverse-transition" target="_blank">here</a>


    :param group: See description |v-scroll-y-reverse-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-scroll-y-reverse-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-scroll-y-reverse-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-scroll-y-reverse-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scroll-y-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideXTransition(HtmlElement):
    """
    Vuetify's v-slide-x-transition component. See more info and examples |v-slide-x-transition_vuetify_link|.

    .. |v-slide-x-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-x-transition" target="_blank">here</a>


    :param group: See description |v-slide-x-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-slide-x-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-slide-x-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-slide-x-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-x-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideXReverseTransition(HtmlElement):
    """
    Vuetify's v-slide-x-reverse-transition component. See more info and examples |v-slide-x-reverse-transition_vuetify_link|.

    .. |v-slide-x-reverse-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-x-reverse-transition" target="_blank">here</a>


    :param group: See description |v-slide-x-reverse-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-slide-x-reverse-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-slide-x-reverse-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-slide-x-reverse-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-x-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideYTransition(HtmlElement):
    """
    Vuetify's v-slide-y-transition component. See more info and examples |v-slide-y-transition_vuetify_link|.

    .. |v-slide-y-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-y-transition" target="_blank">here</a>


    :param group: See description |v-slide-y-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-slide-y-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-slide-y-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-slide-y-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-y-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideYReverseTransition(HtmlElement):
    """
    Vuetify's v-slide-y-reverse-transition component. See more info and examples |v-slide-y-reverse-transition_vuetify_link|.

    .. |v-slide-y-reverse-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-slide-y-reverse-transition" target="_blank">here</a>


    :param group: See description |v-slide-y-reverse-transition_vuetify_link|.
    :type boolean:
    :param hide_on_leave: Hides the leaving element (no exit animation)
    :type boolean:
    :param leave_absolute: See description |v-slide-y-reverse-transition_vuetify_link|.
    :type boolean:
    :param mode: See description |v-slide-y-reverse-transition_vuetify_link|.
    :type string:
    :param origin: See description |v-slide-y-reverse-transition_vuetify_link|.
    :type string:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-y-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            ("hide_on_leave", "hideOnLeave"),
            ("leave_absolute", "leaveAbsolute"),
            "mode",
            "origin",
        ]
        self._event_names += []


class VExpandTransition(HtmlElement):
    """
    Vuetify's v-expand-transition component. See more info and examples |v-expand-transition_vuetify_link|.

    .. |v-expand-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expand-transition" target="_blank">here</a>


    :param mode: Sets the transition mode (does not apply to transition-group).
    :type "in-out" | "out-in" | "default":

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expand-transition", children, **kwargs)
        self._attr_names += [
            "mode",
        ]
        self._event_names += []


class VExpandXTransition(HtmlElement):
    """
    Vuetify's v-expand-x-transition component. See more info and examples |v-expand-x-transition_vuetify_link|.

    .. |v-expand-x-transition_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-expand-x-transition" target="_blank">here</a>


    :param mode: Sets the transition mode (does not apply to transition-group).
    :type "in-out" | "out-in" | "default":

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expand-x-transition", children, **kwargs)
        self._attr_names += [
            "mode",
        ]
        self._event_names += []


class VDataTable(HtmlElement):
    """
    Vuetify's v-data-table component. See more info and examples |v-data-table_vuetify_link|.

    .. |v-data-table_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-data-table" target="_blank">here</a>


    :param items: An array of strings or objects used for automatically generating children components
    :type any[]:
    :param item_title: See description |v-data-table_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_value: See description |v-data-table_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_children: See description |v-data-table_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_props: See description |v-data-table_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param return_object: See description |v-data-table_vuetify_link|.
    :type boolean:
    :param headers: An array of objects that each describe a header column. See the example below for a definition of all properties
    :type { key: string; value: <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>; title: string; colspan: number; rowspan: number; fixed: boolean; align: "start" | "end"; width: number; minWidth: string; maxWidth: string; sortable: boolean; sort: (a: any, b: any) => number }[] | DataTableHeader[][]:
    :param hide_no_data: MISSING DESCRIPTION
    :type boolean:
    :param no_data_text: Text shown when no items are provided to the component
    :type string:
    :param height: Set an explicit height of table
    :type string | number:
    :param width: Sets the width for the component
    :type string | number:
    :param fixed_header: Fixed header to top of table
    :type boolean:
    :param fixed_footer: MISSING DESCRIPTION
    :type boolean:
    :param expand_on_click: MISSING DESCRIPTION
    :type boolean:
    :param show_expand: Shows the expand toggle in default rows
    :type boolean:
    :param expanded: MISSING DESCRIPTION
    :type string[]:
    :param group_by: Changes which item property should be used for grouping items. Currently only supports a single grouping in the format: `group` or `['group']`. When using an array, only the first element is considered. Can be used with `.sync` modifier
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L27-L27" target="_blank">SortItem</a>[]:
    :param show_select: Shows the select checkboxes in both the header and rows (if using default rows)
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any[]:
    :param sort_by: Changes which item property (or properties) should be used for sort order. Can be used with `.sync` modifier
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L27-L27" target="_blank">SortItem</a>[]:
    :param multi_sort: If `true` then one can sort on multiple properties
    :type boolean:
    :param must_sort: If `true` then one can not disable sorting, it will always switch between ascending and descending
    :type boolean:
    :param page: The current displayed page number (1-indexed)
    :type string | number:
    :param items_per_page: Changes how many items per page should be visible. Can be used with `.sync` modifier. Setting this prop to `-1` will display all items on the page
    :type string | number:
    :param filter_mode: See description |v-data-table_vuetify_link|.
    :type "every" | "some" | "union" | "intersection":
    :param no_filter: See description |v-data-table_vuetify_link|.
    :type boolean:
    :param custom_filter: Function to filter items
    :type (value: string, query: string, item: any) => number | boolean | [number, number] | [number, number][]:
    :param custom_key_filter: See description |v-data-table_vuetify_link|.
    :type {  }:
    :param filter_keys: See description |v-data-table_vuetify_link|.
    :type string | string[]:
    :param search: Text input used to filter items
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_page: Emits when the **page** property of the **options** prop is updated
    :param update_itemsPerPage: MISSING DESCRIPTION
    :param update_sortBy: MISSING DESCRIPTION
    :param update_options: Emits when one of the **options** properties is updated
    :param update_groupBy: MISSING DESCRIPTION
    :param update_expanded: MISSING DESCRIPTION
    :param click_row: Emits when a table row is clicked. This event provides 2 arguments: the first is the item data that was clicked and the second is the other related data provided by the `item` slot. **NOTE:** will not emit when table rows are defined through a slot such as `item` or `body`.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-data-table", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            "headers",
            ("hide_no_data", "hideNoData"),
            ("no_data_text", "noDataText"),
            "height",
            "width",
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("group_by", "groupBy"),
            ("show_select", "showSelect"),
            ("model_value", "modelValue"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            "page",
            ("items_per_page", "itemsPerPage"),
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            "search",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_groupBy", "update:groupBy"),
            ("update_expanded", "update:expanded"),
            ("click_row", "click:row"),
        ]


class VDataTableRows(HtmlElement):
    """
    Vuetify's v-data-table-rows component. See more info and examples |v-data-table-rows_vuetify_link|.

    .. |v-data-table-rows_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-data-table-rows" target="_blank">here</a>


    :param loading: MISSING DESCRIPTION
    :type string | boolean:
    :param loading_text: MISSING DESCRIPTION
    :type string:
    :param hide_no_data: MISSING DESCRIPTION
    :type boolean:
    :param items: An array of strings or objects used for automatically generating children components
    :type (DataTableItem | GroupHeaderItem)[]:
    :param no_data_text: Text shown when no items are provided to the component
    :type string:
    :param row_height: MISSING DESCRIPTION
    :type number:

    Events

    :param click_row: MISSING DESCRIPTION
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-data-table-rows", children, **kwargs)
        self._attr_names += [
            "loading",
            ("loading_text", "loadingText"),
            ("hide_no_data", "hideNoData"),
            "items",
            ("no_data_text", "noDataText"),
            ("row_height", "rowHeight"),
        ]
        self._event_names += [
            ("click_row", "click:row"),
        ]


class VDataTableRow(HtmlElement):
    """
    Vuetify's v-data-table-row component. See more info and examples |v-data-table-row_vuetify_link|.

    .. |v-data-table-row_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-data-table-row" target="_blank">here</a>


    :param item: MISSING DESCRIPTION
    :type { title: string; value: any; props: { title: string; value: any }; children: InternalItem<any>[]; raw: any } & { type: "item"; columns: Record<string, unknown> }:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-data-table-row", children, **kwargs)
        self._attr_names += [
            "item",
        ]
        self._event_names += []


class VDataTableVirtual(HtmlElement):
    """
    Vuetify's v-data-table-virtual component. See more info and examples |v-data-table-virtual_vuetify_link|.

    .. |v-data-table-virtual_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-data-table-virtual" target="_blank">here</a>


    :param items: An array of strings or objects used for automatically generating children components
    :type any[]:
    :param item_title: See description |v-data-table-virtual_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_value: See description |v-data-table-virtual_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_children: See description |v-data-table-virtual_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_props: See description |v-data-table-virtual_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param return_object: See description |v-data-table-virtual_vuetify_link|.
    :type boolean:
    :param headers: Array of header items to display
    :type { key: string; value: <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>; title: string; colspan: number; rowspan: number; fixed: boolean; align: "start" | "end"; width: number; minWidth: string; maxWidth: string; sortable: boolean; sort: (a: any, b: any) => number }[] | DataTableHeader[][]:
    :param hide_no_data: MISSING DESCRIPTION
    :type boolean:
    :param no_data_text: Text shown when no items are provided to the component
    :type string:
    :param height: Set an explicit height of table
    :type string | number:
    :param width: Sets the width for the component
    :type string | number:
    :param fixed_header: Fixed header to top of table
    :type boolean:
    :param fixed_footer: MISSING DESCRIPTION
    :type boolean:
    :param group_by: Changes which item property should be used for grouping items. Currently only supports a single grouping in the format: `group` or `['group']`. When using an array, only the first element is considered. Can be used with `.sync` modifier
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L27-L27" target="_blank">SortItem</a>[]:
    :param expand_on_click: MISSING DESCRIPTION
    :type boolean:
    :param show_expand: Shows the expand toggle in default rows
    :type boolean:
    :param expanded: MISSING DESCRIPTION
    :type string[]:
    :param show_select: Shows the select checkboxes in both the header and rows (if using default rows)
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any[]:
    :param sort_by: Changes which item property (or properties) should be used for sort order. Can be used with `.sync` modifier
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L27-L27" target="_blank">SortItem</a>[]:
    :param multi_sort: If `true` then one can sort on multiple properties
    :type boolean:
    :param must_sort: If `true` then one can not disable sorting, it will always switch between ascending and descending
    :type boolean:
    :param visible_items: MISSING DESCRIPTION
    :type string | number:
    :param item_height: MISSING DESCRIPTION
    :type string | number:
    :param filter_mode: See description |v-data-table-virtual_vuetify_link|.
    :type "every" | "some" | "union" | "intersection":
    :param no_filter: See description |v-data-table-virtual_vuetify_link|.
    :type boolean:
    :param custom_filter: Function to filter items
    :type (value: string, query: string, item: any) => number | boolean | [number, number] | [number, number][]:
    :param custom_key_filter: See description |v-data-table-virtual_vuetify_link|.
    :type {  }:
    :param filter_keys: See description |v-data-table-virtual_vuetify_link|.
    :type string | string[]:
    :param search: Text input used to filter items
    :type string:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_sortBy: MISSING DESCRIPTION
    :param update_options: Emits when one of the **options** properties is updated
    :param update_groupBy: MISSING DESCRIPTION
    :param update_expanded: MISSING DESCRIPTION
    :param click_row: Emits when a table row is clicked. This event provides 2 arguments: the first is the item data that was clicked and the second is the other related data provided by the `item` slot. **NOTE:** will not emit when table rows are defined through a slot such as `item` or `body`.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-data-table-virtual", children, **kwargs)
        self._attr_names += [
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            "headers",
            ("hide_no_data", "hideNoData"),
            ("no_data_text", "noDataText"),
            "height",
            "width",
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            ("group_by", "groupBy"),
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("show_select", "showSelect"),
            ("model_value", "modelValue"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            ("visible_items", "visibleItems"),
            ("item_height", "itemHeight"),
            ("filter_mode", "filterMode"),
            ("no_filter", "noFilter"),
            ("custom_filter", "customFilter"),
            ("custom_key_filter", "customKeyFilter"),
            ("filter_keys", "filterKeys"),
            "search",
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_groupBy", "update:groupBy"),
            ("update_expanded", "update:expanded"),
            ("click_row", "click:row"),
        ]


class VDataTableServer(HtmlElement):
    """
    Vuetify's v-data-table-server component. See more info and examples |v-data-table-server_vuetify_link|.

    .. |v-data-table-server_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-data-table-server" target="_blank">here</a>


    :param items: An array of strings or objects used for automatically generating children components
    :type any[]:
    :param item_title: See description |v-data-table-server_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_value: See description |v-data-table-server_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_children: See description |v-data-table-server_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param item_props: See description |v-data-table-server_vuetify_link|.
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>:
    :param return_object: See description |v-data-table-server_vuetify_link|.
    :type boolean:
    :param headers: Array of header items to display
    :type { key: string; value: <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/util/helpers.ts#L71-L75" target="_blank">SelectItemKey</a>; title: string; colspan: number; rowspan: number; fixed: boolean; align: "start" | "end"; width: number; minWidth: string; maxWidth: string; sortable: boolean; sort: (a: any, b: any) => number }[] | DataTableHeader[][]:
    :param hide_no_data: MISSING DESCRIPTION
    :type boolean:
    :param no_data_text: Text shown when no items are provided to the component
    :type string:
    :param height: Set an explicit height of table
    :type string | number:
    :param width: Sets the width for the component
    :type string | number:
    :param fixed_header: Fixed header to top of table
    :type boolean:
    :param fixed_footer: MISSING DESCRIPTION
    :type boolean:
    :param expand_on_click: MISSING DESCRIPTION
    :type boolean:
    :param show_expand: Shows the expand toggle in default rows
    :type boolean:
    :param expanded: MISSING DESCRIPTION
    :type string[]:
    :param show_select: Shows the select checkboxes in both the header and rows (if using default rows)
    :type boolean:
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array
    :type any[]:
    :param sort_by: Changes which item property (or properties) should be used for sort order. Can be used with `.sync` modifier
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L27-L27" target="_blank">SortItem</a>[]:
    :param multi_sort: If `true` then one can sort on multiple properties
    :type boolean:
    :param must_sort: If `true` then one can not disable sorting, it will always switch between ascending and descending
    :type boolean:
    :param page: The current displayed page number (1-indexed)
    :type string | number:
    :param items_per_page: Changes how many items per page should be visible. Can be used with `.sync` modifier. Setting this prop to `-1` will display all items on the page
    :type string | number:
    :param group_by: Changes which item property should be used for grouping items. Currently only supports a single grouping in the format: `group` or `['group']`. When using an array, only the first element is considered. Can be used with `.sync` modifier
    :type <a href="https://github.com/vuetifyjs/vuetify/blob/next/packages/vuetify/src/labs/VDataTable/composables/sort.ts#L27-L27" target="_blank">SortItem</a>[]:
    :param color: See description |v-data-table-server_vuetify_link|.
    :type string:
    :param loading: MISSING DESCRIPTION
    :type string | boolean:
    :param loading_text: MISSING DESCRIPTION
    :type string:
    :param items_length: MISSING DESCRIPTION
    :type string | number:

    Events

    :param update_modelValue: Event that is emitted when the component's model changes
    :param update_page: Emits when the **page** property of the **options** prop is updated
    :param update_itemsPerPage: MISSING DESCRIPTION
    :param update_sortBy: MISSING DESCRIPTION
    :param update_options: Emits when one of the **options** properties is updated
    :param update_expanded: MISSING DESCRIPTION
    :param update_groupBy: MISSING DESCRIPTION
    :param click_row: Emits when a table row is clicked. This event provides 2 arguments: the first is the item data that was clicked and the second is the other related data provided by the `item` slot. **NOTE:** will not emit when table rows are defined through a slot such as `item` or `body`.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-data-table-server", children, **kwargs)
        self._attr_names += [
            "items",
            ("item_title", "itemTitle"),
            ("item_value", "itemValue"),
            ("item_children", "itemChildren"),
            ("item_props", "itemProps"),
            ("return_object", "returnObject"),
            "headers",
            ("hide_no_data", "hideNoData"),
            ("no_data_text", "noDataText"),
            "height",
            "width",
            ("fixed_header", "fixedHeader"),
            ("fixed_footer", "fixedFooter"),
            ("expand_on_click", "expandOnClick"),
            ("show_expand", "showExpand"),
            "expanded",
            ("show_select", "showSelect"),
            ("model_value", "modelValue"),
            ("sort_by", "sortBy"),
            ("multi_sort", "multiSort"),
            ("must_sort", "mustSort"),
            "page",
            ("items_per_page", "itemsPerPage"),
            ("group_by", "groupBy"),
            "color",
            "loading",
            ("loading_text", "loadingText"),
            ("items_length", "itemsLength"),
        ]
        self._event_names += [
            ("update_modelValue", "update:modelValue"),
            ("update_page", "update:page"),
            ("update_itemsPerPage", "update:itemsPerPage"),
            ("update_sortBy", "update:sortBy"),
            ("update_options", "update:options"),
            ("update_expanded", "update:expanded"),
            ("update_groupBy", "update:groupBy"),
            ("click_row", "click:row"),
        ]


class VVirtualScroll(HtmlElement):
    """
    Vuetify's v-virtual-scroll component. See more info and examples |v-virtual-scroll_vuetify_link|.

    .. |v-virtual-scroll_vuetify_link| raw:: html

        <a href="https://vuetifyjs.com/api/v-virtual-scroll" target="_blank">here</a>


    :param items: The array of items to display
    :type unknown[]:
    :param item_key: Required when using **dynamic-item-height** together with object items. Should point to a property with a unique value for each item.
    :type string:
    :param item_height: Height in pixels of each item to display. When using **dynamic-item-height** this should be an average initial size.
    :type string | number:
    :param visible_items: MISSING DESCRIPTION
    :type string | number:
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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-virtual-scroll", children, **kwargs)
        self._attr_names += [
            "items",
            ("item_key", "itemKey"),
            ("item_height", "itemHeight"),
            ("visible_items", "visibleItems"),
            "height",
            ("max_height", "maxHeight"),
            ("max_width", "maxWidth"),
            ("min_height", "minHeight"),
            ("min_width", "minWidth"),
            "width",
        ]
        self._event_names += []
