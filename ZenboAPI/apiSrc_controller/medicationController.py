from apiSrc_service import medicationService

def getAll():
    
    results = medicationService.getAll()
    
    return results

def getMedicationById(id):

    results = medicationService.getMedicationById(id)

    return results

def getMedicationByName(name):
    
    results = medicationService.getMedicationByName(name)

    return results

def createMedication(name, dosage, frequency, description):
        
    results = medicationService.createMedication(name, dosage, frequency, description)
    
    return results


def updateMedication(medicationId, name, dosage, frequency, description):
        
    results = medicationService.updateMedication(medicationId, name, dosage, frequency, description)
    
    return results 

def deleteMedicationById(id):
    
    results = medicationService.deleteMedicationById(id)

    return results
    