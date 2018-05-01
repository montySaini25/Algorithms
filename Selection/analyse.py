import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading data generated by algorithm [input_size,comparisons]
data = pd.read_csv("selection_analysis.csv",header = None,names = [0,1])

data.head()
#sorting data according to input_size so to make a smooth curve
data.sort_values(by = [0] , inplace = True)

#calculating lower and upper bounds of algorithm
log = np.log2(data[0])
nlog= data[0]*log

nsqre = data[0] ** 2

#time for the magic. i.e. Graphical representaion
plt.plot(data[0], data[1], '-r', label = "comp")
plt.plot(data[0],nlog, '-b', label = "nlogn")
plt.plot(data[0],data[0], '-g', label = "n")
plt.plot(data[0],nsqre,'-c',label = "nsquare")
plt.legend()

plt.show()
