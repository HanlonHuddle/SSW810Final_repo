"""
Part 2 unittest module
Hanrun Li
"""
import unittest
from indexer import index_dir
from indexer import print_summary
from indexer import lookup

# remember to change this dir for test
CONST_FILEDIR = "/home/hli68/Programming/SSW810/HanrunLiFinal/HW08TestFiles"


def main():
    """ main entrance for test """
    unittest.main(exit=False, verbosity=2)


class FunctionTest(unittest.TestCase):
    """ verify that functions works fine """

    def test_indexer(self):
        """ verify indexer works fine """
        res = index_dir(CONST_FILEDIR)
        self.assertEqual(res[1], 3)
        self.assertEqual(res[2], 592)
        self.assertEqual(res[3], 1341)

        print_summary(res)
        result1 = lookup(res, 'Sherlock')
        result2 = lookup(res, 'reasoning')
        result3 = lookup(res, 'always')
        result4 = lookup(res, 'I')
        result5 = lookup(res, 'Project')
        result6 = lookup(res, 'extra')
        result7 = lookup(res, 'Holmes')
        result8 = lookup(res, 'Ebook')
        result9 = lookup(res, 'Not_a_word')

        cr1 = [['sherlock1.txt', [2, 10, 20]], ['sherlock2.txt', [12, 40]]]
        cr2 = [['sherlock2.txt', [46]], ['sherlock3.txt', [33]]]
        cr3 = [['sherlock2.txt', [40, 85]], ['sherlock3.txt', [31]]]
        cr4 = [['sherlock2.txt', [36, 38, 40, 45, 60, 73, 78, 79, 82, 83, 84, 87, 89, 96, 99,
                                  106, 107, 109, 111, 112]],
               ['sherlock3.txt', [0, 4, 6, 7, 9, 26, 29, 30, 32, 33, 34]]]
        cr5 = [['sherlock1.txt', [2, 6, 20]], ['sherlock2.txt', [2]]]
        cr6 = [['sherlock1.txt', [0]], ['sherlock2.txt', [0]]]
        cr7 = [['sherlock1.txt', [2, 10, 20]], ['sherlock2.txt', [12, 40, 60, 64, 87]],
               ['sherlock3.txt', [4]]]
        cr8 = [['sherlock1.txt', [4, 7, 14, 20]]]
        cr9 = []

        self.assertEqual(result1, cr1)
        self.assertEqual(result2, cr2)
        self.assertEqual(result3, cr3)
        self.assertEqual(result4, cr4)
        self.assertEqual(result5, cr5)
        self.assertEqual(result6, cr6)
        self.assertEqual(result7, cr7)
        self.assertEqual(result8, cr8)
        self.assertEqual(result9, cr9)

        # test with invalid dir
        self.assertRaises(OSError, index_dir("invalid_dir"))


if __name__ == "__main__":
    main()
