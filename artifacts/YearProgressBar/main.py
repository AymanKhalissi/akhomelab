import sys
import datetime
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QLabel, QMenuBar, QMessageBox, QGridLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont, QAction

class YearProgressApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Year & Month Progress")
        self.setFixedSize(600, 500)
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
        self.quote_label.setFont(QFont("Arial", 15))
        self.quote_label.setAlignment(Qt.AlignCenter)
        self.quote_label.setWordWrap(True)
        
        self.time_label = QLabel(self)
        self.time_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.time_label.setAlignment(Qt.AlignCenter)
        
        # Year Progress Bar
        self.year_progress_bar = QProgressBar(self)
        self.year_progress_bar.setStyleSheet("QProgressBar {border: 2px solid white; border-radius: 10px; text-align: center; height: 20px;} QProgressBar::chunk {background-color: #4CAF50; width: 10px;}")
        self.year_percentage_label = QLabel(self)
        self.year_percentage_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.year_percentage_label.setAlignment(Qt.AlignCenter)
        
        # Month Progress Bar
        self.month_progress_bar = QProgressBar(self)
        self.month_progress_bar.setStyleSheet("QProgressBar {border: 2px solid white; border-radius: 10px; text-align: center; height: 20px;} QProgressBar::chunk {background-color: #FF9800; width: 10px;}")
        self.month_percentage_label = QLabel(self)
        self.month_percentage_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.month_percentage_label.setAlignment(Qt.AlignCenter)
        
        # Month Grid
        self.month_grid = QGridLayout()
        self.month_labels = []
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        for i, month in enumerate(months):
            label = QLabel(month)
            label.setFont(QFont("Arial", 12))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: 1px solid white; padding: 5px;")
            self.month_grid.addWidget(label, i // 3, i % 3)
            self.month_labels.append(label)
        
        layout.setMenuBar(self.menu_bar)
        layout.addWidget(self.day_label)
        layout.addWidget(self.date_label)
        layout.addWidget(self.quote_label)
        layout.addWidget(self.time_label)
        layout.addWidget(self.year_progress_bar)
        layout.addWidget(self.year_percentage_label)
        layout.addWidget(self.month_progress_bar)
        layout.addWidget(self.month_percentage_label)
        layout.addLayout(self.month_grid)
        
        self.setLayout(layout)
        
        self.update_progress()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)

    def update_progress(self):
        now = datetime.datetime.now()
        
        # Year Progress
        start_of_year = datetime.datetime(now.year, 1, 1)
        end_of_year = datetime.datetime(now.year + 1, 1, 1)
        total_seconds_year = (end_of_year - start_of_year).total_seconds()
        elapsed_seconds_year = (now - start_of_year).total_seconds()
        year_percentage = (elapsed_seconds_year / total_seconds_year) * 100
        
        # Month Progress
        start_of_month = datetime.datetime(now.year, now.month, 1)
        next_month = now.month % 12 + 1
        year_offset = now.year + (1 if next_month == 1 else 0)
        end_of_month = datetime.datetime(year_offset, next_month, 1)
        total_seconds_month = (end_of_month - start_of_month).total_seconds()
        elapsed_seconds_month = (now - start_of_month).total_seconds()
        month_percentage = (elapsed_seconds_month / total_seconds_month) * 100
        
        self.day_label.setText(now.strftime("%A"))
        self.date_label.setText(now.strftime("%B %d, %Y"))
        self.time_label.setText(now.strftime("%I:%M %p"))
        
        self.year_progress_bar.setValue(int(year_percentage))
        self.year_percentage_label.setText(f"{year_percentage:.2f}% of the year completed")
        
        self.month_progress_bar.setValue(int(month_percentage))
        self.month_percentage_label.setText(f"{month_percentage:.2f}% of the month completed")
        
        # Update month grid
        for i, label in enumerate(self.month_labels):
            if i < now.month - 1:
                label.setStyleSheet("border: 1px solid white; padding: 5px; text-decoration: line-through; color: gray;")
            else:
                label.setStyleSheet("border: 1px solid white; padding: 5px;")

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
