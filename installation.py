<<<<<<< HEAD
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
=======
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
>>>>>>> 693751de77eeb8c60c1b63bac1bad7da24e87e1a
    install_package("pyautogui")