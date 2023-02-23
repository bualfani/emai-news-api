import requests
from send_email import send_email

api_key = "12978a5bca3d43e38c6bebcafaaa1d16"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-22&sortBy=publishedAt&apiKey=12978a5bca3d43e38c6bebcafaaa1d16"

# MAke request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

# Access the article titles and description
body = ""
for article in content['articles']:
    body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*'\n'

send_email(body)