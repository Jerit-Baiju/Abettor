import chat
import scrapper
from basic_functions import check_all, out

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

    else:
        chat.run(main)


while True:
    run()
