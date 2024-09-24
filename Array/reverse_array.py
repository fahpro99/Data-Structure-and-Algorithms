def reverse_arr(numbers):
    first=0
    last=len(numbers)-1
     
    while first<last:
        temp=numbers[first]
        numbers[first]=numbers[last]
        numbers[last]=temp

        first=first+1
        last=last-1
    return numbers

print(reverse_arr([1,2,3,4,5,6,7,8]))


