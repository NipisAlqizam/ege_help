import sys
from PyQt5 import QtWidgets
from design import start_design, themes_design, test_design, res_design
import db
"""
За основу взяты задания с сайта РешуЕГЭ
"""


class TestApp(QtWidgets.QMainWindow, start_design.Ui_MainWindow):
    def __init__(self):
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
        self.theme_window = ThemesChoose(is_teacher, self.subjectComboBox.currentIndex())
        self.theme_window.show()
        self.hide()


class ThemesChoose(QtWidgets.QWidget, themes_design.Ui_Form):
    def __init__(self, is_teacher=False, subject_id=0):
        super().__init__()
        self.setupUi(self)
        self.is_teacher = is_teacher
        self.themes = []

        self.theme_names = db.get_themes(subject_id)
        for theme in self.theme_names:
            edit = QtWidgets.QLineEdit(self)
            edit.setText('0')
            self.themes.append(edit)
            self.formLayout.addRow(self.tr(theme), edit)
        self.startButton.clicked.connect(self.startTest)

    def startTest(self):
        themes = []
        for field in self.themes:
            cnt = field.text()
            cnt = int(cnt)
            themes.append(cnt)
        self.test = TestForm(self.is_teacher, themes)
        self.test.show()
        self.hide()


class TestForm(QtWidgets.QWidget, test_design.Ui_Form):
    def __init__(self, is_teacher:bool=False, themes:list=[]):
        super().__init__()
        self.setupUi(self)
        self.is_teacher = is_teacher

        self.scrollArea.setWidgetResizable(True)
        self.vbox = QtWidgets.QVBoxLayout()
        self.tasks = []
        import generators,random
        for i,cnt in enumerate(themes):
            for j in range(cnt):
                task = QtWidgets.QGroupBox(f'Задание {j+1}')
                task.setMinimumWidth(self.scrollArea.width())

                vl = QtWidgets.QVBoxLayout()

                t = generators.generate_inf[random.randint(0,1)]()

                text = QtWidgets.QTextBrowser()
                text.setMinimumHeight(200)
                text.setText(t[0])
                vl.addWidget(text)

                ans = QtWidgets.QLineEdit()
                ans.setPlaceholderText('Ответ')
                if self.is_teacher:
                    ans.setText(str(t[1]))
                vl.addWidget(ans)

                task.setLayout(vl)

                self.tasks.append(task)
                self.vbox.addWidget(task)
        self.Tasks.setLayout(self.vbox)

        self.finishButton.clicked.connect(self.getResults)

    def getResults(self):
        self.res = ResForm()
        self.res.show()
        self.hide()


class ResForm(QtWidgets.QWidget, res_design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = TestApp()
window.show()
app.exec_()
