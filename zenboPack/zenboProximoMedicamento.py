import sys
sys.path.append('/var/www/ElderMedManagement/zenboPack/pyzenbo/')

import pyzenbo
import requests
import time
import datetime
import sys
import json
import pyzenbo.modules.zenbo_command as commands

from pyzenbo.modules.dialog_system import RobotFace

#definir conexao
host = '192.168.7.23'
zenbo = pyzenbo.connect(host)

#configurar volume e tom de voz da fala
zenbo_speakSpeed = 100
zenbo_speakPitch = 100
zenbo_speakLanguage = 100

api_endpoint = "http://192.168.7.22:1515"
userId = sys.argv[1]

#buscar tratamentos do usuario
def getTreatment(userId):
    
    atendido = []
    nAtendido = []
    
    request_endpoint = "/api/data/treatment/id?id=" + str(userId)

    response = requests.get(api_endpoint + request_endpoint)
    response = response.json()
    
    for i in response:
                
        #dados do medicamento, [nome, frequencia]
        medicationData = getMedication(i['medication'])
        
        now = datetime.datetime.now()
        
        #se foi atendido
        if i['atendido'] != 'n':
            
            calcHorario = calcularHorario(i['atendido'], medicationData[1], i, medicationData[0])
            
            if calcHorario != 'nda':
                atendido.append(calcHorario)
        
        else:
            nAtendido.append("on the last time, you did not take " +medicationData[0]+ " for your " +i['descricao'] + " treatment, it would be good to take it now")
               
    
    return(atendido + nAtendido)
        
def calcularHorario(dateString, frequencia, tratamento, nomeMedicamento):
    
    ano = int(dateString[6:10])
    mes = int(dateString[3:5])
    dia = int(dateString[0:2])
    hora = int(dateString[12:14])
    minuto = int(dateString[15:17])
    
    ultimaIngestao = datetime.datetime(ano, mes, dia, hora, minuto)
    
    proximaIngestao = ultimaIngestao + datetime.timedelta(hours = frequencia)

    #se a proxima ingestao for de agora ate daqui 1 hora
    if (proximaIngestao < (datetime.datetime.now() + datetime.timedelta(hours = 1))) and (proximaIngestao > datetime.datetime.now()):
        
        return(textFormat(tratamento, nomeMedicamento))
    
    else:
        
        return ("nda")
    

#buscar medicamento        
def getMedication(medicationId):
    
    returnArray = []
    
    medicationRequest = requests.get(api_endpoint + "/api/data/medication/id?id=" + str(medicationId))    
    
    medicationRequest = medicationRequest.json()
    
    for i in medicationRequest:
        
        medicationName = i['name']
        
        frequency = i['frequency']
        
        if frequency[len(frequency) - 1] == 'h' and len(frequency) < 3:
            frequency = int(frequency.rstrip(frequency[-1]))
        else:
            frequency = 222
            
        returnArray.append(medicationName)
        returnArray.append(frequency)
    
    return returnArray
   
#formatar resultado da requisicao
def textFormat(treatment, nomeMedicamento):
    
    textReturn = " "+nomeMedicamento+" for the "+treatment['descricao']+" treatment"
        
    return(textReturn)


def getHour():
    
    now = datetime.datetime.now()
        
    hora = now.hour
    minuto = now.minute
                               
    return (str(hora) +" hours and "+ str(minuto) +" minutes")


zenbo.robot.set_expression(RobotFace.DEFAULT, "Hey there, it's "+ getHour() +" and it seems that you gotta take some medication...", {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)
time.sleep(int(1))

response = getTreatment(userId)

for i in response:

    zenbo.robot.set_expression(RobotFace.DEFAULT, i, {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)

time.sleep(int(1))  
 
zenbo.robot.set_expression(RobotFace.DEFAULT, 'And I guess thats it', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)

zenbo.robot.set_expression(RobotFace.HIDEFACE)

zenbo.release()