import sys

from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import  QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

scene = QGraphicsScene()

img = QGraphicsPixmapItem(QPixmap.fromImage(QImage(sys.argv[1])))
scene.addItem(img)

view = QGraphicsView(scene)

view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
view.setDragMode(QGraphicsView.ScrollHandDrag)

view.showFullScreen()

sys.exit(app.exec_())

