##########################################################
# DO NOT EDIT: GENERATED FILE
# => instead run: $ROOT/vue-components/generate_python.py
##########################################################

from trame_client.widgets.core import AbstractElement, Template  # noqa
from trame_vuetify.module import vue2


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(vue2)


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
    "action",
    "actions",
    "activator",
    "append",
    "append-item",
    "append-outer",
    "appendIcon",
    "badge",
    "body",
    "body.append",
    "body.prepend",
    "category",
    "close",
    "counter",
    "day",
    "day-body",
    "day-header",
    "day-label",
    "day-label-header",
    "day-month",
    "default",
    "divider",
    "event",
    "expanded-item",
    "extension",
    "foot",
    "footer",
    "footer.page-text",
    "footer.prepend",
    "group",
    "group.header",
    "group.summary",
    "header",
    "header.<name>",
    "header.data-table-select",
    "icon",
    "img",
    "input",
    "interval",
    "item",
    "item.<name>",
    "item.data-table-expand",
    "item.data-table-select",
    "label",
    "loader",
    "loading",
    "message",
    "next",
    "no-data",
    "no-results",
    "opposite",
    "page-text",
    "placeholder",
    "prepend",
    "prepend-inner",
    "prepend-item",
    "prependIcon",
    "prev",
    "progress",
    "selection",
    "thumb-label",
    "top",
]
Template.slot_names.update(slot_names)


__all__ = [
    "Template",
    "VAlert",
    "VApp",
    "VAppBar",
    "VAppBarNavIcon",
    "VAppBarTitle",
    "VAutocomplete",
    "VAvatar",
    "VBadge",
    "VBanner",
    "VBottomNavigation",
    "VBottomSheet",
    "VBreadcrumbs",
    "VBreadcrumbsDivider",
    "VBreadcrumbsItem",
    "VBtn",
    "VBtnToggle",
    "VCalendar",
    "VCalendarDaily",
    "VCalendarMonthly",
    "VCalendarWeekly",
    "VCard",
    "VCardActions",
    "VCardSubtitle",
    "VCardText",
    "VCardTitle",
    "VCarousel",
    "VCarouselItem",
    "VCarouselReverseTransition",
    "VCarouselTransition",
    "VCheckbox",
    "VChip",
    "VChipGroup",
    "VCol",
    "VColorPicker",
    "VCombobox",
    "VContainer",
    "VContent",
    "VDataFooter",
    "VDataIterator",
    "VDataTable",
    "VDataTableHeader",
    "VDatePicker",
    "VDialog",
    "VDialogBottomTransition",
    "VDialogTopTransition",
    "VDialogTransition",
    "VDivider",
    "VEditDialog",
    "VExpandTransition",
    "VExpandXTransition",
    "VExpansionPanel",
    "VExpansionPanelContent",
    "VExpansionPanelHeader",
    "VExpansionPanels",
    "VFabTransition",
    "VFadeTransition",
    "VFileInput",
    "VFlex",
    "VFooter",
    "VForm",
    "VHover",
    "VIcon",
    "VImg",
    "VInput",
    "VItem",
    "VItemGroup",
    "VLayout",
    "VLazy",
    "VList",
    "VListGroup",
    "VListItem",
    "VListItemAction",
    "VListItemActionText",
    "VListItemAvatar",
    "VListItemContent",
    "VListItemGroup",
    "VListItemIcon",
    "VListItemSubtitle",
    "VListItemTitle",
    "VMain",
    "VMenu",
    "VMenuTransition",
    "VNavigationDrawer",
    "VOtpInput",
    "VOverflowBtn",
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
    "VSheet",
    "VSimpleCheckbox",
    "VSimpleTable",
    "VSkeletonLoader",
    "VSlideGroup",
    "VSlideItem",
    "VSlideXReverseTransition",
    "VSlideXTransition",
    "VSlideYReverseTransition",
    "VSlideYTransition",
    "VSlider",
    "VSnackbar",
    "VSpacer",
    "VSparkline",
    "VSpeedDial",
    "VStepper",
    "VStepperContent",
    "VStepperHeader",
    "VStepperItems",
    "VStepperStep",
    "VSubheader",
    "VSwitch",
    "VSystemBar",
    "VTab",
    "VTabItem",
    "VTabReverseTransition",
    "VTabTransition",
    "VTabs",
    "VTabsItems",
    "VTabsSlider",
    "VTextField",
    "VTextarea",
    "VThemeProvider",
    "VTimePicker",
    "VTimeline",
    "VTimelineItem",
    "VToolbar",
    "VToolbarItems",
    "VToolbarTitle",
    "VTooltip",
    "VTreeview",
    "VVirtualScroll",
    "VWindow",
    "VWindowItem",
    "dataframe_to_grid",
]


class VApp(HtmlElement):
    """
    Vuetify's VApp component.
    See more `info and examples <https://vuetifyjs.com/api/v-app>`_.

    Args:
      id (string):
        Sets the DOM id on the component
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-app", children, **kwargs)
        self._attr_names += [
            "id",
        ]
        self._event_names += []


class VAppBar(HtmlElement):
    """
    Vuetify's VAppBar component.
    See more `info and examples <https://vuetifyjs.com/api/v-app-bar>`_.

    Args:
      absolute (boolean):
        Applies position: absolute to the component.
      app (boolean):
        Designates the component as part of the application layout. Used
        for dynamically adjusting content sizing. Components using this
        prop should reside **outside** of `v-main` component to function
        properly. You can find more information about layouts on the
        `application page </components/application>`_. **Note:** this
        prop automatically applies **position: fixed** to the layout
        element. You can overwrite this functionality by using the `absolute`
        prop
      bottom (boolean):
        Aligns the component towards the bottom.
      clipped_left (boolean):
        Designates that the application's `v-navigation-drawer` that
        is positioned on the left is below the app-bar.
      clipped_right (boolean):
        Designates that the application's `v-navigation-drawer` that
        is positioned on the right is below the app-bar.
      collapse (boolean):
        Puts the toolbar into a collapsed state reducing its maximum width.
      collapse_on_scroll (boolean):
        Puts the app-bar into a collapsed state when scrolling.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the height of the toolbar content to 48px (96px when
        using the **prominent** prop).
      elevate_on_scroll (boolean):
        Elevates the app-bar when scrolling.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      extended (boolean):
        Use this prop to increase the height of the toolbar _without_
        using the `extension` slot for adding content. May be used in
        conjunction with the **extension-height** prop, and any of the
        other props that affect the height of the toolbar, e.g. **prominent**,
        **dense**, etc., **WITH THE EXCEPTION** of **height**.
      extension_height (['number', 'string']):
        Specify an explicit height for the `extension` slot.
      fade_img_on_scroll (boolean):
        When using the **src** prop or `img` slot, will fade the image when scrolling.
      fixed (boolean):
        Applies **position: fixed** to the component.
      flat (boolean):
        Removes the toolbar's box-shadow.
      floating (boolean):
        Applies **display: inline-flex** to the component.
      height (['number', 'string']):
        Designates a specific height for the toolbar. Overrides the heights
        imposed by other props, e.g. **prominent**, **dense**, **extended**,
        etc.
      hide_on_scroll (boolean):
        Hides the app-bar when scrolling. Will still show the `extension` slot.
      inverted_scroll (boolean):
        Hides the app-bar when scrolling down and displays it when scrolling up.
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      outlined (boolean):
        Removes elevation (box-shadow) and adds a *thin* border.
      prominent (boolean):
        Increases the height of the toolbar content to 128px.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      scroll_off_screen (boolean):
        Hides the app-bar when scrolling. Will **NOT** show the `extension` slot.
      scroll_target (string):
        Designates the element to target for scrolling events. Uses `window` by default.
      scroll_threshold (['string', 'number']):
        The amount of scroll distance down before **hide-on-scroll** activates.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      short (boolean):
        Reduce the height of the toolbar content to 56px (112px when
        using the **prominent** prop).
      shrink_on_scroll (boolean):
        Shrinks a **prominent** toolbar to a **dense** or **short** (default)
        one when scrolling.
      src (['string', 'object']):
        Image source. See `v-img` for details
      tag (string):
        Specify a custom tag used on the root element.
      tile (boolean):
        Removes the component's **border-radius**.
      value (boolean):
        Controls whether the component is visible or hidden.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-app-bar", children, **kwargs)
        self._attr_names += [
            "absolute",
            "app",
            "bottom",
            "clipped_left",
            "clipped_right",
            "collapse",
            "collapse_on_scroll",
            "color",
            "dark",
            "dense",
            "elevate_on_scroll",
            "elevation",
            "extended",
            "extension_height",
            "fade_img_on_scroll",
            "fixed",
            "flat",
            "floating",
            "height",
            "hide_on_scroll",
            "inverted_scroll",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "outlined",
            "prominent",
            "rounded",
            "scroll_off_screen",
            "scroll_target",
            "scroll_threshold",
            "shaped",
            "short",
            "shrink_on_scroll",
            "src",
            "tag",
            "tile",
            "value",
            "width",
        ]
        self._event_names += []


class VAppBarNavIcon(HtmlElement):
    """
    Vuetify's VAppBarNavIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-app-bar-nav-icon>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-app-bar-nav-icon", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VAppBarTitle(HtmlElement):
    """
    Vuetify's VAppBarTitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-app-bar-title>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-app-bar-title", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VAlert(HtmlElement):
    """
    Vuetify's VAlert component.
    See more `info and examples <https://vuetifyjs.com/api/v-alert>`_.

    Args:
      border (string):
        Puts a border on the alert. Accepts **top** | **right** | **bottom** | **left**.
      close_icon (string):
        Change the default icon used for **dismissible** alerts.
      close_label (string):
        Text used for *aria-label* on **dismissible** alerts. Can also
        be customizing globally in `Internationalization </customization/internationalization>`_.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      colored_border (boolean):
        Applies the defined **color** to the alert's border.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Decreases component's height.
      dismissible (boolean):
        Adds a close icon that can hide the alert.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      height (['number', 'string']):
        Sets the height for the component.
      icon (['boolean', 'string']):
        Designates a specific icon.
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
      outlined (boolean):
        Makes the background transparent and applies a thin border.
      prominent (boolean):
        Displays a larger vertically centered icon to draw more attention.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      tag (string):
        Specify a custom tag used on the root element.
      text (boolean):
        Applies the defined **color** to text and a low opacity background of the same.
      tile (boolean):
        Removes the component's border-radius.
      transition (string):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      type (string):
        Specify a **success**, **info**, **warning** or **error** alert.
        Uses the contextual color and has a pre-defined icon.
      value (boolean):
        Controls whether the component is visible or hidden.
      width (['number', 'string']):
        Sets the width for the component.
      input (event):
        The updated bound model
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-alert", children, **kwargs)
        self._attr_names += [
            "border",
            "close_icon",
            "close_label",
            "color",
            "colored_border",
            "dark",
            "dense",
            "dismissible",
            "elevation",
            "height",
            "icon",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "mode",
            "origin",
            "outlined",
            "prominent",
            "rounded",
            "shaped",
            "tag",
            "text",
            "tile",
            "transition",
            "type",
            "value",
            "width",
        ]
        self._event_names += [
            "input",
        ]


class VAutocomplete(HtmlElement):
    """
    Vuetify's VAutocomplete component.
    See more `info and examples <https://vuetifyjs.com/api/v-autocomplete>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      append_outer_icon (string):
        Appends an icon to the outside the component's input, uses same
        syntax as `v-icon`
      attach (any):
        Specifies which DOM element that this component should detach
        to. String can be any valid querySelector and Object can be any
        valid Node. This will attach to the root `v-app` component by
        default.
      auto_select_first (boolean):
        When searching, will always highlight the first option
      autofocus (boolean):
        Enables autofocus
      background_color (string):
        Changes the background-color of the input
      cache_items (boolean):
        Keeps a local _unique_ copy of all items that have been passed
        through the **items** prop.
      chips (boolean):
        Changes display of selections to chips
      clear_icon (string):
        Applied when using **clearable** and the input is dirty
      clearable (boolean):
        Add input clear functionality, default icon is Material Design
        Icons **mdi-clear**
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      counter (['boolean', 'number', 'string']):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      counter_value (function):

      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      deletable_chips (boolean):
        Adds a remove icon to selected chips
      dense (boolean):
        Reduces the input height
      disable_lookup (boolean):
        Disables keyboard lookup
      disabled (boolean):
        Disables the input
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      filled (boolean):
        Applies the alternate filled input style
      filter (function):
        The filtering algorithm used when searching. `example <https://github.com/vuetifyjs/vuetify/blob/v2-stable/packages/vuetify/src/components/VAutocomplete/VAutocomplete.ts#L40>`_
      flat (boolean):
        Removes elevation (shadow) added to element when using the **solo**
        or **solo-inverted** props
      full_width (boolean):
        Designates input type as full-width
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      hide_selected (boolean):
        Do not display in the select menu items that are already selected.
        Also removes checkboxes from the list when multiple
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      item_color (string):
        Sets color of selected items
      item_disabled (['string', 'array', 'function']):
        Set property of **items**'s disabled value
      item_text (['string', 'array', 'function']):
        Set property of **items**'s text value
      item_value (['string', 'array', 'function']):
        Set property of **items**'s value - **must be primitive**. Dot
        notation is supported. **Note:** This is currently not supported
        with `v-combobox` `GitHub Issue <https://github.com/vuetifyjs/vuetify/issues/5479>`_
      items (array):
        Can be an array of objects or array of strings. When using objects,
        will look for a text, value and disabled keys. This can be changed
        using the **item-text**, **item-value** and **item-disabled**
        props.  Objects that have a **header** or **divider** property
        are considered special cases and generate a list header or divider;
        these items are not selectable.
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      menu_props (['string', 'array', 'object']):
        Pass props through to the `v-menu` component. Accepts either
        a string for boolean props `menu-props="auto, overflowY"`, or
        an object `:menu-props="{ auto: true, overflowY: true }"`
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      multiple (boolean):
        Changes select to multiple. Accepts array for value
      no_data_text (string):
        Display text when there is no data
      no_filter (boolean):
        Do not apply filtering when searching. Useful when data is being
        filtered server side
      open_on_clear (boolean):
        When using the **clearable** prop, once cleared, the select menu
        will either open or stay open, depending on the current state
      outlined (boolean):
        Applies the outlined style to the input
      persistent_hint (boolean):
        Forces hint to always be visible
      persistent_placeholder (boolean):
        Forces placeholder to always be visible
      placeholder (string):
        Sets the input's placeholder text
      prefix (string):
        Displays prefix text
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      prepend_inner_icon (string):
        Prepends an icon inside the component's input, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**
      reverse (boolean):
        Reverses the input orientation
      rounded (boolean):
        Adds a border radius to the input
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      search_input (string):
        Search value. Can be used with `.sync` modifier.
      shaped (boolean):
        Round if `outlined` and increase `border-radius` if `filled`.
        Must be used with either `outlined` or `filled`
      single_line (boolean):
        Label does not move on focus/dirty
      small_chips (boolean):
        Changes display of selections to chips with the **small** property
      solo (boolean):
        Changes the style of the input
      solo_inverted (boolean):
        Reduces element opacity until focused
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      suffix (string):
        Displays suffix text
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      value_comparator (function):
        The comparison algorithm used for values. `More info <https://github.com/vuetifyjs/vuetify/blob/v2-stable/packages/vuetify/src/util/helpers.ts>`_
      blur (event):
        Emitted when the input is blurred
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_append-outer (event):
        Emitted when appended outer icon is clicked
      click_clear (event):
        Emitted when clearable icon clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      click_prepend-inner (event):
        Emitted when prepended inner icon is clicked
      focus (event):
        Emitted when component is focused
      input (event):
        The updated bound model
      keydown (event):
        Emitted when **any** key is pressed
      update_error (event):
        The `error.sync` event
      update_list-index (event):
        Emitted when menu item is selected using keyboard arrows
      update_search-input (event):
        The `search-input.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-autocomplete", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "append_outer_icon",
            "attach",
            "auto_select_first",
            "autofocus",
            "background_color",
            "cache_items",
            "chips",
            "clear_icon",
            "clearable",
            "color",
            "counter",
            "counter_value",  # JS functions unimplemented
            "dark",
            "deletable_chips",
            "dense",
            "disable_lookup",
            "disabled",
            "eager",
            "error",
            "error_count",
            "error_messages",
            "filled",
            "filter",  # JS functions unimplemented
            "flat",
            "full_width",
            "height",
            "hide_details",
            "hide_no_data",
            "hide_selected",
            "hint",
            "id",
            "item_color",
            "item_disabled",  # JS functions unimplemented
            "item_text",  # JS functions unimplemented
            "item_value",  # JS functions unimplemented
            "items",
            "label",
            "light",
            "loader_height",
            "loading",
            "menu_props",
            "messages",
            "multiple",
            "no_data_text",
            "no_filter",
            "open_on_clear",
            "outlined",
            "persistent_hint",
            "persistent_placeholder",
            "placeholder",
            "prefix",
            "prepend_icon",
            "prepend_inner_icon",
            "readonly",
            "return_object",
            "reverse",
            "rounded",
            "rules",
            "search_input",
            "shaped",
            "single_line",
            "small_chips",
            "solo",
            "solo_inverted",
            "success",
            "success_messages",
            "suffix",
            "validate_on_blur",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "blur",
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_append_outer", "click:append-outer"),
            ("click_clear", "click:clear"),
            ("click_prepend", "click:prepend"),
            ("click_prepend_inner", "click:prepend-inner"),
            "focus",
            "input",
            "keydown",
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
            ("update_list_index", "update:list-index"),
            ("update_search_input", "update:search-input"),
        ]


class VAvatar(HtmlElement):
    """
    Vuetify's VAvatar component.
    See more `info and examples <https://vuetifyjs.com/api/v-avatar>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      height (['number', 'string']):
        Sets the height for the component.
      left (boolean):
        Designates that the avatar is on the left side of a component.
        This is hooked into by components such as `v-chip </components/chips>`_
        and `v-btn </components/buttons>`_.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      right (boolean):
        Designates that the avatar is on the right side of a component.
        This is hooked into by components such as `v-chip </components/chips>`_
        and `v-btn </components/buttons>`_.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      size (['number', 'string']):
        Sets the height and width of the component.
      tile (boolean):
        Removes the component's **border-radius**.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-avatar", children, **kwargs)
        self._attr_names += [
            "color",
            "height",
            "left",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "right",
            "rounded",
            "size",
            "tile",
            "width",
        ]
        self._event_names += []


class VBadge(HtmlElement):
    """
    Vuetify's VBadge component.
    See more `info and examples <https://vuetifyjs.com/api/v-badge>`_.

    Args:
      avatar (boolean):
        Removes badge padding for the use of the `v-avatar` in the **badge** slot.
      bordered (boolean):
        Applies a **2px** by default and **1.5px** border around the
        badge when using the **dot** property.
      bottom (boolean):
        Aligns the component towards the bottom.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      content (any):
        Any content you want injected as text into the badge.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dot (boolean):
        Reduce the size of the badge and hide its contents
      icon (string):
        Designates a specific icon used in the badge.
      inline (boolean):
        Moves the badge to be inline with the wrapping element. Supports
        the usage of the **left** prop.
      label (string):
        The **aria-label** used for the badge
      left (boolean):
        Aligns the component towards the left.
      light (boolean):
        Applies the light theme variant to the component.
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      offset_x (['number', 'string']):
        Offset the badge on the x-axis.
      offset_y (['number', 'string']):
        Offset the badge on the y-axis.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
      overlap (boolean):
        Overlaps the slotted content on top of the component.
      tile (boolean):
        Removes the component's border-radius.
      transition (string):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      value (any):
        Controls whether the component is visible or hidden.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-badge", children, **kwargs)
        self._attr_names += [
            "avatar",
            "bordered",
            "bottom",
            "color",
            "content",
            "dark",
            "dot",
            "icon",
            "inline",
            "label",
            "left",
            "light",
            "mode",
            "offset_x",
            "offset_y",
            "origin",
            "overlap",
            "tile",
            "transition",
            "value",
        ]
        self._event_names += []


class VBanner(HtmlElement):
    """
    Vuetify's VBanner component.
    See more `info and examples <https://vuetifyjs.com/api/v-banner>`_.

    Args:
      app (boolean):
        When used inside of `v-main`, will calculate top based upon application
        `v-toolbar` and `v-system-bar`.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      height (['number', 'string']):
        Sets the height for the component.
      icon (string):
        Designates a specific icon.
      icon_color (string):
        Designates a specific icon color.
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      mobile_breakpoint (['number', 'string']):
        Sets the designated mobile breakpoint for the component.
      outlined (boolean):
        Removes elevation (box-shadow) and adds a *thin* border.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      single_line (boolean):
        Forces the banner onto a single line.
      sticky (boolean):
        Applies **position: sticky** to the component (**Evergreen browsers
        only**>`_. You can find more information on the `MDN documentation
        for sticky position <https://developer.mozilla.org/en-US/docs/Web/CSS/position>`_.
      tag (string):
        Specify a custom tag used on the root element.
      tile (boolean):
        Removes the component's **border-radius**.
      value (boolean):
        Controls whether the component is visible or hidden.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-banner", children, **kwargs)
        self._attr_names += [
            "app",
            "color",
            "dark",
            "elevation",
            "height",
            "icon",
            "icon_color",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "mobile_breakpoint",
            "outlined",
            "rounded",
            "shaped",
            "single_line",
            "sticky",
            "tag",
            "tile",
            "value",
            "width",
        ]
        self._event_names += []


class VBottomNavigation(HtmlElement):
    """
    Vuetify's VBottomNavigation component.
    See more `info and examples <https://vuetifyjs.com/api/v-bottom-navigation>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      active_class (string):
        The class applied to a `v-btn </components/buttons>`_ when activated.
      app (boolean):
        Designates the component as part of the application layout. Used
        for dynamically adjusting content sizing. Components using this
        prop should reside **outside** of `v-main` component to function
        properly. You can find more information about layouts on the
        `application page </components/application>`_. **Note:** this
        prop automatically applies **position: fixed** to the layout
        element. You can overwrite this functionality by using the `absolute`
        prop
      background_color (string):
        Changes the background-color for the component.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      fixed (boolean):
        Applies **position: fixed** to the component.
      grow (boolean):
        Force `v-btn </components/buttons>`_s to take up all available space.
      height (['number', 'string']):
        Sets the height for the component.
      hide_on_scroll (boolean):
        Will transition the navigation off screen when scrolling up.
      horizontal (boolean):
        Uses an alternative horizontal styling for `v-btn </components/buttons>`_.
      input_value (boolean):
        Controls whether the component is visible or hidden. Supports
        the **.sync** modifier.
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      scroll_target (string):
        Designates the element to target for scrolling events. Uses `window` by default.
      scroll_threshold (['string', 'number']):
        The amount of scroll distance down before **hide-on-scroll** activates.
      shift (boolean):
        Hides text of `v-btn </components/buttons>`_s when they are not active.
      tag (string):
        Specify a custom tag used on the root element.
      value (any):
        Holds the value of the currently active `v-btn </components/buttons>`_.
        If the button has no value supplied, its index will be used instead..
      width (['number', 'string']):
        Sets the width for the component.
      change (event):
        The value of currently selected button. If no value is assigned,
        will be the current index of the button.
      update_input-value (event):
        The event used for `input-value.sync`.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-bottom-navigation", children, **kwargs)
        self._attr_names += [
            "absolute",
            "active_class",
            "app",
            "background_color",
            "color",
            "dark",
            "fixed",
            "grow",
            "height",
            "hide_on_scroll",
            "horizontal",
            "input_value",
            "light",
            "mandatory",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "scroll_target",
            "scroll_threshold",
            "shift",
            "tag",
            "value",
            "width",
        ]
        self._event_names += [
            "change",
            ("update_input_value", "update:input-value"),
        ]


class VBottomSheet(HtmlElement):
    """
    Vuetify's VBottomSheet component.
    See more `info and examples <https://vuetifyjs.com/api/v-bottom-sheet>`_.

    Args:
      activator (any):
        Designate a custom activator when the `activator` slot is not
        used. String can be any valid querySelector and Object can be
        any valid Node.
      attach (any):
        Specifies which DOM element that this component should detach
        to. String can be any valid querySelector and Object can be any
        valid Node. This will attach to the root `v-app` component by
        default.
      close_delay (['number', 'string']):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      content_class (string):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Disables the ability to open the component.
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      fullscreen (boolean):
        Changes layout for fullscreen display.
      hide_overlay (boolean):
        Hides the display of the overlay.
      inset (boolean):
        Reduces the sheet content maximum width to 70%.
      internal_activator (boolean):
        Detaches the menu content inside of the component as opposed to the document.
      light (boolean):
        Applies the light theme variant to the component.
      max_width (['string', 'number']):
        Sets the maximum width for the component.
      no_click_animation (boolean):
        Disables the bounce effect when clicking outside of a `v-dialog`'s
        content when using the **persistent** prop.
      open_delay (['number', 'string']):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      open_on_click (boolean):

      open_on_focus (boolean):

      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
      overlay_color (string):
        Sets the overlay color.
      overlay_opacity (['number', 'string']):
        Sets the overlay opacity.
      persistent (boolean):
        Clicking outside of the element or pressing **esc** key will not deactivate it.
      retain_focus (boolean):
        Tab focus will return to the first child of the dialog by default.
        Disable this when using external tools that require focus such
        as TinyMCE or vue-clipboard.
      return_value (any):

      scrollable (boolean):
        When set to true, expects a `v-card` and a `v-card-text` component
        with a designated height. For more information, check out the
        `scrollable example </components/dialogs#scrollable>`_.
      transition (string):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      value (any):
        Controls whether the component is visible or hidden.
      width (['string', 'number']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-bottom-sheet", children, **kwargs)
        self._attr_names += [
            "activator",
            "attach",
            "close_delay",
            "content_class",
            "dark",
            "disabled",
            "eager",
            "fullscreen",
            "hide_overlay",
            "inset",
            "internal_activator",
            "light",
            "max_width",
            "no_click_animation",
            "open_delay",
            "open_on_click",
            "open_on_focus",
            "origin",
            "overlay_color",
            "overlay_opacity",
            "persistent",
            "retain_focus",
            "return_value",
            "scrollable",
            "transition",
            "value",
            "width",
        ]
        self._event_names += []


class VBreadcrumbs(HtmlElement):
    """
    Vuetify's VBreadcrumbs component.
    See more `info and examples <https://vuetifyjs.com/api/v-breadcrumbs>`_.

    Args:
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      divider (string):
        Specifies the dividing character between items.
      items (array):
        An array of objects for each breadcrumb.
      large (boolean):
        Increase the font-size of the breadcrumb item text to 16px (14px default).
      light (boolean):
        Applies the light theme variant to the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-breadcrumbs", children, **kwargs)
        self._attr_names += [
            "dark",
            "divider",
            "items",
            "large",
            "light",
        ]
        self._event_names += []


class VBreadcrumbsItem(HtmlElement):
    """
    Vuetify's VBreadcrumbsItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-breadcrumbs-item>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      append (boolean):
        Setting **append** prop always appends the relative path to the
        current path. You can find more information about the `**append**
        prop <https://router.vuejs.org/api/#append>`_ on the vue-router
        documentation.
      disabled (boolean):
        Removes the ability to click or target the component.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the `**exact** prop <https://router.vuejs.org/api/#exact>`_
        on the vue-router documentation.
      exact_active_class (string):
        Configure the active CSS class applied when the link is active
        with exact match. You can find more information about the `**exact-active-class**
        prop <https://router.vuejs.org/api/#exact-active-class>`_ on
        the vue-router documentation.
      exact_path (boolean):
        Exactly match the link, ignoring the `query` and the `hash` sections.
        You can find more information about the `**exact-path** prop
        <https://router.vuejs.org/api/#exact-path>`_ on the vue-router
        documentation.
      href (['string', 'object']):
        Designates the component as anchor and applies the **href** attribute.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the **href** or **to** prop.
      nuxt (boolean):
        Specifies the link is a `nuxt-link`. For use with the `nuxt framework
        <https://nuxtjs.org/api/components-nuxt-link/>`_.
      replace (boolean):
        Setting **replace** prop will call `router.replace(>`_` instead
        of `router.push(>`_` when clicked, so the navigation will not
        leave a history record. You can find more information about the
        `**replace** prop <https://router.vuejs.org/api/#replace>`_ on
        the vue-router documentation.
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      tag (string):
        Specify a custom tag used on the root element.
      target (string):
        Designates the target attribute. This should only be applied
        when using the **href** prop.
      to (['string', 'object']):
        Denotes the target route of the link. You can find more information
        about the `**to** prop <https://router.vuejs.org/api/#to>`_ on
        the vue-router documentation.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-breadcrumbs-item", children, **kwargs)
        self._attr_names += [
            "active_class",
            "append",
            "disabled",
            "exact",
            "exact_active_class",
            "exact_path",
            "href",
            "link",
            "nuxt",
            "replace",
            "ripple",
            "tag",
            "target",
            "to",
        ]
        self._event_names += []


class VBreadcrumbsDivider(HtmlElement):
    """
    Vuetify's VBreadcrumbsDivider component.
    See more `info and examples <https://vuetifyjs.com/api/v-breadcrumbs-divider>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-breadcrumbs-divider", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VBtn(HtmlElement):
    """
    Vuetify's VBtn component.
    See more `info and examples <https://vuetifyjs.com/api/v-btn>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      append (boolean):
        Setting **append** prop always appends the relative path to the
        current path. You can find more information about the `**append**
        prop <https://router.vuejs.org/api/#append>`_ on the vue-router
        documentation.
      block (boolean):
        Expands the button to 100% of available space.
      bottom (boolean):
        Aligns the component towards the bottom.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      depressed (boolean):
        Removes the button box shadow.
      disabled (boolean):
        Removes the ability to click or target the component.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the `**exact** prop <https://router.vuejs.org/api/#exact>`_
        on the vue-router documentation.
      exact_active_class (string):
        Configure the active CSS class applied when the link is active
        with exact match. You can find more information about the `**exact-active-class**
        prop <https://router.vuejs.org/api/#exact-active-class>`_ on
        the vue-router documentation.
      exact_path (boolean):
        Exactly match the link, ignoring the `query` and the `hash` sections.
        You can find more information about the `**exact-path** prop
        <https://router.vuejs.org/api/#exact-path>`_ on the vue-router
        documentation.
      fab (boolean):
        Designates the button as a floating-action-button. Button will become _round_.
      fixed (boolean):
        Applies **position: fixed** to the component.
      height (['number', 'string']):
        Sets the height for the component.
      href (['string', 'object']):
        Designates the component as anchor and applies the **href** attribute.
      icon (boolean):
        Designates the button as icon. Button will become _round_ and
        applies the **text** prop.
      input_value (any):
        Controls the button's active state.
      large (boolean):
        Makes the component large.
      left (boolean):
        Aligns the component towards the left. This should be used with
        the **absolute** or **fixed** props.
      light (boolean):
        Applies the light theme variant to the component.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the **href** or **to** prop.
      loading (boolean):
        Adds a loading icon animation.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      nuxt (boolean):
        Specifies the link is a `nuxt-link`. For use with the `nuxt framework
        <https://nuxtjs.org/api/components-nuxt-link/>`_.
      outlined (boolean):
        Makes the background transparent and applies a thin border.
      plain (boolean):
        Removes the default background change applied when hovering over the button.
      replace (boolean):
        Setting **replace** prop will call `router.replace(>`_` instead
        of `router.push(>`_` when clicked, so the navigation will not
        leave a history record. You can find more information about the
        `**replace** prop <https://router.vuejs.org/api/#replace>`_ on
        the vue-router documentation.
      retain_focus_on_click (boolean):
        Don't blur on click.
      right (boolean):
        Aligns the component towards the right. This should be used with
        the **absolute** or **fixed** props.
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      rounded (boolean):
        Applies a large border radius on the button.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      small (boolean):
        Makes the component small.
      tag (string):
        Specify a custom tag used on the root element.
      target (string):
        Designates the target attribute. This should only be applied
        when using the **href** prop.
      text (boolean):
        Makes the background transparent. When using the **color** prop,
        the color will be applied to the button text instead of the background.
      tile (boolean):
        Removes the component's **border-radius**.
      to (['string', 'object']):
        Denotes the target route of the link. You can find more information
        about the `**to** prop <https://router.vuejs.org/api/#to>`_ on
        the vue-router documentation.
      top (boolean):
        Aligns the content towards the top.
      type (string):
        Set the button's **type** attribute.
      value (any):
        Controls whether the component is visible or hidden.
      width (['number', 'string']):
        Sets the width for the component.
      x_large (boolean):
        Makes the component extra large.
      x_small (boolean):
        Makes the component extra small.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-btn", children, **kwargs)
        self._attr_names += [
            "absolute",
            "active_class",
            "append",
            "block",
            "bottom",
            "color",
            "dark",
            "depressed",
            "disabled",
            "elevation",
            "exact",
            "exact_active_class",
            "exact_path",
            "fab",
            "fixed",
            "height",
            "href",
            "icon",
            "input_value",
            "large",
            "left",
            "light",
            "link",
            "loading",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "nuxt",
            "outlined",
            "plain",
            "replace",
            "retain_focus_on_click",
            "right",
            "ripple",
            "rounded",
            "shaped",
            "small",
            "tag",
            "target",
            "text",
            "tile",
            "to",
            "top",
            "type",
            "value",
            "width",
            "x_large",
            "x_small",
        ]
        self._event_names += [
            "click",
        ]


class VBtnToggle(HtmlElement):
    """
    Vuetify's VBtnToggle component.
    See more `info and examples <https://vuetifyjs.com/api/v-btn-toggle>`_.

    Args:
      active_class (string):
        The **active-class** applied to children when they are activated.
      background_color (string):
        Changes the background-color for the component.
      borderless (boolean):
        Removes the group's border.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the button size and padding.
      group (boolean):
        Generally used in `v-toolbar </components/toolbars>`_ and `v-app-bar
        </components/app-bars>`_. Removes background color, border and
        increases space between the buttons
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max (['number', 'string']):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allow multiple selections. The **value** prop must be an _array_.
      rounded (boolean):
        Round edge buttons
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      tag (string):
        Specify a custom tag used on the root element.
      tile (boolean):
        Removes the component's border-radius.
      value (any):
        The designated model value for the component.
      value_comparator (function):
        Apply a custom value comparator function
      change (event):
        Emitted when the input is changed by user interaction
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-btn-toggle", children, **kwargs)
        self._attr_names += [
            "active_class",
            "background_color",
            "borderless",
            "color",
            "dark",
            "dense",
            "group",
            "light",
            "mandatory",
            "max",
            "multiple",
            "rounded",
            "shaped",
            "tag",
            "tile",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "change",
        ]


class VCalendar(HtmlElement):
    """
    Vuetify's VCalendar component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar>`_.

    Args:
      categories (['array', 'string']):
        Specifies what categories to display in the `category` view.
        This controls the order of the categories as well. If the calendar
        uses events any categories specified in those events not specified
        in this value are dynamically rendered in the view unless `category-hide-dynamic`
        is true.
      category_days (['number', 'string']):
        The number of days to render in the `category` view.
      category_for_invalid (string):
        The category to place events in that have invalid categories.
        A category is invalid when it is not a string. By default events
        without a category are not displayed until this value is specified.
      category_hide_dynamic (boolean):
        Sets whether categories specified in an event should be hidden
        if it's not defined in `categories`.
      category_show_all (boolean):
        Set whether the `category` view should show all defined `categories`
        even if there are no events for a category.
      category_text (['string', 'function']):
        If categories is a list of objects, you can use this to determine
        what property to print out as the category text on the calendar.
        You can provide a function to do some logic or just define the
        prop name. It's similar to item-text on v-select
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      day_format (function):
        Formats day of the month string that appears in a day to a specified locale
      end (['string', 'number', 'date']):
        The ending date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      event_category (['string', 'function']):
        Set property of *event*'s category. Instead of a property a function
        can be given which takes an event and returns the category.
      event_color (['string', 'function']):
        A background color for all events or a function which accepts
        an event object passed to the calendar to return a color.
      event_end (string):
        Set property of *event*'s end timestamp.
      event_height (number):
        The height of an event in pixels in the `month` view and at the
        top of the `day` views.
      event_margin_bottom (number):
        Margin bottom for event
      event_more (boolean):
        Whether the more 'button' is displayed on a calendar with too
        many events in a given day. It will say something like '5 more'
        and when clicked generates a `click:more` event.
      event_more_text (string):
        The text to display in the more 'button' given the number of hidden events.
      event_name (['string', 'function']):
        Set property of *event*'s displayed name, or a function which
        accepts an event object passed to the calendar as the first argument
        and a flag signalling whether the name is for a timed event (true)
        or an event over a day.
      event_overlap_mode (['string', 'function']):
        One of `stack`, `column`, or a custom render function
      event_overlap_threshold (['string', 'number']):
        A value in minutes that's used to determine whether two timed
        events should be placed in column beside each other or should
        be treated as slightly overlapping events.
      event_ripple (['boolean', 'object']):
        Applies the `v-ripple` directive.
      event_start (string):
        Set property of *event*'s start timestamp.
      event_text_color (['string', 'function']):
        A text color for all events or a function which accepts an event
        object passed to the calendar to return a color.
      event_timed (['string', 'function']):
        If Dates or milliseconds are used as the start or end timestamp
        of an event, this prop can be a string to a property on the event
        that is truthy if the event is a timed event or a function which
        takes the event and returns a truthy value if the event is a
        timed event.
      events (array):
        An array of event objects with a property for a start timestamp
        and optionally a name and end timestamp. If an end timestamp
        is not given, the value of start will be used. If no name is
        given, you must provide an implementation for the `event` slot.
      first_interval (['number', 'string']):
        The first interval to display in the `day` view. If `intervalMinutes`
        is set to 60 and this is set to 9 the first time in the view
        is 9am.
      first_time (['number', 'string', 'object']):
        The first time to display in the `day` view. If specified, this
        overwrites any `firstInterval` value specified. This can be the
        number of minutes since midnight, a string in the format of `HH:mm`,
        or an object with number properties hour and minute.
      hide_header (boolean):
        If the header at the top of the `day` view should be visible.
      interval_count (['number', 'string']):
        The number of intervals to display in the `day` view.
      interval_format (function):
        Formats time of day string that appears in the interval gutter
        of the `day` and `week` view to specified locale
      interval_height (['number', 'string']):
        The height of an interval in pixels in the `day` view.
      interval_minutes (['number', 'string']):
        The number of minutes the intervals are in the `day` view. A
        common interval is 60 minutes so the intervals are an hour.
      interval_style (function):
        Returns CSS styling to apply to the interval.
      interval_width (['number', 'string']):
        The width of the interval gutter on the left side in the `day` view.
      light (boolean):
        Applies the light theme variant to the component.
      locale (string):
        The locale of the calendar.
      locale_first_day_of_year (['string', 'number']):
        Sets the day that determines the first week of the year, starting
        with 0 for **Sunday**. For ISO 8601 this should be 4.
      max_days (number):
        The maximum number of days to display in the custom calendar
        if an `end` day is not set.
      min_weeks (any):
        The minimum number of weeks to display in the `month` or `week` view.
      month_format (function):
        Formats month string that appears in a day to specified locale
      now (string):
        Override the day & time which is considered now. This is in the
        format of `YYYY-MM-DD hh:mm:ss`. The calendar is styled according
        to now.
      short_intervals (boolean):
        If true, the intervals in the `day` view will be 9 AM as opposed to 09:00 AM
      short_months (boolean):
        Whether the short versions of a month should be used (Jan vs January).
      short_weekdays (boolean):
        Whether the short versions of a weekday should be used (Mon vs Monday).
      show_interval_label (function):
        Checks if a given day and time should be displayed in the interval
        gutter of the `day` view.
      show_month_on_first (boolean):
        Whether the name of the month should be displayed on the first day of the month.
      show_week (boolean):
        Whether week numbers should be displayed when using the `month` view.
      start (['string', 'number', 'date']):
        The starting date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      type (string):
        A string which is one of `month`, `week`, `day`, `4day`, `custom-weekly`,
        `custom-daily`, and `category`. The custom types look at the
        `start` and `end` dates passed to the component as opposed to
        the `value`.
      value (['string', 'number', 'date']):
        A date in the format of `YYYY-MM-DD` which determines what span
        of time for the calendar.
      weekday_format (function):
        Formats day of the week string that appears in the header to specified locale
      weekdays (['array', 'string']):
        Specifies which days of the week to display. To display Monday
        through Friday only, a value of `[1, 2, 3, 4, 5]` can be used.
        To display a week starting on Monday a value of `[1, 2, 3, 4,
        5, 6, 0]` can be used.
      change (event):
        The range of days displayed on the calendar changed. This is
        triggered on initialization. The event passed is an object with
        start and end date objects.
      click_date (event):
        The click event on the day of the month link. The event passed
        is the day & time object. Native mouse event is passed as a second
        argument.
      click_day (event):
        The click event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      click_day-category (event):
        The click event on a day in the `category` view. The event passed
        is the day object. Native mouse event is passed as a second argument.
      click_event (event):
        The click event on a specific event. The event passed is the day & time object.
      click_interval (event):
        The click event at a specific interval label in the `day` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      click_more (event):
        The click event on the `X more` button on views with too many
        events in a day. Native mouse event is passed as a second argument.
      click_time (event):
        The click event at a specific time in the `day` view. The event
        passed is the day & time object. Native mouse event is passed
        as a second argument.
      click_time-category (event):
        The click event at a specific time in the `category` view. The
        event passed is the day & time object. Native mouse event is
        passed as a second argument.
      contextmenu_date (event):
        The right-click event on the day of the month link. The event
        passed is the day & time object. Native mouse event is passed
        as a second argument.
      contextmenu_day (event):
        The right-click event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      contextmenu_day-category (event):
        The right-click event on a day in the `category` view. The event
        passed is the day object. Native mouse event is passed as a second
        argument.
      contextmenu_event (event):
        The right-click event on an event. The event passed is the day & time object.
      contextmenu_interval (event):
        The right-click event at a specific interval label in the `day`
        view. The event passed is the day & time object. Native mouse
        event is passed as a second argument.
      contextmenu_time (event):
        The right-click event at a specific time in the `day` view. The
        event passed is the day & time object. Native mouse event is
        passed as a second argument.
      contextmenu_time-category (event):
        The right-click event at a specific time in the `category` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      input (event):
        An alias to the `click:date` event used to support v-model.
      mousedown_day (event):
        The mousedown event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      mousedown_day-category (event):
        The mousedown event on a day in the `category` view. The event
        passed is the day object. Native mouse event is passed as a second
        argument.
      mousedown_event (event):
        The mousedown event on an event. The event passed is the day & time object.
      mousedown_interval (event):
        The mousedown event at a specific interval label in the `day`
        view. The event passed is the day & time object. Native mouse
        event is passed as a second argument.
      mousedown_time (event):
        The mousedown event at a specific time in the `day` view. The
        event passed is the day & time object. Native mouse event is
        passed as a second argument.
      mousedown_time-category (event):
        The mousedown event at a specific time in the `category` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      mouseenter_day (event):
        The mouseenter event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      mouseenter_day-category (event):
        The mouseenter event on a day in the `category` view. The event
        passed is the day object. Native mouse event is passed as a second
        argument.
      mouseenter_event (event):
        The mouseenter event on an event. The event passed is the day & time object.
      mouseenter_interval (event):
        The mouseenter event at a specific interval label in the `day`
        view. The event passed is the day & time object. Native mouse
        event is passed as a second argument.
      mouseenter_time (event):
        The mouseenter event at a specific time in the `day` view. The
        event passed is the day & time object. Native mouse event is
        passed as a second argument.
      mouseenter_time-category (event):
        The mouseenter event at a specific time in the `category` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      mouseleave_day (event):
        The mouseleave event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      mouseleave_day-category (event):
        The mouseleave event on a day in the `category` view. The event
        passed is the day object. Native mouse event is passed as a second
        argument.
      mouseleave_event (event):
        The mouseleave event on an event. The event passed is the day & time object.
      mouseleave_interval (event):
        The mouseleave event at a specific interval label in the `day`
        view. The event passed is the day & time object. Native mouse
        event is passed as a second argument.
      mouseleave_time (event):
        The mouseleave event at a specific time in the `day` view. The
        event passed is the day & time object. Native mouse event is
        passed as a second argument.
      mouseleave_time-category (event):
        The mouseleave event at a specific time in the `category` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      mousemove_day (event):
        The mousemove event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      mousemove_day-category (event):
        The mousemove event on a day in the `category` view. The event
        passed is the day object. Native mouse event is passed as a second
        argument.
      mousemove_event (event):
        The mousemove event on an event. The event passed is the day & time object.
      mousemove_interval (event):
        The mousemove event at a specific interval label in the `day`
        view. The event passed is the day & time object. Native mouse
        event is passed as a second argument.
      mousemove_time (event):
        The mousemove event at a specific time in the `day` view. The
        event passed is the day & time object. Native mouse event is
        passed as a second argument.
      mousemove_time-category (event):
        The mousemove event at a specific time in the `category` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      mouseup_day (event):
        The mouseup event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      mouseup_day-category (event):
        The mouseup event on a day in the `category` view. The event
        passed is the day object. Native mouse event is passed as a second
        argument.
      mouseup_event (event):
        The mouseup event on an event. The event passed is the day & time object.
      mouseup_interval (event):
        The mouseup event at a specific interval label in the `day` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      mouseup_time (event):
        The mouseup event at a specific time in the `day` view. The event
        passed is the day & time object. Native mouse event is passed
        as a second argument.
      mouseup_time-category (event):
        The mouseup event at a specific time in the `category` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      moved (event):
        One of the functions `next`, `prev`, and `move` was called. The
        event passed is the day object calculated for the movement.
      touchend_day (event):
        The touchend event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      touchend_day-category (event):
        The touchend event on a day in the `category` view. The event
        passed is the day object. Native mouse event is passed as a second
        argument.
      touchend_event (event):
        The touchend event on am view. The event passed is the day & time object.
      touchend_interval (event):
        The touchend event at a specific interval label in the `day`
        view. The event passed is the day & time object. Native mouse
        event is passed as a second argument.
      touchend_time (event):
        The touchend event at a specific time in the `day` view. The
        event passed is the day & time object. Native mouse event is
        passed as a second argument.
      touchend_time-category (event):
        The touchend event at a specific time in the `category` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      touchmove_day (event):
        The touchmove event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      touchmove_day-category (event):
        The touchmove event on a day in the `category` view. The event
        passed is the day object. Native mouse event is passed as a second
        argument.
      touchmove_event (event):
        The touchmove event on an `event` view. The event passed is the
        day & time object.
      touchmove_interval (event):
        The touchmove event at a specific interval label in the `day`
        view. The event passed is the day & time object. Native mouse
        event is passed as a second argument.
      touchmove_time (event):
        The touchmove event at a specific time in the `day` view. The
        event passed is the day & time object. Native mouse event is
        passed as a second argument.
      touchmove_time-category (event):
        The touchmove event at a specific time in the `category` view.
        The event passed is the day & time object. Native mouse event
        is passed as a second argument.
      touchstart_day (event):
        The touchstart event on a day. The event passed is the day object.
        Native mouse event is passed as a second argument.
      touchstart_day-category (event):
        The touchstart event on a day in the `category` view. The event
        passed is the day object. Native mouse event is passed as a second
        argument.
      touchstart_event (event):
        The touchstart event on an event` view. The event passed is the
        day & time object.
      touchstart_interval (event):
        The touchstart event at a specific interval label in the `day`
        view. The event passed is the day & time object. Native mouse
        event is passed as a second argument.
      touchstart_time (event):
        The touchstart event at a specific time in the `day` view. The
        event passed is the day & time object. Native mouse event is
        passed as a second argument.
      touchstart_time-category (event):
        The touchstart event at a specific time in the `category` view.
        The event passed is the day & time object Native mouse event
        is passed as a second argument..
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-calendar", children, **kwargs)
        self._attr_names += [
            "categories",
            "category_days",
            "category_for_invalid",
            "category_hide_dynamic",
            "category_show_all",
            "category_text",  # JS functions unimplemented
            "color",
            "dark",
            "day_format",  # JS functions unimplemented
            "end",
            "event_category",  # JS functions unimplemented
            "event_color",  # JS functions unimplemented
            "event_end",
            "event_height",
            "event_margin_bottom",
            "event_more",
            "event_more_text",
            "event_name",  # JS functions unimplemented
            "event_overlap_mode",  # JS functions unimplemented
            "event_overlap_threshold",
            "event_ripple",
            "event_start",
            "event_text_color",  # JS functions unimplemented
            "event_timed",  # JS functions unimplemented
            "events",
            "first_interval",
            "first_time",
            "hide_header",
            "interval_count",
            "interval_format",  # JS functions unimplemented
            "interval_height",
            "interval_minutes",
            "interval_style",  # JS functions unimplemented
            "interval_width",
            "light",
            "locale",
            "locale_first_day_of_year",
            "max_days",
            "min_weeks",
            "month_format",  # JS functions unimplemented
            "now",
            "short_intervals",
            "short_months",
            "short_weekdays",
            "show_interval_label",  # JS functions unimplemented
            "show_month_on_first",
            "show_week",
            "start",
            "type",
            "value",
            "weekday_format",  # JS functions unimplemented
            "weekdays",
        ]
        self._event_names += [
            "change",
            ("click_date", "click:date"),
            ("click_day", "click:day"),
            ("click_day_category", "click:day-category"),
            ("click_event", "click:event"),
            ("click_interval", "click:interval"),
            ("click_more", "click:more"),
            ("click_time", "click:time"),
            ("click_time_category", "click:time-category"),
            ("contextmenu_date", "contextmenu:date"),
            ("contextmenu_day", "contextmenu:day"),
            ("contextmenu_day_category", "contextmenu:day-category"),
            ("contextmenu_event", "contextmenu:event"),
            ("contextmenu_interval", "contextmenu:interval"),
            ("contextmenu_time", "contextmenu:time"),
            ("contextmenu_time_category", "contextmenu:time-category"),
            "input",
            ("mousedown_day", "mousedown:day"),
            ("mousedown_day_category", "mousedown:day-category"),
            ("mousedown_event", "mousedown:event"),
            ("mousedown_interval", "mousedown:interval"),
            ("mousedown_time", "mousedown:time"),
            ("mousedown_time_category", "mousedown:time-category"),
            ("mouseenter_day", "mouseenter:day"),
            ("mouseenter_day_category", "mouseenter:day-category"),
            ("mouseenter_event", "mouseenter:event"),
            ("mouseenter_interval", "mouseenter:interval"),
            ("mouseenter_time", "mouseenter:time"),
            ("mouseenter_time_category", "mouseenter:time-category"),
            ("mouseleave_day", "mouseleave:day"),
            ("mouseleave_day_category", "mouseleave:day-category"),
            ("mouseleave_event", "mouseleave:event"),
            ("mouseleave_interval", "mouseleave:interval"),
            ("mouseleave_time", "mouseleave:time"),
            ("mouseleave_time_category", "mouseleave:time-category"),
            ("mousemove_day", "mousemove:day"),
            ("mousemove_day_category", "mousemove:day-category"),
            ("mousemove_event", "mousemove:event"),
            ("mousemove_interval", "mousemove:interval"),
            ("mousemove_time", "mousemove:time"),
            ("mousemove_time_category", "mousemove:time-category"),
            ("mouseup_day", "mouseup:day"),
            ("mouseup_day_category", "mouseup:day-category"),
            ("mouseup_event", "mouseup:event"),
            ("mouseup_interval", "mouseup:interval"),
            ("mouseup_time", "mouseup:time"),
            ("mouseup_time_category", "mouseup:time-category"),
            "moved",
            ("touchend_day", "touchend:day"),
            ("touchend_day_category", "touchend:day-category"),
            ("touchend_event", "touchend:event"),
            ("touchend_interval", "touchend:interval"),
            ("touchend_time", "touchend:time"),
            ("touchend_time_category", "touchend:time-category"),
            ("touchmove_day", "touchmove:day"),
            ("touchmove_day_category", "touchmove:day-category"),
            ("touchmove_event", "touchmove:event"),
            ("touchmove_interval", "touchmove:interval"),
            ("touchmove_time", "touchmove:time"),
            ("touchmove_time_category", "touchmove:time-category"),
            ("touchstart_day", "touchstart:day"),
            ("touchstart_day_category", "touchstart:day-category"),
            ("touchstart_event", "touchstart:event"),
            ("touchstart_interval", "touchstart:interval"),
            ("touchstart_time", "touchstart:time"),
            ("touchstart_time_category", "touchstart:time-category"),
        ]


class VCalendarDaily(HtmlElement):
    """
    Vuetify's VCalendarDaily component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar-daily>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      day_format (function):
        Formats day of the month string that appears in a day to a specified locale
      end (['string', 'number', 'date']):
        The ending date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      first_interval (['number', 'string']):
        The first interval to display in the `day` view. If `intervalMinutes`
        is set to 60 and this is set to 9 the first time in the view
        is 9am.
      first_time (['number', 'string', 'object']):
        The first time to display in the `day` view. If specified, this
        overwrites any `firstInterval` value specified. This can be the
        number of minutes since midnight, a string in the format of `HH:mm`,
        or an object with number properties hour and minute.
      hide_header (boolean):
        If the header at the top of the `day` view should be visible.
      interval_count (['number', 'string']):
        The number of intervals to display in the `day` view.
      interval_format (function):
        Formats time of day string that appears in the interval gutter
        of the `day` and `week` view to specified locale
      interval_height (['number', 'string']):
        The height of an interval in pixels in the `day` view.
      interval_minutes (['number', 'string']):
        The number of minutes the intervals are in the `day` view. A
        common interval is 60 minutes so the intervals are an hour.
      interval_style (function):
        Returns CSS styling to apply to the interval.
      interval_width (['number', 'string']):
        The width of the interval gutter on the left side in the `day` view.
      light (boolean):
        Applies the light theme variant to the component.
      locale (string):
        The locale of the calendar.
      max_days (number):
        The maximum number of days to display in the custom calendar
        if an `end` day is not set.
      now (string):
        Override the day & time which is considered now. This is in the
        format of `YYYY-MM-DD hh:mm:ss`. The calendar is styled according
        to now.
      short_intervals (boolean):
        If true, the intervals in the `day` view will be 9 AM as opposed to 09:00 AM
      short_weekdays (boolean):
        Whether the short versions of a weekday should be used (Mon vs Monday).
      show_interval_label (function):
        Checks if a given day and time should be displayed in the interval
        gutter of the `day` view.
      start (['string', 'number', 'date']):
        The starting date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      weekday_format (function):
        Formats day of the week string that appears in the header to specified locale
      weekdays (['array', 'string']):
        Specifies which days of the week to display. To display Monday
        through Friday only, a value of `[1, 2, 3, 4, 5]` can be used.
        To display a week starting on Monday a value of `[1, 2, 3, 4,
        5, 6, 0]` can be used.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-calendar-daily", children, **kwargs)
        self._attr_names += [
            "color",
            "dark",
            "day_format",  # JS functions unimplemented
            "end",
            "first_interval",
            "first_time",
            "hide_header",
            "interval_count",
            "interval_format",  # JS functions unimplemented
            "interval_height",
            "interval_minutes",
            "interval_style",  # JS functions unimplemented
            "interval_width",
            "light",
            "locale",
            "max_days",
            "now",
            "short_intervals",
            "short_weekdays",
            "show_interval_label",  # JS functions unimplemented
            "start",
            "weekday_format",  # JS functions unimplemented
            "weekdays",
        ]
        self._event_names += []


class VCalendarWeekly(HtmlElement):
    """
    Vuetify's VCalendarWeekly component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar-weekly>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      day_format (function):
        Formats day of the month string that appears in a day to a specified locale
      end (['string', 'number', 'date']):
        The ending date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      hide_header (boolean):
        If the header at the top of the `day` view should be visible.
      light (boolean):
        Applies the light theme variant to the component.
      locale (string):
        The locale of the calendar.
      locale_first_day_of_year (['string', 'number']):
        Sets the day that determines the first week of the year, starting
        with 0 for **Sunday**. For ISO 8601 this should be 4.
      min_weeks (any):
        The minimum number of weeks to display in the `month` or `week` view.
      month_format (function):
        Formats month string that appears in a day to specified locale
      now (string):
        Override the day & time which is considered now. This is in the
        format of `YYYY-MM-DD hh:mm:ss`. The calendar is styled according
        to now.
      short_months (boolean):
        Whether the short versions of a month should be used (Jan vs January).
      short_weekdays (boolean):
        Whether the short versions of a weekday should be used (Mon vs Monday).
      show_month_on_first (boolean):
        Whether the name of the month should be displayed on the first day of the month.
      show_week (boolean):
        Whether week numbers should be displayed when using the `month` view.
      start (['string', 'number', 'date']):
        The starting date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      weekday_format (function):
        Formats day of the week string that appears in the header to specified locale
      weekdays (['array', 'string']):
        Specifies which days of the week to display. To display Monday
        through Friday only, a value of `[1, 2, 3, 4, 5]` can be used.
        To display a week starting on Monday a value of `[1, 2, 3, 4,
        5, 6, 0]` can be used.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-calendar-weekly", children, **kwargs)
        self._attr_names += [
            "color",
            "dark",
            "day_format",  # JS functions unimplemented
            "end",
            "hide_header",
            "light",
            "locale",
            "locale_first_day_of_year",
            "min_weeks",
            "month_format",  # JS functions unimplemented
            "now",
            "short_months",
            "short_weekdays",
            "show_month_on_first",
            "show_week",
            "start",
            "weekday_format",  # JS functions unimplemented
            "weekdays",
        ]
        self._event_names += []


class VCalendarMonthly(HtmlElement):
    """
    Vuetify's VCalendarMonthly component.
    See more `info and examples <https://vuetifyjs.com/api/v-calendar-monthly>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      day_format (function):
        Formats day of the month string that appears in a day to a specified locale
      end (['string', 'number', 'date']):
        The ending date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      hide_header (boolean):
        If the header at the top of the `day` view should be visible.
      light (boolean):
        Applies the light theme variant to the component.
      locale (string):
        The locale of the calendar.
      locale_first_day_of_year (['string', 'number']):
        Sets the day that determines the first week of the year, starting
        with 0 for **Sunday**. For ISO 8601 this should be 4.
      min_weeks (any):
        The minimum number of weeks to display in the `month` or `week` view.
      month_format (function):
        Formats month string that appears in a day to specified locale
      now (string):
        Override the day & time which is considered now. This is in the
        format of `YYYY-MM-DD hh:mm:ss`. The calendar is styled according
        to now.
      short_months (boolean):
        Whether the short versions of a month should be used (Jan vs January).
      short_weekdays (boolean):
        Whether the short versions of a weekday should be used (Mon vs Monday).
      show_month_on_first (boolean):
        Whether the name of the month should be displayed on the first day of the month.
      show_week (boolean):
        Whether week numbers should be displayed when using the `month` view.
      start (['string', 'number', 'date']):
        The starting date on the calendar (inclusive) in the format of
        `YYYY-MM-DD`. This may be ignored depending on the `type` of
        the calendar.
      weekday_format (function):
        Formats day of the week string that appears in the header to specified locale
      weekdays (['array', 'string']):
        Specifies which days of the week to display. To display Monday
        through Friday only, a value of `[1, 2, 3, 4, 5]` can be used.
        To display a week starting on Monday a value of `[1, 2, 3, 4,
        5, 6, 0]` can be used.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-calendar-monthly", children, **kwargs)
        self._attr_names += [
            "color",
            "dark",
            "day_format",  # JS functions unimplemented
            "end",
            "hide_header",
            "light",
            "locale",
            "locale_first_day_of_year",
            "min_weeks",
            "month_format",  # JS functions unimplemented
            "now",
            "short_months",
            "short_weekdays",
            "show_month_on_first",
            "show_week",
            "start",
            "weekday_format",  # JS functions unimplemented
            "weekdays",
        ]
        self._event_names += []


class VCard(HtmlElement):
    """
    Vuetify's VCard component.
    See more `info and examples <https://vuetifyjs.com/api/v-card>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      append (boolean):
        Setting **append** prop always appends the relative path to the
        current path. You can find more information about the `**append**
        prop <https://router.vuejs.org/api/#append>`_ on the vue-router
        documentation.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Removes the ability to click or target the component.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the `**exact** prop <https://router.vuejs.org/api/#exact>`_
        on the vue-router documentation.
      exact_active_class (string):
        Configure the active CSS class applied when the link is active
        with exact match. You can find more information about the `**exact-active-class**
        prop <https://router.vuejs.org/api/#exact-active-class>`_ on
        the vue-router documentation.
      exact_path (boolean):
        Exactly match the link, ignoring the `query` and the `hash` sections.
        You can find more information about the `**exact-path** prop
        <https://router.vuejs.org/api/#exact-path>`_ on the vue-router
        documentation.
      flat (boolean):
        Removes the card's elevation.
      height (['number', 'string']):
        Sets the height for the component.
      hover (boolean):
        Will apply an elevation of 4dp when hovered (default 2dp>`_.
        You can find more information on the `elevation page </styles/elevation>`_.
      href (['string', 'object']):
        Designates the component as anchor and applies the **href** attribute.
      img (string):
        Specifies an image background for the card. For more advanced
        implementations, it is recommended that you use the `v-img </components/images>`_
        component. You can find a `v-img example here </components/cards/#media-with-text>`_.
      light (boolean):
        Applies the light theme variant to the component.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the **href** or **to** prop.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      nuxt (boolean):
        Specifies the link is a `nuxt-link`. For use with the `nuxt framework
        <https://nuxtjs.org/api/components-nuxt-link/>`_.
      outlined (boolean):
        Removes elevation (box-shadow) and adds a *thin* border.
      raised (boolean):
        Specifies a higher default elevation (8dp>`_. You can find more
        information on the `elevation page </styles/elevation>`_.
      replace (boolean):
        Setting **replace** prop will call `router.replace(>`_` instead
        of `router.push(>`_` when clicked, so the navigation will not
        leave a history record. You can find more information about the
        `**replace** prop <https://router.vuejs.org/api/#replace>`_ on
        the vue-router documentation.
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      tag (string):
        Specify a custom tag used on the root element.
      target (string):
        Designates the target attribute. This should only be applied
        when using the **href** prop.
      tile (boolean):
        Removes the component's **border-radius**.
      to (['string', 'object']):
        Denotes the target route of the link. You can find more information
        about the `**to** prop <https://router.vuejs.org/api/#to>`_ on
        the vue-router documentation.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card", children, **kwargs)
        self._attr_names += [
            "active_class",
            "append",
            "color",
            "dark",
            "disabled",
            "elevation",
            "exact",
            "exact_active_class",
            "exact_path",
            "flat",
            "height",
            "hover",
            "href",
            "img",
            "light",
            "link",
            "loader_height",
            "loading",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "nuxt",
            "outlined",
            "raised",
            "replace",
            "ripple",
            "rounded",
            "shaped",
            "tag",
            "target",
            "tile",
            "to",
            "width",
        ]
        self._event_names += [
            "click",
        ]


class VCardActions(HtmlElement):
    """
    Vuetify's VCardActions component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-actions>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card-actions", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCardSubtitle(HtmlElement):
    """
    Vuetify's VCardSubtitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-subtitle>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card-subtitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCardText(HtmlElement):
    """
    Vuetify's VCardText component.
    See more `info and examples <https://vuetifyjs.com/api/v-card-text>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-card-text", children, **kwargs)
        self._attr_names += [
            "tag",
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
        super().__init__("v-card-title", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCarousel(HtmlElement):
    """
    Vuetify's VCarousel component.
    See more `info and examples <https://vuetifyjs.com/api/v-carousel>`_.

    Args:
      active_class (string):
        The **active-class** applied to children when they are activated.
      continuous (boolean):
        Determines whether carousel is continuous
      cycle (boolean):
        Determines if the carousel should cycle through images.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      delimiter_icon (string):
        Sets icon for carousel delimiter
      height (['number', 'string']):
        Sets the height for the component
      hide_delimiter_background (boolean):
        Hides the bottom delimiter background.
      hide_delimiters (boolean):
        Hides the carousel's bottom delimiters.
      interval (['number', 'string']):
        The duration between image cycles. Requires the **cycle** prop.
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max (['number', 'string']):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allow multiple selections. The **value** prop must be an _array_.
      next_icon (['boolean', 'string']):
        The displayed icon for forcing pagination to the next item.
      prev_icon (['boolean', 'string']):
        The displayed icon for forcing pagination to the previous item.
      progress (boolean):
        Displays a carousel progress bar. Requires the **cycle** prop and **interval**.
      progress_color (string):
        Applies specified color to progress bar.
      reverse (boolean):
        Reverse the normal transition direction.
      show_arrows (boolean):
        Displays arrows for next/previous navigation.
      show_arrows_on_hover (boolean):
        Displays navigation arrows only when the carousel is hovered over.
      tag (string):
        Specify a custom tag used on the root element.
      touch (object):
        Provide a custom **left** and **right** function when swiped left or right.
      touchless (boolean):
        Disable touch support.
      value (any):
        The designated model value for the component.
      value_comparator (function):
        Apply a custom value comparator function
      vertical (boolean):
        Uses a vertical transition when changing windows.
      vertical_delimiters (string):
        Displays carousel delimiters vertically.
      change (event):
        Emitted when the component value is changed by user interaction
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-carousel", children, **kwargs)
        self._attr_names += [
            "active_class",
            "continuous",
            "cycle",
            "dark",
            "delimiter_icon",
            "height",
            "hide_delimiter_background",
            "hide_delimiters",
            "interval",
            "light",
            "mandatory",
            "max",
            "multiple",
            "next_icon",
            "prev_icon",
            "progress",
            "progress_color",
            "reverse",
            "show_arrows",
            "show_arrows_on_hover",
            "tag",
            "touch",
            "touchless",
            "value",
            "value_comparator",  # JS functions unimplemented
            "vertical",
            "vertical_delimiters",
        ]
        self._event_names += [
            "change",
        ]


class VCarouselItem(HtmlElement):
    """
    Vuetify's VCarouselItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-carousel-item>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      append (boolean):
        Setting **append** prop always appends the relative path to the
        current path. You can find more information about the `**append**
        prop <https://router.vuejs.org/api/#append>`_ on the vue-router
        documentation.
      disabled (boolean):
        Removes the ability to click or target the component.
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the `**exact** prop <https://router.vuejs.org/api/#exact>`_
        on the vue-router documentation.
      exact_active_class (string):
        Configure the active CSS class applied when the link is active
        with exact match. You can find more information about the `**exact-active-class**
        prop <https://router.vuejs.org/api/#exact-active-class>`_ on
        the vue-router documentation.
      exact_path (boolean):
        Exactly match the link, ignoring the `query` and the `hash` sections.
        You can find more information about the `**exact-path** prop
        <https://router.vuejs.org/api/#exact-path>`_ on the vue-router
        documentation.
      href (['string', 'object']):
        Designates the component as anchor and applies the **href** attribute.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the **href** or **to** prop.
      nuxt (boolean):
        Specifies the link is a `nuxt-link`. For use with the `nuxt framework
        <https://nuxtjs.org/api/components-nuxt-link/>`_.
      replace (boolean):
        Setting **replace** prop will call `router.replace(>`_` instead
        of `router.push(>`_` when clicked, so the navigation will not
        leave a history record. You can find more information about the
        `**replace** prop <https://router.vuejs.org/api/#replace>`_ on
        the vue-router documentation.
      reverse_transition (['boolean', 'string']):
        Sets the reverse transition
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      tag (string):
        Specify a custom tag used on the root element.
      target (string):
        Designates the target attribute. This should only be applied
        when using the **href** prop.
      to (['string', 'object']):
        Denotes the target route of the link. You can find more information
        about the `**to** prop <https://router.vuejs.org/api/#to>`_ on
        the vue-router documentation.
      transition (['boolean', 'string']):
        The transition used when the component progressing through items.
        Can be one of the `built in transitions </styles/transitions>`_
        or one your own.
      value (any):
        The value used when the component is selected in a group. If
        not provided, the index will be used.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-carousel-item", children, **kwargs)
        self._attr_names += [
            "active_class",
            "append",
            "disabled",
            "eager",
            "exact",
            "exact_active_class",
            "exact_path",
            "href",
            "link",
            "nuxt",
            "replace",
            "reverse_transition",
            "ripple",
            "tag",
            "target",
            "to",
            "transition",
            "value",
        ]
        self._event_names += []


class VCheckbox(HtmlElement):
    """
    Vuetify's VCheckbox component.
    See more `info and examples <https://vuetifyjs.com/api/v-checkbox>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      background_color (string):
        Changes the background-color of the input
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the input height
      disabled (boolean):
        Disable the input
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      false_value (any):
        Sets value for falsy state
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      indeterminate (boolean):
        Sets an indeterminate state for the checkbox
      indeterminate_icon (string):
        The icon used when in an indeterminate state
      input_value (any):
        The **v-model** bound value
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      multiple (boolean):
        Changes expected model to an array
      off_icon (string):
        The icon used when inactive
      on_icon (string):
        The icon used when active
      persistent_hint (boolean):
        Forces hint to always be visible
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      true_value (any):
        Sets value for truthy state
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      value_comparator (function):
        Apply a custom value comparator function
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      update_error (event):
        The `error.sync` event
      update_indeterminate (event):
        The **indeterminate.sync** event.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-checkbox", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "background_color",
            "color",
            "dark",
            "dense",
            "disabled",
            "error",
            "error_count",
            "error_messages",
            "false_value",
            "hide_details",
            "hint",
            "id",
            "indeterminate",
            "indeterminate_icon",
            "input_value",
            "label",
            "light",
            "messages",
            "multiple",
            "off_icon",
            "on_icon",
            "persistent_hint",
            "prepend_icon",
            "readonly",
            "ripple",
            "rules",
            "success",
            "success_messages",
            "true_value",
            "validate_on_blur",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_prepend", "click:prepend"),
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
            ("update_indeterminate", "update:indeterminate"),
        ]


class VSimpleCheckbox(HtmlElement):
    """
    Vuetify's VSimpleCheckbox component.
    See more `info and examples <https://vuetifyjs.com/api/v-simple-checkbox>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Disables simple checkbox.
      indeterminate (boolean):
        Sets an indeterminate state for the simple checkbox.
      indeterminate_icon (string):
        The icon used when in an indeterminate state.
      light (boolean):
        Applies the light theme variant to the component.
      off_icon (string):
        The icon used when inactive.
      on_icon (string):
        The icon used when active.
      ripple (boolean):
        Applies the `v-ripple </directives/ripple>`_ directive.
      value (boolean):
        A boolean value that represents whether the simple checkbox is checked.
      input (event):
        The updated bound model
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-simple-checkbox", children, **kwargs)
        self._attr_names += [
            "color",
            "dark",
            "disabled",
            "indeterminate",
            "indeterminate_icon",
            "light",
            "off_icon",
            "on_icon",
            "ripple",
            "value",
        ]
        self._event_names += [
            "input",
        ]


class VChip(HtmlElement):
    """
    Vuetify's VChip component.
    See more `info and examples <https://vuetifyjs.com/api/v-chip>`_.

    Args:
      active (boolean):
        Determines whether the chip is visible or not.
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      append (boolean):
        Setting **append** prop always appends the relative path to the
        current path. You can find more information about the `**append**
        prop <https://router.vuejs.org/api/#append>`_ on the vue-router
        documentation.
      close (boolean):
        Adds remove button
      close_icon (string):
        Change the default icon used for **close** chips
      close_label (string):
        Text used for *aria-label* on the close button in **close** chips.
        Can also be customized globally in `Internationalization </customization/internationalization>`_.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Disables the chip, making it un-selectable
      draggable (boolean):
        Makes the chip draggable
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the `**exact** prop <https://router.vuejs.org/api/#exact>`_
        on the vue-router documentation.
      exact_active_class (string):
        Configure the active CSS class applied when the link is active
        with exact match. You can find more information about the `**exact-active-class**
        prop <https://router.vuejs.org/api/#exact-active-class>`_ on
        the vue-router documentation.
      exact_path (boolean):
        Exactly match the link, ignoring the `query` and the `hash` sections.
        You can find more information about the `**exact-path** prop
        <https://router.vuejs.org/api/#exact-path>`_ on the vue-router
        documentation.
      filter (boolean):
        Displays a selection icon when selected
      filter_icon (string):
        Change the default icon used for **filter** chips
      href (['string', 'object']):
        Designates the component as anchor and applies the **href** attribute.
      input_value (any):
        Controls the **active** state of the item. This is typically
        used to highlight the component.
      label (boolean):
        Removes circle edges
      large (boolean):
        Makes the component large.
      light (boolean):
        Applies the light theme variant to the component.
      link (boolean):
        Explicitly define the chip as a link
      nuxt (boolean):
        Specifies the link is a `nuxt-link`. For use with the `nuxt framework
        <https://nuxtjs.org/api/components-nuxt-link/>`_.
      outlined (boolean):
        Removes background and applies border and text color
      pill (boolean):
        Remove `v-avatar` padding
      replace (boolean):
        Setting **replace** prop will call `router.replace(>`_` instead
        of `router.push(>`_` when clicked, so the navigation will not
        leave a history record. You can find more information about the
        `**replace** prop <https://router.vuejs.org/api/#replace>`_ on
        the vue-router documentation.
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      small (boolean):
        Makes the component small.
      tag (string):
        Specify a custom tag used on the root element.
      target (string):
        Designates the target attribute. This should only be applied
        when using the **href** prop.
      text_color (string):
        Applies a specified color to the control text
      to (['string', 'object']):
        Denotes the target route of the link. You can find more information
        about the `**to** prop <https://router.vuejs.org/api/#to>`_ on
        the vue-router documentation.
      value (any):
        The value used when a child of a `v-chip-group </components/chip-groups>`_.
      x_large (boolean):
        Makes the component extra large.
      x_small (boolean):
        Makes the component extra small.
      click_close (event):
        Emitted when close icon is clicked
      input (event):
        The updated bound model
      update_active (event):
        Emitted when close icon is clicked, sets active to `false`
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-chip", children, **kwargs)
        self._attr_names += [
            "active",
            "active_class",
            "append",
            "close",
            "close_icon",
            "close_label",
            "color",
            "dark",
            "disabled",
            "draggable",
            "exact",
            "exact_active_class",
            "exact_path",
            "filter",
            "filter_icon",
            "href",
            "input_value",
            "label",
            "large",
            "light",
            "link",
            "nuxt",
            "outlined",
            "pill",
            "replace",
            "ripple",
            "small",
            "tag",
            "target",
            "text_color",
            "to",
            "value",
            "x_large",
            "x_small",
        ]
        self._event_names += [
            "click",
            ("click_close", "click:close"),
            "input",
            ("update_active", "update:active"),
        ]


class VChipGroup(HtmlElement):
    """
    Vuetify's VChipGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-chip-group>`_.

    Args:
      active_class (string):
        The **active-class** applied to children when they are activated.
      center_active (boolean):
        Forces the selected chip to be centered
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      column (boolean):
        Remove horizontal pagination and wrap items as needed
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max (['number', 'string']):
        Sets a maximum number of selections that can be made.
      mobile_breakpoint (['number', 'string']):
        Sets the designated mobile breakpoint for the component.
      multiple (boolean):
        Allow multiple selections. The **value** prop must be an _array_.
      next_icon (string):
        Specify the icon to use for the next icon
      prev_icon (string):
        Specify the icon to use for the prev icon
      show_arrows (['boolean', 'string']):
        Force the display of the pagination arrows
      tag (string):
        Specify a custom tag used on the root element.
      value (any):
        The designated model value for the component.
      value_comparator (function):
        Apply a custom value comparator function
      change (event):
        Emitted when the component value is changed by user interaction
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-chip-group", children, **kwargs)
        self._attr_names += [
            "active_class",
            "center_active",
            "color",
            "column",
            "dark",
            "light",
            "mandatory",
            "max",
            "mobile_breakpoint",
            "multiple",
            "next_icon",
            "prev_icon",
            "show_arrows",
            "tag",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "change",
        ]


class VColorPicker(HtmlElement):
    """
    Vuetify's VColorPicker component.
    See more `info and examples <https://vuetifyjs.com/api/v-color-picker>`_.

    Args:
      canvas_height (['string', 'number']):
        Height of canvas
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Disables picker
      dot_size (['number', 'string']):
        Changes the size of the selection dot on the canvas
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      flat (boolean):
        Removes elevation
      hide_canvas (boolean):
        Hides canvas
      hide_inputs (boolean):
        Hides inputs
      hide_mode_switch (boolean):
        Hides mode switch
      hide_sliders (boolean):
        Hides sliders
      light (boolean):
        Applies the light theme variant to the component.
      mode (string):
        Sets mode of inputs. Available modes are 'rgba', 'hsla', and
        'hexa'. Can be synced with the `.sync` modifier.
      show_swatches (boolean):
        Displays color swatches
      swatches (array):
        Sets the available color swatches to select from - This prop
        only accepts rgba hex strings
      swatches_max_height (['number', 'string']):
        Sets the maximum height of the swatches section
      value (['object', 'string']):
        Current color. This can be either a string representing a hex
        color, or an object representing a RGBA, HSLA, or HSVA value
      width (['number', 'string']):
        Sets the width of the color picker
      input (event):
        Selected color. Depending on what you passed to the `value` prop
        this is either a string or an object
      update_color (event):
        Selected color. This is the internal representation of the color,
        containing all values.
      update_mode (event):
        Selected mode
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-color-picker", children, **kwargs)
        self._attr_names += [
            "canvas_height",
            "dark",
            "disabled",
            "dot_size",
            "elevation",
            "flat",
            "hide_canvas",
            "hide_inputs",
            "hide_mode_switch",
            "hide_sliders",
            "light",
            "mode",
            "show_swatches",
            "swatches",
            "swatches_max_height",
            "value",
            "width",
        ]
        self._event_names += [
            "input",
            ("update_color", "update:color"),
            ("update_mode", "update:mode"),
        ]


class VContent(HtmlElement):
    """
    Vuetify's VContent component.
    See more `info and examples <https://vuetifyjs.com/api/v-content>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-content", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VCombobox(HtmlElement):
    """
    Vuetify's VCombobox component.
    See more `info and examples <https://vuetifyjs.com/api/v-combobox>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      append_outer_icon (string):
        Appends an icon to the outside the component's input, uses same
        syntax as `v-icon`
      attach (any):
        Specifies which DOM element that this component should detach
        to. String can be any valid querySelector and Object can be any
        valid Node. This will attach to the root `v-app` component by
        default.
      auto_select_first (boolean):
        When searching, will always highlight the first option
      autofocus (boolean):
        Enables autofocus
      background_color (string):
        Changes the background-color of the input
      cache_items (boolean):
        Keeps a local _unique_ copy of all items that have been passed
        through the **items** prop.
      chips (boolean):
        Changes display of selections to chips
      clear_icon (string):
        Applied when using **clearable** and the input is dirty
      clearable (boolean):
        Add input clear functionality, default icon is Material Design
        Icons **mdi-clear**
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      counter (['boolean', 'number', 'string']):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      counter_value (function):

      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      deletable_chips (boolean):
        Adds a remove icon to selected chips
      delimiters (array):
        Accepts an array of strings that will trigger a new tag when
        typing. Does not replace the normal Tab and Enter keys.
      dense (boolean):
        Reduces the input height
      disable_lookup (boolean):
        Disables keyboard lookup
      disabled (boolean):
        Disables the input
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      filled (boolean):
        Applies the alternate filled input style
      filter (function):
        The function used for filtering items
      flat (boolean):
        Removes elevation (shadow) added to element when using the **solo**
        or **solo-inverted** props
      full_width (boolean):
        Designates input type as full-width
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      hide_selected (boolean):
        Do not display in the select menu items that are already selected.
        Also removes checkboxes from the list when multiple
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      item_color (string):
        Sets color of selected items
      item_disabled (['string', 'array', 'function']):
        Set property of **items**'s disabled value
      item_text (['string', 'array', 'function']):
        Set property of **items**'s text value
      item_value (['string', 'array', 'function']):
        Set property of **items**'s value - **must be primitive**. Dot
        notation is supported. **Note:** This is currently not supported
        with `v-combobox` `GitHub Issue <https://github.com/vuetifyjs/vuetify/issues/5479>`_
      items (array):
        Can be an array of objects or array of strings. When using objects,
        will look for a text, value and disabled keys. This can be changed
        using the **item-text**, **item-value** and **item-disabled**
        props.  Objects that have a **header** or **divider** property
        are considered special cases and generate a list header or divider;
        these items are not selectable.
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      menu_props (['string', 'array', 'object']):
        Pass props through to the `v-menu` component. Accepts either
        a string for boolean props `menu-props="auto, overflowY"`, or
        an object `:menu-props="{ auto: true, overflowY: true }"`
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      multiple (boolean):
        Changes select to multiple. Accepts array for value
      no_data_text (string):
        Display text when there is no data
      no_filter (boolean):
        Do not apply filtering when searching. Useful when data is being
        filtered server side
      open_on_clear (boolean):
        When using the **clearable** prop, once cleared, the select menu
        will either open or stay open, depending on the current state
      outlined (boolean):
        Applies the outlined style to the input
      persistent_hint (boolean):
        Forces hint to always be visible
      persistent_placeholder (boolean):
        Forces placeholder to always be visible
      placeholder (string):
        Sets the input's placeholder text
      prefix (string):
        Displays prefix text
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      prepend_inner_icon (string):
        Prepends an icon inside the component's input, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**
      reverse (boolean):
        Reverses the input orientation
      rounded (boolean):
        Adds a border radius to the input
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      search_input (string):
        Use the **.sync** modifier to catch user input from the search input
      shaped (boolean):
        Round if `outlined` and increase `border-radius` if `filled`.
        Must be used with either `outlined` or `filled`
      single_line (boolean):
        Label does not move on focus/dirty
      small_chips (boolean):
        Changes display of selections to chips with the **small** property
      solo (boolean):
        Changes the style of the input
      solo_inverted (boolean):
        Reduces element opacity until focused
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      suffix (string):
        Displays suffix text
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      value_comparator (function):
        The comparison algorithm used for values. `More info <https://github.com/vuetifyjs/vuetify/blob/v2-stable/packages/vuetify/src/util/helpers.ts>`_
      blur (event):
        Emitted when the input is blurred
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_append-outer (event):
        Emitted when appended outer icon is clicked
      click_clear (event):
        Emitted when clearable icon clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      click_prepend-inner (event):
        Emitted when prepended inner icon is clicked
      focus (event):
        Emitted when component is focused
      input (event):
        The updated bound model
      keydown (event):
        Emitted when **any** key is pressed
      update_error (event):
        The `error.sync` event
      update_list-index (event):
        Emitted when menu item is selected using keyboard arrows
      update_search-input (event):
        The `search-input.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-combobox", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "append_outer_icon",
            "attach",
            "auto_select_first",
            "autofocus",
            "background_color",
            "cache_items",
            "chips",
            "clear_icon",
            "clearable",
            "color",
            "counter",
            "counter_value",  # JS functions unimplemented
            "dark",
            "deletable_chips",
            "delimiters",
            "dense",
            "disable_lookup",
            "disabled",
            "eager",
            "error",
            "error_count",
            "error_messages",
            "filled",
            "filter",  # JS functions unimplemented
            "flat",
            "full_width",
            "height",
            "hide_details",
            "hide_no_data",
            "hide_selected",
            "hint",
            "id",
            "item_color",
            "item_disabled",  # JS functions unimplemented
            "item_text",  # JS functions unimplemented
            "item_value",  # JS functions unimplemented
            "items",
            "label",
            "light",
            "loader_height",
            "loading",
            "menu_props",
            "messages",
            "multiple",
            "no_data_text",
            "no_filter",
            "open_on_clear",
            "outlined",
            "persistent_hint",
            "persistent_placeholder",
            "placeholder",
            "prefix",
            "prepend_icon",
            "prepend_inner_icon",
            "readonly",
            "return_object",
            "reverse",
            "rounded",
            "rules",
            "search_input",
            "shaped",
            "single_line",
            "small_chips",
            "solo",
            "solo_inverted",
            "success",
            "success_messages",
            "suffix",
            "validate_on_blur",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "blur",
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_append_outer", "click:append-outer"),
            ("click_clear", "click:clear"),
            ("click_prepend", "click:prepend"),
            ("click_prepend_inner", "click:prepend-inner"),
            "focus",
            "input",
            "keydown",
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
            ("update_list_index", "update:list-index"),
            ("update_search_input", "update:search-input"),
        ]


class VDataIterator(HtmlElement):
    """
    Vuetify's VDataIterator component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-iterator>`_.

    Args:
      checkbox_color (string):

      custom_filter (function):
        Function to filter items
      custom_group (function):
        Function used to group items
      custom_sort (function):
        Function used to sort items
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disable_filtering (boolean):
        Disables filtering completely
      disable_pagination (boolean):
        Disables pagination completely
      disable_sort (boolean):
        Disables sorting completely
      expanded (array):
        Array of expanded items. Can be used with `.sync` modifier
      footer_props (object):
        See the ``v-data-footer` </api/v-data-footer>`_ API for more information
      group_by (['string', 'array']):
        Changes which item property should be used for grouping items.
        Currently only supports a single grouping in the format: `group`
        or `['group']`. When using an array, only the first element is
        considered. Can be used with `.sync` modifier
      group_desc (['boolean', 'array']):
        Changes which direction grouping is done. Can be used with `.sync` modifier
      hide_default_footer (boolean):
        Hides default footer
      item_key (string):
        The property on each item that is used as a unique key
      items (array):
        The array of items to display
      items_per_page (number):
        Changes how many items per page should be visible. Can be used
        with `.sync` modifier. Setting this prop to `-1` will display
        all items on the page
      light (boolean):
        Applies the light theme variant to the component.
      loading (['boolean', 'string']):
        If `true` and no items are provided, then a loading text will be shown
      loading_text (string):
        Text shown when `loading` is true and no items are provided
      locale (string):
        Sets the locale used for sorting. This is passed into ``Intl.Collator(>`_`
        <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator/Collator>`_
        in the default `customSort` function
      mobile_breakpoint (['number', 'string']):
        Used to set when to toggle between regular table and mobile view
      multi_sort (boolean):
        If `true` then one can sort on multiple properties
      must_sort (boolean):
        If `true` then one can not disable sorting, it will always switch
        between ascending and descending
      no_data_text (string):
        Text shown when no items are provided to the component
      no_results_text (string):
        Text shown when `search` prop is used and there are no results
      options (DataOptions):

      page (number):

      search (string):
        Text input used to filter items
      selectable_key (string):
        The property on each item that is used to determine if it is selectable or not
      server_items_length (number):
        Used only when data is provided by a server. Should be set to
        the total amount of items available on server so that pagination
        works correctly
      single_expand (boolean):
        Changes expansion mode to single expand
      single_select (boolean):
        Changes selection mode to single select
      sort_by (['string', 'array']):
        Changes which item property (or properties) should be used for
        sort order. Can be used with `.sync` modifier
      sort_desc (['boolean', 'array']):
        Changes which direction sorting is done. Can be used with `.sync` modifier
      value (array):
        Used for controlling selected rows
      current-items (event):
        Emits the items provided via the **items** prop, every time the
        internal **computedItems** is changed.
      input (event):
        Array of selected items
      item-expanded (event):
        Event emitted when an item is expanded or closed
      item-selected (event):
        Event emitted when an item is selected or deselected
      page-count (event):
        Emits when the **pageCount** property of the **pagination** prop is updated
      pagination (event):
        Emits when something changed to the `pagination` which can be
        provided via the `pagination` prop
      toggle-select-all (event):
        Emits when the `select-all` checkbox in table header is clicked.
        This checkbox is enabled by the **show-select** prop
      update_expanded (event):
        The `.sync` event for `expanded` prop
      update_group-by (event):
        Emits when the **group-by** property of the **options** property is updated
      update_group-desc (event):
        Emits when the **group-desc** property of the **options** prop is updated
      update_items-per-page (event):
        Emits when the **items-per-page** property of the **options** prop is updated
      update_multi-sort (event):
        Emits when the **multi-sort** property of the **options** prop is updated
      update_must-sort (event):
        Emits when the **must-sort** property of the **options** prop is updated
      update_options (event):
        Emits when one of the **options** properties is updated
      update_page (event):
        Emits when the **page** property of the **options** prop is updated
      update_sort-by (event):
        Emits when the **sort-by** property of the **options** prop is updated
      update_sort-desc (event):
        Emits when the **sort-desc** property of the **options** prop is updated
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-data-iterator", children, **kwargs)
        self._attr_names += [
            "checkbox_color",
            "custom_filter",  # JS functions unimplemented
            "custom_group",  # JS functions unimplemented
            "custom_sort",  # JS functions unimplemented
            "dark",
            "disable_filtering",
            "disable_pagination",
            "disable_sort",
            "expanded",
            "footer_props",
            "group_by",
            "group_desc",
            "hide_default_footer",
            "item_key",
            "items",
            "items_per_page",
            "light",
            "loading",
            "loading_text",
            "locale",
            "mobile_breakpoint",
            "multi_sort",
            "must_sort",
            "no_data_text",
            "no_results_text",
            "options",
            "page",
            "search",
            "selectable_key",
            "server_items_length",
            "single_expand",
            "single_select",
            "sort_by",
            "sort_desc",
            "value",
        ]
        self._event_names += [
            ("current_items", "current-items"),
            "input",
            ("item_expanded", "item-expanded"),
            ("item_selected", "item-selected"),
            ("page_count", "page-count"),
            "pagination",
            ("toggle_select_all", "toggle-select-all"),
            ("update_expanded", "update:expanded"),
            ("update_group_by", "update:group-by"),
            ("update_group_desc", "update:group-desc"),
            ("update_items_per_page", "update:items-per-page"),
            ("update_multi_sort", "update:multi-sort"),
            ("update_must_sort", "update:must-sort"),
            ("update_options", "update:options"),
            ("update_page", "update:page"),
            ("update_sort_by", "update:sort-by"),
            ("update_sort_desc", "update:sort-desc"),
        ]


class VDataFooter(HtmlElement):
    """
    Vuetify's VDataFooter component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-footer>`_.

    Args:
      disable_items_per_page (boolean):
        Disables items-per-page dropdown
      disable_pagination (boolean):
        Disables pagination buttons
      first_icon (string):
        First icon
      items_per_page_all_text (string):
        Text for 'All' option in items-per-page dropdown
      items_per_page_options (array):
        Array of options to show in the items-per-page dropdown
      items_per_page_text (string):
        Text for items-per-page dropdown
      last_icon (string):
        Last icon
      next_icon (string):
        Next icon
      options (object):
        DataOptions
      page_text (string):

      pagination (object):
        DataPagination
      prev_icon (string):
        Previous icon
      show_current_page (boolean):
        Show current page number between prev/next icons
      show_first_last_page (boolean):
        Show first/last icons
      update_options (event):
        The `.sync` event for `options` prop
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-data-footer", children, **kwargs)
        self._attr_names += [
            "disable_items_per_page",
            "disable_pagination",
            "first_icon",
            "items_per_page_all_text",
            "items_per_page_options",
            "items_per_page_text",
            "last_icon",
            "next_icon",
            "options",
            "page_text",
            "pagination",
            "prev_icon",
            "show_current_page",
            "show_first_last_page",
        ]
        self._event_names += [
            ("update_options", "update:options"),
        ]


class VDataTable(HtmlElement):
    """
    Vuetify's VDataTable component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table>`_.

    Args:
      calculate_widths (boolean):
        Enables calculation of column widths. `widths` property will
        be available in select scoped slots
      caption (string):
        Set the caption (using `<caption>`)
      checkbox_color (string):
        Set the color of the checkboxes (showSelect must be used)
      custom_filter (function):
        Function to filter items
      custom_group (function):
        Function used to group items
      custom_sort (function):
        Function used to sort items
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Decreases the height of rows
      disable_filtering (boolean):
        Disables filtering completely
      disable_pagination (boolean):
        Disables pagination completely
      disable_sort (boolean):
        Disables sorting completely
      expand_icon (string):
        Icon used for expand toggle button.
      expanded (array):
        Array of expanded items. Can be used with `.sync` modifier
      filter_mode (string):
        Controls how how custom column filters are combined with the
        default filtering. Both modes only apply the default filter to
        columns not specified in `customKeyFilter`.  - **union**: There
        is at least one match from the default filter, OR all custom
        column filters match. - **intersection**: There is at least one
        match from the default filter, AND all custom column filters
        match.
      fixed_header (boolean):
        Fixed header to top of table. **NOTE:** Does not work in IE11
      footer_props (object):
        See the ``v-data-footer` </api/v-data-footer>`_ API for more information
      group_by (['string', 'array']):
        Changes which item property should be used for grouping items.
        Currently only supports a single grouping in the format: `group`
        or `['group']`. When using an array, only the first element is
        considered. Can be used with `.sync` modifier
      group_desc (['boolean', 'array']):
        Changes which direction grouping is done. Can be used with `.sync` modifier
      header_props (object):
        Pass props to the default header. See ``v-data-table-header`
        API </api/v-data-table-header>`_ for more information
      headers (DataTableHeader[]):
        An array of objects that each describe a header column. See the
        example below for a definition of all properties
      headers_length (number):
        Can be used in combination with `hide-default-header` to specify
        the number of columns in the table to allow expansion rows and
        loading bar to function properly
      height (['number', 'string']):
        Set an explicit height of table
      hide_default_footer (boolean):
        Hides default footer
      hide_default_header (boolean):
        Hide the default headers
      item_class (['string', 'function']):
        Property on supplied `items` that contains item's row class or
        function that takes an item as an argument and returns the class
        of corresponding row
      item_key (string):
        The property on each item that is used as a unique key
      item_style (['string', 'function']):

      items (array):
        The array of items to display
      items_per_page (number):
        Changes how many items per page should be visible. Can be used
        with `.sync` modifier. Setting this prop to `-1` will display
        all items on the page
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        If `true` and no items are provided, then a loading text will be shown
      loading_text (string):
        Text shown when `loading` is true and no items are provided
      locale (string):
        Sets the locale used for sorting. This is passed into ``Intl.Collator(>`_`
        <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator/Collator>`_
        in the default `customSort` function
      mobile_breakpoint (['number', 'string']):
        Used to set when to toggle between regular table and mobile view
      multi_sort (boolean):
        If `true` then one can sort on multiple properties
      must_sort (boolean):
        If `true` then one can not disable sorting, it will always switch
        between ascending and descending
      no_data_text (string):
        Text shown when no items are provided to the component
      no_results_text (string):
        Text shown when `search` prop is used and there are no results
      options (DataOptions):

      page (number):
        The current displayed page number (1-indexed)
      search (string):
        Text input used to filter items
      selectable_key (string):
        The property on each item that is used to determine if it is selectable or not
      server_items_length (number):
        Used only when data is provided by a server. Should be set to
        the total amount of items available on server so that pagination
        works correctly
      show_expand (boolean):
        Shows the expand toggle in default rows
      show_group_by (boolean):
        Shows the group by toggle in the header and enables grouped rows
      show_select (boolean):
        Shows the select checkboxes in both the header and rows (if using default rows)
      single_expand (boolean):
        Changes expansion mode to single expand
      single_select (boolean):
        Changes selection mode to single select
      sort_by (['string', 'array']):
        Changes which item property (or properties) should be used for
        sort order. Can be used with `.sync` modifier
      sort_desc (['boolean', 'array']):
        Changes which direction sorting is done. Can be used with `.sync` modifier
      value (array):
        Used for controlling selected rows
      click_row (event):
        Emits when a table row is clicked. This event provides 3 arguments:
        the first is the item data that was clicked, the second is the
        other related data provided by the `item` slot, and the third
        is the native click event. **NOTE:** will not emit when table
        rows are defined through a slot such as `item` or `body`.
      current-items (event):
        Emits the items provided via the **items** prop, every time the
        internal **computedItems** is changed.
      input (event):
        Array of selected items
      item-expanded (event):
        Event emitted when an item is expanded or closed
      item-selected (event):
        Event emitted when an item is selected or deselected
      page-count (event):
        Emits when the **pageCount** property of the **pagination** prop is updated
      pagination (event):
        Emits when something changed to the `pagination` which can be
        provided via the `pagination` prop
      toggle-select-all (event):
        Emits when the `select-all` checkbox in table header is clicked.
        This checkbox is enabled by the **show-select** prop
      update_expanded (event):
        The `.sync` event for `expanded` prop
      update_group-by (event):
        Emits when the **group-by** property of the **options** property is updated
      update_group-desc (event):
        Emits when the **group-desc** property of the **options** prop is updated
      update_items-per-page (event):
        Emits when the **items-per-page** property of the **options** prop is updated
      update_multi-sort (event):
        Emits when the **multi-sort** property of the **options** prop is updated
      update_must-sort (event):
        Emits when the **must-sort** property of the **options** prop is updated
      update_options (event):
        Emits when one of the **options** properties is updated
      update_page (event):
        Emits when the **page** property of the **options** prop is updated
      update_sort-by (event):
        Emits when the **sort-by** property of the **options** prop is updated
      update_sort-desc (event):
        Emits when the **sort-desc** property of the **options** prop is updated
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-data-table", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            "calculate_widths",
            "caption",
            "checkbox_color",
            "custom_filter",  # JS functions unimplemented
            "custom_group",  # JS functions unimplemented
            "custom_sort",  # JS functions unimplemented
            "dark",
            "dense",
            "disable_filtering",
            "disable_pagination",
            "disable_sort",
            "expand_icon",
            "expanded",
            "filter_mode",
            "fixed_header",
            "footer_props",
            "group_by",
            "group_desc",
            "header_props",
            "headers",
            "headers_length",
            "height",
            "hide_default_footer",
            "hide_default_header",
            "item_class",  # JS functions unimplemented
            "item_key",
            "item_style",  # JS functions unimplemented
            "items",
            "items_per_page",
            "light",
            "loader_height",
            "loading",
            "loading_text",
            "locale",
            "mobile_breakpoint",
            "multi_sort",
            "must_sort",
            "no_data_text",
            "no_results_text",
            "options",
            "page",
            "search",
            "selectable_key",
            "server_items_length",
            "show_expand",
            "show_group_by",
            "show_select",
            "single_expand",
            "single_select",
            "sort_by",
            "sort_desc",
            "value",
        ]
        self._event_names += [
            ("click_date", "click:date"),
            ("click_month", "click:month"),
            ("click_year", "click:year"),
            ("dblclick_date", "dblclick:date"),
            ("dblclick_month", "dblclick:month"),
            ("dblclick_year", "dblclick:year"),
            ("mousedown_date", "mousedown:date"),
            ("mousedown_month", "mousedown:month"),
            ("mousedown_year", "mousedown:year"),
            ("mouseenter_date", "mouseenter:date"),
            ("mouseenter_month", "mouseenter:month"),
            ("mouseenter_year", "mouseenter:year"),
            ("mouseleave_date", "mouseleave:date"),
            ("mouseleave_month", "mouseleave:month"),
            ("mouseleave_year", "mouseleave:year"),
            ("mousemove_date", "mousemove:date"),
            ("mousemove_month", "mousemove:month"),
            ("mousemove_year", "mousemove:year"),
            ("mouseover_date", "mouseover:date"),
            ("mouseover_month", "mouseover:month"),
            ("mouseover_year", "mouseover:year"),
            ("mouseout_date", "mouseout:date"),
            ("mouseout_month", "mouseout:month"),
            ("mouseout_year", "mouseout:year"),
            ("mouseup_date", "mouseup:date"),
            ("mouseup_month", "mouseup:month"),
            ("mouseup_year", "mouseup:year"),
            ("focus_date", "focus:date"),
            ("focus_month", "focus:month"),
            ("focus_year", "focus:year"),
            ("click_row", "click:row"),
            ("current_items", "current-items"),
            "input",
            ("item_expanded", "item-expanded"),
            ("item_selected", "item-selected"),
            ("page_count", "page-count"),
            "pagination",
            ("toggle_select_all", "toggle-select-all"),
            ("update_expanded", "update:expanded"),
            ("update_group_by", "update:group-by"),
            ("update_group_desc", "update:group-desc"),
            ("update_items_per_page", "update:items-per-page"),
            ("update_multi_sort", "update:multi-sort"),
            ("update_must_sort", "update:must-sort"),
            ("update_options", "update:options"),
            ("update_page", "update:page"),
            ("update_sort_by", "update:sort-by"),
            ("update_sort_desc", "update:sort-desc"),
        ]


class VEditDialog(HtmlElement):
    """
    Vuetify's VEditDialog component.
    See more `info and examples <https://vuetifyjs.com/api/v-edit-dialog>`_.

    Args:
      cancel_text (any):
        Sets the default text for the cancel button when using the **large** prop
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      large (boolean):
        Attaches a submit and cancel button to the dialog
      light (boolean):
        Applies the light theme variant to the component.
      persistent (boolean):
        Clicking outside or pressing **esc** key will not dismiss the dialog
      return_value (any):

      save_text (any):
        Sets the default text for the save button when using the **large** prop
      transition (string):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      cancel (event):
        Emits when editing is canceled
      close (event):
        Emits when edit-dialog close button is pressed
      open (event):
        Emits when editing is opened
      save (event):
        Emits when edit-dialog save button is pressed
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-edit-dialog", children, **kwargs)
        self._attr_names += [
            "cancel_text",
            "dark",
            "eager",
            "large",
            "light",
            "persistent",
            "return_value",
            "save_text",
            "transition",
        ]
        self._event_names += [
            "cancel",
            "close",
            "open",
            "save",
        ]


class VDataTableHeader(HtmlElement):
    """
    Vuetify's VDataTableHeader component.
    See more `info and examples <https://vuetifyjs.com/api/v-data-table-header>`_.

    Args:
      checkbox_color (string):

      disable_sort (boolean):
        Toggles rendering of sort button
      every_item (boolean):
        Indicates if all items in table are selected
      headers (array):
        Array of header items to display
      mobile (boolean):
        Renders mobile view of headers
      options (object):
        Options object. Identical to the one on `v-data-table`
      show_group_by (boolean):
        Shows group by button
      single_select (boolean):
        Toggles rendering of select-all checkbox
      some_items (boolean):
        Indicates if one or more items in table are selected
      sort_by_text (string):
        Sets the label text used by the default sort-by selector when
        `v-data-table` is rendering the mobile view
      sort_icon (string):
        Icon used for sort button
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-data-table-header", children, **kwargs)
        self._attr_names += [
            "checkbox_color",
            "disable_sort",
            "every_item",
            "headers",
            "mobile",
            "options",
            "show_group_by",
            "single_select",
            "some_items",
            "sort_by_text",
            "sort_icon",
        ]
        self._event_names += []


class VSimpleTable(HtmlElement):
    """
    Vuetify's VSimpleTable component.
    See more `info and examples <https://vuetifyjs.com/api/v-simple-table>`_.

    Args:
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Decreases paddings to render a dense table
      fixed_header (boolean):
        Sets table header to fixed mode
      height (['number', 'string']):
        Sets the height for the component
      light (boolean):
        Applies the light theme variant to the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-simple-table", children, **kwargs)
        self._attr_names += [
            "dark",
            "dense",
            "fixed_header",
            "height",
            "light",
        ]
        self._event_names += []


class VDatePicker(HtmlElement):
    """
    Vuetify's VDatePicker component.
    See more `info and examples <https://vuetifyjs.com/api/v-date-picker>`_.

    Args:
      active_picker (string):
        Determines which picker in the date or month picker is being
        displayed. Allowed values: `'DATE'`, `'MONTH'`, `'YEAR'`
      allowed_dates (function):
        Restricts which dates can be selected
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      day_format (function):
        Allows you to customize the format of the day string that appears
        in the date table. Called with date (ISO 8601 **date** string)
        arguments.
      disabled (boolean):
        Disables interaction with the picker
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      event_color (['array', 'function', 'object', 'string']):
        Sets the color for event dot. It can be string (all events will
        have the same color) or `object` where attribute is the event
        date and value is boolean/color/array of colors for specified
        date or `function` taking date as a parameter and returning boolean/color/array
        of colors for that date
      events (['array', 'function', 'object']):
        Array of dates or object defining events or colors or function
        returning boolean/color/array of colors
      first_day_of_week (['string', 'number']):
        Sets the first day of the week, starting with 0 for Sunday.
      flat (boolean):
        Removes  elevation
      full_width (boolean):
        Forces 100% width
      header_color (string):
        Defines the header color. If not specified it will use the color
        defined by <code>color</code> prop or the default picker color
      header_date_format (function):
        Allows you to customize the format of the month string that appears
        in the header of the calendar. Called with date (ISO 8601 **date**
        string) arguments.
      landscape (boolean):
        Orients picker horizontal
      light (boolean):
        Applies the light theme variant to the component.
      locale (string):
        Sets the locale. Accepts a string with a BCP 47 language tag.
      locale_first_day_of_year (['string', 'number']):
        Sets the day that determines the first week of the year, starting
        with 0 for **Sunday**. For ISO 8601 this should be 4.
      max (string):
        Maximum allowed date/month (ISO 8601 format)
      min (string):
        Minimum allowed date/month (ISO 8601 format)
      month_format (function):
        Formatting function used for displaying months in the months
        table. Called with date (ISO 8601 **date** string) arguments.
      multiple (boolean):
        Allow the selection of multiple dates
      next_icon (string):
        Sets the icon for next month/year button
      next_month_aria_label (string):

      next_year_aria_label (string):

      no_title (boolean):
        Hide the picker title
      picker_date (string):
        Displayed year/month
      prev_icon (string):
        Sets the icon for previous month/year button
      prev_month_aria_label (string):

      prev_year_aria_label (string):

      range (boolean):
        Allow the selection of date range
      reactive (boolean):
        Updates the picker model when changing months/years automatically
      readonly (boolean):
        Makes the picker readonly (doesn't allow to select new date)
      scrollable (boolean):
        Allows changing displayed month with mouse scroll
      selected_items_text (string):
        Text used for translating the number of selected dates when using
        *multiple* prop. Can also be customizing globally in `Internationalization
        </customization/internationalization>`_.
      show_adjacent_months (boolean):
        Toggles visibility of days from previous and next months
      show_current (['boolean', 'string']):
        Toggles visibility of the current date/month outline or shows
        the provided date/month as a current
      show_week (boolean):
        Toggles visibility of the week numbers in the body of the calendar
      title_date_format (function):
        Allows you to customize the format of the date string that appears
        in the title of the date picker. Called with date (ISO 8601 **date**
        string) arguments.
      type (string):
        Determines the type of the picker - `date` for date picker, `month`
        for month picker
      value (['array', 'string']):
        Date picker model (ISO 8601 format, YYYY-mm-dd or YYYY-mm)
      weekday_format (function):
        Allows you to customize the format of the weekday string that
        appears in the body of the calendar. Called with date (ISO 8601
        **date** string) arguments.
      width (['number', 'string']):
        Width of the picker
      year_format (function):
        Allows you to customize the format of the year string that appears
        in the header of the calendar. Called with date (ISO 8601 **date**
        string) arguments.
      year_icon (string):
        Sets the icon in the year selection button
      change (event):
        Reactive date picker emits `input` even when any part of the
        date (year/month/day) changes, but `change` event is emitted
        only when the day (for date pickers) or month (for month pickers)
        changes. If `range` prop is set, date picker emits `change` when
        both [from, to] are selected.
      input (event):
        The updated bound model
      update_active-picker (event):
        The `.sync` event for `active-picker` prop
      update_picker-date (event):
        The `.sync` event for `picker-date` prop
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-date-picker", children, **kwargs)
        self._attr_names += [
            "active_picker",
            "allowed_dates",  # JS functions unimplemented
            "color",
            "dark",
            "day_format",  # JS functions unimplemented
            "disabled",
            "elevation",
            "event_color",  # JS functions unimplemented
            "events",  # JS functions unimplemented
            "first_day_of_week",
            "flat",
            "full_width",
            "header_color",
            "header_date_format",  # JS functions unimplemented
            "landscape",
            "light",
            "locale",
            "locale_first_day_of_year",
            "max",
            "min",
            "month_format",  # JS functions unimplemented
            "multiple",
            "next_icon",
            "next_month_aria_label",
            "next_year_aria_label",
            "no_title",
            "picker_date",
            "prev_icon",
            "prev_month_aria_label",
            "prev_year_aria_label",
            "range",
            "reactive",
            "readonly",
            "scrollable",
            "selected_items_text",
            "show_adjacent_months",
            "show_current",
            "show_week",
            "title_date_format",  # JS functions unimplemented
            "type",
            "value",
            "weekday_format",  # JS functions unimplemented
            "width",
            "year_format",  # JS functions unimplemented
            "year_icon",
        ]
        self._event_names += [
            ("click_date", "click:date"),
            ("click_month", "click:month"),
            ("click_year", "click:year"),
            ("dblclick_date", "dblclick:date"),
            ("dblclick_month", "dblclick:month"),
            ("dblclick_year", "dblclick:year"),
            ("mousedown_date", "mousedown:date"),
            ("mousedown_month", "mousedown:month"),
            ("mousedown_year", "mousedown:year"),
            ("mouseenter_date", "mouseenter:date"),
            ("mouseenter_month", "mouseenter:month"),
            ("mouseenter_year", "mouseenter:year"),
            ("mouseleave_date", "mouseleave:date"),
            ("mouseleave_month", "mouseleave:month"),
            ("mouseleave_year", "mouseleave:year"),
            ("mousemove_date", "mousemove:date"),
            ("mousemove_month", "mousemove:month"),
            ("mousemove_year", "mousemove:year"),
            ("mouseover_date", "mouseover:date"),
            ("mouseover_month", "mouseover:month"),
            ("mouseover_year", "mouseover:year"),
            ("mouseout_date", "mouseout:date"),
            ("mouseout_month", "mouseout:month"),
            ("mouseout_year", "mouseout:year"),
            ("mouseup_date", "mouseup:date"),
            ("mouseup_month", "mouseup:month"),
            ("mouseup_year", "mouseup:year"),
            ("focus_date", "focus:date"),
            ("focus_month", "focus:month"),
            ("focus_year", "focus:year"),
            ("click_date", "click:date"),
            ("click_month", "click:month"),
            ("click_year", "click:year"),
            ("dblclick_date", "dblclick:date"),
            ("dblclick_month", "dblclick:month"),
            ("dblclick_year", "dblclick:year"),
            ("mousedown_date", "mousedown:date"),
            ("mousedown_month", "mousedown:month"),
            ("mousedown_year", "mousedown:year"),
            ("mouseenter_date", "mouseenter:date"),
            ("mouseenter_month", "mouseenter:month"),
            ("mouseenter_year", "mouseenter:year"),
            ("mouseleave_date", "mouseleave:date"),
            ("mouseleave_month", "mouseleave:month"),
            ("mouseleave_year", "mouseleave:year"),
            ("mousemove_date", "mousemove:date"),
            ("mousemove_month", "mousemove:month"),
            ("mousemove_year", "mousemove:year"),
            ("mouseover_date", "mouseover:date"),
            ("mouseover_month", "mouseover:month"),
            ("mouseover_year", "mouseover:year"),
            ("mouseout_date", "mouseout:date"),
            ("mouseout_month", "mouseout:month"),
            ("mouseout_year", "mouseout:year"),
            ("mouseup_date", "mouseup:date"),
            ("mouseup_month", "mouseup:month"),
            ("mouseup_year", "mouseup:year"),
            ("focus_date", "focus:date"),
            ("focus_month", "focus:month"),
            ("focus_year", "focus:year"),
            ("click_date", "click:date"),
            ("click_month", "click:month"),
            ("click_year", "click:year"),
            ("dblclick_date", "dblclick:date"),
            ("dblclick_month", "dblclick:month"),
            ("dblclick_year", "dblclick:year"),
            ("mousedown_date", "mousedown:date"),
            ("mousedown_month", "mousedown:month"),
            ("mousedown_year", "mousedown:year"),
            ("mouseenter_date", "mouseenter:date"),
            ("mouseenter_month", "mouseenter:month"),
            ("mouseenter_year", "mouseenter:year"),
            ("mouseleave_date", "mouseleave:date"),
            ("mouseleave_month", "mouseleave:month"),
            ("mouseleave_year", "mouseleave:year"),
            ("mousemove_date", "mousemove:date"),
            ("mousemove_month", "mousemove:month"),
            ("mousemove_year", "mousemove:year"),
            ("mouseover_date", "mouseover:date"),
            ("mouseover_month", "mouseover:month"),
            ("mouseover_year", "mouseover:year"),
            ("mouseout_date", "mouseout:date"),
            ("mouseout_month", "mouseout:month"),
            ("mouseout_year", "mouseout:year"),
            ("mouseup_date", "mouseup:date"),
            ("mouseup_month", "mouseup:month"),
            ("mouseup_year", "mouseup:year"),
            ("focus_date", "focus:date"),
            ("focus_month", "focus:month"),
            ("focus_year", "focus:year"),
            "change",
            "input",
            ("update_active_picker", "update:active-picker"),
            ("update_picker_date", "update:picker-date"),
        ]


class VDialog(HtmlElement):
    """
    Vuetify's VDialog component.
    See more `info and examples <https://vuetifyjs.com/api/v-dialog>`_.

    Args:
      activator (any):
        Designate a custom activator when the `activator` slot is not
        used. String can be any valid querySelector and Object can be
        any valid Node.
      attach (any):
        Specifies which DOM element that this component should detach
        to. String can be any valid querySelector and Object can be any
        valid Node. This will attach to the root `v-app` component by
        default.
      close_delay (['number', 'string']):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      content_class (string):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Disables the ability to open the component.
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      fullscreen (boolean):
        Changes layout for fullscreen display.
      hide_overlay (boolean):
        Hides the display of the overlay.
      internal_activator (boolean):
        Detaches the menu content inside of the component as opposed to the document.
      light (boolean):
        Applies the light theme variant to the component.
      max_width (['string', 'number']):
        Sets the maximum width for the component.
      no_click_animation (boolean):
        Disables the bounce effect when clicking outside of a `v-dialog`'s
        content when using the **persistent** prop.
      open_delay (['number', 'string']):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      open_on_click (boolean):

      open_on_focus (boolean):

      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
      overlay_color (string):
        Sets the overlay color.
      overlay_opacity (['number', 'string']):
        Sets the overlay opacity.
      persistent (boolean):
        Clicking outside of the element or pressing **esc** key will not deactivate it.
      retain_focus (boolean):
        Tab focus will return to the first child of the dialog by default.
        Disable this when using external tools that require focus such
        as TinyMCE or vue-clipboard.
      return_value (any):

      scrollable (boolean):
        When set to true, expects a `v-card` and a `v-card-text` component
        with a designated height. For more information, check out the
        `scrollable example </components/dialogs#scrollable>`_.
      transition (['string', 'boolean']):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      value (any):
        Controls whether the component is visible or hidden.
      width (['string', 'number']):
        Sets the width for the component.
      click_outside (event):
        Event that fires when clicking outside an active dialog.
      input (event):
        The updated bound model
      keydown (event):
        Event that fires when key is pressed. If dialog is active and
        not using the **persistent** prop, the **esc** key will deactivate
        it.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-dialog", children, **kwargs)
        self._attr_names += [
            "activator",
            "attach",
            "close_delay",
            "content_class",
            "dark",
            "disabled",
            "eager",
            "fullscreen",
            "hide_overlay",
            "internal_activator",
            "light",
            "max_width",
            "no_click_animation",
            "open_delay",
            "open_on_click",
            "open_on_focus",
            "origin",
            "overlay_color",
            "overlay_opacity",
            "persistent",
            "retain_focus",
            "return_value",
            "scrollable",
            "transition",
            "value",
            "width",
        ]
        self._event_names += [
            ("click_outside", "click:outside"),
            "input",
            "keydown",
        ]


class VDivider(HtmlElement):
    """
    Vuetify's VDivider component.
    See more `info and examples <https://vuetifyjs.com/api/v-divider>`_.

    Args:
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      inset (boolean):
        Adds indentation (72px) for **normal** dividers, reduces max
        height for **vertical**.
      light (boolean):
        Applies the light theme variant to the component.
      vertical (boolean):
        Displays dividers vertically
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-divider", children, **kwargs)
        self._attr_names += [
            "dark",
            "inset",
            "light",
            "vertical",
        ]
        self._event_names += []


class VExpansionPanels(HtmlElement):
    """
    Vuetify's VExpansionPanels component.
    See more `info and examples <https://vuetifyjs.com/api/v-expansion-panels>`_.

    Args:
      accordion (boolean):
        Removes the margin around open panels
      active_class (string):
        The **active-class** applied to children when they are activated.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Disables the entire expansion-panel
      flat (boolean):
        Removes the expansion-panel's elevation and borders
      focusable (boolean):
        Makes the expansion-panel headers focusable
      hover (boolean):
        Applies a background-color shift on hover to expansion panel headers
      inset (boolean):
        Makes the expansion-panel open with a inset style
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max (['number', 'string']):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allow multiple selections. The **value** prop must be an _array_.
      popout (boolean):
        Makes the expansion-panel open with an popout style
      readonly (boolean):
        Makes the entire expansion-panel read only.
      tag (string):
        Specify a custom tag used on the root element.
      tile (boolean):
        Removes the border-radius
      value (any):
        Controls the opened/closed state of content in the expansion-panel.
        Corresponds to a zero-based index of the currently opened content.
        If the `multiple` prop (previously `expand` in 1.5.x) is used
        then it is an array of numbers where each entry corresponds to
        the index of the opened content.  The index order is not relevant.
      value_comparator (function):
        Apply a custom value comparator function
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expansion-panels", children, **kwargs)
        self._attr_names += [
            "accordion",
            "active_class",
            "dark",
            "disabled",
            "flat",
            "focusable",
            "hover",
            "inset",
            "light",
            "mandatory",
            "max",
            "multiple",
            "popout",
            "readonly",
            "tag",
            "tile",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += []


class VExpansionPanel(HtmlElement):
    """
    Vuetify's VExpansionPanel component.
    See more `info and examples <https://vuetifyjs.com/api/v-expansion-panel>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      disabled (boolean):
        Disables the expansion-panel content
      readonly (boolean):
        Makes the expansion-panel content read only.
      change (event):
        Toggles the value of the selected panel
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expansion-panel", children, **kwargs)
        self._attr_names += [
            "active_class",
            "disabled",
            "readonly",
        ]
        self._event_names += [
            "change",
            "click",
        ]


class VExpansionPanelHeader(HtmlElement):
    """
    Vuetify's VExpansionPanelHeader component.
    See more `info and examples <https://vuetifyjs.com/api/v-expansion-panel-header>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      disable_icon_rotate (boolean):
        Removes the icon rotation animation when expanding a panel
      expand_icon (string):
        Set the expand action icon
      hide_actions (boolean):
        Hide the expand icon in the content header
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expansion-panel-header", children, **kwargs)
        self._attr_names += [
            "color",
            "disable_icon_rotate",
            "expand_icon",
            "hide_actions",
            "ripple",
        ]
        self._event_names += [
            "click",
        ]


class VExpansionPanelContent(HtmlElement):
    """
    Vuetify's VExpansionPanelContent component.
    See more `info and examples <https://vuetifyjs.com/api/v-expansion-panel-content>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expansion-panel-content", children, **kwargs)
        self._attr_names += [
            "color",
            "eager",
        ]
        self._event_names += []


class VFileInput(HtmlElement):
    """
    Vuetify's VFileInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-file-input>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      append_outer_icon (string):
        Appends an icon to the outside the component's input, uses same
        syntax as `v-icon`
      autofocus (boolean):
        Enables autofocus
      background_color (string):
        Changes the background-color of the input
      chips (boolean):
        Changes display of selections to chips
      clear_icon (string):
        Applied when using **clearable** and the input is dirty
      clearable (boolean):
        Add input clear functionality, default icon is Material Design
        Icons **mdi-clear**
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      counter (['boolean', 'number', 'string']):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      counter_size_string (string):
        The text displayed when using the **counter** and **show-size**
        props. Can also be customized globally on the `internationalization
        page </customization/internationalization>`_.
      counter_string (string):
        The text displayed when using the **counter** prop. Can also
        be customized globally on the `internationalization page </customization/internationalization>`_.
      counter_value (function):

      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the input height
      disabled (boolean):
        Disable the input
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      filled (boolean):
        Applies the alternate filled input style
      flat (boolean):
        Removes elevation (shadow) added to element when using the **solo**
        or **solo-inverted** props
      full_width (boolean):
        Designates input type as full-width
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hide_input (boolean):
        Display the icon only without the input (file names)
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      multiple (boolean):
        Adds the **multiple** attribute to the input, allowing multiple file selections.
      outlined (boolean):
        Applies the outlined style to the input
      persistent_hint (boolean):
        Forces hint to always be visible
      persistent_placeholder (boolean):
        Forces placeholder to always be visible
      placeholder (string):
        Sets the input's placeholder text
      prefix (string):
        Displays prefix text
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      prepend_inner_icon (string):
        Prepends an icon inside the component's input, uses the same syntax as `v-icon`
      reverse (boolean):
        Reverses the input orientation
      rounded (boolean):
        Adds a border radius to the input
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      shaped (boolean):
        Round if `outlined` and increase `border-radius` if `filled`.
        Must be used with either `outlined` or `filled`
      show_size (['boolean', 'number']):
        Sets the displayed size of selected file(s). When using **true**
        will default to _1000_ displaying (**kB, MB, GB**) while _1024_
        will display (**KiB, MiB, GiB**).
      single_line (boolean):
        Label does not move on focus/dirty
      small_chips (boolean):
        Changes display of selections to chips with the **small** property
      solo (boolean):
        Changes the style of the input
      solo_inverted (boolean):
        Reduces element opacity until focused
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      suffix (string):
        Displays suffix text
      truncate_length (['number', 'string']):
        The length of a filename before it is truncated with ellipsis
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        A single or array of `File objects <https://developer.mozilla.org/en-US/docs/Web/API/File>`_.
      blur (event):
        Emitted when the input is blurred
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_append-outer (event):
        Emitted when appended outer icon is clicked
      click_clear (event):
        Emitted when clearable icon clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      click_prepend-inner (event):
        Emitted when prepended inner icon is clicked
      focus (event):
        Emitted when component is focused
      input (event):
        The updated bound model
      keydown (event):
        Emitted when **any** key is pressed
      update_error (event):
        The `error.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-file-input", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "append_outer_icon",
            "autofocus",
            "background_color",
            "chips",
            "clear_icon",
            "clearable",
            "color",
            "counter",
            "counter_size_string",
            "counter_string",
            "counter_value",  # JS functions unimplemented
            "dark",
            "dense",
            "disabled",
            "error",
            "error_count",
            "error_messages",
            "filled",
            "flat",
            "full_width",
            "height",
            "hide_details",
            "hide_input",
            "hint",
            "id",
            "label",
            "light",
            "loader_height",
            "loading",
            "messages",
            "multiple",
            "outlined",
            "persistent_hint",
            "persistent_placeholder",
            "placeholder",
            "prefix",
            "prepend_icon",
            "prepend_inner_icon",
            "reverse",
            "rounded",
            "rules",
            "shaped",
            "show_size",
            "single_line",
            "small_chips",
            "solo",
            "solo_inverted",
            "success",
            "success_messages",
            "suffix",
            "truncate_length",
            "validate_on_blur",
            "value",
        ]
        self._event_names += [
            "blur",
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_append_outer", "click:append-outer"),
            ("click_clear", "click:clear"),
            ("click_prepend", "click:prepend"),
            ("click_prepend_inner", "click:prepend-inner"),
            "focus",
            "input",
            "keydown",
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
        ]


class VFooter(HtmlElement):
    """
    Vuetify's VFooter component.
    See more `info and examples <https://vuetifyjs.com/api/v-footer>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      app (boolean):
        Designates the component as part of the application layout. Used
        for dynamically adjusting content sizing. Components using this
        prop should reside **outside** of `v-main` component to function
        properly. You can find more information about layouts on the
        `application page </components/application>`_. **Note:** this
        prop automatically applies **position: fixed** to the layout
        element. You can overwrite this functionality by using the `absolute`
        prop
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      fixed (boolean):
        Applies **position: fixed** to the component.
      height (['number', 'string']):
        Sets the height for the component.
      inset (boolean):
        Positions the toolbar offset from an application `v-navigation-drawer`
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      outlined (boolean):
        Removes elevation (box-shadow) and adds a *thin* border.
      padless (boolean):
        Remove all padding from the footer
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      tag (string):
        Specify a custom tag used on the root element.
      tile (boolean):
        Removes the component's **border-radius**.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-footer", children, **kwargs)
        self._attr_names += [
            "absolute",
            "app",
            "color",
            "dark",
            "elevation",
            "fixed",
            "height",
            "inset",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "outlined",
            "padless",
            "rounded",
            "shaped",
            "tag",
            "tile",
            "width",
        ]
        self._event_names += []


class VForm(HtmlElement):
    """
    Vuetify's VForm component.
    See more `info and examples <https://vuetifyjs.com/api/v-form>`_.

    Args:
      disabled (boolean):
        Puts all children inputs into a disabled state.
      lazy_validation (boolean):
        If enabled, **value** will always be _true_ unless there are
        visible validation errors. You can still call `validate()` to
        manually trigger validation
      readonly (boolean):
        Puts all children inputs into a readonly state.
      value (boolean):
        A boolean value representing the validity of the form.
      input (event):
        The updated bound model
      submit (event):
        Emitted when form is submitted
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-form", children, **kwargs)
        self._attr_names += [
            "disabled",
            "lazy_validation",
            "readonly",
            "value",
        ]
        self._event_names += [
            "input",
            "submit",
        ]


class VContainer(HtmlElement):
    """
    Vuetify's VContainer component.
    See more `info and examples <https://vuetifyjs.com/api/v-container>`_.

    Args:
      fluid (boolean):
        Removes viewport maximum-width size breakpoints
      id (string):
        Sets the DOM id on the component
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-container", children, **kwargs)
        self._attr_names += [
            "fluid",
            "id",
            "tag",
        ]
        self._event_names += []


class VCol(HtmlElement):
    """
    Vuetify's VCol component.
    See more `info and examples <https://vuetifyjs.com/api/v-col>`_.

    Args:
      align_self (string):
        Applies the `align-items <https://developer.mozilla.org/en-US/docs/Web/CSS/align-items>`_
        css property. Available options are **start**, **center**, **end**,
        **auto**, **baseline** and **stretch**.
      cols (['boolean', 'string', 'number']):
        Sets the default number of columns the component extends. Available
        options are **1 -> 12** and **auto**.
      lg (['boolean', 'string', 'number']):
        Changes the number of columns on large and greater breakpoints.
      md (['boolean', 'string', 'number']):
        Changes the number of columns on medium and greater breakpoints.
      offset (['string', 'number']):
        Sets the default offset for the column.
      offset_lg (['string', 'number']):
        Changes the offset of the component on large and greater breakpoints.
      offset_md (['string', 'number']):
        Changes the offset of the component on medium and greater breakpoints.
      offset_sm (['string', 'number']):
        Changes the offset of the component on small and greater breakpoints.
      offset_xl (['string', 'number']):
        Changes the offset of the component on extra large and greater breakpoints.
      order (['string', 'number']):
        Sets the default `order <https://developer.mozilla.org/en-US/docs/Web/CSS/order>`_
        for the column.
      order_lg (['string', 'number']):
        Changes the order of the component on large and greater breakpoints.
      order_md (['string', 'number']):
        Changes the order of the component on medium and greater breakpoints.
      order_sm (['string', 'number']):
        Changes the order of the component on small and greater breakpoints.
      order_xl (['string', 'number']):
        Changes the order of the component on extra large and greater breakpoints.
      sm (['boolean', 'string', 'number']):
        Changes the number of columns on small and greater breakpoints.
      tag (string):
        Specify a custom tag used on the root element.
      xl (['boolean', 'string', 'number']):
        Changes the number of columns on extra large and greater breakpoints.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-col", children, **kwargs)
        self._attr_names += [
            "align_self",
            "cols",
            "lg",
            "md",
            "offset",
            "offset_lg",
            "offset_md",
            "offset_sm",
            "offset_xl",
            "order",
            "order_lg",
            "order_md",
            "order_sm",
            "order_xl",
            "sm",
            "tag",
            "xl",
        ]
        self._event_names += []


class VRow(HtmlElement):
    """
    Vuetify's VRow component.
    See more `info and examples <https://vuetifyjs.com/api/v-row>`_.

    Args:
      align (string):
        Applies the `align-items <https://developer.mozilla.org/en-US/docs/Web/CSS/align-items>`_
        css property. Available options are **start**, **center**, **end**,
        **baseline** and **stretch**.
      align_content (string):
        Applies the `align-content <https://developer.mozilla.org/en-US/docs/Web/CSS/align-content>`_
        css property. Available options are **start**, **center**, **end**,
        **space-between**, **space-around** and **stretch**.
      align_content_lg (string):
        Changes the **align-content** property on large and greater breakpoints.
      align_content_md (string):
        Changes the **align-content** property on medium and greater breakpoints.
      align_content_sm (string):
        Changes the **align-content** property on small and greater breakpoints.
      align_content_xl (string):
        Changes the **align-content** property on extra large and greater breakpoints.
      align_lg (string):
        Changes the **align-items** property on large and greater breakpoints.
      align_md (string):
        Changes the **align-items** property on medium and greater breakpoints.
      align_sm (string):
        Changes the **align-items** property on small and greater breakpoints.
      align_xl (string):
        Changes the **align-items** property on extra large and greater breakpoints.
      dense (boolean):
        Reduces the gutter between `v-col`s.
      justify (string):
        Applies the `justify-content <https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content>`_
        css property. Available options are **start**, **center**, **end**,
        **space-between** and **space-around**.
      justify_lg (string):
        Changes the **justify-content** property on large and greater breakpoints.
      justify_md (string):
        Changes the **justify-content** property on medium and greater breakpoints.
      justify_sm (string):
        Changes the **justify-content** property on small and greater breakpoints.
      justify_xl (string):
        Changes the **justify-content** property on extra large and greater breakpoints.
      no_gutters (boolean):
        Removes the gutter between `v-col`s.
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-row", children, **kwargs)
        self._attr_names += [
            "align",
            "align_content",
            "align_content_lg",
            "align_content_md",
            "align_content_sm",
            "align_content_xl",
            "align_lg",
            "align_md",
            "align_sm",
            "align_xl",
            "dense",
            "justify",
            "justify_lg",
            "justify_md",
            "justify_sm",
            "justify_xl",
            "no_gutters",
            "tag",
        ]
        self._event_names += []


class VSpacer(HtmlElement):
    """
    Vuetify's VSpacer component.
    See more `info and examples <https://vuetifyjs.com/api/v-spacer>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-spacer", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VLayout(HtmlElement):
    """
    Vuetify's VLayout component.
    See more `info and examples <https://vuetifyjs.com/api/v-layout>`_.

    Args:
      align_baseline (Boolean):

      align_center (Boolean):

      align_content_center (Boolean):

      align_content_end (Boolean):

      align_content_space_around (Boolean):

      align_content_space_between (Boolean):

      align_content_start (Boolean):

      align_end (Boolean):

      align_start (Boolean):

      column (boolean):

      d_{type} (Boolean):

      fill_height (Boolean):

      id (string):
        Sets the DOM id on the component
      justify_center (Boolean):

      justify_end (Boolean):

      justify_space_around (Boolean):

      justify_space_between (Boolean):

      justify_start (Boolean):

      reverse (boolean):

      row (boolean):

      tag (String):
        Specify a custom tag used on the root element.
      wrap (boolean):

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-layout", children, **kwargs)
        self._attr_names += [
            "align_baseline",
            "align_center",
            "align_content_center",
            "align_content_end",
            "align_content_space_around",
            "align_content_space_between",
            "align_content_start",
            "align_end",
            "align_start",
            "column",
            "d_{type}",
            "fill_height",
            "id",
            "justify_center",
            "justify_end",
            "justify_space_around",
            "justify_space_between",
            "justify_start",
            "reverse",
            "row",
            "tag",
            "wrap",
        ]
        self._event_names += []


class VFlex(HtmlElement):
    """
    Vuetify's VFlex component.
    See more `info and examples <https://vuetifyjs.com/api/v-flex>`_.

    Args:
      (size)(1_12) (boolean):

      align_self_baseline (boolean):

      align_self_center (boolean):

      align_self_end (boolean):

      align_self_start (boolean):

      grow (boolean):

      id (string):
        Sets the DOM id on the component
      offset_(size)(0_12) (boolean):

      order_(size)(1_12) (boolean):

      shrink (boolean):

      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-flex", children, **kwargs)
        self._attr_names += [
            "sm1",
            "sm2",
            "sm3",
            "sm4",
            "sm5",
            "sm6",
            "sm7",
            "sm8",
            "sm9",
            "sm10",
            "sm11",
            "sm12",
            "md1",
            "md2",
            "md3",
            "md4",
            "md5",
            "md6",
            "md7",
            "md8",
            "md9",
            "md10",
            "md11",
            "md12",
            "lg1",
            "lg2",
            "lg3",
            "lg4",
            "lg5",
            "lg6",
            "lg7",
            "lg8",
            "lg9",
            "lg10",
            "lg11",
            "lg12",
            "xl1",
            "xl2",
            "xl3",
            "xl4",
            "xl5",
            "xl6",
            "xl7",
            "xl8",
            "xl9",
            "xl10",
            "xl11",
            "xl12",
            "align_self_baseline",
            "align_self_center",
            "align_self_end",
            "align_self_start",
            "grow",
            "id",
            "offset_sm0",
            "offset_sm1",
            "offset_sm2",
            "offset_sm3",
            "offset_sm4",
            "offset_sm5",
            "offset_sm6",
            "offset_sm7",
            "offset_sm8",
            "offset_sm9",
            "offset_sm10",
            "offset_sm11",
            "offset_sm12",
            "offset_md0",
            "offset_md1",
            "offset_md2",
            "offset_md3",
            "offset_md4",
            "offset_md5",
            "offset_md6",
            "offset_md7",
            "offset_md8",
            "offset_md9",
            "offset_md10",
            "offset_md11",
            "offset_md12",
            "offset_lg0",
            "offset_lg1",
            "offset_lg2",
            "offset_lg3",
            "offset_lg4",
            "offset_lg5",
            "offset_lg6",
            "offset_lg7",
            "offset_lg8",
            "offset_lg9",
            "offset_lg10",
            "offset_lg11",
            "offset_lg12",
            "offset_xl0",
            "offset_xl1",
            "offset_xl2",
            "offset_xl3",
            "offset_xl4",
            "offset_xl5",
            "offset_xl6",
            "offset_xl7",
            "offset_xl8",
            "offset_xl9",
            "offset_xl10",
            "offset_xl11",
            "offset_xl12",
            "order_sm1",
            "order_sm2",
            "order_sm3",
            "order_sm4",
            "order_sm5",
            "order_sm6",
            "order_sm7",
            "order_sm8",
            "order_sm9",
            "order_sm10",
            "order_sm11",
            "order_sm12",
            "order_md1",
            "order_md2",
            "order_md3",
            "order_md4",
            "order_md5",
            "order_md6",
            "order_md7",
            "order_md8",
            "order_md9",
            "order_md10",
            "order_md11",
            "order_md12",
            "order_lg1",
            "order_lg2",
            "order_lg3",
            "order_lg4",
            "order_lg5",
            "order_lg6",
            "order_lg7",
            "order_lg8",
            "order_lg9",
            "order_lg10",
            "order_lg11",
            "order_lg12",
            "order_xl1",
            "order_xl2",
            "order_xl3",
            "order_xl4",
            "order_xl5",
            "order_xl6",
            "order_xl7",
            "order_xl8",
            "order_xl9",
            "order_xl10",
            "order_xl11",
            "order_xl12",
            "shrink",
            "tag",
        ]
        self._event_names += []


class VHover(HtmlElement):
    """
    Vuetify's VHover component.
    See more `info and examples <https://vuetifyjs.com/api/v-hover>`_.

    Args:
      close_delay (['number', 'string']):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      disabled (boolean):
        Turns off hover functionality
      open_delay (['number', 'string']):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      value (boolean):
        Controls whether the component is visible or hidden.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-hover", children, **kwargs)
        self._attr_names += [
            "close_delay",
            "disabled",
            "open_delay",
            "value",
        ]
        self._event_names += []


class VIcon(HtmlElement):
    """
    Vuetify's VIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-icon>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Makes icon smaller (20px)
      disabled (boolean):
        Disable the input
      large (boolean):
        Makes the component large.
      left (boolean):
        Applies appropriate margins to the icon inside of a button when
        placed to the **left** of another element or text
      light (boolean):
        Applies the light theme variant to the component.
      right (boolean):
        Applies appropriate margins to the icon inside of a button when
        placed to the **right** of another element or text
      size (['number', 'string']):
        Specifies a custom font size for the icon
      small (boolean):
        Makes the component small.
      tag (string):
        Specifies a custom tag to be used
      x_large (boolean):
        Makes the component extra large.
      x_small (boolean):
        Makes the component extra small.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-icon", children, **kwargs)
        self._attr_names += [
            "color",
            "dark",
            "dense",
            "disabled",
            "large",
            "left",
            "light",
            "right",
            "size",
            "small",
            "tag",
            "x_large",
            "x_small",
        ]
        self._event_names += []


class VImg(HtmlElement):
    """
    Vuetify's VImg component.
    See more `info and examples <https://vuetifyjs.com/api/v-img>`_.

    Args:
      alt (string):
        Alternate text for screen readers. Leave empty for decorative images
      aspect_ratio (['string', 'number']):
        Calculated as `width/height`, so for a 1920x1080px image this
        will be `1.7778`. Will be calculated automatically if omitted
      contain (boolean):
        Prevents the image from being cropped if it doesn't fit
      content_class (string):
        Apply a custom class to the responsive content div.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      gradient (string):
        Overlays a gradient onto the image. Only supports `linear-gradient
        <https://developer.mozilla.org/en-US/docs/Web/CSS/linear-gradient>`_
        syntax, anything else should be done with classes (see examples>`_
      height (['number', 'string']):
        Sets the height for the component.
      lazy_src (string):
        Something to show while waiting for the main image to load, typically
        a small base64-encoded thumbnail. Has a slight blur filter applied.
         Use `vuetify-loader <https://github.com/vuetifyjs/vuetify-loader>`_
        to generate automatically
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      options (object):
        Options that are passed to the `Intersection observer <https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API>`_
        constructor.
      position (string):
        Overrides the default to change which parts get cropped off.
        Uses the same syntax as ``background-position` <https://developer.mozilla.org/en-US/docs/Web/CSS/background-position>`_
      sizes (string):
        For use with `srcset`, see `MDN <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes>`_
      src (['string', 'object']):
        The image URL. This prop is mandatory
      srcset (string):
        A set of alternate images to use based on device size. `Read
        more... <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset>`_
      transition (['boolean', 'string']):
        The transition to use when switching from `lazy-src` to `src`
      width (['number', 'string']):
        Sets the width for the component.
      error (event):
        Emitted when there is an error
      load (event):
        Emitted when image is loaded
      loadstart (event):
        Emitted when the image starts to load
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-img", children, **kwargs)
        self._attr_names += [
            "alt",
            "aspect_ratio",
            "contain",
            "content_class",
            "dark",
            "eager",
            "gradient",
            "height",
            "lazy_src",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "options",
            "position",
            "sizes",
            "src",
            "srcset",
            "transition",
            "width",
        ]
        self._event_names += [
            "error",
            "load",
            "loadstart",
        ]


class VInput(HtmlElement):
    """
    Vuetify's VInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-input>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      background_color (string):
        Changes the background-color of the input
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the input height
      disabled (boolean):
        Disable the input
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loading (boolean):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      persistent_hint (boolean):
        Forces hint to always be visible
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      update_error (event):
        The `error.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-input", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "background_color",
            "color",
            "dark",
            "dense",
            "disabled",
            "error",
            "error_count",
            "error_messages",
            "height",
            "hide_details",
            "hide_spin_buttons",
            "hint",
            "id",
            "label",
            "light",
            "loading",
            "messages",
            "persistent_hint",
            "prepend_icon",
            "readonly",
            "rules",
            "success",
            "success_messages",
            "validate_on_blur",
            "value",
        ]
        self._event_names += [
            "change",
            ("click_append", "click:append"),
            ("click_prepend", "click:prepend"),
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
        ]


class VItem(HtmlElement):
    """
    Vuetify's VItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-item>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      disabled (boolean):
        Removes the ability to click or target the component.
      value (any):
        The value used when the component is selected in a group. If
        not provided, the index will be used.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-item", children, **kwargs)
        self._attr_names += [
            "active_class",
            "disabled",
            "value",
        ]
        self._event_names += []


class VItemGroup(HtmlElement):
    """
    Vuetify's VItemGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-item-group>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max (['number', 'string']):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allow multiple selections. The **value** prop must be an _array_.
      tag (string):
        Specify a custom tag used on the root element.
      value (any):
        The designated model value for the component.
      value_comparator (function):
        Apply a custom value comparator function
      change (event):
        Emitted when the component value is changed by user interaction
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-item-group", children, **kwargs)
        self._attr_names += [
            "active_class",
            "dark",
            "light",
            "mandatory",
            "max",
            "multiple",
            "tag",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "change",
        ]


class VLazy(HtmlElement):
    """
    Vuetify's VLazy component.
    See more `info and examples <https://vuetifyjs.com/api/v-lazy>`_.

    Args:
      height (['number', 'string']):
        Sets the height for the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      options (object):
        Options that are passed to the `Intersection observer <https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API>`_
        constructor.
      tag (string):
        Specify a custom tag used on the root element.
      transition (string):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      value (any):
        Controls whether the component is visible or hidden.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-lazy", children, **kwargs)
        self._attr_names += [
            "height",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "options",
            "tag",
            "transition",
            "value",
            "width",
        ]
        self._event_names += []


class VListItemActionText(HtmlElement):
    """
    Vuetify's VListItemActionText component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-action-text>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-action-text", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListItemContent(HtmlElement):
    """
    Vuetify's VListItemContent component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-content>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-content", children, **kwargs)
        self._attr_names += [
            "tag",
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
        super().__init__("v-list-item-title", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VListItemSubtitle(HtmlElement):
    """
    Vuetify's VListItemSubtitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-subtitle>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-subtitle", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VList(HtmlElement):
    """
    Vuetify's VList component.
    See more `info and examples <https://vuetifyjs.com/api/v-list>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Lowers max height of list tiles
      disabled (boolean):
        Disables all children `v-list-item` components
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      expand (boolean):
        Will only collapse when explicitly closed
      flat (boolean):
        Remove the highlighted background on active `v-list-item`s
      height (['number', 'string']):
        Sets the height for the component.
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      nav (boolean):
        An alternative styling that reduces `v-list-item` width and rounds
        the corners. Typically used with **`v-navigation-drawer </components/navigation-drawers>`_**
      outlined (boolean):
        Removes elevation (box-shadow) and adds a *thin* border.
      rounded (boolean):
        Rounds the `v-list-item` edges
      shaped (boolean):
        Provides an alternative active style for `v-list-item`.
      subheader (boolean):
        Removes top padding. Used when previous sibling is a header
      tag (string):
        Specify a custom tag used on the root element.
      three_line (boolean):
        Increases list-item height for three lines. This prop uses `line-clamp
        <https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp>`_
        and is not supported in all browsers.
      tile (boolean):
        Removes the component's **border-radius**.
      two_line (boolean):
        Increases list-item height for two lines. This prop uses `line-clamp
        <https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp>`_
        and is not supported in all browsers.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list", children, **kwargs)
        self._attr_names += [
            "color",
            "dark",
            "dense",
            "disabled",
            "elevation",
            "expand",
            "flat",
            "height",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "nav",
            "outlined",
            "rounded",
            "shaped",
            "subheader",
            "tag",
            "three_line",
            "tile",
            "two_line",
            "width",
        ]
        self._event_names += []


class VListGroup(HtmlElement):
    """
    Vuetify's VListGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-group>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      disabled (boolean):
        Disables all children `v-list-item` components
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      group (['string', 'regexp']):
        Assign a route namespace. Accepts a string or regexp for determining
        active state
      no_action (boolean):
        Removes left padding assigned for action icons from group items
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      sub_group (boolean):
        Designate the component as nested list group
      value (any):
        Expands / Collapse the list-group
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-group", children, **kwargs)
        self._attr_names += [
            "active_class",
            "append_icon",
            "color",
            "disabled",
            "eager",
            "group",
            "no_action",
            "prepend_icon",
            "ripple",
            "sub_group",
            "value",
        ]
        self._event_names += [
            "click",
        ]


class VListItem(HtmlElement):
    """
    Vuetify's VListItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      append (boolean):
        Setting **append** prop always appends the relative path to the
        current path. You can find more information about the `**append**
        prop <https://router.vuejs.org/api/#append>`_ on the vue-router
        documentation.
      color (string):
        Applies specified color to the control when in an **active**
        state or **input-value** is **true** - it can be the name of
        material color (for example `success` or `purple`) or css color
        (`#033` or `rgba(255, 0, 0, 0.5)`)
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Lowers max height of list tiles
      disabled (boolean):
        Disables the component
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the `**exact** prop <https://router.vuejs.org/api/#exact>`_
        on the vue-router documentation.
      exact_active_class (string):
        Configure the active CSS class applied when the link is active
        with exact match. You can find more information about the `**exact-active-class**
        prop <https://router.vuejs.org/api/#exact-active-class>`_ on
        the vue-router documentation.
      exact_path (boolean):
        Exactly match the link, ignoring the `query` and the `hash` sections.
        You can find more information about the `**exact-path** prop
        <https://router.vuejs.org/api/#exact-path>`_ on the vue-router
        documentation.
      href (['string', 'object']):
        Designates the component as anchor and applies the **href** attribute.
      inactive (boolean):
        If set, the list tile will not be rendered as a link even if
        it has to/href prop or @click handler
      input_value (any):
        Controls the **active** state of the item. This is typically
        used to highlight the component
      light (boolean):
        Applies the light theme variant to the component.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the **href** or **to** prop.
      nuxt (boolean):
        Specifies the link is a `nuxt-link`. For use with the `nuxt framework
        <https://nuxtjs.org/api/components-nuxt-link/>`_.
      replace (boolean):
        Setting **replace** prop will call `router.replace(>`_` instead
        of `router.push(>`_` when clicked, so the navigation will not
        leave a history record. You can find more information about the
        `**replace** prop <https://router.vuejs.org/api/#replace>`_ on
        the vue-router documentation.
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      selectable (boolean):
        Allow text selection inside `v-list-item`. This prop uses `user-select
        <https://developer.mozilla.org/en-US/docs/Web/CSS/user-select>`_
      tag (string):
        Specify a custom tag used on the root element.
      target (string):
        Designates the target attribute. This should only be applied
        when using the **href** prop.
      three_line (boolean):
        Increases list-item height for three lines. This prop uses `line-clamp
        <https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp>`_
        and is not supported in all browsers.
      to (['string', 'object']):
        Denotes the target route of the link. You can find more information
        about the `**to** prop <https://router.vuejs.org/api/#to>`_ on
        the vue-router documentation.
      two_line (boolean):
        Increases list-item height for two lines. This prop uses `line-clamp
        <https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp>`_
        and is not supported in all browsers.
      value (any):
        The value used when a child of a `v-list-item-group </components/list-item-groups>`_.
      keydown (event):

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item", children, **kwargs)
        self._attr_names += [
            "active_class",
            "append",
            "color",
            "dark",
            "dense",
            "disabled",
            "exact",
            "exact_active_class",
            "exact_path",
            "href",
            "inactive",
            "input_value",
            "light",
            "link",
            "nuxt",
            "replace",
            "ripple",
            "selectable",
            "tag",
            "target",
            "three_line",
            "to",
            "two_line",
            "value",
        ]
        self._event_names += [
            "click",
            "keydown",
        ]


class VListItemAction(HtmlElement):
    """
    Vuetify's VListItemAction component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-action>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-action", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VListItemAvatar(HtmlElement):
    """
    Vuetify's VListItemAvatar component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-avatar>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      height (['number', 'string']):
        Sets the height for the component.
      horizontal (boolean):
        Uses an alternative horizontal style.
      left (boolean):
        Designates that the avatar is on the left side of a component.
        This is hooked into by components such as `v-chip </components/chips>`_
        and `v-btn </components/buttons>`_.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      right (boolean):
        Designates that the avatar is on the right side of a component.
        This is hooked into by components such as `v-chip </components/chips>`_
        and `v-btn </components/buttons>`_.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      size (['number', 'string']):
        Sets the height and width of the component.
      tile (boolean):
        Removes the component's **border-radius**.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-avatar", children, **kwargs)
        self._attr_names += [
            "color",
            "height",
            "horizontal",
            "left",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "right",
            "rounded",
            "size",
            "tile",
            "width",
        ]
        self._event_names += []


class VListItemIcon(HtmlElement):
    """
    Vuetify's VListItemIcon component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-icon>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-icon", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VListItemGroup(HtmlElement):
    """
    Vuetify's VListItemGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-list-item-group>`_.

    Args:
      active_class (string):
        The **active-class** applied to children when they are activated.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max (['number', 'string']):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allow multiple selections. The **value** prop must be an _array_.
      tag (string):
        Specify a custom tag used on the root element.
      value (any):
        Sets the active list-item inside the list-group
      value_comparator (function):
        Apply a custom value comparator function
      change (event):
        Emitted when the component value is changed by user interaction
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-list-item-group", children, **kwargs)
        self._attr_names += [
            "active_class",
            "color",
            "dark",
            "light",
            "mandatory",
            "max",
            "multiple",
            "tag",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "change",
        ]


class VMain(HtmlElement):
    """
    Vuetify's VMain component.
    See more `info and examples <https://vuetifyjs.com/api/v-main>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-main", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VMenu(HtmlElement):
    """
    Vuetify's VMenu component.
    See more `info and examples <https://vuetifyjs.com/api/v-menu>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      activator (any):
        Designate a custom activator when the `activator` slot is not
        used. String can be any valid querySelector and Object can be
        any valid Node.
      allow_overflow (boolean):
        Removes overflow re-positioning for the content
      attach (any):
        Specifies which DOM element that this component should detach
        to. String can be any valid querySelector and Object can be any
        valid Node. This will attach to the root `v-app` component by
        default.
      auto (boolean):
        Centers list on selected element
      bottom (boolean):
        Aligns the component towards the bottom.
      close_delay (['number', 'string']):
        Milliseconds to wait before closing component. Only works with
        the **open-on-hover** prop
      close_on_click (boolean):
        Designates if menu should close on outside-activator click
      close_on_content_click (boolean):
        Designates if menu should close when its content is clicked
      content_class (string):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      content_props (object):
        Applies props/attributes to the detached menu. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the attach prop is provided) and is not targetable
        by classes passed directly on the component. You could use this
        for example for applying a `data-cy` for cypress testing purposes.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disable_keys (boolean):
        Removes all keyboard interaction
      disabled (boolean):
        Disables the menu
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      internal_activator (boolean):
        Detaches the menu content inside of the component as opposed to the document.
      left (boolean):
        Aligns the component towards the left.
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the max height of the menu content
      max_width (['number', 'string']):
        Sets the maximum width for the content
      min_width (['number', 'string']):
        Sets the minimum width for the content
      nudge_bottom (['number', 'string']):
        Nudge the content to the bottom
      nudge_left (['number', 'string']):
        Nudge the content to the left
      nudge_right (['number', 'string']):
        Nudge the content to the right
      nudge_top (['number', 'string']):
        Nudge the content to the top
      nudge_width (['number', 'string']):
        Nudge the content width
      offset_overflow (boolean):
        Causes the component to flip to the opposite side when repositioned
        due to overflow
      offset_x (boolean):
        Offset the menu on the x-axis. Works in conjunction with direction left/right
      offset_y (boolean):
        Offset the menu on the y-axis. Works in conjunction with direction top/bottom
      open_delay (['number', 'string']):
        Milliseconds to wait before opening component. Only works with
        the **open-on-hover** prop
      open_on_click (boolean):
        Designates whether menu should open on activator click
      open_on_focus (boolean):

      open_on_hover (boolean):
        Designates whether menu should open on activator hover
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
      position_x (number):
        Used to position the content when not using an activator slot
      position_y (number):
        Used to position the content when not using an activator slot
      return_value (any):
        The value that is updated when the menu is closed - must be primitive.
        Dot notation is supported
      right (boolean):
        Aligns the component towards the right.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      tile (boolean):
        Removes the component's **border-radius**.
      top (boolean):
        Aligns the content towards the top.
      transition (['boolean', 'string']):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      value (any):
        Controls whether the component is visible or hidden.
      z_index (['number', 'string']):
        The z-index used for the component
      input (event):
        The updated bound model
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-menu", children, **kwargs)
        self._attr_names += [
            "absolute",
            "activator",
            "allow_overflow",
            "attach",
            "auto",
            "bottom",
            "close_delay",
            "close_on_click",
            "close_on_content_click",
            "content_class",
            "content_props",
            "dark",
            "disable_keys",
            "disabled",
            "eager",
            "internal_activator",
            "left",
            "light",
            "max_height",
            "max_width",
            "min_width",
            "nudge_bottom",
            "nudge_left",
            "nudge_right",
            "nudge_top",
            "nudge_width",
            "offset_overflow",
            "offset_x",
            "offset_y",
            "open_delay",
            "open_on_click",
            "open_on_focus",
            "open_on_hover",
            "origin",
            "position_x",
            "position_y",
            "return_value",
            "right",
            "rounded",
            "tile",
            "top",
            "transition",
            "value",
            "z_index",
        ]
        self._event_names += [
            "input",
        ]


class VNavigationDrawer(HtmlElement):
    """
    Vuetify's VNavigationDrawer component.
    See more `info and examples <https://vuetifyjs.com/api/v-navigation-drawer>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      app (boolean):
        Designates the component as part of the application layout. Used
        for dynamically adjusting content sizing. Components using this
        prop should reside **outside** of `v-main` component to function
        properly. You can find more information about layouts on the
        `application page </components/application>`_. **Note:** this
        prop automatically applies **position: fixed** to the layout
        element. You can overwrite this functionality by using the `absolute`
        prop
      bottom (boolean):
        Expands from the bottom of the screen on mobile devices
      clipped (boolean):
        A clipped drawer rests under the application toolbar. **Note:**
        requires the **clipped-left** or **clipped-right** prop on `v-app-bar`
        to work as intended
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disable_resize_watcher (boolean):
        Will automatically open/close drawer when resized depending if
        mobile or desktop.
      disable_route_watcher (boolean):
        Disables opening of navigation drawer when route changes
      expand_on_hover (boolean):
        Collapses the drawer to a **mini-variant** until hovering with the mouse
      fixed (boolean):
        Applies **position: fixed** to the component.
      floating (boolean):
        A floating drawer has no visible container (no border-right)
      height (['number', 'string']):
        Sets the height of the navigation drawer
      hide_overlay (boolean):
        Hides the display of the overlay.
      light (boolean):
        Applies the light theme variant to the component.
      mini_variant (boolean):
        Condenses navigation drawer width, also accepts the **.sync**
        modifier. With this, the drawer will re-open when clicking it
      mini_variant_width (['number', 'string']):
        Designates the width assigned when the `mini` prop is turned on
      mobile_breakpoint (['number', 'string']):
        Sets the designated mobile breakpoint for the component. This
        will apply alternate styles for mobile devices such as the `temporary`
        prop, or activate the `bottom` prop when the breakpoint value
        is met. Setting the value to `0` will disable this functionality.
      overlay_color (string):
        Sets the overlay color.
      overlay_opacity (['number', 'string']):
        Sets the overlay opacity.
      permanent (boolean):
        The drawer remains visible regardless of screen size
      right (boolean):
        Places the navigation drawer on the right
      src (['string', 'object']):
        Specifies a `v-img </components/images>`_ as the component's background.
      stateless (boolean):
        Remove all automated state functionality (resize, mobile, route)
        and manually control the drawer state
      tag (string):
        Specify a custom tag used on the root element.
      temporary (boolean):
        A temporary drawer sits above its application and uses a scrim
        (overlay) to darken the background
      touchless (boolean):
        Disable mobile touch functionality
      value (any):
        Controls whether the component is visible or hidden.
      width (['number', 'string']):
        Sets the width for the component.
      input (event):
        The updated bound model
      transitionend (event):
        Emits event object when transition is complete.
      update_mini-variant (event):
        The `mini-variant.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-navigation-drawer", children, **kwargs)
        self._attr_names += [
            "absolute",
            "app",
            "bottom",
            "clipped",
            "color",
            "dark",
            "disable_resize_watcher",
            "disable_route_watcher",
            "expand_on_hover",
            "fixed",
            "floating",
            "height",
            "hide_overlay",
            "light",
            "mini_variant",
            "mini_variant_width",
            "mobile_breakpoint",
            "overlay_color",
            "overlay_opacity",
            "permanent",
            "right",
            "src",
            "stateless",
            "tag",
            "temporary",
            "touchless",
            "value",
            "width",
        ]
        self._event_names += [
            "input",
            "transitionend",
            ("update_mini_variant", "update:mini-variant"),
        ]


class VOtpInput(HtmlElement):
    """
    Vuetify's VOtpInput component.
    See more `info and examples <https://vuetifyjs.com/api/v-otp-input>`_.

    Args:
      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Disable the input
      id (string):
        Sets the DOM id on the component
      length (['number', 'string']):
        The OTP field's length
      plain (boolean):
        Outlined style applied by default to the input, set to `true`
        to apply plain style
      readonly (boolean):
        Puts input in readonly state
      type (string):
        Supported types: `text`, `password`, `number`
      value (any):
        The input's value
      change (event):
        Emitted when the input is changed by user interaction
      finish (event):
        Emitted when the input is filled completely and cursor is blurred
      input (event):
        The updated bound model
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-otp-input", children, **kwargs)
        self._attr_names += [
            "dark",
            "disabled",
            "id",
            "length",
            "plain",
            "readonly",
            "type",
            "value",
        ]
        self._event_names += [
            "change",
            "finish",
            "input",
        ]


class VOverflowBtn(HtmlElement):
    """
    Vuetify's VOverflowBtn component.
    See more `info and examples <https://vuetifyjs.com/api/v-overflow-btn>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      append_outer_icon (string):
        Appends an icon to the outside the component's input, uses same
        syntax as `v-icon`
      attach (any):
        Specifies which DOM element that this component should detach
        to. String can be any valid querySelector and Object can be any
        valid Node. This will attach to the root `v-app` component by
        default.
      auto_select_first (boolean):
        When searching, will always highlight the first option
      autofocus (boolean):
        Enables autofocus
      background_color (string):
        Changes the background-color of the input
      cache_items (boolean):
        Keeps a local _unique_ copy of all items that have been passed
        through the **items** prop.
      chips (boolean):
        Changes display of selections to chips
      clear_icon (string):
        Applied when using **clearable** and the input is dirty
      clearable (boolean):
        Add input clear functionality, default icon is Material Design
        Icons **mdi-clear**
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      counter (['boolean', 'number', 'string']):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      counter_value (function):

      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      deletable_chips (boolean):
        Adds a remove icon to selected chips
      dense (boolean):
        Reduces the input height
      disable_lookup (boolean):
        Disables keyboard lookup
      disabled (boolean):
        Disables the input
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      editable (boolean):
        Creates an editable button
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      filled (boolean):
        Applies the alternate filled input style
      filter (function):
        The function used for filtering items
      flat (boolean):
        Removes elevation (shadow) added to element when using the **solo**
        or **solo-inverted** props
      full_width (boolean):
        Designates input type as full-width
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hide_no_data (boolean):
        Hides the menu when there are no options to show.  Useful for
        preventing the menu from opening before results are fetched asynchronously.
         Also has the effect of opening the menu when the `items` array
        changes if not already open.
      hide_selected (boolean):
        Do not display in the select menu items that are already selected.
        Also removes checkboxes from the list when multiple
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      item_color (string):
        Sets color of selected items
      item_disabled (['string', 'array', 'function']):
        Set property of **items**'s disabled value
      item_text (['string', 'array', 'function']):
        Set property of **items**'s text value
      item_value (['string', 'array', 'function']):
        Set property of **items**'s value - **must be primitive**. Dot
        notation is supported. **Note:** This is currently not supported
        with `v-combobox` `GitHub Issue <https://github.com/vuetifyjs/vuetify/issues/5479>`_
      items (array):
        Can be an array of objects or array of strings. When using objects,
        will look for a text, value and disabled keys. This can be changed
        using the **item-text**, **item-value** and **item-disabled**
        props.  Objects that have a **header** or **divider** property
        are considered special cases and generate a list header or divider;
        these items are not selectable.
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      menu_props (['string', 'array', 'object']):
        Pass props through to the `v-menu` component. Accepts either
        a string for boolean props `menu-props="auto, overflowY"`, or
        an object `:menu-props="{ auto: true, overflowY: true }"`
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      multiple (boolean):
        Changes select to multiple. Accepts array for value
      no_data_text (string):
        Display text when there is no data
      no_filter (boolean):
        Do not apply filtering when searching. Useful when data is being
        filtered server side
      open_on_clear (boolean):
        When using the **clearable** prop, once cleared, the select menu
        will either open or stay open, depending on the current state
      outlined (boolean):
        Applies the outlined style to the input
      persistent_hint (boolean):
        Forces hint to always be visible
      persistent_placeholder (boolean):
        Forces label to always be visible
      placeholder (string):
        Sets the input's placeholder text
      prefix (string):
        Displays prefix text
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      prepend_inner_icon (string):
        Prepends an icon inside the component's input, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**
      reverse (boolean):
        Reverses the input orientation
      rounded (boolean):
        Adds a border radius to the input
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      search_input (string):
        Use the **.sync** modifier to catch user input from the search input
      segmented (boolean):
        Creates a segmented button
      shaped (boolean):
        Round if `outlined` and increase `border-radius` if `filled`.
        Must be used with either `outlined` or `filled`
      single_line (boolean):
        Label does not move on focus/dirty
      small_chips (boolean):
        Changes display of selections to chips with the **small** property
      solo (boolean):
        Changes the style of the input
      solo_inverted (boolean):
        Reduces element opacity until focused
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      suffix (string):
        Displays suffix text
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      value_comparator (function):
        The comparison algorithm used for values. `More info <https://github.com/vuetifyjs/vuetify/blob/v2-stable/packages/vuetify/src/util/helpers.ts>`_
      blur (event):
        Emitted when the input is blurred
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_append-outer (event):
        Emitted when appended outer icon is clicked
      click_clear (event):
        Emitted when clearable icon clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      click_prepend-inner (event):
        Emitted when prepended inner icon is clicked
      focus (event):
        Emitted when component is focused
      input (event):
        The updated bound model
      keydown (event):
        Emitted when **any** key is pressed
      update_error (event):
        The `error.sync` event
      update_list-index (event):
        Emitted when menu item is selected using keyboard arrows
      update_search-input (event):
        The `search-input.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-overflow-btn", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "append_outer_icon",
            "attach",
            "auto_select_first",
            "autofocus",
            "background_color",
            "cache_items",
            "chips",
            "clear_icon",
            "clearable",
            "color",
            "counter",
            "counter_value",  # JS functions unimplemented
            "dark",
            "deletable_chips",
            "dense",
            "disable_lookup",
            "disabled",
            "eager",
            "editable",
            "error",
            "error_count",
            "error_messages",
            "filled",
            "filter",  # JS functions unimplemented
            "flat",
            "full_width",
            "height",
            "hide_details",
            "hide_no_data",
            "hide_selected",
            "hint",
            "id",
            "item_color",
            "item_disabled",  # JS functions unimplemented
            "item_text",  # JS functions unimplemented
            "item_value",  # JS functions unimplemented
            "items",
            "label",
            "light",
            "loader_height",
            "loading",
            "menu_props",
            "messages",
            "multiple",
            "no_data_text",
            "no_filter",
            "open_on_clear",
            "outlined",
            "persistent_hint",
            "persistent_placeholder",
            "placeholder",
            "prefix",
            "prepend_icon",
            "prepend_inner_icon",
            "readonly",
            "return_object",
            "reverse",
            "rounded",
            "rules",
            "search_input",
            "segmented",
            "shaped",
            "single_line",
            "small_chips",
            "solo",
            "solo_inverted",
            "success",
            "success_messages",
            "suffix",
            "validate_on_blur",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "blur",
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_append_outer", "click:append-outer"),
            ("click_clear", "click:clear"),
            ("click_prepend", "click:prepend"),
            ("click_prepend_inner", "click:prepend-inner"),
            "focus",
            "input",
            "keydown",
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
            ("update_list_index", "update:list-index"),
            ("update_search_input", "update:search-input"),
        ]


class VOverlay(HtmlElement):
    """
    Vuetify's VOverlay component.
    See more `info and examples <https://vuetifyjs.com/api/v-overlay>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      light (boolean):
        Applies the light theme variant to the component.
      opacity (['number', 'string']):
        Sets the overlay opacity
      value (any):
        Controls whether the component is visible or hidden.
      z_index (['number', 'string']):
        The z-index used for the component
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-overlay", children, **kwargs)
        self._attr_names += [
            "absolute",
            "color",
            "dark",
            "light",
            "opacity",
            "value",
            "z_index",
        ]
        self._event_names += []


class VPagination(HtmlElement):
    """
    Vuetify's VPagination component.
    See more `info and examples <https://vuetifyjs.com/api/v-pagination>`_.

    Args:
      circle (boolean):
        Shape pagination elements as circles
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      current_page_aria_label (string):

      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Disables component
      length (number):
        The length of the pagination component
      light (boolean):
        Applies the light theme variant to the component.
      navigation_color (string):

      navigation_text_color (string):

      next_aria_label (string):

      next_icon (string):
        Specify the icon to use for the next icon
      page_aria_label (string):

      prev_icon (string):
        Specify the icon to use for the prev icon
      previous_aria_label (string):

      total_visible (['number', 'string']):
        Specify the max total visible pagination numbers
      value (number):
        Current selected page
      wrapper_aria_label (string):

      input (event):
        The updated bound model
      next (event):
        Emitted when going to next item
      previous (event):
        Emitted when going to previous item
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-pagination", children, **kwargs)
        self._attr_names += [
            "circle",
            "color",
            "current_page_aria_label",
            "dark",
            "disabled",
            "length",
            "light",
            "navigation_color",
            "navigation_text_color",
            "next_aria_label",
            "next_icon",
            "page_aria_label",
            "prev_icon",
            "previous_aria_label",
            "total_visible",
            "value",
            "wrapper_aria_label",
        ]
        self._event_names += [
            "input",
            "next",
            "previous",
        ]


class VSheet(HtmlElement):
    """
    Vuetify's VSheet component.
    See more `info and examples <https://vuetifyjs.com/api/v-sheet>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      height (['number', 'string']):
        Sets the height for the component.
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      outlined (boolean):
        Removes elevation (box-shadow) and adds a *thin* border.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      tag (string):
        Specify a custom tag used on the root element.
      tile (boolean):
        Removes the component's **border-radius**.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-sheet", children, **kwargs)
        self._attr_names += [
            "color",
            "dark",
            "elevation",
            "height",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "outlined",
            "rounded",
            "shaped",
            "tag",
            "tile",
            "width",
        ]
        self._event_names += []


class VParallax(HtmlElement):
    """
    Vuetify's VParallax component.
    See more `info and examples <https://vuetifyjs.com/api/v-parallax>`_.

    Args:
      alt (string):
        Attaches an alt property to the parallax image
      height (['string', 'number']):
        Sets the height for the component
      src (string):
        The image to parallax
      srcset (string):
        A set of alternate images to use based on device size. `Read
        more... <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset>`_
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-parallax", children, **kwargs)
        self._attr_names += [
            "alt",
            "height",
            "src",
            "srcset",
        ]
        self._event_names += []


class VProgressCircular(HtmlElement):
    """
    Vuetify's VProgressCircular component.
    See more `info and examples <https://vuetifyjs.com/api/v-progress-circular>`_.

    Args:
      button (boolean):
        Deprecated - Pending removal
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      indeterminate (boolean):
        Constantly animates, use when loading progress is unknown.
      rotate (['number', 'string']):
        Rotates the circle start point in deg
      size (['number', 'string']):
        Sets the diameter of the circle in pixels
      value (['number', 'string']):
        The percentage value for current progress
      width (['number', 'string']):
        Sets the stroke of the circle in pixels
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-progress-circular", children, **kwargs)
        self._attr_names += [
            "button",
            "color",
            "indeterminate",
            "rotate",
            "size",
            "value",
            "width",
        ]
        self._event_names += []


class VProgressLinear(HtmlElement):
    """
    Vuetify's VProgressLinear component.
    See more `info and examples <https://vuetifyjs.com/api/v-progress-linear>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      active (boolean):
        Reduce the height to 0, hiding component
      background_color (string):
        Background color, set to component's color if null
      background_opacity (['number', 'string']):
        Background opacity, if null it defaults to 0.3 if background
        color is not specified or 1 otherwise
      bottom (boolean):
        Aligns the component towards the bottom.
      buffer_value (['number', 'string']):
        The percentage value for the buffer
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      fixed (boolean):
        Applies **position: fixed** to the component.
      height (['number', 'string']):
        Sets the height for the component
      indeterminate (boolean):
        Constantly animates, use when loading progress is unknown.
      light (boolean):
        Applies the light theme variant to the component.
      query (boolean):
        Animates like **indeterminate** prop but inverse
      reverse (boolean):
        Displays reversed progress (right to left in LTR mode and left to right in RTL)
      rounded (boolean):
        Adds a border radius to the progress component
      stream (boolean):
        An alternative style for portraying loading that works in tandem
        with **buffer-value**
      striped (boolean):
        Adds a stripe background to the filled portion of the progress component
      top (boolean):
        Aligns the content towards the top.
      value (['number', 'string']):
        The designated model value for the component.
      change (event):
        Emitted when the component value is changed by user interaction
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-progress-linear", children, **kwargs)
        self._attr_names += [
            "absolute",
            "active",
            "background_color",
            "background_opacity",
            "bottom",
            "buffer_value",
            "color",
            "dark",
            "fixed",
            "height",
            "indeterminate",
            "light",
            "query",
            "reverse",
            "rounded",
            "stream",
            "striped",
            "top",
            "value",
        ]
        self._event_names += [
            "change",
        ]


class VRadioGroup(HtmlElement):
    """
    Vuetify's VRadioGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-radio-group>`_.

    Args:
      active_class (string):
        The **active-class** applied to children when they are activated.
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      background_color (string):
        Changes the background-color of the input
      column (boolean):
        Displays radio buttons in column
      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the input height
      disabled (boolean):
        Disable the input
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max (['number', 'string']):
        Sets a maximum number of selections that can be made.
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      multiple (boolean):
        Allow multiple selections. The **value** prop must be an _array_.
      name (string):
        Sets the component's name attribute
      persistent_hint (boolean):
        Forces hint to always be visible
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      row (boolean):
        Displays radio buttons in row
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      tag (string):
        Specify a custom tag used on the root element.
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      value_comparator (function):
        Apply a custom value comparator function
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      update_error (event):
        The `error.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-radio-group", children, **kwargs)
        self._attr_names += [
            "active_class",
            "append_icon",
            "background_color",
            "column",
            "dark",
            "dense",
            "disabled",
            "error",
            "error_count",
            "error_messages",
            "hide_details",
            "hint",
            "id",
            "label",
            "light",
            "mandatory",
            "max",
            "messages",
            "multiple",
            "name",
            "persistent_hint",
            "prepend_icon",
            "readonly",
            "row",
            "rules",
            "success",
            "success_messages",
            "tag",
            "validate_on_blur",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "change",
            ("click_append", "click:append"),
            ("click_prepend", "click:prepend"),
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
        ]


class VRadio(HtmlElement):
    """
    Vuetify's VRadio component.
    See more `info and examples <https://vuetifyjs.com/api/v-radio>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Removes the ability to click or target the component.
      id (string):
        Sets the DOM id on the component
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      name (string):
        Sets the component's name attribute
      off_icon (string):
        The icon used when inactive
      on_icon (string):
        The icon used when active
      readonly (boolean):
        Puts input in readonly state
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      value (any):
        The value used when the component is selected in a group. If
        not provided, the index will be used.
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      update_error (event):
        The `error.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-radio", children, **kwargs)
        self._attr_names += [
            "active_class",
            "color",
            "dark",
            "disabled",
            "id",
            "label",
            "light",
            "name",
            "off_icon",
            "on_icon",
            "readonly",
            "ripple",
            "value",
        ]
        self._event_names += [
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_prepend", "click:prepend"),
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
        ]


class VRangeSlider(HtmlElement):
    """
    Vuetify's VRangeSlider component.
    See more `info and examples <https://vuetifyjs.com/api/v-range-slider>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      background_color (string):
        Changes the background-color of the input
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the input height
      disabled (boolean):
        Disable the input
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      inverse_label (boolean):
        Reverse the label position. Works with **rtl**.
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      max (['number', 'string']):
        Sets the maximum allowed value
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      min (['number', 'string']):
        Sets the minimum allowed value
      persistent_hint (boolean):
        Forces hint to always be visible
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      step (['number', 'string']):
        If greater than 0, sets step interval for ticks
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      thumb_color (string):
        Sets the thumb and thumb label color
      thumb_label (['boolean', 'string']):
        Show thumb label. If `true` it shows label when using slider.
        If set to `'always'` it always shows label.
      thumb_size (['number', 'string']):
        Controls the size of the thumb label.
      tick_labels (array):
        When provided with Array<string>, will attempt to map the labels
        to each step in index order
      tick_size (['number', 'string']):
        Controls the size of **ticks**
      ticks (['boolean', 'string']):
        Show track ticks. If `true` it shows ticks when using slider.
        If set to `'always'` it always shows ticks.
      track_color (string):
        Sets the track's color
      track_fill_color (string):
        Sets the track's fill color
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      vertical (boolean):
        Changes slider direction to vertical
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      end (event):
        Slider value emitted at the end of slider movement
      input (event):
        The updated bound model
      start (event):
        Slider value emitted at start of slider movement
      update_error (event):
        The `error.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-range-slider", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "background_color",
            "color",
            "dark",
            "dense",
            "disabled",
            "error",
            "error_count",
            "error_messages",
            "height",
            "hide_details",
            "hint",
            "id",
            "inverse_label",
            "label",
            "light",
            "loader_height",
            "loading",
            "max",
            "messages",
            "min",
            "persistent_hint",
            "prepend_icon",
            "readonly",
            "rules",
            "step",
            "success",
            "success_messages",
            "thumb_color",
            "thumb_label",
            "thumb_size",
            "tick_labels",
            "tick_size",
            "ticks",
            "track_color",
            "track_fill_color",
            "validate_on_blur",
            "value",
            "vertical",
        ]
        self._event_names += [
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_prepend", "click:prepend"),
            "end",
            "input",
            "mousedown",
            "mouseup",
            "start",
            ("update_error", "update:error"),
        ]


class VRating(HtmlElement):
    """
    Vuetify's VRating component.
    See more `info and examples <https://vuetifyjs.com/api/v-rating>`_.

    Args:
      background_color (string):
        The color used for empty icons
      clearable (boolean):
        Allows for the component to be cleared. Triggers when the icon
        containing the current value is clicked.
      close_delay (['number', 'string']):
        Milliseconds to wait before closing component. Only applies to
        hover and focus events.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Icons have a smaller size
      empty_icon (string):
        The icon displayed when empty
      full_icon (string):
        The icon displayed when full
      half_icon (string):
        The icon displayed when half (requires **half-increments** prop)
      half_increments (boolean):
        Allows the selection of half increments
      hover (boolean):
        Provides visual feedback when hovering over icons
      icon_label (string):
        The **aria-label** used for icons
      large (boolean):
        Makes the component large.
      length (['number', 'string']):
        The amount of ratings to show
      light (boolean):
        Applies the light theme variant to the component.
      open_delay (['number', 'string']):
        Milliseconds to wait before opening component. Only applies to
        hover and focus events.
      readonly (boolean):
        Removes all hover effects and pointer events
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      size (['number', 'string']):
        Sets the height and width of the component.
      small (boolean):
        Makes the component small.
      value (number):
        The rating value
      x_large (boolean):
        Makes the component extra large.
      x_small (boolean):
        Makes the component extra small.
      input (event):
        Emits the rating number when this value changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-rating", children, **kwargs)
        self._attr_names += [
            "background_color",
            "clearable",
            "close_delay",
            "color",
            "dark",
            "dense",
            "empty_icon",
            "full_icon",
            "half_icon",
            "half_increments",
            "hover",
            "icon_label",
            "large",
            "length",
            "light",
            "open_delay",
            "readonly",
            "ripple",
            "size",
            "small",
            "value",
            "x_large",
            "x_small",
        ]
        self._event_names += [
            "input",
        ]


class VResponsive(HtmlElement):
    """
    Vuetify's VResponsive component.
    See more `info and examples <https://vuetifyjs.com/api/v-responsive>`_.

    Args:
      aspect_ratio (['string', 'number']):
        Sets a base aspect ratio, calculated as width/height. This will
        only set a **minimum** height, the component can still grow if
        it has a lot of content.
      content_class (string):
        Apply a custom class to the responsive content div.
      height (['number', 'string']):
        Sets the height for the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-responsive", children, **kwargs)
        self._attr_names += [
            "aspect_ratio",
            "content_class",
            "height",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "width",
        ]
        self._event_names += []


class VSelect(HtmlElement):
    """
    Vuetify's VSelect component.
    See more `info and examples <https://vuetifyjs.com/api/v-select>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      append_outer_icon (string):
        Appends an icon to the outside the component's input, uses same
        syntax as `v-icon`
      attach (any):
        Specifies which DOM element that this component should detach
        to. String can be any valid querySelector and Object can be any
        valid Node. This will attach to the root `v-app` component by
        default.
      autofocus (boolean):
        Enables autofocus
      background_color (string):
        Changes the background-color of the input
      cache_items (boolean):
        Keeps a local _unique_ copy of all items that have been passed
        through the **items** prop.
      chips (boolean):
        Changes display of selections to chips
      clear_icon (string):
        Applied when using **clearable** and the input is dirty
      clearable (boolean):
        Add input clear functionality, default icon is Material Design
        Icons **mdi-clear**
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      counter (['boolean', 'number', 'string']):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      counter_value (function):

      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      deletable_chips (boolean):
        Adds a remove icon to selected chips
      dense (boolean):
        Reduces the input height
      disable_lookup (boolean):
        Disables keyboard lookup
      disabled (boolean):
        Disables the input
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      filled (boolean):
        Applies the alternate filled input style
      flat (boolean):
        Removes elevation (shadow) added to element when using the **solo**
        or **solo-inverted** props
      full_width (boolean):
        Designates input type as full-width
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hide_selected (boolean):
        Do not display in the select menu items that are already selected.
        Also removes checkboxes from the list when multiple
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      item_color (string):
        Sets color of selected items
      item_disabled (['string', 'array', 'function']):
        Set property of **items**'s disabled value
      item_text (['string', 'array', 'function']):
        Set property of **items**'s text value
      item_value (['string', 'array', 'function']):
        Set property of **items**'s value - **must be primitive**. Dot
        notation is supported. **Note:** This is currently not supported
        with `v-combobox` `GitHub Issue <https://github.com/vuetifyjs/vuetify/issues/5479>`_
      items (array):
        Can be an array of objects or array of strings. When using objects,
        will look for a text, value and disabled keys. This can be changed
        using the **item-text**, **item-value** and **item-disabled**
        props.  Objects that have a **header** or **divider** property
        are considered special cases and generate a list header or divider;
        these items are not selectable.
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      menu_props (['string', 'array', 'object']):
        Pass props through to the `v-menu` component. Accepts either
        a string for boolean props `menu-props="auto, overflowY"`, or
        an object `:menu-props="{ auto: true, overflowY: true }"`
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      multiple (boolean):
        Changes select to multiple. Accepts array for value
      no_data_text (string):
        Display text when there is no data
      open_on_clear (boolean):
        When using the **clearable** prop, once cleared, the select menu
        will either open or stay open, depending on the current state
      outlined (boolean):
        Applies the outlined style to the input
      persistent_hint (boolean):
        Forces hint to always be visible
      persistent_placeholder (boolean):
        Forces placeholder to always be visible
      placeholder (string):
        Sets the input's placeholder text
      prefix (string):
        Displays prefix text
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      prepend_inner_icon (string):
        Prepends an icon inside the component's input, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      return_object (boolean):
        Changes the selection behavior to return the object directly
        rather than the value specified with **item-value**
      reverse (boolean):
        Reverses the input orientation
      rounded (boolean):
        Adds a border radius to the input
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      shaped (boolean):
        Round if `outlined` and increase `border-radius` if `filled`.
        Must be used with either `outlined` or `filled`
      single_line (boolean):
        Label does not move on focus/dirty
      small_chips (boolean):
        Changes display of selections to chips with the **small** property
      solo (boolean):
        Changes the style of the input
      solo_inverted (boolean):
        Reduces element opacity until focused
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      suffix (string):
        Displays suffix text
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      value_comparator (function):
        The comparison algorithm used for values. `More info <https://github.com/vuetifyjs/vuetify/blob/v2-stable/packages/vuetify/src/util/helpers.ts>`_
      blur (event):
        Emitted when the input is blurred
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_append-outer (event):
        Emitted when appended outer icon is clicked
      click_clear (event):
        Emitted when clearable icon clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      click_prepend-inner (event):
        Emitted when prepended inner icon is clicked
      focus (event):
        Emitted when component is focused
      input (event):
        The updated bound model
      keydown (event):
        Emitted when **any** key is pressed
      update_error (event):
        The `error.sync` event
      update_list-index (event):
        Emitted when menu item is selected using keyboard arrows
      update_search-input (event):
        The `search-input.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-select", children, **kwargs)
        self.ttsSensitive()
        self._attr_names += [
            "append_icon",
            "append_outer_icon",
            "attach",
            "autofocus",
            "background_color",
            "cache_items",
            "chips",
            "clear_icon",
            "clearable",
            "color",
            "counter",
            "counter_value",  # JS functions unimplemented
            "dark",
            "deletable_chips",
            "dense",
            "disable_lookup",
            "disabled",
            "eager",
            "error",
            "error_count",
            "error_messages",
            "filled",
            "flat",
            "full_width",
            "height",
            "hide_details",
            "hide_selected",
            "hint",
            "id",
            "item_color",
            "item_disabled",  # JS functions unimplemented
            "item_text",  # JS functions unimplemented
            "item_value",  # JS functions unimplemented
            "items",
            "label",
            "light",
            "loader_height",
            "loading",
            "menu_props",
            "messages",
            "multiple",
            "no_data_text",
            "open_on_clear",
            "outlined",
            "persistent_hint",
            "persistent_placeholder",
            "placeholder",
            "prefix",
            "prepend_icon",
            "prepend_inner_icon",
            "readonly",
            "return_object",
            "reverse",
            "rounded",
            "rules",
            "shaped",
            "single_line",
            "small_chips",
            "solo",
            "solo_inverted",
            "success",
            "success_messages",
            "suffix",
            "validate_on_blur",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "blur",
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_append_outer", "click:append-outer"),
            ("click_clear", "click:clear"),
            ("click_prepend", "click:prepend"),
            ("click_prepend_inner", "click:prepend-inner"),
            "focus",
            "input",
            "keydown",
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
            ("update_list_index", "update:list-index"),
            ("update_search_input", "update:search-input"),
        ]


class VSkeletonLoader(HtmlElement):
    """
    Vuetify's VSkeletonLoader component.
    See more `info and examples <https://vuetifyjs.com/api/v-skeleton-loader>`_.

    Args:
      boilerplate (boolean):
        Remove the loading animation from the skeleton
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      height (['number', 'string']):
        Sets the height for the component.
      light (boolean):
        Applies the light theme variant to the component.
      loading (boolean):
        Applies a loading animation with a on-hover loading cursor. A
        value of **false** will only work when there is content in the
        `default` slot.
      loading_text (string):

      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      tile (boolean):
        Removes the component's border-radius
      transition (string):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      type (string):
        A string delimited list of skeleton components to create such
        as `type="text@3"` or `type="card, list-item"`. Will recursively
        generate a corresponding skeleton from the provided string. Also
        supports short-hand for multiple elements such as **article@3**
        and **paragraph@2** which will generate 3 _article_ skeletons
        and 2 _paragraph_ skeletons. Please see below for a list of available
        pre-defined options.
      types (object):
        A custom types object that will be combined with the pre-defined
        options. For a list of available pre-defined options, see the
        **type** prop.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-skeleton-loader", children, **kwargs)
        self._attr_names += [
            "boilerplate",
            "dark",
            "elevation",
            "height",
            "light",
            "loading",
            "loading_text",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "tile",
            "transition",
            "type",
            "types",
            "width",
        ]
        self._event_names += []


class VSlider(HtmlElement):
    """
    Vuetify's VSlider component.
    See more `info and examples <https://vuetifyjs.com/api/v-slider>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      background_color (string):
        Changes the background-color of the input
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the input height
      disabled (boolean):
        Disable the input
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      inverse_label (boolean):
        Reverse the label position. Works with **rtl**.
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      max (['number', 'string']):
        Sets the maximum allowed value
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      min (['number', 'string']):
        Sets the minimum allowed value
      persistent_hint (boolean):
        Forces hint to always be visible
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      step (['number', 'string']):
        If greater than 0, sets step interval for ticks
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      thumb_color (string):
        Sets the thumb and thumb label color
      thumb_label (['boolean', 'string']):
        Show thumb label. If `true` it shows label when using slider.
        If set to `'always'` it always shows label.
      thumb_size (['number', 'string']):
        Controls the size of the thumb label.
      tick_labels (array):
        When provided with Array<string>, will attempt to map the labels
        to each step in index order
      tick_size (['number', 'string']):
        Controls the size of **ticks**
      ticks (['boolean', 'string']):
        Show track ticks. If `true` it shows ticks when using slider.
        If set to `'always'` it always shows ticks.
      track_color (string):
        Sets the track's color
      track_fill_color (string):
        Sets the track's fill color
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      vertical (boolean):
        Changes slider direction to vertical
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      end (event):
        Slider value emitted at the end of slider movement
      input (event):
        The updated bound model
      start (event):
        Slider value emitted at start of slider movement
      update_error (event):
        The `error.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slider", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "background_color",
            "color",
            "dark",
            "dense",
            "disabled",
            "error",
            "error_count",
            "error_messages",
            "height",
            "hide_details",
            "hint",
            "id",
            "inverse_label",
            "label",
            "light",
            "loader_height",
            "loading",
            "max",
            "messages",
            "min",
            "persistent_hint",
            "prepend_icon",
            "readonly",
            "rules",
            "step",
            "success",
            "success_messages",
            "thumb_color",
            "thumb_label",
            "thumb_size",
            "tick_labels",
            "tick_size",
            "ticks",
            "track_color",
            "track_fill_color",
            "validate_on_blur",
            "value",
            "vertical",
        ]
        self._event_names += [
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_prepend", "click:prepend"),
            "end",
            "input",
            "mousedown",
            "mouseup",
            "start",
            ("update_error", "update:error"),
        ]


class VSlideGroup(HtmlElement):
    """
    Vuetify's VSlideGroup component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-group>`_.

    Args:
      active_class (string):
        The **active-class** applied to children when they are activated.
      center_active (boolean):
        Forces the selected component to be centered
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max (['number', 'string']):
        Sets a maximum number of selections that can be made.
      mobile_breakpoint (['number', 'string']):
        Sets the designated mobile breakpoint for the component.
      multiple (boolean):
        Allow multiple selections. The **value** prop must be an _array_.
      next_icon (string):
        The appended slot when arrows are shown
      prev_icon (string):
        The prepended slot when arrows are shown
      show_arrows (['boolean', 'string']):
        Change when the overflow arrow indicators are shown. By **default**,
        arrows *always* display on Desktop when the container is overflowing.
        When the container overflows on mobile, arrows are not shown
        by default. A **show-arrows** value of `true` allows these arrows
        to show on Mobile if the container overflowing. A value of `desktop`
        *always* displays arrows on Desktop while a value of `mobile`
        always displays arrows on Mobile. A value of `always` always
        displays arrows on Desktop *and* Mobile. A value of `never` always
        hides the arrows. Find more information on how to customize breakpoint
        thresholds on the `breakpoints page </customizing/breakpoints>`_.
      tag (string):
        Specify a custom tag used on the root element.
      value (any):
        The designated model value for the component.
      value_comparator (function):
        Apply a custom value comparator function
      change (event):
        Emitted when the component value is changed by user interaction
      click_next (event):
        Emitted when the next is clicked
      click_prev (event):
        Emitted when the prev is clicked
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-group", children, **kwargs)
        self._attr_names += [
            "active_class",
            "center_active",
            "dark",
            "light",
            "mandatory",
            "max",
            "mobile_breakpoint",
            "multiple",
            "next_icon",
            "prev_icon",
            "show_arrows",
            "tag",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "change",
            ("click_next", "click:next"),
            ("click_prev", "click:prev"),
        ]


class VSlideItem(HtmlElement):
    """
    Vuetify's VSlideItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-item>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      disabled (boolean):
        Removes the ability to click or target the component.
      value (any):
        The value used when the component is selected in a group. If
        not provided, the index will be used.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-item", children, **kwargs)
        self._attr_names += [
            "active_class",
            "disabled",
            "value",
        ]
        self._event_names += []


class VSnackbar(HtmlElement):
    """
    Vuetify's VSnackbar component.
    See more `info and examples <https://vuetifyjs.com/api/v-snackbar>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      app (boolean):
        Respects boundaries of—and will not overlap with—other `app`
        components like `v-app-bar`, `v-navigation-drawer`, and `v-footer`.
      bottom (boolean):
        Aligns the component towards the bottom.
      centered (boolean):
        Positions the snackbar in the center of the screen, (x and y axis).
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      content_class (string):
        Apply a custom class to the snackbar content
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      height (['number', 'string']):
        Sets the height for the component.
      left (boolean):
        Aligns the component towards the left.
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      multi_line (boolean):
        Gives the snackbar a larger minimum height.
      outlined (boolean):
        Removes elevation (box-shadow) and adds a *thin* border.
      right (boolean):
        Aligns the component towards the right.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      tag (string):
        Specify a custom tag used on the root element.
      text (boolean):
        Applies the defined **color** to text and a low opacity background of the same.
      tile (boolean):
        Removes the component's **border-radius**.
      timeout (['number', 'string']):
        Time (in milliseconds) to wait until snackbar is automatically
        hidden.  Use `-1` to keep open indefinitely (`0` in version <
        2.3 ). It is recommended for this number to be between `4000`
        and `10000`. Changes to this property will reset the timeout.
      top (boolean):
        Aligns the content towards the top.
      transition (['boolean', 'string']):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      value (any):
        Controls whether the component is visible or hidden.
      vertical (boolean):
        Stacks snackbar content on top of the actions (button).
      width (['number', 'string']):
        Sets the width for the component.
      input (event):
        The updated bound model
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-snackbar", children, **kwargs)
        self._attr_names += [
            "absolute",
            "app",
            "bottom",
            "centered",
            "color",
            "content_class",
            "dark",
            "elevation",
            "height",
            "left",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "multi_line",
            "outlined",
            "right",
            "rounded",
            "shaped",
            "tag",
            "text",
            "tile",
            "timeout",
            "top",
            "transition",
            "value",
            "vertical",
            "width",
        ]
        self._event_names += [
            "input",
        ]


class VSparkline(HtmlElement):
    """
    Vuetify's VSparkline component.
    See more `info and examples <https://vuetifyjs.com/api/v-sparkline>`_.

    Args:
      auto_draw (boolean):
        Trace the length of the line when first rendered
      auto_draw_duration (number):
        Amount of time (in ms) to run the trace animation
      auto_draw_easing (string):
        The easing function to use for the trace animation
      auto_line_width (boolean):
        Automatically expand bars to use space efficiently
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      fill (boolean):
        Using the **fill** property allows you to better customize the
        look and feel of your sparkline.
      gradient (array):
        An array of colors to use as a linear-gradient
      gradient_direction (string):
        The direction the gradient should run
      height (['string', 'number']):
        Height of the SVG trendline or bars
      label_size (['number', 'string']):
        The label font size
      labels (array):
        An array of string labels that correspond to the same index as
        its data counterpart
      line_width (['string', 'number']):
        The thickness of the line, in px
      padding (['string', 'number']):
        Low `smooth` or high `line-width` values may result in cropping,
        increase padding to compensate
      show_labels (boolean):
        Show labels below each data point
      smooth (['boolean', 'number', 'string']):
        Number of px to use as a corner radius. `true` defaults to 8, `false` is 0
      type (string):
        Choose between a trendline or bars
      value (array):
        An array of numbers.
      width (['number', 'string']):
        Width of the SVG trendline or bars
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-sparkline", children, **kwargs)
        self._attr_names += [
            "auto_draw",
            "auto_draw_duration",
            "auto_draw_easing",
            "auto_line_width",
            "color",
            "fill",
            "gradient",
            "gradient_direction",
            "height",
            "label_size",
            "labels",
            "line_width",
            "padding",
            "show_labels",
            "smooth",
            "type",
            "value",
            "width",
        ]
        self._event_names += []


class VSpeedDial(HtmlElement):
    """
    Vuetify's VSpeedDial component.
    See more `info and examples <https://vuetifyjs.com/api/v-speed-dial>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      bottom (boolean):
        Aligns the component towards the bottom.
      direction (string):
        Direction in which speed-dial content will show. Possible values
        are `top`, `bottom`, `left`, `right`.
      fixed (boolean):
        Applies **position: fixed** to the component.
      left (boolean):
        Aligns the component towards the left.
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      open_on_hover (boolean):
        Opens speed-dial on hover
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
      right (boolean):
        Aligns the component towards the right.
      top (boolean):
        Aligns the content towards the top.
      transition (string):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      value (any):
        Controls whether the component is visible or hidden.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-speed-dial", children, **kwargs)
        self._attr_names += [
            "absolute",
            "bottom",
            "direction",
            "fixed",
            "left",
            "mode",
            "open_on_hover",
            "origin",
            "right",
            "top",
            "transition",
            "value",
        ]
        self._event_names += []


class VStepper(HtmlElement):
    """
    Vuetify's VStepper component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper>`_.

    Args:
      alt_labels (boolean):
        Places the labels beneath the step
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      flat (boolean):
        Removes the stepper's elevation.
      height (['number', 'string']):
        Sets the height for the component.
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      non_linear (boolean):
        Allow user to jump to any step
      outlined (boolean):
        Removes elevation (box-shadow) and adds a *thin* border.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      tag (string):
        Specify a custom tag used on the root element.
      tile (boolean):
        Removes the component's **border-radius**.
      value (any):
        The designated model value for the component.
      vertical (boolean):
        Display steps vertically
      width (['number', 'string']):
        Sets the width for the component.
      change (event):
        Emitted when step is changed by user interaction
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-stepper", children, **kwargs)
        self._attr_names += [
            "alt_labels",
            "color",
            "dark",
            "elevation",
            "flat",
            "height",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "non_linear",
            "outlined",
            "rounded",
            "shaped",
            "tag",
            "tile",
            "value",
            "vertical",
            "width",
        ]
        self._event_names += [
            "change",
        ]


class VStepperContent(HtmlElement):
    """
    Vuetify's VStepperContent component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-content>`_.

    Args:
      step (['number', 'string']):
        Sets step to associate the content to
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-stepper-content", children, **kwargs)
        self._attr_names += [
            "step",
        ]
        self._event_names += []


class VStepperStep(HtmlElement):
    """
    Vuetify's VStepperStep component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-step>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      complete (boolean):
        Marks step as complete
      complete_icon (string):
        Icon to display when step is marked as completed
      edit_icon (string):
        Icon to display when step is editable
      editable (boolean):
        Marks step as editable
      error_icon (string):
        Icon to display when step has an error
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      step (['number', 'string']):
        Content to display inside step circle
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-stepper-step", children, **kwargs)
        self._attr_names += [
            "color",
            "complete",
            "complete_icon",
            "edit_icon",
            "editable",
            "error_icon",
            "rules",
            "step",
        ]
        self._event_names += [
            "click",
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
        super().__init__("v-stepper-header", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VStepperItems(HtmlElement):
    """
    Vuetify's VStepperItems component.
    See more `info and examples <https://vuetifyjs.com/api/v-stepper-items>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-stepper-items", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VSubheader(HtmlElement):
    """
    Vuetify's VSubheader component.
    See more `info and examples <https://vuetifyjs.com/api/v-subheader>`_.

    Args:
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      inset (boolean):
        Adds indentation (72px)
      light (boolean):
        Applies the light theme variant to the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-subheader", children, **kwargs)
        self._attr_names += [
            "dark",
            "inset",
            "light",
        ]
        self._event_names += []


class VSwitch(HtmlElement):
    """
    Vuetify's VSwitch component.
    See more `info and examples <https://vuetifyjs.com/api/v-switch>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      background_color (string):
        Changes the background-color of the input
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the input height
      disabled (boolean):
        Disable the input
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      false_value (any):
        Sets value for falsy state
      flat (boolean):
        Display component without elevation. Default elevation for thumb
        is 4dp, `flat` resets it
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      input_value (any):
        The **v-model** bound value
      inset (boolean):
        Enlarge the `v-switch` track to encompass the thumb
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loading (['boolean', 'string']):
        Displays circular progress bar. Can either be a String which
        specifies which color is applied to the progress bar (any material
        color or theme color - primary, secondary, success, info, warning,
        error) or a Boolean which uses the component color (set by color
        prop - if it's supported by the component) or the primary color
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      multiple (boolean):
        Changes expected model to an array
      persistent_hint (boolean):
        Forces hint to always be visible
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      true_value (any):
        Sets value for truthy state
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      value_comparator (function):
        Apply a custom value comparator function
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      update_error (event):
        The `error.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-switch", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "background_color",
            "color",
            "dark",
            "dense",
            "disabled",
            "error",
            "error_count",
            "error_messages",
            "false_value",
            "flat",
            "hide_details",
            "hint",
            "id",
            "input_value",
            "inset",
            "label",
            "light",
            "loading",
            "messages",
            "multiple",
            "persistent_hint",
            "prepend_icon",
            "readonly",
            "ripple",
            "rules",
            "success",
            "success_messages",
            "true_value",
            "validate_on_blur",
            "value",
            "value_comparator",  # JS functions unimplemented
        ]
        self._event_names += [
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_prepend", "click:prepend"),
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
        ]


class VSystemBar(HtmlElement):
    """
    Vuetify's VSystemBar component.
    See more `info and examples <https://vuetifyjs.com/api/v-system-bar>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      app (boolean):
        Designates the component as part of the application layout. Used
        for dynamically adjusting content sizing. Components using this
        prop should reside **outside** of `v-main` component to function
        properly. You can find more information about layouts on the
        `application page </components/application>`_. **Note:** this
        prop automatically applies **position: fixed** to the layout
        element. You can overwrite this functionality by using the `absolute`
        prop
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      fixed (boolean):
        Applies **position: fixed** to the component.
      height (['number', 'string']):
        Sets the height for the component.
      light (boolean):
        Applies the light theme variant to the component.
      lights_out (boolean):
        Reduces the system bar opacity.
      window (boolean):
        Increases the system bar height to 32px (24px default).
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-system-bar", children, **kwargs)
        self._attr_names += [
            "absolute",
            "app",
            "color",
            "dark",
            "fixed",
            "height",
            "light",
            "lights_out",
            "window",
        ]
        self._event_names += []


class VTabs(HtmlElement):
    """
    Vuetify's VTabs component.
    See more `info and examples <https://vuetifyjs.com/api/v-tabs>`_.

    Args:
      active_class (string):
        The **active-class** applied to children when they are activated.
      align_with_title (boolean):
        Make `v-tabs` lined up with the toolbar title
      background_color (string):
        Changes the background color of the component.
      center_active (boolean):
        Forces the selected tab to be centered
      centered (boolean):
        Centers the tabs
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      fixed_tabs (boolean):
        `v-tabs-item` min-width 160px, max-width 360px
      grow (boolean):
        Force `v-tab`'s to take up all available space
      height (['number', 'string']):
        Sets the height of the tabs bar
      hide_slider (boolean):
        Hide's the generated `v-tabs-slider`
      icons_and_text (boolean):
        Will stack icon and text vertically
      light (boolean):
        Applies the light theme variant to the component.
      mobile_breakpoint (['string', 'number']):
        Sets the designated mobile breakpoint for the component.
      next_icon (string):
        Right pagination icon
      optional (boolean):
        Does not require an active item. Useful when using `v-tab` as a `router-link`
      prev_icon (string):
        Left pagination icon
      right (boolean):
        Aligns tabs to the right
      show_arrows (['boolean', 'string']):
        Show pagination arrows if the tab items overflow their container.
        For mobile devices, arrows will only display when using this
        prop.
      slider_color (string):
        Changes the background color of an auto-generated `v-tabs-slider`
      slider_size (['number', 'string']):
        Changes the size of the slider, **height** for horizontal, **width**
        for vertical.
      value (any):
        The designated model value for the component.
      vertical (boolean):
        Stacks tabs on top of each other vertically.
      change (event):
        Emitted when tab is changed by user interaction. Returns a string
        if **href** attribute is set and number if it is not.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tabs", children, **kwargs)
        self._attr_names += [
            "active_class",
            "align_with_title",
            "background_color",
            "center_active",
            "centered",
            "color",
            "dark",
            "fixed_tabs",
            "grow",
            "height",
            "hide_slider",
            "icons_and_text",
            "light",
            "mobile_breakpoint",
            "next_icon",
            "optional",
            "prev_icon",
            "right",
            "show_arrows",
            "slider_color",
            "slider_size",
            "value",
            "vertical",
        ]
        self._event_names += [
            "change",
        ]


class VTab(HtmlElement):
    """
    Vuetify's VTab component.
    See more `info and examples <https://vuetifyjs.com/api/v-tab>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      append (boolean):
        Setting **append** prop always appends the relative path to the
        current path. You can find more information about the `**append**
        prop <https://router.vuejs.org/api/#append>`_ on the vue-router
        documentation.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        Removes the ability to click or target the component.
      exact (boolean):
        Exactly match the link. Without this, '/' will match every route.
        You can find more information about the `**exact** prop <https://router.vuejs.org/api/#exact>`_
        on the vue-router documentation.
      exact_active_class (string):
        Configure the active CSS class applied when the link is active
        with exact match. You can find more information about the `**exact-active-class**
        prop <https://router.vuejs.org/api/#exact-active-class>`_ on
        the vue-router documentation.
      exact_path (boolean):
        Exactly match the link, ignoring the `query` and the `hash` sections.
        You can find more information about the `**exact-path** prop
        <https://router.vuejs.org/api/#exact-path>`_ on the vue-router
        documentation.
      href (['string', 'object']):
        Designates the component as anchor and applies the **href** attribute.
      light (boolean):
        Applies the light theme variant to the component.
      link (boolean):
        Designates that the component is a link. This is automatic when
        using the **href** or **to** prop.
      nuxt (boolean):
        Specifies the link is a `nuxt-link`. For use with the `nuxt framework
        <https://nuxtjs.org/api/components-nuxt-link/>`_.
      replace (boolean):
        Setting **replace** prop will call `router.replace(>`_` instead
        of `router.push(>`_` when clicked, so the navigation will not
        leave a history record. You can find more information about the
        `**replace** prop <https://router.vuejs.org/api/#replace>`_ on
        the vue-router documentation.
      ripple (['boolean', 'object']):
        Applies the `v-ripple </directives/ripple>`_ directive.
      tab_value (any):

      tag (string):
        Specify a custom tag used on the root element.
      target (string):
        Designates the target attribute. This should only be applied
        when using the **href** prop.
      to (['string', 'object']):
        Denotes the target route of the link. You can find more information
        about the `**to** prop <https://router.vuejs.org/api/#to>`_ on
        the vue-router documentation.
      change (event):
        Emitted when tab becomes active
      keydown (event):
        Emitted when **enter** key is pressed
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tab", children, **kwargs)
        self._attr_names += [
            "active_class",
            "append",
            "dark",
            "disabled",
            "exact",
            "exact_active_class",
            "exact_path",
            "href",
            "light",
            "link",
            "nuxt",
            "replace",
            "ripple",
            "tab_value",
            "tag",
            "target",
            "to",
        ]
        self._event_names += [
            "change",
            "click",
            "keydown",
        ]


class VTabItem(HtmlElement):
    """
    Vuetify's VTabItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-tab-item>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      disabled (boolean):
        Removes the ability to click or target the component.
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      id (string):
        Sets the DOM id on the component
      reverse_transition (['boolean', 'string']):
        Sets the reverse transition
      transition (['boolean', 'string']):
        The transition used when the component progressing through items.
        Can be one of the `built in transitions </styles/transitions>`_
        or one your own.
      value (any):
        Sets the value of the tab. If not provided, the index will be used.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tab-item", children, **kwargs)
        self._attr_names += [
            "active_class",
            "disabled",
            "eager",
            "id",
            "reverse_transition",
            "transition",
            "value",
        ]
        self._event_names += []


class VTabsItems(HtmlElement):
    """
    Vuetify's VTabsItems component.
    See more `info and examples <https://vuetifyjs.com/api/v-tabs-items>`_.

    Args:
      active_class (string):
        The **active-class** applied to children when they are activated.
      continuous (boolean):
        If `true`, window will "wrap around" from the last item to the
        first, and from the first item to the last
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      light (boolean):
        Applies the light theme variant to the component.
      mandatory (boolean):
        Forces a value to always be selected (if available).
      max (['number', 'string']):
        Sets a maximum number of selections that can be made.
      multiple (boolean):
        Allow multiple selections. The **value** prop must be an _array_.
      next_icon (['boolean', 'string']):
        Icon used for the "next" button if `show-arrows` is `true`
      prev_icon (['boolean', 'string']):
        Icon used for the "prev" button if `show-arrows` is `true`
      reverse (boolean):
        Reverse the normal transition direction.
      show_arrows (boolean):
        Display the "next" and "prev" buttons
      show_arrows_on_hover (boolean):
        Display the "next" and "prev" buttons on hover. `show-arrows` MUST ALSO be set.
      tag (string):
        Specify a custom tag used on the root element.
      touch (object):
        Provide a custom **left** and **right** function when swiped left or right.
      touchless (boolean):
        Disable touch support.
      value (any):
        The designated model value for the component.
      value_comparator (function):
        Apply a custom value comparator function
      vertical (boolean):
        Uses a vertical transition when changing windows.
      change (event):
        Emitted when user swipes between tabs.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tabs-items", children, **kwargs)
        self._attr_names += [
            "active_class",
            "continuous",
            "dark",
            "light",
            "mandatory",
            "max",
            "multiple",
            "next_icon",
            "prev_icon",
            "reverse",
            "show_arrows",
            "show_arrows_on_hover",
            "tag",
            "touch",
            "touchless",
            "value",
            "value_comparator",  # JS functions unimplemented
            "vertical",
        ]
        self._event_names += [
            "change",
        ]


class VTabsSlider(HtmlElement):
    """
    Vuetify's VTabsSlider component.
    See more `info and examples <https://vuetifyjs.com/api/v-tabs-slider>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tabs-slider", children, **kwargs)
        self._attr_names += [
            "color",
        ]
        self._event_names += []


class VTextarea(HtmlElement):
    """
    Vuetify's VTextarea component.
    See more `info and examples <https://vuetifyjs.com/api/v-textarea>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      append_outer_icon (string):
        Appends an icon to the outside the component's input, uses same
        syntax as `v-icon`
      auto_grow (boolean):
        Automatically grow the textarea depending on amount of text
      autofocus (boolean):
        Enables autofocus
      background_color (string):
        Changes the background-color of the input
      clear_icon (string):
        Applied when using **clearable** and the input is dirty
      clearable (boolean):
        Add input clear functionality, default icon is Material Design
        Icons **mdi-clear**
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      counter (['boolean', 'number', 'string']):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      counter_value (function):

      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the input height
      disabled (boolean):
        Disable the input
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      filled (boolean):
        Applies the alternate filled input style
      flat (boolean):
        Removes elevation (shadow) added to element when using the **solo**
        or **solo-inverted** props
      full_width (boolean):
        Designates input type as full-width
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      no_resize (boolean):
        Remove resize handle
      outlined (boolean):
        Applies the outlined style to the input
      persistent_hint (boolean):
        Forces hint to always be visible
      persistent_placeholder (boolean):
        Forces placeholder to always be visible
      placeholder (string):
        Sets the input's placeholder text
      prefix (string):
        Displays prefix text
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      prepend_inner_icon (string):
        Prepends an icon inside the component's input, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      reverse (boolean):
        Reverses the input orientation
      rounded (boolean):
        Adds a border radius to the input
      row_height (['number', 'string']):
        Height value for each row. Requires the use of the **auto-grow** prop.
      rows (['number', 'string']):
        Default row count
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      shaped (boolean):
        Round if `outlined` and increase `border-radius` if `filled`.
        Must be used with either `outlined` or `filled`
      single_line (boolean):
        Label does not move on focus/dirty
      solo (boolean):
        Changes the style of the input
      solo_inverted (boolean):
        Reduces element opacity until focused
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      suffix (string):
        Displays suffix text
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      blur (event):
        Emitted when the input is blurred
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_append-outer (event):
        Emitted when appended outer icon is clicked
      click_clear (event):
        Emitted when clearable icon clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      click_prepend-inner (event):
        Emitted when prepended inner icon is clicked
      focus (event):
        Emitted when component is focused
      input (event):
        The updated bound model
      keydown (event):
        Emitted when **any** key is pressed
      update_error (event):
        The `error.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-textarea", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "append_outer_icon",
            "auto_grow",
            "autofocus",
            "background_color",
            "clear_icon",
            "clearable",
            "color",
            "counter",
            "counter_value",  # JS functions unimplemented
            "dark",
            "dense",
            "disabled",
            "error",
            "error_count",
            "error_messages",
            "filled",
            "flat",
            "full_width",
            "height",
            "hide_details",
            "hint",
            "id",
            "label",
            "light",
            "loader_height",
            "loading",
            "messages",
            "no_resize",
            "outlined",
            "persistent_hint",
            "persistent_placeholder",
            "placeholder",
            "prefix",
            "prepend_icon",
            "prepend_inner_icon",
            "readonly",
            "reverse",
            "rounded",
            "row_height",
            "rows",
            "rules",
            "shaped",
            "single_line",
            "solo",
            "solo_inverted",
            "success",
            "success_messages",
            "suffix",
            "validate_on_blur",
            "value",
        ]
        self._event_names += [
            "blur",
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_append_outer", "click:append-outer"),
            ("click_clear", "click:clear"),
            ("click_prepend", "click:prepend"),
            ("click_prepend_inner", "click:prepend-inner"),
            "focus",
            "input",
            "keydown",
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
        ]


class VTextField(HtmlElement):
    """
    Vuetify's VTextField component.
    See more `info and examples <https://vuetifyjs.com/api/v-text-field>`_.

    Args:
      append_icon (string):
        Appends an icon to the component, uses the same syntax as `v-icon`
      append_outer_icon (string):
        Appends an icon to the outside the component's input, uses same
        syntax as `v-icon`
      autofocus (boolean):
        Enables autofocus
      background_color (string):
        Changes the background-color of the input
      clear_icon (string):
        Applied when using **clearable** and the input is dirty
      clearable (boolean):
        Add input clear functionality, default icon is Material Design
        Icons **mdi-clear**
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      counter (['boolean', 'number', 'string']):
        Creates counter for input length; if no number is specified,
        it defaults to 25. Does not apply any validation.
      counter_value (function):

      dark (boolean):
        Applies the dark theme variant to the component. This will default
        the components color to _white_ unless you've configured your
        `application theme </customization/theme>`_ to **dark** or if
        you are using the **color** prop on the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the input height
      disabled (boolean):
        Disable the input
      error (boolean):
        Puts the input in a manual error state
      error_count (['number', 'string']):
        The total number of errors that should display at once
      error_messages (['string', 'array']):
        Puts the input in an error state and passes through custom error
        messages. Will be combined with any validations that occur from
        the **rules** prop. This field will not trigger validation
      filled (boolean):
        Applies the alternate filled input style
      flat (boolean):
        Removes elevation (shadow) added to element when using the **solo**
        or **solo-inverted** props
      full_width (boolean):
        Designates input type as full-width
      height (['number', 'string']):
        Sets the height of the input
      hide_details (['boolean', 'string']):
        Hides hint and validation errors. When set to `auto` messages
        will be rendered only if there's a message (hint, error message,
        counter value etc) to display
      hide_spin_buttons (boolean):
        Hides spin buttons on the input when type is set to `number`.
      hint (string):
        Hint text
      id (string):
        Sets the DOM id on the component
      label (string):
        Sets input label
      light (boolean):
        Applies the light theme variant to the component.
      loader_height (['number', 'string']):
        Specifies the height of the loader
      loading (['boolean', 'string']):
        Displays linear progress bar. Can either be a String which specifies
        which color is applied to the progress bar (any material color
        or theme color - **primary**, **secondary**, **success**, **info**,
        **warning**, **error**) or a Boolean which uses the component
        **color** (set by color prop - if it's supported by the component)
        or the primary color
      messages (['string', 'array']):
        Displays a list of messages or message if using a string
      outlined (boolean):
        Applies the outlined style to the input
      persistent_hint (boolean):
        Forces hint to always be visible
      persistent_placeholder (boolean):
        Forces placeholder to always be visible
      placeholder (string):
        Sets the input’s placeholder text
      prefix (string):
        Displays prefix text
      prepend_icon (string):
        Prepends an icon to the component, uses the same syntax as `v-icon`
      prepend_inner_icon (string):
        Prepends an icon inside the component's input, uses the same syntax as `v-icon`
      readonly (boolean):
        Puts input in readonly state
      reverse (boolean):
        Reverses the input orientation
      rounded (boolean):
        Adds a border radius to the input
      rules (array):
        Accepts a mixed array of types `function`, `boolean` and `string`.
        Functions pass an input value as an argument and must return
        either `true` / `false` or a `string` containing an error message.
        The input field will enter an error state if a function returns
        (or any value in the array contains) `false` or is a `string`
      shaped (boolean):
        Round if `outlined` and increase `border-radius` if `filled`.
        Must be used with either `outlined` or `filled`
      single_line (boolean):
        Label does not move on focus/dirty
      solo (boolean):
        Changes the style of the input
      solo_inverted (boolean):
        Reduces element opacity until focused
      success (boolean):
        Puts the input in a manual success state
      success_messages (['string', 'array']):
        Puts the input in a success state and passes through custom success messages.
      suffix (string):
        Displays suffix text
      type (string):
        Sets input type
      validate_on_blur (boolean):
        Delays validation until blur event
      value (any):
        The input's value
      blur (event):
        Emitted when the input is blurred
      change (event):
        Emitted when the input is changed by user interaction
      click_append (event):
        Emitted when appended icon is clicked
      click_append-outer (event):
        Emitted when appended outer icon is clicked
      click_clear (event):
        Emitted when clearable icon clicked
      click_prepend (event):
        Emitted when prepended icon is clicked
      click_prepend-inner (event):
        Emitted when prepended inner icon is clicked
      focus (event):
        Emitted when component is focused
      input (event):
        The updated bound model
      keydown (event):
        Emitted when **any** key is pressed
      update_error (event):
        The `error.sync` event
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-text-field", children, **kwargs)
        self._attr_names += [
            "append_icon",
            "append_outer_icon",
            "autofocus",
            "background_color",
            "clear_icon",
            "clearable",
            "color",
            "counter",
            "counter_value",  # JS functions unimplemented
            "dark",
            "dense",
            "disabled",
            "error",
            "error_count",
            "error_messages",
            "filled",
            "flat",
            "full_width",
            "height",
            "hide_details",
            "hide_spin_buttons",
            "hint",
            "id",
            "label",
            "light",
            "loader_height",
            "loading",
            "messages",
            "outlined",
            "persistent_hint",
            "persistent_placeholder",
            "placeholder",
            "prefix",
            "prepend_icon",
            "prepend_inner_icon",
            "readonly",
            "reverse",
            "rounded",
            "rules",
            "shaped",
            "single_line",
            "solo",
            "solo_inverted",
            "success",
            "success_messages",
            "suffix",
            "type",
            "validate_on_blur",
            "value",
        ]
        self._event_names += [
            "blur",
            "change",
            "click",
            ("click_append", "click:append"),
            ("click_append_outer", "click:append-outer"),
            ("click_clear", "click:clear"),
            ("click_prepend", "click:prepend"),
            ("click_prepend_inner", "click:prepend-inner"),
            "focus",
            "input",
            "keydown",
            "mousedown",
            "mouseup",
            ("update_error", "update:error"),
        ]


class VThemeProvider(HtmlElement):
    """
    Vuetify's VThemeProvider component.
    See more `info and examples <https://vuetifyjs.com/api/v-theme-provider>`_.

    Args:
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      light (boolean):
        Applies the light theme variant to the component.
      root (boolean):
        Use the current value of `$vuetify.theme.dark` as opposed to the provided one.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-theme-provider", children, **kwargs)
        self._attr_names += [
            "dark",
            "light",
            "root",
        ]
        self._event_names += []


class VTimeline(HtmlElement):
    """
    Vuetify's VTimeline component.
    See more `info and examples <https://vuetifyjs.com/api/v-timeline>`_.

    Args:
      align_top (boolean):
        Align caret and dot of timeline items to the top
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Hide opposite slot content, and position all items to one side of timeline
      light (boolean):
        Applies the light theme variant to the component.
      reverse (boolean):
        Reverse direction of timeline items
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-timeline", children, **kwargs)
        self._attr_names += [
            "align_top",
            "dark",
            "dense",
            "light",
            "reverse",
        ]
        self._event_names += []


class VTimelineItem(HtmlElement):
    """
    Vuetify's VTimelineItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-timeline-item>`_.

    Args:
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      fill_dot (boolean):
        Remove padding from dot container
      hide_dot (boolean):
        Hide display of timeline dot
      icon (string):
        Specify icon for dot container
      icon_color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      large (boolean):
        Large size dot
      left (boolean):
        Explicitly set the item to a left orientation
      light (boolean):
        Applies the light theme variant to the component.
      right (boolean):
        Explicitly set the item to a right orientation
      small (boolean):
        Small size dot
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-timeline-item", children, **kwargs)
        self._attr_names += [
            "color",
            "dark",
            "fill_dot",
            "hide_dot",
            "icon",
            "icon_color",
            "large",
            "left",
            "light",
            "right",
            "small",
        ]
        self._event_names += []


class VTimePicker(HtmlElement):
    """
    Vuetify's VTimePicker component.
    See more `info and examples <https://vuetifyjs.com/api/v-time-picker>`_.

    Args:
      active_picker (string):
        Determines which picker is being displayed. Allowed values: `'HOUR'`,
        `'MINUTE'`, `'SECOND'`
      allowed_hours (['function', 'array']):
        Restricts which hours can be selected
      allowed_minutes (['function', 'array']):
        Restricts which minutes can be selected
      allowed_seconds (['function', 'array']):
        Restricts which seconds can be selected
      ampm_in_title (boolean):
        Place AM/PM switch in title, not near the clock.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      disabled (boolean):
        disables picker
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      flat (boolean):
        Removes  elevation
      format (string):
        Defines the format of a time displayed in picker. Available options
        are `ampm` and `24hr`.
      full_width (boolean):
        Forces 100% width
      header_color (string):
        Defines the header color. If not specified it will use the color
        defined by <code>color</code> prop or the default picker color
      landscape (boolean):
        Orients picker horizontal
      light (boolean):
        Applies the light theme variant to the component.
      max (string):
        Maximum allowed time
      min (string):
        Minimum allowed time
      no_title (boolean):
        Hide the picker title
      readonly (boolean):
        Puts picker in readonly state
      scrollable (boolean):
        Allows changing hour/minute with mouse scroll
      use_seconds (boolean):
        Toggles the use of seconds in picker
      value (any):
        Time picker model (ISO 8601 format, 24hr hh:mm)
      width (['number', 'string']):
        Width of the picker
      change (event):
        Emitted when the time selection is done (when user changes the
        minute for HH:MM picker and the second for HH:MM:SS picker
      click_hour (event):
        Emitted when user selects the hour
      click_minute (event):
        Emitted when user selects the minute
      click_second (event):
        Emitted when user selects the second
      input (event):
        The updated bound model
      update_active-picker (event):
        The `.sync` event for `active-picker` prop
      update_period (event):
        Emitted when user clicks the AM/PM button
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-time-picker", children, **kwargs)
        self._attr_names += [
            "active_picker",
            "allowed_hours",  # JS functions unimplemented
            "allowed_minutes",  # JS functions unimplemented
            "allowed_seconds",  # JS functions unimplemented
            "ampm_in_title",
            "color",
            "dark",
            "disabled",
            "elevation",
            "flat",
            "format",
            "full_width",
            "header_color",
            "landscape",
            "light",
            "max",
            "min",
            "no_title",
            "readonly",
            "scrollable",
            "use_seconds",
            "value",
            "width",
        ]
        self._event_names += [
            "change",
            ("click_hour", "click:hour"),
            ("click_minute", "click:minute"),
            ("click_second", "click:second"),
            "input",
            ("update_active_picker", "update:active-picker"),
            ("update_period", "update:period"),
        ]


class VToolbar(HtmlElement):
    """
    Vuetify's VToolbar component.
    See more `info and examples <https://vuetifyjs.com/api/v-toolbar>`_.

    Args:
      absolute (boolean):
        Applies position: absolute to the component.
      bottom (boolean):
        Aligns the component towards the bottom.
      collapse (boolean):
        Puts the toolbar into a collapsed state reducing its maximum width.
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Reduces the height of the toolbar content to 48px (96px when
        using the **prominent** prop).
      elevation (['number', 'string']):
        Designates an elevation applied to the component between 0 and
        24. You can find more information on the `elevation page </styles/elevation>`_.
      extended (boolean):
        Use this prop to increase the height of the toolbar _without_
        using the `extension` slot for adding content. May be used in
        conjunction with the **extension-height** prop, and any of the
        other props that affect the height of the toolbar, e.g. **prominent**,
        **dense**, etc., **WITH THE EXCEPTION** of **height**.
      extension_height (['number', 'string']):
        Specify an explicit height for the `extension` slot.
      flat (boolean):
        Removes the toolbar's box-shadow.
      floating (boolean):
        Applies **display: inline-flex** to the component.
      height (['number', 'string']):
        Designates a specific height for the toolbar. Overrides the heights
        imposed by other props, e.g. **prominent**, **dense**, **extended**,
        etc.
      light (boolean):
        Applies the light theme variant to the component.
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      outlined (boolean):
        Removes elevation (box-shadow) and adds a *thin* border.
      prominent (boolean):
        Increases the height of the toolbar content to 128px.
      rounded (['boolean', 'string']):
        Designates the **border-radius** applied to the component. You
        can find more information on the `Border Radius page </styles/border-radius>`_.
      shaped (boolean):
        Applies a large border radius on the top left and bottom right of the card.
      short (boolean):
        Reduce the height of the toolbar content to 56px (112px when
        using the **prominent** prop).
      src (['string', 'object']):
        Specifies a `v-img </components/images>`_ as the component's background.
      tag (string):
        Specify a custom tag used on the root element.
      tile (boolean):
        Removes the component's **border-radius**.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-toolbar", children, **kwargs)
        self._attr_names += [
            "absolute",
            "bottom",
            "collapse",
            "color",
            "dark",
            "dense",
            "elevation",
            "extended",
            "extension_height",
            "flat",
            "floating",
            "height",
            "light",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "outlined",
            "prominent",
            "rounded",
            "shaped",
            "short",
            "src",
            "tag",
            "tile",
            "width",
        ]
        self._event_names += []


class VToolbarItems(HtmlElement):
    """
    Vuetify's VToolbarItems component.
    See more `info and examples <https://vuetifyjs.com/api/v-toolbar-items>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-toolbar-items", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VToolbarTitle(HtmlElement):
    """
    Vuetify's VToolbarTitle component.
    See more `info and examples <https://vuetifyjs.com/api/v-toolbar-title>`_.

    Args:
      tag (string):
        Specify a custom tag used on the root element.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-toolbar-title", children, **kwargs)
        self._attr_names += [
            "tag",
        ]
        self._event_names += []


class VTooltip(HtmlElement):
    """
    Vuetify's VTooltip component.
    See more `info and examples <https://vuetifyjs.com/api/v-tooltip>`_.

    Args:
      absolute (boolean):
        Applies **position: absolute** to the component.
      activator (any):
        Designate a custom activator when the `activator` slot is not
        used. String can be any valid querySelector and Object can be
        any valid Node.
      allow_overflow (boolean):
        Removes overflow re-positioning for the content
      attach (any):
        Specifies which DOM element that this component should detach
        to. String can be any valid querySelector and Object can be any
        valid Node. This will attach to the root `v-app` component by
        default.
      bottom (boolean):
        Aligns the component towards the bottom.
      close_delay (['number', 'string']):
        Delay (in ms) after which menu closes (when open-on-hover prop is set to true)
      color (string):
        Applies specified color to the control - it can be the name of
        material color (for example `success` or `purple`>`_ or css color
        (`#033` or `rgba(255, 0, 0, 0.5>`_`>`_. You can find a list of
        built-in classes on the `colors page </styles/colors#material-colors>`_.
      content_class (string):
        Applies a custom class to the detached element. This is useful
        because the content is moved to the beginning of the `v-app`
        component (unless the **attach** prop is provided) and is not
        targetable by classes passed directly on the component.
      disabled (boolean):
        Disables the tooltip
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      internal_activator (boolean):
        Designates whether to use an internal activator
      left (boolean):
        Aligns the component towards the left.
      max_width (['number', 'string']):
        Sets the maximum width for the content
      min_width (['number', 'string']):
        Sets the minimum width for the content
      nudge_bottom (['number', 'string']):
        Nudge the content to the bottom
      nudge_left (['number', 'string']):
        Nudge the content to the left
      nudge_right (['number', 'string']):
        Nudge the content to the right
      nudge_top (['number', 'string']):
        Nudge the content to the top
      nudge_width (['number', 'string']):
        Nudge the content width
      offset_overflow (boolean):
        Causes the component to flip to the opposite side when repositioned
        due to overflow
      open_delay (['number', 'string']):
        Delay (in ms) after which tooltip opens (when `open-on-hover`
        prop is set to **true**)
      open_on_click (boolean):
        Designates whether the tooltip should open on activator click
      open_on_focus (boolean):

      open_on_hover (boolean):
        Designates whether the tooltip should open on activator hover
      position_x (number):
        Used to position the content when not using an activator slot
      position_y (number):
        Used to position the content when not using an activator slot
      right (boolean):
        Aligns the component towards the right.
      tag (string):
        Specifies a custom tag for the activator wrapper
      top (boolean):
        Aligns the content towards the top.
      transition (string):
        Sets the component transition. Can be one of the `built in transitions
        </styles/transitions>`_ or one your own.
      value (any):
        Controls whether the component is visible or hidden.
      z_index (['number', 'string']):
        The z-index used for the component
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tooltip", children, **kwargs)
        self._attr_names += [
            "absolute",
            "activator",
            "allow_overflow",
            "attach",
            "bottom",
            "close_delay",
            "color",
            "content_class",
            "disabled",
            "eager",
            "internal_activator",
            "left",
            "max_width",
            "min_width",
            "nudge_bottom",
            "nudge_left",
            "nudge_right",
            "nudge_top",
            "nudge_width",
            "offset_overflow",
            "open_delay",
            "open_on_click",
            "open_on_focus",
            "open_on_hover",
            "position_x",
            "position_y",
            "right",
            "tag",
            "top",
            "transition",
            "value",
            "z_index",
        ]
        self._event_names += []


class VTreeview(HtmlElement):
    """
    Vuetify's VTreeview component.
    See more `info and examples <https://vuetifyjs.com/api/v-treeview>`_.

    Args:
      activatable (boolean):
        Allows user to mark a node as active by clicking on it
      active (array):
        Syncable prop that allows one to control which nodes are active.
        The array consists of the `item-key` of each active item.
      active_class (string):
        The class applied to the node when active
      color (string):
        Sets the color of the active node
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      dense (boolean):
        Decreases the height of the items
      disable_per_node (boolean):
        Prevents disabling children nodes
      disabled (boolean):
        Disables selection for all nodes
      expand_icon (string):
        Icon used to indicate that a node can be expanded
      filter (function):
        Custom item filtering function. By default it will use case-insensitive
        search in item's label.
      hoverable (boolean):
        Applies a hover class when mousing over nodes
      indeterminate_icon (string):
        Icon used when node is in an indeterminate state. Only visible
        when `selectable` is `true`.
      item_children (string):
        Property on supplied `items` that contains its children
      item_disabled (string):
        Property on supplied `items` that contains the disabled state of the item
      item_key (string):
        Property on supplied `items` used to keep track of node state.
        The value of this property has to be unique among all items.
      item_text (string):
        Property on supplied `items` that contains its label text
      items (array):
        An array of items used to build the treeview
      light (boolean):
        Applies the light theme variant to the component.
      load_children (function):
        A function used when dynamically loading children. If this prop
        is set, then the supplied function will be run if expanding an
        item that has a `item-children` property that is an empty array.
        Supports returning a Promise.
      loading_icon (string):
        Icon used when node is in a loading state
      multiple_active (boolean):
        When `true`, allows user to have multiple active nodes at the same time
      off_icon (string):
        Icon used when node is not selected. Only visible when `selectable` is `true`.
      on_icon (string):
        Icon used when leaf node is selected or when a branch node is
        fully selected. Only visible when `selectable` is `true`.
      open (array):
        Syncable prop that allows one to control which nodes are open.
        The array consists of the `item-key` of each open item.
      open_all (boolean):
        When `true` will cause all branch nodes to be opened when component is mounted
      open_on_click (boolean):
        When `true` will cause nodes to be opened by clicking anywhere
        on it, instead of only opening by clicking on expand icon. When
        using this prop with `activatable` you will be unable to mark
        nodes with children as active.
      return_object (boolean):
        When `true` will make `v-model`, `active.sync` and `open.sync`
        return the complete object instead of just the key
      rounded (boolean):
        Provides an alternative active style for `v-treeview` node. Only
        visible when `activatable` is `true` and should not be used in
        conjunction with the `shaped` prop.
      search (string):
        The search model for filtering results
      selectable (boolean):
        Will render a checkbox next to each node allowing them to be selected
      selected_color (string):
        The color of the selection checkbox
      selection_type (string):
        Controls how the treeview selects nodes. There are two modes
        available: 'leaf' and 'independent'
      shaped (boolean):
        Provides an alternative active style for `v-treeview` node. Only
        visible when `activatable` is `true` and should not be used in
        conjunction with the `rounded` prop.
      transition (boolean):
        Applies a transition when nodes are opened and closed
      value (array):
        Allows one to control which nodes are selected. The array consists
        of the `item-key` of each selected item. Is used with `@input`
        event to allow for `v-model` binding.
      input (event):
        Emits the array of selected items when this value changes
      update_active (event):
        Emits the array of active items when this value changes
      update_open (event):
        Emits the array of open items when this value changes
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-treeview", children, **kwargs)
        self._attr_names += [
            "activatable",
            "active",
            "active_class",
            "color",
            "dark",
            "dense",
            "disable_per_node",
            "disabled",
            "expand_icon",
            "filter",  # JS functions unimplemented
            "hoverable",
            "indeterminate_icon",
            "item_children",
            "item_disabled",
            "item_key",
            "item_text",
            "items",
            "light",
            "load_children",  # JS functions unimplemented
            "loading_icon",
            "multiple_active",
            "off_icon",
            "on_icon",
            "open",
            "open_all",
            "open_on_click",
            "return_object",
            "rounded",
            "search",
            "selectable",
            "selected_color",
            "selection_type",
            "shaped",
            "transition",
            "value",
        ]
        self._event_names += [
            "input",
            ("update_active", "update:active"),
            ("update_open", "update:open"),
        ]


class VVirtualScroll(HtmlElement):
    """
    Vuetify's VVirtualScroll component.
    See more `info and examples <https://vuetifyjs.com/api/v-virtual-scroll>`_.

    Args:
      bench (['number', 'string']):
        The number of items **outside** the user view that are rendered
        (even if they are **not** viewable); to help prevent empty white
        space when scrolling *fast*.
      height (['number', 'string']):
        Height of the component as a css value
      item_height (['number', 'string']):
        Height in pixels of the items to display
      items (array):
        The array of items to display
      max_height (['number', 'string']):
        Sets the maximum height for the component.
      max_width (['number', 'string']):
        Sets the maximum width for the component.
      min_height (['number', 'string']):
        Sets the minimum height for the component.
      min_width (['number', 'string']):
        Sets the minimum width for the component.
      width (['number', 'string']):
        Sets the width for the component.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-virtual-scroll", children, **kwargs)
        self._attr_names += [
            "bench",
            "height",
            "item_height",
            "items",
            "max_height",
            "max_width",
            "min_height",
            "min_width",
            "width",
        ]
        self._event_names += []


class VWindow(HtmlElement):
    """
    Vuetify's VWindow component.
    See more `info and examples <https://vuetifyjs.com/api/v-window>`_.

    Args:
      active_class (string):
        The **active-class** applied to children when they are activated.
      continuous (boolean):
        If `true`, window will "wrap around" from the last item to the
        first, and from the first item to the last
      dark (boolean):
        Applies the dark theme variant to the component. You can find
        more information on the Material Design documentation for `dark
        themes <https://material.io/design/color/dark-theme.html>`_.
      light (boolean):
        Applies the light theme variant to the component.
      next_icon (['boolean', 'string']):
        Icon used for the "next" button if `show-arrows` is `true`
      prev_icon (['boolean', 'string']):
        Icon used for the "prev" button if `show-arrows` is `true`
      reverse (boolean):
        Reverse the normal transition direction.
      show_arrows (boolean):
        Display the "next" and "prev" buttons
      show_arrows_on_hover (boolean):
        Display the "next" and "prev" buttons on hover. `show-arrows` MUST ALSO be set.
      tag (string):
        Specify a custom tag used on the root element.
      touch (object):
        Provide a custom **left** and **right** function when swiped left or right.
      touchless (boolean):
        Disable touch support.
      value (any):
        The designated model value for the component.
      value_comparator (function):
        Apply a custom value comparator function
      vertical (boolean):
        Uses a vertical transition when changing windows.
      change (event):
        Emitted when the component value is changed by user interaction
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-window", children, **kwargs)
        self._attr_names += [
            "active_class",
            "continuous",
            "dark",
            "light",
            "next_icon",
            "prev_icon",
            "reverse",
            "show_arrows",
            "show_arrows_on_hover",
            "tag",
            "touch",
            "touchless",
            "value",
            "value_comparator",  # JS functions unimplemented
            "vertical",
        ]
        self._event_names += [
            "change",
        ]


class VWindowItem(HtmlElement):
    """
    Vuetify's VWindowItem component.
    See more `info and examples <https://vuetifyjs.com/api/v-window-item>`_.

    Args:
      active_class (string):
        Configure the active CSS class applied when the link is active.
        You can find more information about the `**active-class** prop
        <https://router.vuejs.org/api/#active-class>`_ on the vue-router
        documentation.
      disabled (boolean):
        Prevents the item from becoming active when using the "next"
        and "prev" buttons or the `toggle` method
      eager (boolean):
        Will force the components content to render on mounted. This
        is useful if you have content that will not be rendered in the
        DOM that you want crawled for SEO.
      reverse_transition (['boolean', 'string']):
        Sets the reverse transition
      transition (['boolean', 'string']):
        The transition used when the component progressing through items.
        Can be one of the `built in transitions </styles/transitions>`_
        or one your own.
      value (any):
        The value used when the component is selected in a group. If
        not provided, the index will be used.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-window-item", children, **kwargs)
        self._attr_names += [
            "active_class",
            "disabled",
            "eager",
            "reverse_transition",
            "transition",
            "value",
        ]
        self._event_names += []


class VCarouselTransition(HtmlElement):
    """
    Vuetify's VCarouselTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-carousel-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-carousel-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VCarouselReverseTransition(HtmlElement):
    """
    Vuetify's VCarouselReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-carousel-reverse-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-carousel-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VTabTransition(HtmlElement):
    """
    Vuetify's VTabTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-tab-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tab-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VTabReverseTransition(HtmlElement):
    """
    Vuetify's VTabReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-tab-reverse-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-tab-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VMenuTransition(HtmlElement):
    """
    Vuetify's VMenuTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-menu-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-menu-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VFabTransition(HtmlElement):
    """
    Vuetify's VFabTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-fab-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-fab-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VDialogTransition(HtmlElement):
    """
    Vuetify's VDialogTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-dialog-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-dialog-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VDialogBottomTransition(HtmlElement):
    """
    Vuetify's VDialogBottomTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-dialog-bottom-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-dialog-bottom-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VDialogTopTransition(HtmlElement):
    """
    Vuetify's VDialogTopTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-dialog-top-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-dialog-top-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VFadeTransition(HtmlElement):
    """
    Vuetify's VFadeTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-fade-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-fade-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VScaleTransition(HtmlElement):
    """
    Vuetify's VScaleTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scale-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scale-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollXTransition(HtmlElement):
    """
    Vuetify's VScrollXTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scroll-x-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scroll-x-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollXReverseTransition(HtmlElement):
    """
    Vuetify's VScrollXReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scroll-x-reverse-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scroll-x-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollYTransition(HtmlElement):
    """
    Vuetify's VScrollYTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scroll-y-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scroll-y-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VScrollYReverseTransition(HtmlElement):
    """
    Vuetify's VScrollYReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-scroll-y-reverse-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-scroll-y-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideXTransition(HtmlElement):
    """
    Vuetify's VSlideXTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-x-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-x-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideXReverseTransition(HtmlElement):
    """
    Vuetify's VSlideXReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-x-reverse-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-x-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideYTransition(HtmlElement):
    """
    Vuetify's VSlideYTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-y-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-y-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VSlideYReverseTransition(HtmlElement):
    """
    Vuetify's VSlideYReverseTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-slide-y-reverse-transition>`_.

    Args:
      group (boolean):
        Creates a `transition-group` component. `vue docs <https://vuejs.org/v2/api/#transition-group>`_
      hide_on_leave (boolean):
        Hides the leaving element (no exit animation)
      leave_absolute (boolean):
        Absolutely positions the leaving element (useful for `FLIP <https://aerotwist.com/blog/flip-your-animations/>`_>`_
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
      origin (string):
        Sets the transition origin on the element. You can find more
        information on the MDN documentation `for transition origin <https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-slide-y-reverse-transition", children, **kwargs)
        self._attr_names += [
            "group",
            "hide_on_leave",
            "leave_absolute",
            "mode",
            "origin",
        ]
        self._event_names += []


class VExpandTransition(HtmlElement):
    """
    Vuetify's VExpandTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-expand-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expand-transition", children, **kwargs)
        self._attr_names += [
            "mode",
        ]
        self._event_names += []


class VExpandXTransition(HtmlElement):
    """
    Vuetify's VExpandXTransition component.
    See more `info and examples <https://vuetifyjs.com/api/v-expand-x-transition>`_.

    Args:
      mode (string):
        Sets the transition mode (does not apply to transition-group>`_.
        You can find more information on the Vue documentation `for transition
        modes <https://vuejs.org/v2/api/#transition>`_.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-expand-x-transition", children, **kwargs)
        self._attr_names += [
            "mode",
        ]
        self._event_names += []
