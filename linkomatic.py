import requests
import json
from pprint import pprint

ini = "cheese"
end = "jesus"

API = "https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=linkshere&format=json"

start = "|".join((ini, end))

pprint(requests.get(API.format(start)).json())

