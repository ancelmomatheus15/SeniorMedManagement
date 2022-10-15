class Appointment():
    
    id = ""
    user = ""
    hora = ""
    data = ""
    hospital = ""
    medic = ""
    descricao = ""
    
    def toString(self, appointment):
        
        return("["+ appointment.id +", "+ appointment.user +", "+ appointment.hora +", "+ appointment.data +", "+ appointment.hospital +" ,"+ appointment.medic +", "+ appointment.descricao+ "]")

