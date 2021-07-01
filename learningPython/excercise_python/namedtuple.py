from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'city'])

s1 = Student("kannan", 24, "Evansville")

print(s1.name)
print(s1._fields)

s1._replace(name="ramchi")

print(s1)