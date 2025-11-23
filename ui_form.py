# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_anaPencere(object):
    def setupUi(self, anaPencere):
        if not anaPencere.objectName():
            anaPencere.setObjectName(u"anaPencere")
        anaPencere.resize(1018, 549)
        anaPencere.setAutoFillBackground(True)
        self.verticalLayoutWidget = QWidget(anaPencere)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(380, 10, 272, 61))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.lblTarihSaat = QLabel(self.verticalLayoutWidget)
        self.lblTarihSaat.setObjectName(u"lblTarihSaat")
        self.lblTarihSaat.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.lblTarihSaat)

        self.verticalLayoutWidget_2 = QWidget(anaPencere)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 160, 111, 331))
        font1 = QFont()
        font1.setPointSize(11)
        self.verticalLayoutWidget_2.setFont(font1)
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_3)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_6)

        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_9)

        self.verticalLayoutWidget_3 = QWidget(anaPencere)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(130, 150, 91, 351))
        self.verticalLayoutWidget_3.setFont(font1)
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lblSiparisNo = QLineEdit(self.verticalLayoutWidget_3)
        self.lblSiparisNo.setObjectName(u"lblSiparisNo")
        self.lblSiparisNo.setFont(font1)

        self.verticalLayout_10.addWidget(self.lblSiparisNo)

        self.txtKizartma = QLineEdit(self.verticalLayoutWidget_3)
        self.txtKizartma.setObjectName(u"txtKizartma")
        self.txtKizartma.setFont(font1)

        self.verticalLayout_10.addWidget(self.txtKizartma)

        self.txtOgle = QLineEdit(self.verticalLayoutWidget_3)
        self.txtOgle.setObjectName(u"txtOgle")
        self.txtOgle.setFont(font1)

        self.verticalLayout_10.addWidget(self.txtOgle)

        self.txtBurger = QLineEdit(self.verticalLayoutWidget_3)
        self.txtBurger.setObjectName(u"txtBurger")
        self.txtBurger.setFont(font1)

        self.verticalLayout_10.addWidget(self.txtBurger)

        self.txtPizza = QLineEdit(self.verticalLayoutWidget_3)
        self.txtPizza.setObjectName(u"txtPizza")
        self.txtPizza.setFont(font1)

        self.verticalLayout_10.addWidget(self.txtPizza)

        self.txtCheeseBurger = QLineEdit(self.verticalLayoutWidget_3)
        self.txtCheeseBurger.setObjectName(u"txtCheeseBurger")
        self.txtCheeseBurger.setFont(font1)

        self.verticalLayout_10.addWidget(self.txtCheeseBurger)

        self.txtIcecekler = QLineEdit(self.verticalLayoutWidget_3)
        self.txtIcecekler.setObjectName(u"txtIcecekler")
        self.txtIcecekler.setFont(font1)

        self.verticalLayout_10.addWidget(self.txtIcecekler)

        self.verticalLayoutWidget_4 = QWidget(anaPencere)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(340, 270, 91, 231))
        self.verticalLayoutWidget_4.setFont(font1)
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.txtFiyat = QLineEdit(self.verticalLayoutWidget_4)
        self.txtFiyat.setObjectName(u"txtFiyat")
        self.txtFiyat.setFont(font1)
        self.txtFiyat.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.txtFiyat)

        self.txtServisHizmeti = QLineEdit(self.verticalLayoutWidget_4)
        self.txtServisHizmeti.setObjectName(u"txtServisHizmeti")
        self.txtServisHizmeti.setFont(font1)
        self.txtServisHizmeti.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.txtServisHizmeti)

        self.txtKDV = QLineEdit(self.verticalLayoutWidget_4)
        self.txtKDV.setObjectName(u"txtKDV")
        self.txtKDV.setFont(font1)
        self.txtKDV.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.txtKDV)

        self.txtAltToplam = QLineEdit(self.verticalLayoutWidget_4)
        self.txtAltToplam.setObjectName(u"txtAltToplam")
        self.txtAltToplam.setFont(font1)
        self.txtAltToplam.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.txtAltToplam)

        self.txtToplam = QLineEdit(self.verticalLayoutWidget_4)
        self.txtToplam.setObjectName(u"txtToplam")
        self.txtToplam.setFont(font1)
        self.txtToplam.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.txtToplam)

        self.verticalLayoutWidget_5 = QWidget(anaPencere)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(240, 280, 101, 211))
        self.verticalLayoutWidget_5.setFont(font1)
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.verticalLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_12)

        self.label_13 = QLabel(self.verticalLayoutWidget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_13)

        self.label_14 = QLabel(self.verticalLayoutWidget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_14)

        self.label_15 = QLabel(self.verticalLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_15)

        self.label_16 = QLabel(self.verticalLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_16)

        self.verticalLayoutWidget_6 = QWidget(anaPencere)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(460, 290, 121, 211))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btnFiyatlar = QPushButton(self.verticalLayoutWidget_6)
        self.btnFiyatlar.setObjectName(u"btnFiyatlar")
        font2 = QFont()
        font2.setPointSize(16)
        self.btnFiyatlar.setFont(font2)
        self.btnFiyatlar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.btnFiyatlar)

        self.btnToplam = QPushButton(self.verticalLayoutWidget_6)
        self.btnToplam.setObjectName(u"btnToplam")
        self.btnToplam.setFont(font2)
        self.btnToplam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.btnToplam)

        self.btnSifirla = QPushButton(self.verticalLayoutWidget_6)
        self.btnSifirla.setObjectName(u"btnSifirla")
        self.btnSifirla.setFont(font2)
        self.btnSifirla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.btnSifirla)

        self.btnCikis = QPushButton(self.verticalLayoutWidget_6)
        self.btnCikis.setObjectName(u"btnCikis")
        self.btnCikis.setFont(font2)
        self.btnCikis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.btnCikis)

        self.verticalLayoutWidget_7 = QWidget(anaPencere)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(620, 140, 342, 351))
        self.verticalLayout_14 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(7)
        self.btn5 = QPushButton(self.verticalLayoutWidget_7)
        self.btn5.setObjectName(u"btn5")
        font3 = QFont()
        font3.setPointSize(25)
        self.btn5.setFont(font3)
        self.btn5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn5, 2, 1, 1, 1)

        self.btn0 = QPushButton(self.verticalLayoutWidget_7)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setFont(font3)
        self.btn0.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn0, 4, 0, 1, 1)

        self.btnC = QPushButton(self.verticalLayoutWidget_7)
        self.btnC.setObjectName(u"btnC")
        self.btnC.setFont(font3)
        self.btnC.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnC, 4, 1, 1, 1)

        self.btn6 = QPushButton(self.verticalLayoutWidget_7)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setFont(font3)
        self.btn6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn6, 2, 2, 1, 1)

        self.btn2 = QPushButton(self.verticalLayoutWidget_7)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setFont(font3)
        self.btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn2, 3, 1, 1, 1)

        self.btn8 = QPushButton(self.verticalLayoutWidget_7)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setFont(font3)
        self.btn8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn8, 1, 1, 1, 1)

        self.btn9 = QPushButton(self.verticalLayoutWidget_7)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setFont(font3)
        self.btn9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn9, 1, 2, 1, 1)

        self.btnNokta = QPushButton(self.verticalLayoutWidget_7)
        self.btnNokta.setObjectName(u"btnNokta")
        self.btnNokta.setFont(font3)
        self.btnNokta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnNokta, 4, 2, 1, 1)

        self.btn1 = QPushButton(self.verticalLayoutWidget_7)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setFont(font3)
        self.btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn1, 3, 0, 1, 1)

        self.btn4 = QPushButton(self.verticalLayoutWidget_7)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setFont(font3)
        self.btn4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 1)

        self.btn3 = QPushButton(self.verticalLayoutWidget_7)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setFont(font3)
        self.btn3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn3, 3, 2, 1, 1)

        self.btnTopla = QPushButton(self.verticalLayoutWidget_7)
        self.btnTopla.setObjectName(u"btnTopla")
        self.btnTopla.setFont(font3)
        self.btnTopla.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnTopla, 1, 3, 1, 1)

        self.btnCikar = QPushButton(self.verticalLayoutWidget_7)
        self.btnCikar.setObjectName(u"btnCikar")
        self.btnCikar.setFont(font3)
        self.btnCikar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnCikar, 2, 3, 1, 1)

        self.btnCarp = QPushButton(self.verticalLayoutWidget_7)
        self.btnCarp.setObjectName(u"btnCarp")
        self.btnCarp.setFont(font3)
        self.btnCarp.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnCarp, 3, 3, 1, 1)

        self.btnBol = QPushButton(self.verticalLayoutWidget_7)
        self.btnBol.setObjectName(u"btnBol")
        self.btnBol.setFont(font3)
        self.btnBol.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnBol, 4, 3, 1, 1)

        self.btnEsittir = QPushButton(self.verticalLayoutWidget_7)
        self.btnEsittir.setObjectName(u"btnEsittir")
        self.btnEsittir.setFont(font3)
        self.btnEsittir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnEsittir, 5, 0, 1, 4)

        self.txtHesapMakinesiEkran = QLineEdit(self.verticalLayoutWidget_7)
        self.txtHesapMakinesiEkran.setObjectName(u"txtHesapMakinesiEkran")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtHesapMakinesiEkran.sizePolicy().hasHeightForWidth())
        self.txtHesapMakinesiEkran.setSizePolicy(sizePolicy)
        self.txtHesapMakinesiEkran.setFont(font3)
        self.txtHesapMakinesiEkran.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.txtHesapMakinesiEkran, 0, 0, 1, 4)

        self.btn7 = QPushButton(self.verticalLayoutWidget_7)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setFont(font3)
        self.btn7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btn7, 1, 0, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout)

        self.label_2 = QLabel(anaPencere)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 520, 111, 16))

        self.retranslateUi(anaPencere)

        QMetaObject.connectSlotsByName(anaPencere)
    # setupUi

    def retranslateUi(self, anaPencere):
        anaPencere.setWindowTitle(QCoreApplication.translate("anaPencere", u"anaPencere", None))
        self.label.setText(QCoreApplication.translate("anaPencere", u"Restoran Y\u00f6netim Sistemi", None))
        self.lblTarihSaat.setText(QCoreApplication.translate("anaPencere", u"25 Nov 2023 02:40:37", None))
        self.label_3.setText(QCoreApplication.translate("anaPencere", u"Sipari\u015f No.", None))
        self.label_4.setText(QCoreApplication.translate("anaPencere", u"K\u0131zartma", None))
        self.label_5.setText(QCoreApplication.translate("anaPencere", u"\u00d6\u011fle Yeme\u011fi", None))
        self.label_6.setText(QCoreApplication.translate("anaPencere", u"Burger", None))
        self.label_7.setText(QCoreApplication.translate("anaPencere", u"Pizza", None))
        self.label_8.setText(QCoreApplication.translate("anaPencere", u"Cheese burger", None))
        self.label_9.setText(QCoreApplication.translate("anaPencere", u"\u0130\u00e7ecekler", None))
        self.lblSiparisNo.setText(QCoreApplication.translate("anaPencere", u"...", None))
        self.txtKizartma.setText(QCoreApplication.translate("anaPencere", u"0", None))
        self.txtOgle.setText(QCoreApplication.translate("anaPencere", u"0", None))
        self.txtBurger.setText(QCoreApplication.translate("anaPencere", u"0", None))
        self.txtPizza.setText(QCoreApplication.translate("anaPencere", u"0", None))
        self.txtCheeseBurger.setText(QCoreApplication.translate("anaPencere", u"0", None))
        self.txtIcecekler.setText(QCoreApplication.translate("anaPencere", u"0", None))
        self.label_12.setText(QCoreApplication.translate("anaPencere", u"Fiyat", None))
        self.label_13.setText(QCoreApplication.translate("anaPencere", u"Servis Hizmeti", None))
        self.label_14.setText(QCoreApplication.translate("anaPencere", u"%18 KDV", None))
        self.label_15.setText(QCoreApplication.translate("anaPencere", u"Alt Toplam", None))
        self.label_16.setText(QCoreApplication.translate("anaPencere", u"Toplam", None))
        self.btnFiyatlar.setText(QCoreApplication.translate("anaPencere", u"F\u0130YATLAR", None))
        self.btnToplam.setText(QCoreApplication.translate("anaPencere", u"Toplam", None))
        self.btnSifirla.setText(QCoreApplication.translate("anaPencere", u"S\u0131f\u0131rla", None))
        self.btnCikis.setText(QCoreApplication.translate("anaPencere", u"\u00c7\u0131k\u0131\u015f", None))
        self.btn5.setText(QCoreApplication.translate("anaPencere", u"5", None))
        self.btn0.setText(QCoreApplication.translate("anaPencere", u"0", None))
        self.btnC.setText(QCoreApplication.translate("anaPencere", u"c", None))
        self.btn6.setText(QCoreApplication.translate("anaPencere", u"6", None))
        self.btn2.setText(QCoreApplication.translate("anaPencere", u"2", None))
        self.btn8.setText(QCoreApplication.translate("anaPencere", u"8", None))
        self.btn9.setText(QCoreApplication.translate("anaPencere", u"9", None))
        self.btnNokta.setText(QCoreApplication.translate("anaPencere", u".", None))
        self.btn1.setText(QCoreApplication.translate("anaPencere", u"1", None))
        self.btn4.setText(QCoreApplication.translate("anaPencere", u"4", None))
        self.btn3.setText(QCoreApplication.translate("anaPencere", u"3", None))
        self.btnTopla.setText(QCoreApplication.translate("anaPencere", u"+", None))
        self.btnCikar.setText(QCoreApplication.translate("anaPencere", u"-", None))
        self.btnCarp.setText(QCoreApplication.translate("anaPencere", u"*", None))
        self.btnBol.setText(QCoreApplication.translate("anaPencere", u"/", None))
        self.btnEsittir.setText(QCoreApplication.translate("anaPencere", u"=", None))
        self.txtHesapMakinesiEkran.setText("")
        self.btn7.setText(QCoreApplication.translate("anaPencere", u"7", None))
        self.label_2.setText(QCoreApplication.translate("anaPencere", u"o\u011fuz han duran :)", None))
    # retranslateUi

