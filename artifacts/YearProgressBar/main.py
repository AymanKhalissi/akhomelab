import sys
import datetime
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QLabel, QMenuBar, QMessageBox
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont, QAction

class YearProgressApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Year Progress")
        self.setFixedSize(600, 350)  # Fixed size
        self.setStyleSheet("background-color: #1a1f2b; color: white;")
        
        layout = QVBoxLayout()
        
        self.menu_bar = QMenuBar(self)
        self.setup_menu = self.menu_bar.addMenu("Setup")
        
        self.startup_action = QAction("Start app at launch", self, checkable=True)
        self.startup_action.setChecked(self.check_startup())
        self.startup_action.triggered.connect(self.toggle_startup)
        self.setup_menu.addAction(self.startup_action)
        
        self.day_label = QLabel(self)
        self.day_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.day_label.setAlignment(Qt.AlignCenter)
        
        self.date_label = QLabel(self)
        self.date_label.setFont(QFont("Arial", 14))
        self.date_label.setAlignment(Qt.AlignCenter)
        
        self.quote_label = QLabel("Because hardships strengthen resolve, the strong-minded will not be lured by worldly affairs. Today I step on grass; later I shall step on mountains and rivers!", self)
        self.quote_label.setFont(QFont("Arial", 10))
        self.quote_label.setAlignment(Qt.AlignCenter)
        self.quote_label.setWordWrap(True)
        
        self.time_label = QLabel(self)
        self.time_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setStyleSheet("QProgressBar {border: 2px solid white; border-radius: 10px; text-align: center; height: 20px;} QProgressBar::chunk {background-color: #4CAF50; width: 10px;}")
        
        self.percentage_label = QLabel(self)
        self.percentage_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.percentage_label.setAlignment(Qt.AlignCenter)
        
        layout.setMenuBar(self.menu_bar)
        layout.addWidget(self.day_label)
        layout.addWidget(self.date_label)
        layout.addWidget(self.quote_label)
        layout.addWidget(self.time_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.percentage_label)
        
        self.setLayout(layout)
        
        self.update_progress()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)

    def update_progress(self):
        now = datetime.datetime.now()
        start_of_year = datetime.datetime(now.year, 1, 1)
        end_of_year = datetime.datetime(now.year + 1, 1, 1)
        total_seconds = (end_of_year - start_of_year).total_seconds()
        elapsed_seconds = (now - start_of_year).total_seconds()
        percentage = (elapsed_seconds / total_seconds) * 100
        
        self.day_label.setText(now.strftime("%A"))
        self.date_label.setText(now.strftime("%B %d, %Y"))
        self.time_label.setText(now.strftime("%I:%M %p"))
        self.progress_bar.setValue(int(percentage))
        self.percentage_label.setText(f"{percentage:.2f}% of the year completed")

    def check_startup(self):
        startup_path = os.path.expanduser("~/.config/autostart/year_progress.desktop")
        return os.path.exists(startup_path)

    def toggle_startup(self, checked):
        startup_path = os.path.expanduser("~/.config/autostart/year_progress.desktop")
        if checked:
            with open(startup_path, "w") as f:
                f.write("[Desktop Entry]\nType=Application\nExec=python3 /path/to/this_script.py\nHidden=false\nNoDisplay=false\nX-GNOME-Autostart-enabled=true\nName[en_US]=Year Progress\n")
        else:
            if os.path.exists(startup_path):
                os.remove(startup_path)
        QMessageBox.information(self, "Setup", "Startup setting updated.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YearProgressApp()
    window.show()
    sys.exit(app.exec())
