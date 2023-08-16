from time import process_time
import sys 
sys.setrecursionlimit(10**6) 
# Função para realizar a filtragem recursiva dos dados
def filtrar_dados(dados, coluna, valor):
    return [linha for linha in dados if linha[coluna] == valor]

# Função para realizar o mapeamento dos dados
def mapear_dados(dados, coluna, funcao):
    return [[funcao(linha[coluna]) if i == coluna else linha[i] for i in range(len(linha))] for linha in dados]

def reduzir_dados(dados, coluna, funcao):
    resultado = dados[0][coluna]
    for linha in dados[1:]:
        resultado = funcao(resultado, linha[coluna])
    return resultado

# Função para ordenar os dados
def ordenar_dados(dados, coluna):
    return sorted(dados, key=lambda x: x[coluna])

# Função auxiliar recursiva para ler as linhas do arquivo
def ler_linhas_arquivo(arquivo):
    return [linha.strip().split(",") for linha in arquivo if linha.strip()]

# Função para carregar os dados de um arquivo CSV
def carregar_dados_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        dados = ler_linhas_arquivo(arquivo)
    return dados

# Exemplo de uso do código
t1_start = process_time()
dados = carregar_dados_arquivo("dados.csv") # UTILIZE QUALQUER CSV que se adeque com o problema.
t1_stop = process_time()

# Filtrar os dados com base na coluna "idade"
t2_start = process_time()
dados_filtrados = filtrar_dados(dados, coluna=1, valor="30")
t2_stop = process_time()
print("Dados Filtrados:")
print(dados_filtrados)

# Mapear os dados na coluna "salario" com uma função de aumento
t3_start = process_time()
dados_mapeados = mapear_dados(dados_filtrados, coluna=2, funcao=lambda x: float(x) * 1.1)
t3_stop = process_time()
print("Dados Mapeados:")
print(dados_mapeados)

# Reduzir os dados para obter a média dos salários
t4_start = process_time()
media_salarios = reduzir_dados(dados_mapeados, coluna=2, funcao=lambda x, y: x + y) / len(dados_mapeados)
t4_stop = process_time()
print("Média dos Salários:")
print(media_salarios)

# Ordenar os dados pela coluna "nome"
t5_start = process_time()
dados_ordenados = ordenar_dados(dados_mapeados, coluna=0)
t5_stop = process_time()

print("Tempo de leitura do arquivo: ", t1_stop - t1_start)
print("Tempo de filtragem dos dados: ", t2_stop - t2_start)
print("Tempo de mapeamento dos dados: ", t3_stop - t3_start)
print("Tempo de redução dos dados: ", t4_stop - t4_start)
print("Tempo de ordenação dos dados: ", t5_stop - t5_start)
