### Algoritmo de Detecção de Outliers Usando Z-Score

O **Z-Score** é uma medida que indica quantos desvios padrão um valor está distante da média de uma lista de números. Esse método é útil para identificar *outliers*, ou seja, valores que estão significativamente distantes dos demais dados.

#### Passos para encontrar outliers utilizando Z-Score:

1. **Calcular a média** da lista de números.
2. **Calcular o desvio padrão** da lista.
3. Para cada número na lista:
   - **Calcular o Z-Score** do número usando a seguinte fórmula:

   ```
   Z = (X - média) / desvio padrão
   ```

   Onde:
   - `Z` é o Z-Score.
   - `X` é o valor do número.
   - `média` é a média da lista.
   - `desvio padrão` é o desvio padrão da lista.

4. **Definir um limiar de Z-Score**: Um valor de Z-Score maior que `3` ou menor que `-3` é normalmente considerado um outlier, pois indica que o valor está a mais de 3 desvios padrão da média.

5. **Marcar os outliers**: Qualquer valor com Z-Score fora do intervalo `[-3, 3]` será considerado um outlier.

#### Exemplo de código em Python:

```python
import numpy as np

def detect_outliers_zscore(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    
    outliers = []
    for num in data:
        z_score = (num - mean) / std_dev
        if np.abs(z_score) > 3:  # Considera-se um outlier se o Z-Score for maior que 3 ou menor que -3
            outliers.append(num)
    
    return outliers

# Exemplo de uso
data = [10, 12, 12, 13, 12, 11, 11, 12, 10, 13, 15, 14, 30]  # O valor 30 é um outlier
outliers = detect_outliers_zscore(data)
print("Outliers detectados:", outliers)
# Outliers detectados: [30]
```

#### Explicação:

- **Cálculo do Z-Score**: Para cada número da lista, subtrai-se a média e, em seguida, divide-se pelo desvio padrão, resultando no Z-Score.
- **Identificação dos Outliers**: Valores com Z-Scores fora do intervalo `[-3, 3]` são considerados outliers.

#### Considerações:

- **Limiar ajustável**: O valor `3` é uma convenção comum, mas pode ser ajustado conforme a distribuição dos dados ou a aplicação.
- **Distribuição normal dos dados**: O Z-Score é mais eficaz quando os dados seguem uma distribuição aproximadamente normal (gaussiana).
