import sys
from cx_Freeze import setup, Executable

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "snake",
        version = "0.1",
        description = "My GUI application!",
        executables = [Executable("snake_game.py", base=base)])
