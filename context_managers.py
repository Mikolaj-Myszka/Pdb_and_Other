"""
f = open('sample.txt', 'w')
f.write('Lorem ipsum dolor sit amet')
f.close()

with open('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet2')
"""

from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()


with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor etc.')

print(f.closed)