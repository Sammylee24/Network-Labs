import zipfile
import os

zip_file = "Huawei Projects.zip"
extract_to = "Huawei_Projects"

# Ensure the output directory exists
os.makedirs(extract_to, exist_ok=True)

# Unzip the file
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print(f"✅ Successfully extracted '{zip_file}' to '{extract_to}'")
