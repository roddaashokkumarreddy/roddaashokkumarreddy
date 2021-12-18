def ShellSort(array):
	n = len(array)
	gap = n//2
	while gap > 0:
		for i in range(gap,n):
			temp = array[i]
			j = i
			while j >= gap and array[j-gap] >temp:
				array[j] = array[j-gap]
				j -= gap
			array[j] = temp
		gap //= 2

array = [9,8,7,6,5,4,11,90,89,1,100,78,23,34,67,101,-1,0,-2]
ShellSort(array)
print("After Sorting:\n",array)

