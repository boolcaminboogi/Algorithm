import math
import random
import enum

Scale = enum.Enum("Scale", ["LeftHeavy", "RightHeavy", "Balanced"])

#1
class Pair:
    def __init__(self):
        self.min = 0
        self.max = 0
        
        
class Lab05:
    #1-1 p7-8
    def interpolationSearchItr(self, A, x):
        (left, right) = (0, len(A) - 1)

        while A[right] != A[left] and A[left] <= x <= A[right]:
            mid = left + (x - A[left]) * (right - left) // (A[right] - A[left])
            if x == A[mid]:
                return mid
            elif x < A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def interpolationSearchRec(self,left, right, x, A):
        if (left<= right and x >= A[left] and x <= A[right]):
            mid = left + ((x - A[left]) * (right - left)) // (A[right] - A[left])
            if x == A[mid]:
                return mid
            elif x < A[mid]:
                return self.interpolationSearchRec(left, mid-1, x, A)
            else:
                return self.interpolationSearchRec(mid+1, right, x, A)
        return -1
    
    #1-2 p10
    def findSL_large(self, A):
        n=len(A)
        small=large=A[0]
        for i in range(1,n):
            if A[i]>large:
                large=A[i]
        return large
            
    def findSL_small(self, A):
        n=len(A)
        small=large=A[0]
        for i in range(1,n):
            if small>A[i]:
                small=A[i]
        return small
        
    #1-3 p11
    def findSLPK_small(self, A):
        n=len(A)
        if A[0]<A[1]:
            small=A[0]
        else:
            small=A[1]
            
        for i in range(2, n, 2):
            if A[i]<A[i+1]:
                if A[i]<small:
                    small=A[i]
            else:
                if A[i+1]<small:
                    small=S[i+1]
        return small
    
    def findSLPK_large(self, A):
        n=len(A)
        if A[0]<A[1]:
            large=A[1]
        else:
            large=A[0]
            
        for i in range(2, n, 2):
            if A[i]<A[i+1]:
                if A[i+1]>large:
                    large=A[i+1]
            else:
                if A[i]>large:
                    large=A[i]
        return large

            
    #1-4 p14-15
    def rankSelection(self, A, low, high, k):
        pos=self.partition(A,low,high)
        
        if(pos+1==low+k):
            return A[pos]
        elif(pos+1>low+k):
            return self.rankSelection(A,low,pos-1,k)
        else:
            return self.rackSelection(A,pos+1,high,k-(pos+1-low))   
  
    def partition(self, A, low, high):
        pivot = A[low]
        j = low
        for i in range(low+1, high+1):
            if A[i] < pivot:
                j += 1
                A[j], A[i] = A[i], A[j]
                
        A[j], A[low] = A[low], A[j]
        return j
    
    
    #1-5
    def ternarySearchItr(self,A, x):
        (left, right) = (0, len(A) - 1)
        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            if A[mid1] == x:
                return mid1
            elif A[mid2] == x:
                return mid2
            elif A[mid1] > x:
                right = mid1 - 1
            elif A[mid2] < x:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
 
        return -1
    
    def ternarySearchRec(self,left, right, x, A):
        if (right >= left):
            mid1 = left + (right - left) //3
            mid2 = right - (right - left) //3
            
            if (A[mid1] == x):
                return mid1
         
            if (A[mid2] == x):
                return mid2
            if (x < A[mid1]):
                return self.ternarySearchRec(left, mid1 - 1, x, A)
            elif (x > A[mid2]):
                return self.ternarySearchRec(mid2 + 1, right, x, A)
            else:
                return self.ternarySearchRec(mid1 + 1, mid2 - 1, x, A)
        return -1
    
    
    def getMinMax1(self, arr: list) -> Pair:
        minmax = Pair()
        n=len(arr)

        if n == 1:
            minmax.max = arr[0]
            minmax.min = arr[0]
            return minmax

        if arr[0] > arr[1]:
            minmax.max = arr[0]
            minmax.min = arr[1]
        else:
            minmax.max = arr[1]
            minmax.min = arr[0]
 
        for i in range(2, n):
            if arr[i] > minmax.max:
                minmax.max = arr[i]
            elif arr[i] < minmax.min:
                minmax.min = arr[i]
        return minmax
    


#2
#2-1 p25
    def postOfficeLocation(self, P):
        Xs, Ys = zip(*P)
        Xs=list(Xs)
        Ys=list(Ys)
        print (Xs)
        print (Ys)
        ax=sum(Xs)//len(Xs)
        ay=sum(Ys)//len(Ys)
        ap=(ax,ay)
        
        mx=self.rankSelection(Xs, 0, len(Xs)-1, len(Xs)//2)
        my=self.rankSelection(Ys, 0, len(Ys)-1, len(Ys)//2)
        mp=(mx,my)
        mind=0
        for i in range(len(P)):
            mind+=self.Ed(ap,P[i])
        print("total distance from (average point) ({},{}) using Euclidean  = {:.2f}".format(ax,ay,mind))
        
        mind=0
        for i in range(len(P)):
            mind+=self.Md(ap,P[i])
        print("total distance from (average point) ({},{}) using Manhattan = {:.2f}".format(ax,ay,mind))
        
        mind=0
        for i in range(len(P)):
            mind+=self.Ed(mp,P[i])
        print("total distance from (median point) ({},{}) using Euclidean = {:.2f}".format(mx,my,mind))
        
        mind=0
        for i in range(len(P)):
            mind+=self.Md(mp,P[i])
        print("total distance from (median point) ({},{}) using Manhattan = {:.2f}".format(mx,my,mind))
            
    
    def Ed(self,p1, p2):		
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    def Md(self,p1, p2):		
        return (abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))
    
    def rankSelection(self,A, low, high, k): 
        pos = self.partition(A, low, high) 	

        if (pos+1 == low+k):				
            return A[pos] 
        elif (pos+1 > low+k):				 
            return self.rankSelection(A, low, pos-1, k) 
        else : 							
            return self.rankSelection(A, pos+1, high, k-(pos+1-low)) 
        
    def partition(self,A, low, high):
        pivot = A[low]
        j=low
        for i in range(low+1,high+1):
            if (A[i] < pivot):
                j+=1
                A[j],A[i]=A[i],A[j]
        A[j],A[low]=A[low],A[j]   
        return j


#2-2 p22-24
class FakeCoin:
    def __init__(self, n=10):
        self.n = n
        self.coins=self.random_coins(n)

    def random_coins(self,n):
        coins = [2] * (n - 1) + [1] * (1)
        random.shuffle(coins)
        print(coins)
        return coins
    
    def fake_coin_DQ2(self):
        pile = list(self.coins)
        while len(pile) > 1:
            n = len(pile) // 2
            A = pile[:n]
            B = pile[n : 2 * n]
            result = self.compare(A, B)
            if result == Scale.LeftHeavy:
                pile = B
            elif result == Scale.RightHeavy:
                pile = A
            elif result == Scale.Balanced:
                C = pile[2 * n :]
                pile = C
        return pile[0]
    
    def compare(self,left, right):
        delta = sum(right) - sum(left)
        if delta < 0:
            return Scale.LeftHeavy
        elif delta > 0:
            return Scale.RightHeavy
        else:
            return Scale.Balanced
        

#2-3
class BitFlips:
    def flip(self,ch):
        return '1' if (ch == '0') else '0'

    def minBitFlips(self,start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        res = 0
        if len(start) < len(goal):
            start = "0" * (len(goal) - len(start)) + start
        elif len(start) > len(goal):
            goal = "0" * (len(start) - len(goal)) + goal

        print(" start {} , goal {}".format(start, goal))
        startc = list(start)
        for i in range(len(start)):

            if start[i] != goal[i]:
                ch=start[i]
                startc[i]=self.flip(ch)
                print(startc)
                res += 1
        return res

