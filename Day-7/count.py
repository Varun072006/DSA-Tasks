n = int(input())
c = 0
t = n
while (n != 0):
    n //= 10
    c += 1
print(f"Count of digits in {t} is {c}")