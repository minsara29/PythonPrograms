from collections import Counter

c = Counter("Kannan")
print(c)
print(list(c.elements()))


l = Counter([1, 2, 3, 4, 5, 6, 3, 2, 2, 4, 5, 7])
print(l)
print(l.most_common(1))

d = Counter({'red': 4, 'blue': 2})

print(d.most_common(1))