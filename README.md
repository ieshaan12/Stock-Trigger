# Stock Trigger App

This is a windows app which will give you notifications when you set up triggers based on different relations that you provide. A sample file is provided as MainFile.py. 

## Useful Contributions

- Making a GUI which lets you add, view and delete triggers using PyQt5 (preferably, but if you have something, else sure, why not) [Priority - High]
    - Since this program uses threads, you'll probably have to kill the original running process and re-run with new triggers, if triggers are added. If trigger is removed, then no problem either
- Making this cross-platform [Priortiy - Medium]
- Comment the code, I'd prefer to do this later myself, but any volunteers are welcome [Priority - Low]
    - If you take up doing this, follow Numpy's Python Documentaion Format. Available [here](https://numpydoc.readthedocs.io/en/latest/format.html).

Note: Please note that this uses the Linter as flake8.

## Thanks

Big thanks to other repos which helped in making of this project.

- [yfinance](https://github.com/ranaroussi/yfinance)
- [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
- [pandas](https://github.com/pandas-dev/pandas)