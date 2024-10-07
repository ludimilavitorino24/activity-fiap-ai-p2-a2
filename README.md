# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Watchcows

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

*Descreva seu projeto com base no texto do PBL (até 600 palavras)*

//TODO: write the description above

Para mais informações, acesse o [documento do projeto](./document/ai_project_document_fiap.md).

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*


#### Requisitos e Dependências

Para usar este projeto de forma eficaz, você precisa:

- **Python 3.x**: Verifique se o Python 3 está instalado em seu sistema.
- **Docker**: Verifique se o Docker está instalado em seu sistema.

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
    source .venv/bin/activate  # No Windows, use `.venv\Scripts\activate`
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

6. **Execute o servidor Postgres usando um contêiner Docker**
    ```sh
    docker compose up -d
    ```
6. **Popule o banco de dados inicial**:
    ```sh
    python3 src/populate_db.py
    ```

#### Uso

Execute o seguinte comando:

```sh
python src/main.py
```


## 🗃 Histórico de lançamentos

* 0.1.0 - XX/XX/2024
    *

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
