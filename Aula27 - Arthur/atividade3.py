def verificar_idade(idade):
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")


idade = int(input("Digite sua idade: "))
verificar_idade(idade)