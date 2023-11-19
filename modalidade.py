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
    nome_modalidade = input('Nome da modalidade: ')
    atleta =input('Nome do atleta: ')
    duracao= input('Tempo de atividade:')
    sql = 'insert into modalidade (nome_modalidade,atleta,duracao) values(%s,%s,%s)'
    dados = (nome_modalidade,atleta, duracao)
    meucursor = banco.cursor()
    pesquisa = 'select * from modalidade;'
    meucursor.execute(sql, dados)
    print('Dados inseridos com sucesso.')
    banco.commit()
    meucursor.close()
    banco.close()

elif opcao =='2':
    meucursor = banco.cursor()
    pesquisa = 'select * from modalidade;'
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    print('Nossa consulta encontro o seguinte resultado:')
    for x in resultado:
        print(x)
        exit()


elif opcao =='3':
    exc=input('Qual a ID do modalidade quer deletar?')
    meucursor = banco.cursor()
    sql=f'delete from modalidade where id_modalidade={exc}'
    meucursor.execute(sql)
    print('Arquivo deletado com sucesso.')
    banco.commit()
    meucursor.close()
    banco.close()

elif opcao == '4':
    meucursor = banco.cursor()
    qm= input('Qual a ID de quem deseja alterar:')
    mat=input('Qual dado deseja atualizar:\n[1] -Nome da atividade\n[2] -Nome do atleta\n[3] -4Tempo de pratida da atividade')
    campo_alterado= input('Escreva a atualização:')

    if mat =='1':
        meucursor = banco.cursor()
        sql=f'update modalidade set nome_modalidade = "{campo_alterado}" where id_modalidade = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
    elif mat =='2':
        meucursor = banco.cursor()
        sql=f'update modalidade set atleta = "{campo_alterado}" where id_modalidade = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()
    elif mat == '3':
        meucursor = banco.cursor()
        sql = f'update modalidade set duracao = "{campo_alterado}" where id_modalidade = {qm};'
        meucursor.execute(sql)
        print('Dado atualizado.')
        banco.commit()
        meucursor.close()
        banco.close()