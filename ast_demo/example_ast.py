import ast
from pathlib import Path


def main():
    code = Path('code.py').read_text()

    nodes = ast.dump(ast.parse(code), indent=4)
    print(nodes)


if __name__ == '__main__':
    main()
