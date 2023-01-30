import pandas as pd
from bs4 import BeautifulSoup
import requests
from winotify import Notification
# from twilio.rest import Client
# import keys
# import sys

# print(sys.executable)
f = requests.get('https://www.prothomalo.com/')
soup = BeautifulSoup(f.text, "lxml")
top_news = soup.find("div", {"class": "_4OsHC"}).find("a", {"class": "card-with-image-zoom"})
top_news_title = top_news['aria-label']
top_news_url = top_news['href']
# print(top_news_title)
# print(top_news_url)

# save as pandas dataframe, for future use
news_frame = pd.DataFrame({
    'title': top_news_title,
    'url': top_news_url
}, index=[0])

# save to a text file
with open('top-news.txt', 'w', encoding="utf-8") as f:
    f.write(top_news_title)
    f.write('\n')
    f.write(top_news_url)
    f.write('\n')

# # send as sms [Twilio API]
# client = Client(keys.account_sid, keys.auth_token)
# message = client.messages.create(
#                      body=top_news_title + '\n' + top_news_url + '\n',
#                      from_=keys.twilio_number,
#                      to=keys.target_number
#                  )
#
# print(message.body)

toast = Notification(app_id="Prothom Alo",
                     title="Top News",
                     msg=top_news_title,
                     duration="short",
                     icon=r"D:\pycode\Web-Scraper-Python\palo.jpg")
toast.add_actions(label="Show Details",
                  launch=top_news_url)

toast.show()
