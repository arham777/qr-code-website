from setuptools import setup, find_packages

setup(
    name="qr-code-generator",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit==1.24.0",
        "qrcode[pil]==7.3.1",
        "pillow==9.5.0",
        "pytest==7.1.2",
        "python-multipart==0.0.6",
        "watchdog==3.0.0",
    ],
    python_requires=">=3.9,<3.10",
) 