import requests
import re
from bs4 import BeautifulSoup
count=0
song=[]
df = "http://cspro.sogang.ac.kr/~gr120170213/"
def ina(link):	
	global song
	global count
	link = re.sub(r"#","",link)
	link = re.sub(r"\?","",link)
	
	if link[0:7] != "http://":
		link1 = df+link
	else:
		link1 = link

	if link1 in song:
		return	
	r = requests.get(link1)
	soup = BeautifulSoup(r.content,"html.parser")
	results = soup.find_all('a')
	if r.ok == False:
		return
	if r.status_code == 404:
		return
	count= count+1

	if link1[len(link1)-1] == '\n':
		link1[len(link1)-1]='\0' 
	song.append(link1)
	str1 = "Output_{:04}.txt".format(count)
	f2 = open(str1,"w")
	f2.write(soup.get_text())
	f2.close()

	for i in results :
		if i["href"] == "":
			continue
		ina(i["href"])

ina(df+"index.html")
f= open('URL.txt', 'w')

for i in range(len(song)-1):
	f.write(song[i]+"\n")
if song[len(song)-1][ len(song[len(song)-1])-1] == '\n':
	song[len(song)-1][ len(song[len(song)-1])-1]='\0' 
f.write(song[len(song)-1])
f.close()
