import train_test as test
import simples, mtrhead
import report

from time import perf_counter_ns

'''Retorna uma lista com os numeros primos e o tempo de execução do script sem threads'''
def exec_simple(data:list) -> list:
    start_simples = perf_counter_ns()
    primo_simples = simples.resolve_simple(data)
    finish_simples = perf_counter_ns()
    exec_time = (finish_simples-start_simples)/1000000
    return [primo_simples, exec_time]


'''Retorna uma lista com os numeros primos e o tempo de execução do script com threads'''
def exec_mthred(data:list, threads:int) -> list:
    start_mthread = perf_counter_ns()
    primo_mthread = mtrhead.resolve_trhread(data, threads)
    finish_mthread = perf_counter_ns()
    exec_time = (finish_mthread-start_mthread)/1000000
    return [primo_mthread, exec_time]


'''Retorna uma lista com os numeros primos da base de dados'''
def open_file(csv) -> list:
    with open(csv) as file:
        data = [line.strip() for line in file]
    data = list(map(int, data))
    return data


'''Roda os 50 cenarios de teste para cada cenario'''
def run_tests(data:list):
    print('Calculando 50 cenários de teste...')
    test.exec_fifty_times(data, 'relatorio_simples')
    test.exec_fifty_times(data, 'relatorio_5_threads', 5)
    test.exec_fifty_times(data, 'relatorio_500_threads', 500)


'''Retorna uma lista com as medias de cada cenario executado'''
def run_median(reports:list) -> list:
    median_simple = test.median_time(reports[0])
    median_few_threads = test.median_time(reports[1])
    median_lot_threads = test.median_time(reports[2])
    return [median_simple, median_few_threads, median_lot_threads]


'''Retorna uma lista com os speedups de cada cenario executado'''
def run_speedup(medians:list) -> list:
    speedup_simple_few_threads = test.speedup(medians[0], medians[1])
    speedup_simple_lot_threads = test.speedup(medians[0], medians[2])
    return [speedup_simple_few_threads, speedup_simple_lot_threads]


def main():
    data = open_file("base_dados/data.csv")
    reports = ["relatorio_simples","relatorio_5_threads","relatorio_500_threads"]
    report.delete_report(reports)
  
    run_tests(data)
    medians = run_median(reports)
    speedup = run_speedup(medians)
    
    print('Média do tempo de execução calculada dos 50 cenários:')
    print('--------------------------------------------------------------')
    print(f'Tempo de execução simples: {medians[0]} ms')
    print(f'Tempo de execução com poucas threads: {medians[1]} ms')
    print(f'Tempo de execução com muitas threads: {medians[2]} ms\n')

    print('Speedups calculado:')
    print('--------------------------------------------------------------')
    print(f'Speedup compração simples e poucas threads: {speedup[0]}')
    print(f'Speedup compração simples e muitas threads: {speedup[1]}\n')



if __name__ == "__main__":
    main()










