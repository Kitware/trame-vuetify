import "vuetify/styles";

import { createVuetify as _createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as labsComponents from "vuetify/labs/components";
import * as directives from "vuetify/directives";

function createVuetify(options) {
  return _createVuetify({
    components: {
      ...components,
      ...labsComponents,
    },
    directives,
    ...options,
  });
}

export default {
  createVuetify,
};
