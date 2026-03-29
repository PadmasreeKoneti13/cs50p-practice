range_of_series = int(input("Enter the range of series: "))
if range_of_series <= 0:
    print("You have not entered a valid range of series")
else:
    a = 0
    b = 1
    print(a,end=",")
    for i in range(1,range_of_series):
        a,b = b,a+b
        print(a,sep=',',end=",")

#approach 2
# a = 0
# b = 1
# print(a, b, sep=',', end=",")
# for i in range(2, range_of_series):
#     c = a + b
#     print(c, end=",")
#     a = b
#     b = c



