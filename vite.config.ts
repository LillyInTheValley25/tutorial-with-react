import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import "react";
import "react-dom";
import deno from "@deno/vite-plugin";

export default defineConfig({
  root: ".",
  build: {
    outDir: "dist",
    emptyOutDir: true,
  },
  server: {
    port: 3000,
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
    },
  },
  plugins: [react(), deno()],
  optimizeDeps: {
    include: ["react/jsx-runtime"],
  },
});
