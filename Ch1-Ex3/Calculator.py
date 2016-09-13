l = 0
b = 0
while l <1:
    n1 = float(input("Enter a number:"))
    sign = input("Enter the operator:")
    n2 = float(input("Enter another number:"))
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
    total = a + b
    b = total
    print("Your total is:", total)