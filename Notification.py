from win10toast import ToastNotifier
import logging
logger = logging.getLogger(__name__)


class Notification:
    def __init__(self, trigger=None, CompanyName: str = ""):
        self.toast = ToastNotifier()
        self.toast.show_toast(trigger.name, f"{CompanyName}'s has been triggered, Price {trigger.relationName} {trigger.value}")
        logger.info(f"Trigger initialized with name: {trigger.name} for company: {CompanyName}")
