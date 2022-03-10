from main import exec_mthred, exec_simple
from report import save_report, gen_report

import pandas as pd
from statistics import median


'''Executa 50 cenários de teste'''
def exec_fifty_times(data:list, report:str, threads:int=0):
    for i in range(50):
        if threads == 0:
            infos = exec_simple(data)
        else:
            infos = exec_mthred(data, threads)
        save_report(gen_report(infos), f"relatorios/{report}.csv")


'''Retorna a media dos tempos de execução da base da dados'''
def median_time(report:str) -> int:
    df = pd.read_csv(f"relatorios/{report}.csv")
    time_exec = df['Tempo de execução']
    return median(time_exec)


'''Retorna o speedup baseado nos tempos de execução passados'''
def speedup(time_exec1:int , time_exec2:int) -> int:
    return time_exec1/time_exec2


'''Retorna o valor do percentual de perda dos valores passados'''
def perc_variation(x:int, y:int) -> int:
    return ((x-y)*100)/x
    


