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
    outDir: "../../trame_vuetify/module/v4-lab-serve/",
    assetsDir: ".",
  },
  define: {
    // Needed from migrating Vite v4 -> v8, process is no longer globally injected at runtime
    "process.env.NODE_ENV": JSON.stringify(
      process.env.NODE_EV ?? "development",
    ),
  },
};
