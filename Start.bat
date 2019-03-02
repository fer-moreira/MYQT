@ECHO OFF

REM cls
REM %localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\MainWindow.ui       -o  .\assets\UI\Scripts\MainWindow.py  
REM %localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\ConnectorWindow.ui  -o  .\assets\UI\Scripts\ConnectorWindow.py  
REM %localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\TB_Creator.ui       -o  .\assets\UI\Scripts\TB_Creator.py
REM %localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\DB_Creator.ui       -o  .\assets\UI\Scripts\DB_Creator.py
REM %localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\Console.ui          -o  .\assets\UI\Scripts\Console.py
REM %localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\assets\UI\Layout\PlotVisualizer.ui   -o  .\assets\UI\Scripts\PlotVisualizer.py
REM py.exe Connector.py

cls

pyuic5 -x .\assets\UI\Layout\MainWindow.ui         -o .\assets\UI\Scripts\MainWindow.py  
pyuic5 -x .\assets\UI\Layout\ConnectorWindow.ui    -o .\assets\UI\Scripts\ConnectorWindow.py  
pyuic5 -x .\assets\UI\Layout\TB_Creator.ui         -o .\assets\UI\Scripts\TB_Creator.py
pyuic5 -x .\assets\UI\Layout\DB_Creator.ui         -o .\assets\UI\Scripts\DB_Creator.py
pyuic5 -x .\assets\UI\Layout\Console.ui            -o .\assets\UI\Scripts\Console.py
pyuic5 -x .\assets\UI\Layout\PlotVisualizer.ui     -o  .\assets\UI\Scripts\PlotVisualizer.py
pythonw Connector.py
