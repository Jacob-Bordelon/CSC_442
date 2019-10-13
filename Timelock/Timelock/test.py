import json
from hashlib import md5
import sys
import os

with open('testCases.json', 'r') as f:
    Jdict = json.load(f)

l = int(sys.argv[1])

test = Jdict[u'testCases'][l]


with open('current.txt','w') as w:
    w.write(test[u'current'])



f = "echo '{}' | python timelock.py".format(test[u'epoch'])
print f
os.system(f)

print "\nExpected Result: {}".format(test[u'result'])

