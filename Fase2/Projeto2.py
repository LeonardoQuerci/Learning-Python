import json
import os

# suas exceções aqui
class BancoError(Exception):
    pass
class SaldoInsuficiente(BancoError):
    def __init__(self, valorDesejado: float, valorDisponivel: float):
        self.valorDesejado = valorDesejado
        self.valorDisponivel = valorDisponivel
        super().__init__(
            f"Saldo insuficiente. "
            f"Solicitado: R$ {valorDesejado:.2f} | "
            f"Disponível: R$ {valorDisponivel:.2f}"
        )
class valorInvalidoErro(BancoError):
    def __init__(self, valor: float):
        self.valor = valor
        super().__init__(
            f"Valor inválido: R$ {valor:.2f}. Deve ser maior que zero."
        )
class contaNaoEncontrada(BancoError):
    def __init__(self, conta: int):
        self.conta = conta
        super().__init__(f"Conta número {conta} não encontrada.")
class semMovimentacao(BancoError):
    def __init__(self):
        super().__init__(f"Sem movimentação na conta ainda")

# suas classes aqui
class ContaBancaria:
    def __init__(self, numero: int, titular: str, saldo: float = 0.0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self._extrato: list[str] = []
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    def para_dict(self) -> dict:
        return {
            "tipo": "ContaBancaria",  # guarda o tipo para saber qual classe recriar
            "numero": self.numero,
            "titular": self.titular,
            "saldo": self._saldo,
            "extrato": self._extrato
        }
    
    def depositar (self,quantia: float) -> None:
        if quantia <= 0:
            raise valorInvalidoErro(quantia)
        self._saldo += quantia
        self._extrato.append(f"Depósito: += R$ {quantia:.2f}")
        print(f"Depósito de R${quantia:.2f} realizado")

    def mostrarExtrato(self) -> None:
        if not self._extrato:
            raise semMovimentacao()
        for linha in self._extrato:
            print(linha)
        print(f"Saldo atual: R${self._saldo:.2f}");
    
    def __str__(self) -> str:
        return f"Conta {self.numero} | {self.titular} | R$ {self._saldo:.2f}"
    
class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo = 0, limite: float = 500.0):
        super().__init__(numero, titular, saldo)
        self.limite = limite
    def sacar(self, valor: float) -> None:
        if valor <= 0: 
            raise valorInvalidoErro(valor)
        elif valor > self._saldo + self.limite :
            raise SaldoInsuficiente(valor, self._saldo + self.limite) 
        self._saldo -= valor
        self._extrato.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado.")

    def para_dict(self) -> dict:
        dados = super().para_dict()  # pega o dict do pai
        dados["tipo"] = "ContaCorrente"  # sobrescreve o tipo
        dados["limite"] = self.limite    # adiciona o campo extra
        return dados
    
    def __str__(self):
        return f"[Corrente] {super().__str__()} | Limite: R$ {self.limite:.2f}"

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero: int, titular: str, saldo: float = 0.0, rendimento: float = 0.5):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise valorInvalidoErro(valor)
        if valor > self._saldo:
            raise SaldoInsuficiente(valor, self._saldo)
        self._saldo -= valor
        self._extrato.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado.")

    def aplicarRendimento(self) -> None:
        valor_rendimento = self._saldo * (self.rendimento / 100)
        self._saldo += valor_rendimento
        self._extrato.append(f"Rendimento: +R$ {valor_rendimento:.2f}")
        print(f"Rendimento de R$ {valor_rendimento:.2f} aplicado.")

    def para_dict(self) -> dict:
        dados = super().para_dict()
        dados["tipo"] = "ContaPoupanca"
        dados["rendimento"] = self.rendimento
        return dados
    
    def __str__(self) -> str:
        return f"[Poupança] {super().__str__()} | Rendimento: {self.rendimento}% a.m."   

def de_dict(dados: dict) -> ContaBancaria:
    if dados["tipo"] == "ContaCorrente":
        conta = ContaCorrente(
            numero=dados["numero"],
            titular=dados["titular"],
            saldo=dados["saldo"],
            limite=dados["limite"]
        )
    elif dados["tipo"] == "ContaPoupanca":
        conta = ContaPoupanca(
            numero=dados["numero"],
            titular=dados["titular"],
            saldo=dados["saldo"],
            rendimento=dados["rendimento"]
        )
    else:
        raise BancoError(f"Tipo desconhecido: {dados['tipo']}")
    conta._extrato = dados["extrato"]
    return conta

ARQUIVO = "contas.json"
_contador = 1000

def proximo_numero() -> int:
    global _contador
    _contador += 1
    return _contador

def salvar_contas(contas: list) -> None:
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump([conta.para_dict() for conta in contas], arquivo, indent=4, ensure_ascii=False)

def carregar_contas() -> list:
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return [de_dict(d) for d in dados]

def criar_conta(contas: list) -> None:
    escolha = input("Deseja cria 1-conta corrente ou 2-Poupanca")
    if escolha == "1":
        nome = input("Qual o nome do titular da conta: ")
        saldo = float(input("Qual o saldo da conta: "))
        limite = float(input("Qual o limite da conta: "))
        novaConta = ContaCorrente(proximo_numero(),nome,saldo,limite)
        contas.append(novaConta)
        salvar_contas(contas)

    elif escolha == "2":
        nome = input("Qual o nome do titular da conta: ")
        saldo = float(input("Qual o saldo da conta: "))
        rendimento = float(input("Qual o rendimento da conta: "))

        novaConta = ContaPoupanca(proximo_numero(), nome, saldo, float(rendimento))
        contas.append(novaConta)
        salvar_contas(contas)

def depositar(contas: list) -> None:
    numero = int(input("Número da conta: "))
    quantia = float(input("Valor a depositar: "))
    
    conta = buscar_conta(contas, numero) 
    conta.depositar(quantia)              
    salvar_contas(contas) 

def sacar(contas: list) -> None:
    numero = int(input("Número da conta: "))
    quantia = float(input("Valor a depositar: "))
    
    conta = buscar_conta(contas, numero) 
    conta.sacar(quantia)              
    salvar_contas(contas)

def transferir(contas: list) -> None:
    numero_origem = int(input("Conta de origem: "))
    numero_destino = int(input("Conta de destino: "))
    valor = float(input("Valor a transferir: "))

    origem = buscar_conta(contas, numero_origem)
    destino = buscar_conta(contas, numero_destino)
    origem.sacar(valor)       
    destino.depositar(valor) 
    salvar_contas(contas)
    print("Transferência realizada!")

def ver_extrato(contas: list) -> None:
    numero = int(input("Qual o numero da conta"))
    conta = buscar_conta(contas, numero)
    conta.mostrarExtrato()
def aplicar_rendimentos(contas: list) -> None:
    for conta in contas:
        if isinstance(conta, ContaPoupanca):
            conta.aplicarRendimento()
    salvar_contas(contas)

def listar_contas(contas: list) -> None:
    if not contas:
        print("Nenhuma conta cadastrada")
        return
    for conta in contas:
        print(conta)

def buscar_conta(contas: list, numero: int) -> ContaBancaria:
    # levanta ContaNaoEncontradaError se não achar
    for conta in contas:
        if conta.numero == numero:
            return conta
    raise contaNaoEncontrada(numero)
        
def menu():
    contas = carregar_contas()
    while True:
        print("\n=== Banco Python ===")
        print("1. Criar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Transferir")
        print("5. Ver extrato")
        print("6. Aplicar rendimentos")
        print("7. Listar contas")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "1":
                criar_conta(contas)
            elif opcao == "2":
                depositar(contas)
            elif opcao == "3":
                sacar(contas)
            elif opcao == "4":
                transferir(contas)
            elif opcao == "5":
                ver_extrato(contas)
            elif opcao == "6":
                aplicar_rendimentos(contas)
            elif opcao == "7":
                listar_contas(contas)
            elif opcao == "0":
                print("Até logo!")
                break
            else:
                print("Opção inválida.")
        except BancoError as e:
            print(f"\nErro: {e}")

menu()