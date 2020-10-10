import sys
from PyQt5 import QtWidgets
from design import res_design
from start_widget import TestApp
from choose_themes import ThemesChoose
from test_form import TestForm
import db
"""
За основу взяты задания с сайта РешуЕГЭ
"""

def launch_theme_chooser(self, is_teacher, subject_id):
        self.theme_window = ThemesChoose(is_teacher, subject_id, db)
        self.theme_window.show()
        self.hide()

def launch_test(self, is_teacher, themes, subject_id):
    self.test = TestForm(is_teacher, themes, subject_id, db)
    self.test.show()
    self.hide()

def getResults(self):
    self.res = ResForm()
    self.res.show()
    self.hide()

TestApp.launch_theme_chooser = launch_theme_chooser
ThemesChoose.showTestForm = launch_test
TestForm.getResults = getResults


class ResForm(QtWidgets.QWidget, res_design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = TestApp(db)
window.show()
app.exec_()
