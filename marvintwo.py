#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""marvin-filer marvin4"""


def filanalys():
    """Analysera filer"""

    filtext = input("1. Enter the file's name (.txt) : ")
    fileLower = filtext.lower()

    def mostCommonWords(files):
        """ 7 mest förekommande ord"""

        fhand = open(files)
        counts = dict()
        for line in fhand:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) +1
                lst = list()
                commonWords = list()
            for key, val in counts.items():
                lst.append((val, key))
                lst.sort(reverse=True)

            for val, key in lst[:7]:
                commonWords += key, val

        return "\n".join(map(str, commonWords))

    def commonWordsTwo(files):
        """7 mest förekommande ord utan dem vanliga"""

        fhand = open(files)
        counts = dict()
        for line in fhand:
            words = line.split()
            for word in words:
                with open('common-words.txt', 'r') as line:
                    data = line.read()
                    if word in data:
                        pass
                    elif '\'' in word or '\'s' in word or '*' in word:
                        pass
                    else:
                        counts[word] = counts.get(word, 0) +1
            lst = list()
            commonWords = list()
            for key, val in counts.items():
                lst.append((val, key))
                lst.sort(reverse=True)
            for val, key in lst[:7]:
                commonWords += key, val

        return "\n".join(map(str, commonWords))


    def commonCorrectlyWords(files):
        """7 mest förekommande ord utan dem vanliga"""

        fhand = open(files)
        counts = dict()
        for line in fhand:
            words = line.split()
            for word in words:
                with open('common-words.txt', 'r') as line:
                    data = line.read()
                with open('words.txt', 'r') as lines:
                    datas = lines.read()
                    if word in data:
                        pass
                    elif word in datas:
                        counts[word] = counts.get(word, 0) +1
            lst = list()
            commonWords = list()
            for key, val in counts.items():
                lst.append((val, key))
                lst.sort(reverse=True)
            for val, key in lst[:7]:
                commonWords += key, val

        return "\n".join(map(str, commonWords))


    def letterFrekvens(files):
        """7 mest kommande bokstaver"""
        from collections import Counter
        fhand = open(files, 'r')
        data = fhand.read()
        dataRemix = data.lower()
        textNospace = dataRemix.replace(' ', '')
        letters = Counter(textNospace)
        commonLetters = list()
        listeFinal = list()
        for key, val in letters.items():
            commonLetters.append((val, key))
            commonLetters.sort(reverse=True)
        for val, key in commonLetters[:7]:
            """beräkna %"""
            leng = len(textNospace) #längden av filen utan 'space'
            listeFinal += key, round((val*100/leng), 2)
        return "\n".join(map(str, listeFinal))




    if fileLower == 'quotes.txt' or fileLower == 'test.txt':
        with open(fileLower, 'r') as line:
            data = line.read()
            leng = len(data)
            sevenMostCommonWords = mostCommonWords(fileLower)
            sevenMostNoUsually = commonWordsTwo(fileLower)
            sevenMostLetters = letterFrekvens(fileLower)
            sevencorrectspelled = commonCorrectlyWords(fileLower)
            print("\n 2. The file %s has : " % fileLower)
            print("%s Words" % leng)
            print("\n 3. The seven most common words are : ")
            print("----------------------------------")
            print(sevenMostCommonWords)
            print("\n 4. The seven most common words expect usual are : ")
            print("------------------------------------------------------------\n")
            print(sevenMostNoUsually)
            print("\n 5. The seven most common words and correct spelled are : ")
            print("------------------------------------------------------------\n")
            print(sevencorrectspelled)
            print('\n 6. The seven most common letters in (%) are : ')
            print('---------------------------------------')
            print(sevenMostLetters)



    else:
        print('file dont exist and by defautl E-G analyse Alice-file : \n')
        with open('alice-ch1.txt', 'r') as line:
            data = line.read()
            leng = len(data)
            sevenMostCommonWords = mostCommonWords('alice-ch1.txt')
            sevenMostNoUsually = commonWordsTwo('alice-ch1.txt')
            sevenMostLetters = letterFrekvens('alice-ch1.txt')
            sevencorrectspelled = commonCorrectlyWords('alice-ch1.txt')
            print('2. Alice-file has :')
            print('----------------')
            print('%s words' % leng)

            print("\n 3. The seven most common words are : ")
            print('-------------------------------------')
            print(sevenMostCommonWords)
            print('\n 4. The seven most common words expect usually words are : ')
            print('----------------------------------------------------------')
            print(sevenMostNoUsually)
            print("\n 5. The seven most common words and correct spelled are : ")
            print("------------------------------------------------------------\n")
            print(sevencorrectspelled)
            print('\n 6. The seven most common letters in (%) are : ')
            print('---------------------------------------')
            print(sevenMostLetters)
