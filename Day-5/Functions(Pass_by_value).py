def reverse_tuple(arr):
    arr = arr[::-1]
    print("Inside function:", arr)

nums = (1, 2, 3, 4, 5)
print("Before function:", nums)
reverse_tuple(nums)
print("After function:", nums)