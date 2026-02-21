# Exemplo de código executável que ilustra a aplicação de conceitos estatísticos:

import pandas as pd

# Exemplo de dados: salários dos 25 esportistas mais bem pagos de 2023
data = {
    'Nome': ['Esportista1', 'Esportista2', 'Esportista3', 'Esportista4', 'Esportista5'],
    'Salário': [100, 150, 200, 250, 300]
}

df = pd.DataFrame(data)

# Cálculo da média
media = df['Salário'].mean()
print(f'Média: {media}')

# Cálculo da mediana
mediana = df['Salário'].median()
print(f'Mediana: {mediana}')

# Cálculo da moda
moda = df['Salário'].mode()[0]
print(f'Moda: {moda}')

# Cálculo do desvio padrão
desvio_padrao = df['Salário'].std()
print(f'Desvio Padrão: {desvio_padrao}')