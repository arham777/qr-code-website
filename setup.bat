@echo off

REM Create and activate virtual environment
python -m venv venv
call venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install development dependencies
pip install -e .

REM Install additional development packages
pip install black flake8 pytest

REM Verify installations
python -c "import streamlit; import qrcode; import PIL; print('All packages installed successfully!')"

pause 