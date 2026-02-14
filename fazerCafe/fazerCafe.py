# Preparação

iniciar = True
cafe_sem_acucar = True

lista_ingredientes = ["café", "açucar", "água"]
lista_utensilhos = ["colher", "garrafa de café", "coador", "panela", "fogão"]


# iniciar

esquentar_agua = []


esquentar_agua.append(lista_ingredientes[2])
lista_ingredientes.remove("água")
esquentar_agua.append(lista_utensilhos[3])
lista_utensilhos.remove("panela")
esquentar_agua.append(lista_utensilhos[3])
lista_utensilhos.remove("fogão")


print("lista_ingredientes", lista_ingredientes)
print(20*"-")
print("lista_utensilhos", lista_utensilhos)
print(20*"-")
print("esquentar_agua", esquentar_agua)

#Esquentar garrafa de café
limpar_garrada = []

#jogar metade da água quente na garrafa com coador
limpar_garrada.append(esquentar_agua[0])
esquentar_agua.remove("água")
limpar_garrada.append(lista_utensilhos[2])
lista_utensilhos.remove("coador")
limpar_garrada.append(lista_utensilhos[1])
lista_utensilhos.remove("garrafa de café")

print(20*"-")
print(20*"-")
print(20*"-")
print("Esquentar garrafa de café")
print(20*"-")
print(20*"-")
print("lista_ingredientes", lista_ingredientes)
print(20*"-")
print("lista_utensilhos", lista_utensilhos)
print(20*"-")
print("esquentar_agua", esquentar_agua)
print(20*"-")
print("limpar_garrada", limpar_garrada)