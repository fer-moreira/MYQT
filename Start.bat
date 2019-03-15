@ECHO OFF

cls
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\MainWindow.ui       -o  .\assets\UI\Scripts\MainWindow.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\ConnectorWindow.ui  -o  .\assets\UI\Scripts\ConnectorWindow.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\TB_Creator.ui       -o  .\assets\UI\Scripts\TB_Creator.py
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\DB_Creator.ui       -o  .\assets\UI\Scripts\DB_Creator.py
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\Console.ui          -o  .\assets\UI\Scripts\Console.py
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\PlotVisualizer.ui   -o  .\assets\UI\Scripts\PlotVisualizer.py
py.exe Connector.py

REM cls
REM pyuic5 -x .\assets\UI\Layout\MainWindow.ui         -o .\assets\UI\Scripts\MainWindow.py  
REM pyuic5 -x .\assets\UI\Layout\ConnectorWindow.ui    -o .\assets\UI\Scripts\ConnectorWindow.py  
REM pyuic5 -x .\assets\UI\Layout\TB_Creator.ui         -o .\assets\UI\Scripts\TB_Creator.py
REM pyuic5 -x .\assets\UI\Layout\DB_Creator.ui         -o .\assets\UI\Scripts\DB_Creator.py
REM pyuic5 -x .\assets\UI\Layout\Console.ui            -o .\assets\UI\Scripts\Console.py
REM pyuic5 -x .\assets\UI\Layout\PlotVisualizer.ui     -o  .\assets\UI\Scripts\PlotVisualizer.py
REM pythonw Connector.py
