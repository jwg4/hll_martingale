from random import getrandbits, seed

seed(1337)

for i in range(100000):
    print getrandbits(64)
