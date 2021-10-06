def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)
        return arr

def merge(arr, left, right):
    i = 0
    j = 0
    k = 0

    left.append(2**20)
    right.append(2**20)

    while k < len(arr):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    return arr


if __name__ == '__main__':
    arr = [4, 3, 2, 1, 0, -1]
    # arr = [3, 4, 1, 2]
 
    arr = [i for i in range(2**15)]
    # arr = arr[::-1]

    print(merge_sort(arr))
