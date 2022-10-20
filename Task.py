a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
d = int(input("Input d: "))

max = d
if a > b and a > c and a >d:
    max = a
elif b > a and b > c and b > d:
    max = b
elif c > a and c > b and c > d:
    max = c
else:
    print(max)


max = d
if a > b and a > c and a >d:
    max = a
elif b > c and b > d:
    max = b
elif c > d:
    max = c
else:
    print(max)