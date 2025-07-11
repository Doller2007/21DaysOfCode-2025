def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage:
print(selection_sort([64, 34, 25, 12, 22, 11, 90]))
print(selection_sort([5, 2, 8, 6, 1, 9, 4]))
print(selection_sort([100, 50, 25, 75]))
