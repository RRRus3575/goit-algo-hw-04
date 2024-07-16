import random
import timeit

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Функція для порівняння алгоритмів сортування
def compare_sorting_algorithms():
    sizes = [100, 1000, 10000]  
    results = []

    for size in sizes:
        array = [random.randint(0, 10000) for _ in range(size)]
        print(f"Testing with array size: {size}")

        array_insertion = list(array)
        array_merge = list(array)
        array_timsort = list(array)

        # Час сортування вставками
        insertion_time = timeit.timeit(lambda: insertion_sort(array_insertion), number=1)
        print(f"Insertion sort time for size {size}: {insertion_time}")

        # Час сортування злиттям
        merge_time = timeit.timeit(lambda: merge_sort(array_merge), number=1)
        print(f"Merge sort time for size {size}: {merge_time}")

        # Час Timsort 
        timsort_time = timeit.timeit(lambda: sorted(array_timsort), number=1)
        print(f"Timsort time for size {size}: {timsort_time}")

        results.append((size, insertion_time, merge_time, timsort_time))

    return results

compare_sorting_algorithms()

#Timsort є найбільш ефективним алгоритмом сортування серед трьох, оскільки він поєднує в собі переваги сортування злиттям і вставками. 
# Це робить його швидким та ефективним як для великих, так і для майже відсортованих масивів, що і є причиною використання цього алгоритму в Python. 
# Програмісти часто покладаються на вбудовані функції сортування саме через їх оптимізовану продуктивність та надійність.

#Results:

# Testing with array size: 100
# Insertion sort time for size 100: 0.00040579999949841294
# Merge sort time for size 100: 0.0003114000010100426     
# Timsort time for size 100: 1.9999999494757503e-05  
#      
# Testing with array size: 1000
# Insertion sort time for size 1000: 0.049375399999917136
# Merge sort time for size 1000: 0.004144299999097711
# Timsort time for size 1000: 0.001797499999156571

# Testing with array size: 10000
# Insertion sort time for size 10000: 4.660787200000414
# Merge sort time for size 10000: 0.059191500000451924
# Timsort time for size 10000: 0.0029281999995873775