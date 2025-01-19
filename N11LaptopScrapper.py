import requests
from bs4 import BeautifulSoup

# URL ve başlık bilgisi
url = input("lütfen bir url girin: ")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# HTML içeriğini çek ve kontrol et
try:
    html = requests.get(url, headers=headers, timeout=10)
    html.raise_for_status()
    soup = BeautifulSoup(html.content, "html.parser")
except requests.exceptions.RequestException as e:
    print(f"HTML isteği başarısız oldu: {e}")
    exit()

# Ürün listesini bul
liste = soup.find_all("li", {"class": "column"}, limit=10)
if not liste:
    print("Ürün listesi bulunamadı. Sayfa yapısını kontrol edin veya dinamik veri yüklemesini inceleyin.")
    exit()

# Ürün bilgilerini çek ve ekrana yazdır
count = 1
for li in liste:
    try:
        # Ürün linki
        link = li.a.get("href", "Link bulunamadı")

        # Ürün adı
        p_name = li.a.h3.text.strip() if li.a.h3 else "Ad bilgisi yok"

        # Ürün fiyatı
        price_tag = li.find("div", {"class": "priceContainer"})
        price = (
            price_tag.find_all("span")[-1].ins.text.strip(" TL") if price_tag else "Fiyat bilgisi yok"
        )

        # Ürün resimleri
        img_tag = li.find("img", {"class": "cardImage"})
        images = img_tag.get("data-images", "Resim bilgisi yok").split(",") if img_tag else ["Resim bilgisi yok"]

        # Ürün bilgilerini yazdır
        print(f"{count}. Ürün adı: {p_name}")
        print(f"   Fiyat: {price}")
        print(f"   Link: {link}")
        print(f"   Resimler: {images}")
        print()
        count += 1
    except Exception as e:
        print(f"Hata oluştu: {e}")

"""
N11LaptopScraper

Bu uygulama, n11.com üzerindeki "Dizüstü Bilgisayarlar" kategorisinde yer alan ürünlerin 
ilk 10'unu tarar ve ürün adını, fiyatını, ürün bağlantısını ve resim bağlantılarını 
çıkarır. Uygulama, `requests` ve `BeautifulSoup` modüllerini kullanarak sayfayı analiz eder 
ve sonuçları terminale yazdırır.

Fonksiyonlar:
- n11.com'un Dizüstü Bilgisayarlar kategorisinden HTML içeriğini alır.
- BeautifulSoup ile sayfayı analiz ederek ürün adını, fiyatını ve resim bağlantılarını çeker.
- İlk 10 ürünü sıralı olarak terminalde listeler.

Kısıtlamalar:
- Ürün fiyatı, TL simgesinden arındırılmıştır.
- Resim bağlantıları virgülle ayrılmış bir liste şeklinde işlenmiştir.
- n11.com'un HTML yapısı zamanla değişebilir. Bu kodun çalışabilirliğini korumak için
n11.com'un güncel HTML yapısını kontrol edin.

Yazar: [Kendi adınız veya takma adınız]
Tarih: [Bugünkü tarih]

Gerekli Kütüphaneler:
- requests
- BeautifulSoup (bs4)

"""
