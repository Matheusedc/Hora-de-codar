'''
       1. Verificando Se um Número é Positivo, Negativo ou Zero
    Crie um programa que solicita um número ao usuário e verifica se ele é positivo, negativo
    ou zero.
'''

n = 10

if n > 0:
    
    print("Número positivo")

elif n < 0:
    
    print("Número negativo")

else:
    
    print("Número é zero ")
    
    
print( 40 * "-")
'''
    2. Calculadora Simples
Crie um programa que pede ao usuário dois números e uma operação (+,-, *, /) e realiza
o cálculo correspondente.

'''

n1 = 10
n2 = 20
n3 = "+"

if n3 == '+' :
    
    resultado = n1 + n2
    print(resultado)
elif n3 == '-':

    resultado = n1 - n2
    print(resultado)
    
elif n3 == '*':

    resultado = n1 * n2
    print(resultado)

else:

    resultado = n1 / n2
    print(resultado)

print( 40 * "-")

'''
    3.ClassificaçãodeIdade
Crieumprogramaqueclassificaaidadedeumapessoaem:
● Criança:0a12anos
● Adolescente:13a17anos
● Adulto:18a59anos
● Idoso:60anosoumais

'''

idade = 10

if idade <= 12 and idade >= 0:
    
    print('Criança')

elif idade <= 17 and idade >= 13:
    
    print('Adolecente')
    
elif idade <= 59 and idade >= 18:
    
    print('Adulto')
    
else:
    
    print('Idoso')
    
'''
    4. Verificando Ano Bissexto
Crie um programa que verifica se um ano é bissexto.
● Umanoébissexto se for divisível por 4.
● Masnãoébissexto se for divisível por 100, exceto se for divisível por 400.
'''