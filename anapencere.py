import sys
import random
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (QApplication, QWidget, QDialog, QDialogButtonBox,
                             QVBoxLayout, QFormLayout, QDoubleSpinBox, QMessageBox)


from ui_form import Ui_anaPencere
from ui_fiyatlar_dialog import Ui_FiyatlarDialog


class FiyatPenceresi(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FiyatlarDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Fiyatları Düzenle")

        self.urunler_map = {
            "kizartma": self.ui.spinKizartma,
            "ogle": self.ui.spinOgle,
            "burger": self.ui.spinBurger,
            "pizza": self.ui.spinPizza,
            "cheese_burger": self.ui.spinCheeseBurger,
            "icecekler": self.ui.spinIcecekler
        }

        for spinBox in self.urunler_map.values():
            spinBox.setDecimals(2)
            spinBox.setMinimum(0.0)
            spinBox.setMaximum(9999.99)
            spinBox.setSuffix(" ₺")

    def fiyatlariAyarla(self, mevcut_fiyatlar):
        for anahtar, spinBox in self.urunler_map.items():
            fiyat = mevcut_fiyatlar.get(anahtar, Decimal("0.0"))
            spinBox.setValue(float(fiyat))

    def guncelFiyatlariAl(self):
        yeni_fiyatlar = {}
        for anahtar, spinBox in self.urunler_map.items():
            yeni_fiyatlar[anahtar] = Decimal(str(spinBox.value()))
        return yeni_fiyatlar


class anaPencere(QWidget):
    SERVIS_ORANI = Decimal("0.08")
    KDV_ORANI = Decimal("0.18")
    FIYAT_DOSYASI = "fiyat.inf"
    SATIS_DOSYASI = "satis.txt"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_anaPencere()
        self.ui.setupUi(self)

        self.setWindowTitle("Restaurant Yönetim Sistemi")
        self.fiyat_listesi = {}
        self.calc_sayi1 = ""
        self.calc_islem = ""
        self.calc_yeni_sayi_girilmeli = True


        self.fiyatlariYukle()
        self.sinyalleriBagla()
        self.zamanlayiciyiBaslat()
        self.sifirla()

    def sinyalleriBagla(self):
        self.ui.btnToplam.clicked.connect(self.hesapla)
        self.ui.btnSifirla.clicked.connect(self.sifirla)
        self.ui.btnCikis.clicked.connect(self.close)
        self.ui.btnFiyatlar.clicked.connect(self.fiyatPenceresiniAc)

        self.ui.btn0.clicked.connect(lambda: self.calcRakamBas("0"))
        self.ui.btn1.clicked.connect(lambda: self.calcRakamBas("1"))
        self.ui.btn2.clicked.connect(lambda: self.calcRakamBas("2"))
        self.ui.btn3.clicked.connect(lambda: self.calcRakamBas("3"))
        self.ui.btn4.clicked.connect(lambda: self.calcRakamBas("4"))
        self.ui.btn5.clicked.connect(lambda: self.calcRakamBas("5"))
        self.ui.btn6.clicked.connect(lambda: self.calcRakamBas("6"))
        self.ui.btn7.clicked.connect(lambda: self.calcRakamBas("7"))
        self.ui.btn8.clicked.connect(lambda: self.calcRakamBas("8"))
        self.ui.btn9.clicked.connect(lambda: self.calcRakamBas("9"))
        self.ui.btnNokta.clicked.connect(lambda: self.calcRakamBas("."))

        self.ui.btnTopla.clicked.connect(lambda: self.calcIslemBas("+"))
        self.ui.btnCikar.clicked.connect(lambda: self.calcIslemBas("-"))
        self.ui.btnCarp.clicked.connect(lambda: self.calcIslemBas("*"))
        self.ui.btnBol.clicked.connect(lambda: self.calcIslemBas("/"))

        self.ui.btnC.clicked.connect(self.calcTemizle)
        self.ui.btnEsittir.clicked.connect(self.calcEsittir)

    def zamanlayiciyiBaslat(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.saatiGuncelle)
        self.timer.start(1000)
        self.saatiGuncelle()

    def saatiGuncelle(self):
        simdi = datetime.now()
        formatli_tarih = simdi.strftime('%d %b %Y %H:%M:%S')
        try:
            self.ui.lblTarihSaat.setText(formatli_tarih)
        except AttributeError:
            pass

    def fiyatlariYukle(self):
        varsayilan_fiyatlar = {
            "kizartma": Decimal("50.00"),
            "ogle": Decimal("120.00"),
            "burger": Decimal("90.00"),
            "pizza": Decimal("150.00"),
            "cheese_burger": Decimal("100.00"),
            "icecekler": Decimal("30.00")
        }
        try:
            with open(self.FIYAT_DOSYASI, "r") as f:
                satirlar = f.readlines()
                if len(satirlar) == len(varsayilan_fiyatlar):
                    for satir in satirlar:
                        anahtar, fiyat = satir.strip().split("=")
                        self.fiyat_listesi[anahtar] = Decimal(fiyat)
                else:
                    raise FileNotFoundError
        except (FileNotFoundError, ValueError, IndexError):
            self.fiyat_listesi = varsayilan_fiyatlar
            self.fiyatlariDosyayaKaydet(varsayilan_fiyatlar)

    def fiyatlariDosyayaKaydet(self, fiyat_listesi):
        try:
            with open(self.FIYAT_DOSYASI, "w") as f:
                for anahtar, fiyat in fiyat_listesi.items():
                    f.write(f"{anahtar}={fiyat}\n")
        except Exception as e:
            QMessageBox.warning(self, "Dosya Hatası", f"Fiyatlar kaydedilemedi tüh : {e}")

    def fiyatPenceresiniAc(self):
        dialog = FiyatPenceresi(self)
        dialog.fiyatlariAyarla(self.fiyat_listesi)

        if dialog.exec() == QDialog.Accepted:
            yeni_fiyatlar = dialog.guncelFiyatlariAl()
            self.fiyatlariDosyayaKaydet(yeni_fiyatlar)
            self.fiyatlariYukle()
            QMessageBox.information(self, "Başarılı", "Fiyatlar güncellendi süpersin :) ")

    def _get_decimal_from_lineedit(self, line_edit):

        text = line_edit.text().strip()
        if not text:
            return Decimal("0")
        try:
            return Decimal(text)
        except Exception:
            return Decimal("0")

    def hesapla(self):
        try:
            siparis_no = random.randint(10000, 99999)
            self.ui.lblSiparisNo.setText(str(siparis_no))

            adet_kizartma = self._get_decimal_from_lineedit(self.ui.txtKizartma)
            adet_ogle = self._get_decimal_from_lineedit(self.ui.txtOgle)
            adet_burger = self._get_decimal_from_lineedit(self.ui.txtBurger)
            adet_pizza = self._get_decimal_from_lineedit(self.ui.txtPizza)
            adet_cheese = self._get_decimal_from_lineedit(self.ui.txtCheeseBurger)
            adet_icecek = self._get_decimal_from_lineedit(self.ui.txtIcecekler)

            fiyat = (
                (adet_kizartma * self.fiyat_listesi["kizartma"]) +
                (adet_ogle * self.fiyat_listesi["ogle"]) +
                (adet_burger * self.fiyat_listesi["burger"]) +
                (adet_pizza * self.fiyat_listesi["pizza"]) +
                (adet_cheese * self.fiyat_listesi["cheese_burger"]) +
                (adet_icecek * self.fiyat_listesi["icecekler"])
            )

            servis_hizmeti = fiyat * self.SERVIS_ORANI
            alt_toplam = fiyat + servis_hizmeti
            kdv = alt_toplam * self.KDV_ORANI
            toplam = alt_toplam + kdv
            fiyat = fiyat.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            servis_hizmeti = servis_hizmeti.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            alt_toplam = alt_toplam.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            kdv = kdv.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            toplam = toplam.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

            self.ui.txtFiyat.setText(f"₺{fiyat}")
            self.ui.txtServisHizmeti.setText(f"₺{servis_hizmeti}")
            self.ui.txtAltToplam.setText(f"₺{alt_toplam}")
            self.ui.txtKDV.setText(f"₺{kdv}")
            self.ui.txtToplam.setText(f"₺{toplam}")
            self.satisKaydet(siparis_no, toplam)

        except Exception as e:
            QMessageBox.critical(self, "Hesaplama Hatası", f"hata oluştu: {e}")

    def satisKaydet(self, siparis_no, toplam_tutar):
        try:
            with open(self.SATIS_DOSYASI, "a", encoding="utf-8") as f:
                tarih_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log = (f"Sipariş No: {siparis_no}, "
                       f"Tutar: ₺{toplam_tutar}, "
                       f"Tarih: {tarih_str}\n")
                f.write(log)
        except Exception as e:
            QMessageBox.warning(self, "Kayıt Hatası", f"satış kaydı yapılamadı :( : {e}")

    def sifirla(self):
        self.ui.txtKizartma.setText("0")
        self.ui.txtOgle.setText("0")
        self.ui.txtBurger.setText("0")
        self.ui.txtPizza.setText("0")
        self.ui.txtCheeseBurger.setText("0")
        self.ui.txtIcecekler.setText("0")
        self.ui.txtFiyat.clear()
        self.ui.txtServisHizmeti.clear()
        self.ui.txtAltToplam.clear()
        self.ui.txtKDV.clear()
        self.ui.txtToplam.clear()
        self.ui.lblSiparisNo.setText("...")
        self.calcTemizle()



    def calcRakamBas(self, rakam):

        if self.calc_yeni_sayi_girilmeli:
            self.ui.txtHesapMakinesiEkran.setText(rakam)
            self.calc_yeni_sayi_girilmeli = False
        else:
            if rakam == "." and "." in self.ui.txtHesapMakinesiEkran.text():
                return
            self.ui.txtHesapMakinesiEkran.setText(self.ui.txtHesapMakinesiEkran.text() + rakam)

    def calcIslemBas(self, islem):

        if not self.ui.txtHesapMakinesiEkran.text():
            return

        self.calc_sayi1 = self.ui.txtHesapMakinesiEkran.text()
        self.calc_islem = islem
        self.calc_yeni_sayi_girilmeli = True

    def calcTemizle(self):
        self.ui.txtHesapMakinesiEkran.clear()
        self.calc_sayi1 = ""
        self.calc_islem = ""
        self.calc_yeni_sayi_girilmeli = True

    def calcEsittir(self):

        if not self.calc_sayi1 or not self.calc_islem or self.calc_yeni_sayi_girilmeli:
            return

        try:
            sayi1 = Decimal(self.calc_sayi1)
            sayi2 = Decimal(self.ui.txtHesapMakinesiEkran.text())
            sonuc = Decimal("0")

            if self.calc_islem == "+":
                sonuc = sayi1 + sayi2
            elif self.calc_islem == "-":
                sonuc = sayi1 - sayi2
            elif self.calc_islem == "*":
                sonuc = sayi1 * sayi2
            elif self.calc_islem == "/":
                if sayi2 == Decimal("0"):
                    self.ui.txtHesapMakinesiEkran.setText("Hata: 0'a bölünmez ????")
                    self.calc_yeni_sayi_girilmeli = True
                    return
                sonuc = sayi1 / sayi2


            sonuc = sonuc.quantize(Decimal("0.00000001"), rounding=ROUND_HALF_UP).normalize()
            self.ui.txtHesapMakinesiEkran.setText(str(sonuc))

        except Exception as e:
            self.ui.txtHesapMakinesiEkran.setText("Hata")


        self.calc_sayi1 = ""
        self.calc_islem = ""
        self.calc_yeni_sayi_girilmeli = True



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = anaPencere()
    widget.show()
    sys.exit(app.exec())
