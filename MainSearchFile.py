from Search import Search
import logging
from datetime import datetime
import os

if __name__ == "__main__":
    if os.path.isdir('logs'):
        if os.path.isdir('logs/search'):
            pass
        else:
            os.mkdir('logs/search')
    else:
        os.mkdir('logs')
        if os.path.isdir('logs/search'):
            pass
        else:
            os.mkdir('logs/search')

    logFile = 'logs/search/{}.log'.format(
        datetime.now().strftime("%d-%m-%y"))
    logForm = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s -\
%(funcName)s: %(message)s'
    logging.basicConfig(filename=logFile,
                        filemode='a',
                        format=logForm,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    logging.debug("----- PROGRAM[MainSearchFile.py] RUN START FROM HERE -----")
    search = Search("Axis Bank")
    retVal = search.topResults()
    if retVal == -1:
        print("No elements returned")
        exit(0)
    print(search.results)
    print(search.resultsDataFrame)
    print(search.getTopSearch())
