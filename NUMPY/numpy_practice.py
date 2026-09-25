import numpy as np

# arr=np.array([1,2,3,4])
# print(arr)
# print(arr.ndim)
# print(arr.shape)
# [1 2 3 4]
# (4,) >>> this tuple indicates that it is a one dimensional array with 4 elements



# an arrayb containing single row of elements can be considered as one-dimensional-array
# we can check the dimension using ndim
# eg:print(arr.ndim)


# 2-Dimensional Array
# ================

# arr_2=np.array([[1,2,3,4],[5,6,7,8]])

# an array containing more than one rows(rows and columns)like a table format
# can be termed as 2-Dimensional array

# print(arr_2)
# print(arr_2.ndim)
# print(arr_2.shape)

# [[1 2 3 4]
#  [5 6 7 8]]
# 2
# (2, 4) >>> indicates 2d array with 2 rows and 3 columns


# 3-Dimensional Array
# =====================

# an array contains multiple 2 dimensional arrays

# arr_3=np.array([[[1,2,3,4],[5,6,7,8]],
#                 [[1,2,3,4],[5,6,7,8]],
#                 [[1,2,3,4],[5,6,7,8]]])

# print(arr_3)
# print(arr_3.ndim)
# print(arr_3.shape)

# [[[1 2 3 4]
#   [5 6 7 8]]

#  [[1 2 3 4]
#   [5 6 7 8]]

#  [[1 2 3 4]
#   [5 6 7 8]]]
# 3
# (3, 2, 4) >>>indicates 3 2-d arrays each having 2 rows and 4 columns


# zero matrix
# ============

# matrix with all elements being zeros
# np.zeros(shape,dtype)

# matrix=np.zeros((3,4),int)
# print(matrix)

# one matrix
# ==========
# matrix in which all elements are 1
# matrix_1=np.ones(shape=(3,5),dtype=int)
# print(matrix_1)


# Full Matrix
# ============

# create a matrix with all elements being a specific value
# print(np.full(shape=(3,4),fill_value=4,dtype=int))


# Identity matrix
# =================

# the matrix where no of rows=no of columns
# diagonal elements should be 1 and other elements filled with 0
# n = >>represents no. of rows and columns
# print(np.identity(n=3,dtype=int))

# print(np.eye(N=3,dtype=int))
# both gives same identity matrix but eye() is 
# used where we may need to modify the identity matrix


# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr.shape)

# print(arr.reshape(2,4))
"""
[1 2 3 4 5 6 7 8]

1 2 3 4 
5 6 7 8

"""

# arr_2=np.array([i for i in range(1,9)])
# print(arr_2)#[1 2 3 4 5 6 7 8]

# arr_3=np.arange(1,9)
# print(arr_3)#[1 2 3 4 5 6 7 8]

# print(np.arange(1,9).reshape(2,4).ndim) #2

# print(arr_3.flatten())#[1 2 3 4 5 6 7 8]
# convert 2d or 3d array into 1d array



# Arithemtic operations in array
# =================================

a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array([[9,12,5,13],[8,16,3,11]])
print(a,b)
print(a+b)


# [[1 2 3 4]
#  [5 6 7 8]] 

# [[ 9 12  5 13]
#  [ 8 16  3 11]]

# [[10 14  8 17]
#  [13 22 10 19]]

print(a-b)

# [[ -8 -10  -2  -9]
#  [ -3 -10   4  -3]]

print(a*b)

# [[ 9 24 15 52]
#  [40 96 21 88]]

print(a/b)

# [[0.11111111 0.16666667 0.6        0.30769231]
#  [0.625      0.375      2.33333333 0.72727273]]

print(a*2)
# [[ 2  4  6  8]
#  [10 12 14 16]]

"""
list1=[1,2,3,4]
print(list1*2)#[1, 2, 3, 4, 1, 2, 3, 4]
for i in range(len(list1)):
    list1[i]=list1[i]*2
print(list1)#[2, 4, 6, 8]

instead of this array uses vectors ...so it is 
faster and need only few lines of code

"""
print(a+3)
#[[ 4  5  6  7]
# [ 8  9 10 11]]


print(a**3)
#[[  1   8  27  64]
# [125 216 343 512]]

print(np.add(a,b))
# [[10 14  8 17]
#  [13 22 10 19]]

print(np.subtract(a,b))
# [[ -8 -10  -2  -9]
#  [ -3 -10   4  -3]]

print(np.multiply(a,b))
# [[ 9 24 15 52]
#  [40 96 21 88]]

print(np.divide(a,b))
# [[0.11111111 0.16666667 0.6        0.30769231]
#  [0.625      0.375      2.33333333 0.72727273]]

print(np.sqrt(a))
# [[1.         1.41421356 1.73205081 2.        ]
#  [2.23606798 2.44948974 2.64575131 2.82842712]]

print(np.square(a))
# [[ 1  4  9 16]
#  [25 36 49 64]]


a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array([[4,3,2,1],[6,7,5,4]])

print(a+b)
# print(a*2)        This is called vector calculation>>>all elements mul by 2 and retirn in a new array
print(a**2)

""" 
[[ 5  5  5  5]
 [11 13 12 12]]

[[ 2  4  6  8]
 [10 12 14 16]]

[[ 1  4  9 16]
 [25 36 49 64]]

"""
print(a%2)
# [[1 0 1 0]
#  [1 0 1 0]]

print(np.sum(a))#36 add all elements in the array and return sum
print(np.sum(a,axis=0))#[ 6  8 10 12] return sum of elements in column wise
print(np.sum(a,axis=1))#[10 26] return row wise sum



a=np.array([2,4,3,5,7,1])
print(np.sort(a))#[1 2 3 4 5 7] arrange elements in ascending order
print(np.sort(a)[::-1])#[7 5 4 3 2 1] arrange elements in descending order


# slicing
# ==========
# arrayname[row_start:row_stop:step,column_Start:column_stop:step]

array=np.arange(1,21).reshape(5,4)
print(array)

"""
   0  1  2  3
0[ 1  2  3  4] 
1[ 5  6  7  8]
2[ 9 10 11 12]
3[13 14 15 16]
4[17 18 19 20]
"""
print(array[2:4,1::])
"""
[[10 11 12]
 [14 15 16]]
"""

print(array[1:4,1:3])

"""
[[ 6  7]
 [10 11]
 [14 15]]
"""

a=np.array([10,3,5,9,12])
print(np.argsort(a))#[1 2 3 0 4] return the index position that would sort the array
print(np.argsort(a)[::-1])#[4 0 3 2 1]
print(np.argmax(a))#4 return index of largest element in the array
                    #for a 2d array it flattens then retuns the index position
print(np.argmin(a))#1 return index of smallest element in the array


b=np.array([[3,10,11],[2,5,1],[6,10,4]])
print(b)
"""
[ 3 10 11]
[ 2  5  1]
[ 6 10  4]
"""

print(np.argmax(b))#2
print(np.argmax(b,axis=0))#[2 0 0]
print(np.argmax(b,axis=1))#[2 1 1]


# where
# =======

# find the position of elements that satisfy a condition
# replace all elememnts

# np.where(condition,value_if_true,value_if_false)

arr=np.array([10,30,15,8,20,43])
print(np.where(arr>=15))#(array([1, 2, 4, 5]),)



b=np.array([[3,10,11],[2,5,1],[6,10,4]])
"""
[ 3 10 11]
[ 2  5  1]
[ 6 10  4]
"""
print(np.where(b>5))#(array([0, 0, 2, 2]), array([1, 2, 0, 1]))
"""
first given is row indes and second given is column index

 so 01>>10
    02>>20
    20>>6
    21>>10
"""
print(np.where(b>5,"pass","fail"))
"""
[['fail' 'pass' 'pass']
 ['fail' 'fail' 'fail']
 ['pass' 'pass' 'fail']]
"""

b=np.array([[3,10,11],[2,5,1],[6,10,4]])
"""
[ 3 10 11]
[ 2  5  1]
[ 6 10  4]
"""
print(np.sort(b))
# [[ 3 10 11]
#  [ 1  2  5]
#  [ 4  6 10]]
print(np.sort(b)[::-1])
# [[ 4  6 10]
#  [ 1  2  5]
#  [ 3 10 11]]
# print(np.sort(b)[-1::])


arr=np.array([[30,10,20],[60,40,50],[90,70,80]])
print(arr[:,0:2])
"""
[[30 10]
 [60 40]
 [90 70]]
"""
print(arr[0:2,:])
"""
[[30 10 20]
 [60 40 50]]
"""
print(arr[::-1,:])
"""
[[90 70 80]
 [60 40 50]
 [30 10 20]]
"""

print(arr)
"""
[[30 10 20]
 [60 40 50]]
[[90 70 80]
"""
print(np.sort(arr))

"""
[[10 20 30]
 [40 50 60]
 [70 80 90]]
"""
print(np.sort(arr)[::-1,:])
"""
[[70 80 90]
 [40 50 60]
 [10 20 30]]
"""
print(np.sort(arr)[:,::-1])
"""
[[30 20 10]
 [60 50 40]
 [90 80 70]]
"""
print(np.sort(arr)[::-1,::-1])#fulldescending order
"""
[[90 80 70]
 [60 50 40]
 [30 20 10]]
"""

array1=np.array([[3,6,1],[5,2,9],[3,8,7]])
print(np.sort(array1)[::-1,::-1])
"""
[[8 7 3]
 [9 5 2]
 [6 3 1]]
"""
array2=np.array([1.67,2.5,3.75,4.65])
print(np.round(array2,decimals=1))#[1.7 2.5 3.8 4.6]
# round the number to nearest integer

print(np.floor(array2))#[1. 2. 3. 4.]
# floor the decimal numbers to largest number <= the number


print(np.ceil(array2))#[2. 3. 4. 5.] 
# rounds each value upto the nearest greatest or equal integer(moving towards ppositive infinity)


