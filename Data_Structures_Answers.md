Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
    O(n), runs through storage twice. once to check if storage is at cap, then again to insert the item if storage is not at cap.

2. What is the space complexity of your ring buffer's `append` function?
    O(n), saves the array twice. Once in when the get method is ran, then again when the item is inserted.

3. What is the runtime complexity of your ring buffer's `get` method?
    O(n), n is the length of storage

4. What is the space complexity of your ring buffer's `get` method?
    O(n), saves stroage in a temp arr, if the value of the index is not none.

5. What is the runtime complexity of the provided code in `names.py`?
    O(n^2), nested for loop. as the input grows, the runtime grows by its square.

6. What is the space complexity of the provided code in `names.py`?
    O(log n) only the duplicates are stored. or O(n) if you count the initail saving of the 2 names lists.

7. What is the runtime complexity of your optimized code in `names.py`?
    O(log n) the first list is turned into a set, then the second list is traversed checking the set for the name at each index. I'm pretty sure this is O(log n) and not O(n) because the input is both lists, and the runtime is based off only one of those lists, preferably the shortest one.

8. What is the space complexity of your optimized code in `names.py`?
    O(log n) only the duplicates are saved, I think.