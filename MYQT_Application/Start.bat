@ECHO OFF
cls

REM %localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\MainWindow.ui       -o  .\assets\UI\Scripts\MainWindow.py
REM %localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\ConnectorWindow.ui  -o  .\assets\UI\Scripts\ConnectorWindow.py
REM py.exe App.py

pyuic5 -x .\assets\UI\Layout\MainWindow.ui         -o .\assets\UI\Scripts\MainWindow.py
pyuic5 -x .\assets\UI\Layout\ConnectorWindow.ui    -o .\assets\UI\Scripts\ConnectorWindow.py
python App.py
