// @ts-check
import { defineConfig } from 'astro/config';
import { symlinkIntegration } from './src/integrations/symlink';

import vue from '@astrojs/vue';
import path from 'path';

// https://astro.build/config
export default defineConfig({
  site: 'https://clubrugby.ca',
  integrations: [vue(), symlinkIntegration()],
  vite: {
      resolve: {
          preserveSymlinks: true,
          alias: {
            '@': path.resolve('./src'),
          },
      },
  },
});