number1 = [5, 2, 5, 2, 5]
for x in number1:
    print('X' * x)

print("")
print("")
number2 = [5, 2, 5, 2, 5]
for ii in number2:
    op = " "
    for jj in range(ii):
        op += "$"
    print(op)

print("")
print("")
number3 = [1, 1, 1, 1, 5]
for y in number3:
    op1 = " "
    for z in range(y):
        op1 += "# "
    print(op1)