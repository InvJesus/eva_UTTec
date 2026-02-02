# 🏗️ ARQUITECTURA DEL SISTEMA

## 📊 Flujo de Datos

```
┌─────────────────────────────────────────────────────────────────┐
│                         USUARIO                                  │
│                    (Navegador Web)                               │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ 1. Accede a la Web App
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                  GOOGLE APPS SCRIPT                              │
│                  (Servidor Backend)                              │
│                                                                  │
│  ┌──────────────────────────────────────────────────┐          │
│  │  Code.gs                                          │          │
│  │  • doGet()          → Sirve la aplicación        │          │
│  │  • include()        → Incluye módulos HTML       │          │
│  │  • getEncrypted...()→ Lee archivo de Drive       │          │
│  └──────────────────────────────────────────────────┘          │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ 2. Renderiza HTML
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    APLICACIÓN WEB                                │
│                  (Frontend - HTML/JS)                            │
│                                                                  │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐       │
│  │ Index.html  │  │ Styles.html  │  │ Content.html    │       │
│  │ • Config    │  │ • CSS        │  │ • HTML Body     │       │
│  │ • Loader    │  │ • Animations │  │ • Formularios   │       │
│  └─────────────┘  └──────────────┘  └─────────────────┘       │
│                                                                  │
│  ┌────────────────────────────────────────────────────┐        │
│  │ MainScript.html                                     │        │
│  │ • Lógica de evaluación                             │        │
│  │ • Manejo de secciones                              │        │
│  │ • Generación de PDFs                               │        │
│  │ • Sistema de puntos                                │        │
│  └────────────────────────────────────────────────────┘        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ 3. Usuario ingresa clave
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              AUTENTICACIÓN Y DESCIFRADO                          │
│                                                                  │
│  Usuario ingresa clave → loadJSONConfig(clave)                  │
│                             │                                    │
│                             │ 4. Solicita archivo                │
│                             ▼                                    │
│              google.script.run.getEncryptedFileContent(ID)      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ 5. Busca archivo en Drive
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GOOGLE DRIVE                                 │
│                                                                  │
│  ┌──────────────────────────────────────┐                      │
│  │  admDB01.enc                          │                      │
│  │  • Archivo cifrado con AES-256       │                      │
│  │  • Contiene JSON de configuración    │                      │
│  │  • ID: 1IBtatGgMNe9FDcT6hJWbDyDPg... │                      │
│  └──────────────────────────────────────┘                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ 6. Devuelve contenido cifrado
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                 DESCIFRADO EN EL CLIENTE                         │
│                                                                  │
│  CryptoJS.AES.decrypt(contenidoCifrado, clave)                  │
│                             │                                    │
│                             │ 7. JSON descifrado                 │
│                             ▼                                    │
│              EVALUATION_CONFIG = JSON.parse(texto)              │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ 8. Carga exitosa
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    EVALUACIÓN ACTIVA                             │
│                                                                  │
│  • Sección 1: Opción Múltiple                                   │
│  • Sección 2: Relación de Columnas                              │
│  • Sección 3: Ahorcado                                          │
│  • Sistema de puntos                                            │
│  • Generación de reportes PDF                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Comparación: Antes vs Ahora

### ANTES (GitHub Pages)
```
Usuario → GitHub Pages (HTML) → fetch(url.enc) → Descifrar → Evaluar
          └─ URL directa del archivo .enc
```

### AHORA (Google Apps Script)
```
Usuario → Apps Script → getFileContent(ID) → Google Drive → Archivo .enc
                    ↓
              Descifrar con clave → Evaluar
```

---

## 🔐 Seguridad en Capas

```
Capa 1: GOOGLE DRIVE
├─ Control de acceso por usuario
├─ Permisos de compartición
└─ Historial de versiones

Capa 2: CIFRADO AES-256
├─ Archivo .enc cifrado
├─ Clave requerida para descifrar
└─ Sin clave = sin acceso a datos

Capa 3: APPS SCRIPT
├─ Autenticación de Google
├─ Permisos de ejecución
└─ Logs de acceso

Capa 4: APLICACIÓN
├─ Validación de datos
├─ Protección contra inspección
└─ Control de intentos
```

---

## 📁 Responsabilidad de Cada Archivo

### **Code.gs** (Backend)
```javascript
Responsabilidades:
✓ Servir la aplicación web
✓ Conectar con Google Drive
✓ Leer archivo .enc
✓ Manejar errores de Drive
```

### **Index.html** (Orquestador)
```javascript
Responsabilidades:
✓ Configurar ID del archivo
✓ Incluir módulos (Styles, Content, Script)
✓ Gestionar carga desde Drive
✓ Descifrar contenido
✓ Inicializar aplicación
```

### **Styles.html** (Presentación)
```css
Responsabilidades:
✓ Estilos CSS personalizados
✓ Animaciones
✓ Diseño responsive
✓ Temas visuales
```

### **Content.html** (Estructura)
```html
Responsabilidades:
✓ Estructura HTML del body
✓ Formularios
✓ Secciones de evaluación
✓ Modales y pantallas
```

### **MainScript.html** (Lógica)
```javascript
Responsabilidades:
✓ Lógica de evaluación
✓ Manejo de preguntas
✓ Sistema de puntos
✓ Generación de PDFs
✓ Cronómetro
✓ Validaciones
```

---

## 🎯 Puntos Clave de Integración

### 1. Comunicación Cliente-Servidor
```javascript
// Cliente solicita archivo
google.script.run
  .withSuccessHandler(procesarRespuesta)
  .withFailureHandler(manejarError)
  .getEncryptedFileContent(FILE_ID);
```

### 2. Inclusión de Módulos
```html
<?!= include('NombreDelArchivo'); ?>
```

### 3. Variables de Configuración
```javascript
const GOOGLE_DRIVE_FILE_ID = "TU_ID_AQUI";
```

---

## 🚀 Flujo de Despliegue

```
1. DESARROLLO LOCAL
   ├─ Editar archivos .html y .gs
   └─ Probar lógica localmente

2. SUBIR A APPS SCRIPT
   ├─ Crear proyecto en script.google.com
   ├─ Copiar contenido de cada archivo
   └─ Configurar ID del archivo Drive

3. CONFIGURAR PERMISOS
   ├─ Autorizar acceso a Drive
   └─ Definir quién puede ejecutar

4. IMPLEMENTAR WEB APP
   ├─ Implementar → Nueva implementación
   ├─ Tipo: Aplicación Web
   └─ Obtener URL pública

5. COMPARTIR
   ├─ Distribuir URL de la Web App
   └─ Proporcionar clave de descifrado
```

---

## 💡 Ventajas de Esta Arquitectura

✅ **Modular**: Fácil mantenimiento de cada componente
✅ **Seguro**: Múltiples capas de seguridad
✅ **Escalable**: Google maneja la infraestructura
✅ **Gratuito**: Sin costos de hosting
✅ **Confiable**: 99.9% de uptime de Google
✅ **Integrado**: Nativo con ecosistema Google

---

## 🔄 Actualizaciones

Para actualizar:
1. **Archivo .enc**: Reemplazar en Drive (mismo ID)
2. **Código**: Editar en Apps Script → Nueva implementación
3. **Configuración**: Cambiar variables y re-implementar

---

## 📊 Métricas y Monitoreo

Disponibles en Google Apps Script:
- **Registros de ejecución**: Ver errores y logs
- **Uso de cuotas**: Monitorear límites
- **Tiempo de ejecución**: Optimizar performance
- **Errores**: Detectar problemas

---

Esta arquitectura combina lo mejor de:
- **Google Drive** (almacenamiento)
- **Apps Script** (backend)
- **Web estática** (frontend)
- **Cifrado AES** (seguridad)

Para crear una solución robusta, mantenible y segura. 🎉
