# ds-langchain
I this repo I have a collection of sample code using langchain and with different vector stores. The goal is to evaluate the existing support of the popular langchain framework with various vector databases. The goal was to use the exact same code by just changing the vector store implementation and experiment a bit. In some cases, I also have the **hello world** version without langchain. 

All examples are prefixed by the vector db name.

## Vector DB summary
Below are the list of vector DBs in the study so far.
* Redis - I started with Redis Cloud but due to an issue with vector index capacity I switched to running redis-stack locally
* Neo4J - Unlike Redis, PostgreSQL and MongoDB, I'm the least familiar with Neo4J. I used the Neo4J AuraDB (cloud offering).
* PostgreSQL - My reasearch led me to the TimescaleDB tutorial but even though they have an cloud offering, I used postgreSQL locally.
* MongoDB - Started with Atlas and their hello world tutorial worked fine. I struggle a bit to run the langchain sample that was returning no results. 

