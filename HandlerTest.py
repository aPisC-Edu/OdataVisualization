import numpy as np
import matplotlib.pyplot as plt
from MyOdata import Service as MyOdata

odata = MyOdata('https://oktnb132.inf.elte.hu:51006/index.xsodata/')

qn = "Ozone_2"

data = odata.query(qn)

f1 = plt.figure()


if qn == "CashFlows_1":
    plt.plot(data['signal_time'], data['signal_value'], 'b-')
if qn == "Ozone_1":
    plt.plot(data['signal_time'], data['signal_value'], 'b-')

if qn == "CashFlows_2":
    plt.plot(data['signal_value'] )
if qn == "Ozone_2":
    plt.plot(data['signal_value'] )



plt.show()