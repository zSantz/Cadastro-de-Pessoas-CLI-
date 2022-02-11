print('#############################')
print('SISTEM DE CADASTRO DE PESSOAS')
print('#############################\n')

init_system = input('Para iniciar o sistema digite entrar: ')
print ("\n" * 130)

dados_cadastrais = {}
while init_system == 'entrar' and 'Entrar':
    print('######################################################')
    print('Bem vindo ao Sistem de cadastro de pessoas em python!!')
    print('######################################################')

    print('- Para se cadastrar digite "cadastro"'
          '\n- Para consultar digite "consulta"'
          '\n- Para sair digite "sair"')
    menu_op = input('Digite uma opção: ')
    print('######################################################')
    print("\n" * 130)

    if menu_op == 'cadastro':
        dados_cadastrais['NOME'] = input('Digite seu Nome: ')
        dados_cadastrais['CPF'] = input('Digite seu CPF: ')
        dados_cadastrais['ENDEREÇO'] = input("Digite seu Endereço: ")
        dados_cadastrais['IDADE'] = input('Digite sua Idade: ')
        dados_cadastrais['ALTURA'] = input('Digite sua Altura: ')
        dados_cadastrais['TELEFONE'] = input('Digite seu Telefone: ')
        print('\n######################################################')
        print('CADASTRO EFETUADO COM SUCESSO')
    elif menu_op == 'consulta':
        print('######################################################')
        print('Nome: ', dados_cadastrais['NOME'], '\nCPF: ', dados_cadastrais['CPF'],
                '\nEndereço: ', dados_cadastrais['ENDEREÇO'], "\nIdade: ", dados_cadastrais['IDADE'],
                '\nAltura: ', dados_cadastrais['ALTURA'], '\nTelefone: ', dados_cadastrais['TELEFONE'])
    elif menu_op == 'sair':
        break
print('O sistema foi encerrado. Obrigado e volte sempre :)')