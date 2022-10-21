from pathlib import Path

import astroid


def main():
    code = Path('code.py').read_text()

    nodes = astroid.parse(code)

    for node in nodes.body:
        print(node.repr_tree())


if __name__ == '__main__':
    main()
