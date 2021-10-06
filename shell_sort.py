def shell_sort(arr):
    size = len(arr)
    h = 1
    while h < (size / 3):
        h = 3 * h + 1
    while h >= 1:
        # h-sort the arr
        for i in range(h, size):
            j = i
            while j >= h and arr[j] < arr[j - h]:
                # swap
                arr[j - h], arr[j] = arr[j], arr[j - h]
                j -= h
        h = int(h / 3)
    return arr


if __name__ == '__main__':
    arr = [4, 3, 2, 1, 0, -1]
    # arr = [3, 4, 1, 2]
 
    arr = [i for i in range(2**15)]
    arr = arr[::-1]

    print(shell_sort(arr))
