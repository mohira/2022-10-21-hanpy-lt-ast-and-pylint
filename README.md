# 2022-10-21 はんなりPython プログラミングに詳しくなるための静的解析

## スライド

[2022-10-21 はんなりPython プログラミングに詳しくなるための静的解析](https://docs.google.com/presentation/d/1azFHtHx_M25fPUIe-Gn3HlOxpj7MTH2cLAle-g_hYyo/edit#slide=id.p)

## 主張

- ASTを学ぶとプログラミングに詳しくなれる
- 自作のLintツールを作ることで意見を具体化する
- 自作のLintツールのは大変ではない
- ASTを学ぶコツは語彙を正確に扱う

## demo

```python
# src/a.py
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

```

```
$ pylint --load-plugins=my_plugins src --init-hook='import sys; sys.path.append(".")'
************* Module a
src/a.py:4:0: E9999: 👺 "func_x" has too many args. got=5 (too-many-args)
src/a.py:9:4: E9998: 😢 "new_navigation_controller_wrapping_view_controller_for_data_source_of_class" is too long. got=75 (too-long-var-name)
```
