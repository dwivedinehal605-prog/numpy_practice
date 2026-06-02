# Lecture 1
import numpy as np
# creat a array
x = np.array([1, 2, 3])
print(x)
print(type(x))
#creat a list
y=[1,2,3,4]
print(y)
print(type(y))

#Lecture 2
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

# Lecture 3
#creating arrays in numpy
# 1. using array function
import numpy as np
x=[1,2,3,4]
y=np.array(x)
print(y)
print(type(y))
# 2. by taking user input
l=[]
for i in range(1,5):
    int_1=int(input("enter a number: "))
    l.append(int_1)
y=np.array(l)
print(y)
print(y.ndim)# check dimension of array
#creating 2D array
ar2=np.array([[1,2,3],[4,5,6]])# no. of elements in each list should be same 
print(ar2)
print(ar2.ndim)
# creating 3D array
ar3=np.array([[[1,2,3],[1,2,3],[1,2,3]]])
print(ar3)
print(ar3.ndim)
# creating n dimensional array
arn=np.array([1,2,3,4],ndmin=10)
print(arn)
print(arn.ndim)

# Lecture 4
# creating numpy array using numpy function
# 1.arrey filled with 0's
import numpy as np
ar_zeros=np.zeros(5) #1D array with 5 elements
print(ar_zeros)
print()
ar_zeros2=np.zeros((2,3)) # 2D array with 2 rows and 3 columns
print(ar_zeros2)
# 2. array filled with 1's
ar_one=np.ones(4)
print(ar_one)
# 3.creat an empty array
ar_emp=np.empty(4)
print(ar_emp) #here we will get previous value of memory location.
# 4.creat an array with a range of values
ar_range=np.arange(4)
print(ar_range)
ar_range2=np.arange(1,10,2) # here 1 is starting point, 10 is ending point and 2 is step size.
print(ar_range2)
# 5. create array diagonally filled with 1's
ar_diag=np.eye(4) # 
print(ar_diag)
ar_diag2=np.eye(4,k=1) # here k is the diagonal above the main diagonal.        
print(ar_diag2)
# 6.create an array with values equally spaced between a given range
ar_lin=np.linspace(0,20,5) # 5 values equally spaced between 0 and 20
print(ar_lin)

#Lecture 5