import numpy as np

#Using numpy we created an array with 15 random elements
a= np.random.randint(1,20,15)
print("Random array \n", a)

#Reshape the array to 3 by 5
b= np.reshape(a, [3, 5])
print("Reshaped array: \n", b)
print("Shape: ", b.shape)

#Replace the max in each row by 0
for i in b:
    i[i == max(i)] = 0

print("Replacing max in each row by 0 \n", b)