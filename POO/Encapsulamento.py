# Emcapsulamento

""" Consiste em restringir o acesso a atributos, metodos de um objeto, 
protegendo dados sensíveis fazendo com que sejam usados de forma correta. 

Objetivo:

- Proteger
- Controlar
- Isolar


Níveis de acesso:

Público: Acessado e alterado por qualquer pessoa.
Sintaxe: Nome normal.

Protegido: Pode ser acessado diretamente mas é indicado que o acesso seja 
restrito a subclasses ou a própria classe.
Sintaxe: _nome

Privado: Só pode ser acessado dentro da própria classe.
sintaxe: __nome """

# Exemplo

class Conta_Bancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular # Público
        self._saldo = saldo_inicial # Protegido
        self.__senha = 'Daniel123' # Privado

    
    def depositar (self, valor):
        if valor > 0:
            self._saldo += valor # Manipula saldo protegido
            print(f'Deposito no valor de \033[1;32mR${valor}\033[m')
        else:
            print(f'\033[1;4;31mFavor depositar um valor válido\033[m')

    
    def sacar(self, saque, senha):
        if senha == self.__senha: # Acessando o atributo privado dentro da classe
            if 0 < self._saldo >= saque:
                print(f"Saque de \033[1;32mR${saque}\033[m realizado com sucesso!")
                self._saldo -= saque
            elif self._saldo == 0:
                print('Seu saldo é \033[1;4;31m0\033[m impossível sacar.') 
            else:
                print('Saque impossivel de ser concluido, digite um valor válido.')   
        else:
            print(f'\033[1;4;31mSenha incorreta!!!\033[m')
    

    def consultar_saldo(self):
        return self._saldo  # Método público para acessar atributo protegido
    

    def alterar_senha(self, senha):
        if senha == self.__senha: 
            nova_senha = str(input('Digite a nova senha: '))
            self.__senha = nova_senha # Método para modificar atributo privado
            print("\033[1;4;32mSenha alterada com sucesso!\033[m")
        else:
            print(f'\033[1;4;31mSenha incorreta!!!\033[m')


# Testando Classe

conta = Conta_Bancaria('Daniel', 0)
print(conta.consultar_saldo())

conta.depositar(90)
print(conta.consultar_saldo())

conta.sacar(10, 'Daniel123')
print(conta.consultar_saldo())

conta.alterar_senha('Daniel123')


