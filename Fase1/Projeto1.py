import json
import os

ARQUIVO = "contatos.json"

def carregarContatos() -> list[dict]:
    if not os.path.exists(ARQUIVO):
        return []
    
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvarContatos (contatos: list[dict]) -> None:
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(contatos,arquivo,indent=4, ensure_ascii=False)

def adicionarContato(contatos: list[dict]) -> None:
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    for contato in contatos:
        if contato['email'] == email:
            print("Email ja cadastrado")
            return
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvarContatos(contatos)
    print("Contato Adicionado com Sucesso !!!")


def listarContatos(contatos: list[dict]) -> None:
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    print(f"\n{len(contatos)} contato(s) encontrados")
    for i, contato in enumerate(contatos):
        print(f"{i+1}. {contato['nome']}")
        print(f"   Telefone: {contato['telefone']}")
        print(f"   Email: {contato['email']}")
        print()

def buscarContato(contatos: list[dict]) -> None:
    desejado = input("Qual o email do contato desejado: ")
    for contato in contatos:
        if desejado == contato['email']:
             print("Informações do contato desejado: ")
             print(f"Nome: {contato['nome']}")
             print(f"Telefone: {contato['telefone']}")
             print(f"Email: {contato['email']}")

def removerContato(contatos: list[dict]) -> None:
    desejado = input("Qual o email do contato desejado: ")
    for contato in contatos:
        if desejado == contato['email']:
            confirmacao = input(f"Tem certeza que deseja remover {contato['nome']}? (s/n): ")
            if confirmacao.lower() == "s":
                contatos.remove(contato)
                salvarContatos(contatos)
                print("Contato removido com sucesso!")
            else:
                print("Operação cancelada.")
            return

    print("Contato não encontrado.")

def menu():
    contatos = carregarContatos()
    while True:
        print("\n=== Gerenciador de Contatos ===")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionarContato(contatos)
        elif opcao == "2":
            listarContatos(contatos)
        elif opcao == "3":
            buscarContato(contatos)
        elif opcao == "4":
            removerContato(contatos)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

menu() 