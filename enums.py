from enum import IntEnum

## TipoHardware e TipoSoftware substituem a classe TipoAtivo que misturava objetos diferentes e dificultava a separação dos objetos (com muitos if's)

class TipoHardware(IntEnum):

    NOTEBOOK = 1
    SERVIDOR = 2
    IMPRESSORA_DE_REDE = 3

class TipoSoftware(IntEnum):

    BANCO_DE_DADOS = 3
    SOFTWARE_LICENCIADO = 4

class TipoVulnerabilidade(IntEnum):

    QUEBRADO = 1
    DESATUALIZADO = 2
    COM_DEFEITO = 3
    SEM_SEGURANCA = 4
    MAL_CONFIGURADO = 5

class Severidade(IntEnum):

    BAIXA = 1
    MEDIA = 2
    ALTA  = 3
    CRITICA = 4 

class StatusTratamento(IntEnum):

    AGUARDANDO = 1
    EM_PROCESSO = 2
    CORRIGIDA = 3
    RISCO_ACEITO = 4
