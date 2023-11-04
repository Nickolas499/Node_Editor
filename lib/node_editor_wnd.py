from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from lib.node_scene import Scene
from lib.node_node import Node
from lib.node_socket import Socket
from lib.node_graphics_view import QDMGraphicsView



class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stylesheet_filename = 'qss/nodestyle.qss'
        self.loadStylesheet(self.stylesheet_filename)

        self.initUI()


    def initUI(self):
        self.setGeometry(1750, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # crate graphics scene
        self.scene = Scene()

        node = Node(self.scene, "Hello World",inputs=[1,2,3,4], outputs=[1,2])
        # node2 = Node(self.scene, "Hello World2")
        #self.grScene = self.scene.grScene

        # create graphics view

        self.view = QDMGraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)




        self.setWindowTitle("Node Editor")
        self.show()

    def loadStylesheet(self, filename):
        print('STYLE loading:', filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        QApplication.instance().setStyleSheet(str(stylesheet, encoding='utf-8'))



