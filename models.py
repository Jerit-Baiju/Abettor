from base import *


class Data():
    instances = []

    def __init__(self, text):
        self.data = text
        self.intents = text.split()
        self.type_triggers = []
        if check_any(['is', 'are'], self.intents):
            self.type_triggers.append('assign')
        if '?' in self.data:
            self.type_triggers.append('question')

        Data.instances.append(self)


a = Data('my name is Jerit?')
print(a.type_triggers)
