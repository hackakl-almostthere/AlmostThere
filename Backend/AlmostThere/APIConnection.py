import urllib.request


API_KEY = "api_key=d0efe139-8e8d-4ff1-b020-7a71c9bbcb8e"


def makeConnection(query):
    data = urllib.request.urlopen('http://api.at.govt.nz/v1/' + query + '&' + API_KEY)
    return data