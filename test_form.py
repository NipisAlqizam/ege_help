from PyQt5 import QtWidgets
from design import test_design

class TestForm(QtWidgets.QWidget, test_design.Ui_Form):
    def __init__(self, is_teacher:bool=False, themes:dict={}, subject_id=1, db=None):
        super().__init__()
        self.setupUi(self)
        self.is_teacher = is_teacher

        self.scrollArea.setWidgetResizable(True)
        self.vbox = QtWidgets.QVBoxLayout()
        self.tasks = []
        self.answers = []
        self.ans_fields = []
        import generate
        for i,cnt in themes.items():
            for j in range(cnt):
                task = QtWidgets.QGroupBox(f'Задание {j+1}')
                task.setMinimumWidth(self.scrollArea.width())

                vl = QtWidgets.QVBoxLayout()

                t = generate.generate(subject_id,i-1)

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
                self.answers.append(t[1])
                self.ans_fields.append(ans)
                self.vbox.addWidget(task)
        self.Tasks.setLayout(self.vbox)

        self.finishButton.clicked.connect(self.getResults)

    def checkTest(self):
            correct_cnt = 0
            for ans, correct_ans in zip(self.ans_fields, self.answers):
                if ans.text() == str(correct_ans):
                    correct_cnt += 1
            print(correct_cnt)
            return correct_cnt

    def getResults(self):
        pass
