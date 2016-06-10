import requests

ini = "Cheese"
end = "Jesus"

API = "https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=links&pllimit=100&plnamespace=0&format=json"

seen = []
search = []
search.append(ini)

while True:
    n = search.pop()
    if n in seen:
        continue
    seen.append(n)
    try:
        print('search', n)
        json = requests.get(API.format(n)).json()
        key = list(json['query']['pages'].keys())[0]
        links = json['query']['pages'][key]['links']
        news = [t['title'] for t in links if t['title'] not in search]

        if end in news:
            print("I FOUND {}".format(end))
            break

        search.extend(news)
    except Exception:
        pass

