"""
Author Hanrun Li
SSW 810 Final Main
"""

from indexer import index_dir
from indexer import print_summary
from indexer import lookup

# remember to change this dir for test
CONST_FILEDIR = "/home/hli68/Programming/SSW810/HanrunLiFinal/HW08TestFiles"


def main():
    """main entrance for HW08"""
    res = index_dir(CONST_FILEDIR)
    print_summary(res)
    lookup(res, 'Sherlock')
    lookup(res, 'I')
    return 0


if __name__ == "__main__":
    main()
