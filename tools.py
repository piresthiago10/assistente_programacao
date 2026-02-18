import os
from typing import List

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build"
}

EXCLUDED_FILES = {
    ".env",
    ".gitignore"
}

EXCLUDED_EXTENSIONS = {
    ".bak",
    ".log"
}


def _is_valid_file(file: str) -> bool:
    if file in EXCLUDED_FILES:
        return False

    _, ext = os.path.splitext(file)
    if ext in EXCLUDED_EXTENSIONS:
        return False

    return True


def list_files(project_path: str) -> List[str]:
    """
    Lista arquivos de código dentro do projeto,
    ignorando diretórios e arquivos irrelevantes.
    """
    code_files = []

    for root, dirs, files in os.walk(project_path):

        # remove dirs excluídos do walk
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in files:
            if _is_valid_file(file):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, project_path)
                code_files.append(rel_path)

    return code_files


def read_code(project_path: str, files_list: List[str]) -> dict:
    """
    Lê o conteúdo de um ou mais arquivos.
    Retorna dict {filepath: content}
    """
    contents = {}

    for file in files_list:
        full_path = os.path.join(project_path, file)

        if not os.path.exists(full_path):
            contents[file] = "FILE NOT FOUND"
            continue

        with open(full_path, "r", encoding="utf-8") as f:
            contents[file] = f.read()

    return contents


def write_file(project_path: str, filepath: str, content: str) -> str:
    """
    Escreve ou sobrescreve um arquivo dentro do projeto.
    """
    full_path = os.path.join(project_path, filepath)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"File written: {filepath}"