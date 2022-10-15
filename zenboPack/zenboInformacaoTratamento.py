import sys
sys.path.append('/var/www/ElderMedManagement/zenboPack/pyzenbo/')

import pyzenbo
import requests
import time
import sys
import json
import pyzenbo.modules.zenbo_command as commands

from pyzenbo.modules.dialog_system import RobotFace

#definir conexao
host = '192.168.7.18'
zenbo = pyzenbo.connect(host)

#configurar volume e tom de voz da fala
zenbo_speakSpeed = 100
zenbo_speakPitch = 100
zenbo_speakLanguage = 100

api_endpoint = "http://192.168.7.23:1515"
userId = sys.argv[1]

#buscar tratamentos do usuario
def getTreatment(userId):
    
    treatment = []
    
    request_endpoint = "/api/data/treatment/id?id=" + userId

    response = requests.get(api_endpoint + request_endpoint)
    response = response.json()
    
    for i in response:
        
        medication = getMedication(i['medication'])
            
        treatment.append(textFormat(i, medication))
                  
    return(treatment)

#buscar medicamento        
def getMedication(medicationId):
    
    medicationRequest = requests.get(api_endpoint + "/api/data/medication/id?id=" + str(medicationId))    
    
    medicationRequest = medicationRequest.json()
    
    return medicationRequest[0]

#formatar resultado da requisicao
def textFormat(treatment, medication):
    
    description = treatment['descricao']
    medName = medication['name']
    dataUltima = dataFormat(treatment['last_occurrence'])
    dataFinal = dataFormat(treatment['data_fim'])
    atendido = treatment['atendido']
    frequency = medication['frequency']
    
    if atendido != 'n':
        atendido = 'did'
    else:
        atendido = 'did not'
        
    if frequency[len(frequency) - 1] == 'h' and len(frequency) < 3:
        frequency = frequency.rstrip(frequency[-1]) + " hours"
    
    treatmentDescription = "for the "+ description +" treatment, you have to take "+ medName +" until "+ dataFinal +", the last occurrence for this treatment was in "+ dataUltima +" and you "+ atendido +" took the medication."
    treatmentRemember = " Remember to take "+medName+" on each and every "+ frequency
    
    return(treatmentDescription + treatmentRemember)

def dataFormat(data):
    ano = data[0:4]
    dia = data[len(data) - 2:len(data)]
    mes = int(data[5:len(data)-3])
    
    meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    mes = meses[mes-1]
    
    return (dia +" of "+ mes +" of "+ ano)

zenbo.robot.set_expression(RobotFace.DEFAULT, 'Lets fetch data about this treatment...', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)
time.sleep(int(1))

response = getTreatment(userId)

for i in response:

    zenbo.robot.set_expression(RobotFace.DEFAULT, i, {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)

time.sleep(int(1))  
 
zenbo.robot.set_expression(RobotFace.DEFAULT, 'And I guess thats it', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)

zenbo.robot.set_expression(RobotFace.HIDEFACE)

zenbo.release()



