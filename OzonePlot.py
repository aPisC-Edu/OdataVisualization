import numpy as np
import matplotlib.pyplot as plt
from MyOdata import Service as MyOdata

odata = MyOdata('https://oktnb132.inf.elte.hu:51006/index.xsodata/')

data1 = odata.query("Ozone_1")
data2 = odata.query("Ozone_2")

f1 = plt.figure()
plt.plot(data1['signal_time'], data1['signal_value'], 'b-')

f2 = plt.figure()
plt.plot(data2['signal_value'])


plt.show()