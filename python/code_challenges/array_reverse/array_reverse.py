def reverse_array(arr):
    leftIndex = 0
    rightIndex = len(arr)-1

    while leftIndex < rightIndex:
        arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]
        leftIndex += 1
        rightIndex -= 1
    return arr

result = reverse_array([2,4,5,6])
print(result)
