# Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

def remove_key(arr, key):
    i, j = 0, 0

    if (len(arr) < 2):
        return len(arr)

    while(j < len(arr)):
        if (arr[j] == key):
            j += 1
        # Include j element in new array.
        else:
            if j != i:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            i += 1
            j += 1

    return i

if __name__ == "__main__":
    print("Remove key")

    assert(remove_key([1, 2, 4, 2, 3, 9, 5, 2], 2)) == 5
    assert(remove_key([1, 2, 4, 3], 5)) == 4
    assert(remove_key([1, 2, 9, 4, 3, 9], 9)) == 4

