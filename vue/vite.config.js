import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from "url";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: [
      { find: '@', replacement: fileURLToPath(new URL('./src', import.meta.url)) }
    ],
  },
  server: {
	proxy: {
		"/api": {
			target: PROXY_URL,
			changeOrigin: true,
			secure: false,
			rewrite: path => path.replace(/^\/api/, '')
		}
	  },
  },
})
