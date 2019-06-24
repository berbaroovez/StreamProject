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
        #self.media = self.instance.media_new()
        #Creates a mediaplyer and loads the selected media in
        self.mediaplayer = self.instance.media_player_new()
        self.mediaplayer.set_mrl("https://video-weaver.ord02.hls.ttvnw.net/v1/playlist/Cr0DWQtBRBZWEZFtHY1AinsOtgn-9CXiT_k8ieqG33QHq0LHi6CwyCGi33l6gydA7BspRvkOvgf60wKKbQR0e_FHIv7ADzX7JSUrmWvl8dJ95IfnqUWUoxEbEIHbNj_er32zmyMdvqs0Qywd8plM2yfSOQohCm1XOoHlle4NuF_hI-TvvoS5IE-QEjddcV8-gEyXrOK7_zVZbDPufaESOG4_E9jhTCaWczCbm2nlzUwccmcdgwIWQ7nVNTAgMs1j0e_nloBxwASeRzpAN8sE_dzTlhJbH65iB-2FvDwwaMaY08pwhaAqB52I-NGXWfVboAG1TX6DV3_SUSDMJ0V-2qGUIbDrzCDXQpjB9Luk32znNCDUE-OmD6nMvzoC0UlMM0-57wvJ21ktz4zpfRTZirVrQxKnXxVssMFX2yLHgBZqZXqv2PFaagpSv1nhYSTb7I69fFCRB7WDG9Do9NK3onfqV08yZj78k09EW2ZGYfucyWVFYjFyK1HsJz2u97erRIYHwarbnX_zgZYuVPlYgvdaxTmKaVx5ZJOY8frUzJL_1N20W6sEfR7YeyxsSxa-b6ksGsNurpoKkfoSVTV62hIQq-s-qSUlC0Z0JRSDSaNBUBoMQIkcBsL4sxeebjZP.m3u8")



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
      #  self.mediaplayer.play()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    ex.mediaplayer.play()
    sys.exit(app.exec_())

    #