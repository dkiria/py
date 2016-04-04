#!/usr/bin/python
# -*- coding: utf-8 -*-

#-------------------------AUTHORS--------------------------

#-Dimitris Kyriakatis <<dimitriskiriakatis@outlook.com.gr>>

#----------------------------------------------------------

import Tkinter, Tkconstants, tkFileDialog
import threading
import os
import commands

import re


class MedLabApp(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.label_text = 'Welcome!'
        self.file_text = 'file'
        self.result = 'Results'
        self.result_pdb = ''
        self.error = "Here will be displayed errors"
        self.file_opt = options = {}
        self.file_opt1 = options1 = {}
        options1['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['defaultextension'] = '.pdb'
        options['filetypes'] = [('pdb files', '.pdb')]
        options['initialdir'] = '~/'
        self.initialize()


    def initialize(self):
        self.minsize(width=400, height=400)
        self.grid()
        self.label = Tkinter.Label(self, text=self.label_text)
        self.label.grid(column=0,row=0)
        self.button1 = Tkinter.Button(text="Run first program", command=self.run_giba_pre)
        self.button1.grid(column=0, row=1)
        self.button2 = Tkinter.Button(text="Run second program", command=self.run_gomir_pre)
        self.button2.grid(column=0, row=2)
        self.button3 = Tkinter.Button(text="Run third program", command=self.run_taggo_pre)
        self.button3.grid(column=0, row=3)
        self.button4 = Tkinter.Button(text="Run other program", command=self.space_convert)
        self.button4.grid(column=0, row=6)
        self.filed = Tkinter.Button(self, text=' open file', command=self.askopenfilename)
        self.filed.grid(column=0, row=4)
        self.label1 = Tkinter.Label(self, text=self.file_text)
        self.label1.grid(column=0,row=5)
        self.label2 = Tkinter.Label(self, text=self.error, fg="red")
        self.label2.grid(column=0,row=8)
        self.label3 = Tkinter.Label(self, text=self.result)
        self.label3.grid(column=0,row=7)

    def askopenfilename(self):
        self.clear_error()
        self.filename = tkFileDialog.askopenfilename(**self.file_opt)
        print self.filename
        self.label1.config(text=self.filename)

    def space_convert(self):
        self.clear_error()
        self.result =  commands.getstatusoutput('run_command '+str(self.filename))
        self.label3.config(text=self.result[1])

    def run_giba_pre(self):
        self.clear_error()
        ltrt = threading.Thread(target=self.run_giba)
        ltrt.start()

    def run_gomir_pre(self):
        self.clear_error()
        ltrt = threading.Thread(target=self.run_gomir)
        ltrt.start()

    def run_taggo_pre(self):
        self.clear_error()
        ltrt = threading.Thread(target=self.run_taggo)
        ltrt.start()

    def run_giba(self):
        self.clear_error()
        self.error =  commands.getstatusoutput('run_command')
        self.label2.config(text=self.error[1])

    def run_gomir(self):
        self.clear_error()
        self.error =  commands.getstatusoutput('run_command')
        self.label2.config(text=self.error[1])

    def run_taggo(self):
        self.clear_error()
        self.error =  commands.getstatusoutput('run_command')
        self.label2.config(text=self.error[1])

    def clear_error(self):
        self.error = 'No Errors'
        self.label2.config(text=self.error)


if __name__ == "__main__":
    app = MedLabApp(None)
    app.title('platform by Dimitris Kyriakatis ')
    app.mainloop()
