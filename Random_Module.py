import random

for i in range(3):
    print(random.random())

print("..............")
for j in range(3):
    print(random.randint(10, 20))

print("..............")
member = ['mosh', 'josh', 'posh']
print(random.choice(member))
