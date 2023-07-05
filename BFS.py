from queue import Queue

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import QPixmap
from threading import Thread

import cv2
import time
import random

'''
def olustur_graf_1():
    graf = {}
    graf["A"] = ["B"]
    graf["B"] = ["A","C","F"]
    graf["C"] = ["B","D"]
    graf["F"] = ["B","E"]
    graf["D"] = ["C","E","G"]
    graf["E"] = ["D","F","H"]
    graf["G"] = ["D","H"]
    graf["H"]  = ["G","E","J"]
    graf["J"] = ["H"]

    return graf

def olustur_gorsel_lokasyon_dugum_1():
    konumlar = {}
    konumlar["A"] = (400,450)
    konumlar["B"] = (350,250)
    konumlar["C"] = (400,100)
    konumlar["F"] = (450,300)
    konumlar["E"] = (600,250)
    konumlar["D"] = (500,100)
    konumlar["G"] = (650,150)
    konumlar["H"] = (750,200)
    konumlar["J"] = (800,300)
    return konumlar

def olustur_graf_2():
    graf = {}
    graf["A"] = ["B"]
    graf["B"] = ["A","C","F"]
    graf["C"] = ["B","D"]
    graf["F"] = ["B","E"]
    graf["E"] = ["D","F"]
    graf["D"] = ["C","E"]

    return graf

def olustur_gorsel_lokasyon_dugum_2():
    konumlar = {}
    konumlar["A"] = (400,450)
    konumlar["B"] = (350,250)
    konumlar["C"] = (400,100)
    konumlar["F"] = (450,300)
    konumlar["E"] = (600,250)
    konumlar["D"] = (500,100)

    return konumlar
'''
def olustur_graf_3():
    graf = {}
    
    graf["A"] = ["B","D","G","J","K"]
    graf["B"] = ["A","C","J","P","R"]
    graf["C"] = ["B","D","E","S"]
    graf["D"] = ["C","A","E","H"]
    graf["E"] = ["D","F","C","I"]
    graf["F"] = ["E","G","H"]
    graf["G"] = ["F","A","K"]    
    graf["H"] = ["D","F","I"]
    graf["I"] = ["E","H","S"]
    graf["J"] = ["A","B","K","L"]
    graf["K"] = ["A","J","G","O"]
    graf["L"] = ["J","M","O","P"]    
    graf["M"] = ["L","N"]    
    graf["N"] = ["M","O"]  
    graf["O"] = ["N","K","L","P"]
    graf["P"] = ["O","L","B","R"]
    graf["R"] = ["P","B","S"]
    graf["S"] = ["C","I","R"]







    return graf

def olustur_gorsel_lokasyon_dugum_3():
    konumlar = {}
    
    konumlar["A"] = (600,350)
    konumlar["B"] = (550,250)
    konumlar["C"] = (500,300)
    konumlar["D"] = (475,425)
    konumlar["E"] = (425,250)
    konumlar["F"] = (350,375)
    konumlar["G"] = (575,525)
    konumlar["H"] = (200,525)
    konumlar["I"] = (225,225)
    konumlar["J"] = (700,300)
    konumlar["K"] = (750,475)
    konumlar["L"] = (800,275)    
    konumlar["M"] = (850,350)    
    konumlar["N"] = (900,350)    
    konumlar["O"] = (1100,375)    
    konumlar["P"] = (925,225)      
    konumlar["R"] = (750,175)
    konumlar["S"] = (550,125)   

    return konumlar











##DÜĞÜMLERDEN , KOMUŞULUKLARINDAN VE LOKASYONLARINDAN KENARLARI OLUŞTUR
def olustur_gorsel_lokasyon_kenar(graf,konumlar):
    keys = graf.keys()
    kenarlar = {}
    for key in keys:
        for row_values in graf[key]:
            for value in row_values:
                #print(key," ",value," ",konumlar[key]," ",konumlar[value])
                
                temp= f"{key}-{value}"
                kenarlar[temp] = (konumlar[key],konumlar[value])
    return kenarlar
                

graf = olustur_graf_3()                                                                                         
dugumlar_konumlar = olustur_gorsel_lokasyon_dugum_3()
kenarlar_konumlar = olustur_gorsel_lokasyon_kenar(graf,dugumlar_konumlar)
print("düğüm sayısı : ",len(dugumlar_konumlar))
print("kenar sayısı : ",len(kenarlar_konumlar))
#%%gui
class BFS_gui(QWidget):
    
    ##KENARLARI VE DÜĞÜMLERİ AL VE ÇİZ ARDINDAN ARAMAYA BAŞLA
    def __init__(self,konumlar,kenarlar):
        QWidget.__init__(self)
        self.save_sayac = 10
        self.konumlar = konumlar
        self.kenarlar = kenarlar
        self.olustur_ekran()
        self.ciz_baglantilar()
        
        self.arama_thread()
        

        
    ##pyqt5 EKRANI OLUŞTUR
    def olustur_ekran(self):
        pixmap = QPixmap("harita.jpg")
        self.ekran = QLabel()
        self.ekran.setPixmap(pixmap)
        
        layout = QGridLayout()
        layout.addWidget(self.ekran)
        self.setLayout(layout)
        self.setWindowTitle("Harita")
        self.resize(1200,700)
    
    ##KENAR VE DÜĞÜMLERİ ÇİZ
    def ciz_baglantilar(self):
        image = cv2.imread("harita.jpg")
        image = self.ciz_kenar(image)
        image = self.ciz_dugum(image)
        cv2.imwrite("guncel_harita.jpg",image)
        image = QPixmap("guncel_harita.jpg")
        self.ekran.setPixmap(image)
        
    ##KENARLARI ÇİZ
    def ciz_kenar(self,image):
        
        renk = (95,95,95)
        kalinlik = 2
        
        for key in self.kenarlar.keys():
            baslangic_konum = self.kenarlar[key][0]
            bitis_konum = self.kenarlar[key][1]
            cv2.line(image, baslangic_konum , bitis_konum , renk , kalinlik) 
        return image
    
    #DÜĞÜMLERİ ÇİZ
    def ciz_dugum(self,image):
        renk = (0,0,0)
        kalinlik = -1
        yaricap = 20
        
        for key in self.konumlar.keys():
            konum = self.konumlar[key]
            cv2.circle(image, konum, yaricap, renk,kalinlik)
            cv2.putText(image,key,(konum[0]-10,konum[1]-30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA) 
        return image
    
    #SONUC SÖZLĞÜNDEN PARENT VE CHİLDİN KONUMLARINI ÇEK VE ONA GÖRE EKRANI TEKRARDAN ÇİZ . (SONUC SÖZLÜĞÜ A'NIN KİME KAÇ KENAR YAKIN OLDUGUNU SIRA SIRA TUTAR)
    def ciz(self,parent,child,sonuc,renk_='yesil'):
        if renk_ == 'yesil':
            renk = (80,255,50)
        elif renk_ == 'kirmizi':
            renk = (49,49,255)
        kalinlik = 2
        
        elem = f"{parent}-{child}"
        baslangic_konum = self.kenarlar[elem][0]
        bitis_konum = self.kenarlar[elem][1]
        
        image = cv2.imread("guncel_harita.jpg")
        cv2.line(image, baslangic_konum , bitis_konum , renk , kalinlik) 
        cv2.putText(image,str(sonuc[child]),(bitis_konum[0]+20,bitis_konum[1]+20),cv2.FONT_HERSHEY_SIMPLEX,1,(80,255,50),2,cv2.LINE_AA) 
        
        cv2.imwrite("guncel_harita.jpg",image)
        cv2.imwrite(f"gif_im_{self.save_sayac}.jpg",image)   # gidişatı görsel olarak kaydetmek için
        self.save_sayac += 1
        pixmap = QPixmap("guncel_harita.jpg")
        time.sleep(1)
        self.ekran.setPixmap(pixmap)
    
    #ARAMA FONKSİYONUNU FARKLI BİR THREAD İLE BAŞLAT
    def arama_thread(self):
        t1 = Thread(target=self.arama)
        t1.start()
        


    #YOL ARAMA FONKSİYONU
    #ARAMA FONKSİYONU GRAFTA TUTULAN PARENTIN CHILDLARININ SIRASINA GÖRE HAREKET EDER
    def arama(self):
        baslangic_dugum = "A"
        hedef_dugum = "I"
        
        ##HEDEF - BASLANGİC KONUM BİLGİSİNİ EKRANA YAZDIR
        image = cv2.imread("guncel_harita.jpg")
        cv2.putText(image,f"BASLANGIC : {baslangic_dugum}",(900,550),cv2.FONT_HERSHEY_SIMPLEX,1,(49,49,255),2,cv2.LINE_AA) 
        cv2.putText(image,F"HEDEF : {hedef_dugum}",(900,600),cv2.FONT_HERSHEY_SIMPLEX,1,(49,40,255),2,cv2.LINE_AA)     
        cv2.imwrite("guncel_harita.jpg",image)
        
        
        
        kullanılanlar = []
        self.sonuc = {}
        self.yol = {} # 'X DÜĞÜMÜ', ['X düğümünün parent'ı',X düğümünün parentında kaçıncı indekste olduğu bilgisi]
        q = Queue()
        
        
        self.sonuc["A"] = 0
        q.put("A")
        kullanılanlar.append("A")
        
        for i in range(len(graf)):
            next_parent = q.get()
            print(self.sonuc)
            for num , child in enumerate(graf[next_parent]):
                
                if child not in kullanılanlar:
                    
                    #print(child)
                    self.sonuc[child] = self.sonuc[next_parent] +1
                    self.yol[child] = [next_parent,num]     
                    
                    kullanılanlar.append(child)
                    q.put(child)
                    self.ciz(next_parent,child,self.sonuc)
                    if child == hedef_dugum:
                        self.ciz_en_iyi_yol(hedef_dugum)
                else:
                    #print("Already have")
                    continue


        print("SONUC \n",self.sonuc)
        print("YOL \n",self.yol)
        
    
    ##HEDEF BULUNDUGUNDA GERİYE GOĞRU ÇİZİM YAP
    def ciz_en_iyi_yol(self,hedef_dugum):
    
           
        print("hedefe en yakın uzaklık : ",self.sonuc[hedef_dugum])
        
        time.sleep(1.5)
        
        for i in range(self.sonuc[hedef_dugum]):
            parent,index = self.yol[hedef_dugum]
            self.ciz(parent,hedef_dugum,self.sonuc,'kirmizi')
            print(f"{hedef_dugum}-> {parent}")
            hedef_dugum = parent
        
app = QApplication([])
widget = BFS_gui(dugumlar_konumlar,kenarlar_konumlar)
widget.show()
app.exec_()
        

#%%search
"""
    #YOL ARAMA FONKSİYONU
    def arama(self):
        
        kullanılanlar = []
        sonuc = {}
        q = Queue()
        
        
        sonuc["A"] = 0
        q.put("A")
        kullanılanlar.append("A")
        
        for i in range(len(graf)):
            next_parent = q.get()
            print(sonuc)
            for child in graf[next_parent]:
                
                if child not in kullanılanlar:
                    
                    #print(child)
                    sonuc[child] = sonuc[next_parent] +1
                    kullanılanlar.append(child)
                    q.put(child)
                    self.ciz(next_parent,child,sonuc)
                else:
                    #print("Already have")
                    continue
        
        print(sonuc)
        
"""