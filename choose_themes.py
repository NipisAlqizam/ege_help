from PyQt5 import QtWidgets
from design import themes_design

class ThemesChoose(QtWidgets.QWidget, themes_design.Ui_Form):
    def __init__(self, is_teacher, subject_name, db):
        super().__init__()
        self.setupUi(self)
        self.is_teacher = is_teacher
        self.themes = []
        self.subject_name = subject_name

        self.theme_names= db.get_themes(subject_name)
        for theme in self.theme_names:
            edit = QtWidgets.QLineEdit(self)
            edit.setText('0')
            self.themes.append((theme,edit))
            self.formLayout.addRow(self.tr(theme), edit)
        self.startButton.clicked.connect(self.startTest)

    def startTest(self):
        themes = {}
        for name,field in self.themes:
            cnt = field.text()
            try:
                cnt = int(cnt)
            except ValueError:
                return
            themes[name] = cnt
        self.showTestForm(self.is_teacher, themes, self.subject_name)
    
    def showTestForm(self, is_teacher, themes, subject_name):
        pass
