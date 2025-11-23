# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fiyatlar_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_FiyatlarDialog(object):
    def setupUi(self, FiyatlarDialog):
        if not FiyatlarDialog.objectName():
            FiyatlarDialog.setObjectName(u"FiyatlarDialog")
        FiyatlarDialog.resize(434, 353)
        self.buttonBox = QDialogButtonBox(FiyatlarDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 290, 341, 32))
        font = QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.verticalLayoutWidget = QWidget(FiyatlarDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(90, 30, 113, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.verticalLayoutWidget_2 = QWidget(FiyatlarDialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(200, 20, 121, 251))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.spinKizartma = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.spinKizartma.setObjectName(u"spinKizartma")

        self.verticalLayout_2.addWidget(self.spinKizartma)

        self.spinOgle = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.spinOgle.setObjectName(u"spinOgle")

        self.verticalLayout_2.addWidget(self.spinOgle)

        self.spinBurger = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.spinBurger.setObjectName(u"spinBurger")

        self.verticalLayout_2.addWidget(self.spinBurger)

        self.spinPizza = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.spinPizza.setObjectName(u"spinPizza")

        self.verticalLayout_2.addWidget(self.spinPizza)

        self.spinCheeseBurger = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.spinCheeseBurger.setObjectName(u"spinCheeseBurger")

        self.verticalLayout_2.addWidget(self.spinCheeseBurger)

        self.spinIcecekler = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.spinIcecekler.setObjectName(u"spinIcecekler")

        self.verticalLayout_2.addWidget(self.spinIcecekler)


        self.retranslateUi(FiyatlarDialog)
        self.buttonBox.accepted.connect(FiyatlarDialog.accept)
        self.buttonBox.rejected.connect(FiyatlarDialog.reject)

        QMetaObject.connectSlotsByName(FiyatlarDialog)
    # setupUi

    def retranslateUi(self, FiyatlarDialog):
        FiyatlarDialog.setWindowTitle(QCoreApplication.translate("FiyatlarDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("FiyatlarDialog", u"K\u0131zartma", None))
        self.label_2.setText(QCoreApplication.translate("FiyatlarDialog", u"\u00d6\u011fle Yeme\u011fi", None))
        self.label_3.setText(QCoreApplication.translate("FiyatlarDialog", u"Burger", None))
        self.label_4.setText(QCoreApplication.translate("FiyatlarDialog", u"Pizza", None))
        self.label_5.setText(QCoreApplication.translate("FiyatlarDialog", u"Cheese Burger", None))
        self.label_6.setText(QCoreApplication.translate("FiyatlarDialog", u"\u0130\u00e7ecekler", None))
    # retranslateUi

