import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find("ul", {"class":"ipc-metadata-list"}).find_all("li", limit=100)

for item in liste:
    filmadi = item.find("h3", {"class":"ipc-title__text"}).text
    puan = item.find("span", {"class":"ipc-rating-star"}).text

    print(filmadi, puan)

"""
TopIMDBScraper

Bu uygulama, IMDb'nin "En İyi TV Dizileri" sayfasını tarayarak ilk 100 TV dizisinin 
adını ve IMDb puanlarını çıkarmayı amaçlar. Uygulama, `requests` ve `BeautifulSoup` 
modüllerini kullanarak sayfayı analiz eder ve kullanıcıya sonuçları terminalde listeler.

Fonksiyonlar:
- IMDb'nin "En İyi TV Dizileri" sayfasından HTML içeriği alır.
- BeautifulSoup ile sayfayı analiz ederek başlık ve puan bilgilerini çeker.
- İlk 100 TV dizisinin adını ve IMDb puanını terminale yazdırır.

Not: IMDb'nin HTML yapısı zamanla değişebilir. Bu kodun çalışabilirliğini korumak için
IMDb'nin güncel HTML yapısını kontrol edin.

Yazar: [Kendi adınız veya takma adınız]
Tarih: [Bugünkü tarih]

Gerekli Kütüphaneler:
- requests
- BeautifulSoup (bs4)

"""