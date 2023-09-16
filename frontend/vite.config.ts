import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/core/css/global/index.scss";`
      }
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      //'@': path.resolve(__dirname, 'src'),
    }
  }
})
