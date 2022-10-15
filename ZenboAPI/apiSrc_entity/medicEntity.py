class Medic():
    
    id = ""
    name = ""
    specialty = ""
    addressStreet = ""
    addressNumber = ""
    addressZip = ""
    
    def toString(self, medic):
        
        return("["+ medic.id +", "+ medic.name +", "+ medic.specialty +", "+ medic.addressStreet +", "+ medic.addressNumber +" ,"+ medic.addressZip+ "]")