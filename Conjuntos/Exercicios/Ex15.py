""" Em uma loja, você tem uma lista de produtos que estão em estoque e outra lista de produtos 
que foram vendidos. Você deseja encontrar quais produtos ainda estão disponíveis """

produtos_estoque = {"Macarrão", "Feijão", "Fandangos", "Azeitona", "Coca-Cola"}
produtos_vendidos = {"Macarrão",  "Azeitona", "Feijão"}

produtos_disponiveis = produtos_estoque - produtos_vendidos

print(produtos_disponiveis)

