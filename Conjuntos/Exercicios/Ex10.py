""" Exercício 10: Crie dois conjuntos que representem as notas de dois alunos em uma prova. 
Em seguida, encontre quais notas foram tiradas por pelo menos um dos alunos (união) e quais notas foram 
tiradas por ambos (interseção). Imprima ambos os resultados """

notas_aluno1 = {85, 90, 78, 92}
notas_aluno2 = {78, 85, 88, 95}

uniao_notas = notas_aluno1 | notas_aluno2
intersecao_notas = notas_aluno1 & notas_aluno2

print(uniao_notas)        # Resultado: {78, 85, 88, 90, 92, 95}
print(intersecao_notas)   # Resultado: {78, 85}
