class Cities:
    all_cities = []
    def __init__(self ,id, name, region_id):
        self.id = id
        self.name = name
        self.region_id = region_id
        Cities.all_cities.append(self)
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
        if not isinstance(value,int):
            raise ValueError("must be a integer")
        self._id = value
        # self._id = value (validation checks are always at the end)
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("must be of type string")
        elif not 5<= len(value) <=50: 
            #  elif not (5<= len(value) <=50):
             raise ValueError("must be between 5 and 50 characters")
        self._name = value
    
    @region_id.setter
    def id(self,value):
        if not isinstance(value,int):
            raise ValueError("must be a integer")
        self._region_id = value
    