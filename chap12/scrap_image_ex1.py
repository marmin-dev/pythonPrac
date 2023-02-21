import requests
import bs4
import lxml
import os

queentxt = requests.get('https://en.wikipedia.org/wiki/Queen_(band)')
# print(queentxt.text)
queenbs = bs4.BeautifulSoup(queentxt.text,'lxml')
queenimg = queenbs.select('.thumbimage')[0]
print(queenimg['srcset'].split(' ')[2])
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Queen_%40_Imperial_College_campus_-_1970.jpg/440px-Queen_%40_Imperial_College_campus_-_1970.jpg')

f = open(os.getcwd()+'mycomputer_image.jpg','wb')
f.write(image_link.content)
f.close()