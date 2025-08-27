def reverse_list(arr):
    arr.reverse()
    print("Inside function:", arr)

nums = [1, 2, 3, 4, 5]
print("Before function:", nums)
reverse_list(nums)
print("After function:", nums)  