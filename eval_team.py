# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eval_team.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
conn=sqlite3.connect('fantasy_cricket.db')
cur=conn.cursor()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(519, 454)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 501, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 90, 521, 20))
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 50, 501, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cb1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cb1.setObjectName("cb1")
        self.horizontalLayout_2.addWidget(self.cb1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cb2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cb2.setObjectName("cb2")
        self.cb2.addItem("")
        self.cb2.addItem("")
        self.cb2.addItem("")
        self.horizontalLayout_2.addWidget(self.cb2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(19, 139, 481, 221))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.list01 = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.list01.setObjectName("list01")
        self.horizontalLayout_3.addWidget(self.list01)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.list02 = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.list02.setObjectName("list02")
        self.horizontalLayout_3.addWidget(self.list02)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(19, 100, 481, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(169, 370, 161, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        #Adding names of teams to combo Box1.
        cur.execute("SELECT name FROM teams")
        team_data = cur.fetchall()
        team_data = list(set(team_data))
        for data in team_data:
            self.cb1.addItem(data[0])
        conn.close()
        self.pushButton.clicked.connect(self.display)
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Evaluate the Performance of your Fantasy Team"))
        self.label_3.setText(_translate("Dialog", "Select Team"))
        self.label_2.setText(_translate("Dialog", "Select Match"))
        self.cb2.setItemText(0, _translate("Dialog", "match1"))
        self.cb2.setItemText(1, _translate("Dialog", "match2"))
        self.cb2.setItemText(2, _translate("Dialog", "match3"))
        self.label_5.setText(_translate("Dialog", "Players"))
        self.label_4.setText(_translate("Dialog", "Points"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))


    def display(self):
        import sqlite3
        conn=sqlite3.connect('fantasy_cricket.db')
        team=self.cb1.currentText()
        self.list01.clear()
        try:
            #Adding players to list1 according to team name.
            sql1="SELECT players,tot_value from teams where name='"+team+"';"
            cur=conn.execute(sql1)
            row=cur.fetchone()
            list_add=row[0].split(',')
            self.list01.addItems(list_add)
        except:
            conn.rollback()
        team_total=0
        self.list02.clear()
        match=self.cb2.currentText()
        try:
            #For every player in list1:
            for i in range(self.list01.count()):
                total=0
                batscore=0
                bowlscore=0
                fieldscore=0
                name=self.list01.item(i).text()
                cursor1=cur.execute("SELECT * from "+match+" WHERE player='"+name+"';")
                row=cursor1.fetchone()
                batscore=int(row[1]/2)
                if batscore>=50:
                    batscore+=5
                if batscore>=100:
                    batscore+=10
                #Calculating strike rate.
                if row[2]>0:
                    strike_rate=row[1]/row[2]
                    if strike_rate>=80 and strike_rate<=100:
                        batscore+=2
                    if strike_rate>100:
                        batscore+=4
                #Calculating score for 4s and 6s.
                batscore+=row[3]
                batscore+=(2*row[4])
                bowlscore=10*row[8]
                if row[8]>=3:
                    bowlscore+=5
                if row[8]>=5:
                    bowlscore+=10
                #Calculating economy rate.
                if row[5]>0:
                    eco_rate=6*row[7]/row[5]
                    if eco_rate>=3.5 and eco_rate<=4.5:
                        bowlscore+=4
                    if eco_rate>=2 and eco_rate<3.5:
                        bowlscore+=7
                    if eco_rate<2:
                        bowlscore+=10
                #Calculating fieldscore.
                fieldscore=10*(row[9]+row[10]+row[11])
                #Calculating score of individual player,setting value in list2
                #Adding to team total.
                total=batscore+bowlscore+fieldscore
                self.list02.addItem(str(total))
                team_total+=total
        except:
            conn.rollback()
        #Setting total team score in textbox.
        self.lineEdit.setText(str(team_total))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
