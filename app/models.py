import classifier.classifier as CSO
import json
from py2neo import *

def dataProcess(datas):
    paper={}
    idnumber=0
    for data in json.loads(datas):
        idnumber=idnumber+1
        idname="id"+str(idnumber)
        paper[idname]={
            "title":data["title"],
            "abstract":data["abstract"],
            "keywords":data["keywords"]
        }
    return CSOToResult(CSO.run_cso_classifier_batch_mode(paper,workers=1,modules="both",enhancement="first"))

def CSOToResult(data):
    # For test
    # with open('app/static/data.json', 'w') as outfile:
    #     json.dump(data, outfile)
    graph = Graph(uri="http://127.0.0.1:7474/", username="neo4j", password="Wnwwykcj6")
    results=graph.cypher.execute("MATCH (n:Ontology)")
    return ""