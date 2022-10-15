import json
from apiSrc_entity import appointmentEntity, treatmentEntity
from apiSrc_repository import appointmentRepository

def getAppointment(userId):
    
    jsonMedicationList = "["
    
    appointmentList = appointmentRepository.getAppointmentsById(userId)
    
    print(appointmentList)
    
    if appointmentList == []:
        
        return '[]'
    
    else:
    
        for i in appointmentList:
            
            
            medicationJson = json.dumps(i.__dict__)
            
            jsonMedicationList = jsonMedicationList + medicationJson + ", "
            
        
        auxConvert = list(jsonMedicationList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonAppointmentList = "".join(auxConvert)
        
        print(jsonAppointmentList)
        
        return (jsonAppointmentList)
    
def getAppointmentWithDate(userId, date):
    
    jsonMedicationList = "["
    
    appointmentList = appointmentRepository.getAppointmentWithDate(userId, date)
    
    print(appointmentList)
    
    if appointmentList == []:
        
        return '[]'
    
    else:
    
        for i in appointmentList:
            
            
            medicationJson = json.dumps(i.__dict__)
            
            jsonMedicationList = jsonMedicationList + medicationJson + ", "
            
        
        auxConvert = list(jsonMedicationList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonAppointmentList = "".join(auxConvert)
        
        print(jsonAppointmentList)
        
        return (jsonAppointmentList)
    
def getAppointmentWeek(userId):
    
    jsonMedicationList = "["
    
    appointmentList = appointmentRepository.getAppointmentWeek(userId)
    
    print(appointmentList)
    
    if appointmentList == []:
        
        return '[]'
    
    else:
    
        for i in appointmentList:
            
            
            medicationJson = json.dumps(i.__dict__)
            
            jsonMedicationList = jsonMedicationList + medicationJson + ", "
            
        
        auxConvert = list(jsonMedicationList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonAppointmentList = "".join(auxConvert)
        
        print(jsonAppointmentList)
        
        return (jsonAppointmentList)

def getTreatment(id):
    
    jsonMedicationList = "["
    
    appointmentList = appointmentRepository.getTreatmentById(id)
    
    print(appointmentList)
    
    if appointmentList == []:
        
        return '[]'
    
    else:
    
        for i in appointmentList:
            
            i.data_inicio = i.data_inicio.strftime("%Y-%m-%d")  
            i.data_fim = i.data_fim.strftime("%Y-%m-%d")  
            i.last_occurrence = i.last_occurrence.strftime("%Y-%m-%d")  
            
            medicationJson = json.dumps(i.__dict__)
            
            jsonMedicationList = jsonMedicationList + medicationJson + ", "
            
        
        auxConvert = list(jsonMedicationList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonAppointmentList = "".join(auxConvert)
        
        print(jsonAppointmentList)
        
        return (jsonAppointmentList)

def createAppointment(user, hora, data, hospital, medic, descricao):
    
    insertResult = appointmentRepository.createAppointment(user, hora, data, hospital, medic, descricao)
     
    appointmentJson = json.dumps(insertResult)
    
    print(appointmentJson)
    
    return (appointmentJson)

def createTreatment(user, medication, data_inicio, data_fim, last_occurrence, medic, descricao, monitorado, atendido):
    
    insertResult = appointmentRepository.createTreatment(user, medication, data_inicio, data_fim, last_occurrence, medic, descricao, monitorado, atendido)
     
    treatmentJson = json.dumps(insertResult)
    
    print(treatmentJson)
    
    return (treatmentJson)


def updateAppointment(appointmentId, user, hora, data, hospital, medic, descricao):
    
    updtAppointment = appointmentEntity.Appointment() 
    
    #buscar um usuario
    getAppointmentAux = getAppointment(appointmentId)
    getAppointmentAux = json.loads(getAppointmentAux)
    getAppointmentAux = getAppointmentAux[0]
    
    #definir id
    updtAppointment.id = appointmentId
    
    #atualizar user
    if user != "":
        updtAppointment.user = user
    else:
        updtAppointment.user = getAppointmentAux["user"]

    #atualizar hora
    if hora != "":
        updtAppointment.hora = hora
    else:
        updtAppointment.hora = getAppointmentAux["hora"]
        
    #atualizar data
    if data != "":
        updtAppointment.data = data
    else:
        updtAppointment.data = getAppointmentAux["data"]
        
    #converter a data
    updtAppointment.data = dataConverter(updtAppointment.data)
                
    #atualizar hospital
    if hospital != "":
        updtAppointment.hospital = hospital
    else:
        updtAppointment.hospital = getAppointmentAux["hospital"]
        
    #atualizar medic
    if medic != "":
        updtAppointment.medic = medic
    else:
        updtAppointment.medic = getAppointmentAux["medic"]
        
    #atualizar descricao
    if descricao != "":
        updtAppointment.descricao = descricao
    else:
        updtAppointment.descricao = getAppointmentAux["descricao"]
        
    #jogar appointment no banco
    return(appointmentRepository.updateAppointment(updtAppointment)) 

    
def updateTreatment(treatmentId, user, medication, data_inicio, data_fim, last_occurrence, medic, descricao, monitorado, atendido):

    updtTreatment = treatmentEntity.Treatment()
    
    #buscar um usuario
    getTreatmentAux = getTreatment(treatmentId)
    getTreatmentAux = json.loads(getTreatmentAux)
    getTreatmentAux = getTreatmentAux[0]

    #definir id
    updtTreatment.id = treatmentId

    #atualizar user
    if user != "":
        updtTreatment.user = user
    else:
        updtTreatment.user = getTreatmentAux["user"]
        
    #atualizar medication
    if medication != "":
        updtTreatment.medication = medication
    else:
        updtTreatment.medication = getTreatmentAux["medication"]
        
    #atualizar data_inicio
    if data_inicio != "":
        updtTreatment.data_inicio = data_inicio
    else:
        updtTreatment.data_inicio = getTreatmentAux["data_inicio"]
        
    #atualizar data_fim
    if data_fim != "":
        updtTreatment.data_fim = data_fim
    else:
        updtTreatment.data_fim = getTreatmentAux["data_fim"]
        
    #atualizar last_occurrence
    if last_occurrence != "":
        updtTreatment.last_occurrence = last_occurrence
    else:
        updtTreatment.last_occurrence = getTreatmentAux["last_occurrence"]
        
    #atualizar medic
    if medic != "":
        updtTreatment.medic = medic
    else:
        updtTreatment.medic = getTreatmentAux["medic"]
        
    #atualizar descricao
    if descricao != "":
        updtTreatment.descricao = descricao
    else:
        updtTreatment.descricao = getTreatmentAux["descricao"]
        
    #atualizar monitorado
    if monitorado != "":
        updtTreatment.monitorado = monitorado
    else:
        updtTreatment.monitorado = getTreatmentAux["monitorado"]
        
    #atualizar atendido
    if atendido != "":
        updtTreatment.atendido = atendido
    else:
        updtTreatment.atendido = getTreatmentAux["atendido"]  
        
    #jogar treatment no banco
    return(appointmentRepository.updateTreatment(updtTreatment))

def deleteAppointmentById(id):
    
    print("id recebido: " + id)
    
    deleteReturn = appointmentRepository.deleteAppointmentById(id)
    
    print(deleteReturn)
    
    return (deleteReturn)

def deleteTreatmentById(id):
    
    print("id recebido: " + id)
    
    deleteReturn = appointmentRepository.deleteTreatmentById(id)
    
    print(deleteReturn)
    
    return (deleteReturn)

def dataConverter(data):
    
    dia = data[0:2]
    ano = data[len(data) - 4:len(data)]
    mes = data[3:len(data) - 5]
    
    meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    if (meses.index(mes) + 1) > 9:
        mes = str(meses.index(mes) + 1)
    else:
        mes = '0' + str(meses.index(mes) + 1)
    
    return (ano +"-"+ mes +"-"+ dia)
    



