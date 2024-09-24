def maxSubarraySum(numbers):
    maxSum=float('-inf')
    for i in range(len(numbers)):
        start=i
        
        for j in range(i,len(numbers)):
            end=j
            currSum=0
            for k in range(start,end+1):
                currSum=+numbers[k]
            print(currSum)

            if maxSum<currSum:
                maxSum=currSum
    print(maxSum)
print(maxSubarraySum([20,30,40,-8,-9,20]))
                
