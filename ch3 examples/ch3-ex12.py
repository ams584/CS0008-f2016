p = int(input("Enter the number of packages bought:"))
d = 0
if p >= 10 and p <= 19:
    d = .10
elif p >= 20 and p <= 49:
    d = .20
elif p >= 50 and p <= 99:
    d = .30
elif p >= 100:
    d = .40
discount = 99 * d
c = 99 - discount
print("Your discount is:", discount, "Your total cost is:", c)