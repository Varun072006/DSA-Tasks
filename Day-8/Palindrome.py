n=int(input())
s=str(n)[::-1]
t=str(n)
if(t==s):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")