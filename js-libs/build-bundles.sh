#!/bin/bash

export SRC_URL=https://cdn.jsdelivr.net/npm

# Vuetify 3
export V3_VERSION=vuetify@3.12.10
export V3_DST_PATH=../trame_vuetify/module/v3-serve
export V3_LAB_DST_PATH=../trame_vuetify/module/v3-lab-serve
mkdir -p $V3_DST_PATH/{fonts,css}
mkdir -p $V3_LAB_DST_PATH/{fonts,css}

# Make and download Vuetify 3
curl "$SRC_URL/$V3_VERSION/dist/vuetify.min.css" -Lo "$V3_DST_PATH/vuetify3.css"
curl "$SRC_URL/$V3_VERSION/dist/vuetify.min.js" -Lo "$V3_DST_PATH/vuetify3.js"

# Prepare icons + fonts for regular Vuetify 3
curl "$SRC_URL/@mdi/font@7.x/css/materialdesignicons.min.css" -Lo "$V3_DST_PATH/css/mdi.css"
curl "$SRC_URL/@mdi/font@7.x/fonts/materialdesignicons-webfont.woff2" -Lo "$V3_DST_PATH/fonts/materialdesignicons-webfont.woff2"

# Prepare icons + fonts for Vuetify 3 Lab
curl "$SRC_URL/@mdi/font@7.x/css/materialdesignicons.min.css" -Lo "$V3_LAB_DST_PATH/css/mdi.css"
curl "$SRC_URL/@mdi/font@7.x/fonts/materialdesignicons-webfont.woff2" -Lo "$V3_LAB_DST_PATH/fonts/materialdesignicons-webfont.woff2"

# Re-generate the Python bindings
curl "$SRC_URL/$V3_VERSION/dist/json/web-types.json" -Lo ./v3/web-types.json
./v3/generate_python.py

# Vuetify 4
export V4_VERSION=vuetify@4.2.1
export V4_DST_PATH=../trame_vuetify/module/v4-serve
export V4_LAB_DST_PATH=../trame_vuetify/module/v4-lab-serve
mkdir -p $V4_DST_PATH/{fonts,css}
mkdir -p $V4_LAB_DST_PATH/{fonts,css}

# Make and download Vuetify 4
curl "$SRC_URL/$V4_VERSION/dist/vuetify.min.css" -Lo "$V4_DST_PATH/vuetify4.css"
curl "$SRC_URL/$V4_VERSION/dist/vuetify.min.js" -Lo "$V4_DST_PATH/vuetify4.js"

# Prepare icons + fonts for regular Vuetify 4
curl "$SRC_URL/@mdi/font@7.x/css/materialdesignicons.min.css" -Lo "$V4_DST_PATH/css/mdi.css"
curl "$SRC_URL/@mdi/font@7.x/fonts/materialdesignicons-webfont.woff2" -Lo "$V4_DST_PATH/fonts/materialdesignicons-webfont.woff2"

# Prepare icons + fonts for Vuetify 4 Lab
curl "$SRC_URL/@mdi/font@7.x/css/materialdesignicons.min.css" -Lo "$V4_LAB_DST_PATH/css/mdi.css"
curl "$SRC_URL/@mdi/font@7.x/fonts/materialdesignicons-webfont.woff2" -Lo "$V4_LAB_DST_PATH/fonts/materialdesignicons-webfont.woff2"

# Re-generate the Python bindings
curl "$SRC_URL/$V4_VERSION/dist/json/web-types.json" -Lo ./v4/web-types.json
./v4/generate_python.py
