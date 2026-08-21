import numpy as np

array=np.array([[10,25,30,45],
                [15,20,35,40],
                [50,60,55,70],
                [80,75,90,65]])

print(array)
print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)
print(array[1,2])
print(array[0])
print(array[-1])
print(array[:,0:1])
print(array[0:2,1:3])
print(np.sum(array))
print(np.max(array))
print(np.min(array))
print(np.sum(array,axis=1))
print(np.sum(array,axis=0))
print(np.argmax(array))
print(np.argmin(array))
print(np.sort(array,axis=1))
print(np.argsort(array,axis=1))
print(np.square(array))
print(np.sqrt(array))
print(np.round(array))
print(np.cumsum(array))
print(array.reshape(2,8))
