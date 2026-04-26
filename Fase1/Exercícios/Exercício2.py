numeros = [64, 34, 25, 12, 22, 11, 90]

tamanho: int = len(numeros)

for i in range(tamanho):
    for j in range(0,tamanho-1-i):
        if numeros[j] > numeros[j+1]:
            numeros[j],numeros[j+1] = numeros[j+1], numeros[j]

for n in numeros:
    print(n)

#Filtro de Notas
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 5.0},
    {"nome": "Beatriz", "nota": 9.2},
    {"nome": "Diego", "nota": 4.5},
    {"nome": "Elena", "nota": 7.0},
]

#alunos reprovados
alunosAprovados: int = 0
somaNota: float = 0
cont: int = 0
maiorNota: float = 0
menorNota: float = 15
alunosReprovados = []
for aluno in alunos:
    if aluno["nota"] >= 7:
        alunosAprovados+=1
    else:
        alunosReprovados.append(aluno["nome"])
    
    somaNota += aluno["nota"]
    cont+=1
    if aluno["nota"] > maiorNota:
        maiorNota = aluno["nota"]
    
    if aluno["nota"] < menorNota:
        menorNota = aluno["nota"]

media: float = somaNota/cont
print(f"A média da turma é {media}")
print(f"A quantidade de alunos que foram Aprovados é {alunosAprovados}")
print(f"A Maior nota é {maiorNota}")
print(f"A Menor nota é {menorNota}")

print("Alunos reprovados:")
for aluno in alunosReprovados:
    print(aluno)


