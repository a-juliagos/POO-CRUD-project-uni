from enums import TipoHardware, TipoSoftware, TipoVulnerabilidade, Severidade, StatusTratamento
from utils import proibir_vazio, ler_opcao, ler_enum

def mostrar_menu_principal():

    print('\n---- Bem Vindo ao Sistema de Cadastro ----')
    print("""
   1 - Cadastrar Ativo/Vulnerabilidade
   2 - Buscar/Listar
   3 - Atualizar
   4 - Remover
   0 - Sair 
""")
    
def mostrar_menu_cadastro():

    print("""Opções de cadastro: 
               
   1 - Cadastrar Ativo
   2 - Cadastrar Vulnerabilidade             
     """)
    
def mostrar_menu_tipo_ativo():

     print("""Opções de cadastro: 
               
   1 - Hardware
   2 - Software            
     """)

def mostrar_menu_busca():

    print("""Opções de busca: 
               
   1 - Buscar 
   2 - Listar todos            
     """)
    
def pegar_ativo_buscado():

    return proibir_vazio('Digite o nome/hostname ou ID do ativo buscado: ')


def pegar_dados_hardware():
                            
    nome_hostname = input('Nome ou nome host: ')
                            
    responsavel = input('Responsável: ')

    setor = input('Setor: ')

    for tipo in TipoHardware:
        
        print(f'{tipo.value} - {tipo.name}')

    tipo = TipoHardware(int(input('Tipo: ')))

    ano = int(input("Ano: "))

    if tipo == TipoHardware.SERVIDOR:
        cor = None

    else:
        cor = input("Cor: ")

    return nome_hostname, responsavel, setor, tipo, ano, cor


def pegar_dados_software():

    print('Digite as informações do ativo a ser cadastrado.')
                            
    nome_hostname = input('Nome ou nome host: ')
                            
    responsavel = input('Responsável: ')

    setor = input('Setor: ')

    for tipo in TipoSoftware:
        print(f'{tipo.value} - {tipo.name}')

    tipo = TipoSoftware(int(input('Tipo: ')))

    versao = input("Versão: ")

    li = input("O software possui licença? (s/n): ")

    if li == 'n':
        licenca = None

    else:
        licenca = input("Licença: ")

    return nome_hostname, responsavel, setor, tipo, versao, licenca

def pegar_dados_vulne():

    descricao = input('Descrição: ')

    for vuln in TipoVulnerabilidade:
        print(f'{vuln.value} - {vuln.name}')

    tipo = TipoVulnerabilidade(int(input('Tipo: ')))

    for sev in Severidade:
        print(f'{sev.value} - {sev.name}')

    severidade = Severidade(int(input('Severidade: ')))

    for status in StatusTratamento:
        print(f'{status.value} - {status.name}')

    status = StatusTratamento(int(input('Status: ')))

    return descricao, tipo, severidade, status

def pegar_dados_atualizacao(ativo):

    novo_nome = proibir_vazio('Novo nome ou nome host: ')
    novo_responsavel = proibir_vazio('Novo responsável: ')
    novo_setor = proibir_vazio('Novo setor: ')

    if hasattr(ativo, "licenca"):

        nova_versao = proibir_vazio("Nova versão: ")

        licenca_atual = ativo.licenca if ativo.licenca else "Não possui"
        manter = input(f"Manter a licença atual ({licenca_atual})? (s/n): ")

        if manter.lower() == 's':
            nova_licenca = ativo.licenca
        else:
            possui_licenca = input("Possui licença? (s/n): ")
            nova_licenca = proibir_vazio("Nova licença: ") if possui_licenca.lower() == 's' else None

        return novo_nome, novo_responsavel, novo_setor, nova_versao, nova_licenca

    return novo_nome, novo_responsavel, novo_setor, None, None
                






