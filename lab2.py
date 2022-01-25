#list1 = []
#neglist = []
#for i in range(10):
#    x = int(input("Enter a number to add to the list"))
#    if x >= 0:
#        list1.append(x)
#    elif x < 0:
#        neglist.append(x)
#print(list1)
#for i in neglist:
#    list1.append(i)
#print(list1)
#print(neglist)

oddlist = []
evenlist = []
for i in range(10):
    y = int(input("Enter number: "))
    z = y%2
    if z == 1:
        oddlist.append(y)
    elif z == 0:
        evenlist.append(y)
print(oddlist)
print(evenlist)
