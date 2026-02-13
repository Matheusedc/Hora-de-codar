# Preparação

iniciar = True
cafe_sem_acucar = True

lista_ingredientes = ["café", "açucar", "água"]
lista_utensilhos = ["colher", "garrafa de café", "coador", "panela", "fogão"]


# iniciar

lista_ingredientes.remove("água")
lista_utensilhos.remove("panela")
lista_utensilhos.remove("fogão")

esquentar_agua = []


esquentar_agua.append(lista_ingredientes[2])
esquentar_agua.append(lista_utensilhos[3])
esquentar_agua.append(lista_utensilhos[4])

print("lista_ingredientes", lista_ingredientes)
print(20*"-")
print("lista_utensilhos", lista_utensilhos)
print(20*"-")
print("esquentar_agua", esquentar_agua)
