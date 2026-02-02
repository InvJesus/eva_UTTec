#!/usr/bin/env python3
"""
Script Helper para actualizar el ID del archivo de Google Drive
Uso: python3 update_file_id.py NUEVO_ID
"""

import sys
import re

def update_file_id(new_id):
    """
    Actualiza el ID del archivo en Index.html
    """
    filename = 'Index.html'
    
    try:
        # Leer el archivo
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar y reemplazar el ID
        pattern = r'const GOOGLE_DRIVE_FILE_ID = "[^"]+";'
        replacement = f'const GOOGLE_DRIVE_FILE_ID = "{new_id}";'
        
        # Verificar si se encontró el patrón
        if not re.search(pattern, content):
            print("❌ Error: No se encontró la línea de configuración del ID")
            return False
        
        # Hacer el reemplazo
        new_content = re.sub(pattern, replacement, content)
        
        # Guardar el archivo
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ ID actualizado exitosamente en {filename}")
        print(f"📁 Nuevo ID: {new_id}")
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {filename}")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def extract_id_from_url(url):
    """
    Extrae el ID de una URL de Google Drive
    """
    # Patrón para URLs de Drive
    patterns = [
        r'/file/d/([a-zA-Z0-9_-]+)',
        r'id=([a-zA-Z0-9_-]+)',
        r'^([a-zA-Z0-9_-]+)$'  # Solo el ID
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def main():
    print("=" * 60)
    print("🔧 ACTUALIZADOR DE ID DE GOOGLE DRIVE")
    print("=" * 60)
    
    if len(sys.argv) < 2:
        print("\n❌ Error: Falta el ID o URL del archivo")
        print("\n📖 Uso:")
        print("  python3 update_file_id.py NUEVO_ID")
        print("  python3 update_file_id.py URL_COMPLETA_DE_DRIVE")
        print("\n💡 Ejemplos:")
        print("  python3 update_file_id.py 1IBtatGgMNe9FDcT6hJWbDyDPgSo5KH2E")
        print("  python3 update_file_id.py https://drive.google.com/file/d/1IBtatGgMNe9FDcT6hJWbDyDPgSo5KH2E/view")
        sys.exit(1)
    
    input_value = sys.argv[1]
    
    # Intentar extraer el ID si es una URL
    file_id = extract_id_from_url(input_value)
    
    if not file_id:
        print(f"❌ Error: No se pudo extraer un ID válido de: {input_value}")
        sys.exit(1)
    
    print(f"\n📁 ID extraído: {file_id}")
    print(f"📝 Actualizando Index.html...\n")
    
    if update_file_id(file_id):
        print("\n✅ ¡Actualización completada!")
        print("\n📋 Próximos pasos:")
        print("  1. Sube el archivo Index.html actualizado a Google Apps Script")
        print("  2. Asegúrate de que el archivo .enc esté compartido en Drive")
        print("  3. Implementa/actualiza tu Web App")
        print("\n" + "=" * 60)
    else:
        print("\n❌ La actualización falló. Verifica los errores arriba.")
        sys.exit(1)

if __name__ == "__main__":
    main()
