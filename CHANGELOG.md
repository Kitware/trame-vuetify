# CHANGELOG


## v2.9.0 (2025-03-28)

### Features

- **v3.7.19**: Update vuetify and add missing fonts
  ([`cc62ae2`](https://github.com/Kitware/trame-vuetify/commit/cc62ae2b4d620d617bffed74baf5ba3bde424f6f))


## v2.8.2 (2025-03-25)

### Bug Fixes

- **copyright**: Update copyright dates
  ([`a53d702`](https://github.com/Kitware/trame-vuetify/commit/a53d702a7b058c678db84d0f0b59f1683e400702))


## v2.8.1 (2025-01-23)

### Bug Fixes

- Replace applymap with map for dataframe serialization
  ([`ac30ba3`](https://github.com/Kitware/trame-vuetify/commit/ac30ba361f078e547778040dbfd2388a5cff88e2))

### Documentation

- Update README.rst
  ([`56ab62b`](https://github.com/Kitware/trame-vuetify/commit/56ab62b29e9ad3dbd2ff082325bfd76a1d934b32))

- **js**: List JS dependency
  ([`39354d7`](https://github.com/Kitware/trame-vuetify/commit/39354d7b689c72520268901b487cc74462c4322e))


## v2.8.0 (2024-12-31)

### Bug Fixes

- **ruff**: Noqa F403 for trame imports
  ([`f20bc9c`](https://github.com/Kitware/trame-vuetify/commit/f20bc9c9bbe7620087867411afb6ea69d1866ce1))

### Continuous Integration

- Update to v3.7.6
  ([`c8fefd5`](https://github.com/Kitware/trame-vuetify/commit/c8fefd56551399546b8d6d76190425aa3ca19da2))

### Features

- **v3.7.6**: Update generator and version
  ([`9d80364`](https://github.com/Kitware/trame-vuetify/commit/9d80364b77f0fc8b2d777a3c375c26eb30e87540))


## v2.7.2 (2024-11-14)

### Bug Fixes

- **layout**: Singlepagelayout vue warnings
  ([`bdcb663`](https://github.com/Kitware/trame-vuetify/commit/bdcb66308292bf7c4fb9af7590c5f4cf8f5715e0))

### Continuous Integration

- Fix pre-commit
  ([`a582382`](https://github.com/Kitware/trame-vuetify/commit/a58238292034ea8166897fa7b5a077b32eef3da8))

- Website
  ([`465ab7a`](https://github.com/Kitware/trame-vuetify/commit/465ab7a4f1bd62abb35ee95240a15adb74db4908))

### Documentation

- Spelling
  ([`93fe89b`](https://github.com/Kitware/trame-vuetify/commit/93fe89bb2297a2084b39e338ffb85dda3ba30c39))

- **example**: Add multi slider time controller
  ([`a5faf22`](https://github.com/Kitware/trame-vuetify/commit/a5faf228a0c3a4921941566a499f196be2a7c80a))

- **website**: Add vitepress website
  ([`e789a54`](https://github.com/Kitware/trame-vuetify/commit/e789a54f28160751051b17256c905df2f5d7d250))


## v2.7.1 (2024-09-03)

### Bug Fixes

- **lab**: Set vuetify to 3.7.1
  ([`cc388ac`](https://github.com/Kitware/trame-vuetify/commit/cc388ac22d52909c18d3b7ed8ad0c8b141639b4c))


## v2.7.0 (2024-08-28)

### Features

- **3.7.1**: Update to vuetify 3.7.1
  ([`78f2616`](https://github.com/Kitware/trame-vuetify/commit/78f2616690cb8993b6c6d3a15ea26e810daf75e2))


## v2.6.2 (2024-07-21)

### Bug Fixes

- **get_trame_versions**: Avoid errors
  ([`ce320be`](https://github.com/Kitware/trame-vuetify/commit/ce320be356876c48f6117a7fae0bbd774c313440))

For some currently unknown reason, not every PathDistribution contains a "Name" in the metadata.
  These are probably not trame packages and thus we can probably just ignore them. But if we notice
  that we are missing trame packages in the future, we should potentially find an alternative way to
  identify them.

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>


## v2.6.1 (2024-07-03)

### Bug Fixes

- Avoid pkg_resources for get_trame_versions()
  ([`49010b3`](https://github.com/Kitware/trame-vuetify/commit/49010b30eb9cff1202822f494af50a54cd338e6c))

`pkg_resources` is not always available for newer setups. But since trame requires python 3.8,
  `importlib.metadata` can be used instead. Update `get_trame_versions()` to use
  `importlib.metadata` instead of `pkg_resources`.

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

### Documentation

- **example**: Update tree example
  ([`4648a2c`](https://github.com/Kitware/trame-vuetify/commit/4648a2cd3ba9314f222c5ae4c3513a97f7426884))

- **lab**: Add another tree example
  ([`67381d0`](https://github.com/Kitware/trame-vuetify/commit/67381d04d6242602ff482a5c14ecc3a711516443))


## v2.6.0 (2024-06-11)

### Continuous Integration

- Fix path for vue-lab
  ([`f75ecde`](https://github.com/Kitware/trame-vuetify/commit/f75ecde72eb0ddd61f8642305ae756d571914a13))

- Vuetify-lab
  ([`3baeda6`](https://github.com/Kitware/trame-vuetify/commit/3baeda62bdbde69da521637417fa09f16a44286b))

- Vuetify-lab
  ([`6e1902c`](https://github.com/Kitware/trame-vuetify/commit/6e1902c3d8e5876b8a8fd7d1e36a2769cf3fea98))

### Features

- **lab**: Add option to enable lab components
  ([`8e06f4d`](https://github.com/Kitware/trame-vuetify/commit/8e06f4da534c279ffc0f338ba6cc342031105621))


## v2.5.0 (2024-05-06)

### Features

- **3.6.3**: Expose Vuetify v3.6.3
  ([`55bac1b`](https://github.com/Kitware/trame-vuetify/commit/55bac1b08112ee949a4982ebccd93a708aade9e3))


## v2.4.3 (2024-03-13)

### Bug Fixes

- Uniform __init__.py for package
  ([`28deeaa`](https://github.com/Kitware/trame-vuetify/commit/28deeaaae6c569e3059975e4275a573fd1a9d7e4))

### Documentation

- **example**: Expend stepper with custom actions
  ([`66720b6`](https://github.com/Kitware/trame-vuetify/commit/66720b6cc4ad346aa24900b219bfe85836ac35df))


## v2.4.2 (2024-01-18)

### Bug Fixes

- **release**: Patch ci to release the proper version
  ([`ebbdf80`](https://github.com/Kitware/trame-vuetify/commit/ebbdf80db78a15c9f25658222c55e2703d17704e))

### Documentation

- **examples**: More vuetify3 examples
  ([`015c81e`](https://github.com/Kitware/trame-vuetify/commit/015c81e8426a6a86c6d2fcd3ddaaaf51f86fff9d))


## v2.4.1 (2024-01-17)

### Bug Fixes

- **vuetify3**: Allow to provide config
  ([`9aebd64`](https://github.com/Kitware/trame-vuetify/commit/9aebd64728ed6746604569561633e0cd4f7c1ff8))


## v2.4.0 (2024-01-17)

### Continuous Integration

- **tests**: Use vue3 by default
  ([`4b487b8`](https://github.com/Kitware/trame-vuetify/commit/4b487b8fc1125f19d1f06e56d81d03407e19a7a6))

### Documentation

- **datatable**: Advanced slot usage
  ([`74f77be`](https://github.com/Kitware/trame-vuetify/commit/74f77be2a9b7a43f5438615ea59d0e5e483f0474))

### Features

- **vue2**: Update to vuetify 2.7.1
  ([`9a97abf`](https://github.com/Kitware/trame-vuetify/commit/9a97abf81aa32060403b5e4d32274927727bcd7a))

- **vue3**: Update to vuetify 3.4.10
  ([`814d428`](https://github.com/Kitware/trame-vuetify/commit/814d4283900f5bc5a7234058ee493a3a304931ce))


## v2.3.1 (2023-07-19)

### Bug Fixes

- **vuetify2**: Add vuetify2 namespace
  ([`4d9c9e1`](https://github.com/Kitware/trame-vuetify/commit/4d9c9e1278c26989362cde28d6a9c862426d5846))


## v2.3.0 (2023-07-19)

### Features

- **versions**: Bump to v2.7.0 and v3.3.9
  ([`e691dee`](https://github.com/Kitware/trame-vuetify/commit/e691dee9564e91f872114e6dd611d500c2d251f7))


## v2.2.4 (2023-02-26)

### Bug Fixes

- **vue3**: Update to new template syntax
  ([`b839955`](https://github.com/Kitware/trame-vuetify/commit/b8399555bfce9370474347d16182458b756bdb55))


## v2.2.3 (2023-02-23)

### Bug Fixes

- **version**: Add __version__
  ([`fdf7ff5`](https://github.com/Kitware/trame-vuetify/commit/fdf7ff57d2f13c4bc58edb051aff922c2da93508))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>


## v2.2.2 (2023-02-14)

### Bug Fixes

- **warn**: Prevent prop type warning
  ([`e53aae7`](https://github.com/Kitware/trame-vuetify/commit/e53aae76c563b7bcc6a16584b8573747b293d057))


## v2.2.1 (2023-02-13)

### Bug Fixes

- **vue3**: Convert CamelCase attributes to snake_case
  ([`8a2d7c0`](https://github.com/Kitware/trame-vuetify/commit/8a2d7c0d3ddbd95bfbe0bd4194f5b5f012e9533e))

- **vue3**: Layout attr update
  ([`d7a2492`](https://github.com/Kitware/trame-vuetify/commit/d7a24928141722415f8c8e2e94a63e3336bae19d))


## v2.2.0 (2023-02-11)

### Features

- **vue3**: Add support for vue3
  ([`494bfa6`](https://github.com/Kitware/trame-vuetify/commit/494bfa6d207114d8297b1b4c11e937e100dc2db8))


## v2.1.0 (2023-01-21)

### Features

- **on_server_reload**: Pass server instance to ctrl.on_server_reload
  ([`e552141`](https://github.com/Kitware/trame-vuetify/commit/e552141b88e41be258a1edd3bc47aaf1f0a287f7))


## v2.0.2 (2022-10-03)

### Bug Fixes

- Expose dataframe_to_grid() in __all__
  ([`94675c6`](https://github.com/Kitware/trame-vuetify/commit/94675c6c0e5d9e8cc645219123e0616d81537f84))

This is used to convert a pandas dataframe to the `VDataTable()` grid format. This fix is necessary
  for one of the trame examples to work. This commit also adds the missing `Template` import in the
  `.header.py` file.

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

### Chores

- **semantic-release**: Bump version to latest
  ([`475e0a1`](https://github.com/Kitware/trame-vuetify/commit/475e0a188bc1e97ff2eddb6e9d09596131dbc94f))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

### Documentation

- **ci**: Add coverage and codecov upload
  ([`7d9b1b4`](https://github.com/Kitware/trame-vuetify/commit/7d9b1b4261221c0b93e262e9e4e207e4542caed1))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **contributing**: Add CONTRIBUTING.rst
  ([`808a0a4`](https://github.com/Kitware/trame-vuetify/commit/808a0a4c48e8fcfdf60cabac25af619b814d0f20))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **coverage**: Add .coveragerc
  ([`8b3cf3e`](https://github.com/Kitware/trame-vuetify/commit/8b3cf3e879c89288d4b237e9b26a340aba1f7fee))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **coverage**: Remove codecov PR comment
  ([`41127a6`](https://github.com/Kitware/trame-vuetify/commit/41127a6e07e81357cc2ee34d485155e1f4438764))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **readme**: Add CI badge
  ([`1a8c9b5`](https://github.com/Kitware/trame-vuetify/commit/1a8c9b5086b5923cd19dfcfe39693a263e19fc4b))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>


## v2.0.1 (2022-05-27)

### Bug Fixes

- Add semantic release to github actions
  ([`d7f0179`](https://github.com/Kitware/trame-vuetify/commit/d7f0179990168dafe7d51bafefa34455e32a86b9))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- Downgrade python semantic release for fix
  ([`823508e`](https://github.com/Kitware/trame-vuetify/commit/823508e1d13f542686d0fde6866e7784dcbafc39))

The newest version of semantic release has a bug that causes it to exit with errors. Downgrade to
  the latest version without the bug.

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- Use npm ci instead of npm install
  ([`4300a2d`](https://github.com/Kitware/trame-vuetify/commit/4300a2d4df15b025962c7e1380f52c2fd39693c9))

Signed-off-by: Patrick Avery <patrick.avery@kitware.com>

- **Template**: Expose under widgets.vuetify namespace
  ([`8b692b1`](https://github.com/Kitware/trame-vuetify/commit/8b692b1ed52a5003ab279ac429d0dc5596646f49))

### Documentation

- **api**: Add missing information
  ([`bbbb2d1`](https://github.com/Kitware/trame-vuetify/commit/bbbb2d14507bc6d5d5a73fc8ec0511be35e19bc3))
