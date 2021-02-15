import requests
import re
from bs4 import BeautifulSoup

# address = input("Type web address.\n")

address = "https://www.items7.com/diablo-2-amulets-5231.html"

Results_url = address # URl to page you want to scrape goes here 
url_headers = {'User-Agent': 'Mozilla/5.0'}

try:
	response = requests.get(Results_url, headers = url_headers)
	
	if response.status_code == 200:
		print("Status code ok: " + str(200)) # if = 200 we know we downloaded the html correctly
		# print(response.content) # print the entire response
		#soup = BeautifulSoup(response.content, 'html.parser') # variable to store the entire html response in
		#containers = soup.find_all('ul', class_= 'lb1_list') # A smaller subset of soup that we can start drilling down into/parsing
		# print(len(containers)) # Number of unorganized list items in the entire 'containers' variable, should be 1 as per htlm code
		# print(type(containers))
		#products = containers[0].find_all('li')
		# print(type(product))
	
		soup = BeautifulSoup(response.content, 'html.parser') # variable to store the entire html response in
		containers = soup.find_all('ul', class_= 'lb1_list') # A smaller subset of soup that we can start drilling down into/parsing
		products = containers[0].find_all('li') # Drilling down to the list items that contain the text we want

		# for product in products: 
		# 	print(product)

		#items = soup('font', color="#FFFF00")

		items = soup('div', "desc")

		for item in items:
			for line in item:
				result = re.search('">(.*)</', str(line))
				if result:
					print(result.group(1))
		
	else:
		print("Error: Status code " + str(response.status_code))
		
except:
	print("Something went wrong yo")
