def countVowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

s = "hello world"
print("Number of vowels:", countVowels(s)) 