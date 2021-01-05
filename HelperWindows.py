from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from constants import GEOMETRY, TABLE_CSS
from ErrorWindow import Ui_Dialog as ErrorDialog
import logging
logger = logging.getLogger(__name__)


class DataFrameView(QWidget):

    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout(self)
        self.webEngineView = QWebEngineView()
        self.setData()

        vbox.addWidget(self.webEngineView)

        self.setLayout(vbox)

        self.setGeometry(GEOMETRY[0], GEOMETRY[1], GEOMETRY[2], GEOMETRY[3])
        self.setWindowTitle('Search Data')
        logger.debug("DataFrameView object created!")

    def setData(self, df=None):
        html = ""
        html += "<html><style>"
        html += TABLE_CSS
        html += "</style><body><div class=\"container\">"
        if df is not None:
            html += df.to_html()
        html += "</div></body></html>"
        self.webEngineView.setHtml(html)
        logger.info("Data Frame View added the HTML data along with css!")


class StandardErrorDialog(QDialog):
    def __init__(self, parent=None, text=""):
        super().__init__(parent)

        self.ui = ErrorDialog()
        self.ui.setupUi(self, text)
        logger.info(f"Standard Error Dialog initialized with text={text}")
