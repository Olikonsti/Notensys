from tkinter import *
import sys
import os
try:
    user = sys.argv[1]
except:
    pass

from Notensys import *
Notensys(web_mode=True)