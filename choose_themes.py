from PyQt5 import QtWidgets
from design import themes_design

class ThemesChoose(QtWidgets.QWidget, themes_design.Ui_Form):
    def __init__(self, is_teacher=False, subject_id=0, db=None):
        super().__init__()
        self.setupUi(self)
        self.is_teacher = is_teacher
        print(subject_id)
        self.themes = []
        self.subject_id = subject_id

        self.theme_names_and_ids = db.get_themes(subject_id)
        for id,theme in self.theme_names_and_ids:
            edit = QtWidgets.QLineEdit(self)
            edit.setText('0')
            self.themes.append((id,edit))
            self.formLayout.addRow(self.tr(theme), edit)
        self.startButton.clicked.connect(self.startTest)

    def startTest(self):
        themes = {}
        for id,field in self.themes:
            cnt = field.text()
            cnt = int(cnt)
            themes[id] = cnt
        self.showTestForm(self.is_teacher, themes, self.subject_id)
    
    def showTestForm(self, is_teacher, themes, subject_id):
        pass
