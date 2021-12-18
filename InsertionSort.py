def InsertionSort(array):
  for i in range(1,len(array)):
    key = array[i]
    j= i-1
    while j >= 0 and key < array[j]:
      array[j+1] = array[j]
      j = j-1
    array[j+1] = key
  print("After Sorting:\n",array)
  
array = [4,2,1,8,9,5,10,7,5,6,11,0,-1]
InsertionSort(array)