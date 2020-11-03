from distutils.core import setup
import py2exe
setup(console=['Combined_run.py'], requires=['openpyxl', 'PyAutoGUI', 'bs4', 'requests', 'pygame'])