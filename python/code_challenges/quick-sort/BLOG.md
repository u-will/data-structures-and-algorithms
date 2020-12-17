That is how the a how the computer will  solve the quick_sort problem

```
arr= [8,4,23,42,16,15]
  left = 0 right = 5
position = partition(arr , 0, 5)
 => pivot = 15
    low = -1
loop i = 0 => low = 0
                      Swap(arr, 0, 0) => temp;
          temp = 8
          arr[0] = 8
          arr[0] = 8 {arr= [8,4,23,42,16,15]}
 loop i =1 => low = 1
                     Swap (arr, 1, 1)=> temp = 4
               arr[1] = 4
              arr [1] = 4 {arr= [8,4,23,42,16,15]}
 loop i=2 => low =1
  loop i =3 => low = 1
loop i = 4 => low = 1
loop i = 5 => low =1

Swap(arr , 5, 2) => temp = 15
                arr[5] =23
               arr [2] = 15 {arr = [8,4, 15,42, 16, 23]}
(BACK TO POSITION) position = 2
(NEW-ARR = [8,4, 15,42, 16, 23])

quickstart(arr , 0, 1) =>  position = partition(arr , 0, 1)
=> pivot = 4
    low = -1
loop i = 0 => low = -1
loop i = 1 => low  = 0
                Swap( arr, 1, 0) => temp = 4
                    arr[1] = 8
                     arr [0] = 4 {[4, 8, 15, 42, 16, 23]}

                  AND SO ON.....
```
