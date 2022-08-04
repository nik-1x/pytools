class DiffieHellmanEncrypt:
    """ Diffie Hellman library """

    def __init__(self):
        print("Init:", self.__doc__)

    def do(self, g: int, a: int, p: int) -> int:
        c = 0
        f = 1
        a = bin(a)
        a = a[2:len(a)]
        g = g % p
        for i in range(0, len(a)):
            c *= 2
            f = (f * f) % p
            if a[i] == '1':
                c += 1
                f = (f * g) % p
        return f
