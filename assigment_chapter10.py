def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

bubble_sort(arr)

print("Sorted array:", arr)
