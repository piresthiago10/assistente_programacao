# Assistente de Programacao

Exercício final: Code Assistant

A missão é construir um assistente de programação para ser executado na linha de comando.

Ao iniciar, o assistente deve solicitar (ou receber como parâmetro) o caminho da pasta do projeto. Ele deve ler e escrever somente dentro dessa pasta.

O assistente deve ter acesso às seguintes ferramentas:

- list_files() — lista os arquivos de código do projeto.
  Atenção: essa ferramenta deve ignorar arquivos e pastas que não fazem parte do código do projeto, como .env, .venv, .git, .gitignore, *.bak e *.log.
- read_code(files: list) — obtém o conteúdo de um ou mais arquivos.
- write_file(filepath: str, content: str) — escreve o conteúdo de um arquivo.

## Instalação das Dependências

Para instalar as dependências do projeto, você precisará ter o Python e o gerenciador de pacotes `pip` instalados. É recomendado criar e ativar um ambiente virtual para isolar as dependências do projeto. Siga os passos abaixo:

1. **Criar um ambiente virtual**:
   
   Para criar um ambiente virtual, execute o seguinte comando no terminal:
   
   ```
   python -m venv env
   ```
   
   Isso criará uma pasta chamada `env` com o ambiente virtual.

2. **Ativar o ambiente virtual**:
   
   - No Windows:
   ```
   .\env\Scripts\activate
   ```
   - No macOS e Linux:
   ```
   source env/bin/activate
   ```

3. **Instalar as dependências**:
   
   Após ativar o ambiente virtual, você pode instalar as dependências do projeto executando:
   
   ```
   pip install -r requirements.txt
   ```

## Execução do Projeto

Após instalar as dependências, você pode executar o assistente de programação usando o seguinte comando:

```
python cli.py [diretório/do/seu/código]
python cli.py /home/seu-usuario/desenvolvimento/calcularora
```

## Configuração do Ambiente

Para que o assistente funcione corretamente, é necessário adicionar um arquivo chamado `.env` na raiz do projeto com a seguinte chave:

```
export OPENAI_API_KEY=your_api_key_here
```

Capriche nas instruções que você vai passar ao agente. Habilite histórico. Teste o agente usando a cópia de alguma pasta de um projeto real que você tenha aí.