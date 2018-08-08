def cmp(a, b):
    return (a > b) - (a < b)

list1, list2 = ['xyz',123],['abc',456]

print (cmp(list1, list2))
print (cmp(list2, list1))

list3 = list2 + [786];
print (list3)
print (cmp(list2, list3))


