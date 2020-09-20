import sys
import cx_Freeze

executables = [cx_Freeze.Executable("snake_game.py")]

cx_Freeze.setup(

    name="Snake Game",

    options={"build_exe": {"packages":["pygame"],

                           "include_files":["corps.png","fruit.png","head.png","collision.wav","move.wav"]}},

    executables = executables

    )

 