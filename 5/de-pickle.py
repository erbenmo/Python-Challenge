import pprint, pickle
import sys

f = open('banner.p', 'rb')

data = pickle.load(f)

for ls in data:
    for l in ls:
        sym, n = l
        for i in range(n):
            sys.stdout.write(sym)
    sys.stdout.write('\n')
