class Solution:
	def LongestBitonicSequence(self, nums):
		n = len(nums)
		lis = [1]*n
		# Compute LIS values from left to right
		for i in range(n):
			for j in range(i):
				if(nums[i] > nums[j] and lis[i] < lis[j] + 1):
					lis[i] = lis[j] + 1
		
		lds = [1]*n
		# Compute LDS values from right to left */
		for i in range(n-2,-1,-1):
			for j in range(n-1,i,-1):
				if(nums[i] > nums[j] and lds[i] < lds[j] + 1):
					lds[i] = lds[j] + 1

		# Return the maximum value of lis[i] + lds[i] - 1*/
		ans = lis[0] + lds[0] - 1
		for i in range(1,n):
			ans = max(ans, lis[i] + lds[i] - 1)
		return ans

# Driver program to test the above function
arr = [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13,
		3, 11 , 7 , 15]
ob = Solution()
print(ob.LongestBitonicSequence(arr))


