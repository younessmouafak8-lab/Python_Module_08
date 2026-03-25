import sys
import os

if __name__ == "__main__":
    if sys.base_prefix == sys.prefix:
        print("MATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("To enter the construct, run:")
        print("python-m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows\n")

        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")

        print("Current Python:", sys.executable)
        venv_path = os.environ.get('VIRTUAL_ENV')
        venv_name = os.path.basename(venv_path) if venv_path else None
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}\n")

        print("SUCCESS: You're in an isolated environment")
        print("Safe to install packages without affecting")
        print("the global system")

        print("Package installation path:")
        for path in sys.path:
            if "site-packages" in path:
                print(path)
                break
