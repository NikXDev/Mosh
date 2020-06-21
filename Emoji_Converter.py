def fun(userinput):
    inp1 = userinput.split(" ")
    dict1 = {":)": "😀", ":(": "😔"}
    op = ""
    for i in inp1:
        op += dict1.get(i, i) + " "
    return op


inp = input("> ")
print(fun(inp))
