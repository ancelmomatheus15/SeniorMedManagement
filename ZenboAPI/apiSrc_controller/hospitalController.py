from apiSrc_service import hospitalService

def getAll():
    
    results = hospitalService.getAll()
    
    return results

def getHospitalById(id):

    results = hospitalService.getHospitalById(id)

    return results

def getHospitalByName(name):
    
    results = hospitalService.getHospitalByName(name)

    return results

def createHospital(name, addressStreet, addressNumber, addressZip):
    
    results = hospitalService.createHospital(name, addressStreet, addressNumber, addressZip)
    
    return results

def updateHospital(hospitalId, name, addressStreet, addressNumber, addressZip):
        
    results = hospitalService.updateHospital(hospitalId, name, addressStreet, addressNumber, addressZip)
    
    return results 

def deleteHospitalById(id):
    
    results = hospitalService.deleteHospitalById(id)

    return results