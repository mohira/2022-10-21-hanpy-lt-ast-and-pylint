__doc__ = """module a"""


def func_x(arg1, arg2, arg3, arg4, arg5):
    """引数が多い！ && 長い変数名もある"""
    some_value = arg1 + arg2 + arg3 + arg4 + arg5

    # 『リーダブルコード』p.22
    new_navigation_controller_wrapping_view_controller_for_data_source_of_class = 1

    return some_value + new_navigation_controller_wrapping_view_controller_for_data_source_of_class


def func_y(arg1, arg2, arg3):
    """違反していない関数"""
    return arg1 + arg2 + arg3
