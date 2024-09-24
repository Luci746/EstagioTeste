
class reverse():

    def __init__(self) -> None:

        self.palavra = str(input("digite uma palavra para inverter: "))

        def invert(self, palavra) -> str:

            extendido = list(palavra)
            
            # inversão de cadeia de caracteres
            listaInvertida = []
            index = len(extendido)
            for i in range(index):
                inverso = (index - i -1)
                listaInvertida.append(extendido[inverso])
            
            # convertendo cadeia de caracteres para string
            cont = 0
            plv = ""
            for i in listaInvertida:
                plv += i[cont]
                
            print(f"aqui está: {plv}")

        invert(self, self.palavra)

if __name__ == '__main__':
    reverse()
