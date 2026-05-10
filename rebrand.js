const fs = require('fs')
const path = require('path')

const BRANDING = {
  names: [
    { old: 'Black Tube', new: 'Black Tube' },
    { old: 'Free Tube', new: 'Black Tube' },
    { old: 'freetube', new: 'blacktube' }
  ]
}

function replaceInFile(filePath) {
  try {
    let content = fs.readFileSync(filePath, 'utf8')
    let original = content

    for (const { old, new: newName } of BRANDING.names) {
      const regex = new RegExp(old, 'g')
      content = content.replace(regex, newName)
    }

    if (content !== original) {
      fs.writeFileSync(filePath, content, 'utf8')
      console.log(`✅ Actualizado: ${filePath}`)
    }
  } catch (err) {
    console.error(`❌ Error en ${filePath}:`, err.message)
  }
}

function processDirectory(dir) {
  if (!fs.existsSync(dir)) return

  const files = fs.readdirSync(dir)
  for (const file of files) {
    const fullPath = path.join(dir, file)
    const stat = fs.statSync(fullPath)

    if (stat.isDirectory()) {
      // Ignorar carpetas generadas
      if (!['node_modules', '.git', 'dist', 'build', 'out'].includes(file)) {
        processDirectory(fullPath)
      }
    } else {
      // Solo editar archivos relevantes
      if (/\.(js|vue|json|html|css|scss|md|yml|ejs)$/.test(file)) {
        if (!file.includes('lock')) {
          replaceInFile(fullPath)
        }
      }
    }
  }
}

console.log('🚀 Iniciando refactorización de marca a Black Tube...')

// 1. Reemplazar texto en código fuente y traducciones
processDirectory(path.join(__dirname, 'src'))
processDirectory(path.join(__dirname, 'static', 'locales'))

// 2. Reemplazar en archivos raíz
const rootFiles = ['package.json', 'README.md', 'electron-builder.yml', '_scripts/webpack.renderer.config.js']
for (const file of rootFiles) {
  const fullPath = path.join(__dirname, file)
  if (fs.existsSync(fullPath)) replaceInFile(fullPath)
}

console.log('✨ Rebranding completado exitosamente.')
