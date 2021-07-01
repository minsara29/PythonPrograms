from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for k, v in s:
    d[k].append(v)

print(sorted(d.items()))

d1 = defaultdict(lambda: "NA")

d1["Kannan"] = 24
d1["dahlia"] = 10

print(d1["Kannan"])
print(d1["Pranav"])

string = "kannan"

c = defaultdict(int)

for i in string:
    c[i] += 1

print(c.items())