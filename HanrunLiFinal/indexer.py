"""
Indexer which index all txt files in a given folder
Hanrun Li
"""

from os import listdir
from os import chdir


def index_dir(directory):
    """ function to analyze and index the dir """
    try:
        listdir(directory)
    except OSError:
        return
    else:
        pass
    flist = listdir(directory)
    chdir(directory)
    index_result = {}
    # summarize the total number of files
    file_number = 0
    # total distinct words
    dist_word_number = 0
    # total words read from all files
    words_total = 0
    for file_name in flist:
        if file_name.endswith('.txt'):
            file_number += 1
            try:
                fprocess = open(file_name, 'r')
            except FileNotFoundError:
                print("Can't find file:", file_name)
            else:
                with fprocess:
                    line_number = -1
                    for line in fprocess:
                        line_number += 1
                        for origin_word in line.split():
                            word = origin_word.lower()
                            words_total += 1
                            if not word in index_result:
                                dist_word_number += 1
                                index_result[word] = {}
                                index_result[word][file_name] = []
                                index_result[word][file_name].append(line_number)
                            else:
                                if not file_name in index_result[word]:
                                    index_result[word][file_name] = []
                                    index_result[word][file_name].append(line_number)
                                else:
                                    if not line_number in index_result[word][file_name]:
                                        index_result[word][file_name].append(line_number)
    result = [index_result, file_number, dist_word_number, words_total]
    return result


def print_summary(res):
    """" Function to print the summary of index result """
    print('The summary of index result: (All words normalized to lower case)')
    print('Total of', res[1], 'files')
    print('Total of', res[2], 'distinct words')
    print('Total of', res[3], 'words read')
    print()


def lookup(res, word_in):
    """ Finction to lookup and print the result of finding a certain word """
    index_res = res[0]
    word = word_in.lower()
    ans = []
    if word in index_res:
        print("Result of", "'" + word_in + "':", '(All words normalized to lower case.)')
        for key in index_res[word]:
            tmp = [key]
            tmp.append(sorted(index_res[word][key]))
            ans.append(tmp)
        ans.sort()
        print(ans)
    else:
        print("Word", word, 'not found in the txt files')
    print()
    return ans
