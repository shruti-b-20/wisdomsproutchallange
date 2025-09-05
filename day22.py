from collections import Counter

def first_element_k_times(arr, k):
    freq = Counter(arr)
    for num in arr:
        if freq[num] == k:
            return num
    return -1

print(first_element_k_times([3, 1, 4, 4, 5, 2, 6, 1, 4], 2))
print(first_element_k_times([2, 3, 4, 2, 2, 5, 5], 2))
print(first_element_k_times([1, 1, 1, 1], 1))
print(first_element_k_times([10], 1))
print(first_element_k_times([6, 6, 6, 6, 7, 7, 8, 8, 8], 3))
