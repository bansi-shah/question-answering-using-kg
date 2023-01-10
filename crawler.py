from lxml import html
import requests
from bs4 import BeautifulSoup

f = open('taj.txt', 'a')

# var = [i for i in range(20, 400, 20)]
var = [1]
url = 'https://www.tripadvisor.in'
for v in var:
	sub_url = '/ShowForum-g297683-i1206-Agra_Agra_District_Uttar_Pradesh.html'
	page = requests.get(url + sub_url)
	soup = BeautifulSoup(page.content, "html.parser")



	for tr in soup.findAll("table"):
		for td in tr.find_all("b"):
			sub_url = td.a['href']	
			sub_page = requests.get(url + sub_url)
			sub_soup = BeautifulSoup(sub_page.content, "html.parser")
			result = sub_soup.find_all("div", {"class":"postBody"})
			for i, x in enumerate(result):
				if i == 0:
					f.write('\n---------------------------QUESTION-------------------------\n')
				if i == 1:
					f.write('\n---------------------------ANSWER-------------------------\n')					
				for p in x:
					if p.name == 'p' and len(p.text) > 0:
						f.write(p.text)
						f.write('\n')
		break


# url = 'https://www.thrillophilia.com/cities/pune'
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
# for tags in soup.findAll("div", { "class" : "common_wrapper_details description_details" }):
# 	for tag in tags.find_all():
# 		if tag.name == 'h3':
# 			with open('thrillophilia.txt', 'a') as f:
# 				for h in tag:
# 					f.write('\n----------------------------QUESTION---------------------------\n')
# 					f.write(h)
# 					f.write('\n----------------------------ANSWER-----------------------------\n')

# 		elif tag.name == 'li':
# 			with open('thrillophilia.txt', 'a') as f:
# 				for li in tag:
# 					f.write(li)

# url = 'https://www.thrillophilia.com/states/uttarakhand/things-to-do'
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
# for tags in soup.findAll("p", { "class" : "recommendation-text section-heading" }):
# 	for tag in tags.find_all():
# 		if tag.name == 'h3':
# 			with open('thrillophilia.txt', 'a') as f:
# 				for h in tag:
# 					f.write('\n----------------------------QUESTION---------------------------\n')
# 					f.write(h)
# 					f.write('\n----------------------------ANSWER-----------------------------\n')

# 		elif tag.name == 'li':
# 			with open('thrillophilia.txt', 'a') as f:
# 				for li in tag:
# 					f.write(li)



# url = 'https://www.thrillophilia.com/cities/bangalore/tours'
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
# for tags in soup.findAll("ul", { "class" : "collapsible" }):
# 	for tag in tags.find_all("li"):
# 		for li in tag.find_all():
# 			with open('thrillophilia.txt', 'a') as f:
# 				if li.name == 'div':
# 					f.write('\n-----------------------QUESTION----------------------\n')
# 					f.write(li.text)
# 					f.write('\n-----------------------ANSWER------------------------\n')
# 				if li.name == 'p':
# 					string = str(li)
# 					string = string.replace('<p>', '')
# 					string = string.replace('</p>', '')
# 					string = string.replace('<li>', '')
# 					string = string.replace('</li>', '')
# 					string = string.replace('<ul>', '')
# 					string = string.replace('</ul>', '')
# 					string = string.replace('<b>', '')
# 					string = string.replace('</b>', '')
# 					string = string.replace('<br>', '')
# 					string = string.strip()
# 					string = string.replace('\n', '')

# 					f.write(string)
# 				