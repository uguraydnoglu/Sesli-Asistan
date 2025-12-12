import random # rastgele işlemleri için
import time # Zaman işlemleri
from playsound import playsound # Ses dosyası oynatma
import speech_recognition as sr # Speech to text
from gtts import gTTS # Google text to speech kütüphanesi
import os # Dosya işlemleri
from datetime import datetime # Tarih işlemleri için
import webbrowser # Arama işlemleri için


r=sr.Recognizer() # speech_recognition için recognizer nesnesi tanımlama

class SesliAsistan():

    # Asistanın Konuşmasını Sağlayan Fonksiyon
    def yanit(kisi,metin):
        tts = gTTS(text=metin, lang="tr")
        sesDosyasi = "asistan.mp3"
        tts.save(sesDosyasi) # Dosyayı kaydetme
        playsound(sesDosyasi) # Ses Dosyayı oynatma
        os.remove(sesDosyasi) # Dosyayı silme

    def ses_kayit(kisi):
        with sr.Microphone() as kaynak: #  Giriş kaynağı olarak mikrofon kullanımı
            r.adjust_for_ambient_noise(kaynak, duration= 0.5) # Mikrofon ses optimizasyonu işlemi
            print("Asistan: Sizi dinliyorum...")
            listen=r.listen(kaynak) # Kullanıcı girişini alma
            voice=" "
            try:
                voice=r.recognize_google(listen,language="tr-TR") # Google ile sesi metine çevirme
            except sr.UnknownValueError:
                kisi.yanit("Ne söylediğinizi anlayamadım. Lütfen tekrar ediniz.")
                print("Asistan: Ne söylediğinizi anlayamadım. Lütfen tekrar ediniz.")
            except sr.RequestError:
                kisi.yanit("Asistan: Sistem çalışmıyor")
                print("Asistan: Sistem çalışmıyor")
            return voice

    def gelen_ses(kisi,söylenen_ses):
            if "merhaba" in söylenen_ses or "selamlar" in söylenen_ses:
                print(söylenen_ses)
                kisi.yanit("Size de selamlar")
                print("Asistan: Size de selamlar")
            elif "nasılsın" in söylenen_ses:
                print(söylenen_ses)
                kisi.yanit("iyiyim sen nasılsın")
                print("Asistan: iyiyim sen nasılsın")
            elif "nasıl gidiyor" in söylenen_ses:
                print(söylenen_ses)
                kisi.yanit("iyi senin?")
                print("Asistan: iyi senin?")
            elif "teşekkür ederim" in söylenen_ses or "teşekkürler" in söylenen_ses:
                print(söylenen_ses)
                kisi.yanit("rica ederim")
                print("Asistan: rica ederim?")
            elif "görüşürüz" in söylenen_ses:
                print(söylenen_ses)
                kisi.yanit("görüşürüz")
                print("Asistan: görüşürüz")
                playsound("kapat.mp3") # Kapanış sesi
                exit() # Uygulamanın kapatılması için kullanılan

            if "not et" in söylenen_ses:
                kisi.yanit("Dosya ismi ne olsun?")
                print("Asistan: Dosya ismi ne olsun?")
                txtDosya = asistan.ses_kayit() + ".txt" # Kayıt edilecek notun adını belirleme
                kisi.yanit("Ne kaydetmek istiyorsun?")
                print("Asistan: Ne kaydetmek istiyorsun?")
                yazi = asistan.ses_kayit() # Kayıt edilecek notun not defterine yazılması işlemi
                n = open(txtDosya, "w", encoding="utf-8")
                n.writelines(yazi) 
                kisi.yanit("Notunuz kaydedildi.")
                print("Asistan: Notunuz kaydedildi.")
                n.close # Kapanma işlemi

            if "günlerden ne" in söylenen_ses:
                gun = time.strftime("%A")
                gun.capitalize()
                if gun == "Monday":
                    gun = "Pazartesi"
                elif gun == "Tuesday":
                    gun = "Salı"
                elif gun == "Wednesday":
                    gun = "Çarşamba"
                elif gun == "Thursday":
                    gun = "Perşembe"
                elif gun == "Friday":
                    gun = "Cuma"
                elif gun == "Saturday":
                    gun = "Cumartesi"
                elif gun == "Sunday":
                    gun = "Pazar"
                kisi.yanit(gun)
                print("Asistan: "+gun)                            

            elif "video aç" in söylenen_ses or "müzik aç" in söylenen_ses:
                try:
                    kisi.yanit("Ne açmamı istersiniz?")
                    print("Asistan: Ne açmamı istersiniz?")
                    veri=kisi.ses_kayit()
                    kisi.yanit("{} açılıyor...".format(veri))
                    time.sleep(1)
                    url="https://www.youtube.com/results?search_query={}".format(veri)
                    webbrowser.get().open(url)
                except:
                    kisi.yanit("internetten kaynaklı bir hata meydana geldi.lütfen internetinizi kontrol ediniz")

            elif "arama yap" in söylenen_ses:
                try:
                    kisi.yanit("Ne aramamı istersiniz")
                    print("Asistan: Ne aramamı istersiniz")
                    veri=kisi.ses_kayit()
                    kisi.yanit("{} için bulduklarım bunlar".format(veri))
                    print("{} için bulduklarım bunlar".format(veri))
                    url="https://www.google.com/search?q={}".format(veri)
                    webbrowser.get().open(url)
                except:
                    kisi.yanit("internetten kaynaklı bir hata meydana geldi.lütfen internetinizi kontrol ediniz")

            if "hava durumu" in söylenen_ses or "hava nasıl" in söylenen_ses or "hava kaç derece" in söylenen_ses:
                kisi.yanit ("hangi şehrin hava durumunu öğrenmek istersiniz ? ")
                print("Asistan: hangi şehrin hava durumunu öğrenmek istersiniz ?")   
                search = asistan.ses_kayit()
                url = "https://mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={}".format(search)
                webbrowser.get().open(url)
                kisi.yanit (" {} için hava durumu verilerini açıyorum".format(search))
                print("{} için hava durumu verilerini açıyorum".format(search))         

            if "saat kaç" in söylenen_ses:
                selection = ["Saat şu an: ", "Hemen Bakıyorum: Saat ", "Saat:"]
                clock = datetime.now().strftime("%H:%M")
                selection = random.choice(selection)
                kisi.yanit(selection + clock)
                print(selection + clock)      

asistan=SesliAsistan() #SesliAsistan classının özelliklerini alma

def uyanma_fonksiyonu(metin): # Asistanın çağırılması işlemi
    if(metin=="hey asistan" or metin=="asistan"):
        playsound("dinleme.mp3") # Dinleme sesi
        asistan.yanit("Dinliyorum...")
        cevap=asistan.ses_kayit()
        if(cevap!=""):
            asistan.gelen_ses(cevap)

playsound("basla.mp3") # Başlangıç Sesi

time.sleep(1) # Bekleme süresi
while True:
    ses=asistan.ses_kayit()# Ses girişini alma
    if(ses!=" "):
        ses=ses.lower()
        print(ses)
        uyanma_fonksiyonu(ses)#Cevaplama işlemi