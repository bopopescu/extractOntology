import classifier.classifier as CSO
import json

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
    print(data)
    return 0