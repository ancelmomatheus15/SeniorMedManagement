class User():
    
    id = ""
    name = ""
    birthDate = ""
    city = ""
    country = ""
    gender = ""
    phone = ""
    mail = ""  

    def toString(self, user):
        
        return("["+ user.id +", "+ user.name +", "+ user.birthDate +", "+ user.city +", "+ user.country +", "+ user.gender +", "+ user.phone +", "+ user.mail + "]") 