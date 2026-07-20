from ativos import AtivoHardware, AtivoSoftware
from vulnerabilidades import Vulnerabilidade
from enums import TipoHardware, TipoSoftware, TipoVulnerabilidade, Severidade, StatusTratamento
from salvamento import salvar_dados, carregar_dados

class Sistema:

    def __init__(self):
        
        self.ativos = []
        self.id_ativo = 1

        self.carregar()

## Funções que se comunicam com o main.py
## Funções (Métodos) de cadastramento (ativos e vulnerabilidades), busca, listagem e exclusão
## Funções limpas sem print e input (Boas práticas)

    def cadastrar_ativo_hardware(
            
        self,         
        nome_hostname,
        responsavel,
        setor,
        tipo, 
        ano,
        cor

        ):

        ativo = AtivoHardware(

            self.id_ativo,
            nome_hostname,
            responsavel,
            setor,
            tipo,
            ano,
            cor
            
            )
        
        self.ativos.append(ativo)
        self.id_ativo += 1

        self.salvar()
                                      
        return True, 'Ativo cadastrado com sucesso!!'


    def cadastrar_ativo_software(
            
        self,         
        nome_hostname,
        responsavel,
        setor,
        tipo, 
        versao,
        licenca

        ):

        ativo = AtivoSoftware(

            self.id_ativo,
            nome_hostname,
            responsavel,
            setor,
            tipo,
            versao,
            licenca
            
            )
        
        self.ativos.append(ativo)
        self.id_ativo += 1

        self.salvar()
                                      
        return True, 'Ativo cadastrado com sucesso!!'
        

    def cadastrar_vulne(
        
        self,
        ativo,
        descricao,
        tipo,
        severidade,
        status
        ):

        vulne = Vulnerabilidade(

            descricao,
            tipo,
            severidade,
            status
        )

        ativo.vulnerabilidades.append(vulne)

        self.salvar()
        
        return True, 'Vulnerabilidade cadastrada com sucesso!!'


    def buscar_ativo(self, ativo_buscado):
        
        if not self.ativos:

              return None, 'Não existem Ativos cadastrados!!'

        if ativo_buscado.isdigit():
            ativo_buscado = int(ativo_buscado)

        for ativo in self.ativos:
            
            if (isinstance(ativo_buscado, str)
        and ativo_buscado.lower() == ativo.nome_hostname.lower() ): 
                
                return ativo, 'Ativo encontrado com sucesso!!'

            if ativo_buscado == ativo.id_ativo:
                
                return ativo, 'Ativo encontrado com sucesso!!'
      
        return None, 'O ativo não existe ou foi excluído.'


    def listar_todos(self):
        
        for ativo in self.ativos:

            ativo.listar()


    def atualizar_ativo(
            
        self,
        ativo,
        novo_nome,
        novo_responsavel,
        novo_setor,
        nova_versao=None,
        nova_licenca=None

        ):

        ativo.nome_hostname = novo_nome
        ativo.responsavel = novo_responsavel
        ativo.setor = novo_setor

        if hasattr(ativo, "licenca"):

            ativo.versao = nova_versao
            ativo.licenca = nova_licenca

        self.salvar()

        return True, 'Ativo atualizado com sucesso!!'
        

    def excluir_ativo(self, ativo):
        
        nome = ativo.nome_hostname
        
        self.ativos.remove(ativo)

        self.salvar()
        
        return True, f'O ativo {nome} foi excluído com sucesso!!'


## Funções que se comunicam com salvamento.py (json)


    def salvar(self):
        
        dados = [
           
           ativo.to_dict() 
           for ativo in self.ativos

           ]
       
        salvar_dados(dados)


    def carregar(self):
        
        dados = carregar_dados()
        self.ativos = []

        for item in dados:
            
            if "ano" in item:
                
                ativo = AtivoHardware(
                item["id"],
                item["nome"],
                item["responsavel"],
                item["setor"],
                TipoHardware[item["tipo"]],
                item["ano"],
                item["cor"]
            )
            else:
                
                ativo = AtivoSoftware(
                item["id"],
                item["nome"],
                item["responsavel"],
                item["setor"],
                TipoSoftware[item["tipo"]],
                item["versao"],
                item["licenca"]
            )

            for vuln in item.get("vulnerabilidades", []):
                ativo.vulnerabilidades.append(
                Vulnerabilidade(
                    vuln["descricao"],
                    TipoVulnerabilidade[vuln["tipo"]],
                    Severidade[vuln["severidade"]],
                    StatusTratamento[vuln["status"]]
                )
            )

            self.ativos.append(ativo)

        if self.ativos:

            self.id_ativo = max(
            ativo.id_ativo 
            for ativo in self.ativos
            ) + 1



