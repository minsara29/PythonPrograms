import sys

import numpy as np
import  time

# Size comparison with list
alist = range(1000)
print(f"list size: {sys.getsizeof(5)*len(alist)}") # getsizeof(4) -> return the size of the 4

array = np.arange(1000)
print(f"array size: {array.size * array.itemsize }")


# time comparison
l1 = range(1000000)
l2 = range(1000000)

start = time.time()
rst = [x+y for x,y in zip(l1,l2)]
# print(rst)
print((time.time() - start)*1000)

start = time.time()
a1 = np.arange(1000000)
a2 = np.arange(1000000)
rst = a1 + a2
# print(rst)
print((time.time() - start)*1000) #it takes less times than list











