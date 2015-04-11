# Python 3.4


# Input output associated functions


def lineate(file_name):
    """ (file) -> list of (int, str)

        Return list of all stripped lines in file file_name.
    """
    with open(file_name) as fin:
        lines = [line.strip() for line in fin]
        return lines


def write_results(file_name, result_tuple):
    """ (filename, list of (test case, solution)) -> NoneType

    result_tuple is a list data structure that contains tuples of every
    test case and its solution.

    i.e [(1, 2), (2, 5), (3, 100)]

    Creates a new file file_name and writes the all results from
    result_tuple in correct output format.
    """

    with open(file_name, 'a') as fout:
        for case_num, result in result_tuple:
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
    while shyness_lvl > 0:
        digit = int(s[shyness_lvl])
        if digit != 0:
            potential_standees -= digit
            if potential_standees < shyness_lvl:
                # not enough people for shyness_lvl people to applause
                possible_solutions.append(shyness_lvl - potential_standees)
        shyness_lvl -= 1

    return max(possible_solutions)


def main(input_file, output_file):
    """ (filename) -> NoneType

    Processes the file input_file and writes the solution to
    output_file.
    """
    pass
