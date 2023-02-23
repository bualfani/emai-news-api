import requests
from send_email import send_email

topic = "tesla"
api_key = "12978a5bca3d43e38c6bebcafaaa1d16"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-01-22&sortBy=publishedAt&" \
      "apiKey=12978a5bca3d43e38c6bebcafaaa1d16&" \
      "language=en"

# MAke request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

# Access the article titles and description
body = ""
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = "Subject: Today's News" + '\n'\
               + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*'\n'

body = body.encode("utf-8")
send_email(message=body)