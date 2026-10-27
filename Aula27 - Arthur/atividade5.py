def ler_nota():
    nota = float(input("Digite uma nota (0 a 10): "))
    while nota < 0 or nota > 10:
        print("Nota inválida! A nota deve estar entre 0 e 10.")
        nota = float(input("Digite uma nota (0 a 10): "))
    return nota


def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"


nota1 = ler_nota()
nota2 = ler_nota()
nota3 = ler_nota()

media = calcular_media(nota1, nota2, nota3)
situacao = verificar_situacao(media)

print(f"\nMédia: {media:.2f}")
print(f"Situação: {situacao}")