class fibonacci():
    def __init__(self) -> None:            
        num = int(input("Digite um numero: "))

        def fibonacci(numero):
            lista = []
            n1, n2 = 0, 1

            while n1 <= numero:
                lista.append(n1)
                n1, n2 = n2, n1 + n2
            return lista

        if num in fibonacci(num):
            print(f"{num} pertence na sequencia de fibonacci")
        else: 
            print(f"{num} não pertence na sequencia de fibonacci")

if __name__ == '__main__':
    fibonacci()