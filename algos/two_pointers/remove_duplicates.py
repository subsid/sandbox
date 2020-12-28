# Given an array of sorted numbers, remove all duplicates from it.
# You should not use any extra space; after removing the duplicates
# in-place return the length of the subarray that has no duplicate in it.
# 

def remove_duplicates(arr):
    i = 0
    j = i + 1

    if (len(arr) < 2):
        return len(arr)

    while(j < len(arr)):
        # If duplicate, increment only inner pointer
        if arr[i] == arr[j]:
            j += 1
        # Swap i+1 and j (Ignore if they point to same element)
        else:
            if (i + 1) != j:
                temp = arr[i + 1]
                arr[i + 1] = arr[j]
                arr[j] = temp
            i += 1
            j += 1

    return i + 1;



if __name__ == "__main__":
    print("Remove duplicates")

    assert remove_duplicates([1, 2, 2, 3, 4, 5, 5]) == 5
    assert remove_duplicates([1, 1, 1, 2, 9, 14, 14, 15, 17]) == 6
    assert remove_duplicates([1, 2, 9, 10]) == 4



