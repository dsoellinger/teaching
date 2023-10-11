import numpy as np

def create_multiplication_chart(size=10):

    """
    Returns a multiplication chart for numbers in the range 1 to <size>
    """

    # Created a 2d numpy array with numbers from 1 to <size>
    factors = np.arange(size)[np.newaxis, :]

    # Use a matrix multiplication to generate the multiplication matrix.
    # Note: factors.T => Transpose of <factors>
    mult_matrix = factors * factors.T

    return mult_matrix


def print_multiplication_chart(multi_chart):

    """ 
    Takes a two-dimensional array (i.e., multiplication chart) as input and writes
    it to STDOUT (nicely formatted).
    """

    for row in multi_chart:
        print('\t'.join(map(str, row)))


multi_chart = create_multiplication_chart()
print_multiplication_chart(multi_chart)
