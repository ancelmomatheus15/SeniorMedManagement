import mysql.connector
#from ElderMedManagement.ZenboAPI.apiSrc_entity import medicationEntity


def connect():
    
    dbConn = mysql.connector.connect(host="localhost", user="python", password="102030", database="zenboIntegrationDB")
    print(dbConn)
    
    dbCursor = dbConn.cursor()
    
    query = "SELECT * FROM medication"
    
    print (query)
#    dbCursor.execute(query)
    
#    dbQueryResult = dbCursor.fetchall()
    
#    print(entityConverter(dbQueryResult))
    
    dbCursor.close()
#    dbConn.close()
    
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

connect()
