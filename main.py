import sys
from PyQt5 import QtWidgets
from design import start_design, themes_design, test_design, res_design


class TestApp(QtWidgets.QMainWindow, start_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.subjectComboBox.addItem('Информатика')
        self.subjectComboBox.addItem('Химия')
        self.startButton.clicked.connect(self.choose_theme)

    def choose_theme(self):
        is_teacher = self.roleTeacher.isChecked()
        self.theme_window = ThemesChoose(is_teacher)
        self.theme_window.show()
        self.hide()


class ThemesChoose(QtWidgets.QWidget, themes_design.Ui_Form):
    def __init__(self, is_teacher=False):
        super().__init__()
        self.setupUi(self)
        self.is_teacher = is_teacher
        self.themes = []

        for i in range(5): 
            edit = QtWidgets.QLineEdit(self)
            edit.setText('0')
            self.themes.append(edit)
            self.formLayout.addRow(self.tr(f'Тема {i+1}'), edit)
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
        for i in range(sum(themes)):
            task = QtWidgets.QGroupBox(f'Задание {i+1}')
            task.setMinimumWidth(self.scrollArea.width())

            vl = QtWidgets.QVBoxLayout()

            text = QtWidgets.QTextBrowser()
            text.setMinimumHeight(200)
            text.setText('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris varius nisi dapibus dolor malesuada posuere. In consectetur quam id diam sodales venenatis. Aenean ultrices eget nulla quis pharetra. Donec sit amet metus in diam imperdiet convallis. Proin consequat ex sed neque pulvinar volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec at odio eget nibh aliquet sodales vitae quis augue. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur tempor est ac dolor facilisis luctus ut id felis. Nullam nec egestas sapien, eget euismod nulla.')
            vl.addWidget(text)

            ans = QtWidgets.QLineEdit()
            ans.setPlaceholderText('Ответ')
            if self.is_teacher:
                ans.setText('0')
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
