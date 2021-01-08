"""
@author Swopnil Shrestha
@date 2021-01-08
"""

from collections.abc import Sequence
List = list[int]
AlphaList = list[str]

# Iteration
# Worst Case Asymptotic Runtime : O(N^2) where N = len(unsorted)
# Best Case Asymptotic Runtime: O(N) where N = len(unsorted)
# Average Case Asymptotic Runtime: O(N^2) where N = len(unsorted)

def insertion_sort(arr:Sequence[List]) -> Sequence[List]:
    """
    A Python List implementation of Insertion Sort
    
    @params 
        arr : Python list of int to be sorted
    @return 
        arr : A sorted arr

    Preconditions
        * arr is a List[int]

    Postconditions
        * arr[n] < arr[n+1]

    Invariants
        * len(arr)
        * type(arr)
        * sum(arr)
    """
    # LSI is the last sorted index
    lsi = 1
    while lsi <= len(arr)-1:
        insert_into = 0
        compare = arr[lsi]
        for idx in range(lsi,-1,-1):
            if compare > arr[idx]:break
            insert_into = idx
        del arr[lsi]
        arr.insert(insert_into,compare)
        lsi += 1
    return arr


def insertion_sort_single_alpha(arr:Sequence[AlphaList]) -> AlphaList:
    """
    A Python List of str implementation of Insertion Sort
    
    @params 
        arr : Python list of int to be sorted
    @return 
        arr : A sorted arr

    Preconditions
        * arr is a List[int]
        * len(arr[n]) == 1

    Postconditions
        * arr[n] < arr[n+1]

    Invariants
        * len(arr)
        * type(arr)
        * sum(arr)
    """
    lsi = 1
    while lsi <= len(arr)-1:
        insert_into = 0
        compare = arr[lsi]
        for idx in range(lsi,-1,-1):
            if ord(compare) > ord(arr[idx]):break
            insert_into = idx
        del arr[lsi]
        arr.insert(insert_into,compare)
        lsi += 1
    return arr


def main():
    cases = [[1,2,3,4,5],[5,4,3,2,1],[],[1,3,2,4,3,5]]
    cases_single_alpha = ["bacd","tiff","","hello","oooo"]
    for case in cases:print(insertion_sort(case))
    for case in cases_single_alpha:
        print(insertion_sort_single_alpha([x for x in case]))

if __name__ == "__main__":
    main()