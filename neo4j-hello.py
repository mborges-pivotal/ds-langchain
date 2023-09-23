# Neo4J
#
# See:
# https://neo4j.com/docs/python-manual/current/
# https://neo4j.com/docs/cypher-manual/current/indexes-for-vector-search/
# https://medium.com/@yu-joshua/efficient-similarity-search-clustering-of-dense-vectors-in-neo4j-b06c6f4bf9ce
# https://python.langchain.com/docs/integrations/vectorstores/neo4jvector

from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "<YOUR_URI>"
AUTH = ("neo4j", "<YOUR_PASSWORD>")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

# Get the name of all 42 year-olds
records, summary, keys = driver.execute_query(
    "MATCH (n:Product) RETURN n LIMIT 25;",
    database_="neo4j",
)

# Loop through results and do something with them
for product in records:
    print(product)

# Summary information
print("The query `{query}` returned {records_count} records in {time} ms.".format(
    query=summary.query, records_count=len(records),
    time=summary.result_available_after,
))

driver.close()
