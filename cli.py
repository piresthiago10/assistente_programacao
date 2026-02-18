import argparse
from agent import create_code_assistant


def main():

    parser = argparse.ArgumentParser(
        description="AI Code Assistant"
    )

    parser.add_argument(
        "project_path",
        help="Caminho da pasta do projeto"
    )

    args = parser.parse_args()

    agent = create_code_assistant(args.project_path)

    print("\n=== Code Assistant iniciado ===")
    print("Digite 'exit' para sair\n")

    while True:
        agent.cli_app(stream=True, debug_mode=False)


if __name__ == "__main__":
    main()