from PyQt5 import QtWidgets
from design import themes_design

class ThemesChoose(QtWidgets.QWidget, themes_design.Ui_Form):
    def __init__(self, is_teacher=False, subject_id=0, db=None):
        super().__init__()
        self.setupUi(self)
        self.is_teacher = is_teacher
        self.themes = []
        self.subject_id = subject_id

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
        self.showTestForm(self.is_teacher, themes, self.subject_id)
    
    def showTestForm(self, is_teacher, themes, subject_id):
        pass
