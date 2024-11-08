class Region:
    all_regions = []
    def __init__(self,id, name):
        self.id = id
        self.name = name
        Region.all_regions.append(self)
    

    @property
    def id(self):
        return self._id  
    @property
    def name(self):
        return self._name 
      

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
             raise ValueError("must be between 5 and 50 characters")  
        elif hasattr(self, "_name"): 
            raise AttributeError("this is unique")  
        self._name = value
        # self._name = value (validation checks are always at the end)
        