# algorithmic-analysis-4
Python solutions for common algorithmic problems: Fibonacci sequence, merging K sorted arrays using a min-heap, and removing duplicates from a sorted array.

### Problem 0: Fibonacci Sequence

#### Code Implementation:

```python

def fib(n):

    if n == 0:

        return 0

    if n == 1:

        return 1

    return fib(n-1) + fib(n-2)

x = fib(5)

print(x)

```

#### Recursive Call Stack for `fib(5)`:

1\. `fib(5)` calls `fib(4)` and `fib(3)`

2\. `fib(4)` calls `fib(3)` and `fib(2)`

3\. `fib(3)` calls `fib(2)` and `fib(1)`

4\. `fib(2)` calls `fib(1)` and `fib(0)`

Now let's break it down step-by-step:

- `fib(5)` -> `fib(4)` -> `fib(3)` -> `fib(2)` -> `fib(1)`

- `fib(5)` -> `fib(4)` -> `fib(3)` -> `fib(2)` -> `fib(0)`

- `fib(5)` -> `fib(4)` -> `fib(3)` -> `fib(1)`

- `fib(5)` -> `fib(4)` -> `fib(2)` -> `fib(1)`

- `fib(5)` -> `fib(4)` -> `fib(2)` -> `fib(0)`

- `fib(5)` -> `fib(3)` -> `fib(2)` -> `fib(1)`

- `fib(5)` -> `fib(3)` -> `fib(2)` -> `fib(0)`

Final result: `fib(5) = 5`.

### Problem 1: Merging K Sorted Arrays

#### Approach:

We can merge K sorted arrays efficiently using a min-heap (or priority queue). The idea is to push the first element of each array into the heap and then extract the smallest element from the heap to add to the result array. Once an element is removed, the next element from the same array is pushed into the heap.

```python

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

```

#### Time Complexity Analysis:

- Insertion and extraction from the heap take `O(log K)`, and there are `K * N` elements in total.

- Thus, the overall time complexity is `O(N * K * log K)`.

#### Improvement Suggestions:

- If we know the arrays are balanced, we could use a more specialized merging technique like a balanced binary merge.

### Problem 2: Removing Duplicates from a Sorted Array

#### Approach:

Since the array is sorted, we can use a two-pointer approach. One pointer (`i`) will iterate through the array, and the other pointer (`j`) will track the position to place the next unique element.

#### Code

```python

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

```

#### Time Complexity Analysis:

- We only traverse the array once, making the time complexity `O(N)`.

#### Improvement Suggestions

- My suggestions for improvement would be since the array is already sorted, this approach is optimal. Any improvements would likely involve reducing space complexity, though it is already `O(1)` since we're modifying the array in-place.
