"""Main logic"""

import sys

from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window

def main():
    #Create app
    app = QApplication(sys.argv)
    # # Connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    #Create main window
    win = Window()
    win.show()
    #Run
    sys.exit(app.exec())
