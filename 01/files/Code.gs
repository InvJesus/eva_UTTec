/**
 * EVALUACIÓN DIGITAL - GOOGLE APPS SCRIPT
 * 
 * Este archivo maneja la lógica del servidor para servir la aplicación
 * y obtener el archivo cifrado desde Google Drive
 */

// ====================================
// FUNCIÓN PRINCIPAL - SERVIR LA WEB APP
// ====================================

function doGet() {
  return HtmlService.createTemplateFromFile('admDB01_GoogleAppsScript')
    .evaluate()
    .setTitle('Evaluación Digital')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0');
}

// ====================================
// FUNCIÓN PARA INCLUIR ARCHIVOS HTML
// ====================================

function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

// ====================================
// FUNCIÓN PARA OBTENER ARCHIVO .ENC DE GOOGLE DRIVE
// ====================================

/**
 * Obtiene el contenido del archivo cifrado desde Google Drive
 * @param {string} fileId - ID del archivo en Google Drive
 * @returns {string} Contenido del archivo cifrado
 */
function getEncryptedFileContent(fileId) {
  try {
    Logger.log('📁 Obteniendo archivo con ID: ' + fileId);
    
    // Obtener el archivo de Google Drive
    const file = DriveApp.getFileById(fileId);
    
    if (!file) {
      throw new Error('No se pudo encontrar el archivo con ID: ' + fileId);
    }
    
    Logger.log('✅ Archivo encontrado: ' + file.getName());
    
    // Leer el contenido como texto
    const content = file.getBlob().getDataAsString('UTF-8');
    
    Logger.log('📦 Contenido leído: ' + content.length + ' caracteres');
    
    return content;
    
  } catch (error) {
    Logger.log('❌ Error al obtener archivo: ' + error.toString());
    throw new Error('Error al acceder al archivo de Google Drive: ' + error.message);
  }
}

// ====================================
// FUNCIONES AUXILIARES OPCIONALES
// ====================================

/**
 * Verifica si el usuario tiene acceso al archivo
 * @param {string} fileId - ID del archivo en Google Drive
 * @returns {boolean} true si tiene acceso, false en caso contrario
 */
function checkFileAccess(fileId) {
  try {
    const file = DriveApp.getFileById(fileId);
    return file !== null;
  } catch (error) {
    Logger.log('❌ Sin acceso al archivo: ' + error.toString());
    return false;
  }
}

/**
 * Obtiene información del archivo sin descargar su contenido
 * @param {string} fileId - ID del archivo en Google Drive
 * @returns {object} Información del archivo
 */
function getFileInfo(fileId) {
  try {
    const file = DriveApp.getFileById(fileId);
    
    return {
      name: file.getName(),
      size: file.getSize(),
      mimeType: file.getMimeType(),
      dateCreated: file.getDateCreated(),
      lastUpdated: file.getLastUpdated(),
      url: file.getUrl()
    };
    
  } catch (error) {
    Logger.log('❌ Error al obtener info del archivo: ' + error.toString());
    throw new Error('Error al obtener información del archivo: ' + error.message);
  }
}
