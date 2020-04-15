from bs4 import BeautifulSoup
import requests


base_url = "https://www.jobsinkenya.co.ke/jobs-in-kenya/page/"

source = []

for i in range(1, 2):
    source = requests.get(base_url + str(i)).text

    soup = BeautifulSoup(source, "lxml")
    # print(source)


for article in soup.find_all("article"):
    job_title = article.find("header", class_="entry-header").text
    date_posted = article.find("a", class_="updated").text
    job_url = article.find("a", class_="updated")["href"]

    if job_url is not None:
        source = requests.get(job_url).text
        soup = BeautifulSoup(source, "lxml")
        job_description = soup.find("div", class_="entry-content").text

    print(job_title)
    print(job_description)
