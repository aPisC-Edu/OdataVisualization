import numpy as np
import matplotlib.pyplot as plt
from MyOdata import Service as MyOdata

odata = MyOdata('https://oktnb132.inf.elte.hu:51006/index.xsodata/')

data = odata.query("TrendAndCyclic_1")

f1 = plt.figure()
plt.plot(data['signal_time'], data['signal_value'])
plt.plot(data['signal_time'], data['signal_wn'])
plt.plot(data['signal_time'], data['signal_4n'])

f2 = plt.figure()
plt.plot(np.sort(data['signal_value']))
plt.plot(np.sort(data['signal_wn']))
plt.plot(np.sort(data['signal_4n']))


plt.show()