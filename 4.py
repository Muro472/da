n = int(input("значення n"))
a = 0
b = 9
c = 9
i = 2
while i < n:
    d = c + 4 * a
    a = b
    b = c
    c = d
    i += 1
print(d)
print("x{0} = {1}".format(n,d))