# Variáveis

idade = 25
nome = "Matheus"
altura = 1.68

# Tipos de dados
# int, float, textos = strings, bool = True ou false

cidade = 'São Paulo'
esta_logado = True

# python não alerta com a mudança de tipo de dados silenciosa (alterar valor)

print(nome)

nome = 2

print(nome)

# ver o tipo de dados

print(type(nome)) # int
print(type(cidade)) # str
print(type(esta_logado)) #bool
print(type(altura)) # float

# operadores matemáticos

print(5 + 1.2)
print(5 * 2)
print(5 / 10)
print(5 - 50)

#contatenação -> união de textos

nomeUsuario = "joão"

frase = "Olá" + nomeUsuario + "Tudo bem?"

print(frase)

#comparações

maior = 15>2

print(maior)

menor = 5<12
menor2 = 5<2

print(menor)
print(menor2)

print( 5 ==5)
print( "teste" == "teste")

print(15 != 2)