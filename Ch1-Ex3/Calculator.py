n1 = float(input("Enter the first number:"))
sign = input("Enter the operator:")
n2 = float(input("Enter the second number:"))
a = 0
if sign == "+":
    a = n1+n2
    print(a)
elif sign == "-":
    a = n1-n2
    print(a)
elif sign == "*":
    a = n1*n2
    print(a)
elif sign == "/":
    a = n1/n1
    print(a)
