#!/usr/bin/env node
/**
 * DG AUDIOSOUND — GENERADOR DE BUNDLE DESDE ATOMIC DESIGN
 * Lee `styles/main.css` y `scripts/main.js`, resuelve todos los `@import` / `import`
 * de las carpetas atómicas, y genera `styles/bundle.min.css` y `scripts/bundle.min.js`
 * para producción (evitando el límite HTTP 429 de Hostinger CDN).
 *
 * Uso:
 *   npm run build
 *   (o directamente: node scripts/build-bundle.mjs)
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT_DIR = path.resolve(__dirname, '..');
const STYLES_DIR = path.join(ROOT_DIR, 'styles');
const SCRIPTS_DIR = path.join(ROOT_DIR, 'scripts');

function buildCssBundle() {
    const mainCssPath = path.join(STYLES_DIR, 'main.css');
    const mainCssContent = fs.readFileSync(mainCssPath, 'utf8');

    const importRegex = /@import\s+['"](.+?)['"]\s*;/g;
    const chunks = [
        '/* ==========================================================================',
        '   DG AUDIOSOUND — BUNDLE DE PRODUCCIÓN (GENERADO AUTOMÁTICAMENTE)',
        '   Unifica las capas de Atomic Design (00-tokens a 04-pages) en una sola',
        '   respuesta HTTP para eliminar el bloqueo HTTP 429 (Too Many Requests) en CDN.',
        '   Para editar estilos, modifica los archivos en styles/00-tokens/ .. styles/04-pages/.',
        '   ========================================================================== */\n'
    ];

    let match;
    let count = 0;
    while ((match = importRegex.exec(mainCssContent)) !== null) {
        const cleanRelPath = match[1].split('?')[0];
        const absFilePath = path.resolve(STYLES_DIR, cleanRelPath);
        let fileCss = fs.readFileSync(absFilePath, 'utf8');

        // Ajustar rutas relativas de subcarpetas (ej. styles/03-organisms/hero.css -> styles/bundle.min.css)
        fileCss = fileCss.replace(/url\((['"]?)\.\.\/\.\.\/assets\//g, 'url($1../assets/');

        chunks.push(`/* --- SOURCE: ${cleanRelPath} --- */`);
        chunks.push(fileCss.trim());
        chunks.push('');
        count++;
    }

    const outPath = path.join(STYLES_DIR, 'bundle.min.css');
    fs.writeFileSync(outPath, chunks.join('\n'), 'utf8');
    console.log(`✅ CSS Bundle generado: styles/bundle.min.css (${count} módulos atómicos integrados)`);
}

function buildJsBundle() {
    const mainJsPath = path.join(SCRIPTS_DIR, 'main.js');
    const mainJsContent = fs.readFileSync(mainJsPath, 'utf8');

    const importRegex = /^import\s+\{[^}]+\}\s+from\s+['"](.+?)['"]\s*;?\s*$/gm;
    const chunks = [
        '/**',
        ' * DG AUDIOSOUND — BUNDLE DE PRODUCCIÓN (GENERADO AUTOMÁTICAMENTE)',
        ' * Archivo compilado a partir de scripts/main.js y sus módulos atómicos.',
        ' * Para editar el código fuente, modifica los archivos en scripts/organisms/ y scripts/molecules/.',
        ' */\n'
    ];

    let match;
    let count = 0;
    while ((match = importRegex.exec(mainJsContent)) !== null) {
        const cleanRelPath = match[1].split('?')[0];
        const absFilePath = path.resolve(SCRIPTS_DIR, cleanRelPath);
        const modContent = fs.readFileSync(absFilePath, 'utf8');
        chunks.push(`/* --- SOURCE: ${cleanRelPath} --- */`);
        chunks.push(modContent.trim());
        chunks.push('');
        count++;
    }

    const bodyWithoutImports = mainJsContent.replace(importRegex, '').trim();
    chunks.push('/* --- ORCHESTRATOR: main.js --- */');
    chunks.push(bodyWithoutImports);
    chunks.push('');

    const outPath = path.join(SCRIPTS_DIR, 'bundle.min.js');
    fs.writeFileSync(outPath, chunks.join('\n'), 'utf8');
    console.log(`✅ JS Bundle generado: scripts/bundle.min.js (${count} módulos atómicos integrados)`);
}

buildCssBundle();
buildJsBundle();
