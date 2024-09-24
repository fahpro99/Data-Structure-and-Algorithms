def num_pairs(numbers):
    pairs=[]
    for i in range(len(numbers)):
         curr=numbers[i]
         for j in range(i+1,len(numbers)):
              pairs.append(f"{curr},{numbers[j]}")
    return pairs

            

print(num_pairs([1,2,3,4,5,6]))