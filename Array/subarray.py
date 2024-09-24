def subarray(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            # To print the subarray from index i to j (inclusive)
            print(numbers[i:j+1])

subarray([20, 30, 40, 50, 60])
