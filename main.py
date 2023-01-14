from PySide6.QtGui import QIcon

from GUI.WinContr.mw import MainWindow
from PySide6.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    app.setWindowIcon(QIcon(":/App/Icons/Logo/EM_Logo.png"))
    app.exec()