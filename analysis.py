import random
import time
import matplotlib.pyplot as plt
from pprint import pprint
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort import shell_sort

def generate_arrays(size: int):
    """
    generate an array with random numbers (5 experiments)
            array with sorted numbers, descending order
            array with sorted numbers, ascending order
            array contains only three elements from the set {1,2,3} (3 experiments)
    """
    rand_numbers_arr = [[random.random() for _ in range(size)] for _ in range(5)]
    sorted_nums_ascend_arr = [[el for el in range(size)]]
    sorted_nums_descend_arr = [[el for el in range(size, 0, -1)]]
    three_el_arr = [[random.choice([1, 2, 3]) for _ in range(size)] for _ in range(3)]

    return [rand_numbers_arr, sorted_nums_ascend_arr, sorted_nums_descend_arr, three_el_arr]


def run_algorithms():
    size = 2**7
    algorithms = [selection_sort, insertion_sort, merge_sort, shell_sort]
    data = {
        "selection_sort": {},
        "insertion_sort": {},
        "merge_sort": {},
        "shell_sort": {}
    }
    # for every arr length, there are 5 possible lengths
    for _ in range(5):
        # generate arrays
        # test_arrays = generate_arrays(size)

        for algo in algorithms:
            test_arrays = generate_arrays(size)
            for case in range(len(test_arrays)):
                sorting_time = []
                for arr in test_arrays[case]:
                    start = time.time()
                    algo(arr)
                    end = time.time() - start
                    sorting_time.append(end)
                
                avg_time = sum(sorting_time) / len(sorting_time)
                write_info(data, algo.__name__, size, case, avg_time)
                print("finnished working with", algo.__name__, case)
        
        print("finnished working for length: ", size)
        size *= 4
        print("new size to work with: ", size)
        print()

    return data


def write_info(data, algo_name, arr_size, test_case, time):
    """
    Structure of data
    {
        algo_name: {
            size: {
                test_case1: time,
                test_case2: time,
                ...
            }
        }
    }
    """
    if not arr_size in data[algo_name]:
        data[algo_name][arr_size] = {}
    data[algo_name][arr_size][test_case] = time


def get_case_info(data: dict, case: int):
    """
    get info for making a diagram
    for every algo and array length, get specific case,
    form list of lists where each list contains running time for each algorithm
    for each size of array.
    """
    # array for keeping running times for different algos for a spesific case
    case_running_times_for_algorithms = {}
    for algo in data:
        case_running_time = []
        for arr_size in data[algo]:
            case_running_time.append(data[algo][arr_size][case])
        case_running_times_for_algorithms[algo + str(case)] = case_running_time
    
    return case_running_times_for_algorithms


def build_diagrams():
    data = run_algorithms()

    arr_size = [2**7, 2**9, 2**11, 2**13, 2**15]

    for case in range(4):
        case_data = get_case_info(data, case)

        # pprint(case_data)

        plt.xlabel("arr length")
        plt.ylabel("execution time")
        for algorithm in case_data:
            plt.plot(arr_size, case_data[algorithm], label=algorithm[:-1])
        plt.yscale("log")
        plt.xscale("log")
        plt.legend()
        plt.title("case " + str(case))
        plt.show()



if __name__ == '__main__':
    # data = run_algorithms()
    # pprint(data)
    build_diagrams()