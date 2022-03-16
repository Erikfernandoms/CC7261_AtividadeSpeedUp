import sympy
import concurrent.futures as thread


'''Gera as threads'''
def gen_thread() -> list:
    threads=[]
    for i in range(1,151):
        if i % 10 == 0:
            threads.append(i)
    return threads

'''Retorna a quantidade de num. primos achados na base de dados passada com threads'''
def tCalculaPrimo(data:list, primes:int=0) -> int:
    for i in range(len(data)):
        if sympy.isprime(data[i]):
            primes  += 1
    return primes 


def resolve_trhread(data, ThreadsQtdd):
    lenlista = len(data)
    index = range(0, lenlista+(lenlista//ThreadsQtdd), lenlista//ThreadsQtdd)
    primes  = 0
    with thread.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(ThreadsQtdd):
            futures.append(executor.submit(tCalculaPrimo, data=data[index[i]:index[i+1]]))
        for future in thread.as_completed(futures):
            primes += future.result()
    return primes
