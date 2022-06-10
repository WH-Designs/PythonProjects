import time
import random


def selection_sort(arr: list):
    time.sleep(1.0)

    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    # return arr


def insertion_sort(arr: list):
    time.sleep(1.0)

    for p in range(1, len(arr)):
        temp = arr[p]
        j = p

        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = temp

    # return arr


def merge_sort(arr: list):
    time.sleep(1.0)

    new_arr = [None] * len(arr)

    merge_sorter(arr, new_arr, 0, len(arr) - 1)

    # return new_arr


def merge_sorter(arr: list, temp_arr: list, left, right):
    if left < right:
        center = int((left + right) // 2)  # left + (right - left) // 2
        merge_sorter(arr, temp_arr, left, center)
        merge_sorter(arr, temp_arr, center + 1, right)
        merge(arr, temp_arr, left, center + 1, right)


def merge(arr: list, temp_arr: list, left, right, right_end):
    left_end = right - 1
    temp_pos = left
    num_elements = right_end - left + 1

    while left <= left_end and right <= right_end:
        if arr[left] <= arr[right]:
            temp_arr[temp_pos] = arr[left]
            temp_pos += 1
            left += 1
        else:
            temp_arr[temp_pos] = arr[right]
            temp_pos += 1
            right += 1

    while left <= left_end:
        temp_arr[temp_pos] = arr[left]
        temp_pos += 1
        left += 1
    while right <= right_end:
        temp_arr[temp_pos] = arr[right]
        temp_pos += 1
        right += 1

    for i in range(num_elements):
        arr[right_end] = temp_arr[right_end]
        right_end -= 1


CutOff = 10


def quick_sort(arr: list):
    time.sleep(1.0)

    quick_sorter(arr, 0, len(arr) - 1)


def quick_sorter(arr: list, low, high):
    if low + CutOff > high:
        for p in range(low, high):
            temp = arr[p]
            j = p

            while j > low and temp < arr[j - 1]:
                arr[j] = arr[j - 1]
                j -= 1

            arr[j] = temp

    else:
        middle = int((low + high) // 2)

        if arr[middle] < arr[low]:
            temp = arr[low]
            arr[low] = arr[middle]
            arr[middle] = temp

        if arr[high] < arr[low]:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp

        if arr[high] < arr[middle]:
            temp = arr[middle]
            arr[middle] = arr[high]
            arr[high] = temp

        temp = arr[middle]
        arr[middle] = arr[high - 1]
        arr[high - 1] = temp

        pivot = arr[high - 1]

        i = low
        j = high - 1

        while True:
            while True:
                i += 1
                if arr[i] < pivot:
                    break
            while True:
                j -= 1
                if pivot < arr[j]:
                    break
            if i >= j:
                break

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        temp = arr[i]
        arr[i] = arr[high - 1]
        arr[high - 1] = temp

        quick_sorter(arr, low, i - 1)
        quick_sorter(arr, i + 1, high)


def Swap(item1, item2):
    temp = item1
    item1 = item2
    item2 = temp


def shell_sort(arr: list):
    time.sleep(1.0)

    n = len(arr)
    g = int(n / 2)

    while g > 0:

        for i in range(int(g), int(n)):
            temp = arr[i]

            j = i
            while j >= g and arr[j - int(g)] > temp:
                arr[j] = arr[j - int(g)]
                j -= int(g)

            arr[j] = temp
        g /= 2


def random_array(amount):
    arr = []

    tmp = random.randint(0, amount)

    for i in range(amount):
        while tmp in arr:
            tmp = random.randint(0, amount)

        arr.append(tmp)

    return arr


def presorted_array(amount):
    arr = []

    for i in range(amount):
        arr.append(i)

    return arr


def reversed_array(amount):
    arr = []

    for i in range(amount):
        arr.append(i)

    reversed(arr)

    return arr


def main():
    '''
    Main function, for running all of the sorting tests
    '''

    sorted_array_1000 = presorted_array(1000)
    random_array_1000 = random_array(1000)
    reversed_array_1000 = reversed_array(1000)

    sorted_array_5000 = presorted_array(5000)
    random_array_5000 = random_array(5000)
    reversed_array_5000 = reversed_array(5000)

    sorted_array_10000 = presorted_array(10000)
    random_array_10000 = random_array(10000)
    reversed_array_10000 = reversed_array(10000)

    sorted_array_50000 = presorted_array(50000)
    random_array_50000 = random_array(50000)
    reversed_array_50000 = reversed_array(50000)

    sorted_array_100000 = presorted_array(100000)
    random_array_100000 = random_array(100000)
    reversed_array_100000 = reversed_array(100000)

    sorted_array_200000 = presorted_array(200000)
    random_array_200000 = random_array(200000)
    reversed_array_200000 = reversed_array(200000)

    sorted_array_300000 = presorted_array(300000)
    random_array_300000 = random_array(300000)
    reversed_array_300000 = reversed_array(300000)

    t0 = time.time()
    selection_sort(random_array_300000)
    insertion_sort(random_array_300000)
    merge_sort(random_array_300000)
    quick_sort(random_array_200000)
    shell_sort(random_array_300000)
    print('{:.5f}'.format(time.time() - t0))


if __name__ == '__main__':
    main()
