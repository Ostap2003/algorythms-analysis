def selection_sort(arr: list) -> list:
    """Selection sort implementation
    find min in the arr, place it at the begging, continue
    looking for min excluding first entry, until the arr is not sorted"""
    arr_len = len(arr)
    for i in range(arr_len):
        arr_min = i
        for j in range(i + 1, arr_len):
            if arr[j] < arr[i]:
                arr_min = j
        arr[i], arr[arr_min] = arr[arr_min], arr[i]
    return arr


if __name__ == '__main__':
    arr = [4, 3, 2, 1, 0, -1]
    # arr = [3, 4, 1, 2]
 
    arr = [i for i in range(2**15)]
    arr = arr[::-1]

    print(selection_sort(arr))
