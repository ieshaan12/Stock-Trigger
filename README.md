# Stock Trigger App

This is a windows app which will give you notifications when you set up triggers based on different relations that you provide. A sample file is provided as MainFile.py. 

## Useful Contributions

- Making a GUI which lets you add, view and delete triggers using PyQt5 (preferably, but if you have something, else sure, why not) [Priority - High]
    - Since this program uses threads, you'll probably have to kill the original running process and re-run with new triggers, if triggers are added. If trigger is removed, then no problem either
- Making this cross-platform [Priortiy - Medium]
- Comment the code, I'd prefer to do this later myself, but any volunteers are welcome [Priority - Low]
    - If you take up doing this, follow Numpy's Python Documentaion Format. Available [here](https://numpydoc.readthedocs.io/en/latest/format.html).

Note: Please note that this uses the Linter as flake8.

## Setting Up MainFile.py

I'll be introducing you to setting this up via Task Scheduler. This is so far exclusively for Windows. 

- So, the basic idea is to create a Task using Create Basic Task in the Task Scheduler. 
- Give it whatever name you wish, something like `Stock Trigger`. = - This must start on it's own on Startup, so the trigger must be set `When I log on`. 
- Then it'll just say `Start a Program`, other options are deprecated, so ignore them. 
- Then it'll ask you to set a program/script, now go to your directory for Python (this will be in `C:/`) and select <strong>`pythonw.exe`</strong> not `python.exe` for it to run in background. 
- In the `Add arguments` option give the whole path of `MainFile.py` and for `Start In` give the directory of `this project`.


## Thanks

Big thanks to other repos which helped in making of this project.

- [yfinance](https://github.com/ranaroussi/yfinance)
- [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
- [pandas](https://github.com/pandas-dev/pandas)