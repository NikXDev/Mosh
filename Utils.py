def find_max(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return (max(list2))


list1 = list(map(int, input().split()))
print(find_max(list1))