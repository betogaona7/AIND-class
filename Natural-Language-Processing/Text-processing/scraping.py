""" cleaning """

import requests
from bs4 import BeautifulSoup

# Fetch a web page
r = requests.get("https://www.udacity.com/courses/all")

# Remove HTML tags using Beatiful Soup Library
soup = BeautifulSoup(r.text, "html5lib")

# Find all course summaries
summaries = soup.find_all("div", class_="course-summary-card")
#summaries[0]

# Extract title
summaries[0].select_one("h3 a").get_text().split()

# Extract description
summaries[0].select_one("div[data-course-short-summary").get_text().strip()

# Find all course summaries, extract title and description
courses = []
summaries = soup.find_all("div", class_="course-summary-card")
for summary in summaries:
	title = summary.select_one("h3 a").get_text().strip()
	description = summary.select_one("div[data-course-short-summary").get_text().strip()
	courses.append((title, description))

print(len(courses), " course summaries foud. Sample:")
print(courses[0][0])
print(courses[0][1])