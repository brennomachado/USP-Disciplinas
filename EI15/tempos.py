from fibonacci_eficiente import fibonacciI, fibonacciR

from timeit import default_timer as timer

def main():
    #lista = [5, 10, 20, 30, 40]
    lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

    start = timer()
    for i in lista:
        start = timer()
        fibo = fibonacciR(i)
        end = timer()
        print(f"FibonacciR({i}) = {fibo}   =>   Tempo = {end - start}s")

        start = timer()
        fibo = fibonacciI(i)
        end = timer()

        print(f"FibonacciI({i}) = {fibo}   =>   Tempo = {end - start}s\n")
        

if __name__ == '__main__':
    main()
