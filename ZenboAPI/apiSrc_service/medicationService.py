import json
from apiSrc_entity import medicationEntity
from apiSrc_repository import medicationRepository
from flask import jsonify

def getAll():
    
    jsonMedicationList = "["
    
    medicationsList = medicationRepository.getAll()
    
    print(medicationsList)
    
    if medicationsList == []:
        
        return '[]'
    
    else:
    
        for i in medicationsList:        
            
            medicationJson = json.dumps(i.__dict__)
            
            jsonMedicationList = jsonMedicationList + medicationJson + ", "        
        
        auxConvert = list(jsonMedicationList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonMedicationList = "".join(auxConvert)
        
        print(jsonMedicationList)
        
        return (jsonMedicationList)
    
def getMedicationById(id):
    
    jsonMedicationList = "["
    
    medicationsList = medicationRepository.getMedicationById(id)
    
    print(medicationsList)
    
    if medicationsList == []:
        
        return '[]'
    
    else:
    
        for i in medicationsList:
            
            
            medicationJson = json.dumps(i.__dict__)
            
            jsonMedicationList = jsonMedicationList + medicationJson + ", "
            
        
        auxConvert = list(jsonMedicationList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonMedicationList = "".join(auxConvert)
        
        print(jsonMedicationList)
        
        return (jsonMedicationList)
    
    
def getMedicationByName(name):
    
    jsonMedicationList = "["
    
    medicationsList = medicationRepository.getMedicationByName(name)
    
    print(medicationsList)
    
    if medicationsList == []:
        
        return '[]'
    
    else:
    
        for i in medicationsList:
            
            
            medicationJson = json.dumps(i.__dict__)
            
            jsonMedicationList = jsonMedicationList + medicationJson + ", "
            
        
        auxConvert = list(jsonMedicationList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonMedicationList = "".join(auxConvert)
        
        print(jsonMedicationList)
        
        return (jsonMedicationList)


def createMedication(name, dosage, frequency, description):
    
    insertResult = medicationRepository.createMedication(name, dosage, frequency, description)
     
    medicationJson = json.dumps(insertResult)
    
    print(medicationJson)
    
    return (medicationJson)


def updateMedication(medicationId, name, dosage, frequency, description):
    
    updtMedication = medicationEntity.Medication()
    
    #buscar um usuario
    getMedication = getMedicationById(medicationId)
    getMedication = json.loads(getMedication)
    getMedication = getMedication[0]
    
    #definir id
    updtMedication.id = medicationId

    #atualizar nome
    if name != "":
        updtMedication.name = name
    else:
        updtMedication.name = getMedication["name"]
        
    #atualizar dosage
    if dosage != "":
        updtMedication.dosage = dosage
    else:
        updtMedication.dosage = getMedication["dosage"]
        
    #atualizar frequency
    if frequency != "":
        updtMedication.frequency = frequency
    else:
        updtMedication.frequency = getMedication["frequency"]
        
    #atualizar description
    if description != "":
        updtMedication.description = description
    else:
        updtMedication.description = getMedication["description"]
        
    #jogar medicamento no banco
    return(medicationRepository.updateMedication(updtMedication))

    
def deleteMedicationById(id):
    
    print("id recebido: " + id)
    
    deleteReturn = medicationRepository.deleteMedicationById(id)
    
    print(deleteReturn)
    
    return (deleteReturn)


def getMockMedication():
    
    mockMedication = medicationEntity.Medication()
    
    mockMedication.id = "12345"
    mockMedication.name = "Aspirina"
    mockMedication.dosage = "1 comprimido"
    mockMedication.frequency = "8h"
    mockMedication.description = "Remedio para dor"

    return mockMedication



