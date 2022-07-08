from math import sqrt, e, floor, nan, inf


def solve(a: float, b: float, c: float, eps: float = e ** -5):
    if abs(a) < eps:
        raise RuntimeError("a=0 error")

    input_nan = nan in (a, b, c)
    input_inf = inf in (a, b, c)

    if input_nan or input_inf:
        raise ValueError("nan or inf input")

    descriminant = b ** 2 - 4 * a * c
    if descriminant < 0:
        return []
    elif descriminant > eps:
        x1 = (-b + sqrt(descriminant)) / 2 * a * c
        x2 = (-b - sqrt(descriminant)) / 2 * a * c
        return sorted([x1, x2])
    else:
        x = (-b + sqrt(descriminant)) / 2 * a * c
        return [x, ]
        # return [round(x, 2), ]
