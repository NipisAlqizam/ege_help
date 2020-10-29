from fpdf import FPDF

class TestPDFGenerator(FPDF):
    def __init__(self, test, test_name='Задания'):
        super().__init__()
        self.add_font('DejaVu', '', 'font/DejaVuSerif.ttf', uni=True)
        self.add_font('DejaVu', 'B', 'font/DejaVuSansCondensed-Bold.ttf', uni=True)
        self.tasks = [i[0] for i in test]
        self.ans = [i[1] for i in test]
        self.header_text = test_name
    
    def header(self):
        self.set_font('DejaVu', 'B', 16)
        #self.cell((self.w-2*self.l_margin-self.header_width)//2)
        #self.cell(self.header_width,10,self.header_text,1,0,'C')
        self.cell(0,0,self.header_text,0,0,'C')
        self.ln(20)
    
    def write_task(self, text, number):
        self.set_font('DejaVu', 'B', 14)
        self.write(5, f"{number}. ")
        self.set_font('DejaVu', '', 14)
        self.write(5, text.strip())
        self.write(5, '\n')
        self.write(5, 'Ответ: _____________')
        self.ln(15)
    
    def write_tasks(self):
        self.header_width = 35
        self.add_page()
        for i,task in enumerate(self.tasks):
            self.write_task(task,i+1)
    
    def write_answers_table(self, ans, offset):
        self.set_font('DejaVu', '', 14)
        real_page_width = self.w-2*self.l_margin
        col_width = real_page_width / len(ans)
        row_height = self.font_size+1
        for i in range(1+offset,offset+len(ans)+1):
            self.cell(col_width, row_height, f"{i}", 1, 0, 'C')
        self.ln(row_height)
        for i in ans:
            self.cell(col_width, row_height, f"{i}", 1, 0, 'C')
    
    def write_answers(self):
        self.header_width = 30
        self.header_text = 'Ответы'
        self.add_page()
        if len(self.ans) <= 7:
            self.write_answers_table(self.ans,0)
            self.ln(15)
            return
        for i in range(7,len(self.ans)+1,7):
            self.write_answers_table(self.ans[i-7:i], i-7)
            self.ln(15)
        if len(self.ans)%7 != 0:
            self.write_answers_table(self.ans[len(self.ans)//7*7:], len(self.ans)//7*7)
            self.ln(15)


if __name__ == "__main__":
    pass
