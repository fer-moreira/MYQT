@ECHO OFF
cls

REM NO ADM USER COMPUTER
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\UI\LAYOUT\MainWindow.ui         -o .\Lib\UI\SCRIPT\MainWindow.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\UI\LAYOUT\ConnectorWindow.ui    -o .\Lib\UI\SCRIPT\ConnectorWindow.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\UI\LAYOUT\ErrorPopup.ui         -o .\Lib\UI\SCRIPT\ErrorPopup.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\UI\LAYOUT\Testes.ui             -o .\Lib\UI\SCRIPT\Testes.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\UI\LAYOUT\Console.ui             -o .\Lib\UI\SCRIPT\Console.py  
py.exe Connector.py

REM REM NORMAL COMPUTER
REM pyuic5 -x .\Lib\UI\LAYOUT\MainWindow.ui      -o .\Lib\UI\SCRIPT\MainWindow.py  
REM pyuic5 -x .\Lib\UI\LAYOUT\ConnectorWindow.ui -o .\Lib\UI\SCRIPT\ConnectorWindow.py  
REM pyuic5 -x .\Lib\UI\LAYOUT\ErrorPopup.ui      -o .\Lib\UI\SCRIPT\ErrorPopup.py  
REM pyuic5 -x .\Lib\UI\LAYOUT\Testes.ui          -o .\Lib\UI\SCRIPT\Testes.py  
REM pyuic5 -x .\Lib\UI\LAYOUT\Console.ui          -o .\Lib\UI\SCRIPT\Console.py  
REM python Connector.py

