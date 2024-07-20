""" Em uma escola, você tem uma lista de alunos matriculados em um curso. 
Você quer saber quantos alunos estão realmente inscritos, sem repetições. """

lista_alunos = ["Maria", "Joao", "Maria", "Ferreirinha", "Fernando", "Fernando" ]

alunos_unicos = set(lista_alunos)

print(f'Alunos inscritos: {len(alunos_unicos)}')