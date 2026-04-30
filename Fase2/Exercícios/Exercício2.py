# Classe pai já fornecida — não modifique
class ContaBancaria:
    def __init__(self, numero: int, titular: str, saldo: float = 0.0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self._extrato: list[str] = []

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            print("Valor inválido.")
            return
        self._saldo += valor
        self._extrato.append(f"Depósito: +R$ {valor:.2f}")

    def ver_extrato(self) -> None:
        print(f"\n--- Extrato | Conta {self.numero} | {self.titular} ---")
        if not self._extrato:
            print("Nenhuma movimentação.")
        for linha in self._extrato:
            print(linha)
        print(f"Saldo atual: R$ {self._saldo:.2f}")

    def __str__(self) -> str:
        return f"Conta {self.numero} | {self.titular} | R$ {self._saldo:.2f}"


# Implemente as duas classes abaixo:

class ContaCorrente(ContaBancaria):
    # atributo extra: limite (float, padrão 500.0)
    # sacar: pode usar o saldo + limite, registra no extrato
    # __str__: "[Corrente] Conta 1001 | Ana | R$ 1000.00 | Limite: R$ 500.00"
    def __init__(self, numero, titular, saldo = 0, limite: float = 500.0):
        super().__init__(numero, titular, saldo)
        self.limite = limite
    
    def sacar(self, valor: float) -> None:
        if valor < 0 :
            print("Valor inválido")
            return
        if valor >self.limite +self._saldo:
            print("Valor maior do que o permitido")
            return
        self._saldo -= valor
        self._extrato.append(f"Saque de R${valor:.2f}")
        print("Saque realizado com sucesso")

    def __str__(self):
        return f"[CORRENTE] {super().__str__()} | Limite: R${self.limite:.2f}" 

class ContaPoupanca(ContaBancaria):
    # atributo extra: rendimento (float, padrão 0.5 — percentual mensal)
    # sacar: só o saldo disponível, sem limite, registra no extrato
    # aplicar_rendimento: aplica o percentual sobre o saldo, registra no extrato
    # __str__: "[Poupança] Conta 1002 | Carlos | R$ 2000.00 | Rendimento: 0.5% a.m."
    def __init__(self, numero, titular, saldo = 0, rendimento: float = 0.5):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento
    def sacar(self, valor: float) -> None:
        if valor < 0 :
            print("Não é possivel realizar a operação poi o valor é menor do que zero")
            return
        if self._saldo <valor:
            print("Saldo insuficiente")
            return
        self._saldo -= valor
        self._extrato.append(f"Saque R${valor:.2f}")
    def aplicarRendimento (self) -> None:
        valorRendimento = self._saldo*(self.rendimento/100)
        self._saldo += valorRendimento
        self._extrato.append(f"Rendimento de R${valorRendimento:.2f}")

    def __str__(self):
        return f"[Poupança] {super().__str__()} | Rendimento: {self.rendimento:.2f}"
     