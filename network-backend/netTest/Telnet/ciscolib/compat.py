import sys

from pip._vendor.distlib.compat import raw_input

if sys.version_info[0] < 3:
    PY3 = False
    input = raw_input


    def s(a):
        return a
else:
    PY3 = True


    def s(a):
        return a.decode('ascii')
