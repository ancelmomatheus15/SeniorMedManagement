class Hospital():
    
    id = ""
    name = ""
    addressStreet = ""
    addressNumber = ""
    addressZip = ""
    
    def toString(self, hospital):
        
        return("["+ hospital.id +", "+ hospital.name +", "+ hospital.addressStreet +", "+ hospital.addressNumber +" ,"+ hospital.addressZip+ "]")