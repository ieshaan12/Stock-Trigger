import platform
if platform.system() == 'Windows':
    from win10toast import ToastNotifier
elif platform.system() == 'Linux':
    import os
import logging
logger = logging.getLogger(__name__)


class Notification:
    def __init__(self, trigger=None, CompanyName: str = ""):
        if platform.system() == 'Windows':
            self.toast = ToastNotifier()
            self.toast.show_toast(trigger.name, f"{CompanyName}'s has been triggered, Price {trigger.relationName} {trigger.value}")
        elif platform.system() == 'Linux':
            title = "Stock Trigger"
            message = f"{CompanyName}'s has been triggered, Price {trigger.relationName} {trigger.value}"
            os.system('notify-send "{}" "{}"'.format(title,message))
        logger.info(f"Trigger initialized with name: {trigger.name} for company: {CompanyName}")
