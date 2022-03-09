import sympy

def resolve_simples(data:list, primos:int=0) -> int:
    for i in data:
        if sympy.isprime(i):
            primos += 1
    return primos