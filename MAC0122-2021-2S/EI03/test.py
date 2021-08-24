class Fraction:
    def __init__(self, cima, baixo):
        print("__init\n")
        self.num = cima
        self.den = baixo

    def __str__(self):
        print("__str\n")
        return f"{self.num}/{self.den}"

    def show(self):
        print("__show\n")
        print(f"{self.num}/{self.den}")

    def __add__(self, other):
        print("__ad\n")
        #novonum = self.num*other.den + self.den*other.num
        #novoden = self.den*other.den
        #comum = mdc(novonum, novoden)
        return True

    def __eq__(self, other):
         primeiro = self.num * other.den
         segundo  = other.num * self.den
         print("__eq\n")
         return primeiro == segundo

def main():
    f1 = Fraction(3,2)
    f2 = Fraction(2,3)

    # print(f1)
    f3 = f1 + f2

if __name__ == "__main__":
    main()
