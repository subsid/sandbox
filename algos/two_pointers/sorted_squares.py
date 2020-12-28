# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
# O(N) time
# O(N) space

def sorted_squares(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr[0]**2]

    result = []
    # Find first non-negative number in array.
    i = 0
    while (i < len(arr)):
        if (arr[i] >= 0):
            break
        i += 1

    # Merge left and right of i in sorted square order
    j = i - 1
    while (j >= 0) and (i < len(arr)):
        j_sq, i_sq = arr[j]**2, arr[i]**2
        if (j_sq) < (i_sq):
            result.append(j_sq)
            j -= 1
        else:
            result.append(i_sq)
            i += 1

    while(j >= 0):
        result.append(arr[j]**2)
        j -= 1

    while(i < len(arr)):
        result.append(arr[i]**2)
        i += 1

    return result

if __name__ == "__main__":
    print("Sorted squares")

    assert sorted_squares([-2, -1, 0, 3, 4]) == [0, 1, 4, 9, 16]
    assert sorted_squares([-2, -1, 3, 4]) == [1, 4, 9, 16]
    assert sorted_squares([0, 3, 4]) == [0, 9, 16]
