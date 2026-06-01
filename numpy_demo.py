import numpy as np
# creat a array
x = np.array([1, 2, 3])
print(x)
print(type(x))
#creat a list
y=[1,2,3,4]
print(y)
print(type(y))
# list can store multiple data types, numpy array uses only one datatype.
# numpy array use less memory and fast as compare to list.
# numpy array work as a matrix and perform efficiently with numerical operation.

# check who consume less time, numpy array/list python.
# functions (%timeit ->for one line, %%timeit -> for program).
# for list
import timeit
execution_time = timeit.timeit('[j**4 for j in range(1,9)]',
                 number = 100000
               )
print(execution_time)
# for numpy array
import numpy as np
import timeit
result = timeit.timeit("np.arange(1,9)**4",globals=globals(),
        number = 100000 )
print(result)