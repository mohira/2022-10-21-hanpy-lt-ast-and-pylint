from astroid import nodes
from pylint.checkers import BaseChecker


class ManyArgsChecker(BaseChecker):
    name = 'many-args'
    msgs = {
        'E9999': (
            'đș "%s" has too many args. got=%d',
            'too-many-args',
            'ćŒæ°ă5ćăăăŁăŠăăšăŻăăŁăšăăèš­èšăăăăăăăȘăăźăăȘïŒ'
        )
    }

    def visit_functiondef(self, f: nodes.FunctionDef) -> None:
        count_args = len(f.args.args)

        criteria = 5
        if count_args >= criteria:
            self.add_message(msgid='too-many-args', args=(f.name, count_args), node=f)
