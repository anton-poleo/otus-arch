from math import e, nan, inf

from pytest import raises

from ots.qe import solve


def test_solve__without_roots():
    roots = solve(1, 0, 1)
    assert roots == []


def test_solve__with_two_roots():
    roots = solve(1, 0, -1)
    assert roots == [-1, 1]


def test_solve__with_one_root():
    roots = solve(1, 4.000001, 4)
    assert roots == [-7.994345145397156, ]


def test_solve__with_a_equal_zero_error():
    with raises(RuntimeError) as exception:
        roots = solve(e ** -10, 2, 1)

    assert exception.value.args[0] == "a=0 error"


def test_solve__with_input_nan():
    with raises(ValueError) as exception:
        roots = solve(nan, 2, 1)

    assert exception.value.args[0] == "nan or inf input"


def test_solve__with_input_inf():
    with raises(ValueError) as exception:
        roots = solve(inf, 2, 1)

    assert exception.value.args[0] == "nan or inf input"
