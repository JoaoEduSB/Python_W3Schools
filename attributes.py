# Atributos do Python
# Python é uma linguagem que se baseia na indentação para rodar o código, diferentemente de outras linguagens que utilizam o ponto e vírgual (por exemplo) para encerrar uma instrução.

import sys

print(sys.version) # verificar a versão do Python

print("Python é uma linguagem de programação que facilita a leitura e interpretação do usuário e programador")

#         SINTAXE

print("Ela não funciona sem a indentação")
print("Não importa a quantidade de espaços que inserimos na indentação, é obrigatório ao menos 1 espaço.")
print("O mais comum é utilizar 4 espaços na indentação.")

print("Exemplos:")

# Mais comum 4 espaços

if 5 > 2:
    print("5 é maior que 2")

# Menos comum 1 espaço apenas    

if 5 > 2:
 print("5 é maior que 2")
 
# Menos comum vários espaços

if 5 > 2:
            print("5 é maior que 2")
            
# Todos irão funcionar corretamente
              
# TAGS

print("Tags em python")

print("A # é utilizada para definir comentário em uma linha, além disso, o python não possui syntax que permite inserir comentários multi linhas exemplo:")
# Comentário

print("Embora as aspas duplas podem ser utilizadas 3 em conjunto para definir um comentário multi linhas, visto que o python não lerá essas aspas já que elas não definem uma variável, exemplo:")

"""
Teste de comentário multilinhas
Esse texto não irá aparecer no código
Linha 47
"""

