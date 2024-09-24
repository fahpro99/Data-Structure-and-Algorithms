def max_subarray_sum(numbers):
    n = len(numbers)
    if n == 0:
        return 0

    # Step 1: Create the prefix sum array
    prefix = [0] * n
    prefix[0] = numbers[0]
    
    # Calculate the prefix sums
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + numbers[i]

    max_sum = float('-inf')  # Initialize max_sum to the smallest possible value

    # Step 2: Calculate the maximum subarray sum using the prefix sum array
    for i in range(n):
        for j in range(i, n):
            # Subarray sum from i to j: prefix[j] - prefix[i-1] if i > 0
            if i == 0:
                current_sum = prefix[j]
            else:
                current_sum = prefix[j] - prefix[i - 1]
            
            # Update max_sum if current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

# Test with the array
print(max_subarray_sum([20, 30, -10, 50, -60, 40]))  # Should return 90
