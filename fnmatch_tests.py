#### python3 fnmatch_tests.py

import fnmatch, os

current = os.listdir()

for file in current:
    if fnmatch.fnmatch(file, '*.py'): # returns True/False
        continue
    else:
        print(file)

