class Ativo:

    def __init__(self, id_ativo, nome_hostname, responsavel, setor, tipo):

        self.id_ativo = id_ativo
        self.nome_hostname = nome_hostname
        self.responsavel = responsavel
        self.setor = setor
        self.tipo = tipo
        self.vulnerabilidades = []

    def to_dict(self):

        return {
            
        "id":self.id_ativo, 
        "nome":self.nome_hostname, 
        "responsavel":self.responsavel, 
        "setor":self.setor, 
        "tipo":self.tipo.name, 
        "vulnerabilidades": [ 
            vuln.to_dict()
            for vuln in self.vulnerabilidades    
        ]
        
        }


    def listar(self):
        
        print(f""" 
-------------------------
          
ID: {self.id_ativo}
Nome/Hostname: {self.nome_hostname}
Responsável: {self.responsavel}
Setor: {self.setor}
Tipo: {self.tipo.name}   
""")  

        print('---- Vulnerabilidades --- ')
        
        if not self.vulnerabilidades:
            
            print('\nNão existem Vulnerabilidades cadastradas!!')

        else:
            
            for i, vulnerabilidade in enumerate(self.vulnerabilidades, start=1):
                
                print(f"""   
Vulnerabilidade {i}

Descrição: {vulnerabilidade.descricao}
Tipo: {vulnerabilidade.tipo.name}
Severidade: {vulnerabilidade.severidade.name}
Status: {vulnerabilidade.status.name} """)

class AtivoHardware(Ativo):

    def __init__(self, id_ativo, nome_hostname, responsavel, setor, tipo, ano, cor):
        super.__init__(id_ativo, nome_hostname, responsavel, setor, tipo)
        self.ano = ano
        self.cor = cor

    def to_dict(self):

        dados = super().to_dict()
        dados["ano"] = self.ano
        dados["cor"] = self.cor
        
        return dados


    def listar(self):

        super.listar()
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.ano}")
        print("-------------------------")


class AtivoSoftware(Ativo):

    def __init__(self, id_ativo, nome_hostname, responsavel, setor, tipo, versao, licenca):
        super.__init__(id_ativo, nome_hostname, responsavel, setor, tipo)
        self.versao = versao
        self.licenca = licenca if possui_licenca else None

    def to_dict(self):

        dados = super().to_dict()
        dados["versao"] = self.versao
        dados["licenca"] = self.licenca
        
        return dados


    def listar(self):

        super.listar()
        print(f"Versão: {self.versao}")
        if self.possui_licenca:
            print(f"Licença: {self.licenca}")
        else:
            print("Licença: Não possui")
        print("-------------------------")




