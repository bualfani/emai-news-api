import requests

api_key = "12978a5bca3d43e38c6bebcafaaa1d16"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-22&sortBy=publishedAt&apiKey=12978a5bca3d43e38c6bebcafaaa1d16"

# MAke request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])