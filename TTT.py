"""
    @author: Hanrun
"""
from random import randint
import unittest

class TTT:
    """TTT Game"""
    def __init__(self, n):
        self.N = int(n)
        self.map = []
        for i in range(self.N):
            self.map.append([])

    def fill(self):
        for i in range(self.N):
            for j in range(self.N):
                des = randint(1, 3)
                if des == 1:
                    self.map[i].append(' ')
                elif des == 2:
                    self.map[i].append('X')
                else:
                    self.map[i].append('O')
    
    def myPrint(self):
        for i in range(self.N):
            print(self.map[i])
    
    def win(self):
        for i in range(self.N):
            c = self.map[i][0]
            win = 1
            for j in range(self.N):
                if not self.map[i][j] == c:
                   win = 0
                   break
            if win == 1 and not c == ' ':
                return 1
        for i in range(self.N):
            c = self.map[0][i]
            win = 1
            for j in range(self.N):
                if not self.map[j][i] == c:
                   win = 0
                   break
            if win == 1 and not c == ' ':
                return 1
        
        c = self.map[0][0]
        win = 1
        for i in range(self.N):
            if not self.map[i][i] == c:
                win = 0
                break
        if win == 1 and not c == ' ':
            return 1

        c = self.map[0][self.N-1]
        win = 1
        for i in range(self.N):
            if not self.map[i][self.N-1] == c:
                win = 0
                break
        if win == 1 and not c == ' ':
            return 1
        
        return 0

class FractionTest(unittest.TestCase):
    """ verify that Fraction class works fine """
    def test_init(self):
        """ verify that the numerator and denominator are set properly """


def main():
    """main entrance for testinf Fraction class, only test cases here"""
    # unittest.main(exit=False, verbos ity=2)
    t = TTT(3)
    t.fill()
    t.myPrint()
    print(t.win())
    return

if __name__ == "__main__":
    main()
