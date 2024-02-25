'''
Given an 0-indexed array of integers arr[] of size n, find its peak element. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist). The array is guaranteed to be in ascending order before the peak element and in descending order after it.

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

Example 1:

Input: 
n = 3
arr[] = {1, 2, 3}
Peak Element's Index: 2
Output: 1
Explanation: 
If the index returned is 2, then the output printed will be 1. 
Since arr[2] = 3 is greater than its adjacent elements, and 
there is no element after it, we can consider it as a peak 
element. No other index satisfies the same property.
Example 2:

Input:
n = 3
arr[] = {3, 4, 2}
Peak Element's Index: 1
Output: 1
Explanation: 
If the index returned is 1, then the output printed will be 1.
Since arr[1] = 4 is greater than its adjacent elements, and
there is no element after it, we can consider it as a peak
element. No other index satisfies the same property.
Your Task:
You don't have to read input or print anything. Complete the function peakElement() which takes the array arr[] and its size n as input parameters and return the index of the peak element.

Expected Time Complexity: O( log(n) ).
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 106
'''
url = 'https://www.geeksforgeeks.org/batch/dsa-python-self-paced/track/searching-basic-python/problem/peak-element'

class Solution:
    def leftIndex (self, N, arr, X):
        # code here 
        s = 0
        l = N-1
        if arr[s]==X:
            return s
        elif arr[l]==X:
            if arr[l-1]!=X:
                return l
        m = (s+l)//2
        while s<l:
            if arr[m]==X:
                if arr[m-1] != X:
                    return m
                l = m
                m = (s+l)//2
            elif arr[m]>X:
                l = m
                m = (s+l)//2
            else:
                s = m
                m = (s+l)//2
        return -1
 
    def peakElement1(self,arr, n):
        if n==1:
            return 0
        s = 0
        l = n-1
        if arr[s] > arr[l] & arr[s] > arr[s+1]:
            return s
        elif arr[l-1]<=arr[l]:
            return l
        
        while s<l:
            m = (s+l)//2
            if arr[m] >= arr[m-1] and arr[m+1] <= arr[m]:
                return m
            elif arr[m]<arr[m+1]:
                l = m
            else:
                s=m

    def peakElement(self,arr, n):  # [-2, 3, -1, -1, 2, 1, -2] 7
        if n==1:
            return 0
        l, r = 0, n-1   #0,6
        while l<r:      # 0<6
            m = (l+r)//2  # 3 2 1
            if arr[m] > arr[m+1]:   # -1 <2  -1 =-1
                if m==0 or arr[m-1] <= arr[m]:
                    return m
                else:
                    r = m-1
            else:
                l=m+1   #l =4 l=3
        return l
N = 3
arr =[1,2,3]
print(arr)
index = Solution().peakElement1(arr,N)
print(index)
index = Solution().peakElement(arr,N)
print(index)
    
N = 11
arr=[1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
X =7
print(arr)
index = Solution().peakElement1(arr,N)
print(index)
index = Solution().peakElement(arr,N)
print(index)

N = 7
arr =[-2, 3, -1, -1, 2, 1, -2]
X =-1
print(arr)
#index =  Solution().leftIndex(N, arr, X)
index = Solution().peakElement1(arr,N)
print(index)
index = Solution().peakElement(arr,N)
print(index)

N = 5
arr =[3, 5, 2, 3, 3]
print(arr)
index = Solution().peakElement1(arr,N)
print(index)
index = Solution().peakElement(arr,N)
print(index)

N = 1
arr =[3]
print(arr)
index = Solution().peakElement1(arr,N)
print(index)
index = Solution().peakElement(arr,N)
print(index)

N = 4
arr =[3, 2, 2, 1]
print(arr)
index = Solution().peakElement1(arr,N)
print(index)
index = Solution().peakElement(arr,N)
print(index)
