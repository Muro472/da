n1 = int(input('Введіть число n:'))
n2 = 0
while n1 > 0:
    c = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10 + c
print(n2)