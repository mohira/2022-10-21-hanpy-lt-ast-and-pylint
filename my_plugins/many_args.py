from astroid import nodes
from pylint.checkers import BaseChecker


class ManyArgsChecker(BaseChecker):
    name = 'many-args'
    msgs = {
        'E9999': (
            '👺 "%s" has too many args. got=%d',
            'too-many-args',
            '引数が5個あるってことはもっとよい設計があるんじゃないのかな？'
        )
    }

    def visit_functiondef(self, f: nodes.FunctionDef) -> None:
        count_args = len(f.args.args)

        criteria = 5
        if count_args >= criteria:
            self.add_message(msgid='too-many-args', args=(f.name, count_args), node=f)
