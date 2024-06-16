import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from "url";

// const env = loadEnv('all', process.cwd());
const PROXY_URL = "http://atomic-hack-fast-api:5000" // env.VITE_PROXY_URL ?? 'http://127.0.0.1:5000';

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
			// rewrite: path => path.replace(/^\/api/, '')
		}
	  },
  },
})
