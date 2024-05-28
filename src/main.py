def soma(a: int, b: int) -> int:
    return a + b

def subtracao(a: int, b: int) -> int:
    return a - b

def multiplicaca(a: int, b: int) -> int:
    return a * b

def divisao(a: int, b: int) -> int:
    if (b != 0):
        return a/b
    else:
        raise Exception("Impossível dividir por zero.")