expression = input("Expression: ").strip()
x,y,z = expression.split(" ")

if y == "+":
    print(f"{float(x) + float(z):.1f}")
elif y == "-":
    print(f"{float(x) - float(z):.1f}")
elif y == "*":
    print(f"{float(x) * float(z):.1f}")
elif y == "/":
    print(f"{float(x) / float(z):.1f}")