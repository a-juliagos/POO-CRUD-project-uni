class Vulnerabilidade:

    def __init__(self, descricao, tipo, severidade, status):

        self.descricao = descricao
        self.tipo = tipo
        self.severidade = severidade
        self.status = status

    def to_dict(self):

        return {
            
        "descricao": self.descricao, 
        "tipo": self.tipo.name, 
        "severidade": self.severidade.name, 
        "status": self.status.name, 

        }