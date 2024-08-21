import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# -----------------------------Sayaçın fonksiyonları--------------------------
#-----------------------------------------------------------------------------
def baslatici():
    global sayac_baslat
    global toplam_saniye
    
    saat_tosaniye = int(comboboxsaat.get()) * 3600
    dakika_tosaniye = int(comboboxdakika.get()) * 60
    saniye = int(comboboxsaniye.get())
    
    sayac_baslat = True  
    toplam_saniye = (saat_tosaniye+dakika_tosaniye+saniye) 
    
    sayac_fonksiyonu()
    
def sayac_sifirla():
    global sayac_baslat
    
    sayac_baslat = False
    
    sayac_etiketi_saat.config(text=f"00")
    sayac_etiketi_dakika.config(text=f"00")
    sayac_etiketi_saniye.config(text=f"00")
    
    
def sayac_fonksiyonu():
    
    global toplam_saniye
    
    if sayac_baslat == True:
    
        if toplam_saniye != 0:
                
            toplam_saniye -= 1
                
            saat, kalan = divmod(toplam_saniye,3600)
            dakika, saniye = divmod(kalan,60)
                
            sayac_etiketi_saat.config(text=f"{saat:02d}")
            sayac_etiketi_dakika.config(text=f"{dakika:02d}")
            sayac_etiketi_saniye.config(text=f"{saniye:02d}")
            
            sayac_etiketi_saniye.after(1000,sayac_fonksiyonu) # Window.after da olabiir
        
        else:
            sayac_etiketi_saat.config(text=f"-")
            sayac_etiketi_dakika.config(text=f"-")
            sayac_etiketi_saniye.config(text=f"-")

            messagebox.showinfo("Zaman Doldu", "Sayaç bitti!")

            
            
        # Buraya alarm kurabilirsin
        
        # Bu degerleri bu fonksiyon içinde alsaydık sürekli bu fonksiyon döndüğü için
        # Enrtyden get ile gelicek değerlerin hala bitmediğini sanacaktı ve süre başlamayacaktı
        # Bu yüzden bir üst fonksiyonda değerleri aldık

saniyeler = [f"{i:02d}" for i in range(0,60)]  
dakikalar = [f"{i:02d}" for i in range(0,60)] 
saatler = [f"{i:02d}" for i in range(0,24)]       


# ---------------------------Saatin fonksiyonları-----------------------------
#-----------------------------------------------------------------------------
def saatin_zaman_fonksiyonu():
    """
    Etiketin textini config ettikten 1000 milisaniye sonra fonksiyonu çalistir ve
    bu sonsuz döngü yaratir
        
    """
    zaman = time.strftime("%H : %M : %S")
    saat_etiketi.config(text=zaman)
    saat_etiketi.after(1000,saatin_zaman_fonksiyonu)
    
    
# ---------------------------Kronometrenin fonksiyonları-----------------------------
#----------------------------------------------------------------------------------- 
zaman_saniye = 0
def kronometre_fonksiyonu():
    global zaman_saniye # Global önemli
    
    saat, kalan = divmod(zaman_saniye,3600)
    dakika, saniye = divmod(kalan,60)
    
    kronometre_etiketi.config(text=f"{saat:02d}:{dakika:02d}:{saniye:02d}")
    
    if baslat == True:
        zaman_saniye+=1
    
    kronometre_etiketi.after(1000,kronometre_fonksiyonu)    

def baslat():
    global baslat
    baslat = True

def durdur():
    global baslat
    baslat = False
    
def sifirla():
    global zaman_saniye
    zaman_saniye = 0
    
    kronometre_etiketi.config(text=f"00:00:00")
    
#---------------------------------------------------------------------------------  

# Pencere
window = tk.Tk()
canvas = tk.Canvas(master=window)
canvas.pack()

# Pencere özellikleri
canvas.configure(height=600, width=800, bg="#2a53a1")
window.title("Dijital Saat")
window.resizable(False,False)
window.iconbitmap(default="saatikon.ico")


# -----------------------saat--------------------------------

# Saat ve saat başlığının bulunuduğu etiketler

saat_etiketi = tk.Label(master=window, fg="#054f54", font=("arial.ttf",80,"bold"), bg="#c9fbff", relief=tk.SUNKEN,bd=30)
saat_yazisi_etiketi = tk.Label(master=window, fg="white", font=("arial.ttf",25,"bold"), bg="gray", text="GÜNCEL  SAAT",relief=tk.SUNKEN,bd=1)
canvas.create_window(400, 20,window=saat_yazisi_etiketi, height=60, width=800)
canvas.create_window(400,130,window=saat_etiketi, height=160, width=800)

# -----------------kronometre-----------------------

kronometre_yazisi_etiketi = tk.Label(master=window, fg="white", font=("arial.ttf",25,"bold"), bg="gray", text="Kronometre",relief=tk.SUNKEN,bd=2)
kronometre_arka_fonu = tk.Label(master=window, bg="#286665",relief=tk.SUNKEN,bd=2)
canvas.create_window(200,240,window=kronometre_yazisi_etiketi,height=60,width=400)
canvas.create_window(200,450,window=kronometre_arka_fonu,height=360,width=400)

kronometre_etiketi = tk.Label(master=window, fg="#054f54", font=("arial.ttf",40,"bold"), bg="#c9fbff",relief=tk.SUNKEN,bd=10)
canvas.create_window(200,350,window=kronometre_etiketi, height=100,width=350)

kronometre_baslat_tusu = tk.Button(master=window,height=3, width=12,bd=5,text="Başlat", command=baslat, bg="#c9fbff",activebackground="#054f54", activeforeground="#c9fbff", font=("arial.ttf",9,"bold"))
kronometre_durdur_tusu = tk.Button(master=window,height=3, width=12,bd=5,text="Durdur", command=durdur, bg="#c9fbff",activebackground="#054f54" , activeforeground="#c9fbff", font=("arial.ttf",9,"bold"))
kronometre_sifirla_tusu = tk.Button(master=window,height=3, width=12,bd=5,text="Sıfırla", command=sifirla, bg="#c9fbff",activebackground="#054f54", activeforeground="#c9fbff", font=("arial.ttf",9,"bold"))
canvas.create_window(100,480, window=kronometre_baslat_tusu)
canvas.create_window(210,480, window=kronometre_durdur_tusu)
canvas.create_window(320,480, window=kronometre_sifirla_tusu)

# ---------------------------Sayaç----------------------------------------

sayac_yazisi_etiketi = tk.Label(master=window, fg="white", font=("arial.ttf",25,"bold"), bg="gray", text="Sayaç",relief=tk.SUNKEN,bd=2)
sayac_arka_fonu = tk.Label(master=window, bg="#286665",relief=tk.SUNKEN,bd=2)
canvas.create_window(600,450,window=sayac_arka_fonu,height=360,width=400)
canvas.create_window(600,240,window=sayac_yazisi_etiketi,height=60,width=400)

sayac_etiketi_arka_fonu = tk.Label(master=window, fg="#054f54", font=("arial.ttf",10,"bold"), bg="#c9fbff",relief=tk.SUNKEN,bd=10)
canvas.create_window(600, 350, window=sayac_etiketi_arka_fonu, height=100, width=350)

sayac_etiketi_saat = tk.Label(master=window, fg="#054f54", font=("arial.ttf",40,"bold"), bg="#c9fbff", text="00")
sayac_etiketi_dakika = tk.Label(master=window, fg="#054f54", font=("arial.ttf",40,"bold"), bg="#c9fbff", text="00")
sayac_etiketi_saniye = tk.Label(master=window, fg="#054f54", font=("arial.ttf",40,"bold"), bg="#c9fbff", text="00")
canvas.create_window(490, 350, window=sayac_etiketi_saat, height=90, width=118)
canvas.create_window(600, 350, window=sayac_etiketi_dakika, height=90, width=118)
canvas.create_window(710, 350, window=sayac_etiketi_saniye, height=90, width=118)


comboboxsaat = ttk.Combobox(master = window, width=10, font=("arial.ttf",9,"bold"), values=saatler)
comboboxdakika = ttk.Combobox(master = window, width=10, font=("arial.ttf",9,"bold"),values=dakikalar, background="#c9fbff")
comboboxsaniye = ttk.Combobox(master = window, width=10,  font=("arial.ttf",9,"bold"),values=saniyeler,  background="#c9fbff")
canvas.create_window(500,440, window=comboboxsaat)
canvas.create_window(600,440, window=comboboxdakika)
canvas.create_window(700,440, window=comboboxsaniye)


kalan_saat_yazisi_etiketi = tk.Label(master=window,font=("arial.ttf",9,"bold"), text="Saat", bg="gray",width=15,bd=1,fg="white",relief=tk.SUNKEN)
kalan_dakika_yazisi_etiketi = tk.Label(master=window,font=("arial.ttf",9,"bold"), text="Dakika", bg="gray",width=15,bd=1,fg="white" ,relief=tk.SUNKEN)
kalan_saniye_yazisi_etiketi = tk.Label(master=window,font=("arial.ttf",9,"bold"), text="Saniye", bg="gray",width=15 ,bd=1,fg="white",relief=tk.SUNKEN)
canvas.create_window(500,415, window=kalan_saat_yazisi_etiketi)
canvas.create_window(600,415, window=kalan_dakika_yazisi_etiketi)
canvas.create_window(700,415, window=kalan_saniye_yazisi_etiketi)


sayac_baslat_butonu = tk.Button(master=window, text="Başlat", command= baslatici,height=3, width=12, font=("arial.ttf",9,"bold"),bd=5,bg="#c9fbff",activebackground="#054f54", activeforeground="#c9fbff")
canvas.create_window(530, 500, window=sayac_baslat_butonu)

sayac_sifirla_butonu = tk.Button(master=window, text="Sıfırla", command= sayac_sifirla, height=3, width=12, font=("arial.ttf",9,"bold"), bd = 5,bg="#c9fbff",activebackground="#054f54", activeforeground="#c9fbff")
canvas.create_window(660, 500, window=sayac_sifirla_butonu)


# Çalıştırma fonksiyonları
kronometre_fonksiyonu()
saatin_zaman_fonksiyonu()

window.mainloop()