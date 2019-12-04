import requests
import pyodata
import math
import numpy as np
import matplotlib.pyplot as plt

# https://tuomur-python-odata.readthedocs.io/en/latest/query.html

SERVICE_URL = 'https://oktnb132.inf.elte.hu:51045/index.xsodata/'

sess = requests.session()
sess.verify = False

client = pyodata.Client(SERVICE_URL, sess)

query = client.entity_sets.TRAIN.get_entities()
#query = query.filter(query.releaseType == 'SOP')


def fetchData(query):
    dataset = []
    hasData = True
    i = 0
    while hasData:
        data = query.skip(i*100).top(100).execute()
        dataset += data
        hasData = len(data) != 0
        i+=1
    return dataset

def createDtype():
    return np.dtype( 
        [('ID', np.int32)]
        + [('CYCLE', np.int32)]
        + [('S' + str(i+1), np.float64) for i in range(3)] 
        + [('D' + format(i+1, '02d'), np.float64) for i in range(21)]
        + [('HEALTH', np.float64)]
    )

def mapObject(item, dtype) :
    return tuple(getattr(item, n) for n in dtype.names)

dtype = createDtype()

dataset = np.array([mapObject(i, dtype) for i in fetchData(query.filter(query.ID == 1).order_by('ID, CYCLE'))], dtype=dtype)


fig, axs = plt.subplots(11, 2)

for i in range(21) :
    axs[i%11, i // 11].plot(dataset["D{:02d}".format(i+1)])

axs[10, 1].plot(dataset["HEALTH"])

plt.show()