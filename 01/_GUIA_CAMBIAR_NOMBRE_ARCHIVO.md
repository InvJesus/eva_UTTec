# Guía: Cómo Cambiar el Nombre del Archivo Encriptado

## Pasos para Cambiar el Nombre del Archivo

### Paso 1: Cifrar con el Nuevo Nombre

1. Abre `cifrar_json.html` en tu navegador
2. En el campo **"Nombre del archivo cifrado"**, escribe el nuevo nombre (ej: `evaluacion_final.enc`)
3. Pega tu JSON y ingresa la clave secreta
4. Haz clic en "Cifrar JSON"
5. Descarga el archivo con el nuevo nombre

### Paso 2: Subir el Archivo al Servidor

1. Sube el archivo con el nuevo nombre a tu servidor (GitHub Pages, etc.)
2. Anota la URL completa del archivo (ej: `https://tu-usuario.github.io/repo/evaluacion_final.enc`)

### Paso 3: Actualizar la URL en el Código

1. Abre `admDB01.html`
2. Busca la línea que contiene:
   ```javascript
   const ENCRYPTED_CONFIG_URL_B64 = "aHR0cHM6Ly9pbnZqZXN1cy5naXRodWIuaW8vZXZhX1VUVGVjLzAxL2FkbURCMDEuZW5j";
   ```

3. **Codifica tu nueva URL en Base64** usando una de estas opciones:

   **Opción A: Usando la Consola del Navegador**
   - Abre la consola del navegador (F12)
   - Escribe: `btoa("https://tu-usuario.github.io/repo/evaluacion_final.enc")`
   - Copia el resultado

   **Opción B: Usando PowerShell (Windows)**
   ```powershell
   [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("https://tu-usuario.github.io/repo/evaluacion_final.enc"))
   ```

   **Opción C: Usando una herramienta online**
   - Ve a https://www.base64encode.org/
   - Pega tu URL
   - Copia el resultado codificado

4. Reemplaza el valor en `ENCRYPTED_CONFIG_URL_B64` con tu nueva URL codificada:
   ```javascript
   const ENCRYPTED_CONFIG_URL_B64 = "TU_NUEVA_URL_CODIFICADA_AQUI";
   ```

### Ejemplo Completo

**Si tu nueva URL es:**
```
https://invjesus.github.io/eva_UTTec/01/evaluacion_final.enc
```

**La URL codificada en Base64 sería:**
```
aHR0cHM6Ly9pbnZqZXN1cy5naXRodWIuaW8vZXZhX1VUVGVjLzAxL2V2YWx1YWNpb25fZmluYWwuZW5j
```

**Y actualizarías la línea así:**
```javascript
const ENCRYPTED_CONFIG_URL_B64 = "aHR0cHM6Ly9pbnZqZXN1cy5naXRodWIuaW8vZXZhX1VUVGVjLzAxL2V2YWx1YWNpb25fZmluYWwuZW5j";
```

## Verificación

Para verificar que la URL está correcta, puedes decodificarla:
- En la consola del navegador: `atob("TU_URL_CODIFICADA")`
- Debe mostrar tu URL original

## Notas Importantes

- ✅ El nombre del archivo puede ser cualquier cosa, pero debe terminar en `.enc`
- ✅ La URL debe ser accesible públicamente
- ✅ Usa la misma clave secreta que usaste para cifrar
- ✅ No olvides actualizar la URL codificada en Base64 en el código
