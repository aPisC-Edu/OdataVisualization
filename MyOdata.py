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
            defaultQuery = lambda _q: _q.order_by("signal_time"),
            tableName = 'CashFlows'
        )   
        self.addEntity(
            'CashFlows_2', 
            dtype1, 
            defaultQuery = lambda _q: _q.order_by("signal_value, signal_time"),
            tableName = 'CashFlows'
        )  
        self.addEntity(
            'CashFlows_Forecast', 
            np.dtype( 
                [('signal_time', "M8[D]")]
                + [('signal_value', np.float64)]
                + [('kts_1', np.float64)]
                + [('kts_1_lowerlimit_95%', np.float64)]
                + [('kts_1_upperlimit_95%', np.float64)]
            ), 
            defaultQuery = lambda _q: _q.order_by("signal_time"),
            tableName = 'CashFlowsForecast'
        )  
        self.addEntity(
            'CashFlows_Seasonality', 
            np.dtype( 
                [('signal_time', np.int32)]
                + [('seasonal', np.float64)]
                + [('trend', np.float64)]
                + [('random', np.float64)]
            ), 
            defaultQuery = lambda _q: _q.order_by("signal_time"),
            tableName = 'CashFlowsSeasonality'
        )    
        self.addEntity(
            'Ozone_1', 
            dtype1, 
            defaultQuery = lambda _q: _q.order_by("signal_time"),
            tableName = 'Ozone'
        )    
        self.addEntity(
            'Ozone_2', 
            dtype1, 
            defaultQuery = lambda _q: _q.order_by("signal_value"),
            tableName = 'Ozone'
        )   
        self.addEntity(
            'Lag1_1', 
            np.dtype( 
                [('signal_time', "M8[D]")]
                + [('signal_value', np.float64)]
                + [('signal_wn', np.float64)]
                + [('delta', np.float64)]
            ), 
            defaultQuery = lambda _q: _q.filter(_q.signal_value != "0.0d").order_by("signal_time"),
            tableName = 'Lag1'
        )   
        self.addEntity(
            'TrendAndCyclic_1', 
            np.dtype( 
                [('signal_time', "M8[D]")]
                + [('signal_value', np.float64)]
                + [('signal_wn', np.float64)]
                + [('signal_4n', np.float64)]
                + [('delta_wn', np.float64)]
                + [('delta_4n', np.float64)]
            ), 
            defaultQuery = lambda _q: _q.order_by("signal_time"),
            tableName = 'TrendAndCyclic'
        )        

        
        