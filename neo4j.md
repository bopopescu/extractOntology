https://neo4j.com/sandbox-v2/

https://10-0-1-182-35078.neo4jsandbox.com/browser/

https://guides.neo4j.com/wiki

Load wikipedia data

'''
MATCH (c) DETACH DELETE c

'''


```

CREATE INDEX ON: Category(catId)

CREATE INDEX ON: Category(catName)

CREATE (c:Category:RootCategory {catId:0, catName:'Areas of computer science',  fetched:false, level:0})

:param level:1

MATCH (c:Category {fetched: false, level:$level -1})
call apoc.load.json('https://en.wikipedia.org/w/api.php?format=json&action=query&list=categorymembers&cmtype=subcat&cmtitle=Category:'+replace(c.catName,' ','%20')+'&cmprop=ids%7Ctitle&cmlimit=500')
YIELD value	as results
UNWIND results.query.categorymembers AS subcat
MERGE (sc:Category {catId: subcat.pageid})
ON CREATE SET sc.catName=substring(subcat.title,9),sc.fetched=false,sc.level=$level
WITH sc,c
CALL apoc.create.addLabels(sc,['Level'+$level+'Category']) YIELD node
MERGE (sc)-[:SUBCAT_OF]->(c)
WITH DISTINCT c
SET c.fetched=true

MATCH (n)
DETACH DELETE n

```

load CSV data


'''
USING PERIODIC COMMIT 50000
LOAD CSV WITH HEADERS FROM "file:///CSO.3.1.csv" AS row
WITH DISTINCT row.`father` AS ontology_name
MERGE (c:Ontology {name:ontology_name})

CREATE CONSTRAINT ON(c:Ontology) ASSERT c.name IS UNIQUE

'''


d3.js visualization
Collapsible Force Layout




USING PERIODIC COMMIT 50000
LOAD CSV WITH HEADERS FROM "file:///newData.csv" AS row
WITH DISTINCT row.`relationship` AS relationS, row.`father` AS father_Id, row.`son` AS son_Id
MATCH (c:Ontology {id:father_Id}) 
CALL apoc.create.relationship(c, relationsS, {}, c)



USING PERIODIC COMMIT 50000
LOAD CSV WITH HEADERS FROM "file:///son.csv" AS row
WITH DISTINCT row.`id` AS ontologyId, row.`name`
MERGE (c:Ontology {name:ontology_name})


MERGE (sc:Ontology {name: "computer science"})-[:superTopicOf]->(c)
SET c +={level:1}
RETURN c

MATCH (sc:Ontology {name: "computer science"})-[:superTopicOf]->()-[:superTopicOf]->()-[:superTopicOf]->(c)
SET c+={level:3}
RETURN COUNT(c)

MATCH (sc:Ontolgy {name: "computer science"})-[:superTopicOf]->()-[:superTopicOf]->()-[:superTopicOf]->()-[:superTopicOf]->()-[:superTopicOf]->()-[:superTopicOf]->()-[:superTopicOf]->()-[:superTopicOf]->()
SET c+={level:8}
RETURN COUNT(c)