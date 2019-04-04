def SetTheme (app,theme):
    """ Dark = dark theme | White = white theme """
    white = r"assets\css\Style_White.css"
    dark = r"assets\css\Style_Dark.css"
    if theme == 'Dark':
        _style = str(open(dark,'r').read())
    else:
        _style = str(open(white,'r').read())
        
    app.setStyleSheet(_style)