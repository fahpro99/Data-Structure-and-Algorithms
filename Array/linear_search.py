def linear_search(numbers,target):
    for i in range((len(numbers))):
        if numbers[i]==target:
            return i
    return -1

numbers = [1,2,3,4,5,6,7,8,9,10]
target=7

print(linear_search(numbers,target))