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
    return CSO.run_cso_classifier_batch_mode(paper,workers=1,modules="both",enhancement="first")
