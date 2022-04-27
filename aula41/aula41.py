import sys
import time


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))

li1 = [x for x in range(100000)]
li2 = (x for x in range(100000))
for v in li2:
    print(v)

print(sys.getsizeof(li1))
print(sys.getsizeof(li2))