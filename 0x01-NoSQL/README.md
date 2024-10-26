# NoSQL
## Learning Objectives



* What NoSQL means
* What is difference between SQL and NoSQL
* What is ACID
* What is a document storage
* What are NoSQL types
* What are benefits of a NoSQL database
* How to query information from a NoSQL database
* How to insert/update/delete information from a NoSQL database
* How to use MongoDB


----

1. Not only SQL


2. 
### Main differences between NoSQL and SQL

At a high level, NoSQL and SQL databases have many similarities.

In addition to supporting data storage and queries, they both also allow one to retrieve, update, and delete stored data. However, under the surface lie some significant differences that affect NoSQL versus SQL performance, scalability, and flexibility.

Here are some of the main differences between SQL versus NoSQL databases:
### Structure

SQL databases are table based, while NoSQL databases can be document-oriented, key-value pairs, or graph structures. In a NoSQL database, a document can contain key value pairs, which can then be ordered and nested.
### Scalability

SQL databases scale vertically, usually on a single server, and require users to increase physical hardware to increase their storage capacities. In effect, while cloud-storage options are available, SQL databases can be prohibitively expensive for businesses when dealing with vast amounts of big data.

NoSQL databases offer horizontal scalability, meaning that more servers simply need to be added to increase their data load. This means that NoSQL databases are better for modern cloud-based infrastructures, which offer distributed resources.
### Language

SQL databases use SQL (Structured Query Language). NoSQL databases use JSON (JavaScript Object Notation), XML, YAML, or binary schema, facilitating unstructured data. SQL has a fixed-defined schema, while NoSQL databases are more flexible.
### Support

SQL is a popular standard language that is well supported by many different database systems, while NoSQL has varying levels of support in various database systems.

Regarding support, you’ll generally find that more help is available for SQL databases than NoSQL. This is because SQL is a more established technology and thus has many more users and developers who can help you with your problems. In contrast, NoSQL is still relatively new, with less help available on forums or through the community. Your support options may be limited if you run into difficulties using it.

### Pros and cons of SQL

SQL is the lingua franca of data. It's the language you’ll use most to query databases and move structured data between traditional applications. It's a powerful language that can help you do many data-related things but also has some downsides.

Here are some pros and cons of using SQL for data storage and retrieval.

### Pros of SQL:

* SQL is widely understood and supported; most developers know it well.

* SQL is extremely useful for simple aggregations over large datasets, such as calculating averages.

* SQL is extremely useful for setting up simple ETL jobs, especially if the input and output formats are relational databases.

* SQL is well-documented and easy to learn.

### Cons of SQL:

* The performance of SQL can be poor on substantial data sets because it requires multiple passes over the data to complete many operations (especially joins). 

* Debugging SQL can be complicated because it doesn't provide informative error messages.

* The syntax of SQL tends to be verbose compared with programming languages like Python or R, which makes it harder to write complex transformations as scripts or functions. 


3. 

### Atomicity

Atomicity guarantees that all of the commands that make up a transaction are treated as a single unit and either succeed or fail together. This is important in the event of a system failure or power outage, in that if a transaction wasn't completely processed, it will be discarded and the database maintains its data integrity.


### Consistency

Consistency guarantees that changes made within a transaction are populated across the database system (e.g., nodes) and in alignment with DBMS constraints. If data consistency is going to be negatively impacted by a transaction in an inconsistent state, the entire transaction will fail.

### Isolation

Each transaction is isolated from the other transactions to prevent data conflicts. This also helps database operations in relation to managing multiple entries and multi-level transactions. For example, if two users are trying to modify the same data (or even the same transaction), the DBMS uses a mechanism called a lock manager to suspend other users until the changes being made by the first user are complete.

### Durability

Durability guarantees that once the transaction completes and changes are written to the database, they are persisted. This ensures that data within the system will persist even in the case of system failures like crashes or power outages. The concept of durability is a key element in data reliability.

[source](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.mongodb.com/resources/basics/databases/acid-transactions&ved=2ahUKEwiz2omviayJAxV9VfEDHXYMM2sQFnoECBMQAQ&usg=AOvVaw2alQFJVBqO1jKDXEbRYdtU) 

4. A document database is a type of NoSQL database that can be used to store and query data as JSON-like documents. 


5. https://riak.com/resources/nosql-databases/

6. personally I think the ability to add non-relational data, flexibility in storing data, performance with large data and the ability to scale horizontally with multiple nodes which saves money.

7. 
* `db.collection_name.insertOne/Many/({"key": "value"})`
* `db.collection_name.updateOne/Many({"key": "value"}, {"$set:{new_key: new_value}})`
* `db.collection_name.deleteOne/Many({"key": "value"}, {"$set:{new_key: new_value}})`


8. https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/

https://stackoverflow.com/questions/60309575/mongodb-service-failed-with-result-exit-code 


## task resources:

* [pymongo docs](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/read/retrieve/)
