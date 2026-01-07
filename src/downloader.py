import requests
import tarfile
import os

# 1. Definir rutas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00401/TCGA-PANCAN-HiSeq-801x20531.tar.gz"
compressed_file = "raw_data.tar.gz"
folder_name = "data"

# 2. Descargar el archivo
print("Initializing download...")
response = requests.get(url, stream=True)
with open(compressed_file, "wb") as f:
    f.write(response.content)
print("Donload complete")

# 3. Extraer el contenido
print("Extrayendo archivos...")
with tarfile.open(compressed_file, "r:gz") as tar:
    tar.extractall()

# 4. Organizar carpetas (Renombrar la carpeta larga a 'data')
original_folder = "TCGA-PANCAN-HiSeq-801x20531"
if os.path.exists(original_folder):
    if os.path.exists(folder_name):
        import shutil
        shutil.rmtree(folder_name) # Borra la carpeta data si existe pero está vacía
    os.rename(original_folder, folder_name)
    print(f"Extraction succesfully '{folder_name}' ")
else:
    print("Something went wrong")