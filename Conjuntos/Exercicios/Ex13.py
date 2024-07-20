""" Você e seus amigos fazem uma lista dos hobbies que têm. Você quer saber quais hobbies são comuns entre 
vocês. """

meus_hobbies = {"Violão", "Leitura", "Jogar"}
amigos_hobbies = {"Futebol", "Volei", "Violão"}

hobbies_parecidos = meus_hobbies & amigos_hobbies

print(hobbies_parecidos)