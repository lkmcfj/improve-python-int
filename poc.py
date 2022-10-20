import functools
import decimal
from decimal import Decimal

@functools.cache
def quick_power_16(y: int) -> Decimal:
    if y == 0:
        return Decimal(1)
    t = quick_power_16(y // 2)
    t = t * t
    if y % 2 == 1:
        t = t * Decimal(16)
    return t

THRESHOLD_FMT = 500

def divide_hex_str(a: str) -> Decimal:
    if len(a) <= THRESHOLD_FMT:
        return Decimal(int(a, base=16))
    mid = (len(a) + 1) // 2
    l = divide_hex_str(a[:mid])
    r = divide_hex_str(a[mid:])
    return l * quick_power_16(len(a) - mid) + r

def int_to_str(a: int) -> str:
    hex_str = hex(a)[2:]
    hex_len = len(hex_str)
    assert hex_len * 2 <= decimal.MAX_PREC
    assert hex_len * 2 <= decimal.MAX_EMAX
    prev = decimal.getcontext()
    decimal.setcontext(decimal.Context(prec=hex_len * 2, Emax=hex_len * 2))
    ans = str(divide_hex_str(hex_str))
    decimal.setcontext(prev)
    return ans

THRESHOLD_PARSE = 1000

def divide_str(a: str, base: int, qp) -> int:
    if len(a) <= THRESHOLD_PARSE:
        return int(a, base=base)
    mid = (len(a) + 1) // 2
    l = divide_str(a[:mid], base, qp)
    r = divide_str(a[mid:], base, qp)
    return l * qp(len(a) - mid) + r

def str_to_int(x: str, base: int = 10) -> int:

    @functools.cache
    def quick_power(y: int) -> int:
        if y == 0:
            return 1
        t = quick_power(y // 2)
        t = t * t
        if y % 2 == 1:
            t = t * base
        return t
    return divide_str(x, base, quick_power)
