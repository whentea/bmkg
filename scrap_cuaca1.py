#Scraping cuaca

from bs4 import BeautifulSoup
import requests

#request
page_link = 'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Palu&AreaID=1200106&Prov=29'
page_response = requests.get(page_link, timeout = 5)
page_content = BeautifulSoup(page_response.content, "html.parser")

#parse Kota
datakota = page_content.find('h2', attrs ={'class' : 'blog-grid-title-lg'})
kota=datakota.text
print(kota)

#parse Waktu
datawaktu = page_content.find('h2', attrs ={'class' : 'kota'})
waktu = datawaktu.text
print(waktu)

#parse Suhu
datasuhu = page_content.find('h2', attrs ={'class' : 'heading-md'})
suhu = datasuhu.text
print(suhu)

#parseAll
dataall = page_content.find('div', attrs = {'class' : 'kanan'})
dataall1 = dataall.find_next('p')
dataall2 = dataall1.find_next('p')
all=dataall1.text
all2=dataall2.text
print('Hasil',all)
print('Hasil1',all2)
