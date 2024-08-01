# Dicionários aninhados

alunos = {
    "Maria":{
        "Matemática":5.5,
        "Ciências":9.7,
        "História":6.9
    },
    "Daniel":{
        "Matemática":5.5,
        "Ciências":5.7,
        "História":7.9
    },
    "José":{
        "Matemática":9.5,
        "Ciências":1.7,
        "História":3.9
    },
    "Marcos":{
        "Matemática":5.7,
        "Ciências":8.9,
        "História":6.5
    },
}

# Acessar 

nota_jose_ciencias = alunos["José"]["Matemática"]

print(nota_jose_ciencias) # 9.5

# Mudar notas 

alunos['Maria']['História'] = 8.0

print(alunos["Maria"]["História"]) # 8.0

# Acessar usando Loops

for aluno, notas in alunos.items():
    print(f'        Aluno: {aluno}')
    for materia, nota in notas.items():
        print(f'Materia: {materia}  notas: {nota}')

