
"""
for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*", end="")
        else:
            print(" ", end="")
    print()     #--->for new line<---

#-------------------------------------------------

mystr = input("Enter the string: ")
len = len(mystr)

for row in range(len):
    for col in range(row+1):
        print(mystr[col], end="")
    print()         #--->for new line<---

#-------------------------------------------------

n = int(input("Enter the no. of rows: "))
num = 1

for row in range(1, n+1):
    for col in range(1, row+1):
        print(num, end=" ")
        num+=1
    print()
"""
#-------------------------------------------------

for row in range(0,5):
    for col in range(0,row+1):
        print("*", end="")
    print()
