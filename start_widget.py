from design import start_design
from PyQt5 import QtWidgets

class TestApp(QtWidgets.QMainWindow, start_design.Ui_MainWindow):
    def __init__(self, db):
        super().__init__()
        self.setupUi(self)
        subjects = db.get_subjects()
        for subject in subjects:
            self.subjectComboBox.addItem(subject)
        self.startButton.clicked.connect(self.choose_theme)
        self.startButton.setEnabled(False)
        self.subjectComboBox.currentIndexChanged.connect(self.activate_button)
    
    def activate_button(self):
        self.startButton.setEnabled(True)

    def choose_theme(self):
        print(self.subjectComboBox.currentIndex())
        is_teacher = self.roleTeacher.isChecked()
        subject_id = self.subjectComboBox.currentIndex()
        self.launch_theme_chooser(is_teacher, subject_id)

    def launch_theme_chooser(self, is_teacher, subject_id):
        pass

