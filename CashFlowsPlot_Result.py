import numpy as np
import matplotlib.pyplot as plt
from MyOdata import Service as MyOdata

odata = MyOdata('https://oktnb132.inf.elte.hu:51006/index.xsodata/')

data1 = odata.query("CashFlows_Forecast")
data2 = odata.query("CashFlows_Seasonality")

f1 = plt.figure()
plt.title('Forecast Cash Flows')
plt.xlabel('Time')
plt.ylabel('Value')

plt.plot(data1['signal_time'], data1['signal_value'], label='Original')
plt.plot(data1['signal_time'], data1['kts_1'], label='Forecasted')
plt.plot(data1['signal_time'], data1['kts_1_lowerlimit_95%'])
plt.plot(data1['signal_time'], data1['kts_1_upperlimit_95%'])
plt.legend()

f2 = plt.figure()
plt.title('Seasonality Test')
plt.xlabel('Time')
plt.ylabel('Value')
plt.plot(data2['signal_time'], data2['seasonal'], label='Seasonal')
plt.plot(data2['signal_time'], data2['trend'], label='Trend')
plt.plot(data2['signal_time'], data2['random'], label='Random')
plt.legend()

plt.show()