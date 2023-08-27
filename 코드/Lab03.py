import math
import sys

class Lab03:
    #강의자료 8pg
    def powerSet(self, L):
        if len(L)==0:
            return [[]]
        else:
            base = self.powerSet(L[-1])
            print('\n pre-secursive, L=', L)
            operator = L[-1:]
            print('\n post-recursive, L= ', base + [(b + operator) for b in base])
            return base + [(b + operator) for b in base]
        
    def distance(self,p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    def intersectionSet(self,A, B):
        C=[]
        m=len(A)
        n=len(B) 
        i, j = 0, 0
        while i < m and j < n: 
            if A[i] < B[j]: 
                i += 1
            elif B[j] < A[i]: 
                j+= 1
            else: 
                print(B[j]) 
                C.append(B[j])
                j += 1
                i += 1
        return C
    
    def binomialCoeffRec(self, n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
   
        return self.binomialCoeffRec(n-1, k-1) + self.binomialCoeffRec(n-1, k) 
    
    def binomialCoeffDP(self,n, k):
        B = [[0 for x in range(k+1)] for x in range(n+1)]
        for i in range(n+1):
            for j in range(min(i, k)+1):
                if j == 0 or j == i:
                    B[i][j] = 1
                else:
                    B[i][j] = B[i-1][j-1] + B[i-1][j]
 
        return B[n][k]
    
    def maxZeroSumSubmatrix(self,matrix):
        (M, N) = (len(matrix), len(matrix[0]))
        S=self.integralMatrix(matrix)
        maxMS=rowStart = rowEnd = colStart = colEnd = 0

        for i in range(M):
            for j in range(i, M):
                for m in range(N):
                    for n in range(m, N):
                        ssum = S[j + 1][n + 1] - S[j + 1][m]-S[i][n + 1] + S[i][m]
                        ms=((j-i)+1)*((n-m)+1)
                        if ssum == 0 and maxMS < ms:
                            maxMS=ms
                            rowStart = i
                            rowEnd = j
                            colStart = m
                            colEnd = n
        
        A = [ [ matrix[ i ][ j ] for j in range(colStart, colEnd+1 ) ]
                                  for i in range(rowStart ,rowEnd+1 ) ]
                    
        print("Submatrix is formed by rows", rowStart, "to", rowEnd,
            "and columns from", colStart, "to", colEnd)
        return A
    
    def integralMatrix(self, matrix):
        (M, N) = (len(matrix), len(matrix[0]))
        S = [[0 for x in range(N + 1)] for y in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1]+ matrix[i - 1][j - 1]
        return S
    
    def SM(self,txt, pat): 
        m = len(pat) 
        n = len(txt) 
        for i in range(n-m+1): 
            j = 0
            while(j < m): 
                if (txt[i + j] != pat[j]): 
                    break
                j += 1
  
            if (j == m):  
                print("Pattern {} found at index {} ".format (txt[i:i+m],i+1))

#cp에러    
    def closest_pair(self,pList):
        cp=[]
        n = len(pList)
        mindist = float("inf")  
        for i in range(n-1):
            for j in range(i+1, n):
                dist = self.distance(pList[i], pList[j])
                if dist < mindist:
                    mindist = dist
                    cp=(pList[i],pList[j])
        return cp
    
    
#1  
#class sumArray:
    def maxSum1(self, arr):
        mx=sm=0
        noo=0;
        n=len(arr)
        for i in range(n):
            for j in range(i, n):
                sm=0
                for k in range(i, j+1):
                    sm+=arr[k]
                    noo=+1
            mx=+1
        print("noo= ",noo)
        return mx
            
    def maxSum2(self, arr):
        mx = 0
        noo=0
        n=len(arr)
        for i in range(n):
            sm=0
            for j in range(i, n):
                sm+=arr[j]
                noo=noo+1
            mx= max(mx, sm)
        print("noo=",noo)    
        return mx
    
    def maxSum3(self, arr, low, high):
        if(low==high):
            return arr[low]
        mid = (low+high)//2
        return max(self.maxSum3(arr, low, mid),
                   self.maxSum3(arr, mid+1, high))
                   #self.maxCrossingSum(arr, low, mid, high)
        
        
    def maxcorssingSum(self, arr, low, mid, high):
        sm=0
        left_sum=-10000
        for i in range(mid,low-1, -1):
            sm=sm+arr[i]
            if(sm>left_sum):
                left_sum=sm
        sm=0
        right_sum=-1000
        for i in range(mid+1,high+1):
            sm=sm+arr[i]
            if(sm>right_sum):
                right_sum=sm
        return max(left_sum+right_sum, left_sum, right_sum)
    
    
    def maxSum4(self, arr):
        max_so_far=0
        curr_max=arr[0]
        for i in range(1,len(arr)):
            curr_max=max(arr[i], curr_max+arr[i])
            max_so_far=max(max_so_far, curr_max)
        return max_so_far
                         

            
