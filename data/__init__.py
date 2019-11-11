# # import urllib.request, json
# # data = urllib.request.urlopen("https://doaj.org/api/v1/journals/4cf8b72139a749c88d043129f00e1b07").read()
# # output = json.loads(data)
# # print(output)
import pandas as pd
from py2neo import *
import json
import math
def convertToNumber (s):
    return int.from_bytes(s.encode(), 'little')

def convertFromNumber (n):
    return n.to_bytes(math.ceil(n.bit_length() / 8), 'little').decode()

graph = Graph(uri="http://127.0.0.1:7474/", username="neo4j", password="Wnwwykcj6")
graph.delete_all()


df= pd.read_csv("data/CSO.3.1.csv",header=None)
for index,data in df.iteritems():
    df[index] = df[index].str.replace("owl#","")
    df[index] = df[index].str.replace("rdf-schema#", "")
    df[index] = df[index].str.replace("22-rdf-syntax-ns#", "")
    df[index] = df[index].str.replace("cso#","")
    df[index] = df[index].str.replace("-", "_")
    df[index] = df[index].str.extract(r".*\/(\w+(?:\.\w+)?)[?\.]?")


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
tx=graph.begin()
for index,row in df.iterrows():
    tx.evaluate('''
    MATCH (a:)
    ''') 
print("finished load data")