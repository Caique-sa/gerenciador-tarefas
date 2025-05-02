import json
import os

ARQUIVO = 'tarefas.json'

def carregar_tarefas():
    """

    Lê o arquivo tarefas.json e carrega as tarefas salvas.
    Caso o arquivo não exista retorna lista vazia.

    """

    if os.path.exists(ARQUIVO): # Se o arquivo existe:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f) # Lê o arquivo e transforma em lista.
    return []


def salvar_tarefas(tarefas):
    """
    Salva a lista de tarefas no JSON
    
    """

    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, indent=2, ensure_ascii=False)


def adicionar_tarefa(titulo):
    """
    Adiciona tarefa com titulo

    """

    tarefas = carregar_tarefas()
    nova = {"titulo": titulo, 'concluida': False}
    tarefas.append(nova)
    salvar_tarefas(tarefas)


def listar_tarefas():
    """
    Exibe as tarefas com todos os status.
    
    """

    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i}. {tarefa['titulo']} [{status}]")


def concluir_tarefa(indice):
    """
    Marca tarefa como concluida
    
    """           

    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
    else:
        print("Índice inválido")


def remover_tarefa(indice):
    """
    Remove tarefa do indice

    """
    
    tarefas = carregar_tarefas()

    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
    else:
        print("Indice invalido")