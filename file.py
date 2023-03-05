import os, sys
try:
    __import__("FILE").mex()
except Exception as e:
    exit(str(e))
