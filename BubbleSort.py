def BubbleSort(array):
  for i in range(len(array)-1):
    for j in range(len(array)-i-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
  print("After Sorting:\n",array)

array = [2,4,9,10,1,6,3,0,-1,7,11,-2,22,23]
BubbleSort(array)
