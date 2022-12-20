import chat
import scrapper
from base import *

out(["hi there!", "hai there!", "welcome sir", "Greetings from abettor"])


def run():

    main = input("--> ").replace("?", "").replace("_",
                                                  "").casefold().lstrip().rstrip()
    intents = main.split()

    if check_all(['ajent', 'log'], intents) == True:
        out('loading..')
        out(scrapper.ajent_submits())

    elif check_all(['weather'], intents):
        out('loading..')
        out(scrapper.weather())

    elif check_all(['jokes'], intents) == True or check_all(['joke'], intents) == True or check_all(['comedy'], intents):
        try:
            num = word_to_num(intents)
            chat.joke(num)
        except:
            length = 0
            for word in intents:
                length = length + 1
                try:
                    num = int(word)
                    chat.joke(num)
                    break
                except:
                    if length == len(intents):
                        chat.joke(1)
                        break

    elif check_all(['push', 'url'], intents) == True:
        url = main.replace('push url ', '')
        push_url(url)

    elif check_all(['push'], intents) == True:
        content = main.replace('push ', '')
        push(content)

    elif check_all(['spam'], intents) == True:
        length = 0
        for word in intents:
            length = length + 1
            try:
                num = int(word)
                spam(num)
            except:
                if len(intents) == length:
                    out('no number found')

    else:
        chat.run(main)


while True:
    run()
