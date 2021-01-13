

from SPARQLWrapper import SPARQLWrapper, JSON


QUERY = """
PREFIX up:<http://purl.uniprot.org/core/> 
PREFIX taxon:<http://purl.uniprot.org/taxonomy/> 
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 



SELECT ?prot ?name
WHERE { 
  ?bn a up:Family_Membership_Statement.
  ?bn rdf:object ?family.
  ?bn2 rdf:object ?family.
  ?bn2 rdf:object ?prot.
  ?prot a up:Protein.
  ?prot ?p ?name.
}
"""

ENDPOINT = "http://sparql.uniprot.org/sparql"


if __name__ == "__main__":
    sparql = SPARQLWrapper(ENDPOINT)
    sparql.setQuery(QUERY)
    sparql.setReturnFormat(JSON)
    print('Query…', end=' ', flush=True)
    results = sparql.query().convert()
    print('ok !')

    print('Results:')
    for result in results["results"]["bindings"]:
        print(result["label"]["value"])
