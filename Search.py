import requests
import lxml.html as lh
import pandas as pd
import logging
logger = logging.getLogger(__name__)


class Search:
    searchstring = "https://finance.yahoo.com/lookup?s={}&.TSRC=FIN-SRCH"

    def __init__(self, name=""):
        self._name = name
        self.results = None
        self.resultsDataFrame = None
        logging.info(f"Logger initialized with name: {name}")

    def topResults(self) -> int:
        page = requests.get(Search.searchstring.format(self._name))
        doc = lh.fromstring(page.content)
        # Getting results
        tableRowElements = doc.xpath('//tr')
        if len(tableRowElements) == 0:
            logging.warning(f"No elements returned for {self._name}")
            return -1
        col = []
        i = 0
        # * You will get 25 top search results
        for t in tableRowElements[0]:
            i += 1
            name = t.text_content()
            # print(i, ": ", name)
            col.append((name, []))

        for j in range(1, len(tableRowElements)):
            # T is our j'th row
            T = tableRowElements[j]

            # i is the index of our column
            i = 0

            # Iterate through each element of the row
            for t in T.iterchildren():
                data = t.text_content()
                # Check if row is empty
                if i > 0:
                    # Convert any numerical value to integers
                    try:
                        data = float(data)
                    except:  # noqa: E722
                        logger.debug("Not integer data, IGNORE")
                # Append the data to the empty list of the i'th column
                col[i][1].append(data)
                # Increment i for the next column
                i += 1

        stockDict = {title: column for (title, column) in col}
        df = pd.DataFrame(stockDict)
        self.resultsDataFrame = df
        self.results = list(df['Name']+' - '+df['Symbol'])
        logger.debug("results and resultsDataFrame populated")
        return 0

    def getTopSearch(self) -> str:
        if self.results:
            return self.results[0]
        else:
            print("Run topResults() first, otherwise null string will be returned")
            logger.debug("No self.results, therefore empty string returned")
        return ""

    def setName(self, name=""):
        self._name = name
