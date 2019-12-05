class EntityDefinition(object):
    def __init__(self, tableName, dtype, query = None):
        self.tableName = tableName
        self.dtype = dtype
        self.query = query