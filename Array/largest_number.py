def largest_number(numbers):
    largest = float('-inf')  # Define largest inside the function
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

numbers = [7, 8, 9, 12, 16, 16, 3, 4, 89]
print(largest_number(numbers))
