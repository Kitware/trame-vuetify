import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Trame Vuetify",
  description: "Examples on how to use Vuetify with trame ",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/examples/' }
    ],

    sidebar: [
      {
        text: 'Trame',
        items: [
          { text: 'What is it ?', link: '/examples/trame' },
        ]
      },
      {
        text: 'Vuetify',
        items: [
          { text: 'Getting started', link: '/examples/' },
          { text: 'Layout', link: '/examples/ui' },
          { text: 'Login', link: '/examples/login' },
        ]
      },
      {
        text: 'Support',
        items: [
          { text: 'Need help ?', link: '/examples/support' },
        ]
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Kitware/trame-vuetify' }
    ]
  }
})
