# condicionais -> estruturas if, else

idade = 17

# estrutura do if _> if comparação
# Só é executado quando é verdadeiro

if idade >= 18:
    print( "vc é maior de idade")
    
else:
    
    print(" Vc é menor de idade")
    
# meia entrada -> 18 + ou estudando em escola

estudante_rede_publica = False

if idade < 18 or estudante_rede_publica:
    print("tem direito a meia entrada")
 
    
# nota : A, B, C

nota = 6
# elif -> condição intermediaria entre if e else

if nota > 9:
    print(" Seu conceito é A")

elif nota > 8:
    print(" Seu conceito é B")

elif nota > 6:
    print(" Seu conceito é C")

else:
    print(" Precisa melhorar sua nota")
    
# clim,

clima = "chuvoso"

if clima == "ensolarado":
    print("O dia está ensolarado")

elif clima == "nublado":
    print("O dia está nublado")

elif clima == "chuvoso":
    print("O dia está chuvoso")
    
# venda

venda = 1200

if venda > 1000:
    comissao = venda * .005
    print(" Sua comissão da venda foi: ", comissao)

elif venda > 500:
    comissao = venda * .01
    print(" Sua comissão da venda foi: ", comissao)
    
else:
    comissao = venda * .02
    print(" Sua comissão da venda foi: ", comissao)