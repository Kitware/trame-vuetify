# trame-vuetify

This directory capture the steps to enable Vuetify 3.x into trame-vuewtify.

## Environment variables

```bash
export SRC_URL=https://cdn.jsdelivr.net/npm
export DST_PATH=../trame_vuetify/module/vue3-serve
export VUETIFY=vuetify@3.7.6

mkdir -p $DST_PATH/{fonts,css}
```

## Update the vuetify version to bundle

```bash
curl $SRC_URL/$VUETIFY/dist/vuetify.min.css -Lo $DST_PATH/vuetify3.css
curl $SRC_URL/$VUETIFY/dist/vuetify.min.js -Lo $DST_PATH/vuetify3.js
```

## Material Design icons

```bash
curl $SRC_URL/@mdi/font@7.x/css/materialdesignicons.min.css -Lo $DST_PATH/css/mdi.css
curl $SRC_URL/@mdi/font@7.x/fonts/materialdesignicons-webfont.woff2 -Lo $DST_PATH/fonts/materialdesignicons-webfont.woff2
```

## Update Python definition

```bash
curl  $SRC_URL/$VUETIFY/dist/json/web-types.json -Lo web-types.json
./generate_python.py
```