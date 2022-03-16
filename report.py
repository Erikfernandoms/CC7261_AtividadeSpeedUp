from genericpath import isfile
from os.path import exists
import os
import pandas as pd


'''Retorna uma lista com um dataframe contendo as execuções dos cenários para geração do relatório'''
def gen_report(infos:list) -> pd.DataFrame:
    df_list = [(infos[0], infos[1])]
    df = pd.DataFrame(df_list, columns = ['Numeros primos encontrados', 'Tempo de execução'])
    return df


'''Salva o relatório em uma base de dados (.csv)'''
def save_report(df:pd.DataFrame, csv:str):
    if exists(csv):
        report = pd.read_csv(csv)
        if not report.empty:
            final_report = pd.concat([report, df])
            final_report.to_csv(csv, index=False, header=["Numeros primos encontrados","Tempo de execução"])
        else:
            df.to_csv(csv, index=False, header= ["Numeros primos encontrados","Tempo de execução"])
    else:
         df.to_csv(csv, index=False, header= ["Numeros primos encontrados","Tempo de execução"])


'''Exclui os relatórios que já estão criados'''
def delete_report(reports:list):
    for i in reports:
        if exists(f'relatorios/relatorio_{i}_threads.csv'):
            os.remove(f'relatorios/relatorio_{i}_threads.csv')


'''Retorna as threads salvas no relatório'''
def find_reports() -> list:
    reports = []
    for i in range(1,150):
        if i%10==0:
            reports.append(i)
    return reports            
        

        
