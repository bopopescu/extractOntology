https://10-0-1-182-35078.neo4jsandbox.com/browser/

```

CREATE INDEX ON: Category(catId)

CREATE INDEX ON: Category(catName)

CREATE (c:Category:RootCategory {catId:0, catName:'Machine learning', fetched:false, level:0})

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


