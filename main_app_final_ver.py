import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from ui_main import Ui_MainWindow
from guide_window import Ui_Dialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.confirm.clicked.connect(self.open_dialog)
        self.rewatch.clicked.connect(self.open_dialog)
        self.dialog = Dialog(self)






    def open_dialog(self):
        selected_text = self.hero_choose.currentText()
        selected_text2 = self.rule_choose.currentText()
        selected_txt = self.last_hero.selectedText()
        if (selected_text == "Void Spirit" and selected_text2 == "Мид") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Void Spirit Mид</span></p></body></html>" :
            self.dialog.txt_guide.setText(f"Основная роль Void Spirit - быть живучим инициатором"
                                       f" \nдрак и наносить много быстрого урона по врагам."
                                         "\nЭтот герой мобилен, имеет стан, может впитать урон"
                                        " \nщитом и может быть полезным на всех стадиях игры."
                                      "\n\nСуть билда заключается в актуальности артефактов"
                                        "\nMANTA STYLE это отличный начальный артефакт"
                                        "\nК томуже можно взять BOOTS OF TRAVEL а не PT,"
                                        "\nтогда план на раннюю игру: Драка, Фонтан, фарм"
                                       " \nЕсли игра не задалась, стоит взять PT+MAGE SLAYER"
                              "\n\nДалее идут слоты для тимфайта, например AGANIM SEPTER \nAS имеет сразу несколько аспектов полезных в тимфайте:"
                              "\n -массовое безмолвие которое можно использовать дважды \n -неплохой AOE урон \n -2 физ щита усиляющиеся от задетых героев"
                              "\nKAYA-SANGE имеет все необходимые VOIDу статы \nSHIVAS GUARD также помогает в тимфайте: \n -замедляя атаку и скорость врагов \n -повышая входящий урон"
                              "\n -уменьшая восстановление здоровья врагам \nBKB это ситуативный айтем, брать на свое усмотрение \n\nПод конец игры стоит докупить слоты на урон или на сейв"
                              "\n\nТаланты стоит брать: левый левый левый левый")
            pixmap = QPixmap("void2.png")
            self.dialog.img_guide.setPixmap(pixmap)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Void Spirit Mид</span></p></body></html>")

        elif selected_text == "Пусто" or selected_text2 == "Пусто":
            self.dialog.txt_guide.setText("Выбирете героя и роль")
            pixmap14 = QPixmap("rapira.jpg")
            self.dialog.img_guide.setPixmap(pixmap14)
            self.dialog.url_guide.setText("")

        elif (selected_text == "Void Spirit" and selected_text2 == "Оффлейнер") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Void Spirit Оффлейн</span></p></body></html>" :
            self.dialog.txt_guide.setText(
                f"Основная роль Void Spirit - быть живучим инициатором \nдрак и вносить огромное количество быстрого урона врагам."
                "\nЭтот герой очень мобилен, имеет притяжку, может впитать \nурон щитом и может быть очень полезным на всех стадиях игры."
                "\n\nПервый предмет на линию это всегда URN OF SHADOWS \nЗатем берется артефакт для тимфайта:MAGE SLAYER"
                "\nС этими двумя артефактами ты уже неплохо дамажишь. \nПлан на раннюю игру заключается в роуме по карте\nЕсли же игра не задалась, стоит взять MIDAS вместо URNы"
                "\n\nДалее идут слоты для тимфайта, например: \nAGANIM имеющий важные аспекты полезные в тимфайте:"
                "\n -массовое безмолвие которое можно использовать дважды \n -неплохой AOE урон \n -2 щита всегда лучше чем 1"
                "\nKAYA-SANGE имеет все необходимые VOIDу статы \nSHIVAS GUARD также помогает в тимфайте: \n -замедляя атаку и скорость врагов \n -повышая входящий урон"
                "\n -уменьшая восстановление здоровья врагам \nBKB это ситуативный айтем, но очень востребованый\n\nПод конец игры стоит докупить слоты на урон или на сейв"
                "\n\nТаланты стоит брать: левый левый левый левый")
            pixmap1 = QPixmap("void3.jpg")
            self.dialog.img_guide.setPixmap(pixmap1)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Void Spirit Оффлейн</span></p></body></html>")

        elif selected_text == "Void Spirit" and selected_text2 == "Керри" or selected_text2 == "Софт-Саппорт" or selected_text2 == "Фулл-Саппорт":
            self.dialog.txt_guide.setText("Не стоит выбирать этого героя на эту роль")
            pixmap3 = QPixmap("rapira.jpg")
            self.dialog.img_guide.setPixmap(pixmap3)

        elif (selected_text == "Marci" and selected_text2 == "Оффлейнер") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Marci Оффлейн</span></p></body></html>":
            self.dialog.txt_guide.setText(f"Основная роль Marci в игре, это быть инициатором драк\nнаносящим огромное количество урона и контроля по врагам."
                              "\nЭтот герой очень мобилен, имеет стан, много урона,\nпассивный бонус к вампиизму полезный на всех стадиях игры."
                              "\n\nПервый предмет на линию это всегда ORB OF CORROSION\nЗатем берется артефакт для тимфайта:BLADE MAIL"
                              "\nС этими двумя артефактами ты уже неплохо дерешься.\nПлан на раннюю игру заключается в роуме по карте\nили же целенапраленном навязывании драк на своей линии"
                              "\nЕсли же игра не задалась, то вместо ORBа взять MIDAS"
                              "\n\nДалее идут слоты для тимфайта, например:\nAGANIM имеющий важные аспекты полезные в тимфайте:"
                              "\n -массовое безмолвие во время ульты\n -уменьшение кулдауна ультиммейта\n -развеивание при применение ульты"
                              "\nBASHER хорош из за быстроты нанесения ударов\nSHARD дает возможность соло-кила и преследования"
                              "\nBKB это ситуативный айтем, актуальный почти всегда\n\nПод конец игры стоит докупить слот по ситуации\nНапример при нехватке урона можно взять DAEDALUS"
                              "\nа при нехватке выживаемости - LINKEN или WW"
                              "\n\nТаланты стоит брать: правый правый левый левый")
            pixmap5 = QPixmap("marciofflane.png")
            self.dialog.img_guide.setPixmap(pixmap5)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Marci Оффлейн</span></p></body></html>")

        elif (selected_text == "Marci" and selected_text2 == "Мид") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Marci Мид</span></p></body></html>":
            self.dialog.txt_guide.setText(f"Основная роль Marci в игре, это быть инициатором драк\nнаносящим огромное количество урона и контроля по врагам."
                              "\nЭтот герой очень мобилен, имеет стан, много урона,\nпассивный бонус к вампиизму полезный на всех стадиях игры."
                              "\n\nПервый предмет на линию после это всегда ORB OF CORROSION\nЗатем берется артефакт для тимфайта:DIFFUSAL BLADE"
                              "\nС этими двумя артефактами ты уже неплохо дерешься.\nПлан на раннюю игру заключается в демонтаже мид тавера\nа затем навязывании драк на сайд линиях"
                              "\nДраться по кд ульты, смок+2 сапа и вперед\nЕсли же игра не задалась, то вместо ORBа взять MIDAS"
                              "\n\nДалее идут слоты для тимфайта, например:\nAGANIM имеющий важные аспекты полезные в тимфайте:"
                              "\n -массовое безмолвие во время ульты\n -уменьшение кулдауна ультиммейта\n -развеивание при применение ульты"
                              "\nBASHER хорош из за быстроты нанесения ударов\nSHARD дает возможность соло-кила и преследования"
                              "\nBKB это ситуативный айтем, актуальный почти всегда\n\nПод конец игры стоит докупить слот по ситуации\nНапример при нехватке урона можно взять DAEDALUS"
                              "\nа при нехватке выживаемости - LINKEN или DISPERSER"
                              "\n\nТаланты стоит брать: правый правый левый левый")
            pixmap6 = QPixmap("marcimid.png")
            self.dialog.img_guide.setPixmap(pixmap6)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Marci Мид</span></p></body></html>")

        elif (selected_text == "Marci" and selected_text2 == "Софт-Саппорт") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Marci Саппорт</span></p></body></html>":
            self.dialog.txt_guide.setText(f"Основная роль Marci в игре, это быть инициатором драк\nнаносящим огромное количество урона и контроля по врагам."
                              "\nЭтот герой очень мобилен, имеет стан, много урона, а также\nпассивный бонус к вампиизму полезный на всех стадиях игры."
                              "\nХороший агрессивный сап, который хорош в роуме"
                              "\n\nПервый предмет на линию это всегда ORB OF CORROSION\nБотинок на выбор, смотря чего не хватает"
                              "\nЗатем берется либо BLINK DAGGER + SHARD на темп\nЛибо GLIMMER CAPE + AETHER LENS для сейва\nПлан на раннюю игру заключается в роуме по карте"
                              "\nЕсли игра не задалась, стоит сосредоточиться на сейв айтемах"
                              "\n\nДалее идут слоты для тимфайта, например:\nAGANIM имеющий важные аспекты полезные в тимфайте:"
                              "\n -массовое безмолвие во время ульты\n -уменьшение кулдауна ультиммейта\n -развеивание при применение ульты"
                              "\nDIFFUSAL хорош изза быстроты нанесения ударов в ульте\nLINKEN дает возможность сейвить тиммейтов или себя"
                              "\nBKB это ситуативный айтем, актуальный почти всегда\n\nПод конец игры стоит докупить слот по ситуации\nНапример при нехватке урона можно взять DAEDALUS"
                              "\nа при нехватке контроля - BLOTHTORN"
                              "\n\nТаланты стоит брать: правый правый левый левый")
            pixmap7 = QPixmap("marcisupport.png")
            self.dialog.img_guide.setPixmap(pixmap7)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Marci Саппорт</span></p></body></html>")

        elif (selected_text == "Marci" and selected_text2 == "Керри") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Marci Керри</span></p></body></html>":
            self.dialog.txt_guide.setText(f"Основная роль Marci в игре, это быть инициатором драк\nнаносящим огромное количество урона и контроля по врагам."
                              "\nЭтот герой очень мобилен, имеет стан, много урона,\nпассивный бонус к вампиизму полезный на всех стадиях игры."
                              "\n\nПервый предмет на линию после это всегда ORB OF CORROSION\nЗатем берется артефакт для тимфайта:DIFFUSAL BLADE"
                              "\nС этими двумя артефактами ты уже неплохо дерешься.\nПлан на раннюю игру заключается в демонтаже мид тавера\nа затем навязывании драк на сайд линиях"
                              "\nДраться по кд ульты, смок+2 сапа и вперед\nЕсли же игра не задалась, то вместо ORBа взять MIDAS"
                              "\n\nДалее идут слоты для тимфайта, например:\nAGANIM имеющий важные аспекты полезные в тимфайте:"
                              "\n -массовое безмолвие во время ульты\n -уменьшение кулдауна ультиммейта\n -развеивание при применение ульты"
                              "\nBASHER хорош из за быстроты нанесения ударов\nSHARD дает возможность соло-кила и преследования"
                              "\nBKB это ситуативный айтем, актуальный почти всегда\n\nПод конец игры стоит докупить слот по ситуации\nНапример при нехватке урона можно взять DAEDALUS"
                              "\nа при нехватке выживаемости - LINKEN или DISPERSER"
                              "\n\nТаланты стоит брать: правый правый левый левый")
            pixmap8 = QPixmap("marcimid.png")
            self.dialog.img_guide.setPixmap(pixmap8)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Marci Керри</span></p></body></html>")

        elif (selected_text == "Ember Spirit" and selected_text2 == "Мид") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Ember Spirit Мид</span></p></body></html>":
            self.dialog.txt_guide.setText(f"Основная роль Ember Spirit в игре-быть мобильным героем с\nпотенциалом как для затяжной драки, так и быстрого пикофа"
                              "\nЭтот герой мобилен, имеет связку, маг барьер и\nможет быть очень полезным на всех стадиях игры."
                              "\n\nСуть билда заключается в инициации ранних драк в которые\nMAGE SLAYER и ORB могут внести ощутимый импакт"
                              "\nЗатем берется MAELSTORM для того что бы успевать в темп.\nПо игре план такой: подрался, ремнант, тп на базу, фарм\nЕсли игра не задалась, то стоит подключится к комманде"
                              "\n\nДалее идут слоты на тимфайта, например AGANIM SEPTER \nAS имеет сразу несколько аспектов полезных в тимфайте:"
                              "\n -больше ремнантов - значит большая мобильность \n -возможность быстро уйти из драки или зайти в нее"
                              "\nKAYA-SANGE имеет все необходимые EMBERу статы \nSHIVAS GUARD также помогает в тимфайте: \n -замедляя атаку и скорость врагов \n -повышая входящий урон"
                              "\n -уменьшая восстановление здоровья врагам \nBKB это ситуативный айтем, актуальный на каждом герое \n\nПод конец игры стоит докупить слоты на урон или на сейв"
                              "\n\nТаланты стоит брать: левый правый левый правый")
            pixmap9 = QPixmap("embermid.png")
            self.dialog.img_guide.setPixmap(pixmap9)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Ember Spirit Мид</span></p></body></html>")

        elif selected_text == "Ember Spirit" and selected_text2 == "Керри" or selected_text2 == "Оффлейн" or selected_text2 == "Софт-Саппорт" or selected_text2 == "Фулл-Саппорт":
            self.dialog.txt_guide.setText(f"Не стоит пикать этого героя на эту роль")
            pixmap10 = QPixmap("rapira.jpg")
            self.dialog.img_guide.setPixmap(pixmap10)

        elif (selected_text == "Pudge" and selected_text2 == "Мид") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Pudge Мид</span></p></body></html>":
            self.dialog.txt_guide.setText(f"Основная роль PUDGE в игре, это быть живучим героем с\n продолжительным, быстрым уроном и контролем файта."
                              "\nPUDGE может хукнуть врага, нарушив его позиционку,\n может впитывать много урона, а также хорошо гангать"
                              "\n\nСуть билда заключается в постепенном усилении героя \nСтоит взять ORB OF COROSION для доминации на линии"
                              "\nЗатем берется BLINK если лайнинг прошел удачно, \nили начать сразу с ETHERIAL BLADE для усиления прокаста\nЕсли игра не задалась, то стоит пойти в ганги на сайды"
                              "\n\nДалее идут слоты для тимфайта, например AGANIM SEPTER \nAS имеет сразу несколько аспектов полезных в тимфайте:"
                              "\n -усиление и без того большого урона \n -уменьшение восстановление хп врагам\n -радиус урона, замедления и дебафф аувеличивается в два раза"
                              "\nкупив AS необходимо купить SHROUD для маг резиста\nSHIVAS GUARD также помогает в тимфайте: \n -замедляя атаку и скорость врагов \n -повышая входящий урон"
                              "\n -уменьшая восстановление здоровья врагам \nBKB это ситуативный айтем, актуальный на каждом герое \n\nПод конец игры стоит докупить слоты на урон или на сейв"
                              "\n\nТаланты стоит брать: левый правый правый правый")
            pixmap11 = QPixmap("pudgemid.jpg")
            self.dialog.img_guide.setPixmap(pixmap11)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Pudge Мид</span></p></body></html>")

        elif (selected_text == "Pudge" and selected_text2 == "Оффлейнер") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Pudge Оффлейнер</span></p></body></html>":
            self.dialog.txt_guide.setText(f"Основная роль PUDGE в игре, это быть живучим героем с\n продолжительным, быстрым уроном и контролем файта."
                              "\nPUDGE может хукнуть врага, нарушив его позиционку,\n может впитывать много урона, а также хорошо гангать"
                              "\n\nСуть билда заключается в постепенном усилении героя \nСтоит взять ORB OF COROSION для доминации на линии"
                              "\nЗатем берется BLINK если лайнинг прошел удачно, \nили начать сразу с ETHERIAL BLADE для усиления прокаста\nЕсли игра не задалась, то стоит пойти в ганги на сайды"
                              "\n\nДалее идут слоты для тимфайта, например AGANIM SEPTER \nAS имеет сразу несколько аспектов полезных в тимфайте:"
                              "\n -усиление и без того большого урона \n -уменьшение восстановление хп врагам\n -радиус урона, замедления и дебафф аувеличивается в два раза"
                              "\nкупив AS необходимо купить SHROUD для маг резиста\nSHIVAS GUARD также помогает в тимфайте: \n -замедляя атаку и скорость врагов \n -повышая входящий урон"
                              "\n -уменьшая восстановление здоровья врагам \nBKB это ситуативный айтем, актуальный на каждом герое \n\nПод конец игры стоит докупить слоты на урон или на сейв"
                              "\n\nТаланты стоит брать: левый правый правый правый")
            pixmap12 = QPixmap("pudgeofflane.png")
            self.dialog.img_guide.setPixmap(pixmap12)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Pudge Оффлейнер</span></p></body></html>")

        elif (selected_text == "Pudge" and selected_text2 == "Софт-Саппорт") or selected_txt == "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Pudge Ссаппорт</span></p></body></html>":
            self.dialog.txt_guide.setText(f"Основная роль PUDGE в игре, это быть живучим героем с\n продолжительным, быстрым уроном и контролем файта."
                              "\nPUDGE может хукнуть врага, нарушив его позиционку,\n может впитывать много урона, а также хорошо гангать"
                              "\n\nСуть билда заключается в постепенном усилении героя.\nСапог берется в зависимости от кора и того, что ему нужно \nЗатем взять быстрый BLINK для комфортной игры"
                              "\nЕсли игра не задалась, стоит пойти помогать на другие линии"
                              "\n\nДалее идут слоты для тимфайта, например AGANIM SHARD \nAS имеет сразу важнейший для саппорта - сейв"
                              "\n -шард позволяет съесть тиммейта, отхилив его"
                              "\nкупив AS нужно купить AETHER LENS для лучшей позиционки\nFORCE STAFF помогает сейвить тиммейтов или себя\nPIPE берется против большого маг урона"
                              "\nBKB это ситуативный айтем, актуальный на каждом герое \n\nПод конец игры стоит докупить слоты на на сейв или живучесть"
                              "\n\nТаланты стоит брать: левый левый правый правый")
            pixmap13 = QPixmap("pudgesupport.png")
            self.dialog.img_guide.setPixmap(pixmap13)
            self.dialog.url_guide.setText("https://steamcommunity.com/sharedfiles/filedetails/?id=3225093533")
            self.last_hero.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Последний герой: Pudge Ссаппорт</span></p></body></html>")

        self.dialog.show()
        self.dialog.setWindowModality(QtCore.Qt.NonModal)

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())




