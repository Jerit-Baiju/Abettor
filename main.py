import chat
import scrapper
from basic_functions import *

out(["hi there!", "hai there!", "welcome sir", "Greetings from abettor"])


def run():

    main = input("--> ").replace("?", "").replace("_",
                                                  "").casefold().lstrip().rstrip()
    split = main.split()

    if check_all(['ajent', 'log'], split) == True:
        out('loading..')
        out(scrapper.ajent_submits())

    elif check_all(['weather'], split) == True:
        out('loading..')
        out(scrapper.weather())

    elif check_all(['jokes'], split) == True or check_all(['joke'], split) == True or check_all(['comedy'], split):
        length = 0
        for word in split:
            length = length + 1
            try:
                num = int(word)
                chat.joke(num)
            except:
                 if length == len(split):
                     chat.joke(1)

    elif check_all(['push','url'], split) == True:
        url = main.replace('push url ', '')
        push_url(url)

    elif check_all(['push'], split) == True:
        content = main.replace('push ', '')
        push(content)

    
    elif check_all(['spam'], split) == True :
        length = 0
        for word in split:
            length = length + 1
            try:
                num = int(word)
                spam(num)
            except:
                if len(split) == length:
                    out('no number found')

    else:
        chat.run(main)

   

    


while True:
    run()
