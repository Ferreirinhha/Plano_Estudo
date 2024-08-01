""" Aluno com maior nota em uma matéria específica: Faça um programa que
determine qual aluno obteve a maior nota em uma matéria específica fornecida 
pelo usuário. """


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


maior_nota = 0
aluno_maior_nota = ''

busca = str(input('Matéria: '))

# for aluno, materia in alunos.items():
#     for materias, notas in materia.items():  não é necessário esse loop pois podemos acessar a nota diretamente da matéria
#         if materias == busca:
#             if maior_nota < notas:
#                 maior_nota = notas
#                 aluno_maior_nota = aluno



for aluno, materia in alunos.items(): # Resultado 1 loop : Daniel {'Matemática': 10.0, 'História': 5.5, 'Ciências': 6.7, 'Geografia': 7.7}
    if busca in materia: # oque acessamos aqui 'Matemática': 10.0, 'História': 5.5, 'Ciências': 6.7, 'Geografia': 7.7}
        if materia[busca] > maior_nota:
            maior_nota = materia[busca]
            aluno_maior_nota = aluno
print(f'A maior nota de {busca} foi do aluno(a) {aluno_maior_nota} com a nota: {maior_nota}') 