string = 'asdkfjlasL : asdfla: dsfa'
liststring = list(string)
for c in range(0, len(liststring)):
    if liststring[c] == ':':
        liststring[c] = '-'
outString = "".join(liststring)
print(outString)