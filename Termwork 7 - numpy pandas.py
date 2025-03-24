'''Create a Python program for the following exercises by using

Numpy and pandas.
 Create an identity matrix.
 Find the square root of each element in an array.
 Sort an array.
 Square each element in an array.
 Take logs of each element in an array.
 Create an array of zeros. Create an array of ones.
 Find the mean of array.
 Create two data frames and merge them.'''

import numpy as np
import pandas as pd

# 1. Create an identity matrix
identity_matrix = np.eye(4)  # 4x4 Identity Matrix
print("Identity Matrix:\n", identity_matrix)

# 2. Find the square root of each element in an array
arr = np.array([4, 9, 16, 25, 36])
sqrt_arr = np.sqrt(arr)
print("\nSquare root of array elements:\n", sqrt_arr)

# 3. Sort an array
unsorted_arr = np.array([12, 5, 3, 19, 8])
sorted_arr = np.sort(unsorted_arr)
print("\nSorted Array:\n", sorted_arr)

# 4. Square each element in an array
squared_arr = np.square(arr)
print("\nSquared Array:\n", squared_arr)

# 5. Take logs of each element in an array
log_arr = np.log(arr)
print("\nLog of Array Elements:\n", log_arr)

# 6. Create an array of zeros and an array of ones
zeros_arr = np.zeros((3, 3))  # 3x3 array of zeros
ones_arr = np.ones((3, 3))    # 3x3 array of ones
print("\nArray of Zeros:\n", zeros_arr)
print("\nArray of Ones:\n", ones_arr)

# 7. Find the mean of an array
mean_value = np.mean(arr)
print("\nMean of Array:\n", mean_value)

# 8. Create two data frames and merge them
data1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
data2 = {'ID': [2, 3, 4], 'Score': [85, 90, 75]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on='ID', how='outer')  # Merge on 'ID'
print("\nMerged DataFrame:\n", merged_df)
