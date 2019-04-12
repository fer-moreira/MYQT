import configparser

from PyQt5.Qt import QMainWindow
from PyQt5.QtWidgets import QApplication


class ConfigHandler (object):
    def __init__(self, window):

        self.types = {'mysql': 0, 'mssql': 1, 'postgre': 2}
        self.reverse_type = {0: 'mysql', 1: 'mssql', 2: 'postgre'}

        self.config = configparser.ConfigParser()
        self.config.read(r'settings\prefs.ini')
        self._connection = self.config['Connection']
        self._credentials = self.config['Credentials']
        self._option = self.config['Options']
        self.w = window

    def load_config(self):
        sv_host = self._connection['server']
        sv_port = self._connection['port']
        sv_buff = self._connection['buffered']
        sv_remember = self._connection['remember']

        # opt_language = self._option['language']
        opt_type = self.types.get(self._option['type'])

        crdt_login = self._credentials['login']
        crdt_pass = self._credentials['pass']

        self.w.host_in.setText(sv_host)
        self.w.port_in.setText(sv_port)

        self.w.buffered.setChecked(self.conditional(sv_buff))
        self.w.remember.setChecked(self.conditional(sv_remember))

        self.w.user_in.setText(crdt_login)
        self.w.pass_in.setText(crdt_pass)

        self.w.dbType.setCurrentIndex(opt_type)

    def save_config(self):
        self._connection['server'] = str(self.w.host_in.displayText())
        self._connection['port'] = str(self.w.port_in.displayText())
        self._connection['buffered'] = str(self.w.buffered.checkState())
        self._connection['remember'] = str(self.w.remember.checkState())

        self._credentials['login'] = str(self.w.user_in.displayText())

        if self.w.remember.isChecked() == True:
            self._credentials['pass'] = str(self.w.pass_in.text())
        else:
            self._credentials['pass'] = ""

        self._option['type'] = self.reverse_type.get(
            self.w.dbType.currentIndex())
        self.save()

    def save_theme(self, themeIsDark):
        if themeIsDark == True:
            self._option['theme'] = str("Dark")
        else:
            self._option['theme'] = str("White")
        self.save()

    def load_theme(self):
        opt_theme = self._option['theme']
        white = str(open(r'assets\css\Style_White.css', 'r').read())
        dark = str(open(r'assets\css\Style_Dark.css', 'r').read())
        if opt_theme == "White":
            self.w.setStyleSheet(white)
        elif opt_theme == "Dark":
            self.w.setStyleSheet(dark)
        elif opt_theme == "Custom":
            c_path = r'%s' % self._option['custompath']
            custom_theme = str(open(c_path, 'r').read())
            self.w.setStyleSheet(custom_theme)

    def themeIsDark(self):
        if self._option['theme'] == "White":
            return False
        else:
            return True

    def conditional(self, config):
        if config == "2":
            return True
        elif config == "0":
            return False

    def save(self):
        with open(r'settings\prefs.ini', 'w') as cf:
            self.config.write(cf)
