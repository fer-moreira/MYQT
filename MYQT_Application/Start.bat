@ECHO OFF
cls

%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\MainWindow.ui       -o  .\assets\UI\Scripts\MainWindow.py
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\ConnectorWindow.ui  -o  .\assets\UI\Scripts\ConnectorWindow.py
py.exe App.py

REM pyuic5 -x .\assets\UI\Layout\MainWindow.ui         -o .\assets\UI\Scripts\MainWindow.py
REM pyuic5 -x .\assets\UI\Layout\ConnectorWindow.ui    -o .\assets\UI\Scripts\ConnectorWindow.py
REM python App.py
