from numpy import genfromtxt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# load the dataset
dataset = genfromtxt(
    'Data/PM_train.csv', 
    delimiter=';',
    names=["id", "cycle", "s1", "s2", "s3", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13", "d14", "d15", "d16", "d17", "d18", "d19", "d20", "d21", "d22", "d23"]
    )




cycles = (np.bincount(dataset['cycle'].tolist())[1:])
print(cycles)

fig, axs = plt.subplots(11, 2)

for i in range(22) :
    axs[i%11, i // 11].plot(dataset[dataset['id'] == 2]["d" + str(i+1)])

plt.show()