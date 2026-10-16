# Research Summary: Document Databases (Alternative Data Models)

**Author:** Nourah Nassir  
**Project:** Database Alternative Data Models: Beyond Relational (Holberton School)  
**Assigned Model:** Document Database (e.g., MongoDB)

---

## 1. Introduction & Core Concept
Document databases belong to the family of non-relational (NoSQL) database management systems designed to store, retrieve, and manage semi-structured and unstructured data. Unlike traditional relational databases (RDBMS) that enforce rigid table schemas, rows, and foreign-key constraints, a document database stores data as self-describing documents—typically formatted in **JSON** (JavaScript Object Notation) or **BSON** (Binary JSON). 

The primary driver behind adopting document databases is **Polyglot Persistence**, acknowledging that modern applications handle diverse data structures that do not cleanly map to rigid relational rows and tables. They enable developers to model data closer to how application objects are structured in memory.

---

## 2. Core Concepts & Data Architecture
* **Document:** The fundamental unit of data storage. A single document encapsulates fields and values, where values can include scalars, nested objects, and arrays.
* **Collection:** The equivalent of a relational "table," but without a predefined schema. Documents within the same collection can have entirely different fields.
* **Flexible Schema (Schema-less):** Allows developers to modify data fields dynamically at the application level without executing database-wide schema migrations (`ALTER TABLE`).
* **Nested Structures:** Complex relationships (such as a user profile containing multiple addresses or order items) are stored directly inside a single document using embedded sub-documents rather than splitting data across multiple normalized tables and joining them.

---

## 3. Most Useful Findings & Practical Insights
Through exploring and testing document database architectures, several key advantages emerged:
* **Elimination of Complex Joins:** Because related data is embedded inside a single document, data retrieval requires far fewer database queries and eliminates expensive `JOIN` operations common in SQL.
* **High Read/Write Performance:** Storing localized, self-contained objects optimizes disk I/O and accelerates response times for high-throughput transactional applications (e.g., e-commerce product catalogs and user content feeds).
* **Intuitive Application Mapping:** Native compatibility with JSON makes object-relational mapping (ORM) layers much simpler, as application data models map almost directly to database documents.

---

## 4. Surprising Discoveries
* **The Shift in Design Philosophy:** In relational databases, normalization is the gold standard to avoid data duplication. In document databases, **denormalization** (duplicating data intentionally) is often encouraged to maximize read performance and maintain atomicity within a single document fetch.
* **Transactions Have Evolved:** While early NoSQL databases notoriously lacked multi-document transaction support, modern document databases (such as MongoDB) support robust ACID transactions across multiple documents and collections when strict data consistency is required.

---

## 5. Trade-offs and Limitations
* **Lack of Enforced Integrity:** Without native foreign-key constraints enforced at the database engine level, maintaining referential integrity becomes the responsibility of the application logic.
* **Data Bloat and Concurrency Risks:** Heavy embedding of large, rapidly changing arrays can lead to document size inflation and locking overhead during updates.

---

## 6. Resources & References
* [MongoDB Documentation – Introduction to Document Databases](https://www.mongodb.com/document-databases)
* *Designing Data-Intensive Applications* by Martin Kleppmann (Chapters 2 and 3 on Data Models and Storage Engines).
* [Holberton Intranet Project Guide: Database Alternative Data Models](https://intranet.hbtn.io/projects/3992)
