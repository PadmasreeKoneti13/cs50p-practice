num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
if num1 < num2 and num1 < num3:
    print(num1,end=" < ")
    if num2 < num3:
        print(num2,num3,sep=" < ")
    else:
        print(num3,num2,sep=" < ")
elif num2 < num3:
    print(num2,end=" < ")
    if num1 < num3:
        print(num1,num3,sep=" < ")
    else:
        print(num3,num1,sep=" < ")
else:
    print(num3,end=" < ")
    if num2 < num1:
        print(num2,num1,sep=" < ")
    else:
        print(num1,num2,sep=" < ")

#2
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# num3 = int(input("enter third number: "))
if num1 < num2 and num1 < num3:
    if num2 < num3:
        sortedlist = [num1, num2, num3]
    else:
        sortedlist = [num1, num3, num2]
elif num2 < num3:
    if num1 < num3:
        sortedlist = [num2, num1, num3]
    else:
        sortedlist = [num2,num3, num1]
else:
    if num2 < num1:
        sortedlist = [num3, num2, num1]
    else:
        sortedlist = [num3, num1, num2]
print(sortedlist)

#3
nums = [num1, num2, num3]
nums.sort()
print(nums)

