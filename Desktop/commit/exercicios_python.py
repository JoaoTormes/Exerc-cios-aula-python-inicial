# =============================================================================
# EXERCÍCIOS DE PYTHON - VETORES, MATRIZES, BUSCA E ORDENAÇÃO
# Resolvidos de forma simples, usando apenas listas, tuplas e funções básicas
# =============================================================================


# =============================================================================
# 1 - INDICES DE X NO VETOR
# Percorre o vetor e guarda os índices onde encontra o valor X
# =============================================================================
def indices_de_x(vetor, x):
    indices = []
    for i in range(len(vetor)):
        if vetor[i] == x:
            indices.append(i)
    return indices

# Teste
v = [3, 1, 4, 1, 5, 9, 1, 6]
print("Índices de 1:", indices_de_x(v, 1))   # [1, 3, 6]
print("Índices de 9:", indices_de_x(v, 9))   # [5]
print()


# =============================================================================
# 2 - MÉDIA DOS ELEMENTOS
# Soma todos e divide pela quantidade
# =============================================================================
def media(vetor):
    soma = 0
    for x in vetor:
        soma += x
    return soma / len(vetor)

# Teste
v = [4, 8, 15, 16, 23, 42]
print("Média:", media(v))  # 18.0
print()


# =============================================================================
# 3 - MEDIANA DOS ELEMENTOS
# Ordena e pega o elemento do meio. Se par, tira a média dos dois do meio.
# =============================================================================
def mediana(vetor):
    ordenado = sorted(vetor)   # cria uma cópia ordenada
    n = len(ordenado)
    meio = n // 2
    if n % 2 == 1:             # quantidade ímpar
        return ordenado[meio]
    else:                      # quantidade par
        return (ordenado[meio - 1] + ordenado[meio]) / 2

# Teste
print("Mediana de [3,1,4,1,5]:", mediana([3, 1, 4, 1, 5]))   # 3
print("Mediana de [3,1,4,2]:", mediana([3, 1, 4, 2]))         # 2.5
print()


# =============================================================================
# 4 - MODA DO VETOR
# Conta quantas vezes cada elemento aparece e retorna os mais frequentes
# =============================================================================
def moda(vetor):
    # Conta frequência de cada elemento
    contagem = {}
    for x in vetor:
        if x in contagem:
            contagem[x] += 1
        else:
            contagem[x] = 1

    # Acha a maior frequência
    maior = 0
    for freq in contagem.values():
        if freq > maior:
            maior = freq

    # Coleta todos com a maior frequência
    modas = []
    for valor, freq in contagem.items():
        if freq == maior:
            modas.append(valor)

    return modas

# Teste
print("Moda de [1,2,2,3,3,3]:", moda([1, 2, 2, 3, 3, 3]))   # [3]
print("Moda de [1,1,2,2,3]:", moda([1, 1, 2, 2, 3]))         # [1, 2]
print()


# =============================================================================
# 5 - MDC (MÁXIMO DIVISOR COMUM) - Algoritmo de Euclides
# Enquanto b != 0, substitui a por b e b pelo resto da divisão a/b
# =============================================================================
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Teste
print("MDC(12, 8):", mdc(12, 8))    # 4
print("MDC(100, 75):", mdc(100, 75))  # 25
print()


# =============================================================================
# 6 - MMC (MÍNIMO MÚLTIPLO COMUM)
# mmc(a,b) = (a * b) / mdc(a,b)
# =============================================================================
def mmc(a, b):
    return (a * b) // mdc(a, b)

# Teste
print("MMC(4, 6):", mmc(4, 6))    # 12
print("MMC(3, 5):", mmc(3, 5))    # 15
print()


# =============================================================================
# 7 - MDC DE UMA LISTA
# Aplica o MDC par a par ao longo da lista
# =============================================================================
def mdc_lista(lista):
    resultado = lista[0]
    for i in range(1, len(lista)):
        resultado = mdc(resultado, lista[i])
    return resultado

# Teste
print("MDC([12, 8, 4]):", mdc_lista([12, 8, 4]))    # 4
print("MDC([100, 75, 50]):", mdc_lista([100, 75, 50]))  # 25
print()


# =============================================================================
# 8 - MMC DE UMA LISTA
# Aplica o MMC par a par ao longo da lista
# =============================================================================
def mmc_lista(lista):
    resultado = lista[0]
    for i in range(1, len(lista)):
        resultado = mmc(resultado, lista[i])
    return resultado

# Teste
print("MMC([4, 6, 10]):", mmc_lista([4, 6, 10]))   # 60
print("MMC([3, 5, 7]):", mmc_lista([3, 5, 7]))     # 105
print()


# =============================================================================
# 9 - FATORES PRIMOS
# Tenta dividir n por números a partir de 2. Se divide, é fator primo.
# =============================================================================
def fatores_primos(n):
    fatores = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            fatores.append(divisor)
            n = n // divisor       # divide e continua com o quociente
        else:
            divisor += 1
    return fatores

# Teste
print("Fatores de 12:", fatores_primos(12))   # [2, 2, 3]
print("Fatores de 60:", fatores_primos(60))   # [2, 2, 3, 5]
print("Fatores de 13:", fatores_primos(13))   # [13]
print()


# =============================================================================
# 10 - COMBINAÇÕES C(m, n) = m! / (n! * (m-n)!)
# Calcula o fatorial e aplica a fórmula
# =============================================================================
def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def combinacoes(m, n):
    return fatorial(m) // (fatorial(n) * fatorial(m - n))

# Teste
print("C(5,2):", combinacoes(5, 2))   # 10
print("C(6,3):", combinacoes(6, 3))   # 20
print()


# =============================================================================
# 11 - LISTA SEM REPETIÇÕES
# Percorre e adiciona só se o elemento ainda não foi visto
# =============================================================================
def sem_repeticoes(lista):
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado

# Teste
print("Sem repetições:", sem_repeticoes([1, 2, 2, 3, 1, 4]))   # [1, 2, 3, 4]
print()


# =============================================================================
# 12 - MODA DE UMA LISTA (retorna lista com o(s) mais frequente(s))
# Reutiliza a função moda() definida acima
# =============================================================================
def moda_lista(lista):
    return moda(lista)

# Teste
print("Moda:", moda_lista([1, 2, 2, 3, 3, 3]))   # [3]
print()


# =============================================================================
# 13 - UNIÃO DE DOIS CONJUNTOS
# Junta os dois e remove repetições
# =============================================================================
def uniao(a, b):
    resultado = list(a)   # copia o primeiro
    for x in b:
        if x not in resultado:
            resultado.append(x)
    return resultado

# Teste
print("União:", uniao([1, 2, 3], [3, 4, 5]))   # [1, 2, 3, 4, 5]
print()


# =============================================================================
# 14 - INTERSEÇÃO DE DOIS CONJUNTOS
# Pega só o que está nos dois
# =============================================================================
def intersecao(a, b):
    resultado = []
    for x in a:
        if x in b and x not in resultado:
            resultado.append(x)
    return resultado

# Teste
print("Interseção:", intersecao([1, 2, 3], [2, 3, 4]))   # [2, 3]
print()


# =============================================================================
# 15 - DIFERENÇA ENTRE CONJUNTOS (A - B)
# Pega o que está em A mas NÃO está em B
# =============================================================================
def diferenca(a, b):
    resultado = []
    for x in a:
        if x not in b:
            resultado.append(x)
    return resultado

# Teste
print("Diferença A-B:", diferenca([1, 2, 3, 4], [2, 4]))   # [1, 3]
print()


# =============================================================================
# 16 - VERIFICAR SE A É SUBCONJUNTO DE B
# Todo elemento de A deve estar em B
# =============================================================================
def eh_subconjunto(a, b):
    for x in a:
        if x not in b:
            return False
    return True

# Teste
print("É subconjunto?", eh_subconjunto([1, 2], [1, 2, 3]))   # True
print("É subconjunto?", eh_subconjunto([1, 4], [1, 2, 3]))   # False
print()


# =============================================================================
# 17 - LER MATRIZ DO USUÁRIO
# Lê linha a linha até receber uma linha em branco
# =============================================================================
def ler_matriz():
    matriz = []
    print("Digite os números de cada linha separados por espaço.")
    print("Pressione Enter em branco para terminar.")
    while True:
        linha_str = input("> ")
        if linha_str.strip() == "":
            break
        numeros = linha_str.strip().split()
        linha = []
        for n in numeros:
            linha.append(int(n))
        matriz.append(linha)
    return matriz


# =============================================================================
# 18 - VERIFICAR SE LISTA 2D É UMA MATRIZ (todas as linhas com mesmo tamanho)
# Retorna (linhas, colunas) ou () se inválida
# =============================================================================
def verificar_matriz(m):
    if len(m) == 0:
        return ()
    colunas = len(m[0])
    for linha in m:
        if len(linha) != colunas:
            return ()
    return (len(m), colunas)

# Teste
print("É matriz?", verificar_matriz([[1,2],[3,4]]))        # (2, 2)
print("É matriz?", verificar_matriz([[1,2],[3,4,5]]))      # ()
print()


# =============================================================================
# 19 - IMPRIMIR MATRIZ LINHA A LINHA
# =============================================================================
def imprimir_matriz(m):
    for linha in m:
        print(linha)

# Teste
imprimir_matriz([[1, 2, 3], [4, 5, 6]])
print()


# =============================================================================
# 20 - TRANSPOSTA DE UMA MATRIZ
# Linhas viram colunas e vice-versa: Mt[j][i] = M[i][j]
# =============================================================================
def transposta(m):
    linhas = len(m)
    colunas = len(m[0])
    mt = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(m[i][j])
        mt.append(nova_linha)
    return mt

# Teste
m = [[1, 2, 3], [4, 5, 6]]
print("Transposta:")
imprimir_matriz(transposta(m))   # [[1,4],[2,5],[3,6]]
print()


# =============================================================================
# 21 - SOMA DE MATRIZES (A + B)
# Matrizes devem ter as mesmas dimensões
# =============================================================================
def soma_matrizes(a, b):
    dim_a = verificar_matriz(a)
    dim_b = verificar_matriz(b)
    if dim_a == () or dim_b == () or dim_a != dim_b:
        return []
    linhas, colunas = dim_a
    c = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(a[i][j] + b[i][j])
        c.append(linha)
    return c

# Teste
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print("Soma:")
imprimir_matriz(soma_matrizes(a, b))   # [[6,8],[10,12]]
print()


# =============================================================================
# 22 - PRODUTO DE MATRIZES (A x B)
# Colunas de A devem ser iguais às linhas de B
# C[i][j] = soma de A[i][k] * B[k][j]
# =============================================================================
def produto_matrizes(a, b):
    linhas_a = len(a)
    colunas_a = len(a[0])
    linhas_b = len(b)
    colunas_b = len(b[0])
    if colunas_a != linhas_b:
        return []
    c = []
    for i in range(linhas_a):
        linha = []
        for j in range(colunas_b):
            soma = 0
            for k in range(colunas_a):
                soma += a[i][k] * b[k][j]
            linha.append(soma)
        c.append(linha)
    return c

# Teste
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print("Produto:")
imprimir_matriz(produto_matrizes(a, b))   # [[19,22],[43,50]]
print()


# =============================================================================
# 23 - MATRIZ DIAGONAL
# Todos os elementos fora da diagonal principal são zero
# =============================================================================
def eh_diagonal(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if i != j and m[i][j] != 0:
                return False
    return True

# Teste
print("Diagonal?", eh_diagonal([[1,0],[0,2]]))    # True
print("Diagonal?", eh_diagonal([[1,1],[0,2]]))    # False
print()


# =============================================================================
# 24 - MATRIZ TRIANGULAR INFERIOR
# Todos os elementos ACIMA da diagonal principal são zero
# =============================================================================
def eh_triangular_inferior(m):
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):   # j > i  → acima da diagonal
            if m[i][j] != 0:
                return False
    return True

# Teste
print("Tri. Inferior?", eh_triangular_inferior([[1,0,0],[2,3,0],[4,5,6]]))   # True
print()


# =============================================================================
# 25 - MATRIZ TRIANGULAR SUPERIOR
# Todos os elementos ABAIXO da diagonal principal são zero
# =============================================================================
def eh_triangular_superior(m):
    n = len(m)
    for i in range(n):
        for j in range(i):          # j < i  → abaixo da diagonal
            if m[i][j] != 0:
                return False
    return True

# Teste
print("Tri. Superior?", eh_triangular_superior([[1,2,3],[0,4,5],[0,0,6]]))   # True
print()


# =============================================================================
# 26 - QUADRADO MÁGICO
# Mesma soma em linhas, colunas e diagonais + contém todos os números de 1 a n²
# =============================================================================
def eh_quadrado_magico(m):
    n = len(m)
    # Verifica se contém todos os números de 1 a n²
    todos = []
    for linha in m:
        for x in linha:
            todos.append(x)
    for k in range(1, n * n + 1):
        if k not in todos:
            return False

    # Soma alvo = soma da primeira linha
    alvo = sum(m[0])

    # Verifica todas as linhas
    for linha in m:
        if sum(linha) != alvo:
            return False

    # Verifica todas as colunas
    for j in range(n):
        soma = 0
        for i in range(n):
            soma += m[i][j]
        if soma != alvo:
            return False

    # Diagonal principal
    soma = 0
    for i in range(n):
        soma += m[i][i]
    if soma != alvo:
        return False

    # Diagonal secundária
    soma = 0
    for i in range(n):
        soma += m[i][n - 1 - i]
    if soma != alvo:
        return False

    return True

# Teste
magico = [[2,7,6],[9,5,1],[4,3,8]]
print("Quadrado mágico?", eh_quadrado_magico(magico))   # True
print()


# =============================================================================
# 27 - MATRIZ DE PERMUTAÇÕES
# Matriz de 0s e 1s onde cada linha e coluna tem exatamente um 1
# =============================================================================
def eh_permutacao(m):
    n = len(m)
    for linha in m:
        if len(linha) != n:
            return False
    for i in range(n):
        if sum(m[i]) != 1:         # cada linha tem exatamente um 1
            return False
    for j in range(n):
        soma = 0
        for i in range(n):
            soma += m[i][j]
        if soma != 1:              # cada coluna tem exatamente um 1
            return False
    return True

# Teste
perm = [[1,0,0],[0,0,1],[0,1,0]]
print("Permutação?", eh_permutacao(perm))   # True
print()


# =============================================================================
# 28 - BUBBLESORT COM PARADA ANTECIPADA
# Se em uma passagem não houve troca, a lista já está ordenada → para.
# Melhor caso: O(n) comparações (lista já ordenada)
# Pior caso:   O(n²) comparações (lista invertida)
# =============================================================================
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:    # nenhuma troca → já está ordenado
            break
    return lista

# Teste
print("Bubble Sort:", bubble_sort([5, 3, 1, 4, 2]))   # [1,2,3,4,5]
print()


# =============================================================================
# 29 - K-ÉSIMO MENOR ELEMENTO
# Ordena a lista e retorna o elemento na posição k-1
# Custo: O(n²) no pior caso (devido ao sort por bubble)
# =============================================================================
def k_esimo(lista, k):
    copia = list(lista)
    bubble_sort(copia)
    return copia[k - 1]

# Teste
print("3º menor de [5,1,4,2,3]:", k_esimo([5, 1, 4, 2, 3], 3))   # 3
print()


# =============================================================================
# 30 - BUSCA SEQUENCIAL (retorna todos os índices)
# =============================================================================
def busca_sequencial(lista, chave):
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == chave:
            posicoes.append(i)
    return posicoes

# =============================================================================
# BUSCA BINÁRIA (retorna todos os índices, lista deve estar ordenada)
# Acha uma ocorrência e depois expande para os vizinhos
# =============================================================================
def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    posicoes = []

    # Acha qualquer ocorrência
    encontrado = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            encontrado = meio
            break
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    if encontrado == -1:
        return []

    # Expande para a esquerda
    i = encontrado
    while i >= 0 and lista[i] == chave:
        posicoes.append(i)
        i -= 1

    # Expande para a direita
    i = encontrado + 1
    while i < len(lista) and lista[i] == chave:
        posicoes.append(i)
        i += 1

    posicoes.sort()
    return posicoes

# Teste
print("Sequencial [1,1,2,3,1], chave=1:", busca_sequencial([1,1,2,3,1], 1))   # [0,1,4]
print("Binária [1,1,2,3,3], chave=3:", busca_binaria([1,1,2,3,3], 3))         # [3,4]
print()


# =============================================================================
# 31 - BUSCA BINÁRIA QUE RETORNA POSIÇÃO DE INSERÇÃO
# Retorna k tal que: lista[k] == chave  OU  chave ficaria entre pos k-1 e k
# =============================================================================
def busca_insercao(lista, chave):
    inicio = 0
    fim = len(lista)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio
    return inicio

# Teste
print("Inserção de 3 em [1,2,4,5]:", busca_insercao([1,2,4,5], 3))   # 2
print("Inserção de 0 em [1,2,4,5]:", busca_insercao([1,2,4,5], 0))   # 0
print("Inserção de 9 em [1,2,4,5]:", busca_insercao([1,2,4,5], 9))   # 4
print()


# =============================================================================
# 32 - CONTAR CHAVES ENTRE X e Y (inclusive) EM LISTA ORDENADA
# Usa a função de inserção para achar as bordas e subtrai
# =============================================================================
def contar_entre(lista, x, y):
    pos_x = busca_insercao(lista, x)        # primeira posição >= x
    pos_y = busca_insercao(lista, y + 1)    # primeira posição > y
    return pos_y - pos_x

# Teste
lst = [1, 3, 5, 7, 9, 11, 13]
print("Chaves entre 5 e 11:", contar_entre(lst, 5, 11))   # 4  (5,7,9,11)
print("Chaves entre 2 e 6:", contar_entre(lst, 2, 6))     # 1  (5)
