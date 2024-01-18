#!/usr/bin/python3
if __name__ == "__main__":
    from calculator _1 import mul, add, sub, div

    a = 10
    b = 5
    add = add(a, b)
    sub = sub(a, b)
    mul = mul(a, b)
    div = div(a, b)
    print("{0:d} + {1:d} = {2:d}".format(a, b, add))
    print("{0:d} - {1:d} = {2:d}".format(a, b, sub))
    print("{0:d} * {1:d} = {2:d}".format(a, b, mul))
    print("{0:d} / {1:d} = {2:d}".format(a, b, div))
