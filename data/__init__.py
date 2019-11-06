import urllib.request, json
data = urllib.request.urlopen("https://doaj.org/api/v1/journals/4cf8b72139a749c88d043129f00e1b07").read()
output = json.loads(data)
print(output)
