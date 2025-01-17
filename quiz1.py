from bs4 import BeautifulSoup

with open("deneme1.html") as file:
    html_doc=file.read()

obj=BeautifulSoup(html_doc, "html.parser")
print(obj)