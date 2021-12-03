import sys
import pandas as pd
import os
import time
from datetime import date
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from DOC_GUI import Ui_DOC
from TableView import pandasModel


def doc_merge(path):
    '''
    :input: based on the path, programs will auto detect all tcf files under the folder
    :return: a data frame combined all doc records
    '''
    DOC = []
    mydata = []
    file_list = os.listdir(path)
    s = len(file_list)
    #for name in file_list:
    for i in range(0, s):
        name = file_list[i]
        FD = pd.DataFrame(columns=['File_name', 'ID', 'TOC', 'IC', 'TC', 'TN'])
        #file_list = os.listdir(folder)
        if name.split('.')[1] == 'tcf':

            md = open(path + '\\' + name)

            # print("now deal with the file of {0} \n".format(name))

            for line in md:
                mydata.append(line)

            for line in mydata:

                a = line.replace("\n", "abc")

                b = a.split('|')

                # print(b)
                if a == 'abc':

                    pass

                else:
                    FD = FD.append(
                        {'File_name': name.split('.')[0],
                         'ID': b[0],
                         'TOC': format(float(b[1]), '.4f'),
                         'IC': format(float(b[2]), '.4f'),
                         'TC': format(float(b[3]), '.4f'),
                         'TN': format(float(b[4]), '.4f')},
                        ignore_index=True)

            else:
                pass
            DOC.append(FD)
    DOC_DATA = pd.concat(DOC, axis=0)
    return DOC_DATA


class MainWindow(QMainWindow, Ui_DOC):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.message_box = QMessageBox()
        # Events for 'select buttons'
        self.pushButton.clicked.connect(self.goSearch)
        # register events for radioButtons 2 -- set '.csv' file is the default
        self.radioButton_2.setChecked(True)
        # run buttons events-- for save file
        self.pushButton_2.clicked.connect(self.goSave)
        # self.radioButton.toggled.connect(self.goSave)

    def goSearch(self):
        global md
        global folder
        folder = QFileDialog.getExistingDirectory(None, 'Select your folder:')
        self.textEdit.setText(folder)
        file_list = os.listdir(folder)
        md = doc_merge(folder)
        self.model = pandasModel(md)

        for j in range(0, len(file_list)):
            if j < (len(file_list)):
                count = (j / (len(file_list)-1)) * 100
                #time.sleep(0.1)
                self.progressBar.setValue(count)

        self.tableView.setModel(self.model)
        self.tableView.show()
        # progress bar
    def goSave(self):
        file_name = self.textEdit_2.text()
        # if user forget input file name then
        # system time will replace the empty name
        if file_name:
            pass
        else:
            today = date.today()
            file_name = str(today.strftime("%d/%m/%Y")) + "_DOC"
        # check the output file format
        if self.radioButton.isChecked():
            file_format = 'txt'
        elif self.radioButton_2.isChecked():
            file_format = 'csv'
        else:
            file_format = 'xlsx'

        try:
            fullPathName = folder + "\\" + file_name + "." + file_format
            if file_format in ['txt', 'csv']:
                md.to_csv(fullPathName, index=False)
            else:
                md.to_excel(fullPathName)
            self.message_box.setWindowTitle("Finished!")
            self.message_box.setText("""You file is successfully saved""")
            self.message_box.exec()
        except:
            self.message_box.setWindowTitle("OPS!")
            self.message_box.setText(f"something wrong {sys.exc_info()[0]} occurred!")
            self.message_box.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    ret = app.exec_()
    sys.exit(ret)
