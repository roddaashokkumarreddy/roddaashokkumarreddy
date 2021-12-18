def Merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l+i]
    for j in range(0, n2):
        R[j] = customList[m+1+j]
    
    i = 0 
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

def MergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2
        MergeSort(customList, l, m)
        MergeSort(customList, m+1, r)
        Merge(customList, l, m, r)
    return customList

array = [9,8,7,6,5,4,11,90,89,1,100,78,23,34,67,101,-1,0,-2]
l=0
r=len(array)-1
print("After Sorting:\n",MergeSort(array,l,r))