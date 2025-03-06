import json
import os
import re

def extraer_metadatos(directorio_md):
    metadatos_lista = []
    for nombre_archivo in os.listdir(directorio_md):
        if nombre_archivo.endswith(".md"):
            ruta_archivo = os.path.join(directorio_md, nombre_archivo)
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo_md:
                    contenido = archivo_md.read()

                # Buscar el bloque YAML al principio del archivo
                match = re.match(r"^---\n(.*?)\n---\n", contenido, re.DOTALL)

                if match:
                    yaml_bloque = match.group(1)
                    metadatos = {}
                    for linea in yaml_bloque.splitlines():
                        if ":" in linea:
                            clave, valor = linea.split(":", 1)
                            clave = clave.strip()
                            valor = valor.strip().strip('"')  # Eliminar comillas alrededor del valor
                            metadatos[clave] = valor
                    metadatos['link'] = nombre_archivo[:-3] # Remove '.md' extension
                    metadatos_lista.append(metadatos)

            except Exception as e:
                print(f"Error al procesar {nombre_archivo}: {e}")

    return metadatos_lista

def ordenar_por_fecha(metadatos_lista):
  """Ordena la lista de metadatos por fecha (de más reciente a menos reciente)."""
  return sorted(metadatos_lista, key=lambda x: x.get('date', ''), reverse=True)

def guardar_en_json(metadatos_lista, archivo_json):
    datos = {"posts": metadatos_lista}
    try:
        with open(archivo_json, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        print(f"Metadatos guardados en {archivo_json}")
    except Exception as e:
        print(f"Error al guardar en {archivo_json}: {e}")

if __name__ == "__main__":
    # Directorios de los archivos
    directorio_md = './docs/blog/posts'
    archivo_json = './docs/en/blog/posts.json' 
    directorio_md_es = './docs/es/blog/posts'
    archivo_json_es = './docs/es/blog/posts.json' 
    metadatos = extraer_metadatos(directorio_md)
    metadatos_es = extraer_metadatos(directorio_md_es)
    metadatos_ordenados = ordenar_por_fecha(metadatos) 
    metadatos_ordenados_es = ordenar_por_fecha(metadatos_es) 
    guardar_en_json(metadatos_ordenados, archivo_json)
    guardar_en_json(metadatos_ordenados_es, archivo_json_es)
