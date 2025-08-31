n = int(input())
t = n
c = 0
s = 0

while (n != 0):
    n //= 10
    c += 1

n = t
while (n != 0):
    rem = n % 10
    s += rem ** c
    n //= 10

if (s == t):
    print(f"{t} is an armstrong number")
else:
    print(f"{t} is not an armstrong number")