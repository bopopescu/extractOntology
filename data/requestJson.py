import requests
import json
from pymongo import MongoClient
import time

def getJson(urls):
    if len(urls):
        nextUrls=[]
        for url in urls:
            time.sleep(1)
            print('THIS IS THE URL YOU NEED RUN',url)
            if "http" not in str(url):
                continue
            resp = requests.get(url=url)
            try:
                data = resp.json()
            except:
                continue
            if len(data):
                # print(data)
                index=0
                for i in range(len(data)):
                    if data[i]['@id']==url.replace('.json',''):
                        index=i
                        break
                if  "http://cso.kmi.open.ac.uk/schema/cso#superTopicOf" in data[index] and len(data[index]["http://cso.kmi.open.ac.uk/schema/cso#superTopicOf"]):
                    dataJson.append({
                        "id": data[index]['@id'],
                        "resource": data[index]['http://www.w3.org/2002/07/owl#sameAs'] if 'http://www.w3.org/2002/07/owl#sameAs' in data[index] else "null",
                        "name": data[index]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'],
                        "relationship": list(set([record['@id'] for record in data[index]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']])) if 'http://cso.kmi.open.ac.uk/schema/cso#superTopicOf' in data[index] else 'null'
                    })
                    nextUrls.append(getJson(list(set([record['@id']+'.json' for record in data[index]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']]))))
                else:
                    dataJson.append({
                        "id": data[index]['@id'],
                        "resource": data[index]['http://www.w3.org/2002/07/owl#sameAs'] if 'http://www.w3.org/2002/07/owl#sameAs' in data[index] else "null",
                        "name": data[index]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'],
                        "relationship": list(set([record['@id'] for record in data[index]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']])) if 'http://cso.kmi.open.ac.uk/schema/cso#superTopicOf' in data[index] else 'null'
                    })

        time.sleep(10)
        with open('data/runningJson.json', 'w') as fp:
            json.dump(dataJson, fp)
        return getJson(nextUrls)
    else:
        return 0
# def start():


client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['extractOntology']
url = 'https://cso.kmi.open.ac.uk/topics/computer_science.json'
dataJson = []
getJson([url])
with open('data/testJson.json', 'w') as fp:
        json.dump(dataJson, fp)
#     url = 'https://cso.kmi.open.ac.uk/topics/computer_science.json'

#     graph = Graph(uri="http://127.0.0.1:7474/", username="neo4j", password="Wnwwykcj6")
#     graph.delete_all()

#     resp = requests.get(url=url)
#     data = resp.json() # Check the JSON Response Content documentation below
#     node1=Node('Ontology',name=data[0]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'])
#     data_node1={
#         "id":data[0]['@id'],
#         "resource":data[0]['http://www.w3.org/2002/07/owl#sameAs']
#     }
#     node1.update(data_node1)
#     for url in data[0]["http://cso.kmi.open.ac.uk/schema/cso#superTopicOf"]:
#         resp=requests.get(url=url)
#         data=resp.json()

#     # print(data[0]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'])


# url = 'https://cso.kmi.open.ac.uk/topics/computer_science.json'
# resp = requests.get(url=url)
# data = resp.json()
# while True:

#     if len(data[0]["http://cso.kmi.open.ac.uk/schema/cso#superTopicOf"]) == 0:
#         break
#     else:
#         resp = requests.get(url=url)

# def getJson(urls):
#     if len(urls) ==0:
#         return 0
#     else:
#         for url in urls:
#             resp=requests.get(url=url)
#             data = resp.json()
