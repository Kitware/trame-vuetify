.. |pypi_download| image:: https://img.shields.io/pypi/dm/trame-vuetify

trame-vuetify: Material Design widgets |pypi_download|
===========================================================================

.. image:: https://github.com/Kitware/trame-vuetify/actions/workflows/test_and_release.yml/badge.svg
    :target: https://github.com/Kitware/trame-vuetify/actions/workflows/test_and_release.yml
    :alt: Test and Release

Trame-vuetify extend trame **widgets** and **ui** with all the beautiful Vuetify UI components.
Vuetify is a UI Library with beautifully handcrafted Material Components. No design skills required — everything you need to create amazing applications is at your fingertips.

This package is not supposed to be used by itself but rather should come as a dependency of **trame**.
For any specificity, please refer to `the trame documentation <https://kitware.github.io/trame/>`_.


Installing
-----------------------------------------------------------

trame-vuetify can be installed with `pip <https://pypi.org/project/trame-vuetify/>`_:

.. code-block:: bash

    pip install --upgrade trame-vuetify


Usage
-----------------------------------------------------------

The `Trame Tutorial <https://kitware.github.io/trame/guide/tutorial>`_ is the place to go to learn how to use the library and start building your own application.

The `API Reference <https://trame.readthedocs.io/en/latest/index.html>`_ documentation provides API-level documentation.

The `Vuetify website <https://vuetifyjs.com/en/>`_ is very well made for exploring components and understanding components' parameters and controls, while a reference to our wrapper API is available `here <https://trame-vuetify.readthedocs.io/en/latest/trame.html.vuetify.html>`_.

The way trame translate Vue templates into plain Python code is by doing the following.


Material Design Widgets
```````````````````````````````````````````````````````````

First you need to import the `vuetify` module so you can instantiate the various Material Components like illustrated below. Moreover, in the documentation the component names use dashes as separators while in Python we use the Camelcase notation for the class name.

.. code-block:: python

    from trame.widgets import vuetify

    # <v-btn>Hello World</v-btn>
    btn = vuetify.VBtn("Hello World")

Boolean attributes
```````````````````````````````````````````````````````````

Implicit attribute values must be made explicit in Python by assigning `True` to them.

.. code-block:: python

    # <v-text-field disabled />
    vuetify.VTextField(disabled=True)


Dash and colon separators
```````````````````````````````````````````````````````````

Any special characters (`-` and `:`) become `_` in Python.

.. code-block:: python

    # <v-text-field v-model="myText" />
    vuetify.VTextField(v_model=("myText",))


Events
```````````````````````````````````````````````````````````

Events in vue are prefixed with a `@` but in Python we declare them the same way we declare regular attributes.

.. code-block:: python

    def runMethod():
        pass

    # <v-btn @click="runMethod" />
    vuetify.VBtn(click=runMethod)


License
-----------------------------------------------------------

trame-vuetify is made available under the MIT License. For more details, see `LICENSE <https://github.com/Kitware/trame-vuetify/blob/master/LICENSE>`_
This license has been chosen to match the one use by `Vuetify <https://github.com/vuetifyjs/vuetify/blob/master/LICENSE.md>`_ which is instrumental for making that library possible.


Community
-----------------------------------------------------------

`Trame <https://kitware.github.io/trame/>`_ | `Discussions <https://github.com/Kitware/trame/discussions>`_ | `Issues <https://github.com/Kitware/trame/issues>`_ | `Contact Us <https://www.kitware.com/contact-us/>`_

.. image:: https://zenodo.org/badge/410108340.svg
    :target: https://zenodo.org/badge/latestdoi/410108340


Enjoying trame?
-----------------------------------------------------------

Share your experience `with a testimonial <https://github.com/Kitware/trame/issues/18>`_ or `with a brand approval <https://github.com/Kitware/trame/issues/19>`_.


JavaScript dependency
-----------------------------------------------------------

This Python package bundle the following Vuetify libraries. For ``client_type="vue2"``, it exposes ``vuetify@2.7.1`` and for ``client_type="vue3"``, it exposes ``vuetify@3.8.0``.
If you would like us to upgrade any of those dependencies, `please reach out <https://www.kitware.com/trame/>`_.
