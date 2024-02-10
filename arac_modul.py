import time
import random
import sqlite3
import os
import requests
from bs4 import BeautifulStoneSoup
import urllib.request
import json
import signal
#veri alma sınıfı

class lib():
    def __init__(self,url,url1,url2,url3):
        self.url=url
        self.url1=url1
        self.url2=url2
        self.url3=url3

    def link_al(self):
        print("Birinci Url'yi Girin:")
        self.url1=input(str())
        print("İkinci Url'yi Girin:")
        self.url2=input(str())
        print("Üçüncü Url'yi Gir")
        self.url3=input(str())

    def veri_al(self):
        urllistesi=[self.url1,self.url2,self.url3]
        sayac=1
        for i in urllistesi:
            urllib.request.urlretrieve(self.url,"Nesne",+str(sayac)+"Nesne Özelliği")




#veritabanı özellikleri
class veri_ekle():
    def __init__(self,veritabanı,motor_tipi,ecu_sistem,im):
        self.veritabanı=veritabanı
        self.ecu_sitem=ecu_sistem
        self.im=im

    def baglantı(self):
        self.veritabanı=sqlite3.connect("araclar.db")
        self.im=self.veritabanı.cursor()

    def tabloolustur(self):
        self.im.execute("CREATE TABLE İF NOT EXİST arababilgileri""(motor_tipi,kontrol_tarihi,aracın_markası)""")

    def veri_ekle(self):
        print("Veri Eklemek İçin ")


#Bağlantı Sağlama


class device():
    def __init__(self,tophone,green_dot,connect):
        self.tophone=tophone
        self.green_dot=green_dot
        self.connect=connect


    def connect_kontrol(self,pid):
        self.pid=pid
        i=0
        while(i<10):
            pid=os.fork()
            if self.pid:
                print("\nIn Ana Arama Süreci Başladı")
                os.kill(self.pid, signal.SIGSTOP)
                print("Birinci Süreç Bitirildi...")
            else:
                print("\nIn İkincil Süreç Başladı")
                print("PROCESS ID:", os.getpid())
                print("Aracın Motor Bilgileri Okunuyor.")
















# motor sınıfındaki fonksiyon çalışacak motor tipi mi  söyledi. ardından veri tabanına ekleme yapacak neyi motor tipini

