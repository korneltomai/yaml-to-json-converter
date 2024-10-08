A python script to convert yaml files into json. It converts every .yml and .yaml files in the source directory into json, while retatining the names and file structure, copying every subdirectory that contains a convertable file.

# Dependencies:
- PyYAML

# Usage:
### 1. Install PyYAML
   ```
   pip install pyyaml
   ```
### 2. Run the script
   ```
   python convert_yaml.py [source directory] [target directory]
   ```
