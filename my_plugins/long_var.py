from astroid import nodes
from pylint.checkers import BaseChecker


class TooLongVariableNameChecker(BaseChecker):
    name = 'too-long-var-name'
    msgs = {
        'E9998': (
            '😢 "%s" is too long. got=%d',
            'too-long-var-name',
            '変数名が長いということは？'
        )
    }

    def visit_assign(self, a: nodes.Assign) -> None:
        for target in a.targets:
            target: nodes.AssignName
            length = len(target.name)

            if length >= 20:
                self.add_message(msgid='too-long-var-name', args=(target.name, length), node=a)
