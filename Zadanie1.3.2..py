print("Lista zakupów:")
print()
lista_zakupow = {"piekarnia": ["chleb", "bułki", "pączek"], "warzywniak": ["marchew", "seler", "rukola"]}
piekarnia = lista_zakupow.get("piekarnia")
warzywniak = lista_zakupow.get("warzywniak")
for i in range(len(piekarnia)):
    piekarnia[i] = piekarnia[i].title()
for i in range(len(warzywniak)):
    warzywniak[i] = warzywniak[i].title() 