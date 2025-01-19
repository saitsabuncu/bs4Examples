import requests
from bs4 import BeautifulSoup
from csv import writer

# Web scraping yapılacak URL
url = "https://www.sadikturan.com"

def fetch_courses(url):
    """
    Belirtilen URL'den kurs bilgilerini çeker ve bir CSV dosyasına kaydeder.

    Args:
        url (str): Kursların bulunduğu web sayfasının URL'si.

    Returns:
        None: Fonksiyon herhangi bir değer döndürmez, sonuçları bir CSV dosyasına kaydeder.
    """
    # Web sayfasından veri çek
    response = requests.get(url)

    # HTML içeriğini BeautifulSoup ile ayrıştır
    soup = BeautifulSoup(response.text, "html.parser")

    # Kursları içeren sınıfları bul
    kurslar = soup.find_all(class_="kurs")

    # CSV dosyasını oluştur ve başlık satırını ekle
    with open('kurslar.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(['kurs_resmi', 'kurs_baslik', 'kurs_aciklama', 'udemy_link', 'site_link'])

        # Her bir kurs için bilgileri ayıkla ve CSV'ye yaz
        for kurs in kurslar:
            kurs_resmi = kurs.find('img')['src']  # Kurs resminin kaynağı
            kurs_basligi = kurs.find(class_="media-body").find('h2').string  # Kurs başlığı
            kurs_aciklama = kurs.find(class_="media-body").find('span').string  # Kurs açıklaması
            linkler = kurs.find(class_="card-footer").find_all('div')[1].find_all('a')
            kurs_udemy_link = linkler[0]['href']  # Udemy kurs linki
            kurs_site_link = url + linkler[1]['href']  # Sitedeki kurs linki

            # CSV dosyasına kurs bilgilerini ekle
            csv_writer.writerow([kurs_resmi, kurs_basligi, kurs_aciklama, kurs_udemy_link, kurs_site_link])

# Fonksiyonu çağır
fetch_courses(url)