from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui",self)
        self.controller = LoginController(self,self)

class Sells(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main.ui",self)

class AppManager:
    def __init__(self):
        self.login_window=Login()
        self.sell_window = None
        
        self.login_window.show()
        
app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())         