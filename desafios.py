# Desafios alura - OO

# 1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
# Inicie o atributo ativo como False por padrão.

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

 # 3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True.
# Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f"Nome do titular: {self.titular}, Saldo em conta: {self.saldo}, Conta ativada: {self.ativo}"

    def ativar_conta(self):
        self.ativo = True

pessoa_1 = ContaBancaria("Breno", 1000,)
pessoa_1.ativar_conta()
print(pessoa_1)

# 4 - Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos.
# Utilize propriedades, se necessário.

class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Nome do titular: {self._titular}, Saldo em conta: {self._saldo}, Status conta: {self.ativo}"

    def ativar_conta(self):
        self._ativo = True

    @property
    def ativo(self):
        return 'Ativada' if self._ativo else 'Desativada'

pessoa_1 = ContaBancaria("Breno", 1000,)
pessoa_1.ativar_conta()
print(pessoa_1)

# 5 - Crie uma instância da classe e imprima o valor da propriedade titular.
# class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Nome do titular: {self._titular}, Saldo em conta: {self._saldo}, Status conta: {self.ativo}"

    def ativar_conta(self):
        self._ativo = True

    @property
    def ativo(self):
        return 'Ativada' if self._ativo else 'Desativada'

    @property
    def titular(self):
        return self._titular

pessoa_1 = ContaBancaria("Breno", 1000,)
pessoa_1.ativar_conta()
print(pessoa_1.titular)

# 6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe
# e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:
    def __init__(self, titular, idade, saldo, ano_criacao_da_conta, etnia):
        self._titular = titular
        self._idade = idade
        self._saldo = saldo
        self._etnia = etnia
        self._ano_criacao_da_conta = ano_criacao_da_conta

    def __str__(self):
        return f"Titular: {self._titular} | Idade: {self._idade} | Saldo: R$ {self._saldo:.2f} | Etnia: {self._etnia} | Conta criada em: {self._ano_criacao_da_conta}"

cliente_1 = ClienteBanco("Ana Costa", 34, 8750.00, 2019, "Parda")
cliente_2 = ClienteBanco("Carlos Mendes", 52, 142300.00, 2005, "Branco")
cliente_3 = ClienteBanco("Juliana Souza", 27, 1200.00, 2022, "Negra")
print(cliente_1)
print(cliente_2)
print(cliente_3)