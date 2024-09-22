
class soma():

    def __init__(self) -> None:        
        indice = 13
        soma = 0
        k = 0

        while k < indice:
            k += 1
            soma += k

        print(f"Resultado da soma {soma}")

if __name__ == "__main__":
    soma()
