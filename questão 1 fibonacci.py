def fibonacci(n):
    # Inicia a sequência de Fibonacci com os dois primeiros números
    a, b = 0, 1
    
    # Gera os próximos números da sequência até que 'a' seja maior ou igual a 'n'
    while a < n:
        a, b = b, a + b
    
    # Verifica se o número informado pertence à sequência
    return a == n

# Solicita ao usuário que informe um número
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")



