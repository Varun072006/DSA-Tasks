def findMax(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

arr = [3, 7, 1, 9, 5]
print("Largest Element:", findMax(arr)) 