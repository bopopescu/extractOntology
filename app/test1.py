import json
from py2neo import *
from json import dumps
import operator

def calculateSimilarity(data):

    return ""
def Merge(dict1,dict2):
    return {**dict1,**dict2}

def recommendRoute(enhance_exist_term,union_exist_term):
    new_union={}
    for key,value in union_exist_term.items():
        new_union[key+0.5]=value*0.7
    result=sorted(Merge(new_union,enhance_exist_term).items(),key=lambda x:x[1],reverse=True)[0]
    if isinstance(result[0],int):
        return {"method":"enhance_exist", "index" :result[0]}
    else:
        return {"method":"union_exist","index":result[0]-0.5}

def existNodeRoute(data):
    allLastNode=[]
    allNode=[]
    unionEnhance={}
    for key, value in data["union_exist"].items():
        allLastNode.append(value[0]['p'].end_node)
        allNode.append(list(value[0]['p'].nodes))

    for key, value in data["enhance_exist"].items():
        allLastNode.append(value[0]['p'].end_node)
        allNode.append(list(value[0]['p'].nodes))
    
    # for value in allNode:
    #     print(allNode.count(value)/len(allNode))
    union_exist_term={}
    enhance_exist_term={}
    for key,value in data["union_exist"].items():
        termFrequency=0
        for node in value[0]['p'].nodes:
            termFrequency=termFrequency+allNode.count(node)/len(allNode)
            if node in allLastNode:
                termFrequency = termFrequency+allLastNode.count(node)/len(allLastNode)
        union_exist_term[key]=termFrequency
    
    for key,value in data["enhance_exist"].items():
        termFrequency=0
        for node in value[0]['p'].nodes:
            termFrequency=termFrequency+allNode.count(node)/len(allNode)
            if node in allLastNode:
                termFrequency = termFrequency+allLastNode.count(node)/len(allLastNode)
        enhance_exist_term[key]=termFrequency
        

    # print(allNode)
    # print(unionEnhance)
        # print(type(value[0]['p']))
    # print(data)
    result=recommendRoute(enhance_exist_term,union_exist_term)

    return data[result["method"]][result["index"]]

def noExistNodeRoute(data):

    return ""
with open('app/static/data.json') as json_file:
    data = json.load(json_file)
    print(len(data))
    graph = Graph(uri="http://127.0.0.1:7474/",
                  username="neo4j", password="Wnwwykcj6")

    level = 7
    results = dumps(
        graph.run("MATCH (n:Ontology) WHERE n.level="+str(level)+" RETURN n").data())
    print(len(results))
    # for result in results:
    # print(results)
    i = 0
    validation = {}
    outputData={}
    for newdata in data:
        validation[newdata] = {
            "found": False,
            "articleData": data[newdata]
        }
        # update through straightfward method
        # results = graph.run("MATCH (m:Ontology),(n:Ontology),p = shortestPath((m)-[superTopicOf*]-(n)) WHERE m.name=\"computer science\" AND n.name="++"RETURN p").data()
        # print(results)
        unionData_insert = {}
        unionData_node = {}
        enhanceData_insert = {}
        enhanceData_node = {}
        # print(data[newdata]["union"])

        # 1. find words from union
        for index, unionData in enumerate(data[newdata]["union"]):
            # print('MATCH (m:Ontology),(n:Ontology),p = shortestPath((m)-[superTopicOf*]-(n)) WHERE m.name="computer science" AND n.name="'+unionData+'"RETURN p')
            try:
                rootresults = graph.run('MATCH (m:Ontology),(n:Ontology),p = shortestPath((m)-[:superTopicOf*]-(n)) WHERE m.name="computer science" AND n.name="'+unionData+'"RETURN p').data()
                if not rootresults:
                    unionData_insert[index] = unionData
                else:
                    unionData_node[index] = rootresults
            except:
                unionData_insert[index] = unionData

        # 2. find words from enhanced
        for index, enhenceData in enumerate(data[newdata]["enhanced"]):
            # print(enhenceData)
            # print('MATCH (m:Ontology),(n:Ontology),p = shortestPath((m)-[superTopicOf*]-(n)) WHERE m.name="computer science" AND n.name="'+enhenceData+'" RETURN p')
            try:
                rootresults = graph.run('MATCH (m:Ontology),(n:Ontology),p = shortestPath((m)-[:superTopicOf*]-(n)) WHERE m.name="computer science" AND n.name="'+enhenceData+'" RETURN p').data()
                if not rootresults:
                    enhanceData_insert[index] = enhenceData
                else:
                    enhanceData_node [index]= rootresults
            except:
                enhanceData_insert[index] = enhenceData
        
        outputData[newdata]={
            "enhance_noExist":enhanceData_insert,
            "enhance_exist":enhanceData_node,
            "union_noExist":unionData_insert,
            "union_exist":unionData_node
        }
        recommendPath=existNodeRoute({"enhance_exist":enhanceData_node,"union_exist":unionData_node})
        print(recommendPath)
    # print(outputData)

        # for level in range(7, 0, -1):
        #     results = graph.run(
        #         "MATCH (n:Ontology) WHERE n.level="+str(level)+" RETURN n").data()
        #     for result in results:
        #         # print(newd)
        #         if data[newdata]["union"][0] == result['n']["name"]:
        #             validation[newdata] = {
        #                 "found": True,
        #                 "resultNode": result['n']
        #             }
        # '''
        # for level in range(7,0,-1):
        #     results=graph.run("MATCH (n:Ontology) WHERE n.level="+str(level)+" RETURN n").data()
        #     for result in results:
        #         # print(newd)
        #         if data[newdata]["union"][0]==result['n']["name"]:
        #             validation[newdata]={
        #                 "found":True,
        #                 "resultNode":result['n']
        #             }        
        #             '''

    # print(validation)
        # results=graph.run("MATCH (n:Ontology) WHERE n.level="+str(level)+" RETURN n").data()
