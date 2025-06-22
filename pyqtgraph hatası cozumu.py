#pyqtgraph arrayleri destekler yani tek bir çıplak veri türünden diğer veri türüne örneğin .plot(0,1) gibi bir kullanım hatalı olur örnek kullanım aşağıdaki gibidir...


  import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer 
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.plotWidget = pg.PlotWidget()
        self.setCentralWidget(self.plotWidget)

        self.x = np.array([1, 2, 3, 4, 1, 2, 3, 4], dtype=np.int8)                 
        self.y = np.array([1.0, 4.0, 9.0, 16.0, 1.0, 4.0, 9.0, 16.0], dtype=np.float64) 

        self.display_x = []
        self.display_y = []

        self.curve = self.plotWidget.plot(pen='y')  # Single persistent plot curve

        self.t = QTimer(self)
        self.t.timeout.connect(self.plot_updater)
        self.t.start(1000)  # update every second

        self.index = 0

    def plot_updater(self):
        if self.index >= len(self.x):
            self.t.stop()
            return

        self.display_x.append(self.x[self.index])
        self.display_y.append(self.y[self.index])

        self.curve.setData(self.x[self.index], self.y[self.index]) #bir arrayın içindeki mevcut veriyi indeksleme ile aldık ve plot ettirdik ve buda normal bir value yerine npArray olarak algılandı#
        self.index += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

