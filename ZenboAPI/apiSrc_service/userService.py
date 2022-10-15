import json
from apiSrc_entity import userEntity
from flask import jsonify
from apiSrc_repository import userRepository

def getAll():
    
    jsonUserList = "["
    
    userList = userRepository.getAll()
    
    print(userList)
    
    if userList == []:
        
        return '[]'
    
    else:
    
        for i in userList:
            
            i.birthDate = i.birthDate.strftime("%d/%m/%Y")       
            
            userJson = json.dumps(i.__dict__)
            
            jsonUserList = jsonUserList + userJson + ", "        
        
        auxConvert = list(jsonUserList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonUserList = "".join(auxConvert)
        
        print(jsonUserList)
        
        return (jsonUserList)


def getUserById(id):
    
    jsonUserList = "["
    
    userList = userRepository.getUserById(id)
    
    print(userList)
    
    if userList == []:
        
        return '[]'
    
    else:
    
        for i in userList:   
            
            i.birthDate = i.birthDate.strftime("%d/%m/%Y")  
            
            userJson = json.dumps(i.__dict__)
            
            jsonUserList = jsonUserList + userJson + ", "    
        
        auxConvert = list(jsonUserList)
        auxConvert[len(auxConvert) - 2] = ']'
        jsonUserList = "".join(auxConvert)
        
        print(jsonUserList)
        
        return (jsonUserList)

def createUser(name, birthDate, city, country, gender, phone, mail):
    
    insertResult = userRepository.createUser(name, birthDate, city, country, gender, phone, mail)
     
    userJson = json.dumps(insertResult)
    
    print(userJson)
    
    return (userJson)


def updateUser(usrId, name, birthDate, city, country, gender, phone, mail):
    
    updtUser = userEntity.User()
    
    #buscar um usuario
    getUser = getUserById(usrId)
    getUser = json.loads(getUser)
    getUser = getUser[0]
    
    #definir id
    updtUser.id = usrId

    #atualizar nome
    if name != "":
        updtUser.name = name
    else:
        updtUser.name = getUser["name"]
        
    #atualizar birthdate
    if birthDate != "":
        updtUser.birthDate = birthDate
    else:
        updtUser.birthDate = getUser["birthDate"]
        
    #corrigir formato da data
    updtUser.birthDate = (updtUser.birthDate[6:10] +"-"+ updtUser.birthDate[3:5] +"-"+ updtUser.birthDate[0:2])
    
    updtUser.birthDate
        
    #atualizar birthdate
    if city != "":
        updtUser.city = city
    else:
        updtUser.city = getUser["city"]
        
    #atualizar country
    if country != "":
        updtUser.country = country
    else:
        updtUser.country = getUser["country"]
        
    #atualizar gender
    if gender != "":
        updtUser.gender = gender
    else:
        updtUser.gender = getUser["gender"]
        
    #atualizar phone
    if phone != "":
        updtUser.phone = phone
    else:
        updtUser.phone = getUser["phone"]
        
    #atualizar mail
    if mail != "":
        updtUser.mail = mail
    else:
        updtUser.mail = getUser["mail"]
        
    #jogar user no banco
    return(userRepository.updateUser(updtUser)) 
            

def deleteUserById(id):
    
    print("id recebido: " + id)
    
    deleteReturn = userRepository.deleteUserById(id)
    
    print(deleteReturn)
    
    return (deleteReturn)



def getMockUser():
    
    mockUser = userEntity.User()
    
    mockUser.id = "12345"
    mockUser.name = "Testevaldo Silva"
    mockUser.birthDate = "10/10/1910"
    mockUser.city = "Brasilia"
    mockUser.country = "Brasil"
    mockUser.gender = "M"
    mockUser.phone = "(11) 99999-9999"
    mockUser.mail = "testevaldo.silva@mock.com.br"
        
    return mockUser
    