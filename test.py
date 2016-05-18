#!/usr/bin/python
from scaner import Scaner

import sys

for line in sys.stdin:
    expression = str(line)
    break

print("Expression: " + expression)

s = Scaner()
sc = s.sca(expression)

print sc
