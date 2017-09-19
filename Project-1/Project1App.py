# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project1GUI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import Adafruit_DHT


sensor = 0
pin = 0
		
	

class Ui_Project1EID(object):

    def __init__(self):
        self.temperatureString = 0
        self.humidityString = 0

    def temperatureReadingPrint(self):
        self.humidityString, self.temperatureString = Adafruit_DHT.read_retry(sensor, pin)
        t = QtCore.QTime()
        print("Temperature:"+ str(self.temperatureString) + " at Time:"+ t.currentTime().toString())
        print("\n")
        if self.temperatureString is not None:
            self.temperature_text.setText(str(self.temperatureString))
            self.temperature_request_time.setText(t.currentTime().toString())
        else:
            self.temperature_text.setText("Connection Failed")
            
            
    def humidityReadingPrint(self):
        self.humidityString, self.temperatureString = Adafruit_DHT.read_retry(sensor, pin)
        t = QtCore.QTime()
        print("Humidity:"+ str(self.humidityString) + " at Time:"+ t.currentTime().toString())
        print("\n")
        if self.humidityString is not None:
            self.humidity_text.setText(str(self.humidityString))
            self.humidity_request_time.setText(t.currentTime().toString())
        else:
            self.humidity_text.setText("Connection Failed")
            
    def retranslateUi(self, Project1EID):
        _translate = QtCore.QCoreApplication.translate
        Project1EID.setWindowTitle(_translate("Project1EID", "Project1EID"))
        self.temperature_Button.setText(_translate("Project1EID", "Temperature"))
        self.humidity_Button.setText(_translate("Project1EID", "Humidity"))
        self.temperature_timeout_label.setText(_translate("Project1EID", "Request Time"))
        self.humidity_timeout_label.setText(_translate("Project1EID", "Request Time"))

    def setupUi(self, Project1EID):
        Project1EID.setObjectName("Project1EID")
        Project1EID.resize(800, 396)
        self.temperature_Button = QtWidgets.QPushButton(Project1EID)
        self.temperature_Button.setGeometry(QtCore.QRect(130, 120, 93, 28))
        self.temperature_Button.setObjectName("temperature_Button")
        self.humidity_Button = QtWidgets.QPushButton(Project1EID)
        self.humidity_Button.setGeometry(QtCore.QRect(130, 260, 93, 28))
        self.humidity_Button.setObjectName("humidity_Button")
        self.temperature_text = QtWidgets.QLineEdit(Project1EID)
        self.temperature_text.setGeometry(QtCore.QRect(250, 120, 113, 31))
        self.temperature_text.setText("")
        self.temperature_text.setObjectName("temperature_text")
        self.humidity_text = QtWidgets.QLineEdit(Project1EID)
        self.humidity_text.setGeometry(QtCore.QRect(250, 260, 113, 31))
        self.humidity_text.setObjectName("humidity_text")
        self.temperature_request_time = QtWidgets.QLineEdit(Project1EID)
        self.temperature_request_time.setGeometry(QtCore.QRect(410, 120, 113, 31))
        self.temperature_request_time.setObjectName("temperature_request_time")
        self.humidity_request_time = QtWidgets.QLineEdit(Project1EID)
        self.humidity_request_time.setGeometry(QtCore.QRect(410, 260, 113, 31))
        self.humidity_request_time.setObjectName("humidity_request_time")
        self.temperature_timeout_label = QtWidgets.QLabel(Project1EID)
        self.temperature_timeout_label.setGeometry(QtCore.QRect(430, 100, 91, 20))
        self.temperature_timeout_label.setObjectName("temperature_timeout_label")
        self.humidity_timeout_label = QtWidgets.QLabel(Project1EID)
        self.humidity_timeout_label.setGeometry(QtCore.QRect(430, 240, 91, 20))
        self.humidity_timeout_label.setObjectName("humidity_timeout_label")
        
        self.retranslateUi(Project1EID)
        #self.temperature_Button.clicked.connect(self.temperature_text.clear)
        #self.humidity_Button.clicked.connect(self.humidity_text.clear)
        self.temperature_Button.released.connect(self.temperatureReadingPrint)
        self.humidity_Button.released.connect(self.humidityReadingPrint)
        QtCore.QMetaObject.connectSlotsByName(Project1EID)

        

        


if __name__ == "__main__":
    import sys
	
    # Parse command line parameters.
    sensor_args = { '11': Adafruit_DHT.DHT11,
                    '22': Adafruit_DHT.DHT22,
                    '2302': Adafruit_DHT.AM2302 }
    if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
       sensor = sensor_args[sys.argv[1]]
       pin = sys.argv[2]
    else:
       print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
       print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
       sys.exit(1)
	
    app = QtWidgets.QApplication(sys.argv)
    Project1EID = QtWidgets.QDialog()
    ui = Ui_Project1EID()
    ui.setupUi(Project1EID)
    Project1EID.show()
    sys.exit(app.exec_())


 
