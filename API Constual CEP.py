import requests
import json
import os

def main():
    os.system('cls')
    print('='*16)
    print('| Consulta CEP |')
    print('='*16)
    cep_input = input('Digite o CEP para consulta: ')

    os.system('cls')

    if len(cep_input) != 8:
        print('Quantidade de digitos invalida\n')
        print('='*41)
        print('|  Deseja realizar uma nova consulta ? |')
        print('| [1] Sim                              |')
        print('| [2] Não                              |')
        print('='*41)
    
        option = int(input('Selecione uma das opções: '))

        if option == 1:
            os.system('cls')
            main()
        else:
            os.system('cls')
            print('Saindo...')
            quit()


    request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')

    addres_data = request.json()

    if 'erro' not in addres_data:
        print('==> CEP encontrado <==')
        print('CEP:', addres_data['cep'])
        print('Logradouro:', addres_data['logradouro'])
        if addres_data['complemento'] == '':
            print('Não existe complemento')
        else:
            print('Coplemento:', addres_data['complemento'])
        print('Bairro:', addres_data['bairro'])
        print('Cidade:', addres_data['localidade'])
        print('Estado:', addres_data['uf'], '\n')
    else:
        print('CEP invalido')

    print('='*41)
    print('|  Deseja realizar uma nova consulta ? |')
    print('| [1] Sim                              |')
    print('| [2] Não                              |')
    print('='*41)

    option = int(input('Selecione uma das opções: '))

    if option == 1:
        os.system('cls')
        main()
    else:
        os.system('cls')
        print('Saindo...')
        quit()

if __name__ == '__main__':
    main()