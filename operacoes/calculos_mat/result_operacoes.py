from unittest import result


def operacao(a,b,op):
    if op ==1:
        result = a + b
    if op ==2:
        result = a - b
    if op ==3:
        result = a * b
    if op ==4:
        result = a / b
    return result