#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        
        for i in range(n):
            # Swapping elements to their correct positions
            while 0 < arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        res = n+1
        for i in range(n):
            if arr[i]!=i+1:
                res = min(i+1,res)
        return res
arr=[5,4,-1,1]
ob = Solution()
print(ob.missingNumber(arr,len(arr)))

arr=[-25, 38, 24, -17, 7, 31, 43, 8, 20, 49, -33, -11, 19, 13, -28, 44, 23, -3, -19, 12, 32, 40, 42, 41, 7, -35, -29, 7, 24, 41, -3, 1, -19, -29, -13, -10, 4, -20, 48]
ob = Solution()
print(ob.missingNumber(arr,len(arr)))
