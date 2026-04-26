# Retorna a média da lista
def calcular_media(notas: list[float]) -> float:
    return sum(notas)/len(notas)

# Retorna True se a nota for >= 7, False caso contrário
def esta_aprovado(nota: float, minimo: float = 7.0) -> bool:
    if nota>=minimo:
        return True
    else:
        return False

# Recebe a lista de alunos e retorna duas listas:
# a primeira com nomes dos aprovados, a segunda com nomes dos reprovados
def separar_turma(alunos: list[dict]) -> tuple[list, list]:
    aprovados = []
    reprovados = []
    for aluno in alunos:
        if aluno["nota"] >= 7:
            aprovados.append(aluno["nome"])
        else:
            reprovados.append(aluno["nome"])
    
    return aprovados,reprovados

# Retorna o aluno com maior nota (o dicionário inteiro)
def melhor_aluno(alunos: list[dict]) -> dict:
    melhor = alunos[0]
    for aluno in alunos:
        if aluno["nota"] > melhor["nota"]:
            melhor = aluno
    return melhor

# Use todas as funções aqui
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 5.0},
    {"nome": "Beatriz", "nota": 9.2},
    {"nome": "Diego", "nota": 4.5},
    {"nome": "Elena", "nota": 7.0},
]

media = calcular_media([aluno["nota"] for aluno in alunos])
aprovados, reprovados = separar_turma(alunos)
destaque = melhor_aluno(alunos)

print(f"Média da turma: {media:.1f}")
print(f"Aprovados: {', '.join(aprovados)}")
print(f"Reprovados: {', '.join(reprovados)}")
print(f"Melhor aluno: {destaque['nome']} com {destaque['nota']}")