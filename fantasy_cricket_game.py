# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasy_cricket_game.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3
Mycricket=sqlite3.connect('fantasy_cricket.db')
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 657)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 921, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c1.jpg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-3, 139, 951, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 180, 931, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.t1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.t1.setObjectName("t1")
        self.horizontalLayout_2.addWidget(self.t1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.t2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.t2.setText("")
        self.t2.setObjectName("t2")
        self.horizontalLayout_2.addWidget(self.t2)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.t3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.t3.setText("")
        self.t3.setObjectName("t3")
        self.horizontalLayout_2.addWidget(self.t3)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.t4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.t4.setObjectName("t4")
        self.horizontalLayout_2.addWidget(self.t4)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 230, 931, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.t5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.t5.setObjectName("t5")
        self.horizontalLayout_3.addWidget(self.t5)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.t6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.t6.setObjectName("t6")
        self.horizontalLayout_3.addWidget(self.t6)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 280, 311, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rbtn1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbtn1.setObjectName("rbtn1")
        self.horizontalLayout_4.addWidget(self.rbtn1)
        self.rbtn2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbtn2.setObjectName("rbtn2")
        self.horizontalLayout_4.addWidget(self.rbtn2)
        self.rbtn3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbtn3.setObjectName("rbtn3")
        self.horizontalLayout_4.addWidget(self.rbtn3)
        self.rbtn4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbtn4.setObjectName("rbtn4")
        self.horizontalLayout_4.addWidget(self.rbtn4)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(9, 309, 931, 291))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.list1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_5)
        self.list1.setObjectName("list1")
        self.horizontalLayout_5.addWidget(self.list1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.list2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_5)
        self.list2.setObjectName("list2")
        self.horizontalLayout_5.addWidget(self.list2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(610, 280, 151, 20))
        self.label_9.setObjectName("label_9")
        self.t7 = QtWidgets.QLineEdit(self.centralwidget)
        self.t7.setGeometry(QtCore.QRect(760, 280, 181, 31))
        self.t7.setObjectName("t7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 29))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_TEAM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.actionNEW_TEAM.setFont(font)
        self.actionNEW_TEAM.setObjectName("actionNEW_TEAM")
        self.actionOPEN_TEAM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.actionOPEN_TEAM.setFont(font)
        self.actionOPEN_TEAM.setObjectName("actionOPEN_TEAM")
        self.actionSAVE_TEAM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.actionSAVE_TEAM.setFont(font)
        self.actionSAVE_TEAM.setObjectName("actionSAVE_TEAM")
        self.actionEVALUATE_TEAM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.actionEVALUATE_TEAM.setFont(font)
        self.actionEVALUATE_TEAM.setObjectName("actionEVALUATE_TEAM")
        self.actionEXIT = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.actionEXIT.setFont(font)
        self.actionEXIT.setObjectName("actionEXIT")
        self.menuManage_Teams.addAction(self.actionNEW_TEAM)
        self.menuManage_Teams.addAction(self.actionOPEN_TEAM)
        self.menuManage_Teams.addAction(self.actionSAVE_TEAM)
        self.menuManage_Teams.addAction(self.actionEVALUATE_TEAM)
        self.menuManage_Teams.addAction(self.actionEXIT)
        self.menubar.addAction(self.menuManage_Teams.menuAction())     

        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menuFunction)
              
        self.rbtn1.toggled.connect(self.category)
        self.rbtn2.toggled.connect(self.category)
        self.rbtn3.toggled.connect(self.category)
        self.rbtn4.toggled.connect(self.category)
        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Your Selections"))
        self.label_3.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.label_4.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.label_5.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.label_6.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.label_7.setText(_translate("MainWindow", "Points Available"))
        self.label_8.setText(_translate("MainWindow", "                                                                    Points Used"))
        self.rbtn1.setText(_translate("MainWindow", "BAT"))
        self.rbtn2.setText(_translate("MainWindow", "BOW"))
        self.rbtn3.setText(_translate("MainWindow", "AR"))
        self.rbtn4.setText(_translate("MainWindow", "WK"))
        self.label_9.setText(_translate("MainWindow", "           Team Name"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_TEAM.setText(_translate("MainWindow", "NEW TEAM"))
        self.actionOPEN_TEAM.setText(_translate("MainWindow", "OPEN TEAM"))
        self.actionSAVE_TEAM.setText(_translate("MainWindow", "SAVE TEAM"))
        self.actionEVALUATE_TEAM.setText(_translate("MainWindow", "EVALUATE TEAM"))
        self.actionEXIT.setText(_translate("MainWindow", "EXIT"))




    def menuFunction(self,action):
        txt=(action.text())
    
        if txt=='NEW TEAM':
            self.bat=0
            self.bow=0
            self.ar=0
            self.wk=0
            self.avl=1500
            self.used=0
            self.list1.clear()
            self.list2.clear()
            #pop-up window
            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "New Team", "Enter name of team:")
            if ok and text:
                self.t7.setText(str(text))
            self.show()
        
        if txt=='SAVE TEAM':
            #Making a list of players in list2 separated by commas.
            count=self.list2.count()
            list_save=""
            for i in range(count):
                list_save+=self.list2.item(i).text()
                if i<count:
                    list_save+=","
            self.save_team(self.t7.text(),list_save,self.used)

        if txt=='OPEN TEAM':
            #Clear all present values.
            self.bat=0
            self.bow=0
            self.ar=0
            self.wk=0
            self.avl=1500
            self.used=0
            self.list1.clear()
            self.list2.clear()
            self.show()
            #Open a team.
            self.open_team()

        if txt=='EVALUATE TEAM':
            #Importing contents of eval_team.py
            from eval_team import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            result=Dialog.exec()

        if txt=='EXIT':
            #Exiting the application.
            self.showdlg("Hope you enjoyed!!!\nVisit Again!!")
            import sys
            sys.exit()
            

            
    def show(self):
        #Setting values for all the lineEdits.
        self.t1.setText(str(self.bat))
        self.t2.setText(str(self.bow))
        self.t3.setText(str(self.wk))
        self.t4.setText(str(self.ar))
        self.t5.setText(str(self.avl))
        self.t6.setText(str(self.used))



    def speciality(self,ctgr,item):
        msg=''
        if ctgr=="BAT" and self.bat>=5:
            msg="Batsmen more than 5 not allowed!"
        if ctgr=="BOW" and self.bow>=5:
            msg="Bowlers more than 5 not allowed!"
        if ctgr=="AR" and self.ar>=3:
            msg="Allrounders more than 3 not allowed!"
        if ctgr=="WK" and self.wk>=1:
            msg="Wicketkeepers more than 1 not allowed!"
        if msg!='':
            self.showdlg(msg)
            return False
        #Setting values for BAT,BOW,AR & WK according to their speciality.
        if ctgr=="BAT":
            self.bat+=1
        if ctgr=="BOW":
            self.bow+=1
        if ctgr=="AR":
            self.ar+=1
        if ctgr=="WK":
            self.wk+=1
        #Setting values for points available and points used.
        sql="SELECT value from stats where player='"+item.text()+"'"
        curcricket=Mycricket.execute(sql)
        row=curcricket.fetchone()
        self.avl-=int(row[0])
        self.used+=int(row[0])
        return True



    def category(self):
        #Selecting desired radio button and assigning appropriate category to it.
        ctgr=''
        if self.rbtn1.isChecked()==True:
            ctgr='BAT'
        if self.rbtn2.isChecked()==True:
            ctgr='BOW'
        if self.rbtn3.isChecked()==True:
            ctgr='AR'
        if self.rbtn4.isChecked()==True:
            ctgr='WK'
        self.display_list(ctgr)


    def display_list(self,ctgr):
        #If team name is not entered!
        if self.t7.text()=='':
            self.showdlg("Enter name of team")
            return
        #Displaying players in list1.
        self.list1.clear()
        sql="SELECT player from stats where ctg='"+ctgr+"';"
        curcricket=Mycricket.execute(sql)
        for row in curcricket:
            list_fill=[]
            for i in range(self.list2.count()):
                list_fill.append(self.list2.item(i).text())
            if row[0] not in list_fill:self.list1.addItem(row[0])
            


    def removelist1(self,item):
        #Removing players from list1 and adding to list 2.
        #Based on their speciality if condition is satisfied.
        ctgr=''
        if self.rbtn1.isChecked()==True:
            ctgr='BAT'
        if self.rbtn2.isChecked()==True:
            ctgr='BOW'
        if self.rbtn3.isChecked()==True:
            ctgr='AR'
        if self.rbtn4.isChecked()==True:
            ctgr='WK'
        ret=self.speciality(ctgr,item)
        self.list1.takeItem(self.list1.row(item))
        if ret==True:
            self.list2.addItem(item.text())
            self.show()



    def removelist2(self,item):
        #Removing players from list 2 to list 1.
        #Players are diplayed if their corresponding category radio button is selected.
        self.list2.takeItem(self.list2.row(item))
        curcricket = Mycricket.execute("SELECT player,value,ctg from stats where player='"+item.text()+"'")
        row=curcricket.fetchone()
        self.avl+=int(row[1])
        self.used-=int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.rbtn1.isChecked()==True:
                self.list1.addItem(item.text())
        if ctgr=="BOW":
            self.bow-=1
            if self.rbtn2.isChecked()==True:
                self.list1.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.rbtn3.isChecked()==True:
                self.list1.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.rbtn4.isChecked()==True:
                self.list1.addItem(item.text())
        self.show()


    
        

    def open_team(self):       
        sql="select name from teams;"
        curcricket=Mycricket.execute(sql)
        teams=[]
        for row in curcricket:
            teams.append(row[0])
        #Pop-up window showing a list of team to be selected.
        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Open Team","Select Team",teams,0,False)
        if ok and team:
            self.t7.setText(team)
        #Fetching list of players from database to display in list2.
        res="SELECT players,tot_value from teams where name='"+team+"';"
        curcricket=Mycricket.execute(res)
        row=curcricket.fetchone()
        list_open=row[0].split(',')
        self.list2.addItems(list_open)
        self.used=row[1]
        self.avl=1500-row[1]
        count=self.list2.count()
        #Setting appropriate values for lineEdits.
        for i in range(count-1):
            player=self.list2.item(i).text()
            sql="select ctg from stats where player='"+player+"';"
            curcricket=Mycricket.execute(sql)
            row=curcricket.fetchone()
            ctgr=row[0]
            if ctgr=="BAT":
                self.bat+=1
            if ctgr=="BOW":
                self.bow+=1
            if ctgr=="AR":
                self.ar+=1
            if ctgr=="WK":
                self.wk+=1  
        self.show()


        
    def save_team(self,name,player,val):
        #Setting conditions for players: not > or < 11.
        count=self.list2.count()
        if count!=11:
            self.showdlg("No. of Players should be equal to 11!!")
            return
        #Inserting name of team,players list and their total value in database.
        sql="INSERT INTO teams (name,players,tot_value) VALUES ('"+name+"','"+player+"','"+str(val)+"');"
        curcricket=Mycricket.execute(sql)
        self.showdlg("Team Saved Succesfully")
        Mycricket.commit()
        
        
        
    def showdlg(self,msg):
        #To open a pop-up message box!
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Fantasy Cricket League")
        ret=Dialog.exec()
    


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
