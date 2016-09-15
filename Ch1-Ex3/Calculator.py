l = 0
b = 0
n1 = float(input("Enter a number:"))
sign = input("Enter the operator:")
n2 = float(input("Enter another number:"))
a = 0
if sign == "+":
    a = n1+n2
elif sign == "-":
    a = n1-n2
elif sign == "*":
    a = n1*n2
elif sign == "/":
    a = n1/n1
print(a)

while l < 1:
    b = a
    sign2 = input("Enter an operator:")
    n = float(input("Enter another number:"))
    if sign2 == "+":
        a = b + n
    elif sign2 == "-":
        a = b - n
    elif sign2 == "*":
        a = b * n
    elif sign2 == "/":
        a = b / n
    print(a)

