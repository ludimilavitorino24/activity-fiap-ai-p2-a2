## Microsserviços

### **data_simulation**

Este microsserviço simula dados para os rebanhos. Ele gera dados aleatórios e realistas, como temperatura, frequência cardíaca e movimento, que posteriormente são processados pelo sistema para detectar alertas e gerar relatórios.

Arquivos principais:
- `animal_names.py`: Gera nomes aleatórios de animais para simular indivíduos diferentes no rebanho.
- `main.py`: Script principal para simular dados do rebanho e popular o banco de dados.

### **alert_processing**

Este microsserviço é responsável por processar os dados coletados para identificar qualquer alerta que indique anomalias na saúde do rebanho. Ele utiliza algoritmos de detecção de valores discrepantes para gerar alertas com base em dados incomuns de temperatura, frequência cardíaca e movimento.

### **process_alerts.py**

Este script é responsável pela detecção de alertas com base em dados anômalos de temperatura, frequência cardíaca e movimento. Ele utiliza o cálculo de z-score para identificar outliers em cada um dos parâmetros monitorados. Os limites para cada métrica são configurados através do arquivo `config.py`, que define os thresholds (limiares) para identificar um valor como discrepante.

O projeto está dividido em três principais microsserviços:
- **data_simulation**: Responsável por criar dados simulados realistas.
- **alert_processing**: Processa os dados para gerar alertas sobre a saúde dos animais (atualmente gera alertas com base em valores discrepantes nos dados).
- **report_generation**: Gera relatórios diários sobre a saúde dos rebanhos. Os dados são categorizados por espécie e raça.

## Arquivos principais:

- `fetch_data.py`: Busca os dados relevantes no banco de dados.
- `process_alerts.py`: Processa os dados buscados e identifica valores discrepantes. Gera alertas para temperatura, frequência cardíaca e movimento com base em valores de limite.
- `save_alert.py`: Salva os alertas gerados no banco de dados para posterior análise.

#### Funcionalidades principais:

- **`process_outliers`**: Esta função realiza a análise de outliers, utilizando o cálculo do z-score para identificar valores anômalos acima ou abaixo do threshold definido para cada métrica (temperatura, frequência cardíaca e movimento). Ela retorna um dicionário contendo as informações necessárias para registrar o alerta, como o tipo de alerta (se o valor é acima ou abaixo do threshold) e a métrica analisada.

- **`getAlertDict`**: Converte o DataFrame contendo os dados discrepantes em uma lista de dicionários, com cada dicionário representando um alerta a ser salvo no banco de dados. Garante que as colunas `alert_type` e `alert_metric` estejam presentes no DataFrame antes de processá-lo.

- **`process_alerts`**: Esta função é o ponto de entrada do processamento de alertas. Ela recebe um parâmetro `day` (dia a ser analisado), faz a consulta no banco de dados utilizando a função `fetch_datalogs`, e então processa os alertas para temperatura, frequência cardíaca e movimento, salvando-os no banco de dados com a função `save_alert`.

#### Detalhes do processamento:

- **Temperatura**: Analisada com base no threshold `temp_outlier_z_threshold` configurado no arquivo `config.py`. Se forem detectados valores fora do intervalo esperado (baseado no z-score), alertas são gerados.
- **Frequência Cardíaca**: Processada de forma similar à temperatura, utilizando o threshold `heartrate_outlier_z_threshold`.
- **Movimento (Distância Percorrida)**: A função também analisa o campo `animal_distance_traveled` utilizando o threshold `movement_outlier_z_threshold` para detectar anomalias nos dados de movimentação dos animais.

Essa estrutura modular permite fácil escalabilidade para a inclusão de novas métricas ou a modificação das regras de alerta. A função `process_alerts` imprime quantos alertas foram disparados para cada métrica após o processamento.

Voltar ao [README](/README.md)