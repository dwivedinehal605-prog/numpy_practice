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
#creat numpy arrays with random numbers
# 1. random array elements between 0 and 1
import numpy as np
ar_rand=np.random.rand(5) # 1D array with 5 random elements
print(ar_rand)
ar_rand2=np.random.rand(2,3) # 2D array with 2 rows and 3 columns
print(ar_rand2)
# 2. generate ramndom value close tozero. this may be positive or negative.
ar_randn=np.random.randn(5) # 1D array with 5 random elements
print(ar_randn)
# 3.doing random sampling, it return an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0).
ar_randf=np.random.ranf((2,3)) 
print(ar_randf)
# 4.generate a random number between a given range
ar_randint=np.random.randint(1,10,5) # 5 random integers between 1 and 10
print(ar_randint)

# Lecture 6
# Data types in numpy array
# find data type of array elements
import numpy as np
var=np.array([2,3,5,6])
print("data type: ",var.dtype)# .dtype is used to find data type of array elements. 
var1=np.array([1.2,4.5,3.4,5.2])
print("data type: ",var1.dtype)
var2=np.array(["a","b","h","d"])
print("data type: ",var2.dtype)
var3=np.array(["a","b","h","r",[1,3,5,6]],dtype=object)
print("data type: ",var3.dtype)
# conversion of data type
x=np.array([1,2,3,4],dtype=np.float64)# here we are converting integer array to float array.
print(x)
x1=np.array([1,2,3,4],dtype="uint32")# converting integer into unsighned integer.
# conversion of datatypes as a function.
x1=np.array([1,2,3,4])
new=np.float64(x1)
print("data type: ",x1.dtype)
print("data type: ",new.dtype)
print(x1)
print(new)

# Lecture 7
#Arithmetic operations in numpy array
# for 1D array
import numpy as np
var=np.array([1,2,3,4])
var_add1=var+3 # here we are adding 3 to each element of the array. this is called broadcasting in numpy.
var_add2=var-3
var_add3=var*3
var_add4=var/3
print(var_add1)
print(var_add2)
print(var_add3)
print(var_add4)

var1=np.array([1,2,3,4])
var2=np.array([1,2,3,4])
var_add=var1+var2 #here we are adding two arrays element-wise. this is also called broadcasting in numpy.
var_add=np.add(var1,var2) # addition of two arrays using numpy function.
print(var_add)
print(var_add)
# for 2D array
var1=np.array([[1,2,3,4],[1,2,3,4]])
var2=np.array([[1,3,5,6],[1,3,5,7]])
var_multiply=var1*var2
print(var_multiply)



