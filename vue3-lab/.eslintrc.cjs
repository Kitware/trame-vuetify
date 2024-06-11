/* eslint-env node */
require("@rushstack/eslint-patch/modern-module-resolution");

module.exports = {
  root: true,
  extends: [
    "eslint:recommended",
    "@vue/eslint-config-prettier",
  ],
  env : {
    browser : true,
    es6 : true,
  },
  rules : {
    "no-unused-vars" : 2,
    "no-undef" : 2
  },
  parserOptions: {
    sourceType: "module",
    ecmaVersion: "latest",
  },
};
