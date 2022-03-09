import sympy

'''Retorna a quantidade de num. primos achados na base de dados passada sem threads'''
def resolve_simple(data:list, primos:int=0) -> int:
    for i in data:
        if sympy.isprime(i):
            primos += 1
    return primos