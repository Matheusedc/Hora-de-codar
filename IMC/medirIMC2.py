peso = 100
altura = 1.86

IMC = (peso) / (altura**2)

if IMC < 18.5:
    
    print("Baixo peso")
    
if IMC >= 18.5 and IMC <=24.9:
    
     print("Peso normal")

if IMC >=25 and IMC <= 29.9:
    
    print("Sobrepeso")

if IMC >= 30 and IMC <= 34.9:
    
    print("Obesidade grau I")
    
if IMC >= 35 and IMC <= 39.9:
    
    print("Obesidade grau II")
    
if IMC >= 40:
     
    print("Obesidade grau III")