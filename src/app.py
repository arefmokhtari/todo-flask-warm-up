#   -   -   -   -   -   -   -   -   #

from flask import Flask
from os import getcwd
#   -   -   -   -   -   -   -   -   #

app = Flask(__name__,
            root_path=getcwd())
#   -   -   -   -   -   -   -   -   #

__all__ = [ 'app', ]

#   -   -   -   -   -   -   -   -   #
