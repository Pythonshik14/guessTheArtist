import pandas as pd
from bs4 import BeautifulSoup
import requests
from lxml import etree
import lxml.html

def load_image(name, url):

	head = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:88.0) Gecko/20100101 Firefox/88.0"}
	search_image = requests.get(url, headers=head)

	option_img = open("images\\" + name + ".jpg", "wb")
	option_img.write(search_image.content)

	option_img.close()

url = "https://gallerix.ru/album/200-Russian"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:88.0) Gecko/20100101 Firefox/88.0"}

AllData = {

	"NameOfArt":[],
	"PicturePath":[],
	"TrueArt":[],
	"False1Art":[],
	"False2Art":[]

	}

response = requests.get(url, headers=head)

print(response.status_code)

if response.status_code == 200:

	tree = lxml.html.document_fromstring(response.text)

	# soup = BeautifulSoup(response.text, "lxml")

	right_artists = tree.xpath('/html/body/div[3]/div[2]/main/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/a/text()')	

	right_imgs = tree.xpath('/html/body/div[3]/div[2]/main/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/a/div/img')

	for art in range(len(right_artists)):
		if art < 275:
			xtx = str(right_artists[art]).split(" – ")
			AllData['NameOfArt'].append(xtx[1])
			AllData['TrueArt'].append(xtx[0])
			AllData['PicturePath'].append("images\\" + xtx[1] + ".jpg")
			load_image(xtx[1], "https:"+right_imgs[art].attrib['src'])

		elif art >= 275 and art < 550:
			xtx = str(right_artists[art]).split(" – ")
			AllData['False1Art'].append(xtx[0])
		
		elif art >= 550 and art < 825:
			xtx = str(right_artists[art]).split(" – ")
			AllData['False2Art'].append(xtx[0])

		else:
			break

	print(len(AllData['NameOfArt']))
	print(len(AllData['TrueArt']))
	print(len(AllData['PicturePath']))
	print(len(AllData['False1Art']))
	print(len(AllData['False2Art']))
	print(AllData) 

	data = pd.DataFrame(AllData)
	data.to_csv("artists.csv", index=None)