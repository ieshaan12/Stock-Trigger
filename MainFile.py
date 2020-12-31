from TriggerClass import TriggerHandler
import logging
from datetime import datetime

if __name__ == "__main__":
    logFile = 'logs/stocktrigger/{}.log'.format(
        datetime.now().strftime("%d-%m-%y"))
    logForm = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s -\
%(funcName)s: %(message)s'
    logging.basicConfig(filename=logFile,
                        filemode='a',
                        format=logForm,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    # trigger1 = Trigger("SBIN.NS", 250, "LE", "Buy SBI", False)
    # trigger2 = Trigger("AXISBANK.BO", 700, "GE", "Sell AXISBANK", False)
    # trigger3 = Trigger("RELIANCE.NS", 2200, "GT", "Sell RIL", False)
    # trigger4 = Trigger("AJANTPHARM.NS", 1600, "LE", "Buy AP", False)
    # trigger5 = Trigger("ITC.NS", 200, "LE", "Buy ITC ASAP", False)
    # trigger6 = Trigger("ONGC.NS", 120, "GT", "Sell ONGC", False)
    # trigger6 = Trigger("BURGERKING.NS", 120, "LE", "Buy BurgerKing", False)
    # trigger7 = Trigger("BHARTIARTL.NS", 450, "LE", "Buy Airtel", False)

    # triggers = [trigger1, trigger2, trigger3, trigger4, trigger5, trigger6, trigger7]

    # TH = TriggerHandler(triggers, sleepTime=5)  # In seconds
    th = TriggerHandler.fromJson()
    th.start()
