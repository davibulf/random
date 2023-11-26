# search the word in the phonetic dictionary and get the phonetic spelling
# search all the phonetic/identical words in the phonetic dictionary
# get all the words with the matching phonetic and put them in a list

import pronouncing


def homophone(word):
    phones = pronouncing.phones_for_word(word)[0]
    k = pronouncing.search(phones)
    k.remove(word)
    print(phones)
    print(k)
    print(len(k))


homophone(input("Insert word: "))
