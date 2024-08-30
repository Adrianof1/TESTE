def verificar_letra_a(string):
    # Converte a string para minúsculas e conta quantas vezes 'a' aparece
    contador = string.lower().count('a')
    
    # Verifica se a letra 'a' aparece na string e exibe o resultado
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes no texto informado.")
    else:
        print("A letra 'a' não aparece na string.")

# Solicita ao usuário que informe uma string
texto = input("Informe uma Palavra: ")

# Verifica a quantidade de vezes que a letra 'a' aparece na string
verificar_letra_a(texto)
