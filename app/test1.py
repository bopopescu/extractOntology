import json
from py2neo import *
from json import dumps


def calculateSimilarity (data):
    return ""

with open('app/static/data.json') as json_file:
    data = json.load(json_file)
    # print(data)
    graph = Graph(uri="http://127.0.0.1:7474/", username="neo4j", password="Wnwwykcj6")
    level=7
    results=dumps(graph.run("MATCH (n:Ontology) WHERE n.level="+str(level)+" RETURN n").data())
    # print(len(results))
    # for result in results:
    # print(results)
    i=0
    for newdata in data:
        for level in range(7,0,-1):
            results=graph.run("MATCH (n:Ontology) WHERE n.level="+str(level)+" RETURN n").data()
            for result in results:
                # print(newd)
                if data[newdata]["union"][0]==result['n']["name"]:
                    print(result['n'])
                    print(i)
                    i=i+1

        # results=graph.run("MATCH (n:Ontology) WHERE n.level="+str(level)+" RETURN n").data()
