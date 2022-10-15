import flask
from flask import request
from apiSrc_controller import userController, medicationController, hospitalController, medicController, appointmentController, zenboController

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#API Home=============================================================================

#Home API
@app.route('/', methods=['GET'])
def home():
    
    pagina = htmlPage
    
    return pagina

#User Functions=======================================================================

#Busca todos os usuarios disponiveis
#127.0.0.1:5000/api/data/users/all
@app.route('/api/data/users/all', methods=['GET'])
def getUsers():
    return userController.getUsers()

#busca usuarios com base no id
#param -> id
#127.0.0.1:5000/api/data/users/id?id=0
@app.route('/api/data/users/id', methods=['GET'])
def getUsersById():
    
    id = ""
    
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return userController.getUsersById(id)

#registra um novo usuario
#/api/data/users/create
#{
#    "name" : "",
#    "birthDate" : "",
#    "city" : "",
#    "country" : "",
#    "gender" : "",
#    "phone" : "",
#    "mail" : ""
#} 
@app.route('/api/data/users/create', methods=['POST'])
def createUser():
    
    request_data = request.get_json()
    
    if 'name' and 'birthDate' and  'city' and 'country' and 'gender' and  'phone' and 'mail' in request_data:
        
        name = request_data['name']
        birthDate = request_data['birthDate']
        city = request_data['city']
        country = request_data['country']
        gender = request_data['gender']
        phone = request_data['phone']
        mail = request_data['mail']

        return userController.createUser(name, birthDate, city, country, gender, phone, mail)
    
    else:
        return("ERRO 500: JSON invalido")
    
    
#Atualizar usuario
#/api/data/users/update
#{
#    "usrId" : "",
#    "name" : "",
#    "birthDate" : "",
#    "city" : "",
#    "country" : "",
#    "gender" : "",
#    "phone" : "",
#    "mail" : ""
#} 
@app.route('/api/data/users/update', methods=['PUT'])
def updateUser():
    
    request_data = request.get_json()
    
    if 'usrId' and 'name' and 'birthDate' and  'city' and 'country' and 'gender' and  'phone' and 'mail' in request_data:
        
        usrId = request_data['usrId']
        name = request_data['name']
        birthDate = request_data['birthDate']
        city = request_data['city']
        country = request_data['country']
        gender = request_data['gender']
        phone = request_data['phone']
        mail = request_data['mail']

        return userController.updateUser(usrId, name, birthDate, city, country, gender, phone, mail)
    
    else:
        return("ERRO 500: JSON invalido")
       
        
#exclui usuarios com base no id
#{
#    "id" : "id"
#} 
#127.0.0.1:5000/api/data/users/delete/
@app.route('/api/data/users/delete/', methods=['DELETE'])
def deleteUsersById():
    
    request_data = request.get_json()
    
    if 'id'  in request_data:
        
        id = request_data['id']
        
    else:
        return "Error: No id field provided. Please specify an id."
    
    return userController.deleteUsersById(id)  
   

#Medication Functions=================================================================

#Busca todos os medicamentos
#127.0.0.1:5000/api/data/medication/all
@app.route('/api/data/medication/all', methods=['GET'])
def getAllMedication():    
    return(medicationController.getAll())


#busca medicamentos com base no id
#param -> id
#127.0.0.1:5000/api/data/medication/id?id=0
@app.route('/api/data/medication/id', methods=['GET'])
def getMedicationById():
    
    id = ""
    
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return medicationController.getMedicationById(id)

#busca medicamentos com base no nome
#param -> name
#127.0.0.1:5000/api/data/medication/name?name=medicationName
@app.route('/api/data/medication/name', methods=['GET'])
def getMedicationByName():
    
    name = ""
    
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No name field provided. Please specify an id."
    
    return medicationController.getMedicationByName(name)


#registra um novo medicamento
#/api/data/medication/create
#{
#    "name" : "",
#    "dosage" : "",
#    "frequency" : "",
#    "description" : ""
#} 
@app.route('/api/data/medication/create', methods=['POST'])
def createMedication():
    
    request_data = request.get_json()
    
    if 'name' and 'dosage' and  'frequency' and 'description' in request_data:
        
        name = request_data['name']
        dosage = request_data['dosage']
        frequency = request_data['frequency']
        description = request_data['description']

        return medicationController.createMedication(name, dosage, frequency, description)
    
    else:
        return("ERRO 500: JSON invalido")
    
#Atualizar medicamento
#/api/data/medication/update
#{
#    "medicationId" : "",
#    "name" : "",
#    "dosage" : "",
#    "frequency" : "",
#    "description" : ""
#}  
@app.route('/api/data/medication/update', methods=['PUT'])
def updateMedication():
    
    request_data = request.get_json()
    
    if 'medicationId' and 'name' and 'dosage' and  'frequency' and 'description' in request_data:
        
        medicationId = request_data['medicationId']
        name = request_data['name']
        dosage = request_data['dosage']
        frequency = request_data['frequency']
        description = request_data['description']

        return medicationController.updateMedication(medicationId, name, dosage, frequency, description)
    
    else:
        return("ERRO 500: JSON invalido")
    
#exclui medicamentos com base no id
#{
#    "id" : "id"
#} 
#127.0.0.1:5000/api/data/medication/delete/
@app.route('/api/data/medication/delete/', methods=['DELETE'])
def deleteMedicationById():
    
    request_data = request.get_json()
    
    if 'id'  in request_data:
        
        id = request_data['id']
        
    else:
        return "Error: No id field provided. Please specify an id."
    
    return medicationController.deleteMedicationById(id)  
    

#Hospital Functions ==================================================================

#Busca todos os hospitais
#127.0.0.1:5000/api/data/hospital/all
@app.route('/api/data/hospital/all', methods=['GET'])
def getAllHospital():
    return hospitalController.getAll()

#busca hospital com base no id
#param -> id
#127.0.0.1:5000/api/data/hospital/id?id=0
@app.route('/api/data/hospital/id', methods=['GET'])
def getHospitalById():
    
    id = ""
    
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return hospitalController.getHospitalById(id)

#busca hospital com base no nome
#param -> name
#127.0.0.1:5000/api/data/hospital/name?name=medicationName
@app.route('/api/data/hospital/name', methods=['GET'])
def getHospitalByName():
    
    name = ""
    
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No name field provided. Please specify an id."
    
    return hospitalController.getHospitalByName(name)

#registra um novo hospital
#/api/data/hospital/create
#{
#    "name" : "",
#    "addressStreet" : "",
#    "addressNumber" : "",
#    "addressZip" : ""
#} 
@app.route('/api/data/hospital/create', methods=['POST'])
def createHospital():
    
    request_data = request.get_json()
    
    if 'name' and 'addressStreet' and  'addressNumber' and 'addressZip' in request_data:
        
        name = request_data['name']
        addressStreet = request_data['addressStreet']
        addressNumber = request_data['addressNumber']
        addressZip = request_data['addressZip']

        return hospitalController.createHospital(name, addressStreet, addressNumber, addressZip)
    
    else: 
        return("ERRO 500: JSON invalido")
    
    
#Atualizar hospital
#/api/data/hospital/update
#{
#    "hospitalId": "",
#    "name" : "",
#    "addressStreet" : "",
#    "addressNumber" : "",
#    "addressZip" : ""
#}  
@app.route('/api/data/hospital/update', methods=['PUT'])
def updateHospital():
    
    request_data = request.get_json()
    
    if 'hospitalId' and 'name' and 'addressStreet' and  'addressNumber' and 'addressZip' in request_data:
        
        hospitalId = request_data['hospitalId']
        name = request_data['name']
        addressStreet = request_data['addressStreet']
        addressNumber = request_data['addressNumber']
        addressZip = request_data['addressZip']

        return hospitalController.updateHospital(hospitalId, name, addressStreet, addressNumber, addressZip)
    
    else:
        return("ERRO 500: JSON invalido")
    
    
#exclui hospital com base no id
#{
#    "id" : "id"
#} 
#127.0.0.1:5000/api/data/hospital/delete/
@app.route('/api/data/hospital/delete/', methods=['DELETE'])
def deleteHospitalById():
    
    request_data = request.get_json()
    
    if 'id'  in request_data:
        
        id = request_data['id']
        
    else:
        return "Error: No id field provided. Please specify an id."
    
    return hospitalController.deleteHospitalById(id)  
    


#Medic Functions ==================================================================

#Busca todos os medicos
#127.0.0.1:5000/api/data/medic/all
@app.route('/api/data/medic/all', methods=['GET'])
def getAllMedic():
    return medicController.getAll()

#busca medicos com base no id
#param -> id
#127.0.0.1:5000/api/data/medic/id?id=0
@app.route('/api/data/medic/id', methods=['GET'])
def getMedicById():
    
    id = ""
    
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return medicController.getMedicById(id)

#busca medicos com base no nome
#param -> name
#127.0.0.1:5000/api/data/medic/name?name=medicName
@app.route('/api/data/medic/name', methods=['GET'])
def getMedicByName():
    
    name = ""
    
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No name field provided. Please specify an id."
    
    return medicController.getMedicByName(name)    

#registra um novo medico
#/api/data/medic/create
#{
#    "name" : "",
#    "specialty" : "",
#    "addressStreet" : "",
#    "addressNumber" : "",
#    "addressZip" : ""
#} 
@app.route('/api/data/medic/create', methods=['POST'])
def createMedic():
    
    request_data = request.get_json()
    
    if 'name' and 'specialty' and  'addressStreet' and 'addressNumber' and 'addressZip' in request_data:
        
        name = request_data['name']
        specialty = request_data['specialty']
        addressStreet = request_data['addressStreet']
        addressNumber = request_data['addressNumber']
        addressZip = request_data['addressZip']

        return medicController.createMedic(name, specialty, addressStreet, addressNumber, addressZip)
    
    else: 
        return("ERRO 500: JSON invalido")
    
    
    
#Atualizar medico
#/api/data/hospital/update
#{
#    "medicId" : "",
#    "name" : "",
#    "specialty" : "",
#    "addressStreet" : "",
#    "addressNumber" : "",
#    "addressZip" : ""
#} 
@app.route('/api/data/medic/update', methods=['PUT'])
def updateMedic():
    
    request_data = request.get_json()
    
    if 'medicId' and 'name' and 'specialty' and 'addressStreet' and  'addressNumber' and 'addressZip' in request_data:
        
        medicId = request_data['medicId']
        name = request_data['name']
        specialty = request_data['specialty']
        addressStreet = request_data['addressStreet']
        addressNumber = request_data['addressNumber']
        addressZip = request_data['addressZip']

        return medicController.updateMedic(medicId, name, specialty, addressStreet, addressNumber, addressZip)
    
    else:
        return("ERRO 500: JSON invalido")
    
    
#exclui medico com base no id
#{
#    "id" : "id"
#} 
#127.0.0.1:5000/api/data/medic/delete/id?id=0
@app.route('/api/data/medic/delete/', methods=['DELETE'])
def deleteMedicById():
    
    request_data = request.get_json()
    
    if 'id'  in request_data:
        
        id = request_data['id']
        
    else:
        return "Error: No id field provided. Please specify an id."
    
    return medicController.deleteMedicById(id)  
    

    
#Appointment Functions ==================================================================

#busca agendamentos do usuario com base no id do usuario
#param -> userId
#127.0.0.1:5000/api/data/appointment/id?id=userId
@app.route('/api/data/appointment/id', methods=['GET'])
def getAppointmentByUserId():
    
    userId = ""
    
    if 'id' in request.args:
        userId = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return appointmentController.getAppointment(userId) 


#busca agendamentos do usuario com base no id do usuario e na data
#param -> userId, date (AAAA-MM-DD)
#127.0.0.1:5000/api/data/appointment/idDate?id=userId&date=date
@app.route('/api/data/appointment/idDate', methods=['GET'])
def getAppointmentByUserIdandDate():
    
    userId = ""
    date = ""
    
    if 'id' and 'date' in request.args:
        userId = request.args['id']
        date = request.args['date']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return appointmentController.getAppointmentWithDate(userId, date) 

#busca agendamentos do usuario com base no id do usuario e na data
#param -> userId, date (AAAA-MM-DD)
#127.0.0.1:5000/api/data/appointment/week?id=userId
@app.route('/api/data/appointment/week', methods=['GET'])
def getAppointmentByUserIdandWeek():
    
    userId = ""
    
    if 'id' in request.args:
        userId = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return appointmentController.getAppointmentWeek(userId) 


#busca tratamentos com base no id do usuario
#param -> userId
#127.0.0.1:5000/api/data/treatment/id?id=userId
@app.route('/api/data/treatment/id', methods=['GET'])
def getTreatmentByUserId():
    
    userId = ""
    
    if 'id' in request.args:
        userId = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return appointmentController.getTreatment(userId) 


#registra um novo agendamento
#/api/data/appointment/create
#{
#    "hora" : "",
#    "data" : "",
#    "hospital" : "",
#    "medic" : "",
#    "descricao" : ""
#} 
@app.route('/api/data/appointment/create', methods=['POST'])
def createAppointment():
    
    request_data = request.get_json()
    
    if 'user' and 'hora' and 'data' and  'hospital' and 'medic' and 'descricao' in request_data:
        
        user = request_data['user']
        hora = request_data['hora']
        data = request_data['data']
        hospital = request_data['hospital']
        medic = request_data['medic']
        descricao = request_data['descricao']

        return appointmentController.createAppointment(user, hora, data, hospital, medic, descricao)
    
    else: 
        return("ERRO 500: JSON invalido")
    
    
#registra um novo tratamento
#/api/data/treatment/create
#{
#    "user" : "",
#    "medication" : "",
#    "data_inicio" : "",
#    "data_fim" : "",
#    "last_occurrence" : "",
#    "medic" : "",
#    "descricao" : "",
#    "monitorado" : "",
#    "atendido" : ""
#} 
@app.route('/api/data/treatment/create', methods=['POST'])
def createTreatment():
    
    request_data = request.get_json()
    
    if 'user' and 'medication' and  'data_inicio' and 'data_fim' and 'last_occurrence' and 'medic' and 'descricao' and 'monitorado' and 'atendido' in request_data:
        
        user = request_data['user']
        medication = request_data['medication']
        data_inicio = request_data['data_inicio']
        data_fim = request_data['data_fim']
        last_occurrence = request_data['last_occurrence']
        medic = request_data['medic']
        descricao = request_data['descricao']
        monitorado = request_data['monitorado']
        atendido = request_data['atendido']
        
        return appointmentController.createTreatment(user, medication, data_inicio, data_fim, last_occurrence, medic, descricao, monitorado, atendido)  
    else:  
        return("ERRO 500: JSON invalido")


#atualiza um agendamento
#/api/data/appointment/update
#{
#    "appointmentId" : "",
#    "hora" : "",
#    "data" : "",
#    "hospital" : "",
#    "medic" : "",
#    "descricao" : ""
#} 
@app.route('/api/data/appointment/update', methods=['PUT'])
def updateAppointment():
    
    request_data = request.get_json()
    
    if 'appointmentId' and 'user' and 'hora' and 'data' and  'hospital' and 'medic' and 'descricao' in request_data:
        
        appointmentId = request_data['appointmentId']
        user = request_data['user']
        hora = request_data['hora']
        data = request_data['data']
        hospital = request_data['hospital']
        medic = request_data['medic']
        descricao = request_data['descricao']

        return appointmentController.updateAppointment(appointmentId, user, hora, data, hospital, medic, descricao)
    
    else: 
        return("ERRO 500: JSON invalido")
    

#atualiza tratamento
#/api/data/treatment/update
#{
#    "treatmentId" : "",
#    "user" : "",
#    "medication" : "",
#    "data_inicio" : "",
#    "data_fim" : "",
#    "last_occurrence" : "",
#    "medic" : "",
#    "descricao" : "",
#    "monitorado" : "",
#    "atendido" : ""
#} 
@app.route('/api/data/treatment/update', methods=['PUT'])
def updateTreatment():
    
    request_data = request.get_json()
    
    if 'treatmentId' and 'user' and 'medication' and  'data_inicio' and 'data_fim' and 'last_occurrence' and 'medic' and 'descricao' and 'monitorado' and 'atendido' in request_data:
        
        treatmentId = request_data['treatmentId']
        user = request_data['user']
        medication = request_data['medication']
        data_inicio = request_data['data_inicio']
        data_fim = request_data['data_fim']
        last_occurrence = request_data['last_occurrence']
        medic = request_data['medic']
        descricao = request_data['descricao']
        monitorado = request_data['monitorado']
        atendido = request_data['atendido']
        
        return appointmentController.updateTreatment(treatmentId, user, medication, data_inicio, data_fim, last_occurrence, medic, descricao, monitorado, atendido)  
    else: 
        return("ERRO 500: JSON invalido")    
    
    
#exclui treatment com base no id
#{
#    "id" : "id"
#} 
#127.0.0.1:5000/api/data/treatment/delete/
@app.route('/api/data/treatment/delete/', methods=['DELETE'])
def deleteTreatmentById():
    
    request_data = request.get_json()
    
    if 'id'  in request_data:
        
        id = request_data['id']
        
    else:
        return "Error: No id field provided. Please specify an id."
    
    return appointmentController.deleteTreatmentById(id)  

#exclui appointment com base no id
#{
#    "id" : "id"
#} 
#127.0.0.1:5000/api/data/appointment/delete/
@app.route('/api/data/appointment/delete/', methods=['DELETE'])
def deleteAppointmentById():
    
    request_data = request.get_json()
    
    if 'id'  in request_data:
        
        id = request_data['id']
        
    else:
        return "Error: No id field provided. Please specify an id."
    
    return appointmentController.deleteAppointmentById(id)  

    
#Zenbo Functions ========================================================================

#acorda o Zenbo
#127.0.0.1:5000/api/data/zenbo/awake
@app.route('/api/data/zenbo/awake', methods=['GET'])
def zenboAwake():
    return zenboController.zenboAwake()

#lista os compromissos do dia
#127.0.0.1:5000/api/data/zenbo/listAppointments/id?id=userId
@app.route('/api/data/zenbo/listAppointments/id', methods=['GET'])
def zenboListAppointments():
    userId = ""
    
    if 'id' in request.args:
        userId = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return zenboController.zenboListAppointments(userId) 

#lista os compromissos da semana
#127.0.0.1:5000/api/data/zenbo/listWeekAppointments/id?id=userId
@app.route('/api/data/zenbo/listWeekAppointments/id', methods=['GET'])
def zenboListWeekAppointments():
    userId = ""
    
    if 'id' in request.args:
        userId = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return zenboController.zenboListWeekAppointments(userId) 

#lista os tratamentos do usuario
#127.0.0.1:5000/api/data/zenbo/listTreatments/id?id=userId
@app.route('/api/data/zenbo/listTreatments/id', methods=['GET'])
def zenboListTreatments():
    userId = ""
    
    if 'id' in request.args:
        userId = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return zenboController.zenboListTreatments(userId) 

#verifica a ingestao de medicamentos
#127.0.0.1:5000/api/data/zenbo/ingestMed?userId=userId&treatmentId=treatmentId
@app.route('/api/data/zenbo/ingestMed', methods=['GET'])
def zenboIngestMed():
    
    userId = ""
    treatmentId = ""
    
    if 'userId' and 'treatmentId' in request.args:
        userId = request.args['userId']
        treatmentId = request.args['treatmentId']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return zenboController.zenboIngestMed(userId, treatmentId) 


#informa o proximo medicamento do usuario
#127.0.0.1:5000/api/data/zenbo/nextMedication/id?id=userId
@app.route('/api/data/zenbo/nextMedication/id', methods=['GET'])
def zenboNextMedication():
    userId = ""
    
    if 'id' in request.args:
        userId = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    return zenboController.zenboNextMedication(userId) 


#========================================================================================

htmlFile = open("C:\\Users\\Matheus Ancelmo\\git\\ElderMedManagement\\ZenboAPI\\ZenboApiSrc\\apiSrc_html\\home.txt", "r")
htmlPage = htmlFile.read()

#=====================================================================================


#app.run(host="192.168.1.7", port=1515, debug=True)
app.run(host="192.168.7.15", port=1515)





