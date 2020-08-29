import requests
from bs4 import BeautifulSoup

print("Enter Contest Number:")
contest_no = input()
url = "https://codeforces.com/contest/"
page = requests.get(url + str(contest_no))
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
x = soup.find_all('td',class_='id')
number_problems = len(x)
print(x)


