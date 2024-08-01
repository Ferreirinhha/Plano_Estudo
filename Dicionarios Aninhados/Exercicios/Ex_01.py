""" Cadastro de alunos e suas notas: Crie um programa que permita ao usuário 
cadastrar alunos e suas notas em diferentes matérias. Permita adicionar novos 
alunos e novas matérias, e exiba o cadastro completo no final """

alunos = dict()


def cadastrar_Aluno():
    while True:
        aluno = str(input('Nome aluno: '))
        alunos[aluno]={}

        while True:
            materia = str(input('Matéria: '))
            nota = float(input('Nota: '))
            alunos[aluno][materia] = nota
            cont = str(input('Continuar [S/N]: ')).upper()[0]
            if cont == 'N':
                break

        cont = str(input('Cadastrar outro aluno [S/N]: ')).upper()[0]
        if cont == 'N':
                break
    return alunos



print(cadastrar_Aluno())

for nome, materias in alunos.items():
    print(f'       Aluno: {nome}')
    for materia, nota in materias.items():
         print(f'{materia}: {nota}')
