a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
quotient=0
while a>0:
    a-=b
    quotient+=1
print(quotient)

#improvement
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if b == 0:
    print("Error:cannont divide by zero")
temp_a = abs(a)
temp_b = abs(b)
quotient = 0
while temp_a >= temp_b:
    temp_a -= temp_b
    quotient+=1
if (a<0)^(b<0):
    quotient = -quotient
print(quotient)