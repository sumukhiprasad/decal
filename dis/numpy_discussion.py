import numpy as np

# make a function that takes in an array. Reshape the array so that it tbecomes a swuare matrix. FInally reverse the multi-dimensional array and return it.

# extra think aout what kind of arrays can be inputted

def reverseArray(arr):
    """
    np.random.seet(12345)
    myArr = np.random.randint(0, 10, size=(9))
    myArr
    array([2, 5, 1, 4, 9, 5, 2, 1 6])
    reverseArrau(myArr)
    array([6, 1, 2],
          [5, 9, 4],
          [1, 5, 2]))
    """
    newArr = np.reshape(arr, (len(arr)**(1/2)), len(arr)**(1/2)) # the first part of this input passes in the array we have defined for the function above, the second one dictates the size of the array we want... this needs to be inputted as a tuple (row, column)
    return newArr[::-1, ::-1]


def uniqueCounts(myArr):
    """"""
    arr = np.