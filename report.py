from os.path import exists
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



