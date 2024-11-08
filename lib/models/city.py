class City:
    #@classmethod create table here
    all_cities = []
    def __init__(self, name, region_id, id=None):
        self.id = id
        self.name = name
        self.region_id = region_id
        # type(self).all_cities.append(self)
        
    @property
    def name(self):
        return self._name
        
    @property
    def region_id(self):
        return self._region_id    

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("must be of type string")
        elif not 3 <= len(value) <=50: 
            #  elif not (3<= len(value) <=50):
             raise ValueError("must be between 3 and 50 characters")
        self._name = value
    
    @region_id.setter
    def region_id(self,value):
        if not isinstance(value,int):
            raise ValueError("must be a integer")
        #(find by) elif not region.findby(region_id) (ex we only have 5 regions, but someone looks for region_id 10)
        self._region_id = value
    