# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

> [!NOTE]
> Esse projeto é parte do curso de **Inteligência Artificial** da [FIAP](https://github.com/fiap) - Online 2024. Este repositório é a atividade "**Fase 2** Atividade Cap. 6 - Python e além."

# Watch Cows

## Grupo 45

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/brunoconterato">Bruno Conterato</a> 
- <a href="https://www.linkedin.com/in/luisfuturist">Luis Emidio</a>
- <a href="https://www.linkedin.com/in/willianpmarques">Willian Pinheiro Marques</a> 
- <a href="https://www.linkedin.com/in/robertobesser">Roberto Besser</a>
- <a href="https://www.linkedin.com/in/ludimila-vi">Ludimila Vitorino</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>

## 📜 Descrição

**Watch Cows** é uma empresa que ajuda pecuaristas a monitorarem eletronicamente a saúde de seus rebanhos. Através da detecção de parâmetros (temperatura, frequência cardíaca e movimento) coletados por coleiras, o sistema realiza análises, gera alertas em tempo real e produz relatórios sobre a saúde do rebanho.

Para mais informações, acesse o [documento do projeto](./document/other/project_structure.md).

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

```
Projeto Watch Cows
.
├── assets
│   └── logo-fiap.png                # Logotipo da FIAP usado na documentação ou interface
├── config
│   ├── config.json                  # Arquivo de configuração principal da aplicação
│   └── template.jinja2.md           # Template para geração de relatórios
├── document
│   └── ai_project_document_fiap.md  # Documento principal do projeto AI para FIAP
├── README.md                        # Documentação principal do projeto
├── requirements.txt                 # Lista de dependências Python do projeto
├── scripts                          # Diretório contendo scripts utilitários e de automação
│   ├── clear_database.py            # Script para limpar o banco de dados
│   ├── db_session.sql               # Script SQL para gerenciar sessões de banco de dados
│   ├── demo.py                      # Script de demonstração do pipeline completo da aplicação
│   ├── generate_data.py             # Script principal para gerar dados simulados
│   └── generate_report.py           # Script principal para gerar relatórios de saúde
└── src                              # Código-fonte da aplicação
    ├── alert_processing             # Microsserviço responsável pelo processamento de alertas
    │   ├── fetch_data.py            # Função para buscar dados no banco de dados
    │   ├── process_alerts.py        # Processa os dados para identificar valores discrepantes e gerar alertas
    │   └── save_alert.py            # Salva os alertas gerados no banco de dados
    ├── config.py                    # Manipulador de configuração da aplicação
    ├── data_simulation              # Microsserviço responsável pela simulação de dados
    │   ├── animal_names.py          # Função para gerar nomes aleatórios de animais
    │   └── main.py                  # Script principal para simular dados do rebanho
    ├── db.py                        # Modelos e configurações de banco de dados
    ├── db_utils.py                  # Funções utilitárias para interações com o banco de dados
    ├── main.py                      # Ponto de entrada principal da aplicação
    ├── report_generation            # Microsserviço para geração de relatórios de saúde
    │   ├── analyze_data.py          # Função para analisar dados e gerar relatórios
    │   └── save_report.py           # Salva os relatórios gerados no sistema
    ├── typings.py                   # Definições de tipos usados no código
    └── utils.py                     # Funções utilitárias diversas
```

## 🔧 Como executar o código

#### Requisitos e Dependências

Para usar este projeto de forma eficaz, você precisa:

- [Git](https://git-scm.com/downloads)
- [Vscode](https://code.visualstudio.com/download)
- [Python 3.x](https://www.python.org/)

#### Instalação

Para instalar e executar a aplicação, siga estas etapas:

1. **Clone o repositório**:
    ```sh
    git clone https://github.com/ludimilavitorino24/activity-fiap-ai-p2-a2.git
    ```
2. **Navegue até o diretório do projeto**:
    ```sh
    cd activity-fiap-ai-p2-a2
    ```
3. **(Opcional) Crie e ative um ambiente virtual**:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # No Windows, use `.venv.\Scripts\activate`
    ```
4. **Instale as dependências**:
    ```sh
    pip install -r requirements.txt
    ```
5. **Defina as variáveis de ambiente**:
    ```sh
    cp .env.example .env
    ```
    Edite o arquivo `.env` e defina as variáveis de ambiente conforme necessário.

6. **Rode o script de demonstração**:
    ```sh
    python3 scripts/demo.py
    ```

#### Uso

Para limpar o banco de dados, execute:

```sh
python3 scripts/clear_database.py
```

Para gerar os dados simulados para hoje, execute:

```sh
python3 scripts/generate_data.py
```

Para gerar o relatório diário de saúde do animal, execute:

```sh
python3 scripts/generate_report.py
```

## 🗃 Histórico de lançamentos

* 0.1.0 - 15/10/2024

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

```
______________________________
< Have you been watching me? >
------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
