from base import *


class Data():
    instances = []

    def __init__(self, intent):
        self.words = intent.split()
        self.type_triggers = []
        if 'is' in self.words:
            self.type_triggers.append('assign')
        # if 

        Data.instances.append(self)


a = Data('my name is Jerit')
print(a.get_type())
