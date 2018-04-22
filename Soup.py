import requests
from bs4 import BeautifulSoup

#url = input("What website would you like to scrape?")
urls = []
url = ''
counter = 1

# DSU Catalog : Beacom College
page = requests.get('http://catalog.dsu.edu/content.php?catoid=22&navoid=1083')

# Where each of our links will start
starting = 'http://catalog.dsu.edu/'


soup = BeautifulSoup(page.text, 'html.parser')

#grabs the ul's that make up the different courses
course_list = soup.find_all('ul')[2]
new_list = [item for item in course_list if item != '\n'] #removes new lines

# grabs the original course names and creates a list of course URL's associated with them
for name in new_list:
    print(str(counter) + ". " + name.find('a').get_text())
    course_url = starting + name.find('a').attrs['href']
    urls.append(course_url)
    counter += 1

print("\n") # formatting

enter = input("Enter the number of class you would like to use: ")

print("\n") # formatting

# grabs the correct url that corresponds to the course you select
page2 = requests.get(urls[int(enter) - 1])

# parses the URL with selected course
soup2 = BeautifulSoup(page2.text, 'html.parser')

course_list = soup2.find_all(class_='acalog-course')

# prints out each course that is requred of that major
for course in course_list:
	print(course.find('span').get_text())