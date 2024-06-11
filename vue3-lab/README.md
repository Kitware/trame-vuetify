## Vuetify Lab

This library aims to expose vuetify lab

## Update the vuetify version to bundle

```bash
npm i
npm run build
```

## Material Design icons

```bash
export SRC_URL=https://cdn.jsdelivr.net/npm
export DST_PATH=../trame_vuetify/module/vue3-lab-serve

mkdir -p $DST_PATH/{fonts,css}
curl $SRC_URL/@mdi/font@7.x/css/materialdesignicons.min.css -Lo $DST_PATH/css/mdi.css
curl $SRC_URL/@mdi/font@7.x/fonts/materialdesignicons-webfont.woff2 -Lo $DST_PATH/fonts/materialdesignicons-webfont.woff2
```
