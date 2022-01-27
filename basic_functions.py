from pushbullet import Pushbullet
import random
pb = Pushbullet('o.dWvpPTPP3dsH2vglR3y4YwZyE9AhvPeV')

def push(text):
    pb.push_note('Abettor', text, pb.devices[0])

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
