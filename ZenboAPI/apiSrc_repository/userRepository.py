import mysql.connector
from apiSrc_application import persistanceProperties
from apiSrc_entity import userEntity

def getAll():
    
    try:
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM user"
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except Exception as e: 
                
        return("Erro! " + e)


def getUserById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM user WHERE id = "+ str(id) +";";
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except Exception as e: 
                
        return("Erro! " + str(e)) 
    
    
def createUser(name, birthDate, city, country, gender, phone, mail):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase) 
    
        dbCursor = dbConn.cursor()
    
        query = "INSERT INTO user (userName, birthDate, city, country, gender, phone, mail) VALUES('"+ name +"', '"+ birthDate +"', '"+ city +"', '"+ country +"', '"+ gender +"', '"+ phone +"', '"+ mail +"');"
        dbCursor.execute(query)
    
        dbConn.commit()
        
        retMesage = ""
        
        if dbCursor.lastrowid:
            retMessage = ('last insert id: ' + str(dbCursor.lastrowid))

        else:
            retMessage = 'could not insert register'

        
        dbCursor.close()
        dbConn.close()
        
        return(retMessage)
    
    except Exception as e: 
                
        return("Erro! " + str(e))
    

def updateUser(user):
      
    try:

        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
        
        query = "UPDATE user SET userName = '"+ user.name +"', birthDate = '"+ user.birthDate +"', city = '"+ user.city +"', country = '"+ user.country +"', gender = '"+ user.gender +"', phone = '"+ user.phone +"', mail = '"+ user.mail +"' WHERE id = "+ user.id +";";     
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except Exception as e: 
                
        return("Erro! " + str(e))
    


def deleteUserById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "DELETE FROM user WHERE id = "+ id +";";
        
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except Exception as e: 
                
        return("Erro! " + str(e))


def entityConverter(queryResults):
    
    returnArray = []
    
    for item in queryResults:
        
        newUser = userEntity.User()
        
        newUser.id = item[0]
        newUser.name = item[1]
        newUser.birthDate = item[2]
        newUser.city = item[3]
        newUser.country = item[4]
        newUser.gender = item[5]
        newUser.phone = item[6]
        newUser.mail = item[7]
                
        returnArray.append(newUser)
        
    return(returnArray)