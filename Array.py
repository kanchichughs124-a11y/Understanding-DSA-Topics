# 1. Creating and printing an array
# Import everything from Python's array module
from array import *

# Create an array containing integer numbers from 1 to 9
# 'i' means the array stores signed integers
val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])


# len(val) tells us how many elements are in the array
# range(0, len(val)) gives indexes from 0 to 8
for i in range(0, len(val)):
    # val[i] gets the element at index i
    # end=" " prints elements on the same line with spaces
    print(val[i], end=" ")


# Print a new line
print('\n')

# This loop directly takes each element from the array
# We don't need indexes when we only want to read elements
for x in val:
    # Print each element followed by a comma and a space
    print(x, end=', ')

# Print a new line
print('\n')

# Print the array's type code
# The output is 'i', which means signed integers
print(val.typecode)










# 2. Reversing and inserting elements

from array import *

# Create an array
val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Print the type of elements stored in the array
print(val.typecode)

# Reverse the array
# The first element becomes the last, and the last becomes the first
val.reverse()

# Print the reversed array
for i in range(0, len(val)):
    print(val[i], end=" ")

print()  # Move to the next line

# Insert 50 at index 1 (the second position)
# Existing elements shift one position to the right
val.insert(1, 50)

# Print the array after inserting 50
for i in range(0, len(val)):
    print(val[i], end=" ")











#3. Inserting, appending and changing an element


from array import *

# Create the original array
val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Insert 50 at index 1 (the second position)
val.insert(1, 50)

# Add 100 at the end of the array
val.append(100)

# Change the element at index 2 to 200
# Index 2 contains 2 before this statement runs
val[2] = 200

# Print all elements of the updated array
for i in range(0, len(val)):
    print(val[i], end=" ")














# #4. Creating a new array by multiplying each element by 2

from array import *

# Create the original array
val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Create a new array called copyArray
# val.typecode uses the same integer type as the original array
# for x in val takes each number from the original array
# x * 2 multiplies each number by 2
# The original array remains unchanged
copyArray = array(val.typecode, (x * 2 for x in val))

# Print every element of the new array
for i in range(0, len(val)):
    print(copyArray[i], end=" ")

