import os
import importlib
import subprocess
import sys


def install_requirements():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    requirements_file = os.path.join(script_dir, 'lib', 'requirements.txt')
    with open(requirements_file, encoding='utf-8') as f:
        packages = f.read().splitlines()
    for package in packages:
        if not check_package(package):
            print(f"Installing {package}...")
            subprocess.run([sys.executable, "-m", "pip", "install", package, "-q"], check=True)


def check_package(package_name):
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False


def update_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "-q"])
    except Exception as e:
        print(f"Error updating pip: {e}")


if __name__ == "__main__":
    try:
        print("Installing dependencies...")
        update_pip()
        install_requirements()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        install_ffmpeg_script = os.path.join(script_dir, 'lib', 'install_ffmpeg.py')
        os.system(f'python {install_ffmpeg_script}')
        
        vod_recovery_script = os.path.join(script_dir, 'vod_recovery.py')
        os.system(f'python {vod_recovery_script}')
    except Exception as e:
        print(f"An error occurred: {e}")
        input("\nPress Enter to continue...")