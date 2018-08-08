def cmp(a, b):
    return (a > b) - (a < b)
dict1 = {'Name': 'a', 'Age': 7};
dict2 = {'Name': 'z', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print ("Return Value : %d" %  cmp (dict1["Name"], dict2["Name"]))
#print ("Return Value : %d" %  cmp (dict2, dict3))
#print ("Return Value : %d" %  cmp (dict1, dict4))
