from sistema import Sistema
import interface
from utils import limpar_tela, pausar, proibir_vazio, ler_opcao

sistema = Sistema()

while True:

#     print('\n---- Bem Vindo ao Sistema de Cadastro ----')
#     print("""
#    1 - Cadastrar Ativo/Vulnerabilidade
#    2 - Buscar/Listar
#    3 - Atualizar
#    4 - Remover
#    0 - Sair 
# """)
    
    limpar_tela()

    interface.mostrar_menu_principal()
    
    escolha = ler_opcao('Escolha uma opção para continuar: ')

    match escolha:

        case 0:
            break

        case 1:

            limpar_tela()

#             print("""Opções de cadastro: 
               
#    1 - Cadastrar Ativo
#    2 - Cadastrar Vulnerabilidade             
#      """)

            interface.mostrar_menu_cadastro()
            
            escolha = ler_opcao('Escolha uma opção para continuar: ')      

            match escolha:
                
                case 1:

                    limpar_tela()

                    print('Escolha o tipo de ativo a ser cadastrado.')
                    
#                     print("""Opções de cadastro: 
               
#    1 - Hardware
#    2 - Software            
#      """)
                    interface.mostrar_menu_tipo_ativo()
                    escolha = ler_opcao('Escolha uma opção para continuar: ')

                    match escolha:

                        case 1: 
                            
                            print('Digite as informações do ativo a ser cadastrado.')
                            
                            # nome_hostname = input('Nome ou nome host: ')
                            
                            # responsavel = input('Responsável: ')

                            # setor = input('Setor: ')

                            # for tipo in TipoHardware:
                            #     print(f'{tipo.value} - {tipo.name}')

                            # tipo = TipoHardware(int(input('Tipo: ')))

                            # ano = int(input("Ano: "))

                            # if tipo == TipoHardware.SERVIDOR:
                            #     cor = None

                            # else:
                            #     cor = input("Cor: ")

                            info = interface.pegar_dados_hardware()
                            sistema.cadastrar_ativo_hardware(*info)

                        case 2:

                            print('Digite as informações do ativo a ser cadastrado.')
                            
                            # nome_hostname = input('Nome ou nome host: ')
                            
                            # responsavel = input('Responsável: ')

                            # setor = input('Setor: ')

                            # for tipo in TipoSoftware:
                            #     print(f'{tipo.value} - {tipo.name}')

                            # tipo = TipoSoftware(int(input('Tipo: ')))

                            # versao = input("Versão: ")

                            # li = input("O software possui licença? (s/n): ")

                            # if li == 'n':
                            #     licenca = None

                            # else:
                            #     licenca = input("Licença: ")

                            info = interface.pegar_dados_software()
                            sistema.cadastrar_ativo_software(*info)
         
                case 2:

                    print('Digite as informações da vulnerabilidade a ser cadastrada.')

                    #ativo_buscado = input('Digite o nome/hostname ou ID do ativo buscado: ')

                    ativo_buscado = interface.pegar_ativo_buscado()
                    ativo = sistema.buscar_ativo(ativo_buscado)

                    if ativo:
                         
                        # descricao = input('Descrição: ')

                        # for vuln in TipoVulnerabilidade:
                        #     print(f'{vuln.value} - {vuln.name}')

                        # tipo = TipoVulnerabilidade(int(input('Tipo: ')))

                        # for sev in Severidade:
                        #     print(f'{sev.value} - {sev.name}')

                        # severidade = Severidade(int(input('Severidade: ')))

                        # for status in StatusTratamento:
                        #     print(f'{status.value} - {status.name}')

                        # status = StatusTratamento(int(input('Status: ')))

                        info = interface.pegar_dados_vulne()
                        sistema.cadastrar_vulne(ativo, *info)

                        # sistema.cadastrar_vulne(ativo, descricao, tipo, severidade, status)
                
                case _:
                    print("Escolha um valor válido.")
        
        case 2: 

            limpar_tela()
            
#             print("""Opções de busca: 
               
#    1 - Buscar 
#    2 - Listar todos            
#      """)

            interface.mostrar_menu_busca()
    
            escolha = ler_opcao('Escolha uma opção para continuar: ')
            
            match escolha:
                
                case 1:

                    limpar_tela()
                    #ativo_buscado = input('Digite o nome/hostname ou ID do ativo buscado: ')
                    ativo_buscado = interface.pegar_ativo_buscado()
                    ativo = sistema.buscar_ativo(ativo_buscado)

                    if ativo:
                        ativo.listar()
                        pausar()
                                     
                case 2:

                    limpar_tela()
                    sistema.listar_todos()

                case _:
                    print("Escolha um valor válido.")

        case 3:
            
            #ativo_buscado = input('Digite o nome/hostname ou ID do ativo buscado: ')
            ativo_buscado = interface.pegar_ativo_buscado()
            ativo = sistema.buscar_ativo(ativo_buscado)
            
            if ativo:

                limpar_tela()
                print('Digite as novas informações do ativo')

                # novo_nome = input('Novo nome ou nome host: ')

                # novo_responsavel = input('Novo responsável: ')

                # novo_setor = input('Novo setor: ')

                # if hasattr(ativo, "licenca"):
                    
                #     nova_versao = input("Nova versão: ")
                    
                #     licenca_atual = ativo.licenca if ativo.licenca else "Não possui"
                #     manter = input(f"Manter a licença atual ({ativo.licenca})? (s/n): ")

                #     if manter.lower() == 's':
                        
                #         nova_licenca = ativo.licenca

                #     else:
                        
                #         li = input("Possui licença? (s/n): ")
                #         nova_licenca = None if li == 'n' else input("Nova licença: ")
                    
                #     sistema.atualizar_ativo(ativo, novo_nome, novo_responsavel, novo_setor, nova_versao, nova_licenca)

                # else:

                #     sistema.atualizar_ativo(ativo, novo_nome, novo_responsavel, novo_setor)

                info = interface.coletar_atualizacao(ativo)
                sistema.atualizar_ativo(ativo, *info)
                              
        case 4: 

            limpar_tela()
            #ativo_buscado = input('Digite o nome/hostname ou ID do ativo buscado: ')
            ativo_buscado = interface.pegar_ativo_buscado()
            ativo = sistema.buscar_ativo(ativo_buscado)

            if ativo:

                sistema.excluir_ativo(ativo)

        case _: 
            print("Escolha um valor válido.")

