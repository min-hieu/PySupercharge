# -*- coding: utf-8 -*-
# Author: Nguyen Minh Hieu


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from supernew import superSeq


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1171, 709)
        MainWindow.setMinimumSize(QtCore.QSize(1171, 709))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # self.widgetGraph = QtWidgets.QWidget(self.centralwidget)
        # self.widgetGraph.setMinimumSize(QtCore.QSize(560, 0))
        # self.widgetGraph.setMaximumSize(QtCore.QSize(560, 541))
        # self.widgetGraph.setObjectName("widgetGraph")

        # self.horizontalLayout.addWidget(self.widgetGraph)

        #======== Add Canvas Widget ===========
        canvasGraph = FigureCanvas(Figure(figsize=(5, 3)))
        self.horizontalLayout.addWidget(canvasGraph)
        MainWindow.addToolBar(NavigationToolbar(canvasGraph, MainWindow))

        MainWindow.ax = canvasGraph.figure.subplots()
        MainWindow.ax.text(.2,.5, "HAPPY SUPERCHARGING! - Hieu")


        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.labelSeq = QtWidgets.QLabel(self.centralwidget)
        self.labelSeq.setObjectName("labelSeq")
        self.horizontalLayout_4.addWidget(self.labelSeq)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.buttonGraph = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGraph.setMaximumSize(QtCore.QSize(50, 16777215))
        self.buttonGraph.setObjectName("buttonGraph")
        self.horizontalLayout_7.addWidget(self.buttonGraph)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inputSeq = QtWidgets.QTextEdit(self.centralwidget)
        self.inputSeq.setMinimumSize(QtCore.QSize(0, 0))
        self.inputSeq.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.inputSeq.setObjectName("inputSeq")
        self.horizontalLayout_2.addWidget(self.inputSeq)
        self.buttonImportSeq = QtWidgets.QPushButton(self.centralwidget)
        self.buttonImportSeq.setText("")
        self.buttonImportSeq.setObjectName("buttonImportSeq")
        self.horizontalLayout_2.addWidget(self.buttonImportSeq)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.labelThres = QtWidgets.QLabel(self.centralwidget)
        self.labelThres.setObjectName("labelThres")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelThres)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.inputThres = QtWidgets.QSpinBox(self.centralwidget)
        self.inputThres.setMaximumSize(QtCore.QSize(16777215, 23))
        self.inputThres.setProperty("value", 4)
        self.inputThres.setObjectName("inputThres")
        self.horizontalLayout_3.addWidget(self.inputThres)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.labelTarget = QtWidgets.QLabel(self.centralwidget)
        self.labelTarget.setObjectName("labelTarget")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelTarget)
        self.inputTarget = QtWidgets.QTextEdit(self.centralwidget)
        self.inputTarget.setMaximumSize(QtCore.QSize(16777215, 23))
        self.inputTarget.setObjectName("inputTarget")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputTarget)
        self.labelStandin = QtWidgets.QLabel(self.centralwidget)
        self.labelStandin.setObjectName("labelStandin")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelStandin)
        self.inputStandin = QtWidgets.QTextEdit(self.centralwidget)
        self.inputStandin.setMaximumSize(QtCore.QSize(16777215, 23))
        self.inputStandin.setObjectName("inputStandin")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inputStandin)
        self.labelExclude = QtWidgets.QLabel(self.centralwidget)
        self.labelExclude.setObjectName("labelExclude")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelExclude)
        self.inputExclude = QtWidgets.QTextEdit(self.centralwidget)
        self.inputExclude.setMaximumSize(QtCore.QSize(16777215, 46))
        self.inputExclude.setObjectName("inputExclude")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inputExclude)
        self.labelConsurf = QtWidgets.QLabel(self.centralwidget)
        self.labelConsurf.setObjectName("labelConsurf")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelConsurf)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelConsurfStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelConsurfStatus.setObjectName("labelConsurfStatus")
        self.horizontalLayout_6.addWidget(self.labelConsurfStatus)
        self.buttonImportConsurf = QtWidgets.QPushButton(self.centralwidget)
        self.buttonImportConsurf.setObjectName("buttonImportConsurf")
        self.horizontalLayout_6.addWidget(self.buttonImportConsurf)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.formLayout_2.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.labelInclude = QtWidgets.QLabel(self.centralwidget)
        self.labelInclude.setObjectName("labelInclude")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelInclude)
        self.inputInclude = QtWidgets.QTextEdit(self.centralwidget)
        self.inputInclude.setMaximumSize(QtCore.QSize(16777215, 46))
        self.inputInclude.setObjectName("inputInclude")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inputInclude)
        self.verticalLayout.addLayout(self.formLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.checkAdd = QtWidgets.QCheckBox(self.centralwidget)
        self.checkAdd.setObjectName("checkAdd")
        self.horizontalLayout_5.addWidget(self.checkAdd)
        self.checkSeperate = QtWidgets.QCheckBox(self.centralwidget)
        self.checkSeperate.setObjectName("checkSeperate")
        self.horizontalLayout_5.addWidget(self.checkSeperate)
        self.buttonSupercharge = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSupercharge.setObjectName("buttonSupercharge")
        self.horizontalLayout_5.addWidget(self.buttonSupercharge)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setObjectName("buttonClear")
        self.horizontalLayout_8.addWidget(self.buttonClear)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout_3.addWidget(self.labelResult)
        self.outputResult = QtWidgets.QTextEdit(self.centralwidget)
        self.outputResult.setMinimumSize(QtCore.QSize(213, 345))
        self.outputResult.setObjectName("outputResult")
        self.verticalLayout_3.addWidget(self.outputResult)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem15)
        self.checkPrevious = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPrevious.setObjectName("checkPrevious")
        self.horizontalLayout_10.addWidget(self.checkPrevious)
        self.buttonExport = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExport.setMaximumSize(QtCore.QSize(50, 16777215))
        self.buttonExport.setObjectName("buttonExport")
        self.horizontalLayout_10.addWidget(self.buttonExport)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem17)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem18)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1171, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_Fasta = QtWidgets.QAction(MainWindow)
        self.actionImport_Fasta.setObjectName("actionImport_Fasta")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuHelp.addAction(self.actionImport_Fasta)
        self.menuHelp.addAction(self.actionExport)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #============== Connecting to Backend ==================
        self.buttonImportSeq.clicked.connect(lambda: self.importSeq())

        self.buttonImportConsurf.clicked.connect(lambda: self.importConsurf())

        self.buttonSupercharge.clicked.connect(lambda: self.superCharge(MainWindow.ax))

        self.buttonClear.clicked.connect(lambda: self.clearGraph(MainWindow.ax))

        self.buttonGraph.clicked.connect(lambda: self.drawGraph(MainWindow.ax))

        self.buttonExport.clicked.connect(lambda: self.exportHTML())

        #=============== Extra Variables =================

        self.consurfScore = None
        self.exposureScore = None

        #=============== Default Parameters =================

        self.inputTarget.setText("R,K")
        self.inputStandin.setText("D,E")
        self.inputInclude.setText("")
        self.inputExclude.setText("")

        #=============== Testing ================
        # self.inputSeq.setText('''MLPGVGLTPS AAQTARQHPK MHLAHSTLKP AAHLIGDPSK QNSLLWRANT
        # DRAFLQDGFS LSNNSLLVPT SGIYFVYSQV VFSGKAYSPK ATSSPLYLAH
        # EVQLFSSQYP FHVPLLSSQK MVYPGLQEPW LHSMYHGAAF QLTQGDQLST
        # HTDGIPHLVL SPSTVFFGAF AL''')
        # self.inputBinding.setText('20-23+27')
        # self.inputTarget.setText("R, K")
        # self.inputStandin.setText("D, E")


    @pyqtSlot()
    def importSeq(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Select Sequence File', '.txt')
        file = open(list(filename)[0], 'r')

        with file:
            text = file.read()
            self.inputSeq.setText(text)


    @pyqtSlot()
    def importConsurf(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Select Consurf File', '.txt')

        self.consurfScore, self.exposureScore, aaSeq = superSeq.consurfReader(list(filename)[0])
        print(self.consurfScore)
        self.labelConsurfStatus.setText("Imported")
        self.inputSeq.setText(aaSeq)



    @pyqtSlot()
    def superCharge(self,ax):
        try:
            thres = int(self.inputThres.text())
            target = self.inputTarget.toPlainText().split(',')
            standin = self.inputStandin.toPlainText().split(',')
            exclude = superSeq.formatSite(self.inputExclude.toPlainText())
            include = superSeq.formatSite(self.inputInclude.toPlainText())

            sSeq = superSeq(self.inputSeq.toPlainText())

            print(self.labelConsurfStatus.text)

            if self.labelConsurfStatus.text() == "Imported":
                for i,aa in enumerate(self.inputSeq.toPlainText()):
                    if self.consurfScore[i] < 6:
                        include.append(i)
                    if self.consurfScore[i] > 5:
                        exclude.append(i)

            print(include)

            x, y1, y2, newSeq, mutated = sSeq.superGraph(thres=thres,excl=exclude,incl=include,tar=target, stand=standin)
            if not self.checkAdd.isChecked():
                ax.clear()
                ax.plot(x, y1, color='blue')
                ax.plot(x, y2, color='orange')
                ax.axhline(thres, 0, 1, alpha=0.6, color="#00F481")
            else:
                ax.plot(x,y2)

            if self.checkSeperate.isChecked():
                plt.plot(x, y1, color='blue')
                plt.plot(x, y2, color='orange')
                plt.axhline(thres, 0, 1, alpha=0.6, color="#00F481")
                plt.show()

            ax.figure.canvas.draw()
            mutatedText = '[ ' + ', '.join(map(str, [x+1 for x in mutated])) + ' ]'
            resultText = ''.join(newSeq) + '\n' + mutatedText + '\n\n'
            if self.checkPrevious.isChecked():
                oldResult = self.outputResult.toPlainText()
                self.outputResult.setText(oldResult + resultText)
            else:
                self.outputResult.setText(resultText)

        except Exception as e:
            print(e)



    @pyqtSlot()
    def clearGraph(self, ax):
        ax.clear()
        ax.figure.canvas.draw()

    @pyqtSlot()
    def drawGraph(self,ax):
        excl = superSeq.formatSite(self.inputExclude.toPlainText())
        incl = superSeq.formatSite(self.inputInclude.toPlainText())
        sSeq = superSeq(self.inputSeq.toPlainText())

        ax.clear()
        y = sSeq.getChargePool(sSeq.seqStr)

        ax.plot(range(len(y)),y,color='purple')

        if excl != None:
            yExcl = [y[i] for i in excl]
            ax.plot(excl,yExcl,color='red')
        if incl != None:
            yIncl = [y[i] for i in incl]
            ax.plot(incl,yIncl,color='blue')

        ax.figure.canvas.draw()

    @pyqtSlot()
    def exportHTML(self):
        text = self.outputResult.toPlainText()
        tList = text.split('\n\n')
        tList.remove('')

        consf, consv = [],[]

        writeHTML(tList,consf,consv)

        print('exported')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SuperCharging Automation"))
        self.labelSeq.setText(_translate("MainWindow", "Sequence"))
        self.buttonGraph.setText(_translate("MainWindow", "Graph"))
        self.labelThres.setText(_translate("MainWindow", "Threshold"))
        self.labelTarget.setText(_translate("MainWindow", "Target AA"))
        self.labelStandin.setText(_translate("MainWindow", "Stand-in AA"))
        self.labelExclude.setText(_translate("MainWindow", "Exclusion"))
        self.inputExclude.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-1</p></body></html>"))
        self.labelConsurf.setText(_translate("MainWindow", "ConSurf"))
        self.labelConsurfStatus.setText(_translate("MainWindow", "Not Imported"))
        self.buttonImportConsurf.setText(_translate("MainWindow", "Import"))
        self.labelInclude.setText(_translate("MainWindow", "Inclusion"))
        self.inputInclude.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-1</p></body></html>"))
        self.checkAdd.setText(_translate("MainWindow", "add"))
        self.checkSeperate.setText(_translate("MainWindow", "seperate window"))
        self.buttonSupercharge.setText(_translate("MainWindow", "Supercharge"))
        self.buttonClear.setText(_translate("MainWindow", "clear"))
        self.labelResult.setText(_translate("MainWindow", "Result"))
        self.checkPrevious.setText(_translate("MainWindow", "Keep Previous"))
        self.buttonExport.setText(_translate("MainWindow", "Export"))
        self.label.setText(_translate("MainWindow", "by Hieu @ AhnLab/KSA Microbial Lab"))
        self.menuHelp.setTitle(_translate("MainWindow", "File"))
        self.actionImport_Fasta.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))


def writeHTML(tlist,consf,consv,co=False):

    highlight_dict = {"mu":"FF0000","co":"00CC66","va":"ff5050",}

    with open('result.html', 'w') as html:

        html.write('<center><font face="Times New Roman" size="15">Supercharging Result</font></center><br><br>')

        for text in tlist:
            seq, mu_index = text.split('\n')
            mu_index = list(map(int,mu_index[1:-1].split(', ')))
            mu_index.sort()
            mu_out = map(str, mu_index[:])
            newSeq = ''
            for i,e in enumerate(seq):
                if len(mu_index)>0 and i == mu_index[0]-1:
                    mu_index.pop(0)
                    newSeq+='<span style="background-color: #FF0000">'+e+'</span>'
                else: newSeq+=e 
                if i+1!=0 and (i+1)%10==0:newSeq+='&nbsp;'
                if i+1!=0 and (i+1)%50==0:newSeq+='<br>'

            newSeq = "<font face='Courier New' size='2'>"+newSeq+'</font><br><br>'
            newSeq += "<font face='Times New Roman' size='3'> mutated residue: [ "+', '.join(mu_out)+' ]</font><br><br><br>'

            html.write(newSeq)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
