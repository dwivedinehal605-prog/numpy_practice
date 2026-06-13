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

# Lecture 8
# Arithmetic functions in numpy array
import numpy as np
var=np.array([1,4,3,9])
print("max: ",np.max(var),np.argmax (var)) # find maximum element in the array and its index.
print("min: ",np.min(var),np.argmin(var)) # find minimum element in the array and its index.
print("sqrt: ",np.sqrt(var)) # find square root of each element in the array.
# for 2D array
var2=np.array([[4,7,1],[5,8,7]])
print("min value along column: ",np.min(var2,axis=0)) # find minimum element in each column.
print("min value along row: ",np.min(var2,axis=1)) # find minimum element in each row.
var3=np.array([4,6,2,7])
print("sin value: ",np.sin(var3)) # find sine value of each element in the array.
print("cos value: ",np.cos(var3)) # find cosine value of each element in the array.
print("cumulative sum: ",np.cumsum(var3)) # find cumulative sum of the array elements.

# Lecture 9
# Shape and Reshaping of numpy array
import numpy as np
var=np.array([[1,2,3],[4,5,6]])
print(var)
print("shape: ",var.shape) # find shape of the array.
var1=np.array([1,2,3,4,5,6],ndmin=4) # here we are creating a 4D array with 6 elements.
print(var1)
print(var1.ndim) # find dimension of the array.
var=np.array([4,6,3,9,5,7])
print(var.ndim)
var2=var.reshape(3,2) # here we are reshaping the array from 2D to 3D. the total number of elements should be same.
print("reshaped array: ",var2)
print(var2.ndim)

# Lecture 10
# Broadcasting in numpy array
import numpy as np
var1=np.array([1,2,3,4])
var2=np.array([1,2,3,4])
var_add=var1+var2 # here we are adding two arrays element-wise. this is called broadcasting in numpy.
print("1st array: ",var1)
print("2nd array: ",var2)
print("sum of both array: ",var_add)

# Lecture 11
# Numpy arrays indexing and slicing
#INDEXING
# 1. for 1D array
import numpy as np
var=np.array([1,2,3,4,5])
# indexing    0,1,2,3,4
# -ive indexing -5,-4,-3,-2,-1
print("1D array: ",var)
print("value of index 3: ",var[3]) # access fourth element of the array.
print("value of index -3: ",var[-3]) # access third element of the array.
# 2. for 2D array
var2=np.array([[1,2,3],[4,5,6]])
print("2D array: ",var2)
print("value of index [0][2]: ",var2[0][2]) # access first row and third column element of the array.
print("value of index [1][0]: ",var2[1][0]) # access second row and first column element of the array.
# 3. for 3D array
var=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3D array: ",var)
print("value of [0,1,1]: ",var[0,1,1]) # access first block, second row and second column element of the array.
print("value of [1,0,2]: ",var[1,0,2]) # access second block, first row and third column element of the array.
#SLICING
#Parameter for slicing is [start:stop:step]
# 1. for 1D array
var=np.array([1,2,3,4,5])
# index no.   0,1,2,3,4
print("1D array: ",var)
print("slicing from index 1 to 4: ",var[1:4]) # access elements from index 1 to 3.
print("slicing from start to end: ",var[:]) # access all elements of the array.
print("slicing with step size 2: ",var[::2]) # access elements with step size 2.
# 2. for 2D array
var2=np.array([[1,2,3,5,8],[4,5,6,7,9]])
print("2D array: ",var2)
print("slicing second row: ",var2[1,:]) # access all columns of the second row.
print("slicing first column: ",var2[:,0]) # access all rows of the first column.
print("get subarray by slicing: ",var2[0:2,1:4]) # access first two rows and columns from index 1 to 3.

# Lecture 12
# Numpy iteration arrays (nditer function)
# 1. for 1D array
import numpy as np
var=np.array([3,4,7,9,2,8])
print("1D array: ",var)
print("print iteration of 1D array")
for i  in var: 
    print(i) # here we are iterating through each element of the array.   
# 2. for 2D array
var2=np.array([[1,2,3],[4,5,6]])
print("2D array: ",var2)
print("print iteration of 2D array through each row")
for i in var2:
    print(i) # here we are iterating through each row of the array. 

print("print iteration of 2D array through each element")
for k in var2:
    for j in k:
        print(j) # here we are iterating through each element of the array. 

print("iterate again by using nditer function")
for i in np.nditer(var2): # here we are iterating through each element of the array by using nditer function. it is more efficient than nested for loop.
        print(i)

print("iterate with index by using ndenumerate function")
for i,d in np.ndenumerate(var2): # here we are iterating through each element of the array with its index by using ndenumerate function.
    print(i,d) # i is the index and d is the value of the element at that index.

# Lecture 13
#copy vs view in numpy array
import numpy as np
var=np.array([1,2,3,4,5])
co=var.copy() # here we are creating a copy of the array. it is a new array with same values as original array but it is stored in different memory location. any change in copy array will not affect original array.
var[1]=100
print("original array: ",var)
print("copy of the original array: ",co) # here we are creating a copy of the array. it is a new array with same values as original array but it is stored in different memory location. any change in copy array will not affect original array.

x=np.array([1,2,3,4,5])
vi=x.view() # here we are creating a view of the array. it is not a new array but it is just a reference to the original array. any change in view array will affect original array.
x[1]=200
print("original array: ",x)
print("view of the original array: ",vi) # here we are creating a view of the array. it is not a new array but it is just a reference to the original array. any change in view array will affect original array.
print()
# Lecture 14
# Join and splint functions of numpy array.
# Join array
# 1. for 1D array
import numpy as np
var1=np.array([3,4,6,9])
var2=np.array([6,2,8,1])
ar=np.concatenate((var1,var2))
print("var1: ",var1)
print("var2 :",var2)
print("concatination: ",ar)
print()
# 2. for 2D array
var1=np.array([[3,4,6,9],[5,6,9,3]])
var2=np.array([[6,2,8,1],[5,2,8,5]])
ar=np.concatenate((var1,var2))
print("var1: ",var1)
print("var2 :",var2)
print("concatination along with both row and colunm: ",ar) # here it concatenate along with axis-0(colunm) and axis-1(row) of array.
print()

var1=np.array([[3,4,6,9],[5,6,9,3]])
var2=np.array([[6,2,8,1],[5,2,8,5]])
ar=np.concatenate((var1,var2),axis=1)# it will concatenate along with row.
print("var1: ",var1)
print("var2 :",var2)
print("concatenate along with row: ",ar)
print()

var1=np.array([[3,4,6,9],[5,6,9,3]])
var2=np.array([[6,2,8,1],[5,2,8,5]])
ar=np.concatenate((var1,var2),axis=0)# it will concatenate along with colunm.
print("var1: ",var1)
print("var2 :",var2)
print(" concatenate along with colunm: ",ar)
print()
# merging array using stack function.
var1=np.array([[3,4,6,9],[5,6,9,3]])
var2=np.array([[6,2,8,1],[5,2,8,5]])
ar1=np.stack((var1,var2))# merge along both row and colunm.
ar2=np.hstack((var1,var2))# merge along row.
ar3=np.vstack((var1,var2))# merge along colunm.
ar4=np.dstack((var1,var2))# merge along height.
print("var1: ",var1)
print("var2 :",var2)
print("merge array by using stack function: ",ar1)
print("merge array horizontally(row): ",ar2)
print("merge array vertically(colunm): ",ar3)
print("merge array along with height: ",ar4)
print()
#Splint array
# 1. 1D array
import numpy as np
var=np.array([4,6,9,3])
print("1D array: ",var)
ar=np.array_split(var,2)
print("splited array: ",ar)
print("datatype of splited array: ",type(ar))
print("access specified array[1]: ",ar[1])
print()
# 2. for 2D array
var=np.array([[3,4,5,6],[8,9,1,2]])
print("2D array: ",var)
ar=np.array_split(var,2)
ar=np.array_split(var,2,axis=1) #split along axis.
print("splite 2D array along axis: ",ar)
print()

# Lecture 15
# Numpy arrays function.
# 1. Search(search an array for a certain value, and return the indexes that get a match)
import numpy as np
var=np.array([3,5,7,8,7,9])
print("array: ",var)
x=np.where(var==7) # here it will find 7 and return it's index value.
print("search 7: ",x)
print()
# 2. Search sorted array(it performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.)
var1=np.array([2,4,6,7,8,9])
print("array: ",var1)
x1=np.searchsorted(var1,3) # it will return the index value of where 3 will insert so that it would be in sorted order.
x2=np.searchsorted(var1,[1,3,5],side="right")
print("give index value of [3]: ",x1)
print("give index value of [1,3,5]: ",x2)
print()
# 3. sort(Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical,ascending or descending.)
var2=np.array([2,4,1,6,7,8,5,13,9])
print("array: ",var2)
print("sorted array: ", np.sort(var2))

var3=np.array(["f","j","a","t","c","e"])
print("array: ",var3)
print("sorted array: ", np.sort(var3))
print()

var2=np.array([[2,4,1,6],[7,8,5,13]])
print("2D array: ",var2)
print("sorted 2D array: ", np.sort(var2))
print()
# 4. Filter array(Getting some elements out of an existing array and creating a new array out of then)
var4=np.array(["f","t","a","r","c","y"])
print("array: ",var4)
f=[True,False,True,True,False,False]
new_var4=var4[f]
print("Filtered array: ",new_var4)
print(type(new_var4))
print()

# Lecture 16
# Numpy array functions(shuffle,unique,resize,flatten,ravel)
# 1. Shuffle
import numpy as np
var=np.array([3,4,5,6,7])
print("array: ",var)
np.random.shuffle(var)
print("shuffled array: ",var)
# 2. Unique
var=np.array([3,4,3,5,4,6,5,1,1,7])
print("array: ",var)
x=np.unique(var) #it will return unique values.
print("unique element of array: ",x)
print()
x1=np.unique(var,return_index=True)
print("index of unique element: ",x1)
print()
x2=np.unique(var,return_counts=True)
print("count repitition of unique element: ",x2)
print()
# 3.Resize
var1=np.array([3,4,3,5,4,6,5,1,1])
print("array: ",)
x=np.resize(var1,(3,3))
print("Resized array: ",x)
print()
# 4. Flatten(convert nD array into 1D array)
var1=np.array([[3,4,3],[5,4,6],[5,1,1]])
print("array: ",var1)
print("flattened array: ",var1.flatten()) # it will convert nD array into 1D array.
print("flattened array in C-style(row): ",var1.flatten(order="C")) # "C" means to flatten in row major(C-style) order.
print("flattened array in fortan style(column) : ",var1.flatten(order="F")) #"F" means to flatten in coumn major(fortan style) order 
print()
# 5. Ravel(converts nD array into 1D array)
var2=np.array([[3,4,3],[5,4,6],[5,1,1]])
print("array: ",var2)
print("Ravel: ",np.ravel(var2))
print("Ravel order 'A': ",np.ravel(var2,order="A"))
print("Ravel order 'F': ",np.ravel(var2,order="F"))
print("Ravel order 'K': ",np.ravel(var2,order="K"))
print("Ravel order 'C': ",np.ravel(var2,order="C"))
print()

# Lecture 17
# Numpy insert and delete arrays function.
# 1. for 1D array. 
import numpy as np
var=np.array([4,5,8,2,5])
print("1D array: ",var)
v1=np.insert(var,3,50) # insert(arrayname,position,value)
v2=np.insert(var,(3,4),50)
v3=np.insert(var,(3,4),8.9) #it will not accept float value.
print("insert 50 in the array: ",v1)
print("insert 50 in the array: ",v2)
print("insert 8.9 in the array: ",v3)
print("it will not accept float value")
print()
# for 2D array. 
var_2=np.array([[3,4,5],[7,3,8]])
v4=np.insert(var_2,2,10,axis=0) # insert(arrayname,position,value,axis)
v5=np.insert(var_2,2,10,axis=1) 
v6=np.insert(var_2,2,[10,6],axis=1)# insert multiple values.
v7=np.insert(var_2,2,[10,5,8],axis=0) 
print("2D array:",var_2)
print("insert value in 2D array along axis=0:",v4)
print("insert value in 2D array along axis=1:",v5)
print("insert multiple value in 2D array along axis=1:",v6)
print("insert multiple value in 2D array along axis=1:",v7)
print()
# insert data through append function.
# for 1D array.
var=np.array([4,5,8,2,5])
print("1D array: ",var)
x=np.append(var,6.5)
print("append value in 1D array: ",x)
print()
# for 2D array.
var_2=np.array([[3,4,5],[7,3,8]])
print("2D array:",var_2)
x1=np.append(var_2,[[65,78,43]],axis=0)
print("append multiple value in 1D array: ",x1)
print()
# Delete function.
# for 1D array.
var=np.array([4,5,8,2,5])
print("1D array: ",var)
d=np.delete(var,2)
print("delete perticular value from array:",d)
