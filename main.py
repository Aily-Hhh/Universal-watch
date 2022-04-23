import sys

from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication

from UserInt.mainwindow import MainWindow


app = QApplication(sys.argv)
app.setFont(QFont("Century Gothic", 10))

mw = MainWindow()
palette = QPalette()
palette.setColor(QPalette.Window, QColor(152, 251, 152))
mw.setPalette(palette)
mw.show()

sys.exit(app.exec_())
