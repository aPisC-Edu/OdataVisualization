import OdataHandler.Service as _Service
import numpy as np
import requests

class Service(_Service):
    def __init__(self, url):
        session =  requests.session()
        session.verify = False
        
        _Service.__init__(self, url, session)

        dtype1 = np.dtype( 
            [('signal_time', "M8[D]")]
            + [('signal_value', np.float64)]
        )

        self.addEntity(
            'CashFlows_1',
            dtype1 , 
            defaultQuery = lambda _q: _q.filter(_q.signal_value != "0.0d").order_by("signal_time"),
            tableName = 'CashFlows'
        )   
        self.addEntity(
            'CashFlows_2', 
            dtype1, 
            defaultQuery = lambda _q: _q.filter(_q.signal_value != "0.0d").order_by("signal_value, signal_time"),
            tableName = 'CashFlows'
        )    
        self.addEntity(
            'Ozone_1', 
            dtype1, 
            defaultQuery = lambda _q: _q.filter(_q.signal_value != "0.0d").order_by("signal_time"),
            tableName = 'Ozone'
        )    
        self.addEntity(
            'Ozone_2', 
            dtype1, 
            defaultQuery = lambda _q: _q.filter(_q.signal_value != "0.0d").order_by("signal_value"),
            tableName = 'Ozone'
        )        
        