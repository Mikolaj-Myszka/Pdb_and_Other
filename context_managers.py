"""
f = open('sample.txt', 'w')
f.write('Lorem ipsum dolor sit amet')
f.close()

with open('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet2')
"""

class OpenFile():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
    

with OpenFile('sample.txt', 'w') as f:
    f.write('fdjfdjhfksd')


"""
from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor etceefew22.')

print(f.closed)
"""

"""
import os


cwd = os.getcwd()
os.chdir('ContextManager_sample_dir_1')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('ContextManager_sample_dir_2')
print(os.listdir())
os.chdir(cwd)
"""

"""
import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd  = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('ContextManager_sample_dir_1'):
    print(os.listdir())

with change_dir('ContextManager_sample_dir_2'):
    print(os.listdir())
"""
