import sys, os
import pandas as pd

class analiseFaturamento():

    def __init__(self) -> None:

        with open("dados.json", 'r', encoding='utf-8') as file:
            fatMensal = pd.read_json(file)

        fat = fatMensal

        fat = fat[fat['valor'] != 0] # desconsiderando os dias sem fat
        fat = fat.sort_values(by='valor') # ordenando os valores
        valores = fat

        menorFat = valores.iloc[0]
        maiorFat = valores.iloc[-1]

        valor = valores['valor'].iloc[0]



        media = valores['valor'].mean()
        listaValores = valores['valor'].to_list()


        cont = 0
        for i in listaValores:
            if i > media:
                cont += 1
            else:
                continue

        acimaMedia = (valores['valor'].to_list() > media)

       
        menorValor = float(menorFat['valor'])
        maiorValor = float(maiorFat['valor'])

        menorDia = int(menorFat['dia'])
        maiorDia = int(maiorFat['dia'])

        print("---------------")
        print(f"Seu faturamento ultrapassou a média mensal por {cont} dias.")
        print("---------------")
        print(f"Dia {menorDia} teve o menor faturamento do mês: {menorValor:.2f}")
        print("---------------")
        print(f"Dia {maiorDia} teve o maior faturamento do mês: {maiorValor:.2f}")
        print("---------------")


if __name__ == '__main__':
    analiseFaturamento()