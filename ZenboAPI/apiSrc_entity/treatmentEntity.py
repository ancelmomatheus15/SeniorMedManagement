class Treatment():
    
    id = ""
    user = ""
    medication = ""
    data_inicio = ""
    data_fim = ""
    last_occurence = ""
    medic = ""
    descricao = ""
    monitorado = ""
    atendido = ""
    
    def toString(self, treatment):
        
        return("["+ treatment.id +", "+ treatment.user +", "+ treatment.medication +", "+ treatment.data_inicio +", "+ treatment.data_fim +" ,"+ treatment.last_occurence +", "+ treatment.medic +" ,"+ treatment.descricao +" ,"+ treatment.monitorado +" ,"+ treatment.atendido + "]")