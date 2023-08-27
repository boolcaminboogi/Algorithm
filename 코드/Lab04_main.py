from Lab04 import*

#1
def testMergeSort():
    lab04=Lab04()
    #A=random.sample(range(1,30),15)
    A=[11,23,5,71,90,151,133,15,19,9,25,26,24,14,52,30,82,65,21]
    print("Original : ", A)
    lab04.merge_Sort_itr(A)
    print("Merge Sort Result : ", A)
    
def testQuickSort():
    lab04=Lab04()
    A=random.sample(range(1,30),15)
    print("Original : ", A)
    lab04.quickSort(A, 0, len(A)-1)
    print("Quick Sort Result : ", A)
    
def testHeapSort():
    lab04=Lab04()
    A=random.sample(range(1,30),15)
    print("Original : ", A)
    lab04.heapSort(A)
    print("Heap Sort Result : ", A)
    
def testRadixSort():
    lab04=Lab04()
    A=random.sample(range(1,30), 15)
    print("Original : ", A)
    lab05.radixSort(A)
    print("Radix Sort Result : ", A)
    
def testCountingSort():
    lab04=Lab04()
    A=random.sample(range(1,30),15)
    print("Original : ", A)
    k=max(A)+1
    lab04.countingSort(A, k)
    print("Counting Sort Result : ", A)
    
#2    
def testModifyMergeSort():
    lab04 = Lab04()
    A = random.sample(range(1, 30), 15)
    print('Original   :  ', A)
    lab04.merge_sortmod(A)
    print('Modify Merge Sort Result : ', A)
    
#3
def testCountingInversion():
    lab04 = Lab04()
    A = random.sample(range(1, 30), 15)
    print('Original   :  ', A)
    lab04.CountingInversion(A)
    print('count_inverse Sort Result : ', A)


def main():
    testMergeSort()
    #testQuickSort()
    #testHeapSort()
    #testRadixSort()
    #testCountingSort()
    #testModifyMergeSort()
    #testCountingInversion()
    
    
if __name__=='__main__':
    main()