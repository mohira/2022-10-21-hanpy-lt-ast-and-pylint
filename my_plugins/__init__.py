from pylint.lint import PyLinter

from .long_var import TooLongVariableNameChecker
from .many_args import ManyArgsChecker


def register(linter: "PyLinter"):
    linter.register_checker(ManyArgsChecker(linter))
    linter.register_checker(TooLongVariableNameChecker(linter))
