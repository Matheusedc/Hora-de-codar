# operadores aritiméticos

a = 5 
b = 2

print(a + b) # adição
print(a / b) # divisão
print(a * b) # multiplicação


# ** - exponenciação
# // - divisão inteira

print( a // b)
print( a / b)
print( a % b) # resto da divisão

# operadores de comparação
x = 10
y = 5

print(x > 5)
print(x < 5)
print(x != 5)

print(x >= 5)
print(x <= 5)

# operadores lógicos
# and, or e not
# Unir comparações

idade = 20
possui_carteira = True

pode_dirigir = (idade >= 18) and possui_carteira

print(pode_dirigir)

# And só verdadeiro quando ambas as operações são verdadeiras
# OR é verdadeiro quando pelos menos uma operação é True

eh_estudante = False
idade = 60

# um = é atribuição
# dois == é comparação

meia_entrada = eh_estudante == True or idade >= 60

print(meia_entrada)

# NOT = inverter um booleano

chovendo = True
nao_chovendo = not chovendo

print("Chovendo, chovendo", chovendo)
print(" Não chovendo", nao_chovendo)

# if -> chovendo == false, not chovendo

nota = 8
frequencia = 60

passou_de_ano = (nota > 7) and (frequencia > 80)

print("passou de ano:", passou_de_ano)

# senhas iguais
#criando registro do usuario

senha = "123"
confirmacao_senha = "1234"

senha_errada = senha != confirmacao_senha

print( "Senha errada?", senha_errada)
 