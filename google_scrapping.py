import requests
from bs4 import BeautifulSoup

def google_search_scraper(search_input):
    """
    Kullanıcıdan alınan arama terimini Google'da arar ve sonuçları ekrana yazdırır.
    """
    search_query = search_input.replace(' ', '+')
    link = "https://www.google.com/search?q=" + search_query

    headerParams = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(link, headers=headerParams)

    # Google sonuçlarını ayrıştır
    soup = BeautifulSoup(response.content, "html.parser")

    # Google'ın yeni yapısına göre arama sonuçlarını bul
    results = soup.find_all('div', class_="tF2Cxc")

    if not results:
        print("Sonuç bulunamadı veya Google bot isteğini engelledi.")
        return

    for div in results:
        anchor = div.find('a')
        link = anchor['href']
        text = anchor.find('h3').string
        description = div.find('span', class_="aCOpRe").text if div.find('span', class_="aCOpRe") else "Açıklama bulunamadı."

        print(link + "*** " + text + "*** " + description)
        print('*******************')

search_input = input('Aramak istediğiniz kelime: ')
google_search_scraper(search_input)
