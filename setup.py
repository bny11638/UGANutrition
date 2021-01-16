from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('app/__main__.py', base=base, target_name = 'UGANutrition',icon='app/resources/logosmall.png')
]

setup(name='UGANutrition',
      version = '1.0',
      description = "Calorie Counter for UGA's cafeteria selection.",
      options = {'build_exe': build_options},
      executables = executables)
