# AutoPatchAI - Codex Context

## Project

- Path: `CyberSecurity/AutoPatchAI`
- Type: Web/TypeScript project
- Framework: inspect `package.json` before assuming Next.js or React.
- Package manager: `pnpm` unless repo scripts prove otherwise.

## Workflows

- Inspect `package.json` scripts before running build, lint, test, or dev commands.
- Keep environment variables server-side unless intentionally public with `NEXT_PUBLIC_`.
- Do not commit `.next/`, `dist/`, local env files, generated caches, or deployment secrets.
- For visible UI changes, verify with browser/screenshot checks when feasible.

## Codex Rules

- Global context comes from `~/.codex/AGENTS.md`.
- Verify actual files before claiming repo state, config, counts, or duplicates.
- Do not commit secrets, `.env*`, local config, signing material, generated caches, sessions, or auth files.
- Stage files by explicit path only.
- Prefer focused changes and match existing project patterns.
- Read `CodexConfig/rules/web.md` before substantial web/TypeScript work.

