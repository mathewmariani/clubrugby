// @ts-check
import { defineConfig } from 'astro/config';

import vue from '@astrojs/vue';
import path from 'path';

// https://astro.build/config
export default defineConfig({
  site: 'https://clubrugby.ca',
  integrations: [vue()],
  vite: {
      resolve: {
          preserveSymlinks: true,
          alias: {
            '@': path.resolve('./src'),
          },
      },
  },
});