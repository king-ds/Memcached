from pymemcache.client import base
import time

client = base.Client(('172.31.40.140', 8000))

t0 = time.time()

for i in range(1, 500000):
    client.get(str(i))

t1 = time.time()

print(t1-t0)