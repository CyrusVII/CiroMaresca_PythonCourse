import numpy as np
arr = np.linspace(0,1,5)
print(arr)

random_arr = np.random.rand(3,3)
#matrice 3x3 con valori casuali uniformi
print(random_arr)


arr1 = np.array([1,2,3,4,5])

sum_value = np.sum(arr1)
mean_value = np.mean(arr1)
std_value = np.std(arr1)

print("Sum: ", sum_value )# 15
print("Mean: ", mean_value )# 3.0
print("Std: ", std_value )# 1.4142135623730951