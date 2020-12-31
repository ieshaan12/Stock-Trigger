import yfinance as yf
import pandas as pd
import hashlib
from threading import Thread
from Notification import Notification
import time
import json
import copy
import os
import sys
import logging
logger = logging.getLogger(__name__)

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
        logger.info("Trigger with name: {} created for stock: {}".format(name, symbol))

    def jsondump(self) -> dict:
        copyself = copy.deepcopy(self)
        dumpdict = copyself.__dict__
        popvars = ['relation', 'relationName', 'activated', 'id']  # * Consider removing id or not
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
        logger.info("Creating a class of TriggerHandler")

    def run(self):
        logger.info("Thread of TriggerHandler initialized")
        count = 0
        try:
            while True:
                count += 1
                time.sleep(self.sleepTime)
                logger.debug(f"Checking, Run: {count}")
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
                        Notification(i, information['longName'])
                        if i.autoDeactivateOnTrigger:
                            i.activated = False
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error("ERROR! Type: {}, File: {}, Line: {}".format(exc_type, fname, exc_tb.tb_lineno))

    def addTrigger(self, newTrigger: Trigger) -> None:
        if newTrigger.id in self.triggers:
            print("Name already exists, can't add this trigger with this name")
            logger.debug("Trigger with id: {} already exists [name: {}]".format(newTrigger.id, newTrigger.name))
        else:
            self.triggers[newTrigger.id] = newTrigger
            logger.debug("Trigger added with name: {} and id: {}".format(newTrigger.name, newTrigger.id))

    def deleteTrigger(self, name: str) -> None:
        hashedName = hashlib.sha1(name.encode()).hexdigest()
        if hashedName in self.triggers:
            self.triggers.pop(hashedName)
            logger.debug("Trigger deleted, Name: {}".format(name))
        else:
            logger.debug("Trigger with name:{} not present, nothing to delete".format(name))

    def listAllTriggers(self):
        df = pd.DataFrame(columns=['Symbol', 'Relation Name', 'Cutoff Price', 'Name', 'Activated', 'Deactivate Status'])
        for i in self.triggers.values():
            temp = pd.DataFrame([[i.symbol, i.relationName, i.value, i.name, i.activated, i.autoDeactivateOnTrigger]],
                                columns=['Symbol', 'Relation Name', 'Cutoff Price', 'Name', 'Activated', 'Deactivate Status'])
            df = pd.concat([df, temp], ignore_index=True)
        logger.info("All triggers returned as DataFrame")
        return df

    def toJsonFile(self, fileName='dataFile.json'):
        if os.path.exists(fileName):
            os.remove(fileName)
            logger.debug(f"Removing json file: {fileName}")
        with open(fileName, 'w+') as fo:
            json.dump({'triggers': [i.jsondump() for i in self.triggers.values()], 'sleepTime': self.sleepTime}, fo, indent=4)
        logger.debug(f"New file created: {fileName}")

    @classmethod
    def fromJson(cls, fileName='dataFile.json'):
        logger.debug("Class method fromJson called")
        if not os.path.exists(fileName):
            logger.debug(f"File:{fileName} Doesn't exist")
            return cls()

        with open(fileName) as fi:
            data = json.loads(fi.read())

        triggers = []
        for i in data['triggers']:
            trigger = Trigger(i['symbol'], i['value'], i['relationVar'], i['name'], i['autoDeactivateOnTrigger'])
            triggers.append(trigger)
        handler = cls(triggers, data['sleepTime'])
        logger.info(f"New class of TriggerHandler returned from jsonfile: {fileName}")
        return handler

    def __str__(self):
        returnString = "Triggers: \n"
        for i in self.triggers.values():
            returnString += "\t" + i.__str__() + '\n'
        returnString += "sleepTime: " + str(self.sleepTime) + "\n"
        return returnString
