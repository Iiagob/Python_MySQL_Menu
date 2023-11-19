import mysql.connector
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academiaturmab")

from time import sleep
print('\33[;40;40m Tabela escolhida!Agora escolha umas das ações:\033[m')
sleep(1)
while True:
    opcao = input('[1] ->Inserir\n[2] ->Consultar\n[3] ->Deletar\n[4] ->Atualizar\n')
    if opcao not in['1','2','3','4']:
        print('\033[1;30;41mOPÇÃO INVÁLIDA\033[m')
        print('Escolha novamente:')
    else:
        break

if opcao == '1':
    nome1 = input('Nome:')
    telefone1 =input('Telefone: ')
    end1= input('Endereço:')
    cpf1=input('CPF: ')
    email1=input('E-mail:')
    sql = 'insert into alunos (nome,telefone,end,cpf,email) values(%s,%s,%s,%s,%s)'
    dados = (nome1, telefone1,end1,cpf1,email1)
    meucursor = banco.cursor()
    pesquisa = 'select * from alunos;'
    meucursor.execute(sql, dados)
    print('Dados inseridos com sucesso.')
    banco.commit()
    meucursor.close()
    banco.close()

elif opcao =='2':
    meucursor = banco.cursor()
    pesquisa = 'select * from alunos;'
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    print('Nossa consulta encontrou o seguinte resultado:')
    for x in resultado:
        print(x)
        exit()


elif opcao =='3':
    exc=input('Qual a matricula do aluno quer deletar?')
    meucursor = banco.cursor()
    sql=f'delete from alunos where matricula={exc}'
    meucursor.execute(sql)
    print('Arquivo deletado com sucesso!')
    banco.commit()
    meucursor.close()
    banco.close()

elif opcao == '4':
    meucursor = banco.cursor()
    qm= input('Qual a matricula de quem deseja alterar:')
    mat=input('Qual dado deseja atualizar:\n[1] -Nome\n[2] -Telefone\n[3] -Endereço\n[4] -CPF\n[5] -E-mail')
    campo_alterado= input('Escreva a atualização:')

    if mat =='1':
        meucursor = banco.cursor()
        sql=f'update alunos set nome = "{campo_alterado}" where matricula = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
    elif mat =='2':
        meucursor = banco.cursor()
        sql=f'update alunos set telefone = "{campo_alterado}" where matricula = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
    elif mat =='3':
        meucursor = banco.cursor()
        sql=f'update alunos set end = "{campo_alterado}" where matricula = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
    elif mat =='4':
        meucursor = banco.cursor()
        sql=f'update alunos set cpf = "{campo_alterado}" where matricula = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
    elif mat =='5':
        meucursor = banco.cursor()
        sql=f'update alunos set email = "{campo_alterado}" where matricula = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
