import { SYMLINK_SRC, SYMLINK_DST } from '../consts';
import type { AstroIntegration } from 'astro';
import fs from 'fs';
import path from 'path';
import os from 'os';

export const symlinkIntegration = (): AstroIntegration => {
  const sourceDir = path.resolve(process.cwd(), SYMLINK_SRC);
  const targetDir = path.resolve(process.cwd(), SYMLINK_DST);

  return {
    name: 'astro-symlink-files',
    hooks: {
      'astro:build:start': async () => {
        try {
          if (!fs.existsSync(targetDir)) {
            fs.mkdirSync(targetDir, { recursive: true });
          }

          const files = fs.readdirSync(sourceDir);
          for (const file of files) {
            const sourceFile = path.join(sourceDir, file);
            const targetLink = path.join(targetDir, file);

            if (!fs.existsSync(sourceFile)) {
              continue;
            }

            const stats = fs.statSync(sourceFile);
            if (!stats.isDirectory()) {
              continue;
            }

            if (fs.existsSync(targetLink)) {
              continue;
            }

            try {
              const linkType = os.platform() === 'win32' ? 'file' : 'file';
              fs.symlinkSync(sourceFile, targetLink, linkType);
            } catch (err: any) {
              console.error(
                `[symlinkIntegration] Failed to symlink: ${targetLink} -> ${sourceFile}`
              );
              console.error(err.message);
            }
          }
        } catch (error: any) {
          console.error(`[symlinkIntegration] Error: ${error.message}`);
        }
      },
    },
  };
};

export default symlinkIntegration;