import itertools

counter = itertools.count()

# print(next(counter))
# print(next(counter))

l = ["kannan", "ramchi", "dahlia", "pranav"]

print(list(zip(counter, l)))

counter = itertools.count(start=5)

print(next(counter))
print(next(counter))

counter = itertools.count(start=5, step=5)

print(next(counter))
print(next(counter))

counter = itertools.cycle([1, 2, 3])
print("itertools.cycle")

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


counter = itertools.repeat(2)
# counter = itertools.repeat(2, times=3)
print("itertools.repeat")

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

squares = map(lambda x: x*2, [1, 2, 3, 4, 5, 6])
print(list(squares))
squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))

char = ['a', 'b', 'c', 'd', 'e']
num = [1, 2, 3, 4, 5]
names = ["kannan", "ramchi", "dahlia", "pranav"]
rst = itertools.combinations(char, 2)

for i in rst:
    print(i)

rst = itertools.permutations(char, 2)
print("itertools.permutations")
for i in rst:
    print(i)

combined = itertools.chain(char, num, names) # usefull while list is big

print(list(combined))

people = [
    {"name": "Kannan",
     "age": 40,
     "state": "IN"
    },

    {"name": "ramchi",
     "age": 30,
     "state": "PK"
    },
    {"name": "Pranav",
     "age": 10,
     "state": "IN"
     },
    {"name": "Dahlia",
     "age": 5,
     "state": "US"
    }
]


sorted_people = sorted(people, key=lambda x: x["state"])

print(sorted_people)
# for key in sorted_people:
#     print(key)

group = itertools.groupby(sorted_people, lambda x: x["state"])

for key, val in group:
    print(key)
    for people in val:
        print(people)
    print()

