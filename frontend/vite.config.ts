import fs from 'node:fs'
import path from 'node:path'
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

/** Prefer appwrite.config.json (from `appwrite pull functions`) — it has the real cloud $id. */
function readFunctionIdFromRepo(repoRoot: string): string | undefined {
  for (const file of ['appwrite.config.json', 'appwrite.json']) {
    const full = path.join(repoRoot, file)
    if (!fs.existsSync(full)) continue
    try {
      const data = JSON.parse(fs.readFileSync(full, 'utf8')) as {
        functions?: Array<{ $id?: string; id?: string; name?: string }>
      }
      const fns = data.functions
      if (!Array.isArray(fns) || fns.length === 0) continue
      const byName = fns.find((f) =>
        (f.name ?? '').toLowerCase().includes('predic')
      )
      const fn = byName ?? fns[0]
      const id = fn?.$id ?? fn?.id
      if (typeof id === 'string' && id.length > 0) return id
    } catch {
      continue
    }
  }
  return undefined
}

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const frontendRoot = __dirname
  const repoRoot = path.join(frontendRoot, '..')
  const env = loadEnv(mode, frontendRoot, '')
  const fromRepo = readFunctionIdFromRepo(repoRoot)
  const functionId =
    env.VITE_APPWRITE_FUNCTION_ID ||
    env.VITE_FUNCTION_ID ||
    fromRepo ||
    'predict'

  return {
    plugins: [react()],
    base: './',
    define: {
      'import.meta.env.VITE_APPWRITE_FUNCTION_ID': JSON.stringify(functionId),
    },
  }
})
