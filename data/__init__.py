# # import urllib.request, json
# # data = urllib.request.urlopen("https://doaj.org/api/v1/journals/4cf8b72139a749c88d043129f00e1b07").read()
# # output = json.loads(data)
# # print(output)
import pandas as pd
from py2neo import *
graph = Graph(uri="http://127.0.0.1:7474/", username="neo4j", password="Wnwwykcj6")
tx = graph.begin()

df= pd.read_csv("data/CSO.3.1.csv",header=None)
for index,data in df.iteritems():
    df[index] = df[index].str.replace("owl#","")
    df[index] = df[index].str.replace("rdf-schema#", "")
    df[index] = df[index].str.replace("22-rdf-syntax-ns#", "")
    df[index] = df[index].str.replace("cso#","")
    df[index] = df[index].str.replace("-", "_")
    df[index] = df[index].str.extract(r".*\/(\w+(?:\.\w+)?)[?\.]?")
for index,row in df.iterrows():
    node1=Node('Ontology',name=row[index][0])
    node2=Node('Ontology',name=row[index][1])
    relation=Relationship(node1,row[index][3],node2)
    tx.create(node1)
    tx.create(node2)
    tx.create(relation)
tx.commit()
