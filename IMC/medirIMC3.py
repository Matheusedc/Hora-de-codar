peso = 130
altura = 1.80

def IMC(peso, altura):
    
    IMC = (peso) / (altura**2)
    
    return IMC

def classificacao(resultado):
    
    IMC = resultado
    
    if IMC < 18.5:
    
        return "Baixo peso"
    
    elif IMC >= 18.5 and IMC <=24.9:
        
        return "Peso normal"

    elif IMC >=25 and IMC <= 29.9:
        
        return "Sobrepeso"

    elif IMC >= 30 and IMC <= 34.9:
        
        return "Obesidade grau I"
        
    elif IMC >= 35 and IMC <= 39.9:
        
        return "Obesidade grau II"
        
    else:
        
        return "Obesidade grau III"
    
 
resultado = float(IMC(peso, altura))

print(f"resultado: {resultado:.2f}")

resultado2 = classificacao(resultado)

print(resultado2)