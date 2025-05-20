
## 1. Python – Giriş

- Python, **yorumlanabilir**, **yüksek seviyeli** ve **okunabilirliği yüksek** bir programlama dilidir.
    
- Satır satır çalışır (interpreter tabanlıdır).
    
- Dosya uzantısı: `.py`
    
- Yorum satırı: `#` ile başlar.

örn: # Bu bir yorum satırıdır
print("Merhaba Python!")  # Ekrana yazı yazar


## 2. Değişkenler (Variables)

- Verileri saklamak için kullanılır.
    
- Önceden tanımlamaya gerek yoktur (tip belirtmeden direkt tanımlanır).
    
- Türkçe karakter, boşluk, sayı ile başlayamaz.
    

### 🧠 Kurallar:

- Geçerli örnekler: `sayi`, `ad`, `yas1`
    
- Geçersiz örnekler: `1sayi`, `ad soyad`, `şifre`

 örn:  ad = "Ali"
	 yas = 25
	 ortalama = 75.5


## 📌 3. `input()` Kullanımı

- Kullanıcıdan veri almak için kullanılır.
    
- Aldığı veri **her zaman string (str)** olarak gelir.

örn: isim = input("Adınızı girin: ")
print("Merhaba", isim)
 
Sayısal veri almak istersen:

sayi = int(input("Bir sayı girin: "))     # integer'a çevirir
ondalik = float(input("Bir ondalık sayı girin: "))  # float'a çevirir


## 📌 4. Veri Türleri (Data Types)

	🔢 int (tam sayı)
	
	    yas = 30
	    print(type(yas))  # <class 'int'>
	
	 🧵 str (metin)
		
		isim = "Ayşe"
        print(type(isim))  # <class 'str'> 
	    
	 🔢 float (ondalıklı sayı)
			
	    pi = 3.14
	    primtnt(type(pi))  # <class 'float'>
    
    
    
    