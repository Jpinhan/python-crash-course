words = {"Algoritmo": "Sequência passo a passo de instruções. É a receita que"
" o computador segue para executar uma tarefa específica ou resolver um "
                      "problema.", "Variável": "Espaço de memória"
" reservado. Funciona como uma caixa com etiqueta onde o programa guarda dados "
"(como números ou textos) que podem mudar durante a execução.", "Função": "Bloco de código reutilizável. É um conjunto de instruções agrupadas sob um nome que realiza uma tarefa específica sempre que é chamado."
         , "Sintaxe": "Conjunto de regras gramaticais. Define a forma correta de escrever e combinar as palavras e símbolos em uma linguagem de programação específica."
         , "Bug": "Erro no código de um programa. Trata-se de uma falha ou comportamento inesperado que faz com que o software funcione incorretamente."}

for words, significados in words.items():
    print(f"{words}:\n{significados}\n")