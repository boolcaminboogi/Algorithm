
class Lab01:
    def ssearch(self, S, x):
        location = 0
        c = 0
        while location < len(S):
            if S[location] == x:
                return location
            location = location + 1

        return location

    def bsearchItr(self, S, x):
        (low, high) = (0, len(S) - 1)
        while low <= high:
            mid = (low + high) // 2
            if x == S[mid]:
                return mid
            elif x < S[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def bsearchRec(self, S, x):
        if S > x:
            return -1
        mid = (S + x) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            return self.binarysearchRec(S, mid - 1, x)
        else:
            return self.binarySearchRec(S,mid + 1, x)

    def fibonacciItr(self,n):
        A = [0,1]
        for i in range (2, n + 1):
            A.append(A[i-1] + A[i-2])

            print(A)
            return A[len(A) - 1]

    def hanoi(self, disks, source, auxiliary, target):
        if disks > 0:
            self.hanoi(disks - 1, source, target, auxiliary)
            print('Move disk', disks, 'from', source, '??', target)
            self.hanoi(disks -1, auxiliary, source, target)


    def fibonacciRec(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacciRec(n-1) + self.fibonacciRec(n-2)

    def power2Itr(self, n):
        result = 1
        for i in range(n):
            result = result * 2


    def power2Rec(self, n):
        if n == 0:
            return 1
        else:
            return 2 * self.power2Rec(n-1)
        
    def exchangeSort(self, S):
        n = len(S)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if S[j] < S[i]:
                    S[j], S[i] = S[i], S[j]
        print(S)

    def ArrayMembers(self, n, S):
        sum = 0
        for i in range(n):
            sum += S[i]

        return sum
    
    def MatrixMul(self, n, A, B):
        C = []
        for i in range(n):
            for j in range(n):
                C[i][j] = 0
                for k in range(n):
                    C[i][j] = C[i][j] + A[i][k] * B[k][j]

        return C
    
    