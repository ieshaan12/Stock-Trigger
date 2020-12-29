from TriggerClass import TriggerHandler, Trigger

if __name__ == "__main__":
    trigger1 = Trigger("TSLA", 500, "LT", "YOLO ON Tesla", False)
    trigger2 = Trigger("AAPL", 200, "GE", "SELL APPLE", True)
    trigger3 = Trigger("GOOG", 2000, "GT", "SELL GOOGLE STOCK", True)
    trigger4 = Trigger("MSFT", 225, "GT", "Hmmmmm", False)

    TH = TriggerHandler([trigger1, trigger2, trigger3, trigger4], sleepTime=5)
    TH.start()
