def existeArquivo(nomeArquivo):
    """
    Verifica que o arquivo já existe no projeto

    Args:
        nomeArquivo str: Nome do arquivo
    
    Returns:
        A conclusão se existe ou não
    
    Raises:
        Aviso de que o arquivo já existe
    """
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    """
    Esta função cria um arquivo inexistente

    Args:
        nomeArquivo str: Recebe o nome do arquivo
    
    Returns:
        Cria o arquivo novo

    Raises:
        Printa mensagem de erro ao criar arquivo.
    """
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criacao do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso! \n')

def ler_arquivo(nome_arquivo):
    """
    Esta função cria le o arquivo de palavras e cria uma lista com elas tratadas

    Args:
        nomeArquivo str: Recebe o nome do arquivo
    
    Returns:
        Cria uma lista com palavras tratadas

    Raises:
        Printa mensagem de erro ao ler o arquivo.
    """

    palavras = []
    try:
        with open(nome_arquivo, 'rt') as f:
            for linha in f:
                linha = linha.strip()
                palavra, dica = linha.split(';')
                palavras.append((palavra, dica))
    except:
        print('Erro ao ler o arquivo')
    return palavras

def jogar(palavra, dica):

    """
    Esta função é a lógica por trás do jogo da forca

    Args:
        palavra str: Recebe palavra escolhida aleatoriamente da lista palavras
        dica str: Recebe dica associada a palavra aleatoria de lista palavras
    
    Returns:
        Prints das letras tentadas, acertadas e resultado final.

    Raises:
        Print de letra já tentada
        Print de letra nao existente
    """

    letras_descobertas = ['_'for _ in palavra]
    letras_tentadas = []

    while '_' in letras_descobertas:
        print('\nDica: ', dica)
        print('Palavra: ', ' '.join(letras_descobertas))
        print('letras já tentadas:', ', '.join(letras_tentadas))

        letra = input('Digite uma letra: ').lower()
        
        if letra in letras_tentadas:
            print('Você já tentou essa letra!')
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_descobertas[i] = letra
        else:
            print('Letra nao encontrada!')
    print('\n Parabéns! Você acertou: ', palavra)

def iniciar_jogo(lista):
    """
    Esta função puxa a lista de palavras e escolhe uma palavra aleatoria e uma dica associada.
    Chama a funcao jogar levando as variaveis

    Args:
        lista str: Recebe a lista de palavras tratada do arquivo
    
    Returns:
        Inicia o jogo com a palavra e dica aleatoria

    Raises:
        
    """
    palavra, dica = random.choice(lista)
    jogar(palavra, dica)

# PROGRAMA PRINCIPAL
#imports
import random

#verificacao de arquivo
arquivo = 'palavras.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivado inexistente')
    criarArquivo(arquivo)

#declaracao de variaveis globais
lista = ler_arquivo(arquivo)

#logica principal
print('Bem vindo ao jogo da forca! \n Abaixo selecione para começar: ')
while True:
    print('\n1 - Jogar \n 0 - Encerrar')
    opcao = int(input('Digite a opção: '))
    
    if opcao == 1:
        iniciar_jogo(lista)
        continuar = input('Jogar novamente? (s/n): ').lower()
        if continuar != 's':
            break
    elif opcao == 0:
        break
    else:
        print('Opção inválida')
