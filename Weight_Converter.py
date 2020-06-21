weight = int(input("Weight : "))
u_input = input("(L)bs or (K)g = ")

if u_input.lower() == "l":
    convert1 = weight * 0.45
    convert1 = round(convert1)
    print(f"You are {convert1} kg")

elif u_input.lower() == "k":
    convert = weight / 0.45
    convert = round(convert)
    print(f"You are {convert} pounds")

else:
    print("Invalid Input")
