class lab02:
    #2-1	V
    def unique_elements(self, A):
        n=len(A)
        for i in range(n-1):
            for j in range(i+1, n):
                if A[i] ==A[j]:
                    return False
        return True
 

    #2-2. 시간 효율적인 알고리즘을 찾아라			V
    def GE(self, A):
        n=len(A)
        for i in range(n-1):
            for j in range(i+1, n):
                ratio = A[j][i]/A[i][i]
                for k in range(n+1):
                    A[j, k] = A[j][k]-A[i][k]*ratio

    #2-3. n^2을 2^n = 2^n−1 + 2^n−1 공식을 사용해 재귀적으로 풀어라
    def power(self, x, n):
        if n == 0:
            return 1
        if n&1:
            return x*self.power(x, n//2)*self.power(x, (n//2))
        return self.power(x, n//2)*self.power(x, (n//2))
    
    def power2(self, n):
        if n==0:
            return 1
        if n&1:
            return 2*self.power2(n//2)*self.power2(n//2)
        return self.power2(n//2)*self.power2(n//2)
    
    def power2b(self, n):
        if n==0:
            return 1
        if n&1:
            return self.power2b(n-1)+self.power2b(n-1)
        return self.power2b(n-1)+self.power2b(n-1)
                    
    #2-4. 계단 오르기
    def ways(self, n):
        if n<=2:
            return n
        else:
            return self.ways(n-1)+self.ways(n-2)
        
    #2-5. 공약수(반복)
    def gcd_inter(self, a, b):
        #print("gcd", (a,b))
        while b>0:
            r=a%b
            a=b
            b=r
        #print("gcd", (a,b))
        return a
        
    #2-6. 공약수(재귀)
    def gcd_rec(self, a, b):
        if(b==0): return a
        else: return self.gcd_rec(b, a%b)
    

    
            
        
    
        