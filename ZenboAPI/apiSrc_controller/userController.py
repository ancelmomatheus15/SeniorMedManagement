from apiSrc_service import userService

def getUsers():
    
    results = userService.getAll()
    
    return results

def getUsersById(id):

    results = userService.getUserById(id)

    return results

def createUser(name, birthDate, city, country, gender, phone, mail):
    
    results = userService.createUser(name, birthDate, city, country, gender, phone, mail)
    
    return results
    
    
def updateUser(usrId, name, birthDate, city, country, gender, phone, mail):
    
    results = userService.updateUser(usrId, name, birthDate, city, country, gender, phone, mail)
    
    return results
    
def deleteUsersById(id):

    results = userService.deleteUserById(id)

    return results