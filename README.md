# CC7261_AtividadeSpeedUp

Código destinado para análise dos problemas apresentados em aula:
 1. Quanto mais threads, o SpeedUp melhora?
 
 2. Qual a melhor quebra para ser feita? (Quebra = qtdd de threads!)

 3. Por que se aumentamos MUITO a quantidade de threads, perdemos o SpeedUp?
 
 4. Qual a fração serial do problema?


## Primeiro vamos ao funcionamento do código

Este código visa nos mostrar como é o funcionamento de uma execução de um sistema sem threads e com multi threads e para isso, analisaremos uma base com 250mil valores inteiros e contaremos a quantidade de numeros primos que encontramos nos valores da base de dados.

O código funciona da seguinte forma:

  1. Geração dos relatórios auxiliares
     - Nesse momento, são executados 50 testes para cada cenário disposto no código! Para responder as perguntas propostas, utilizaremos os seguintes cenários: Execução simples (apenas a contagem de numeros primos sem threads), execução com multi threads aumentando gradualmente de 10 em 10 threads até 150 threads.
     - Os 50 testes são salvos em relatórios auxiliares (.csv) contendo a quantidade de numeros primos encontrados mais o tempo de execução de cada teste.
     
![2022-03-10-12-13-40_Trim](https://user-images.githubusercontent.com/70040215/157693185-93de9bc8-1125-4aa4-8d94-fd3f55950c52.gif)


  2. Análise dos relatorios auxiliares
     - A etapa de análise consiste no cálculo da média do tempo de execução dos valores salvos na etapa anterior.
     - Com essa média já podemos ter uma noção da diferença de cada cenário proposto, podendo assim calcular o speedup dos sistemas com multi thread e sem threads.
     - Tendo os valores do speedup realizamos um cálculo para ver o percentual de perda entre os cenários apresentados.

  3. Exibição dos resultados no relatório final
     - Para o relatório final, é organizado e printado todos os valores encontrados anteriormente. Dispondo também, da criação de um gráfico que nos mostra a comparação entre os speedup's encontrados.



# Relatório final + Respondendo as perguntas 

## Relatório final


![image](https://user-images.githubusercontent.com/70040215/158587199-d0c05130-9c1b-45a5-ab46-5df9f28d96f9.png)
![image](https://user-images.githubusercontent.com/70040215/158587181-64e24e58-1650-42d5-a105-9ddf42fe93f7.png)
 
## Respondendo perguntas

***1. Quanto mais threads, o SpeedUp melhora?***
 *R: Não! Como podemos observar nos resultados mostrados anteriormente, foram testados 15 cenários com o aumento de 10 em 10 threads! Podemos observar que com o aumento das threads o SpeedUp piorou.*
 
 ***2. Qual a melhor quebra para ser feita? (Quebra = qtdd de threads!)***
 *R: Para essa pergunta não temos uma resposta exata, tudo depende do sistema e das operações que serão realizadas! Mas olhando para o problema proposto, assumimos que de 2 thread até 6 threads temos um minúsculo ganho entre eles o que não chega a ser significativo, acima disso temos total perda do speedup. Mesmo tendo um ganho nada significativo, nenhum superou a execução sem threads.*

 ***3. Por que se aumentamos MUITO a quantidade de threads, perdemos o SpeedUp?***
 *R: Para que um sistema multi threads funcione, será necessário haver uma comunicação entre cada thread (troca de contexto) e isso consome tempo do processador e memória! Um sistema com MUITAS threads terão múltiplas trocas de contexto o que fará o processador gastar um tempo maior na comunicação das threads do que de fato na realização das operações!*
 
 ***4. Qual a fração serial do problema?***
 *R: Para o primeiro cenário apresentado (execução com 10 threads), temos:* ![image](https://user-images.githubusercontent.com/70040215/157707933-67f051ae-80ef-40b5-85cb-d8497216f2dd.png)

*Já para o segundo cenário (execução 150 threads), temos:*                                                 
![image](https://user-images.githubusercontent.com/70040215/157708079-d6850af7-4711-4371-97da-6ddb338f6702.png)

 
 
## Execução do código

A execução do código é bem simples, apenas execute o arquivo *main.py*

## Alunos envolvidos

Erik Fernando Mendes Silva RA:22.119.074-7                                           
Rafael Tocegui Compri      RA:22.119.063-0
