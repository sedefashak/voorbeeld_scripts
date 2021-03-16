#!/usr/bin/python3

import sys
import os

print('about to exit')
if not os.path.exists('this-file'):
    sys.exit('file "this-file" does not exist')
print('never executed')
