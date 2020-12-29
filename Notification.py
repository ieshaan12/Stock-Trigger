from win10toast import ToastNotifier


class Notification:
    def __init__(self, trigger=None, CompanyName: str = ""):
        self.toast = ToastNotifier()
        self.toast.show_toast(trigger.name, f"{CompanyName}'s has been triggered, Price {trigger.relationName} {trigger.value}")
