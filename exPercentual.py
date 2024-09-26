import pandas as pd

class distribuidora():

    def __init__(self) -> None:
        # • SP – R$67.836,43
        #• RJ – R$36.678,66
        #• MG – R$29.229,88
        #• ES – R$27.165,48
        #• Outros – R$19.849,53
        #Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve #dentro do valor total mensal da distribuidora.

        fatMensal = {
            "dist" : {
                "SP" : 67836.43,
                "RJ" : 36678.66,
                "MG" : 29229.88,
                "ES" : 27165.48,
                "Outros" : 19849.53
            }
            
        }

        dados = pd.DataFrame(fatMensal)

        print(dados['dist'])

        total = (dados['dist'].sum() / 100)

        print(total)
     
if __name__ == '__main__':
    distribuidora()