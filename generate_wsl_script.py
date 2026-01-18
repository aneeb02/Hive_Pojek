
import os

script_content = """#!/bin/bash
# WSL Setup Script for Hive

# 1. Clean up old venv
echo "Cleaning up..."
rm -rf venv

# 2. Create new venv
echo "Creating virtual environment..."
python3 -m venv venv

# 3. Activate and install
echo "Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup Complete!"
echo "Run: source venv/bin/activate"
echo "Then: python manage.py runserver"
"""

with open("setup_wsl.sh", "w", encoding="utf-8", newline='\n') as f:
    f.write(script_content)

print("setup_wsl.sh created with LF line endings.")
