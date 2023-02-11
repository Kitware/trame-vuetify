import '@mdi/font/css/materialdesignicons.css';
import 'vuetify/dist/vuetify.min.css';
import 'typeface-roboto';

import Vuetify from 'vuetify';

const OPTIONS = {};

export default {
  async install(Vue, options = {}) {
    // Get our own custom vuetify
    Vue.use(Vuetify);

    // Configure the root view option
    OPTIONS.vuetify = new Vuetify(options);
  },
  getOptions() {
    return OPTIONS;
  },
};
