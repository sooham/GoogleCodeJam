# Python 3.4


# Input output associated functions


def lineate(file_name):
    """ (file) -> list of (int, str)

        Return list of all stripped lines in file file_name.
    """
    with open(file_name) as fin:
        lines = [line.strip() for line in fin]
        return lines


def write_results(file_name, result_tuples):
    """ (filename, list of (test case, solution)) -> NoneType

    result_tuples is a list data structure that contains tuples of every
    test case and its solution.

    i.e [(1, 2), (2, 5), (3, 100)]

    Creates a new file file_name and writes the all results from
    result_tuple in correct output format.
    """

    with open(file_name, 'w') as fout:
        for case_num, result in result_tuples:
            fout.write('Case #{}: {}\n'.format(case_num, result))

"""
    Objective: Return the minimum number of friends needed to ensue
    a standing ovation for every test case.

    Output format:
        Case #x: y
        (where x is test case number (1 - 1000)
         and y is the answer)
"""

# Simple observation reveals as follows:
# let d_0 d_1 d_2 ... d_n be the test case string with maximum shyness n.
#
# (1) people with shyness k stand implies people with shyness k-1 stand
# (2) people with shyness k stand implies sum(d_(k-1)...d_0) >= k
# (3) sum(d_(k-1)..d_0) < k implies people with shyness k will not stand up

# we can posit a mathematical theory
# if sum(d_0...d_(k-1)) >= k
# and all people of shyness k-1 stand up
# then d_k people will stand up.
# we develop a algorithm from this theory


def solve_test_case(s):
    """ (str) -> str

    Returns the solution to test case s.

    >>> solve_test_case(110011)
    '2'
    >>> solve_test_case(000000)
    '0'
    """

    possible_solutions = []  # holds the extra friends needed if (3) is false
    shyness_lvl = len(s) - 1
    potential_standees = sum((int(digit) for digit in s))
    # Assume even the most shy people applause (standing ovation)
    while shyness_lvl >= 0:
        digit = int(s[shyness_lvl])
        if digit != 0:      # will work correctly for len 1 strings
            potential_standees -= digit
            possible_solutions.append(shyness_lvl - potential_standees)
        shyness_lvl -= 1

    return max(possible_solutions)


def main(input_file, output_file):
    """ (filename) -> NoneType

    Processes the file input_file and writes the solution to
    output_file.
    """
    test_cases = lineate(input_file)
    num_test_cases = int(test_cases[0])
    result_tuples = []

    i = 1

    for i in range(1, num_test_cases + 1):
        _, test_string = test_cases[i].split()
        result_tuples.append((i, solve_test_case(test_string)))

    write_results(output_file, result_tuples)

if __name__ == '__main__':
    main('A-small-attempt0.in.txt', 'results_A_small.txt')
