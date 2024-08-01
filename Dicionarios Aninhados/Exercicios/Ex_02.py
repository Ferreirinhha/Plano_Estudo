""" Consulta de notas específicas: Escreva um programa que, dado um aluno de 
aluno e uma matéria, exiba a nota desse aluno na matéria especificada. Se o 
aluno ou a matéria não existir, informe ao usuário """

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


def buscar(aluno):
    for i, alu in enumerate(alunos):
        if alu == aluno:
            materia = str(input(f'Qual matéria gostaria de ver do aluno {aluno}: ')).capitalize()
            for i, materias in enumerate(alunos[aluno]):
                if materias == materia:
                    print(f'{materia} = {alunos[aluno][materia]}')
                    break
                elif i == len(alunos[aluno]) - 1:
                    print('Materia não encontrada.')
            break
        elif i == len(alunos) - 1:
            print('Aluno não encontrado.')


while True:
    aluno = str(input('Aluno: ')).capitalize()
    buscar(aluno)
    cont = str(input('Continuar [S/N]: ')).upper()[0]
    if cont == 'N':
        break
print('Fim!!! ')

# Gpt

nome1 = input("Digite o nome do aluno: ")
materia1 = input("Digite a matéria: ")

if nome1 in alunos and materia1 in alunos[nome1]:
    nota = alunos[nome1][materia1]
    print(f"A nota de {nome1} em {materia1} é {nota}")
else:
    print("Aluno ou matéria não encontrado.")
