import train_test as test
import simples, mtrhead
import report
import matplotlib.pyplot as plt
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
    test.exec_fifty_times(data, 'relatorio_5_threads', 3)
    test.exec_fifty_times(data, 'relatorio_500_threads', 6)


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


'''Gera o gráfico de comparação dos speedups'''
def graph(y1,y2):
    x = [0, 1]
    y1 = [0, y1]
    y2 = [0, y2] 
    plt.title("Comparação de speedup's")
    plt.xlabel('Speedup', fontsize=20)
    plt.ylabel('Margem Speedup', fontsize=20)
    plt.plot(x,y1, color='green', label='Poucas thread')
    plt.plot(x,y2, color='red', label='Muitas threads')
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    '''Abre a base de dados que será usada e exclui relatorios previamente criados'''
    data = open_file("base_dados/data.csv")
    reports = ["relatorio_simples","relatorio_5_threads","relatorio_500_threads"]
    report.delete_report(reports)
    
    '''Roda os testes de 50 cenarios, depois realiza a media dos valores encontrados, calcula o speedup de cada cenario e o percentual de perda de um cenario para outro'''
    run_tests(data)
    medians = run_median(reports)
    speedup = run_speedup(medians)
    perc_dif = test.perc_variation(speedup[0],speedup[1])

    '''Exibe os resultados obtidos e gera um gráfico com os spedups encontrados'''
    print('\nMédia do tempo de execução calculada dos 50 cenários:')
    print('--------------------------------------------------------------')
    print(f'Tempo de execução simples: {medians[0]} ms')
    print(f'Tempo de execução com poucas threads: {medians[1]} ms')
    print(f'Tempo de execução com muitas threads: {medians[2]} ms\n')

    print('Speedups calculado:')
    print('--------------------------------------------------------------')
    print(f'Speedup compração simples e poucas threads: {speedup[0]}')
    print(f'Speedup compração simples e muitas threads: {speedup[1]}\n')

    print('Percentual de perda entre os speedups:')
    print('--------------------------------------------------------------')
    print(f'O percentual de perda com o aumento de threads foi de: {perc_dif:.2f}%\n')
    
    graph(speedup[0], speedup[1])

if __name__ == "__main__":
    main()










