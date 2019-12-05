import requests
import pyodata
import numpy
from .EntityDefinition import EntityDefinition

_mapper = {
    "float64" : {
        '0.0d': float('nan')
    }
}

def _mapvalue(type, value):
    if type.name in _mapper:
        if value in _mapper[type.name]:
            return _mapper[type.name][value]
    return value

def _mapItem(i, dtype):
    return tuple(_mapvalue(dtype[n] , getattr(i, n)) for n in dtype.names)

class Service(object):

    entities = {}
    def __init__(self, url, session = None):
        self.session = session if session is not None else requests.session()
        self._client = pyodata.Client(url, self.session)
    
    def addEntity(self, name, dtype, tableName = None, defaultQuery = None):
        if tableName is None:
            tableName = name
        self.entities[name] = EntityDefinition(tableName, dtype, defaultQuery);
        
    def query(self, entityName, filterQuery = None):
        entity = self.entities[entityName]
        dtype = entity.dtype
        
        _q = getattr(self._client.entity_sets, entity.tableName).get_entities()

        if entity.query is not None:
            _q = entity.query(_q)

        if filterQuery is not None:
            _q = filterQuery(_q)

        rawData = self._fetchData(_q)

        return numpy.array( 
            [ _mapItem(i, dtype) for i in rawData ], 
            dtype=dtype 
        )
    
    def _fetchData(self, _q):
        _t = _q._top
        _s = _q._skip
        if(_s is None) :
            _s = 0
        dataset = []
        hasData = True
        i = 0
        while hasData:
            if (_t is not None) and i >= _t:
                break
            r = 100
            if (_t is not None) and _t - i < 100:
                r = _t - i

            data = _q.skip(_s + i).top(r).execute()
            dataset += data
            hasData = len(data) != 0
            i+=len(data)
        return dataset
