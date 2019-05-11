#
#
import sys
import flask
import os


print('Python Version = ', sys.version)
print('Flask Version  = ', flask.__version__)


print(os.urandom(24).hex())
