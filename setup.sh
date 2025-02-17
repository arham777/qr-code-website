#!/bin/bash

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # For Unix/macOS
# venv\Scripts\activate  # For Windows (uncomment this line if using Windows)

# Upgrade pip
python -m pip install --upgrade pip

# Install development dependencies
pip install -e .

# Install additional development packages
pip install black flake8 pytest

# Verify installations
python -c "import streamlit; import qrcode; import PIL; print('All packages installed successfully!')" 