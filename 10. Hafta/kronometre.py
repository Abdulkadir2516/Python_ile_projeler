from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kronometre")
        self.setGeometry(100, 100, 300, 200)

        self.time_label = QLabel(self)
        self.time_label.setGeometry(100, 50, 100, 50)

        self.start_button = QPushButton("Başlat", self)
        self.start_button.setGeometry(100, 100, 100, 50)
        self.start_button.clicked.connect(self.start_timer)

        self.stop_button = QPushButton("Durdur", self)
        self.stop_button.setGeometry(100, 150, 100, 50)
        self.stop_button.clicked.connect(self.stop_timer)
        self.stop_button.setEnabled(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        self.time_counter = 0

    def start_timer(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.timer.start(10)  # Her 1000 milisaniyede bir tetikle (1 saniye)

    def stop_timer(self):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.timer.stop()
        self.time_counter = 0
        self.update_time()

    def update_time(self):
        self.time_counter += 1
        minutes = self.time_counter // 60
        seconds = self.time_counter % 60
        mill = self.time_counter
        time_text = "{:02d}:{:02d}:{:02d}".format(minutes, seconds,mill)
        self.time_label.setText(time_text)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
