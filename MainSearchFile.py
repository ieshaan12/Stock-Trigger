from Search import Search
import logging
from datetime import datetime

if __name__ == "__main__":
    logFile = 'logs/search/{}.log'.format(
        datetime.now().strftime("%d-%m-%y"))
    logForm = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s -\
%(funcName)s: %(message)s'
    logging.basicConfig(filename=logFile,
                        filemode='a',
                        format=logForm,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    search = Search("Axis Bank")
    search.topResults()

    print(search.results)
    print(search.resultsDataFrame)
    print(search.getTopSearch())
