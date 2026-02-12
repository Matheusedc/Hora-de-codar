peso = 160
altura = 1.80

def IMC(peso, altura):
    
    IMC = (peso) / (altura**2)
    
    return IMC

resultado = IMC(peso, altura)

print(resultado)

def classificacao(resultado):
    
    IMC = resultado
    
    if IMC < 18.5:
    
        return "Baixo peso"
    
    if IMC >= 18.5 and IMC <=24.9:
        
        return "Peso normal"

    if IMC >=25 and IMC <= 29.9:
        
        return "Sobrepeso"

    if IMC >= 30 and IMC <= 34.9:
        
        return "Obesidade grau I"
        
    if IMC >= 35 and IMC <= 39.9:
        
        return "Obesidade grau II"
        
    if IMC >= 40:
        
        return "Obesidade grau III"
    
    
resultado2 = classificacao(resultado)

print(resultado2)