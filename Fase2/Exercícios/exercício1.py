class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def adicionar_estoque(self, quantidade: int) -> None:
        # adiciona quantidade ao estoque
        # não aceita quantidade <= 0
        if quantidade <= 0 :
            print("Adicion uma quantidade maior que 0")
            return
        self.estoque += quantidade

    def remover_estoque(self, quantidade: int) -> None:
        # remove quantidade do estoque
        # não aceita quantidade <= 0
        # não aceita remover mais do que tem em estoque
        if quantidade <= 0 :
            print("Adicione um valor maior que zero para remover do estoque atual")
        elif quantidade > self.estoque:
            print("Você está tentando remover uma quantidade maior do que há no estoque") 
        else:
             self.estoque -= quantidade  

    def aplicar_desconto(self, percentual: float) -> None:
        # reduz o preço pelo percentual informado
        # percentual deve ser entre 0 e 100
        if percentual < 0 or percentual > 100:
            print("Percentual deve estar entre 0 e 100")
            return
        self.preco *= 1 - percentual/100

    def __str__(self) -> str:
        # retorna: "Notebook | R$ 2500.00 | Estoque: 10"
        return f"{self.nome} | {self.preco:.2f} | Estoque: {self.estoque}"

prod1 = Produto("Arroz", 15.5, 10)
prod2 = Produto("Feijão", 20, 20)

#chamando metodos do primeiro produto
prod1.adicionar_estoque(15)
prod1.adicionar_estoque(-1)
prod1.remover_estoque(0)
prod1.remover_estoque(20)
prod1.remover_estoque(2)
prod1.aplicar_desconto(50)
prod1.aplicar_desconto(150)
print(prod1)

#chamando metodos do segundo produto
prod2.adicionar_estoque(10)
prod2.adicionar_estoque(-1)
prod2.remover_estoque(0)
prod2.remover_estoque(20)
prod2.remover_estoque(2)
prod2.aplicar_desconto(50)
prod2.aplicar_desconto(150)
print(prod2)