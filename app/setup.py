from cx_Freeze import setup, Executable
import os

def find_data_file(filename):
    if getattr(sys, "frozen", False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
    
    print(os.path.join(datadir, 'lib', 'resources', filename))
    return os.path.join(datadir, 'lib', 'resources', filename)

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('__main__.py', base=base, target_name = 'UGANutrition')
]

setup(name='UGANutrition',
      version = '1.0',
      description = "Calorie Counter for UGA's cafeteria selection.",
      options = {'build_exe': build_options},
      executables = executables,
      include_package_data=True)