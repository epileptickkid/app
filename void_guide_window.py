from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLabel
from PyQt5.QtGui import QPixmap
class Ui_Dialog_VoidMid(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(741, 561)
        Dialog.setMinimumSize(QtCore.QSize(741, 561))
        Dialog.setMaximumSize(QtCore.QSize(741, 561))
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Arial Black;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 341, 41))
        self.label.setStyleSheet("background-color:rgba(255,255,255,40)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(380, 20, 341, 41))
        self.label_2.setStyleSheet("background-color:rgba(255,255,255,40)")
        self.label_2.setObjectName("label_2")
        self.txt_guide = QtWidgets.QLabel(Dialog)
        self.txt_guide.setGeometry(QtCore.QRect(20, 70, 340, 391))
        self.txt_guide.setStyleSheet("background-color:rgba(255,255,255,40)")
        self.txt_guide.setObjectName("txt_guide")
        self.img_guide = QtWidgets.QLabel(Dialog)
        self.img_guide.setGeometry(QtCore.QRect(380, 70, 340, 391))
        self.img_guide.setStyleSheet("background-color:rgba(255,255,255,40)")
        self.img_guide.setObjectName("img_guide")
        self.url_guide = QtWidgets.QTextBrowser(Dialog)
        self.url_guide.setGeometry(QtCore.QRect(170, 500, 401, 41))
        self.url_guide.setObjectName("url_guide")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 470, 281, 31))
        self.label_5.setStyleSheet("background-color:rgba(255,255,255,40)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 460, 701, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(360, 20, 21, 441))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.txt_guide.raise_()
        self.img_guide.raise_()
        self.url_guide.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Гайд"))
        Dialog.setWindowIcon(QtGui.QIcon("dota_icon_project"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">Описание билда</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Что собирать и какие брать таланты</span></p></body></html>"))
        self.txt_guide.setText(_translate("Dialog", f"Основная роль Void Spirit в игре, это быть живучим инициатором \nдрак и вносить огромное количество быстрого урона по врагам."
                              "\nЭтот герой очень мобилен, имеет притяжку, может впитать \nурон щитом и может быть очень полезным на всех стадиях игры."
                              "\n\nСуть билда заключается в актуальности артефактов \nMANTA STYLE хорошо себя показывает как начальный артефакт"
                              "\nК томуже с MANTAой можно взять BOOTS OF TRAVEL а не PT \nтогда план на раннюю игру такой: Подрался, TP на базу, фарм \nЕсли же игра не задалась, то стоит взять PT + MAGE SLAYER"
                              "\n\nДалее идут слоты для тимфайта, например AGANIM SEPTER \nAS имеет сразу несколько аспектов полезных в тимфайте:"
                              "\n -массовое безмолвие которое можно использовать дважды \n -неплохой AOE урон \n -2 щита которые тем профитнее, чем больше врагов заденут"
                              "\nKAYA-SANGE имеет все необходимые VOIDу статы \nSHIVAS GUARD также помогает в тимфайте: \n -замедляя атаку и скорость врагов \n -повышая входящий урон"
                              "\n -уменьшая восстановление здоровья врагам \nBKB это ситуативный айтем, актуальный почти на каждом герое \n\nПод конец игры стоит докупить слоты на урон или на сейв"
                              "\n\nТаланты стоит брать: левый левый левый левый"))
        self.img_guide.setPixmap(QPixmap("void2.png"))
        self.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Ссылка на steam-руководство</span></p></body></html>"))

