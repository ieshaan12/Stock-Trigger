import yfinance as yf
import pandas as pd
import hashlib
from threading import Thread
from Notification import Notification,Notification_linux
import time
import json
import copy
import os
import platform

relationDict = {
    "LT": float.__lt__,
    "LE": float.__le__,
    "GT": float.__gt__,
    "GE": float.__ge__,
    "EQ": float.__eq__
}
relationName = {
    "LT": "Less than",
    "LE": "Less than or equal to",
    "GT": "Greater than",
    "GE": "Greater than or equal to",
    "EQ": "Equal"
}


class Trigger:
    def __init__(self, symbol, value, relation, name, deactivateOnTrigger=True):
        # self.triggerbasis = 'Last Traded Price'
        self.symbol = symbol
        self.relation = relationDict[relation]  # Function
        self.relationVar = relation
        self.relationName = relationName[relation]
        self.value = value  # Set by user
        self.name = name
        self.activated = True
        self.autoDeactivateOnTrigger = deactivateOnTrigger
        self.id = hashlib.sha1(self.name.encode()).hexdigest()

    def jsondump(self) -> dict:
        copyself = copy.deepcopy(self)
        dumpdict = copyself.__dict__
        popvars = ['relation', 'relationName', 'activated', 'id']
        for e in popvars:
            dumpdict.pop(e)

        return dumpdict

    def __str__(self):
        return f'{self.symbol}, {self.relationName}, {self.value}, {self.name}, {self.activated}, {self.autoDeactivateOnTrigger}'


class TriggerHandler(Thread):
    def __init__(self, triggers=[], sleepTime=1):
        Thread.__init__(self)
        self.sleepTime = sleepTime
        self.triggers = dict()
        for i in triggers:
            self.triggers[i.id] = i

    def run(self):
        try:
            while True:
                time.sleep(self.sleepTime)
                for i in self.triggers.values():
                    if not i.activated:
                        continue
                    ticker = yf.Ticker(i.symbol)
                    information = ticker.info
                    price = None
                    if information['ask'] == 0:
                        price = float(information['previousClose'])
                    else:
                        price = float(information['ask'])
                    if i.relation(price, float(i.value)):
                        if platform.system() == 'Windows':
                            Notification(i, information['longName'])
                        elif platform.system() == 'Linux':
                            Notification_linux(i,information['longName'])
                        if i.autoDeactivateOnTrigger:
                            i.activated = False
        except Exception as e:
            print(e)

    def addTrigger(self, newTrigger: Trigger) -> None:
        if newTrigger.id in self.triggers:
            print("Name already exists, can't add this trigger with this name")
        else:
            self.triggers[newTrigger.id] = newTrigger
            print("Trigger added")

    def deleteTrigger(self, name: str) -> None:
        hashedName = hashlib.sha1(name.encode()).hexdigest()
        if hashedName in self.triggers:
            self.triggers.pop(hashedName)
            print("Trigger deleted")
        else:
            print("Trigger not present, nothing to delete")

    def listAllTriggers(self):
        df = pd.DataFrame(columns=['Symbol', 'Relation Name', 'Cutoff Price', 'Name', 'Activated', 'Deactivate Status'])
        for i in self.triggers.values():
            temp = pd.DataFrame([[i.symbol, i.relationName, i.value, i.name, i.activated, i.autoDeactivateOnTrigger]],
                                columns=['Symbol', 'Relation Name', 'Cutoff Price', 'Name', 'Activated', 'Deactivate Status'])
            df = pd.concat([df, temp], ignore_index=True)
        return df

    def toJsonFile(self, fileName='dataFile.json'):
        if os.path.exists(fileName):
            os.remove(fileName)
        with open(fileName, 'w+') as fo:
            json.dump({'triggers': [i.jsondump() for i in self.triggers.values()], 'sleepTime': self.sleepTime}, fo, indent=4)

    @classmethod
    def fromJson(cls, fileName='dataFile.json'):
        if not os.path.exists(fileName):
            print("File Doesn't exist")
            return cls()

        with open(fileName) as fi:
            data = json.loads(fi.read())

        triggers = []
        for i in data['triggers']:
            trigger = Trigger(i['symbol'], i['value'], i['relationVar'], i['name'], i['autoDeactivateOnTrigger'])
            triggers.append(trigger)
        handler = cls(triggers, data['sleepTime'])

        return handler

    def __str__(self):
        returnString = "Triggers: \n"
        for i in self.triggers.values():
            returnString += "\t" + i.__str__() + '\n'
        returnString += "sleepTime: " + str(self.sleepTime) + "\n"
        return returnString
