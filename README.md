# Assistente de Programacao

Exercício final: Code Assistant

A missão é construir um assistente de programação para ser executado na linha de comando.

Ao iniciar, o assistente deve solicitar (ou receber como parâmetro) o caminho da pasta do projeto. Ele deve ler e escrever somente dentro dessa pasta.

O assistente deve ter acesso às seguintes ferramentas:

- list_files() — lista os arquivos de código do projeto.
Atenção: essa ferramenta deve ignorar arquivos e pastas que não fazem parte do código do projeto, como .env, .venv, .git, .gitignore, *.bak e *.log.
- read_code(files: list) — obtém o conteúdo de um ou mais arquivos.
- write_file(filepath: str, content: str) — escreve o conteúdo de um arquivo.

Capriche nas instruções que você vai passar ao agente. Habilite histórico. Teste o agente usando a cópia de alguma pasta de um projeto real que você tenha aí.
