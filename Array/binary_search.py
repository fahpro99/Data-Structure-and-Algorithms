def binary_search(numbers, key):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = int((start + end) / 2)  # mid needs to be recalculated in each iteration

        if numbers[mid] == key:
            return mid
        elif numbers[mid] < key:  # right
            start = mid + 1
        else:
            end = mid - 1  # left

    return -1

nums = [56, 78, 86, 92, 98, 99]

print(binary_search(nums, 92))  # Output should be the index of 92, which is 3
