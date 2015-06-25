# Python 3.4

# Input output associated functions


def lineate(file_name):
    """ (file) -> list of (int, str)

        Return list of all stripped lines in file file_name.
    """
    with open(file_name) as fin:
        lines = [line.strip() for line in fin]
        return lines


def write_results(file_name, results):
    """ (filename, list of solution) -> NoneType

    results contains every test case solution.

    i.e [2, 5, 100]

    Creates a new file file_name and writes the all results from
    results in correct output format.
    """

    with open(file_name, 'w') as fout:
        for i in range(len(results)):
            fout.write('Case #{}: {}\n'.format(i + 1, results[i]))

""" Infinte House of Pancakes

    Objective: Find the minimal time for customers to finish all pancakes.

    Two modes:
        Normal: 1 pancake per minute
        Special: Move any number of pancakes from one diner to another.

    Assume we have a set of diners with non-empty plates,
    P_0 P_1 P_2 ... P_D at time T and I remove A pancakes from diner
    P_k, P_k >= A > 0 to a empty diner. Then the new time to consume
    all pancakes shall be max(P_k - A, A, P_0 ... P_k-1, P_k+1 ... P_D) + 1 + T

    From this we can deduce:
        Move iff P_k > 3
        Always try to remove half the pancakes when moving.
        Always remove from the largest stack of pancakes first.
        Always call special minutes first.
"""


def insert(lst, item):
    """ (list, int) -> Nonetype

    Inserts int item into list lst, such that lst remains reverse sorted.

    Precondition: nearly reverse sorted.
    """
    i = 0
    while i < len(lst) and item < lst[i]:
        i += 1
    lst.insert(i, item)


def solve_test_case(input_list, sort=True, time_elapsed=0):
    """ (list of int) -> str

    Return the solution to the input input_list. This is done using simple
    recursion.

    >>> solve_test_case([1, 2, 1, 2])
    3
    """
    if sort:
        input_list.sort(reverse=True)
    finish_time = input_list[0] + time_elapsed

    if input_list[0] <= 3:
        return finish_time

    a = input_list[0] // 2
    b = input_list[0] - a
    del input_list[0]
    insert(input_list, a)
    insert(input_list, b)
    return min(finish_time, solve_test_case(input_list, False, time_elapsed + 1))


def main(input_file, output_file):
    """ (filename) -> NoneType

    Processes the file input_file and writes the solution to
    output_file.
    """
    test_cases = lineate(input_file)
    result_tuples = []

    for case in test_cases[::2][1:]:
        test_string = case
        # make the test_string more manipulable
        input_case = [int(val) for val in test_string.split()]
        result_tuples.append(solve_test_case(input_case))

    write_results(output_file, result_tuples)

if __name__ == '__main__':
    main('B-small-attempt3.in.txt', 'B_small_result.txt')
