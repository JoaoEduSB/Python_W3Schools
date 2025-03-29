import webbrowser

# Variáveis

print("Variáveis em Python")

print() # Pular linha

print("Variáveis são definidas quando atribuímos um valor a elas")

print("Exemplo:")

x = 5
y = "Olá, mundo!"

print("x = 5 (x recebe 5)")
print('y = Olá, mundo! (y recebe a string "Olá, mundo!")')

print() # Pular linha

print("Exibir variável x =",x)
print("Exibir variável y =",y)

print() # Pular linha

print("Além disso, não precisamos necessariamente declarar o tipo da variável porque elas podem ser modificadas apenas definindo-as, exemplo:")

print() # Pular linha

print('x = 4 (x recebeu "4" que é um valor inteiro)')
print('x = Sally (Logo após, x recebeu "Sally" que é um valor em string)')
x = 4       # Variável do tipo inteiro recebe o valor inteiro "4"
x = "Sally" # No entanto logo após, definimos o valor de x como "Sally"

print()

print("Exibir variável x =",x , "(Exibiu o valor em string sem precisar ser declarado o tipo da variável)")

print()

print("Maaas, também podemos definir os tipos das variáveis, exemplos:")

x = str(3)    # x será "3"
y = int(3)    # y será "3"
z = float(3)  # z será "3.0"

print("x = str(3) (aqui foi declarado uma variável do tipo string)")
print("y = int(3) (aqui foi declarado uma variável do tipo inteiro)")
print("z = float(3) (aqui foi declarado uma variável do tipo real)")

print()

print("Exibir variável x =", x, ("str")) # Exibirá "3"
print("Exibir variável y =", y, ("int")) # Exibirá "3"
print("Exibir variável z =", z, ("float")) # Exibirá "3.0"

print()

print("Também podemos exibir o tipo da variável, exemplo:")

print ('x = 5 (automaticamente será identificado o número 5 como variável do tipo inteiro)')

print('y = João (automaticamente será identificado o valor "João" como variável do tipo string)')

x = 5
y = "João"

print()

print("Exibir tipo da variável x", type(x)) # Exibirá que o tipo da variável é inteira (int)

print("Exibir tipo da variável y", type(y)) # Exibirá que o tipo da variável é string (str)

print()

print("As variáveis também podem ser declaradas com aspas duplas ou simples,exemplo:")

print('x = "João')
print("ou")
print("y = 'João'")
x = "João"
x = 'João'

print("Exibir variável x =", x)
print("Exibir variável y =", y)

print()

print ("Python não é Case-Sensitive ou seja, podemos declarar uma variável com letra minúscula e também outra com a mesma letra porém maiúscula, exemplo:")

print('a = João')
print('A = Eduardo')
print("Embora estejamos utilizando a mesma letra, elas diferenciam a variável pelo case-sensitive, uma está minúscula, e a outra maiúscula")

a = "João"
A = "Eduardo"
print("Exibir a variável a =" ,a)
print("Exibir a variável A =" ,A)

print()

# Declaração variáveis - Sintaxe

print("Declaração de variáveis")

print("Existem algumas regras para declarar uma variável em python, vamos ver elas abaixo:")

print("Uma variável deve sempre começar com uma letra ou com o underscore _")

print("Só pode contar números ou letras e underscore (A-z, 0-9 e _)")

print("Python é case-sensitive ou seja, a palavra idade, Idade e IDADE são 3 possibilidades diferentes para nome devariáveis ")

print("Não pode começar com um número")
print("Não pode utilizar palavras reservadas") # https://www.w3schools.com/python/python_ref_keywords.asp

print() # Pular linha

print("Exemplos de palavras aceitáveis para uma variável:")

myvar = "João"
my_var = "Eduardo"
_my_var = "Souza"
myVar = "Barbosa"
MYVAR = "Variáveis"
myvar2 = "Funcionais"

print("myvar = João")
print("my_var = Eduardo")
print("_my_var = Souza")
print("myVar = Barbosa")
print("MYVAR = Variáveis")
print("myvar2 = Funcionais")

print() # Pular linha

print("Exibir variável myvar =", myvar)
print("Exibir variável my_var =", my_var)
print("Exibir variável _my_var =", _my_var)
print("Exibir variável myVar =", myVar)
print("Exibir variável MYVAR =", MYVAR)
print("Exibir variável myvar2 =", myvar2)

# Variáveis que não funcionarão

"""
2myvar = "John"
my-var = "John"
my var = "John"
Exibirá um erro ao executar o código
"""

print() # Pular linha

# Técnicas de representar uma variável

print("Técnicas para representar uma variável:")

print("Camel Case")
print("nomeDaMinhaVariavel") # Consiste em escrever todas as palavras da variável com a primeira letra maiúscula exceto a primeira 

print() # Pular linha

print("Pascal Case") 
print("NomeDaMinhaVariavel") # Consiste em escrever todas as palavras da# Consiste em escrever a primeira letra de todas as palavras maiúscula, até mesmo a primeira

print() # Pular linha

print("Snake Case")
print("nome_da_minha_variavel") # Consiste em escrever todas as palavras separadas pelo underscore

print() # Pular linha

# Vários valores para várias variáveis
print("Podemos declarar vários valores e várias variáveis em uma única linha, exemplo:")

x, y, z = "Laranja", "Banana", "Cereja"

print('x, y, z = "Laranja", "Banana", "Cereja"')

print()

print("Exibir variável x =", x)
print("Exibir variável y =", y)
print("Exibir variável z =", z)

print()