import sys

from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PySide6.QtGui import  QImage, QPixmap
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtCore import Qt

class View(QGraphicsView):
    percent = 1.0

    def __init__(self, scene, original=None, item=None):
        self.original = QImage(original)
        self.canvas = scene
        self.item = item

        super().__init__(scene)
    
    def __resize(self):
        if(self.item != None):
            self.canvas.removeItem(self.item)
        
            width = self.original.width()*self.percent
            height = self.original.height()*self.percent
            
            image = self.original.scaled(width, height)
            item = QGraphicsPixmapItem(QPixmap.fromImage(image))

            self.setSceneRect(0, 0, image.width(), image.height())
            self.canvas.addItem(item)
            self.item = item
            
            del image
            del item

    def wheelEvent(self, e):
        if(e.angleDelta().y() > 0):
            self.percent*=0.90
            self.__resize()
			
        else:
            if(self.percent > 0):
                self.percent*=1.10
            self.__resize()

app = QApplication(sys.argv)

scene = QGraphicsScene()

img = QGraphicsPixmapItem(QPixmap.fromImage(QImage(sys.argv[1])))
scene.addItem(img)

view = View(scene, sys.argv[1], img)

view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
view.setDragMode(QGraphicsView.ScrollHandDrag)

view.showFullScreen()

sys.exit(app.exec())

