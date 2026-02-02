# 🚀 Evaluación Digital - Google Apps Script

## ⚡ Inicio Rápido

### 1️⃣ Subir archivos a Google Apps Script

1. Ve a [script.google.com](https://script.google.com)
2. Crea un nuevo proyecto: **"Evaluación Digital"**
3. Sube estos archivos:
   - `Code.gs`
   - `Index.html`
   - `Styles.html`
   - `Content.html`
   - `MainScript.html`

### 2️⃣ Configurar el ID de Google Drive

En el archivo `Index.html`, línea 27, cambia:

```javascript
const GOOGLE_DRIVE_FILE_ID = "TU_ID_AQUI";
```

**¿Cómo obtener el ID?**
- Abre tu archivo `.enc` en Google Drive
- Copia la URL: `https://drive.google.com/file/d/1IBtatGgMNe9FDcT6hJWbDyDPgSo5KH2E/view`
- El ID es: `1IBtatGgMNe9FDcT6hJWbDyDPgSo5KH2E`

### 3️⃣ Publicar

1. Haz clic en **"Implementar"** → **"Nueva implementación"**
2. Tipo: **"Aplicación web"**
3. Ejecutar como: **"Yo"**
4. Acceso: **"Cualquiera"**
5. Copia la URL generada

### 4️⃣ Dar permisos

La primera vez:
1. Te pedirá permisos para Google Drive
2. Haz clic en **"Revisar permisos"**
3. Selecciona tu cuenta
4. Haz clic en **"Permitir"**

## ✅ ¡Listo!

Abre la URL de tu Web App y disfruta de tu evaluación digital funcionando desde Google Drive.

---

## 📁 Estructura de Archivos

```
Evaluación Digital/
├── Code.gs              # Backend (servidor)
├── Index.html           # HTML principal + Config
├── Styles.html          # Estilos CSS
├── Content.html         # Contenido HTML
└── MainScript.html      # JavaScript principal
```

---

## 🔧 Cambios Principales

| Aspecto | Antes | Ahora |
|---------|-------|-------|
| **Fuente** | URL directa (GitHub) | Google Drive |
| **Método** | `fetch()` | `google.script.run` |
| **Config** | URL en Base64 | ID de archivo |

---

## 🐛 Problemas Comunes

### "No se encontró el archivo"
→ Verifica el ID del archivo en `Index.html`

### "Clave incorrecta"
→ Usa la misma clave con la que cifraste el archivo

### "Access denied"
→ Revisa los permisos en Google Apps Script

---

## 📚 Documentación Completa

Para más detalles, consulta: `GUIA_IMPLEMENTACION.md`

---

## 💡 Ventajas

✅ Hosting gratuito de Google
✅ Sin servidor propio
✅ Integración con Drive
✅ HTTPS incluido
✅ Escalable automáticamente

---

**¿Necesitas ayuda?**
Revisa los logs: Apps Script → **Ver** → **Registros de ejecución**
