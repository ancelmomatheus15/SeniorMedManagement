#Lista os compromissos que o usuario tem no dia
#Parametros
#-ID do usuario

import sys
sys.path.append('/var/www/ElderMedManagement/zenboPack/pyzenbo/')

import pyzenbo
import requests
import time
import sys
import json
import datetime
import pyzenbo.modules.zenbo_command as commands

from pyzenbo.modules.dialog_system import RobotFace

#definir conexao
host = '192.168.7.18'
zenbo = pyzenbo.connect(host)

#configurar volume e tom de voz da fala
zenbo_speakSpeed = 100
zenbo_speakPitch = 100
zenbo_speakLanguage = 100

api_endpoint = "http://192.168.7.22:1515"
userId = sys.argv[1]

#buscar compromissos do usuario
def getAppointments(userId):
    
    appointments = []
    
    dataAtual = datetime.date.today()
    
    request_endpoint = "/api/data/appointment/idDate?id=" + str(userId) + "&date=" + str(dataAtual)

    response = requests.get(api_endpoint + request_endpoint)
    response = response.json()
    
    for i in response:
        
        i['hospital'] = getHospital(i['hospital'])
        i['medic'] = getMedic(i['medic'])
        i['hora'] = formatHora(i['hora'])
        
        appointments.append(textFormat(i))
        
    return(appointments)
        
            
#buscar hospital        
def getHospital(hospId):
    
    hospitalName = ''
    
    hospitalRequest = requests.get(api_endpoint + "/api/data/hospital/id?id=" + str(hospId))    
    
    hospitalRequest = hospitalRequest.json()
    
    for i in hospitalRequest:
        
        hospitalName = i['name']
    
    return hospitalName
   
#buscar medico
def getMedic(medicId):
    
    medicName = ''
    
    medicRequest = requests.get(api_endpoint + "/api/data/medic/id?id=" + str(medicId))    
    
    medicRequest = medicRequest.json()
    
    for i in medicRequest:
    
        medicName = i['name']
    
    return medicName

#formatar horario pra fala   
def formatHora(horario):
    
    horario = str(horario)
    
    hora = str(horario[0:2])
    minuto = str(horario[2:4])
    
    return (hora +" hours and " + minuto + " minutes")
   
#formatar resultado da requisicao
def textFormat(appointment):
    
    article = ''
    
    if (appointment['descricao'][0] in ['a', 'e', 'i', 'o', 'u']):
        article = 'an'
    else:
        article = 'a'
    
    textReturn = "at "+ str(appointment['hora']) +", you have "+ article +" "+ appointment['descricao'] +" with doctor "+ appointment['medic'] + " at "+ appointment['hospital'] +"."
    
    return(textReturn)

zenbo.robot.set_expression(RobotFace.DEFAULT, 'Lets check if there are appointments today...', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)
time.sleep(int(1))

response = getAppointments(userId)

if response == []:
    
    zenbo.robot.set_expression(RobotFace.DEFAULT, '...well, guess there are no appointments for today', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)
    time.sleep(int(1))
    
else:
    
    zenbo.robot.set_expression(RobotFace.DEFAULT, '...Guess You have appointments for today. Listing them now...', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)
    time.sleep(int(1))

    for i in response:
    
        zenbo.robot.set_expression(RobotFace.DEFAULT, i, {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)
   
time.sleep(int(1))  
 
zenbo.robot.set_expression(RobotFace.DEFAULT, 'And I guess thats it', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)

zenbo.robot.set_expression(RobotFace.HIDEFACE)

zenbo.release()