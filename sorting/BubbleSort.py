"""
@author Swopnil Shrestha
@date 2021-01-06
"""

from collections.abc import Sequence
List = list[int]

def bubble_sort(arr:Sequence[List]) -> Sequence[List]:
    """
    Implementation of Bubble Sort
    
    Worst-Case Asymptotic Runtime Complexity
        O(n) where n represents the length of the array

    Preconditions
        * @param arr : List[int]

    Postconditions
        * arr[n] <= arr[n+1] 

    Invariants
        * len(arr)
        * type(arr)

    """
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():
    print(bubble_sort([2,4,3,5,7,6]))
    print(bubble_sort([0,9,8,7,6,5]))

if __name__ == "__main__":
    main()


