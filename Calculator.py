import tkinter as tk

class App():
    def __init__(self,root):
        self.frame = tk.Frame(root)

        self.result = ''
        self.done = False

        self.display = tk.Entry(root,font=("Arial",20))
        self.displayBottom = tk.Entry(root,font=("Arial",14))

        self.btnDelete = tk.Button(root,text="C",font=("Arial",30),command=self.delete)
        self.btnDelLast = tk.Button(root,text="<",font=("Arial",30),command=self.deleteLast)

        self.btnDiv = tk.Button(root,text="/",font=("Arial",30),command=lambda: self.button_operator('/'))

        self.btn9 = tk.Button(root,text="9",font=("Arial",30),command=lambda: self.button_click(9))
        self.btn8 = tk.Button(root,text="8",font=("Arial",30),command=lambda: self.button_click(8))
        self.btn7 = tk.Button(root,text="7",font=("Arial",30),command=lambda: self.button_click(7))
        self.btnMulti = tk.Button(root,text="*",font=("Arial",30),command=lambda: self.button_operator('*'))

        self.btn6 = tk.Button(root,text="6",font=("Arial",30),command=lambda: self.button_click(6))
        self.btn5 = tk.Button(root,text="5",font=("Arial",30),command=lambda: self.button_click(5))
        self.btn4 = tk.Button(root,text="4",font=("Arial",30),command=lambda: self.button_click(4))
        self.btnSubt = tk.Button(root,text="-",font=("Arial",30),command=lambda: self.button_operator('-'))

        self.btn3 = tk.Button(root,text="3",font=("Arial",30),command=lambda: self.button_click(3))
        self.btn2 = tk.Button(root,text="2",font=("Arial",30),command=lambda: self.button_click(2))
        self.btn1 = tk.Button(root,text="1",font=("Arial",30),command=lambda: self.button_click(1))
        self.btnAdd = tk.Button(root,text="+",font=("Arial",30),command=lambda: self.button_operator('+'))

        self.btnNeg = tk.Button(root,text="+/-",font=("Arial",30),command=lambda: self.button_click('neg'))
        self.btn0 = tk.Button(root,text="0",font=("Arial",30),command=lambda: self.button_click(0))
        self.btnDec = tk.Button(root,text=".",font=("Arial",30),command=lambda: self.button_click('.'))
        self.btnRes = tk.Button(root,text="=",font=("Arial",30),command=lambda: self.button_operator('='))

        self.display.grid(row=1,column=1,columnspan=4,ipadx=20,ipady=10)
        self.displayBottom.grid(row=2,column=1,columnspan=4,ipadx=60,ipady=16)

        self.btnDelete.grid(row=5,column=3,ipadx=12)
        self.btnDelLast.grid(row=5,column=4,ipadx=12)

        self.btnDiv.grid(row=6,column=4,ipadx=19)

        self.btn7.grid(row=7,column=1,ipadx=15)
        self.btn8.grid(row=7,column=2,ipadx=15)
        self.btn9.grid(row=7,column=3,ipadx=15)
        self.btnMulti.grid(row=7,column=4,ipadx=17)

        self.btn4.grid(row=8,column=1,ipadx=15)
        self.btn5.grid(row=8,column=2,ipadx=15)
        self.btn6.grid(row=8,column=3,ipadx=15)
        self.btnSubt.grid(row=8,column=4,ipadx=19)

        self.btn1.grid(row=9,column=1,ipadx=15)
        self.btn2.grid(row=9,column=2,ipadx=15)
        self.btn3.grid(row=9,column=3,ipadx=15)
        self.btnAdd.grid(row=9,column=4,ipadx=14)

        self.btnNeg.grid(row=10,column=1,ipadx=2)
        self.btn0.grid(row=10,column=2,ipadx=15)
        self.btnDec.grid(row=10,column=3,ipadx=21)
        self.btnRes.grid(row=10,column=4,ipadx=14)

        self.frame.grid()

    def button_click(self,number):        
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(current) + str(number))

    def deleteLast(self):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current[:-1])
    def delete(self):
        self.display.delete(0, tk.END)
        self.displayBottom.delete(0, tk.END)

    def button_operator(self,opr):
        if self.done:
            print(self.done)
            self.delete()
            self.done = False
            num = self.display.get()
            current = self.displayBottom.get()
            self.displayBottom.delete(0, tk.END)     
            if current:
                self.displayBottom.insert(0, str(current) + num + opr)
            else:
                self.displayBottom.insert(0, num + opr)
            self.display.delete(0, tk.END)    

            if opr == '=':
                self.done = True
                result = self.displayBottom.get()
                final = result[:-1]
                self.result = eval(final)                
                toDisplay = str(result)+str(self.result)
                result = self.displayBottom.get()
                self.displayBottom.delete(0, tk.END)
                self.displayBottom.insert(0, toDisplay)   
            else:
                self.done = False     
        else:
            print(self.done)
            num = self.display.get()
            current = self.displayBottom.get()
            self.displayBottom.delete(0, tk.END)     
            if current:
                self.displayBottom.insert(0, str(current) + num + opr)
            else:
                self.displayBottom.insert(0, num + opr)
            self.display.delete(0, tk.END)    

            if opr == '=':
                result = self.displayBottom.get()
                final = result[:-1]
                self.result = eval(final)
                self.done = True
                toDisplay = str(result)+str(self.result)
                result = self.displayBottom.get()
                self.displayBottom.delete(0, tk.END)
                self.displayBottom.insert(0, toDisplay)                    

    # def button_add(self):
    #     self.first = self.display.get()
    #     current = self.displayBottom.get()
    #     self.displayBottom.delete(0, tk.END)
    #     if current:
    #         self.displayBottom.insert(0, str(current) + self.first + '+')
    #     else:
    #         self.displayBottom.insert(0, self.first + '+')
    #     self.display.delete(0, tk.END)
    #     a = self.displayBottom.get()
    #     last = a[-1]
    #     matches = ['+','-','*','/']
    #     if set(matches) & set(last):
    #         newCurrent = self.displayBottom.get()
    #         self.displayBottom.delete(0, tk.END)
    #         self.displayBottom.insert(0, newCurrent[:-1] + '+')


root = tk.Tk()
main = App(root)
root.mainloop()
