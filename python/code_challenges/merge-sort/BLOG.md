```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

Trace:

Sample Array: ​[8,4,23,42,16,15]

I- working in the Mergesort function:
step #1 : divission of the sample array in 2 arrays (left and right)

arr = [8,4,23,42,16,15]
mid = 3
right = [42, 16, 15]
left = [8,4,23]

step #2 a: divission of the left array in 2 arrays (left(left) and left(right))

​mid(left) = 1
left(left) =[8]
right(left) =[4,23]

step #2 b: divission of the right array in 2 arrays (right(left) and right(right))

​mid(right) = 1
left (right) = [42]
right(right) =[16,15]

step #3 a: divission of the right(left) array in 2 arrays (left(right(left)) and right(right(left)))

mid(​right(left)) =1
left(right(left)=[4]
right(right(left)=[23]

step #3 b:divission of the right(right) array in 2 arrays (left(right(right)) and right(right(right)))
​mid(​right(right)) =1
left(right(right)=[16]
right(right(right)=[15]

II- working in the merge-function inside of the Mergesort function :

slep 1 a: Finding the new right(left) array => right(right(left)=[23],left(right(left)=[4] and right(left) =[4,23]

New-right(left) = [4,23]

slep 1 b: Finding the new right(right) array => right(right(right)=[15], left(right(right)=[16]and right(right) =[16,15]

New-right(right) = [15,16]

 step 2 a: Finding the new left array => New-right(left) = [4, 23], left(left) =[8] and left = [8,4,23]

 ​New-left=[4,8,23]

 slep 2 b: Finding the new right array => ​New-right(right) = [15,16], left (right) = [42]
 and right = [42, 16, 15]

​New-right = [15,16,42]

step 3(FINAL STEP): Finding the new arr array => ​New-right = [15,16,42], New-left=[4,8,23] and arr = [8,4,23,42,16,15]

​​New-arr = [4,8,15,16,23,42]
