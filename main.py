import train_test as test
import simples, mtrhead
import report

import matplotlib.pyplot as plt
from concurrent.futures import thread
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
def run_tests(data:list, threads:int=0):
    print('Calculando 50 cenários de teste...')
    test.exec_fifty_times(data, 'relatorio_simples')
    for threads in range(1,151):
        if threads%10 == 0:
            test.exec_fifty_times(data, f'relatorio_{threads}_threads', threads)
    


'''Retorna uma lista com as medias de cada cenario executado'''
def run_median() -> list:
    medians = []
    median_simple = test.median_time('relatorio_simples.csv')
    medians.append(median_simple)
    for i in range(1,151):
        if i%10==0:
            median_threads = test.median_time(f'relatorio_{i}_threads.csv')
            medians.append(median_threads)
    return medians


'''Retorna uma lista com os speedups de cada cenario executado'''
def run_speedup(medians:list) -> list:
    speedups = []
    for num in range(0,16):
        speedup_threads = test.speedup(medians[0], medians[num])
        speedups.append(speedup_threads)
    return speedups


'''Gera o gráfico de comparação dos speedups'''
def graph(threads:list):
    plt.title("Comparação de tempo de exec X threas's")
    plt.ylabel('Tempos de exec (ms)', fontsize=20)
    plt.xlabel('Quantidade Threads (x10)', fontsize=20)
    y = []
    for i in range(1,151):
        if i%10==0:
            y.append(test.temp_exec(f'relatorio_{i}_threads.csv'))
    plt.boxplot(y)
    plt.grid(True)
    plt.legend()
    plt.show()
            

def main():
    '''Abre a base de dados que será usada e exclui relatorios previamente criados'''
    threads = mtrhead.gen_thread()

    data = open_file("base_dados/data.csv")
    
    reports = report.find_reports()
    report.delete_report(reports)
    
    '''Roda os testes de 50 cenarios, depois realiza a media dos valores encontrados, calcula o speedup de cada cenario e o percentual de perda de um cenario para outro'''
    run_tests(data)
    medians = run_median()
    speedup = run_speedup(medians)
    
    for i in speedup:
        perc_dif = test.perc_variation(speedup[0],i)

    '''Exibe os resultados obtidos e gera um gráfico com os spedups encontrados'''
    print('\nMédia do tempo de execução calculada dos 50 cenários:')
    print('--------------------------------------------------------------')
    print(f'Media do tempo para execução simples: {medians[0]}')
    for i in range(1,16):
        print(f'Media do tempo para {threads[i-1]} threads: {medians[i]}')

    
    print('\nSpeedups calculado:')
    print('--------------------------------------------------------------')
    for i in range(1,16):
        print(f'Speedup compração simples e {threads[i-1]} threads: {speedup[i]}')
    

    print('\nPercentual de perda entre os speedups:')
    print('--------------------------------------------------------------')
    print(f'O percentual de perda com o aumento de threads foi de: {perc_dif:.2f}%\n')
    
    graph(speedup)

if __name__ == "__main__":
    main()










