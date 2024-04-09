class Solution:
    def maxAND(self, arr,N):
        res=0
        msb=31 
        lsb=1
        for bit in range(msb,-1,-1):
            pattern = res | (lsb << bit)
            count = sum((pattern & num) == pattern for num in arr)
            if count >= 2:
                res = res|(lsb<<bit)
        return res 


# Example usage:
arr = [4, 8, 12, 16]
ob= Solution()
max_and_value_pair=ob.maxAND(arr,len(arr))
print("Maximum AND value of a pair in the array:",max_and_value_pair)

''''
Here's how it works:

1. The function `maxAND` takes in an array `arr` of length `N` as input.
2. It initializes `res` to 0, which will eventually store the maximum AND value of any two elements in the array.
3. It iterates over each bit position from the 31st bit (most significant bit) to the 0th bit (least significant bit).
4. For each bit position `i`, it counts how many elements in the array have the bit set at position `i` 
when performing the bitwise AND operation with the current value of `res` combined with setting the `i`th bit to 1.
5. If the count `Count` is greater than or equal to 2 (i.e., there are at least two elements in the 
array with the `i`th bit set to 1), it updates `res` by setting the `i`th bit to 1.
6. Finally, it returns the resulting `res`, which represents the maximum AND value of any two elements in the array.
This solution effectively finds the maximum AND value of any two elements in the array 
by iteratively setting bits in the result (`res`) and checking if there are at least two elements in the array with that bit set.
If so, the bit is retained in the result. This process ensures that the maximum possible AND value is achieved 
while preserving the bitwise AND operation's conditions.
'''
