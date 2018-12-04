import sys

path = '/home/allangoncalves/flask_api'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application