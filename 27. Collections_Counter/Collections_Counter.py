#!/usr/bin/python3

# https://www.codecademy.com/resources/docs/python/collections-module/Counter
# https://www.codecademy.com/resources/docs/python/dictionaries/update
# Syntax : myCollection = collections.Counter()

import collections
c = collections.Counter("supercalifragilisticexpialidocious")
print(f"Counter Collection: {c}\n")
print(f"Sorted: {sorted(c.elements())}\n")


d1 = {1:'one',2:'two', 3:'three'}
d2 = {4:'four', 5:'five', 6:'six'}
d1.update(d2)
print(d1)
