class Cities:
    def __init__(self ,id, name, region_id):
        self.id = id
        self.name = name
        self.region_id = region_id
        pass

@property
def id(self):
    return self._id    
@property
def name(self):
    return self._name    
@property
def region_id(self):
    return self._region_id    

@id.setter
def id(self,value):
    self._id = value
    if not isinstance(value,int):
        raise ValueError("must be a integer")