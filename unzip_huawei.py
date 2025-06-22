import zipfile
import os
import hashlib

# Your ZIP file
zip_file = 'Huawei Projects.zip'
extract_to = os.path.abspath('unzipped')

# Windows long path prefix
long_path_prefix = '\\\\?\\'

# Maximum allowed path length (Windows default is 260)
MAX_PATH = 260

# Ensure extraction folder exists
os.makedirs(extract_to, exist_ok=True)

def shorten_path(path, base_folder):
    """Shorten the path if it exceeds MAX_PATH by truncating folder/file names."""
    if len(path) <= MAX_PATH:
        return path

    # Hash the long part to avoid conflicts
    relative_path = os.path.relpath(path, base_folder)
    hashed = hashlib.md5(relative_path.encode()).hexdigest()[:8]

    # Use base name and hashed suffix
    filename = os.path.basename(path)
    shortened = filename[:100] + '_' + hashed

    # Place all shortened files into a special folder
    return os.path.join(base_folder, "_truncated", shortened)

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    for member in zip_ref.infolist():
        original_path = os.path.join(extract_to, *member.filename.split('/'))

        # Fix long paths
        if len(original_path) > MAX_PATH:
            target_path = shorten_path(original_path, extract_to)
        else:
            target_path = original_path

        if member.is_dir():
            os.makedirs(target_path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, 'wb') as out_file:
                out_file.write(zip_ref.read(member))

print(f"Extraction completed to: {extract_to}")
