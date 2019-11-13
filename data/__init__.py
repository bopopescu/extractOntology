# # import urllib.request, json
# # data = urllib.request.urlopen("https://doaj.org/api/v1/journals/4cf8b72139a749c88d043129f00e1b07").read()
# # output = json.loads(data)
# # print(output)
import pandas as pd
from py2neo import *
import json
import math
import time
import requests
def convertToNumber (s):
    return int.from_bytes(s.encode(), 'little')

def convertFromNumber (n):
    return n.to_bytes(math.ceil(n.bit_length() / 8), 'little').decode()

graph = Graph(uri="http://127.0.0.1:7474/", username="neo4j", password="Wnwwykcj6")
# graph.delete_all()
column=input()

df= pd.read_csv("data/CSO.3.1.csv")
# print(df[column])
dataJson={
    "id":[],
    "resource":[],
    "name":[],
    "relationship":[]
}
print(type(column))
print(column)
if column == "father" or column=="son":
    dataJson={
    "id":[],
    "resource":[],
    "name":[],
    "relationship":[]  
    }
    for data in list(set(df[column].tolist())):
        url=data[1:-1]+'.json'
        # time.sleep(1)
        print('THIS IS THE URL YOU NEED RUN',url)

        if "http" not in str(url) or "wikidata.org" in str(url) :
            continue
        resp = requests.get(url=url)
        try:
            data = resp.json()
        except:
            continue
        if len(data):
            index=0
            for i in range(len(data)):
                if  '@id' not in data[i] or data[i]['@id']==url.replace('.json',''):
                    index=i
                    break
            if  "http://cso.kmi.open.ac.uk/schema/cso#superTopicOf" in data[index] and len(data[index]["http://cso.kmi.open.ac.uk/schema/cso#superTopicOf"]):
                dataJson['id'].append(data[index]['@id'] if '@id' in data[index] else "null")
                dataJson['resource'].append(data[index]['http://www.w3.org/2002/07/owl#sameAs'] if 'http://www.w3.org/2002/07/owl#sameAs' in data[index] else "null")
                dataJson['name'].append(data[index]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'] if 'http://www.w3.org/2000/01/rdf-schema#label' in data[index] else "null")
                dataJson['relationship'].append(list(set([record['@id'] for record in data[index]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']])) if 'http://cso.kmi.open.ac.uk/schema/cso#superTopicOf' in data[index] else 'null')
                
                # dataJson.append({
                #     "id": data[index]['@id'],
                #     "resource": data[index]['http://www.w3.org/2002/07/owl#sameAs'] if 'http://www.w3.org/2002/07/owl#sameAs' in data[index] else "null",
                #     "name": data[index]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'],
                #     "relationship": list(set([record['@id'] for record in data[index]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']])) if 'http://cso.kmi.open.ac.uk/schema/cso#superTopicOf' in data[index] else 'null'
                # })
            else:
                dataJson['id'].append(data[index]['@id'] if '@id' in data[index] else "null")
                dataJson['resource'].append(data[index]['http://www.w3.org/2002/07/owl#sameAs'] if 'http://www.w3.org/2002/07/owl#sameAs' in data[index] else "null")
                dataJson['name'].append(data[index]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'] if 'http://www.w3.org/2000/01/rdf-schema#label' in data[index] else "null")
                dataJson['relationship'].append(list(set([record['@id'] for record in data[index]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']])) if 'http://cso.kmi.open.ac.uk/schema/cso#superTopicOf' in data[index] else 'null')
                # dataJson.append({
                #     "id": data[index]['@id'],
                #     "resource": data[index]['http://www.w3.org/2002/07/owl#sameAs'] if 'http://www.w3.org/2002/07/owl#sameAs' in data[index] else "null",
                #     "name": data[index]["http://www.w3.org/2000/01/rdf-schema#label"][0]['@value'],
                #     "relationship": list(set([record['@id'] for record in data[index]['http://cso.kmi.open.ac.uk/schema/cso#superTopicOf']])) if 'http://cso.kmi.open.ac.uk/schema/cso#superTopicOf' in data[index] else 'null'
                # })
    df=pd.DataFrame(dataJson,columns=["id","resource","name","relationship"])
    df.to_csv("data/"+column+".csv")
else:
    df[column]=df[column].str.replace("owl#","")
    df[column]=df[column].str.replace("rdf-schema#","")
    df[column]=df[column].str.replace("22-rdf-syntax-ns#","")
    df[column]=df[column].str.replace("cso#","")
    df[column]=df[column].str.replace("-","")
    df[column] = df[column].str.extract(r".*\/(\w+(?:\.\w+)?)[?\.]?")
    df[column].to_csv("data/"+column+".csv",header="relation")
# for index,data in df.iteritems():
#     print(index)
#     df[index] = df[index].str.replace("owl#","")
#     df[index] = df[index].str.replace("rdf-schema#", "")
#     df[index] = df[index].str.replace("22-rdf-syntax-ns#", "")
#     df[index] = df[index].str.replace("cso#","")
#     df[index] = df[index].str.replace("-", "_")
#     df[index] = df[index].str.extract(r".*\/(\w+(?:\.\w+)?)[?\.]?")


'''
for index,row in df.iterrows():
    tx = graph.begin()
    node1=Node('Ontology',name=row[0])
    node2=Node('Ontology',name=row[1])
    relation=Relationship(node1,row[2],node2)
    if index==0:
        tx.create(node1)
        tx.create(node2)
    else:
        tx.merge(node1)
        tx.merge(node2)
    
    tx.create(relation)
    print(index)
    tx.commit()

def reversedDic(dic):
    newDic=dict()
    for key,value in dic.items():
        if value in newDic:
            newDic[value] = str(newDic[value])+","+str(key)
        else:
            newDic[value]=str(key)
    return newDic
newJson=dict()
for index,data in df.iteritems():
    newJson[index]=reversedDic(df[index].to_dict())
with open('dataJson.json','w') as fp:
    json.dump(newJson,fp)
'''
# tx=graph.begin()
# for index,row in df.iterrows():
#     tx.evaluate('''
#     MATCH (a:)
#     ''') 
print("finished load data")