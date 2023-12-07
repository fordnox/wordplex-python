import sys

from .wordplex import WordPlex

_format = sys.argv[1]
wp = WordPlex()
wp.set_format(_format)
wp.go(print)
