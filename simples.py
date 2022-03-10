import sympy

'''Retorna a quantidade de num. primos achados na base de dados passada sem threads'''
def resolve_simple(data:list, primes:int=0) -> int:
    for i in data:
        if sympy.isprime(i):
            primes += 1
    return primes