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

api_endpoint = "http://192.168.7.23:1515"
userId = sys.argv[1]
treatmentId = sys.argv[2]

#busca os tratamentos
def getTreatment(userId, treatmentId):
    
    treatment = []
    
    request_endpoint = "/api/data/treatment/id?id=" + str(userId)

    response = requests.get(api_endpoint + request_endpoint)
    response = response.json()    
    
    for i in response:
              
        if str(i['id']) == treatmentId:
            
            i['medication'] = getMedication(i['medication'])
            
            treatment.append(textFormat(i))
        
    return(treatment)

#buscar medicamento        
def getMedication(medicationId):
    
    medicationName = ''
    
    medicationRequest = requests.get(api_endpoint + "/api/data/medication/id?id=" + str(medicationId))    
    
    medicationRequest = medicationRequest.json()
    
    for i in medicationRequest:
        
        medicationName = i['name']
    
    return medicationName

#formatar resultado da requisicao
def textFormat(treatment):
    
    textReturn = " "+treatment['medication']+" for the "+treatment['descricao']+" treatment"
    
    return(textReturn)

def dateFormat():
    
    date = datetime.datetime.now()
    
    year = str(date.year)
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    
    #MES
    if (month < 10):
        month = "0" + str(month)
    else:
        month = str(month)
       
    #DIA 
    if (day < 10):
        day = "0" + str(day)
    else:
        day = str(day)
        
    #HORA
    if (hour < 10):
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    
    #MINUTO
    if (minute < 10):
        minute = "0" + str(minute)
    else:
        minute = str(minute)
        
    #SEGUNDOS
    if (second < 10):
        second = "0" + str(second)
    else:
        second = str(second)
      
    return (day +"/"+ month +"/"+ year +", "+ hour +":"+ minute +":"+ second)


def updtMedication(treatmentId, speechText):
    
    #FUNCOES DE DIALOGO ===================================================================================
    
    #voce tomou o remedio? data atual ou 'n'
    zenbo.robot.set_expression(RobotFace.DEFAULT, (speechText + '. Did you manage to take this medication?...'), {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)    
    
    zenbo.robot.speak_and_listen('', {'listenLanguageId' :2})
    time.sleep(int(3))    
    respostaAtendido = procAnswer(myUtterance, 'r1')  
    
    time.sleep(int(1))
    zenbo.robot.set_expression(RobotFace.DEFAULT, '...All right, a reminder that I will also keep track of this treatment...', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)    
    time.sleep(int(1))  
    
    #ENVIO DA REQUISICAO =================================================================================
    
    request_endpoint = "/api/data/treatment/update"
    
    requestURL = api_endpoint + request_endpoint
    
    body = json.dumps({"treatmentId" : str(treatmentId), "user" : "", "medication" : "", "data_inicio" : "", "data_fim" : "", "last_occurrence" : "", "medic" : "", "descricao" : "", "monitorado" : "s", "atendido" : str(respostaAtendido)})
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.request("PUT", requestURL, headers=headers, data=body)   
    
    response = response.text

def procAnswer(resposta, tipo):
    #retornar 'n' ou dateFormat()
    
    stringArray = resposta.split(" ")
    
    retAnsw = 'void'
    
    for i in stringArray:
        
        try:
            
            #respostas positivas
            if i == "yes" or i == "yeah" or i == "did" or i == "yep":
            
                retAnsw = 's'
            
            #respostas negativas
            if i == "no" or i == "not" or i == "not."or i == "no."or i == "didnt":
               
               retAnsw = 'n'
    
        except:
            print("Invalid answer")
            
            
    #separa retorno de acordo com o tipo de pergunta
    if tipo == 'r1':
        
        if retAnsw == 's':
            
            retAnsw = dateFormat()
    

    return retAnsw
   
      
#ouvir o usuario
def listen_callback(args):
    global myUtterance, zenbo_speakSpeed, zenbo_speakPitch
    event_slu_query = args.get('event_slu_query', None)
    
    if event_slu_query:
        global myUtterance
        myUtterance = str(event_slu_query.get('app_semantic').get('correctedSentence'))    
        
        
#EXECUCAO ==============================================================================================================================================

zenbo.robot.register_listen_callback(1207, listen_callback)     
        
time.sleep(int(0.3))        
    
#busca os medicamentos pendentes    
zenbo.robot.set_expression(RobotFace.DEFAULT, 'A while ago, you had to take...', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)        
        
time.sleep(int(1))        
        
response = getTreatment(userId, treatmentId)

time.sleep(int(1))        

print(response)
        
#registra os tratamentos
updtMedication(treatmentId, response[0])
time.sleep(int(1))  

zenbo.robot.set_expression(RobotFace.DEFAULT, 'And I guess thats it, thank you', {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)

zenbo.robot.set_expression(RobotFace.HIDEFACE)
zenbo.robot.unregister_listen_callback()
zenbo.release()
