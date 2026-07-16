module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ['plugin:vue/essential', 'eslint:recommended', 'plugin:prettier/recommended'],
  parserOptions: {
    parser: '@babel/eslint-parser',
  },
  rules: {
    'import/extensions': 0,
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
  },
};
