def zero_sum_subarrays(arr):
    n = len(arr)
    result = []
    prefix_sum = 0
    prefix_map = {0: [-1]}   
    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum in prefix_map:
            for start_index in prefix_map[prefix_sum]:
                result.append((start_index + 1, i))
        prefix_map.setdefault(prefix_sum, []).append(i)
    return result
