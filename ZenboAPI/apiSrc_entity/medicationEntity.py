class Medication():
    
    id = ""
    name = ""
    dosage = ""
    frequency = ""
    description = ""
    
    def toString(self, medication):
        
        return("["+ str(medication.id) +", "+ medication.name +", "+ medication.dosage +", "+ medication.frequency +", "+ medication.description +"]")