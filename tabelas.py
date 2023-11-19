import mysql.connector
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academiaturmab")

from time import sleep
print('=^='*20)
print('                       \033[7;40;40mBem-vindo!\033[m')
print('=^='*20)
sleep(1)
while True:
    tabela=input('Escolha uma das opções:\n[1] ->Alunos\n[2] ->Funcionários\n[3] ->Modalidades\n[4] ->Personal')
    if tabela not in['1','2','3','4']:
        print('\033[1;30;41mOPÇÃO INVÁLIDA\033[m')
        print('Escolha novamente:')
    else:
        break
sleep(1)
if tabela == '1':
    meucursor = banco.cursor()
    pesquisa = 'select * from alunos;'
elif tabela == '2':
    meucursor = banco.cursor()
    pesquisa = 'select * from funcionarios;'
elif tabela == '3':
    meucursor = banco.cursor()
    pesquisa = 'select * from modalidades;'
elif tabela == '4':
    meucursor = banco.cursor()
    pesquisa = 'select * from personal;'



