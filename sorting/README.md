# Cheatsheet and Implementation of Various Sorting Algos

### Bubble Sort
O(n<sup>2</sup>)

Iterate through all sequential items repeatedly. Swap if first is larger than second.


### Selection Sort
O(n<sup>2</sup>), but typically faster than bubble

Iterate through n times, and place the largest (/next largest etc..) item in it's correct spot


### Insertion Sort
O(n<sup>2</sup>)

Makes one pass through data, inserting each item into it's correct spot in a growing sublist seeded from value at position 0


### Shell Sort
Between O(n) and O(n<sup>2</sup>)

Additional Space: none!

Calls the insertion sort repeatedly on sub-lists created by selecting every n'th item. Then combines all these and does a final insertion sort.

Use when: list is mostly pre-sorted.


### **Heap Sort**
O(n log n)

Additional Space: none! (can be done in-place)

Similar to Selection Sort, but faster since it uses a Heap data structure. It first finds the smallest (or largest) item in a list and inserts it into the Heap. Then it deconstructs the Heap into a list.


### **Merge Sort**
O(n log n)

Additional Space: O(n)

Splits the list into halves recursively until only one item per leaf. Then merges them upwards, incrementing through each sorted list pair to generate a new sorted list.
Requires extra storage.


### **Quick Sort**
Average: O(n log n), Worst: O(n<sup>2</sup>)

Additional Space: O(n)   (but there's a more complex in-place variant which is O(log n) )

Uses a pivot value. Any pair after the pivot value where one is greater and the other smaller will be switched. When the left and right marks cross, thats where the pivot value is placed. The list is divided in two at this point and quicksort is recursively called on those two sublists. It helps a lot to choose the pivot value wisely (aiming for the median value).


### Radix Sort
O(d*(n+b))   or    O((n+b)*logb(k))

where d is the # digits in our input integers, 
k is the maximum possible value of d, 
and b is the base for representing numbers (ex. for decimal b=10).

So for large n if b is ~= n then k will be small, and we'll be closer to O(n).

But if b is small, k is <= n^constant and we're around O(n log n)

Uses a key for each number calculated as (number / keyToAccess) % base, to iteratively sort by digits from least important to most important


.

.

**bold** denotes particularly common sorts
