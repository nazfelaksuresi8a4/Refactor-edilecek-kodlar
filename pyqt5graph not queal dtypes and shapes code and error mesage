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

        self.x = np.array([1, 2, 3, 4,1,2,3,4], dtype=np.int8)                 
        self.y = np.array([1.0, 4.0, 9.0, 16.0,1.0, 4.0, 9.0, 16.0], dtype=np.float64) 

        self.f_arr = []
        self.g_arr = []


        self.t = QTimer(self)
        self.t.timeout.connect(self.plot_updater)
        self.t.start(1000)

        self.index_x = 0
        self.index_y = 0

    def plot_updater(self):

        self.index_x += 1
        self.index_y += 1

        if self.index_x >= len(self.x) or self.index_y >= len(self.y):
            self.t.stop()

            return 0

        self.plotWidget.plot(self.x[self.index_x],self.y[self.index_y])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())





#err msg##


"""

Traceback (most recent call last):
  File "c:\Users\alper\Desktop\Top secret game\database_test.py", line 38, in plot_updater
    self.plotWidget.plot(self.x[self.index_x],self.y[self.index_y])
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\alper\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyqtgraph\graphicsItems\PlotItem\PlotItem.py", line 630, in plot
  File "C:\Users\alper\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyqtgraph\graphicsItems\PlotItem\PlotItem.py", line 630, in plot
    item = PlotDataItem(*args, **kargs)
    item = PlotDataItem(*args, **kargs)
  File "C:\Users\alper\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyqtgraph\graphicsItems\PlotDataItem.py", line 375, in __init__
    self.setData(*args, **kargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\Users\alper\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyqtgraph\graphicsItems\PlotDataItem.py", line 741, in setData
    raise TypeError('When passing two unnamed arguments, both must be a list or array of values. (got %s, %s)' % (str(type(args[0])), str(type(args[1]))))
TypeError: When passing two unnamed arguments, both must be a list or array of values. (got <class 'numpy.int8'>, <class 'numpy.float64'>)

"""
