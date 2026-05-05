class BancoError(Exception):
    pass

class SaldoInsuficienteError(BancoError):
    def __init__(self, saldo_desejado: float, disponivel: float):
        self.saldo_desejado = saldo_desejado
        self.disponivel = disponivel
        super().__init__(
            f"Saldo insuficiente. "
            f"Solicitado: R$ {saldo_desejado:.2f} | "
            f"Disponível: R$ {disponivel:.2f}"
        )

class ValorInvalidoError(BancoError):
    def __init__(self, valor: float):
        self.valor = valor
        super().__init__(f"Valor inválido: R$ {valor:.2f}. Deve ser maior que zero.")

class ContaNaoEncontradaError(BancoError):
    def __init__(self, numero_conta: int):
        self.numero_conta = numero_conta
        super().__init__(f"Conta número {numero_conta} não encontrada.")


class ContaBancaria:
    def __init__(self, numero: int, titular: str, saldo: float = 0.0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self._extrato: list[str] = []

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, quantidade: float) -> None:
        if quantidade <= 0:
            raise ValorInvalidoError(quantidade)
        self._saldo += quantidade
        self._extrato.append(f"Depósito: +R$ {quantidade:.2f}")
        print(f"Depósito de R$ {quantidade:.2f} realizado.")

    def ver_extrato(self) -> None:
        if not self._extrato:
            print("Nenhuma movimentação.")
            return
        for linha in self._extrato:
            print(linha)
        print(f"Saldo atual: R$ {self._saldo:.2f}")

    def __str__(self) -> str:
        return f"Conta {self.numero} | {self.titular} | R$ {self._saldo:.2f}"


class ContaCorrente(ContaBancaria):
    def __init__(self, numero: int, titular: str, saldo: float = 0.0, limite: float = 500.0):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValorInvalidoError(valor)
        if valor > self._saldo + self.limite:
            raise SaldoInsuficienteError(valor, self._saldo + self.limite)
        self._saldo -= valor
        self._extrato.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado.")

    def __str__(self) -> str:
        return f"[Corrente] {super().__str__()} | Limite: R$ {self.limite:.2f}"


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero: int, titular: str, saldo: float = 0.0, rendimento: float = 0.5):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValorInvalidoError(valor)
        if valor > self._saldo:
            raise SaldoInsuficienteError(valor, self._saldo)
        self._saldo -= valor
        self._extrato.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado.")

    def aplicar_rendimento(self) -> None:
        valor_rendimento = self._saldo * (self.rendimento / 100)
        self._saldo += valor_rendimento
        self._extrato.append(f"Rendimento: +R$ {valor_rendimento:.2f}")
        print(f"Rendimento de R$ {valor_rendimento:.2f} aplicado.")

    def __str__(self) -> str:
        return f"[Poupança] {super().__str__()} | Rendimento: {self.rendimento}% a.m."


# Testes
cc = ContaCorrente(1001, "Ana", 1000.0)
cp = ContaPoupanca(1002, "Carlos", 2000.0)

# 1. Valor negativo na ContaCorrente
try:
    cc.sacar(-50)
except BancoError as e:
    print(f"Erro: {e}")

# 2. Excede saldo + limite na ContaCorrente
try:
    cc.sacar(9999)
except BancoError as e:
    print(f"Erro: {e}")

# 3. Excede saldo na ContaPoupanca
try:
    cp.sacar(9999)
except BancoError as e:
    print(f"Erro: {e}")

# 4. ContaNaoEncontradaError
try:
    raise ContaNaoEncontradaError(9999)
except BancoError as e:
    print(f"Erro: {e}")