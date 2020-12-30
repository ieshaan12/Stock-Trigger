from Search import Search

if __name__ == "__main__":
    search = Search("Axis Bank")
    search.topResults()

    print(search.results)
    print(search.resultsDataFrame)
    print(search.getTopSearch())
