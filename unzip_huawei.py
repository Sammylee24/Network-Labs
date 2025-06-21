import zipfile
import os

zip_file = "Huawei Projects.zip"
extract_to = "Huawei_Projects"

print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir("."))

if not os.path.exists(zip_file):
    print(f"File '{zip_file}' not found!")
    exit(1)

try:
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Successfully extracted '{zip_file}' to '{extract_to}'")
except zipfile.BadZipFile:
    print("File exists but is not a valid ZIP archive")
    exit(1)
