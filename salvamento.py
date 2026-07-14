import json

def salvar_dados(dados):

    with open("ativos.json", "w", encoding="utf-8") as arquivo:

        json.dump(
        
        dados, 
        arquivo, 
        ensure_ascii=False, 
        indent=4
        
        )

def carregar_dados():

    try:

        with open("ativos.json", "r", encoding="utf-8") as arquivo:
            
            return json.load(arquivo)
        
    except (FileNotFoundError, json.JSONDecodeError):

        return []