import json
import requests

def getISSLocation():
    
    data = requests.get("http://api.open-notify.org/iss-now.json")
    data = json.loads(data.text)
    
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    
    locationData = requests.get("https://api.bigdatacloud.net/data/reverse-geocode-client?latitude="+ latitude +"&longitude="+ longitude +"&localityLanguage=en")
    
    locationData = json.loads(locationData.text)
    
    locationName = locationData['localityInfo']['informative'][0]['name']
    locationInfo = locationData['localityInfo']['informative'][0]['description']
    
    article = ''
    
    if locationData['continent'] == '':
        article = "the"
    
    textOutput = "Right now, the International Space Station is flying above " + article + " " + locationName + " ," + locationInfo + " and going on, fast and steady!"
    
    print(textOutput)
    
getISSLocation()