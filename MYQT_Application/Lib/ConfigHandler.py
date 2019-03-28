import configparser

from PyQt5.Qt import QMainWindow

# config = configparser.ConfigParser()
# config.read(r'prefs.ini')

# # [Connection]
# # server,port,buffered,trusted
#     # [Credentials]
#     # login
#         # [Options]
#         # theme,language

# _connction = config['Connection']
# _credentials = config['Credentials']
# _option = config['Options']

# user = _credentials['login']

# def load_config ():
#     print("AA")

# def save_config ():
#     print("BB")

class ConfigHandler (object):
    def __init__(self,window):
        self.config = configparser.ConfigParser()
        self.config.read(r'settings\prefs.ini')
        
        self.types = {'mysql':0,'mssql':1,'postgre':2}
        self.reverse_type = {0:'mysql',1:'mssql',2:'postgre'}


        self._connection    = self.config['Connection']
        self._credentials   = self.config['Credentials']
        self._option        = self.config['Options']

        self.w = window

    
    def load_config (self):
        sv_host     = self._connection['server']
        sv_port     = self._connection['port']
        sv_buff     = self._connection['buffered']
        sv_remember = self._connection['remember']
        
        # opt_theme = self._option['theme']
        # opt_language = self._option['language']
        opt_type = self.types.get(self._option['type'])

        crdt_login = self._credentials['login']
        crdt_pass  = self._credentials['pass']


        self.w.host_in.setText(sv_host)
        self.w.port_in.setText(sv_port)
        
        self.w.buffered.setChecked (self.conditional(sv_buff))
        self.w.remember.setChecked (self.conditional(sv_remember))

        self.w.user_in.setText(crdt_login)
        self.w.pass_in.setText(crdt_pass)
        
        self.w.dbType.setCurrentIndex(opt_type)

    def save_config (self):
        self._connection['server']      = str(self.w.host_in.displayText())
        self._connection['port']        = str(self.w.port_in.displayText())
        self._connection['buffered']    = str(self.w.buffered.checkState())
        self._connection['remember']    = str(self.w.remember.checkState())

        self._credentials['login']      = str(self.w.user_in.displayText())

        if self.w.remember.isChecked() == True: self._credentials['pass'] = str(self.w.pass_in.text())
        else: self._credentials['pass'] = ""

        self._option['type'] = self.reverse_type.get(self.w.dbType.currentIndex())

        with open(r'settings\prefs.ini', 'w') as cf:
            self.config.write(cf)

    def conditional (self,config):
        if config == "2":return True
        elif config == "0":return False

