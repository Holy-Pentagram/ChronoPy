import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QIcon, QGuiApplication

class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.UI()
    def UI(self):
        #windows UI
        self.setWindowIcon(QIcon('stopwatch.png'))
        self.setWindowTitle("Stopwatch")
        self.setGeometry(150, 150, 1000, 600)
        #buttons and label UI
        vbox = QVBoxLayout() # creating a vertical layout variable
        #arange widgets
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        self.start_button.setObjectName("startButton")
        self.stop_button.setObjectName("stopButton")
        self.reset_button.setObjectName("resetButton")
        self.setStyleSheet("""
            QPushButton#startButton {
                        background-color: #f1c40f; 
                        color: black;
                        border-radius: 8px;
                        padding: 10px 20px;
                        font-weight: bold;
                        }
            QPushButton#stopButton {
                        background-color: #f39c12;  
                        color: black;
                        border-radius: 8px;
                        padding: 10px 20px;
                        font-weight: bold;
                        }
            QPushButton#resetButton {
                        background-color: #27ae60;  
                        color: white;
                        border-radius: 8px;
                        padding: 10px 20px;
                        font-weight: bold;
                        }
            QPushButton#startButton:hover,
            QPushButton#stopButton:hover,
            QPushButton#resetButton:hover {
                        background-color: #bdc3c7; 
                        color: #7f8c8d; 
                        }
            QPushButton:disabled {
                        background-color: #bdc3c7;
                        color: #7f8c8d;
                        cursor: not-allowed;
                        }
            QLabel {
                        color: #a3c9f1;
                        font-size: 48px;
                        font-weight: bold;
                        qproperty-alignment: AlignCenter;
                        background: rgba(163, 201, 241, 0.3);
                        border-radius: 12px;
                        padding: 20px;
                        border: 2px solid rgba(163, 201, 241, 0.6);
                    }
                        """)
        #trigerrinf the correct function for every button
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)
        self.start_button.setDisabled(True)  
        self.stop_button.setEnabled(True)  
        self.start_button.setText("Start") 
    def stop(self):
        self.timer.stop()
        self.stop_button.setDisabled(True)   
        self.start_button.setEnabled(True)   
        self.start_button.setText("Resume")  

    def reset(self):
        self.timer.stop()
        self.time = QTime(0 , 0 , 0 , 0)
        self.time_label.setText(self.format_time(self.time))
        self.start_button.setEnabled(True)
        self.start_button.setText("Start")
        self.stop_button.setEnabled(True)

    def format_time(self, time):
        hours = self.time.hour()
        minutes = self.time.minute()
        seconds = self.time.second()
        milliseconds = self.time.msec()
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time)) # hmmmm, I never would have thought that someone would be reading my code one day lol
                                                            #so for you who are reading the comment, I wish you a good day
if __name__ == "__main__":                                    
    app = QApplication(sys.argv)
    stopwatch = stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
# I am adding comments just to make it to 120 lines hehehehehe