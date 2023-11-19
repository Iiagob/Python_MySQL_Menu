import mysql.connector
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academiaturmab")

from time import sleep
print('\33[;40;40m Tabela escolhida!Agora escolha umas das ações:\033[m')
while True:
    opcao = input('[1] ->Inserir\n[2] ->Consultar\n[3] ->Deletar\n[4] ->Atualizar\n')
    if opcao not in['1','2','3','4']:
        print('\033[1;30;41mOPÇÃO INVÁLIDA\033[m')
        print('Escolha novamente:')
    else:
        break
sleep(1)
if opcao == '1':
    cpf = input('CPF:')
    nome =input('Nome: ')
    telefone= input('Telefone:')
    endereco=input('Endereço:')
    sql = 'insert into funcionarios (cpf,nome,telefone,endereco) values(%s,%s,%s,%s)'
    dados = (cpf, nome,telefone,endereco)
    meucursor = banco.cursor()
    pesquisa = 'select * from funcionarios;'
    meucursor.execute(sql, dados)
    print('Dados inseridos com sucesso.')
    banco.commit()
    meucursor.close()
    banco.close()

elif opcao =='2':
    meucursor = banco.cursor()
    pesquisa = 'select * from funcionarios;'
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    print('Nossa consulta encontrou o seguinte resultado:')
    for x in resultado:
        print(x)
        exit()


elif opcao =='3':
    exc=input('Qual a ID do funcionario quer deletar?')
    meucursor = banco.cursor()
    sql=f'delete from funcionarios where id_funcionario={exc}'
    meucursor.execute(sql)
    print('Arquivo deletado com sucesso.')
    banco.commit()
    meucursor.close()
    banco.close()

elif opcao == '4':
    meucursor = banco.cursor()
    qm= input('Qual a ID de quem deseja alterar:')
    mat=input('Qual dado deseja atualizar:\n[1] -CPF\n[2] -Nome\n[3] -Telefone\n[4] -Endereço')
    campo_alterado= input('Escreva a atualização:')

    if mat =='1':
        meucursor = banco.cursor()
        sql=f'update funcionarios set cpf = "{campo_alterado}" where id_funcionario = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
    elif mat =='2':
        meucursor = banco.cursor()
        sql=f'update funcionarios set nome = "{campo_alterado}" where id_funcionario = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
    elif mat =='3':
        meucursor = banco.cursor()
        sql=f'update funcionarios set telefone = "{campo_alterado}" where id_funcionario = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
    elif mat =='4':
        meucursor = banco.cursor()
        sql=f'update funcionarios set endereco = "{campo_alterado}" where id_funcionario = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
