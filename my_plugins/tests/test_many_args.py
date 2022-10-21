import astroid
import pylint.testutils

from my_plugins import ManyArgsChecker


class TestManyArgsChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = ManyArgsChecker

    def test_検知する場合(self):
        code = """
        def f(a, b, c, d, e): #@ 
            return 0
        """
        node_f = astroid.extract_node(code)

        with self.assertAddsMessages(
                pylint.testutils.MessageTest(msg_id='too-many-args',
                                             args=('f', 5),
                                             line=node_f.lineno,
                                             col_offset=node_f.col_offset,
                                             end_line=node_f.end_lineno,
                                             end_col_offset=node_f.end_col_offset,
                                             node=node_f)
        ):
            self.checker.visit_functiondef(node_f)

    def test_no_message(self):
        code = """
        def f(a, b, c): #@ 
            return 0
        def g(a, b, c, d): #@  
            return 0
        """
        func_node_a, func_node_b = astroid.extract_node(code)

        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node_a)
            self.checker.visit_functiondef(func_node_b)
