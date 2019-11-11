import requests
import json
from py2neo import *

url = 'https://cso.kmi.open.ac.uk/topics/computer_science.json'

graph = Graph(uri="http://127.0.0.1:7474/", username="neo4j", password="Wnwwykcj6")
graph.delete_all()

resp = requests.get(url=url)
data = resp.json() # Check the JSON Response Content documentation below
node1=Node('Ontology',name=data[0]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'])
data_node1={
    "id":data[0]['@id'],
    "resource":data[0]['http://www.w3.org/2002/07/owl#sameAs']
}
node1.update(data_node1)
for url in data[0]["http://cso.kmi.open.ac.uk/schema/cso#superTopicOf"]:
    print(url['@id'])
print(data[0]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'])
with open('data/testJson.json','w') as fp:
    json.dump(data,fp)

while True:
    url = 'https://cso.kmi.open.ac.uk/topics/computer_science.json'
    resp = requests.get(url=url)
    data = resp.json()
    if len(data[0]["http://cso.kmi.open.ac.uk/schema/cso#superTopicOf"]) == 0:
        break
    else:
        resp = requests.get(url=url)