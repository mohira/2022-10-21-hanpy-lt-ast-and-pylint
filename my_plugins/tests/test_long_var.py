import astroid
import pylint.testutils
import pytest

from my_plugins import TooLongVariableNameChecker


class TestTooLongVariableNameChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = TooLongVariableNameChecker

    def test_発見する(self):
        code = """
        aaaaabbbbbccccceeeee = 1 #@
        """
        assign = astroid.extract_node(code)

        with self.assertAddsMessages(
                pylint.testutils.MessageTest(msg_id='too-long-var-name',
                                             args=('aaaaabbbbbccccceeeee', 20),
                                             line=assign.lineno,
                                             col_offset=assign.col_offset,
                                             end_line=assign.end_lineno,
                                             end_col_offset=assign.end_col_offset,
                                             node=assign)
        ):
            self.checker.visit_assign(assign)

    def test_no_message(self):
        code = """
        aaaaabbbbbccccceeee = 1 #@
        """
        a = astroid.extract_node(code)

        with self.assertNoMessages():
            self.checker.visit_assign(a)

    def test_複数の変数への代入の場合の処理は未定義(self):
        pytest.fail('TODO')
