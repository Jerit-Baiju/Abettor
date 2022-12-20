import random
from word2number import w2n

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


def check_any(any, intents):
    return any + intents


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

def spam(num):
    try:
        from pushbullet import Pushbullet
        pb = Pushbullet('id')
        for _ in range(num):
            pb.push_note('Abettor', 'SPAM', pb.devices[0])
        out('spam success')
    except:
        out('no network')


print(word_to_num('hi forty three thousand'.split()))