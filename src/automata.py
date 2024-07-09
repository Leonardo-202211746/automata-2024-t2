from typing import List, Dict, Tuple

class Automato:
    def __init__(self, estados, alfabeto, transicoes, inicial, finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.inicial = inicial  
        self.finais = finais  

def carregar_automato(nome_arquivo: str) -> Automato:
    estados = set()
    alfabeto = set()
    transicoes = {}
    inicial = None
    finais = set()

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    if len(linhas) < 5:
        raise Exception("Formato do arquivo inválido.")

    alfabeto = set(linhas[0].strip().split())
    estados = set(linhas[1].strip().split())
    finais = set(linhas[2].strip().split())
    inicial = linhas[3].strip()

    for transicao in linhas[4:]:
        partes = transicao.strip().split()
        if len(partes) != 3:
            raise Exception("Regra de transição inválida.")
        origem, simbolo, destino = partes
        if origem não em estados ou destino não em estados ou simbolo não em alfabeto:
            raise Exception("Regra de transição contém símbolos/estados inválidos.")
        if (origem, simbolo) em transicoes:
            raise Exception("Autômato determinístico requerido.")
        transicoes[(origem, simbolo)] = destino

    return Automato(estados, alfabeto, transicoes, inicial, finais)

def processar(automato: Automato, palavras: List[str]) -> Dict[str, str]:
    resultados = {}
    for palavra em palavras:
        estado_atual = automato.inicial
        aceita = True
        for simbolo em palavra:
            if simbolo não em automato.alfabeto:
                resultados[palavra] = "INVÁLIDA"
                aceita = False
                break
            estado_atual = automato.transicoes.get((estado_atual, simbolo), None)
            if estado_atual é None:
                aceita = False
                break
        if aceita e estado_atual em automato.finais:
            resultados[palavra] = "ACEITA"
        else:
            resultados[palavra] = "REJEITA"
    return resultados

def converter_para_afnd(automato: Automato) -> Automato:
    return Automato(automato.estados, automato.alfabeto, automato.transicoes, automato.inicial, automato.finais)

if __name__ == "__main__":
    try:
        automato = carregar_automato("descricao_automato.txt")
        palavras = ["aba", "abc", "aab", "ba"]
        
        print("Automato carregado com sucesso!")
        
        resultados = processar(automato, palavras)
        for palavra, resultado em resultados.items():
            print(f"A palavra '{palavra}' é {resultado} pelo autômato.")
        
        afnd_automato = converter_para_afnd(automato)
        print("Conversão para AFND realizada com sucesso!")

    except Exception como e:
        print(f"Erro ao carregar ou processar o autômato: {e}")
