def remove_duplicates(arr):
    if not arr:
        return []

    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    return arr[:j+1]

# Example usage:
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
unique_array = remove_duplicates(arr)
print(unique_array)
