class Solution:
    def bubbleSort(self,l):
        n = len(l)

        for i in range(n-1):
            swapped = False

            for j in range(n-i-1):
                if l[j]>l[j+1]:
                    l[j],l[j+1] = l[j+1],l[j]

                    swapped = True

            if swapped == False:
                return l

    def selectSort(self,l):
        n = len(l)

        for i in range(n - 1):
            min_ind = i
            for j in range(i + 1, n):

                if l[j] < l[min_ind]:
                    min_ind = j

            l[min_ind], l[i] = l[i], l[min_ind]
        return l

    def insertionSort(self,l):

        for i in range(1,len(l)):
            x = l[i]
            j = i-1

            while j>=0 and x<l[j]:
                l[j+1] = l[j]
                j = j-1

            l[j+1] = x
        return l
    # Merge and sort two arrays        
    def merge(self,arr, l,m,r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        i,j=0,0
        k = l
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                arr[k]=right[j]
                j+=1
                k+=1
            else:
                arr[k]=left[i]
                i+=1
                k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
            
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    
    def mergeSort(self, arr,l,r):
        # Your Code Here
        if l<r:
            m = (l+r)//2
            self.mergeSort(arr,l,m)
            self.mergeSort(arr,m+1,r)
            self.merge(arr, l,m,r)
        return arr
    
    def lomutoPartition(self, arr, l, h):
        pivot = arr[h]
        i = l - 1

        for j in range(l, h):
            if arr[j] <= pivot:  # error
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[h] = arr[h], arr[i + 1]

        return i + 1
    
    def qSort_lomutoPartition(self, arr, l, h):
        if l < h:
            p = self.lomutoPartition(arr, l, h)
            self.qSort_lomutoPartition(arr, l, p - 1)
            self.qSort_lomutoPartition(arr, p + 1, h)
        return arr
    
    def hoarsePartition(self,arr, l, h):
        pivot = arr[l]

        i = l - 1
        j = h + 1

        while True:

            i = i + 1
            while arr[i] < pivot:
                i = i + 1

            j = j - 1
            while arr[j] > pivot:
                j = j - 1

            if i >= j:
                return j

            arr[i], arr[j] = arr[j], arr[i]

    def qSort(self,arr, l, h):
        if l < h:
            p = self.hoarsePartition(arr, l, h)
            self.qSort(arr, l, p)
            self.qSort(arr, p + 1, h)
        return arr
    
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
    
    #Complete this code
    def countOnes(self,arr, N):
        #Your code here
        l = 0
        r = N-1
        if arr[l]==0:
            return 0
        elif arr[r]==1:
            return N
        
        while l<r:    #0<2
            m= (l+r)//2  #1
            if arr[m]==1:   #
                if arr[m+1]==0 or m==r:
                    return m+1
                else:
                    l=m    # 1
            else:
                r=m   # 

    def search(self, arr, N, X):
        l = 0
        r = N

        while l <= r:
            m = (l + r) // 2 
            if arr[m] == X:
                return m
            elif arr[m] < X:
                l = m + 1
            else:
                r = m - 1
        return -1


arr = [5891, 462, 1012, 288, 2897, 4607, 3883, 2095, 7746, 3155, 4495, 6157, 1267, 3484, 5676, 5714, 2827, 5702, 4631, 4010, 8120, 778, 8186, 503, 3833, 3500, 8287, 6136, 547, 121, 6031, 5545, 5661, 6773, 4663, 5283, 4600, 964, 7615, 1885]

bubble_Sort= Solution().bubbleSort(arr.copy())
print('Bubble Sort --> ',bubble_Sort)
print('*'*50)

select_Sort= Solution().selectSort(arr.copy())
print('\nSelection Sort  --> ',select_Sort)
print('*'*50)

insertion_Sort= Solution().insertionSort(arr.copy())
print('\nInsertion Sort  --> ',insertion_Sort)
print('*'*50)

merge_sort= Solution().mergeSort(arr.copy(),l=0,r=len(arr)-1)
print('Merge Sort  --> ',merge_sort)
print('*'*50)

qSort_lomutoPartition= Solution().qSort_lomutoPartition(arr.copy(),l=0,h=len(arr)-1)
print('\nQ Sort with Lomuto Partition  --> ',qSort_lomutoPartition)
print('*'*50)

q_Sort= Solution().qSort(arr.copy(),l=0,h=len(arr)-1)
print('\nQ Sort  --> ',q_Sort)
print('*'*50)

count = Solution().search(merge_sort,N=len(arr),X=4600)
print(count)


arr = [1, 2, 3]
count = Solution().search(arr,N=len(arr),X =1)
print(count)

arr = [0, 1, 2, 3, 4]
count = Solution().search(arr,N=len(arr),X=4)
print(count)
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
