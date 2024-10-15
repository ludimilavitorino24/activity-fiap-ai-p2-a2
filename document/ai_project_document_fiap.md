
<img src="../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=30% height=30%>

# AI Project Document - Módulo 1 - FIAP

## Grupo 45

#### Nomes dos integrantes do grupo

- <a href="https://www.linkedin.com/in/brunoconterato">Bruno Conterato</a> 
- <a href="https://www.linkedin.com/in/luisfuturist">Luis Emidio</a>
- <a href="https://www.linkedin.com/in/willianpmarques">Willian Pinheiro Marques</a> 
- <a href="https://www.linkedin.com/in/robertobesser">Roberto Besser</a>
- <a href="https://www.linkedin.com/in/ludimila-vi">Ludimila Vitorino</a>

## Sumário

[1. Introdução](#c1)

[2. Visão Geral do Projeto](#c2)

[3. Desenvolvimento do Projeto](#c3)

[4. Resultados e Avaliações](#c4)

[5. Conclusões e Trabalhos Futuros](#c5)

[6. Referências](#c6)

<br>

# <a name="c1"></a>1. Introdução

## 1.1. Escopo do Projeto

### 1.1.1. Contexto da Inteligência Artificial

A indústria de Inteligência Artificial (IA) está em constante evolução, oferecendo soluções que transformam diversos setores, desde o agronegócio até a saúde. No contexto da pecuária, a IA tem se mostrado uma ferramenta valiosa para melhorar a gestão e monitoramento da saúde animal. Soluções baseadas em IA, como a desenvolvida pela Watch Cows, aplicam algoritmos avançados para analisar dados coletados em tempo real, identificando anomalias e gerando alertas que permitem uma intervenção rápida e eficaz. Essas soluções possuem uma abrangência internacional, com aplicação em fazendas ao redor do mundo, onde o monitoramento eletrônico do gado está se tornando cada vez mais comum.

### 1.1.2. Descrição da Solução Desenvolvida

A Watch Cows desenvolveu uma solução de IA que monitora a saúde de rebanhos pecuários através de coleiras equipadas com sensores que capturam dados como temperatura, frequência cardíaca e movimento. Esses dados são analisados por algoritmos de detecção de anomalias, gerando alertas em tempo real e relatórios periódicos. A solução permite que os pecuaristas tenham uma visão precisa e detalhada da saúde do rebanho, possibilitando intervenções rápidas e reduzindo riscos associados a doenças. A criação de valor está na capacidade de gerar insights baseados em dados, proporcionando uma gestão mais eficiente e proativa.

# <a name="c2"></a>2. Visão Geral do Projeto

## 2.1. Objetivos do Projeto

O objetivo do projeto é utilizar Inteligência Artificial para monitorar a saúde de rebanhos em tempo real, identificando anomalias e gerando alertas que permitam intervenções rápidas. Além disso, o projeto busca proporcionar uma plataforma que entregue relatórios detalhados sobre a saúde dos animais, categorizados por espécie e raça, oferecendo uma solução completa de monitoramento para os pecuaristas.

## 2.2. Público-Alvo

O público-alvo do projeto são pecuaristas e fazendeiros que buscam melhorar a gestão da saúde de seus rebanhos. A solução também pode ser aplicada em cooperativas de pecuária, organizações de controle sanitário e grandes fazendas que necessitam de ferramentas avançadas para o monitoramento de saúde animal, visando reduzir perdas e aumentar a produtividade.

## 2.3. Metodologia

A metodologia utilizada no desenvolvimento do projeto foi baseada em microsserviços, cada um responsável por uma funcionalidade específica: simulação de dados, processamento de alertas e geração de relatórios. O ciclo de desenvolvimento envolveu as seguintes etapas:

1. **Definição de Requisitos**: Identificação das métricas de saúde animal que seriam monitoradas (temperatura, frequência cardíaca e movimento).
2. **Desenvolvimento Modular**: Implementação dos microsserviços de simulação de dados, processamento de alertas e geração de relatórios.
3. **Testes e Validação**: Execução de scripts de simulação para testar a geração de dados e a resposta do sistema a anomalias.
4. **Implantação**: Implementação em uma arquitetura de microsserviços, permitindo escalabilidade e fácil manutenção do sistema.

# <a name="c3"></a>3. Desenvolvimento do Projeto

## 3.1. Tecnologias Utilizadas

As tecnologias utilizadas no desenvolvimento do projeto "Watchcows" foram:

- **jinja2:**  Biblioteca Python para renderização de templates, utilizada para a geração de relatórios.
- **numpy:** Biblioteca Python para computação científica, utilizada para o processamento de dados.
- **oracledb:** Conector Python para o banco de dados Oracle, utilizado para interação com o banco de dados.
- **pandas:** Biblioteca Python para análise de dados, utilizada para manipulação e análise de dados.
- **perlin-noise:** Biblioteca Python para geração de ruído de Perlin, utilizada para a simulação de dados.
- **psycopg2-binary:** Conector Python para o banco de dados PostgreSQL, utilizado para interação com o banco de dados.
- **python-dotenv:** Biblioteca Python para gerenciamento de variáveis de ambiente, utilizada para configurações do projeto.
- **SQLAlchemy:** Framework Python para mapeamento objeto-relacional (ORM), utilizado para interação com o banco de dados.
- **Python 3.x:** Linguagem de programação utilizada para desenvolver o projeto.
  - **datetime:** Módulo para manipulação de datas e horas.
  - **json:** Módulo para serialização e desserialização de dados em JSON.
  - **math:** Módulo para operações matemáticas.
  - **os:** Módulo para interação com o sistema operacional.
  - **pathlib:** Módulo para manipulação de arquivos e diretórios.
  - **random:** Módulo para geração de números aleatórios.
  - **sys:** Módulo para interação com o interpretador Python.
  - **typing:** Módulo para tipagem estática de código.

## 3.2. Modelagem e Algoritmos

No projeto Watch Cows, a modelagem e os algoritmos de IA utilizados são centrados na detecção de anomalias nos dados de saúde dos animais. Para isso, foram implementados algoritmos baseados na detecção de outliers, utilizando o cálculo de z-score. Essa abordagem foi escolhida devido à sua eficácia em identificar valores discrepantes em conjuntos de dados, que é fundamental para alertar os pecuaristas sobre possíveis problemas de saúde nos rebanhos. [Clique aqui para explicações detalhadas sobre o algorítmo z-score para detecção de outliers.](./other/the_z_score_outlier_detection_algorithm.md)

O algoritmo avalia medições de temperatura, frequência cardíaca e movimento, comparando cada valor observado com a média e o desvio padrão dos dados históricos. Se um valor cai fora de um intervalo de confiança pré-definido (configurado no arquivo de configuração `config.py`), um alerta é gerado. Essa estratégia é eficiente, pois não requer um treinamento extenso de modelos de machine learning, mas sim uma análise estatística direta dos dados.

A implementação do algoritmo ocorre principalmente no microsserviço **alert_processing**, onde funções como `process_outliers` são responsáveis por calcular o z-score e identificar os alertas. Essa abordagem permite que o sistema seja flexível e facilmente adaptável, possibilitando ajustes nos thresholds e a inclusão de novas métricas conforme necessário, sem a complexidade associada ao treinamento de algoritmos de aprendizado de máquina.

## 3.3. Treinamento e Teste

O processo de validação dos algoritmos no projeto foi realizado de maneira iterativa, utilizando dados simulados gerados pelo módulo **data_simulation**. Esses dados incluíam parâmetros como temperatura, frequência cardíaca e movimento, que foram coletados em simulações representativas do comportamento normal e anômalo dos rebanhos.

### Conjuntos de Dados Utilizados

Os conjuntos de dados foram gerados artificialmente para simular diversas situações, incluindo tanto dados normais quanto anômalos. Essa abordagem garantiu uma diversidade de cenários para testar a eficácia dos alertas gerados. Os dados foram organizados em um banco de dados e utilizados para avaliar as funcionalidades dos algoritmos.


# <a name="c4"></a>4. Resultados e Avaliações

## 4.1. Análise dos Resultados

Os testes demonstraram que o sistema foi capaz de identificar a maioria das anomalias corretamente. Os alertas gerados permitem que os pecuaristas recebam informações relevantes e oportunas sobre a saúde de seus rebanhos, possibilitando intervenções rápidas e informadas. Esses resultados indicam que a abordagem estatística implementada é eficaz para o monitoramento da saúde animal, atendendo às necessidades do setor pecuário.

## 4.2. Feedback dos Usuários

Ainda não estamos em produção nem com um MVP rodando para podermos recolher feedbacks de usuários finais. Assim que o projeto atingir essas etapas, poderemos realizar a avaliação baseada no retorno dos usuários.

# <a name="c5"></a>5. Conclusões e Trabalhos Futuros

O projeto "Watch Cows" demonstra o potencial da tecnologia para auxiliar na gestão e no monitoramento da saúde de animais em fazendas. O sistema desenvolvido se mostrou eficaz em identificar outliers nos dados de temperatura, frequência cardíaca e movimentação, gerando relatórios diários que podem auxiliar os fazendeiros na tomada de decisão e no manejo dos animais. 

## 5.1. Pontos Fortes

- O projeto oferece um script simples e direto, facilitando o acesso e a compreensão das informações pelos usuários finais.
- Os algoritmos de detecção de outliers se mostraram eficazes na identificação de anomalias nos dados.
- A geração de relatórios detalhados fornece uma visão abrangente da saúde dos animais, incluindo informações sobre temperatura, frequência cardíaca, movimentação e alertas.

## 5.2. Pontos a Melhorar

- Implementar a integração com sensores reais para a coleta de dados de animais em tempo real.
- Desenvolver funcionalidades adicionais para a análise de dados, como a previsão de doenças e a otimização de recursos.
- Ampliar o conjunto de dados de treinamento para incluir diferentes raças de bovinos e diferentes condições climáticas.

# <a name="c6"></a>6. Referências

- https://en.wikipedia.org/wiki/Perlin_noise
