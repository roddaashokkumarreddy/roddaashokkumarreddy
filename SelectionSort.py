def Selectionsort(array):
  for i in range(0,len(array)):
    min_index = i
    for j in range(i+1,len(array)):
      if array[min_index] > array[j]:
        min_index = j
      array[i], array[min_index] = array[min_index], array[i] 
  print("After Sorting:\n",array)

array = [13,2,4,9,10,1,6,3,0,-1,7,11,-2]
Selectionsort(array)

