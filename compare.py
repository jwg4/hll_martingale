import logging

from hll import HyperLogLog, MartingaleHyperLogLog

logging.basicConfig(level=logging.DEBUG)

hll = HyperLogLog(10, 54)
mhll = MartingaleHyperLogLog(10, 54)

f = open('random_ints', 'r')
for l in f.readlines():
    i = int(l)
    hll.add_object(i)
    mhll.add_object(i)

print hll.unadjusted_count
print mhll.count
