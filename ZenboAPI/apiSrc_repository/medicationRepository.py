import mysql.connector
from apiSrc_application import persistanceProperties
from apiSrc_entity import medicationEntity

def getAll():
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM medication"
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados")
    
    
def getMedicationById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM medication WHERE id = "+ str(id) +";";
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados")    
    
    
def getMedicationByName(name):
    
    try:

        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM medication WHERE name LIKE '%" + name + "%' "
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados")    
    
    
def createMedication(name, dosage, frequency, description):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "INSERT INTO medication (name, dosage, frequency, description) VALUES('"+ name +"', '"+ dosage +"', '"+ frequency +"', '"+ description +"');"
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
    
    
def updateMedication(medication):
    
    try:

        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
        
        query = "UPDATE medication SET name = '"+ medication.name +"', dosage = '"+ medication.dosage +"', frequency = '"+ medication.frequency +"', description = '"+ medication.description +"' WHERE id = "+ medication.id +";";     
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")
            
    
    
def deleteMedicationById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "DELETE FROM medication WHERE id = "+ id +";";
        
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")
           
    
def entityConverter(queryResults):
    
    returnArray = []
    
    for item in queryResults:
        
        newMedication = medicationEntity.Medication()
        
        newMedication.id = item[0]
        newMedication.name = item[1]
        newMedication.dosage = item[2]
        newMedication.frequency = item[3]
        newMedication.description = item[4]
        
        returnArray.append(newMedication)
        
    return(returnArray)
        
