from eg_binomial import binomialI, binomialR, binomialRM, binomialRC, binomialFAT 

from timeit import default_timer as timer

def main():
    

    for n,k in [(0,0),(3,2),(5,1),(1,5),(4,2),(3,6),(160,30)]:
        start = timer()
        biR = binomialR(n,k)
        end = timer()
        print(f"BinomialR ({n},{k}) = {biR}     => Tempo: {end-start}s")

        start = timer()
        biI = binomialI(n,k)
        end = timer()
        print(f"BinomialI ({n},{k}) = {biI}     => Tempo: {end-start}s")

        start = timer()
        biR = binomialRC(n,k)
        end = timer()
        print(f"BinomialRC ({n},{k}) = {biR}     => Tempo: {end-start}s")

        start = timer()
        biI = binomialFAT(n,k)
        end = timer()
        print(f"BinomialFAT ({n},{k}) = {biI}     => Tempo: {end-start}s\n")
        

if __name__ == '__main__':
    main()
