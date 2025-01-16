# Funções que usam a palavran chave (async)
# Boa para trabalhar com tarefas que podem levar tempo como Acessar a internet.


""" 
Definição com (async def)

Função assincrona, chamada de corritina. Essas funções não execultam diretamente o código;
ao invés disso, retornam um objeto de corritina que pode ser aguardado com (await)
"""

"""
Execução com (await)

Dentro da função assincrona, usamos await para 'pausar' a execução enquanto esperamos por algo 
que leva tempo:
"""


import asyncio

async def tarefa(nome, tempo):
    print(f'Tarefa {nome} começou...')
    await asyncio.sleep(tempo) #Simula esperar algo demorado
    print(f'Tarefa {nome} terminou depois de {tempo} segundos.')


# Rodar as tarefas assíncronas

async def main():
    await asyncio.gather(
        tarefa('A', 2),
        tarefa('B', 3),
        tarefa('C', 1),
    )

asyncio.run(main())