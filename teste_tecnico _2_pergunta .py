teste_tecnico_2pergunta .py
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

# Perguntar para o usuário qual número ele quer verificar
num = int(input("Informe um número: "))

if fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
