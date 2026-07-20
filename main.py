from sistema import Sistema
import interface
from time import sleep
from utils import limpar_tela, pausar, ler_opcao

sistema = Sistema()

while True:

    limpar_tela()
    interface.mostrar_menu_principal()
    escolha = ler_opcao('Escolha uma opção para continuar: ')

    match escolha:

        case 0:
            print("Encerrando sistema...")
            sleep(2)
            break

        case 1:
            limpar_tela()
            interface.mostrar_menu_cadastro()
            escolha = ler_opcao('Escolha uma opção para continuar: ')      

            match escolha:
                
                case 1:
                    limpar_tela()
                    print('Escolha o tipo de ativo a ser cadastrado.')
                    interface.mostrar_menu_tipo_ativo()
                    escolha = ler_opcao('Escolha uma opção para continuar: ')

                    match escolha:

                        case 1:  
                            print('Digite as informações do ativo a ser cadastrado.')
                            info = interface.pegar_dados_hardware()
                            sucesso, mensagem = sistema.cadastrar_ativo_hardware(*info)
                            print(mensagem)
                            pausar()

                        case 2:
                            print('Digite as informações do ativo a ser cadastrado.')
                            info = interface.pegar_dados_software()
                            sucesso, mensagem = sistema.cadastrar_ativo_software(*info)
                            print(mensagem)
                            pausar()
         
                case 2:
                    limpar_tela()
                    print('Digite as informações da vulnerabilidade a ser cadastrada.')
                    ativo_buscado = interface.pegar_ativo_buscado()
                    ativo, mensagem = sistema.buscar_ativo(ativo_buscado)

                    if ativo:
                        info = interface.pegar_dados_vulne()
                        sucesso, mensagem = sistema.cadastrar_vulne(ativo, *info)
                        print(mensagem)
                        pausar()

                    else:
                        print(mensagem)
                        pausar()
                
                case _:
                    print("Escolha um valor válido.")
                    pausar()
        
        case 2: 
            limpar_tela()
            interface.mostrar_menu_busca()
            escolha = ler_opcao('Escolha uma opção para continuar: ')
            
            match escolha:
                
                case 1:
                    limpar_tela()
                    ativo_buscado = interface.pegar_ativo_buscado()
                    ativo, mensagem = sistema.buscar_ativo(ativo_buscado)

                    if ativo:
                        ativo.listar()
                        pausar()

                    else:
                        print(mensagem)
                        pausar()
                                     
                case 2:
                    limpar_tela()
                    sistema.listar_todos()
                    pausar()

                case _:
                    print("Escolha um valor válido.")
                    pausar()

        case 3:
            limpar_tela()
            ativo_buscado = interface.pegar_ativo_buscado()
            ativo, mensagem = sistema.buscar_ativo(ativo_buscado)
            
            if ativo:
                limpar_tela()
                print('Digite as novas informações do ativo')
                info = interface.pegar_dados_atualizacao(ativo)
                sucesso, mensagem = sistema.atualizar_ativo(ativo, *info)
                print(mensagem)
                pausar()

            else:
                print(mensagem)
                pausar()
                              
        case 4: 
            limpar_tela()
            ativo_buscado = interface.pegar_ativo_buscado()
            ativo, mensagem = sistema.buscar_ativo(ativo_buscado)

            if ativo:
                sucesso, mensagem = sistema.excluir_ativo(ativo)
                print(mensagem)
                pausar()
            
            else:
                print(mensagem)
                pausar()

        case _: 
            print("Escolha um valor válido.")
            pausar()

