import json
from apiSrc_entity import medicEntity
from apiSrc_repository import medicRepository
from flask import jsonify

def getAll():
    
    jsonMedicList = "["
    
    medicList = medicRepository.getAll()
    
    print(medicList)
    
    if medicList == []:
        
        return '[]'
    
    else:
    
        for i in medicList:        
            
            medicJson = json.dumps(i.__dict__)
            
            jsonMedicList = jsonMedicList + medicJson + ", "        
        
        auxConvert = list(jsonMedicList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonMedicList = "".join(auxConvert)
        
        print(jsonMedicList)
        
        return (jsonMedicList)
    
def getMedicById(id):
    
    jsonMedicList = "["
    
    medicList = medicRepository.getMedicById(id)
    
    print(medicList)
    
    if medicList == []:
        
        return '[]'
    
    else:
    
        for i in medicList:
            
            
            medicJson = json.dumps(i.__dict__)
            
            jsonMedicList = jsonMedicList + medicJson + ", "
            
        
        auxConvert = list(jsonMedicList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonMedicList = "".join(auxConvert)
        
        print(jsonMedicList)
        
        return (jsonMedicList)
    
    
def getMedicByName(name):
    
    jsonMedicList = "["
    
    medicList = medicRepository.getMedicByName(name)
    
    print(medicList)
    
    if medicList == []:
        
        return '[]'
    
    else:
    
        for i in medicList:
            
            
            medicJson = json.dumps(i.__dict__)
            
            jsonMedicList = jsonMedicList + medicJson + ", "
            
        
        auxConvert = list(jsonMedicList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonMedicList = "".join(auxConvert)
        
        print(jsonMedicList)
        
        return (jsonMedicList)



def createMedic(name, specialty, addressStreet, addressNumber, addressZip):
    
    insertResult = medicRepository.createMedic(name, specialty, addressStreet, addressNumber, addressZip)
     
    medicJson = json.dumps(insertResult)
    
    print(medicJson)
    
    return (medicJson)



def updateMedic(medicId, name, specialty, addressStreet, addressNumber, addressZip):
    
    updtMedic = medicEntity.Medic()
    
    #buscar um usuario
    getMedic = getMedicById(medicId)
    getMedic = json.loads(getMedic)
    getMedic = getMedic[0]
    
    #definir id
    updtMedic.id = medicId

    #atualizar nome
    if name != "":
        updtMedic.name = name
    else:
        updtMedic.name = getMedic["name"]
        
    #atualizar specialty
    if specialty != "":
        updtMedic.specialty = specialty
    else:
        updtMedic.specialty = getMedic["specialty"]
        
    #atualizar addressStreet
    if addressStreet != "":
        updtMedic.addressStreet = addressStreet
    else:
        updtMedic.addressStreet = getMedic["addressStreet"]
        
    #atualizar addressNumber
    if addressNumber != "":
        updtMedic.addressNumber = addressNumber
    else:
        updtMedic.addressNumber = getMedic["addressNumber"]
        
    #atualizar description
    if addressZip != "":
        updtMedic.addressZip = addressZip
    else:
        updtMedic.addressZip = getMedic["addressZip"]
        
    #jogar medicamento no banco
    return(medicRepository.updateMedic(updtMedic))
    

def deleteMedicById(id):
    
    print("id recebido: " + id)
    
    deleteReturn = medicRepository.deleteMedicById(id)
    
    print(deleteReturn)
    
    return (deleteReturn)


    
    
def getMockMedic():
    
    mockMedic = medicEntity.Medic()
    
    mockMedic.id = "12345"
    mockMedic.name = "dr. House"
    mockMedic.specialty = "Neurologista"
    mockMedic.addressStreet = "rua Teste"
    mockMedic.addressNumber = "123"
    mockMedic.addressZip = "08335728"

    return mockMedic