

import os
import importlib

def check_package(package_name):
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

def install_requirements():
    requirements_file = 'requirements.txt'
    with open(requirements_file) as f:
        packages = f.read().splitlines()
    for package in packages:
        if not check_package(package):
            print(f"Installing {package}...")
            os.system(f'pip install {package}')
        else:
            print(f"{package} is already installed.")

if __name__ == '__main__':
    install_requirements()
