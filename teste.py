peso = 100
altura = 1.86

IMC = (peso) / (altura**2)

print(IMC)

if IMC < 18.5:
    
    print("Baixo peso")

if 30 <= IMC <= 39.9:
    
    if IMC >= 35:
        
        print("Obesidade grau II")
    
    else:
        
        print("Obesidade grau I")
    

if 18.5 <= IMC <= 29.9:
    
    if IMC >= 25:
        
        print("Sobrepeso")   
    
    else:
        
        print("Peso normal") 

if IMC >= 40:
    
     print("Obesidade grau III") 