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
