import numpy as np

a = np.array([(1,2,3), (4,5,6)])

print(a.ndim) # what dimentional array

print(a.itemsize) #each element occupy size

print(a.dtype) #data type

print(a.size) # size of the array
print((a.shape)) #shape of the array 2 rows and 3 columns


#reshaping and slicing

a = np.array([(1,2,3,4), (4,5,6,7), (8,9,0,10)])

print(a.reshape(4,3)) # make into 4rows and 3 columns

print(a[0,2]) #slicing
print(a[1,0]) #slicing

print(a[0:,2]) #slicing; all rows from 0 but 2 cloumns
print(a[1:,2]) #slicing; all rows from 1 but 2 cloumns

print(a[0:2,2]) #slicing; all rows from 0 to 1 (2-1) but 2 cloumns
print(a[0:2,0:2]) #slicing; all rows from 0 to 1 (2-1) but 0 to 1 cloumns


b = np.linspace(1, 3, 5) # return 5 elements between 1, 3
print(b)

b = np.linspace(1, 5, 10) # return 10 elements between 1, 5
print(b)

#min and max , agg operation

a = np.array([1, 3, 4, 54, 3, 2, 4])

print(a.min())
print(a.max())
print(a.sum())

# axis

a = np.array([(1, 3, 4, 54, 3, 2, 4), (11, 13, 14, 154, 13, 12, 14)])

print(a.sum(axis=0)) # columns
print(a.sum(axis=1)) # rows

# Square and standard deviation

a = np.array([(1, 3, 4, 54, 3, 2, 4), (11, 13, 14, 154, 13, 12, 14)])

print(np.sqrt(a)) # square root of elements
print(np.std(a)) # standard deviation from mean

#arithmatic operation

a = np.array([(11, 13, 14, 14, 15, 12, 14), (11, 13, 14, 154, 13, 12, 14)])
b = np.array([(21, 33, 34, 34, 35, 32, 34), (41, 43, 44, 454, 43, 42, 44)])

print(a+b) # addition
print(a-b) # sub
print(a*b) # mul
print(a/b) # div


#concat - vertical stacking and horizantal stacking

print(np.vstack((a, b))) #() is important
print(np.hstack((a, b))) #() is important

a = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])
# make it single dimention array
print(a.ravel())

