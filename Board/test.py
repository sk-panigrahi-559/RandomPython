import os
import tkinter
print(os.path.dirname(__file__))
print(os.path.join(os.path.dirname(__file__), "images\LOGO.png"))

import pathlib
illust_path = os.fspath(pathlib.Path(__file__).parent / 'images' / 'LOGO.png')
print(illust_path)