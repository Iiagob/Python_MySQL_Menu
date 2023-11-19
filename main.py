continuar='S'
while continuar.upper()=='S':

    from tabelas import *
    if tabela =='1':
        from alunos import *

    elif tabela =='2':
        from funcionarios import *

    elif tabela =='3':
        from modalidade import *

    elif tabela =='4':
        from personal import *

    else:
        print('Opção invalida!')

    continuar=input('Deseja refazer a consulta?')
