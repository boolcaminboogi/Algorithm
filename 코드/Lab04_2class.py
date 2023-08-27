#2번
class Lab04_2:
    mergeSort3(self,A,S,low,high):
        if(high-long<2):
            return
        else:
            mid1=low+((high-low)/3)
            mid2=low+2*((high-low)/3)+1
            self.mergeSort3(A,S,low,mid1)
            self.mergeSort3(A,S,mid1,mid2)
            self.mergeSort3(A,S,mid2,high);
            self.merge3(A,S,low,mid1,mid2,high)