# Python 3.4


# Input output associated functions


def lineate(file_name):
    """ (file) -> list of str

        Return list of all stripped lines in file file_name.
    """
    with open(file_name) as fin:
        lines = [line.strip() for line in fin]
        return lines


def write_results(file_name, results_string):
    """ (filename, str) -> NoneType

        Creates a new file file_name and writes the results_string to filename.
    """

    with open(file_name, 'w') as fout:
        fout.write(results_string)

"""
    Objective: Return the minimum number of friends needed to ensue
    a standing ovation for every test case.

    Output format:
        Case #x: y
        (where x is test case number (1 - 1000)
         and y is the answer)
"""


def main(input_file, output_file):
    """ (filename) -> NoneType

    Processes the file input_file and writes the solution to
    output_file.
    """
    pass
