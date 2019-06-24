import platform
import os
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
import vlc
class App(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480


        #Creates vlc instance
        self.instance = vlc.Instance()

        #Chooses the media that we want to play
        self.media = self.instance.media_new("NickMercsThatsLit.mp4")
        #Creates a mediaplyer and loads the selected media in
        self.mediaplayer = self.instance.media_player_new()
        self.mediaplayer.set_media(self.media)



        self.initUI()


    def initUI(self):

        #Create the widget that well display the video on
        self.widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.widget)
        self.videoframe = QtWidgets.QMacCocoaViewContainer(0)

    #Set the color of the defualt background of videoframe widget
        self.palette = self.videoframe.palette()
        self.palette.setColor(QtGui.QPalette.Window, QtGui.QColor(200, 0, 0))
        self.videoframe.setPalette(self.palette)
        self.videoframe.setAutoFillBackground(True)


    #Sets the layout of the video to a vertical layout
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.addWidget(self.videoframe)
        self.widget.setLayout(self.vboxlayout)



        #Set the vlc player to with in the videoframe widget
        self.mediaplayer.set_nsobject(int(self.videoframe.winId()))
#---------------------------------------------------------
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)



        #Plays the video
        self.mediaplayer.play()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

    #