import random
from word2number import w2n
import requests
import numpy as np

def inp(text):
    return input(f"--> {str(text).upper()} > ")


def out(value):
    if type(value) == str:
        return print(f">>> {str(value).upper()} .")
    elif type(value) == list:
        return print(f">>> {str(random.choice(value)).upper()} .")


def check_all(list, split):
    return all(value in split for value in list)


def compare(list, main_word, split):
    if main_word in split:
        split.pop(split.count(main_word))
        for other_word in list:
            if other_word in split:
                return True


def check_any(words, intents):
    for word in words:
        if word in intents:
            return True


def english_words():
    list_1 = np.array(requests.get('https://raw.githubusercontent.com/Jerit-Baiju/english-words/master/words.txt').text.split())
    list_2 = np.array(requests.get('https://raw.githubusercontent.com/Jerit-Baiju/dictionary/master/popular.txt').text.split())

    op = np.append(list_1,list_2)
    # print(op)
    return  op
            


def find_hidden_word(array):
    arr = []
    count = 3
    op = []
    dictionary = english_words()
    for _ in range(len(array)):
        initial = 0
        final = initial + count
        for _ in range(len(array)):
            if final != len(array) + 1:
                if array[initial:final] not in arr:
                    arr.append(array[initial:final])
                    initial += 1
                    final += 1
        count += 1
    for x in arr:
        word = ''
        for i in x:
            word = word + i
        if word in dictionary:
            op.append(word)
    return op


def push(content):
    try:
        from pushbullet import Pushbullet
        pb = Pushbullet('id')
        pb.push_note('Abettor', content, pb.devices[0])
        out(f'push success ({content}) ')
    except:
        out('No network')


def push_url(url):
    try:
        from pushbullet import Pushbullet
        pb = Pushbullet('id')
        pb.push_link('Abettor', url, device=pb.devices[0])
        out(f'url pushed ({url}) ')
    except:
        out('No network')


def word_to_num(intents):
    nums = ''
    for word in intents:
        if word in w2n.american_number_system.keys():
            nums = f'{nums}{word} '
    return w2n.word_to_num(nums)
