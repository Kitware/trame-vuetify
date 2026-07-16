export default {
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "vuetifylab",
      formats: ["umd"],
      fileName: "trame-vuetify-lab",
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
    outDir: "../../trame_vuetify/module/v3-lab-serve/",
    assetsDir: ".",
  },
};
