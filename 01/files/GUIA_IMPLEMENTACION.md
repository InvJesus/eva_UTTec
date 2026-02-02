# 📚 GUÍA DE IMPLEMENTACIÓN EN GOOGLE APPS SCRIPT

## 📋 Descripción General
Esta guía te ayudará a implementar tu aplicación de Evaluación Digital en Google Apps Script para que pueda leer el archivo `.enc` desde Google Drive.

---

## 🚀 PASO 1: Preparar el Archivo .enc en Google Drive

### 1.1. Subir el archivo a Google Drive
1. Ve a [Google Drive](https://drive.google.com)
2. Sube tu archivo `admDB01.enc` a Google Drive
3. Haz clic derecho en el archivo → **Compartir**
4. En "Acceso general", selecciona **"Cualquier persona con el enlace"**
5. Copia el ID del archivo desde la URL:
   ```
   https://drive.google.com/file/d/1IBtatGgMNe9FDcT6hJWbDyDPgSo5KH2E/view?usp=sharing
                                   ↑ Este es el ID del archivo ↑
   ```

### 1.2. Verificar permisos
- Asegúrate de que el archivo sea accesible (al menos con permisos de "Viewer")
- Si quieres restringir el acceso, puedes compartirlo solo con usuarios específicos

---

## 🔧 PASO 2: Crear el Proyecto en Google Apps Script

### 2.1. Crear nuevo proyecto
1. Ve a [Google Apps Script](https://script.google.com)
2. Haz clic en **"Nuevo proyecto"**
3. Nómbralo: **"Evaluación Digital"**

### 2.2. Estructura de archivos que crearás:
```
Evaluación Digital/
├── Code.gs              (Archivo principal de servidor)
├── Index.html           (Archivo HTML principal)
├── Styles.html          (Estilos CSS)
├── Content.html         (Contenido HTML del body)
└── MainScript.html      (JavaScript principal)
```

---

## 📝 PASO 3: Crear los Archivos

### 3.1. Archivo Code.gs (Backend)

Crea un archivo llamado `Code.gs` con el siguiente contenido:

```javascript
/**
 * EVALUACIÓN DIGITAL - GOOGLE APPS SCRIPT
 * Archivo principal de servidor
 */

function doGet() {
  return HtmlService.createTemplateFromFile('Index')
    .evaluate()
    .setTitle('Evaluación Digital')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0');
}

function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

/**
 * Obtiene el contenido del archivo cifrado desde Google Drive
 * @param {string} fileId - ID del archivo en Google Drive
 * @returns {string} Contenido del archivo cifrado
 */
function getEncryptedFileContent(fileId) {
  try {
    Logger.log('📁 Obteniendo archivo con ID: ' + fileId);
    
    const file = DriveApp.getFileById(fileId);
    
    if (!file) {
      throw new Error('No se pudo encontrar el archivo con ID: ' + fileId);
    }
    
    Logger.log('✅ Archivo encontrado: ' + file.getName());
    
    const content = file.getBlob().getDataAsString('UTF-8');
    
    Logger.log('📦 Contenido leído: ' + content.length + ' caracteres');
    
    return content;
    
  } catch (error) {
    Logger.log('❌ Error al obtener archivo: ' + error.toString());
    throw new Error('Error al acceder al archivo de Google Drive: ' + error.message);
  }
}
```

---

### 3.2. Archivo Index.html (HTML Principal)

**IMPORTANTE:** En este archivo debes cambiar el `GOOGLE_DRIVE_FILE_ID` por el ID real de tu archivo:

Crea un archivo HTML llamado `Index.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evaluación Digital</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/qrious@4.0.2/dist/qrious.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    <?!= include('Styles'); ?>
</head>
<body class="bg-gradient-to-br from-blue-50 via-white to-purple-50 min-h-screen">
    <?!= include('Content'); ?>

    <script>
        // ========================================
        // CONFIGURACIÓN PARA GOOGLE APPS SCRIPT
        // ========================================
        
        // ⚠️ IMPORTANTE: Reemplaza este ID con el ID de tu archivo .enc en Google Drive
        const GOOGLE_DRIVE_FILE_ID = "1IBtatGgMNe9FDcT6hJWbDyDPgSo5KH2E";
        
        let EVALUATION_CONFIG = null;
        let currentEncFileName = 'admDB01.enc';

        // ========================================
        // FUNCIÓN PARA CARGAR DESDE GOOGLE DRIVE
        // ========================================
        
        async function loadJSONConfig(secretKey) {
            console.group('📡 CARGANDO DESDE GOOGLE DRIVE');
            
            if (!secretKey || secretKey.trim().length === 0) {
                throw new Error('Se requiere una clave para descifrar.');
            }
            
            try {
                console.log('⏳ Descargando archivo desde Drive...');
                
                // Llamar a la función del servidor
                const encryptedContent = await new Promise((resolve, reject) => {
                    google.script.run
                        .withSuccessHandler(resolve)
                        .withFailureHandler(reject)
                        .getEncryptedFileContent(GOOGLE_DRIVE_FILE_ID);
                });

                console.log('✅ Archivo descargado');
                console.log('🔓 Descifrando...');
                
                const decrypted = CryptoJS.AES.decrypt(encryptedContent, secretKey.trim());
                const decryptedText = decrypted.toString(CryptoJS.enc.Utf8);

                if (!decryptedText || decryptedText.length === 0) {
                    throw new Error('Clave incorrecta.');
                }

                console.log('✅ Descifrado exitoso');
                
                const config = JSON.parse(decryptedText);
                console.log('✅ JSON cargado');
                console.groupEnd();

                return config;

            } catch (error) {
                console.error('❌ Error:', error);
                console.groupEnd();
                
                if (error.message && error.message.includes('Clave incorrecta')) {
                    throw error;
                } else if (error.message && error.message.includes('JSON')) {
                    throw new Error('El archivo descifrado no es JSON válido. Verifica la clave.');
                } else {
                    throw new Error('Error al cargar: ' + error.message);
                }
            }
        }
        
        // El resto del código JavaScript original va aquí
        <?!= include('MainScript'); ?>
    </script>
</body>
</html>
```

---

### 3.3. Crear archivos modulares

Ahora necesitas dividir tu HTML original en archivos más pequeños:

#### **Styles.html**
Copia SOLO la sección `<style>...</style>` de tu archivo HTML original (desde línea 13 hasta aproximadamente línea 470)

#### **Content.html**
Copia SOLO el contenido del `<body>` sin incluir las etiquetas `<body>` y `</body>`, y SIN el script principal

#### **MainScript.html**
Copia TODO el JavaScript desde donde comienza el código de las variables globales hasta el final (aproximadamente desde línea 1112 hasta línea 4406)

---

## 🔑 PASO 4: Configuración del ID del Archivo

En el archivo `Index.html`, cambia esta línea:

```javascript
const GOOGLE_DRIVE_FILE_ID = "1IBtatGgMNe9FDcT6hJWbDyDPgSo5KH2E";
```

Por el ID real de tu archivo que obtuviste en el Paso 1.1

---

## 🚀 PASO 5: Publicar la Aplicación Web

### 5.1. Implementar como Web App
1. En el editor de Apps Script, haz clic en **"Implementar"** → **"Nueva implementación"**
2. Selecciona el tipo: **"Aplicación web"**
3. Configura:
   - **Descripción:** "Evaluación Digital v1.0"
   - **Ejecutar como:** "Yo (tu email)"
   - **Quién tiene acceso:** "Cualquier usuario" (o según tus necesidades)
4. Haz clic en **"Implementar"**
5. **Copia la URL de la aplicación web**

### 5.2. Permisos
- La primera vez que ejecutes, Google pedirá permisos para acceder a Drive
- Haz clic en **"Revisar permisos"**
- Selecciona tu cuenta
- Haz clic en **"Permitir"**

---

## ✅ PASO 6: Probar la Aplicación

1. Abre la URL de tu Web App en el navegador
2. Verás la pantalla de autenticación
3. Ingresa la clave de descifrado
4. Si todo está configurado correctamente:
   - El archivo `.enc` se descargará desde Google Drive
   - Se descifrará con tu clave
   - La evaluación cargará normalmente

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error: "No se pudo encontrar el archivo"
- ✅ Verifica que el ID del archivo sea correcto
- ✅ Confirma que el archivo esté en tu Drive
- ✅ Asegúrate de que la app tenga permisos para acceder a Drive

### Error: "Clave incorrecta"
- ✅ Verifica que estés usando la misma clave con la que cifraste el archivo
- ✅ Asegúrate de no tener espacios extras en la clave

### Error: "Access denied"
- ✅ Vuelve a dar permisos a la aplicación
- ✅ En Apps Script: **Ejecutar** → **Revisar permisos**

### La aplicación no carga
- ✅ Verifica que hayas copiado TODO el código correctamente
- ✅ Revisa la consola del navegador (F12) para ver errores
- ✅ En Apps Script, revisa los **Registros de ejecución**

---

## 📊 VENTAJAS DE USAR GOOGLE APPS SCRIPT

✅ **Hosting gratuito** de Google
✅ **Integración nativa** con Google Drive
✅ **Sin necesidad de servidor** propio
✅ **Escalable** automáticamente
✅ **Acceso controlado** por permisos de Google
✅ **HTTPS** incluido por defecto

---

## 🔒 SEGURIDAD

- El archivo `.enc` permanece cifrado en Google Drive
- Solo usuarios con la clave correcta pueden descifrar
- Puedes controlar quién tiene acceso a la Web App
- Los registros de Google Apps Script te muestran quién accede

---

## 📞 NOTAS ADICIONALES

- **Límites de Google Apps Script:**
  - 6 minutos de tiempo de ejecución por solicitud
  - Llamadas diarias limitadas según tu cuenta (gratuita o de pago)
  
- **Actualizaciones:**
  - Para actualizar el archivo `.enc`, simplemente reemplázalo en Drive
  - No necesitas cambiar el código si mantienes el mismo ID de archivo

---

## 🎯 RESUMEN DE CAMBIOS PRINCIPALES

### Cambio 1: Carga de archivo
**ANTES (URL directa):**
```javascript
const response = await fetch(url);
```

**AHORA (Google Drive):**
```javascript
const content = await google.script.run.getEncryptedFileContent(fileId);
```

### Cambio 2: Configuración
**ANTES:**
```javascript
const ENCRYPTED_CONFIG_URL_B64 = "aHR0cHM6Ly9...";
```

**AHORA:**
```javascript
const GOOGLE_DRIVE_FILE_ID = "1IBtatGgMNe9FDcT6hJWbDyDPgSo5KH2E";
```

---

¿Necesitas ayuda adicional? Revisa los logs en Google Apps Script:
**Ver** → **Registros de ejecución**
