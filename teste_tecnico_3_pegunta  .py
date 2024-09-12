teste_tecnico_3_pegunta  .py
[15:50, 9/12/2024] Moniele: import json

# Exemplo de dados de faturamento mensal em JSON
faturamento_mensal = {
    "dias": [1000, 2000, 0, 1500, 0, 3000, 0, 2500, 0, 1700, 0, 900]
}

# Pegando os valores sem considerar dias sem faturamento (0)
valores = [valor for valor in faturamento_mensal['dias'] if valor > 0]

# Calculando o menor, maior e a média
menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_faturamento = sum(valores) / len(valores)

# Contando os dias com faturamento acima da média
dias_acima_da_media = len([valor for valor in valores if valor > media_faturamento])

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
