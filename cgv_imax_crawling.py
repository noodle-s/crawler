import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=202&theatercode=0002&date=20190627'
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
imax = soup.select_one('span.imax')
if(imax):
	imax = imax.find_parent('div',class_='col-times')
	title = imax.select_one('div.info-movie > a > strong').text.strip()
	print(title + 'IMAX open')
else:
	print('IMAX not open')
