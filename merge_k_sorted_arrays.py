import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []

    # Insert first element of each array into heap
    for i in range(len(arrays)):
        heapq.heappush(min_heap, (arrays[i][0], i, 0))

    # Extract the smallest and insert the next element from the same array
    while min_heap:
        value, array_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        # If there's a next element in the same array, add it to the heap
        if element_index + 1 < len(arrays[array_index]):
            next_value = arrays[array_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, array_index, element_index + 1))

    return result

# Example usage:
arrays = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
merged_array = merge_k_sorted_arrays(arrays)
print(merged_array)
