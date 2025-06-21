import zipfile
import os

zip_file = "/Huawei Projects.zip"
extract_to = "Huawei_Projects"

if not os.path.exists(zip_file):
    print(f"❌ ZIP file not found: {zip_file}")
    print("Available files:", os.listdir("."))
    exit(1)

print(f"🔍 Found ZIP file: {zip_file}")
print(f"📂 Extracting to: {extract_to}")

# Create output directory if it doesn't exist
os.makedirs(extract_to, exist_ok=True)

try:
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"✅ Successfully extracted '{zip_file}'")
except zipfile.BadZipFile:
    print("❌ The file is not a valid ZIP archive.")
    exit(1)
