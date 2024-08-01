""" Cálculo da média das notas: Crie um programa que calcule e exiba a média das 
notas de cada aluno em todas as matérias. Exiba também a média geral da turma """

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


cont = 0 
soma_geral = 0

for aluno, materia in alunos.items():
    soma = sum(materia.values())
    print(f'Média do aluno(a) {aluno}: {soma/ len(materia)}')
    soma_geral += soma
    cont += len(materia)
print(f'Média geral dos alunos: {soma_geral / cont}')