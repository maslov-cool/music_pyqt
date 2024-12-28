import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl

my_widget_design = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>450</width>
    <height>278</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
    <horstretch>45</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="minimumSize">
   <size>
    <width>450</width>
    <height>278</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>450</width>
    <height>278</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Фортепиано</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 250, 90);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>0</y>
      <width>441</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>MS Reference Sans Serif</family>
      <pointsize>20</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(88, 255, 116);</string>
    </property>
    <property name="text">
     <string>Клавиша F: Space song</string>
    </property>
   </widget>
   <widget class="QPushButton" name="btn">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>110</y>
      <width>241</width>
      <height>101</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 51, 51);</string>
    </property>
    <property name="text">
     <string>Дурак и молния</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>450</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(my_widget_design)
        uic.loadUi(f, self)

        self.player1 = QMediaPlayer()
        self.player2 = QMediaPlayer()
        self.is_playing1 = False
        self.is_playing2 = False
        self.audio = QAudioOutput()

        self.player1.setSource(QUrl.fromLocalFile('korol-i-shut-durak-i-molnija.mp3'))
        self.player2.setSource(QUrl.fromLocalFile('Beach-House-Space-Song.mp3'))

        self.btn.clicked.connect(self.toggle_audio1)

    def toggle_audio1(self):
        if self.is_playing1:
            self.player1.pause()
        else:
            self.player2.pause()
            self.player1.play()
            self.player1.setAudioOutput(self.audio)
        self.is_playing1 = not self.is_playing1

    def keyPressEvent(self, event):
        if event.key() == 70:  # 70 - код клавиши F
            if self.is_playing2:
                self.player2.pause()
            else:
                self.player1.pause()
                self.player2.play()
                self.player2.setAudioOutput(self.audio)
            self.is_playing2 = not self.is_playing2


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exception = except_hook
    sys.exit(app.exec())
