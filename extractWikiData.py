# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/


from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"
wdt = "P279"
wd="Q21198"
query = """
SELECT ?item ?itemLabel ?itemDescription
WHERE 
{
  ?item wdt:"""+wdt+""" wd:"""+wd+""".
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)
