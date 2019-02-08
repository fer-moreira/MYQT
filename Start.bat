@ECHO OFF
cls

:ESPECIFIC COMPUTER
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\MainWindow.ui         -o .\assets\UI\Scripts\MainWindow.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\ConnectorWindow.ui    -o .\assets\UI\Scripts\ConnectorWindow.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\TB_Creator.ui         -o .\assets\UI\Scripts\TB_Creator.py
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\DB_Creator.ui         -o .\assets\UI\Scripts\DB_Creator.py
py.exe Connector.py
