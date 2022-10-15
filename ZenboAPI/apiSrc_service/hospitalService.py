import json
from apiSrc_entity import hospitalEntity
from apiSrc_repository import hospitalRepository

def getAll():
    
    jsonHospitalList = "["
    
    hospitalList = hospitalRepository.getAll()
    
    print(hospitalList)
    
    if hospitalList == []:
        
        return '[]'
    
    else:
    
        for i in hospitalList:        
            
            hospitalJson = json.dumps(i.__dict__)
            
            jsonHospitalList = jsonHospitalList + hospitalJson + ", "        
        
        auxConvert = list(jsonHospitalList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonHospitalList = "".join(auxConvert)
        
        print(jsonHospitalList)
        
        return (jsonHospitalList)


def getHospitalById(id):
    
    jsonHospitalList = "["
    
    hospitalList = hospitalRepository.getHospitalById(id)
    
    print(hospitalList)
    
    if hospitalList == []:
        
        return '[]'
    
    else:
    
        for i in hospitalList:
            
            
            hospitalJson = json.dumps(i.__dict__)
            
            jsonHospitalList = jsonHospitalList + hospitalJson + ", "
            
        
        auxConvert = list(jsonHospitalList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonHospitalList = "".join(auxConvert)
        
        print(jsonHospitalList)
        
        return (jsonHospitalList)


def getHospitalByName(name):
    
    jsonHospitalList = "["
    
    hospitalList = hospitalRepository.getHospitalByName(name)
    
    print(hospitalList)
    
    if hospitalList == []:
        
        return '[]'
    
    else:
    
        for i in hospitalList:
            
            
            hospitalJson = json.dumps(i.__dict__)
            
            jsonHospitalList = jsonHospitalList + hospitalJson + ", "
            
        
        auxConvert = list(jsonHospitalList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonHospitalList = "".join(auxConvert)
        
        print(jsonHospitalList)
        
        return (jsonHospitalList)

def createHospital(name, addressStreet, addressNumber, addressZip):
    
    insertResult = hospitalRepository.createHospital(name, addressStreet, addressNumber, addressZip)
     
    hospitalJson = json.dumps(insertResult)
    
    print(hospitalJson)
    
    return (hospitalJson)


def updateHospital(hospitalId, name, addressStreet, addressNumber, addressZip):
    
    updtHospital = hospitalEntity.Hospital()
    
    #buscar um usuario
    getHospital = getHospitalById(hospitalId)
    getHospital = json.loads(getHospital)
    getHospital = getHospital[0]
    
    #definir id
    updtHospital.id = hospitalId

    #atualizar nome
    if name != "":
        updtHospital.name = name
    else:
        updtHospital.name = getHospital["name"]
        
    #atualizar dosage
    if addressStreet != "":
        updtHospital.addressStreet = addressStreet
    else:
        updtHospital.addressStreet = getHospital["addressStreet"]
        
    #atualizar frequency
    if addressNumber != "":
        updtHospital.addressNumber = addressNumber
    else:
        updtHospital.addressNumber = getHospital["addressNumber"]
        
    #atualizar description
    if addressZip != "":
        updtHospital.addressZip = addressZip
    else:
        updtHospital.addressZip = getHospital["addressZip"]
        
    #jogar medicamento no banco
    return(hospitalRepository.updateHospital(updtHospital))

    

def deleteHospitalById(id):
    
    print("id recebido: " + id)
    
    deleteReturn = hospitalRepository.deleteHospitalById(id)
    
    print(deleteReturn)
    
    return (deleteReturn)



def getMockHospital():
    
    mockHospital = hospitalEntity.Hospital()
    
    mockHospital.id = "12345"
    mockHospital.name = "Santa Marcelina"
    mockHospital.addressStreet = "rua Teste"
    mockHospital.addressNumber = "123"
    mockHospital.addressZip = "08334756"
    
    return mockHospital
    
    