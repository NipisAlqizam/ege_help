from PyQt5 import QtWidgets
from design import test_design

class TestForm(QtWidgets.QWidget, test_design.Ui_Form):
    def __init__(self, is_teacher:bool=False, themes:list=[], subject_id=1, db=None):
        super().__init__()
        self.setupUi(self)
        self.is_teacher = is_teacher

        self.scrollArea.setWidgetResizable(True)
        self.vbox = QtWidgets.QVBoxLayout()
        self.tasks = []
        import generators
        for i,cnt in enumerate(themes):
            for j in range(cnt):
                task = QtWidgets.QGroupBox(f'Задание {j+1}')
                task.setMinimumWidth(self.scrollArea.width())

                vl = QtWidgets.QVBoxLayout()

                t = generators.generate(subject_id,i)

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
            pass
