"""You can install nodemon to watch for file changes.
npm i -g nodemon
Then to use:
nodemon --exec python3 hello.py"""


"Creating Arrays" 

import numpy as np
#print(np.__version__)
L = list(range(10))
print(L)
print("\n")

# Converting integers to string: List Comprehension
print([str(c) for c in L])
print("\n")

print([type(item) for item in L])
print("\n")


# Creating an array
print("\n")
print(np.zeros(10, dtype='int'))

# Create a 3 row x 5 column matrix
print("\n")
print(np.ones((3,5), dtype=float))

# creating a matrix with a predefined value
print("\nCreating a matrix with a predefined value")
print(np.full((3,5), 1.23))

# Create an array with a set sequence
print("\nCreate an array with a set sequence")
print(np.arange(0, 20, 2))

#create an array of even space between the given range of values
print("\nCreate an array of even space between the given range of values")
print(np.linspace(0, 1, 5))

# Create a 3x3 array with mean 0 and standard deviation 1 in a given dimension
print("\nCreate a 3x3 array with mean 0 and standard deviation 1 in a given dimension")
print(np.random.normal(0,1, (3,3)))

# Create an identity matrix
print("\nCreate an identity matrix")
print(np.eye(3))

# Set a random seed
print("\nSet a random seed")
np.random.seed(3)

x1 = np.random.randint(10, size=6) #one dimension
x2 = np.random.randint(10, size=(3,4)) #two dimension
x3 = np.random.randint(10, size=(3,4,5)) #three dimension


print("x3 ndim:", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)

"Array Indexing"
# Important thing to remember in Python is that indexing starts at zero!

x1 = np.array([4,3,4,4,8,4])
print("\nArray Indexing", x1)

# Assess first value to index zero, fifth and get the last + second last value
print(x1[0])
print(x1[4])
print(x1[-1])
print(x1[-2])

# Specify a multidimensional array 
x2 = np.array([[3, 7, 5, 5],
      [0, 1, 5, 9],
      [3, 0, 5, 0]])

print("\nMultidimensional Array\n", x2)

# Get the 1st row and 2nd col value!
print(x2[2,3])

# 3rd Row and last value from the 3rd col
print(x2[2,-1])

# replace the value at 0,0 index
x2[0,0] = 12
print(x2)

"""Array Slicing"""
print("\nArray Slicing\n")

x = np.arange(10)
print(x)

# From start to 4th position
print(x[:5])

# From 4th position to end
print(x[4:])

# Return elements at even place in index of array
print("\nReturn elements at even place in index of array")
print(x[ : : 2])

# Return elements from first position step by two!
print("\nReturn elements from first position step by two!")
print(x[1::2])

print("\nReverse the Array!")
print(x[::-1])

""" Array Concatenation """

print("\nYou can concate multiple arrays together!")
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [21,21,21]
print(np.concatenate([x,y,z]))

print("\nCan also make a 2D array ")
grid = np.array([[1,2,3],[4,5,6]])
print(np.concatenate([grid, grid]))

print("\nUsing its axis parameters, you can define row-wise or column-wise matrix!")
print(np.concatenate([grid, grid], axis = 1))

# What if you are required to combine a 2D array with 1D array? In such situations, np.concatenate might not be the best option to use.
# Instead, you can use np.vstack or np.hstack to do the task.
print("2D and a 1D array concatenation, use np.vstack!")
x = np.array([3,4,5])
print("\n1D Array: ", x)
grid = np.array([[1,2,3,],[17,18,19]])
print("\n2D Array: \n", grid)
print("\nConcatenation : \n", np.vstack([x, grid]))

# Similarly, you can add an array using np.hstack
print("\nSimilarly, you can add an array using np.hstack\n")

z = np.array([[9],[9]])
print(np.hstack([grid,z]))

# Also, we can split the arrays based on pre-defined positions.
print("\nAlso, we can split the arrays based on pre-defined positions.\n")

x = np.arange(10)
x1,x2,x3 = np.split(x,[3,6])
print(x1,x2,x3)

grid = np.arange(16).reshape((4,4))
print("\n", grid)

upper,lower = np.vsplit(grid,[2])
print("\nUpper:\n", upper, "\nLower:\n", lower)

