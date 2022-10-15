import mysql.connector
from apiSrc_application import persistanceProperties
from apiSrc_entity import hospitalEntity

def getAll():
    
    try:
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM hospital"
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados")
    

def getHospitalById(id):
    
    try:
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM hospital WHERE id = "+ str(id) +";";
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados")  
    
    
def getHospitalByName(name):
    
    try:
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM hospital WHERE name LIKE '%" + name + "%' "
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados")  


def createHospital(name, addressStreet, addressNumber, addressZip):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "INSERT INTO hospital (name, addressStreet, addressNumber, addressZip) VALUES('"+ name +"', '"+ addressStreet +"', '"+ addressNumber +"', '"+ addressZip +"');"
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
    
    except:
        
        return("Erro ao conectar com o banco de dados")
    


def updateHospital(hospital):
    
    
    try:

        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
        
        query = "UPDATE hospital SET name = '"+ hospital.name +"', addressStreet = '"+ hospital.addressStreet +"', addressNumber = '"+ hospital.addressNumber +"', addressZip = '"+ hospital.addressZip +"' WHERE id = "+ hospital.id +";";     
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")
    

    
def deleteHospitalById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "DELETE FROM hospital WHERE id = "+ id +";";
        
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")


def entityConverter(queryResults):
    
    returnArray = []
    
    for item in queryResults:
        
        newHospital = hospitalEntity.Hospital()
        
        newHospital.id = item[0]
        newHospital.name = item[1]
        newHospital.addressStreet = item[2]
        newHospital.addressNumber = item[3]
        newHospital.addressZip = item[4]
        
        returnArray.append(newHospital)
        
    return(returnArray)