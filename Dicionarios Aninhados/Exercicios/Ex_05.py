""" Atualização de notas: Implemente um programa que permita ao usuário 
atualizar a nota de um aluno em uma matéria específica. O programa deve 
verificar se o aluno e a matéria existem antes de atualizar """

alunos = {
    "Daniel":{
        "Matemática": 10.0,
        "História": 5.5,
        "Ciências": 6.7,
        "Geografia": 7.7
    },
    "Karine":{
        "Matemática": 5.0,
        "História": 7.5,
        "Ciências": 8.7,
        "Geografia": 5.7
    }
}



busca = str(input('Aluno: '))

for aluno, materia in alunos.items():
    if busca == aluno:
        busca2 = str(input('Matéria: '))
        if busca2 in materia:
            nova_nota = float(input('Nova nota: '))
            materia[busca2] = nova_nota
            break
        else:
            print(f'\033[1;31mA matéria \033[1;33m{busca2}\033[m \033[1;31mnão existe.\033[m')
    else:
        print('Aluno não encontrado')

print(alunos)