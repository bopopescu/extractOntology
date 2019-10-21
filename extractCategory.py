import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "categories",
    "titles": "Category:Computer science",
    # "type": "subcat"
    # "list": "categorymembers"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]
print(PAGES)
# for k, v in PAGES.items():
#     for cat in v['categories']:
#         print(cat["title"])
# https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Areas%20of%20computer%20science&cmtype=subcat