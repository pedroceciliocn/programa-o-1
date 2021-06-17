kwh = float(input("De o consumo em kWh: "))
tipo = input("De o tipo de instalação: ")

if tipo == "residencial":
    if kwh <= 500:
        preço = 0.40*kwh
    else:
        preço = 0.65*kwh
elif tipo == "comercial":
    if kwh <= 1000:
        preço = 0.55*kwh
    else:
        preço = 0.60*kwh
elif tipo == "industrial":
    if kwh <= 5000:
        preço = 0.55*kwh
    else:
        preço = 0.60*kwh
else:
    print("Categoria inválida, digite 'residencial', 'comercial' ou industrial'.")
    preço = 0
print(f"Sua instalação é do tipo {tipo}.\nSeu consumo foi de {kwh:.2f}kWh.\nA conta foi de R${preço:.2f}.")