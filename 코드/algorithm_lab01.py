'''def SEQSEARCH(n, S, x):
    location = 1
    while(location <= n and S[location] != x):
        location += 1

    if (location > n):
        location = -1
    
    return location
        

if __name__=='__main__':
    SEQSEARCH()'''

class Lab01:
    def ssearch(self, S, x):
        location = 1
        while(location<=n and S[location]!=x):
            location = location+1
            if(location>n):
                location = -1
            
        return location
    

    def bsearchItr(self, S, x):
        pass

    def bsearchRec(self, S, x):
        pass

    def fibonacciItr(self,n):
        A=[0,1]
        int i
        int f[0.n]
        f[0]=0
        f[1]=1
        for i in range(2, n+1):
            A.append(A[i-1]+A[i-2])
            
        print(A)
        return A[len(n)]
    

    def hanoi(self, disks, source, aux, target):
        if(n==1):
        else:
           hanoi(disks-1, source, target, aux)
           print("move disks", disks, "from",source, target, aux)
           hanoi(disks-1, aux, source, target)
           

    def fibonacciRec(self,n):
        if(n==0):
            return 0
        elif(n==1):
            return 1
        return fibonacciRec(n-1)+fibonacciRec(n-2)
    
    def power2Itr(self, n):
        pass

    def power2Rec(self, n):
        pass