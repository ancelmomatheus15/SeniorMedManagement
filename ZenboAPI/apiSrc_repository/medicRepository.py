import mysql.connector
from apiSrc_application import persistanceProperties
from apiSrc_entity import medicEntity


def getAll():
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM medic"
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados")
    

def getMedicById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM medic WHERE id = "+ str(id) +";";
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados")  
      
      
def getMedicByName(name):
    
    try:

        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM medic WHERE name LIKE '%" + name + "%' "
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados")      
    
    
def createMedic(name, specialty, addressStreet, addressNumber, addressZip):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "INSERT INTO medic (name, specialty, addressStreet, addressNumber, addressZip) VALUES('"+ name +"', '"+ specialty +"', '"+ addressStreet +"', '"+ addressNumber+"', '"+ addressZip +"');"
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
      
      
      
      
      
def updateMedic(medic):
    
    try:

        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
        
        query = "UPDATE medic SET name = '"+ medic.name +"', specialty = '"+ medic.specialty +"', addressStreet = '"+ medic.addressStreet +"', addressNumber = '"+ medic.addressNumber +"', addressZip = '"+ medic.addressZip +"' WHERE id = "+ medic.id +";";     
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")
            
    
    
    
def deleteMedicById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "DELETE FROM medic WHERE id = "+ id +";";
        
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")  
 
      
      
      
      
      
      
      
      
      
      
    
def entityConverter(queryResults):
    
    returnArray = []
    
    for item in queryResults:
        
        newMedic = medicEntity.Medic()
        
        newMedic.id = item[0]
        newMedic.name = item[1]
        newMedic.specialty = item[2]
        newMedic.addressStreet = item[3]
        newMedic.addressNumber = item[4]
        newMedic.addressZip = item[5]
        
        returnArray.append(newMedic)
        
    return(returnArray)
