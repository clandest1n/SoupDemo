import requests
from bs4 import BeautifulSoup

#url = input("What website would you like to scrape?")

page = requests.get('http://catalog.dsu.edu/content.php?catoid=22&navoid=1083')
starting = 'http://catalog.dsu.edu/'


soup = BeautifulSoup(page.text, 'html.parser')

course_list = soup.find_all('ul')[2]
new_list = [item for item in course_list if item != '\n']

urls = []
url = ''
counter = 1
for course in new_list:

    print(str(counter) + ". " + course.find('a').get_text())
    course_url = starting + course.find('a').attrs['href']
    urls.append(course_url)
    counter += 1

print("")
print("")

enter = input("Enter the number of class you would like to use: ")

print("")
print("")

page2 = requests.get(urls[int(enter) - 1])

soup2 = BeautifulSoup(page2.text, 'html.parser')

course_list = soup2.find_all(class_='acalog-course')


for course in course_list:
	print(course.find('span').get_text())