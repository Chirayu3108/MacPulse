import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MacPulseWidget(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()


    self.text = QtWidgets.QLabel("Mac Pulse", alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

    layout = QtWidgets.QVBoxLayout(self)
    layout.addWidget(self.text)
    


if __name__ == "__main__":
  app = QtWidgets.QApplication([])
  widget = MacPulseWidget()
  widget.resize(400, 300)
  widget.setWindowTitle("Mac Pulse")
  widget.show()
  sys.exit(app.exec())

    

