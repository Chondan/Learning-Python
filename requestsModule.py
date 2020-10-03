import requests

# The requests module allows you to send HTTP requests using Python
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc)
x = requests.get("https://docs.mongodb.com/manual/reference/method/db.collection.drop/")

# print(x.text)
