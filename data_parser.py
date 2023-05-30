from bs4 import BeautifulSoup

with open("data.html") as f:
    html = f.read()


soup = BeautifulSoup(html, 'html.parser')
elements = soup.select("div.notifications-desc")



print(len(elements), elements[0].text)

# document.querySelector("#notification_2022-12-01 > div:nth-child(4) > div > div > div.notifications-desc")
#notification_2022-12-01 > div:nth-child(3) > div > div > div.notifications-desc