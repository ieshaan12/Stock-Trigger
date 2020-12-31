from win10toast import ToastNotifier
import os


class Notification:
    def __init__(self, trigger=None, CompanyName: str = ""):
        self.toast = ToastNotifier()
        self.toast.show_toast(trigger.name, f"{CompanyName}'s has been triggered, Price {trigger.relationName} {trigger.value}")

class Notification_linux:
    def __init__(self, trigger=None, CompanyName: str = ""):
        title = "Stock Trigger"
        message = f"{CompanyName}'s has been triggered, Price {trigger.relationName} {trigger.value}"
        os.system('notify-send "{}" "{}"'.format(title,message))
