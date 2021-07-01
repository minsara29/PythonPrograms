from collections import deque

#double ended queue

d = deque()

d.append(1)
d.append(2)
d.append(3)
d.append(4)
print(d)
d.appendleft(3)
print(d)

d.extend("abc")

print(d) 

d.append("abc")

print(d)