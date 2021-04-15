# YouTube Link:

# Ensure that you have both beautifulsoup and requests installed:
#   pip install beautifulsoup4
#   pip install requests
# 	pip install xlsxwriter

import requests
from bs4 import BeautifulSoup
import xlsxwriter

def get_url_data( url_name, code_page ):
	# requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
	# data = requests.get(url_name, auth=HTTPBasicAuth('michal.kocandrle@gmail.com', '7Kokosak3'))
	data = requests.get(url_name)
	soup = BeautifulSoup(data.text.encode(code_page), 'html.parser')
	data = []
	for div in soup.find_all('div', { 'class': 'article-component' }):
		values = [p.text for p in div.find_all('p')]
		data.append(values)
	return data


print (get_url_data('https://denikn.cz/534236/politikon-ctyri-klicova-poznani-o-piratech-a-starostech-a-proc-je-pro-babise-landa-vic-nez-ockovani/?ref=tit', 'utf-8') )
# print (get_url_data('https://www.itnetwork.cz/navrh/navrhove-vzory/gof/facade-navrhovy-vzor', 'Latin-1') )