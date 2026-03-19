# Desafios alura - OO

# 1- Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
#Inicie o atributo ativo como False por padrão.

class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

# 2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e
# o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f"Nome do titular: {self.titular}, Saldo em conta: {self.saldo}"

pessoa1 = ContaBancaria("Gustavo", 1000)
pessoa2 = ContaBancaria("Breno", -1000)
print(pessoa1)
print(pessoa2)

#  3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True.
# Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f"Nome do titular: {self.titular}, Saldo em conta: {self.saldo}, Conta ativada: {self.ativo}"

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

pessoa_1 = ContaBancaria("Breno", 1000,)
ContaBancaria.ativar_conta(pessoa_1)
print(pessoa_1)
