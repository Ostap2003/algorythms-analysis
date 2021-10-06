def insertion_sort(arr: list) -> list:
    """Inserion sort implementation"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j], arr[j + 1] = key, arr[j]
            j -= 1
    return arr

if __name__ == '__main__':
    arr = [4, 3, 2, 1, 0, -1]
    # arr = [3, 4, 1, 2]
    # arr = [el for el in range(10000)]
 
    arr = [i for i in range(2**15)]
    arr = arr[::-1]

    print(insertion_sort(arr))
