""" ## Exercise 1: NumPy: Create an array with values ranging from 12 to 38 """
import numpy as np
def create_array_with_range(range_start:int=12,range_end:int=38):
    numpy_array_store=np.arange(range_start,range_end,1)
    print(numpy_array_store)


create_array_with_range()


###Exercise 2: Add a border around an existing array###