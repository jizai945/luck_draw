import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico']

# TARGET
target = Executable(
    script="run.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "luck_draw",
    version = "0.0.0",
    description = "luck draw",
    author = "Timo",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)