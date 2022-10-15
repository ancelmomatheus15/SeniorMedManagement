from apiSrc_service import medicService

def getAll():
    
    results = medicService.getAll()
    
    return results

def getMedicById(id):

    results = medicService.getMedicById(id)

    return results

def getMedicByName(name):
    
    results = medicService.getMedicByName(name)

    return results

def createMedic(name, specialty, addressStreet, addressNumber, addressZip):
        
    results = medicService.createMedic(name, specialty, addressStreet, addressNumber, addressZip)
    
    return results

def updateMedic(medicId, name, specialty, addressStreet, addressNumber, addressZip):
        
    results = medicService.updateMedic(medicId, name, specialty, addressStreet, addressNumber, addressZip)
    
    return results 

def deleteMedicById(id):
    
    results = medicService.deleteMedicById(id)

    return results