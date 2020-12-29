import yfinance as yf
import pandas as pd
import hashlib
from threading import Thread
from Notification import Notification
import time


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
        self.triggerbasis = 'Last Traded Price'
        self.symbol = symbol
        self.relation = relationDict[relation]  # Function
        self.relationName = relationName[relation]
        self.value = value  # Set by user
        self.name = name
        self.activated = True
        self.autoDeactivateOnTrigger = deactivateOnTrigger
        self.id = hashlib.sha1(self.name.encode())

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
                        price = information['previousClose']
                    else:
                        price = information['ask']
                    if i.relation(price, i.value):
                        Notification(i, ticker['longName'])
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
        hashedName = hashlib.sha1(name.encode())
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
