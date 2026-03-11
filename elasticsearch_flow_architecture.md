
# Elasticsearch – Detailed Flow and Architecture

This document explains how Elasticsearch works internally, including:

- High-level architecture
- Indexing flow
- Search flow
- Internal storage
- Why Elasticsearch is fast

---

# 1. Elasticsearch High-Level Architecture

Elasticsearch is a distributed search engine built on Apache Lucene.

Key components:

| Component | Description |
|---|---|
Node | Single Elasticsearch server |
Cluster | Group of nodes |
Index | Similar to database |
Document | JSON record |
Shard | Partition of index |
Replica | Copy of shard |

Architecture:

                Client/App
                     |
                     v
             Coordinating Node
                     |
        --------------------------------
        |              |               |
        v              v               v

      Data Node1     Data Node2      Data Node3
      Shard1         Shard2          Shard3
      Replica        Replica         Replica

---

# 2. Indexing Flow (Write Path)

Example document:

{
  "title": "How Elasticsearch Works",
  "author": "John",
  "content": "Search engine internals"
}

Flow:

Client Application
        |
        v
Coordinating Node
        |
        v
hash(document_id)
        |
        v
Primary Shard
        |
        v
Lucene Index
        |
        v
Replica Shards

---

# 3. Text Processing

Document
   |
Analyzer
   |
Tokenizer
   |
Inverted Index

Example:

Text:
"Elasticsearch is fast"

Tokens:

["elasticsearch", "is", "fast"]

Stored as:

Term -> Documents

elasticsearch -> [doc1, doc3]
fast -> [doc1, doc2]

---

# 4. Search Flow

Client
  |
  v
Coordinating Node
  |
Broadcast Query
  |
-----------------------------------
|             |                   |
v             v                   v

Shard1       Shard2              Shard3

Each shard searches locally using Lucene.

Results returned to coordinator.

Coordinator merges results and returns response.

---

# 5. Search Execution Phases

Phase 1: Query Phase

Each shard returns top documents.

Phase 2: Fetch Phase

Coordinator fetches full documents.

---

# 6. Internal Storage

Index
 |
 +-- Shard1
 |     |
 |     +-- Lucene Segment
 |
 +-- Shard2
 |
 +-- Shard3

Segments are immutable and merged periodically.

---

# 7. Why Elasticsearch is Fast

1. Inverted Index
2. Parallel search across shards
3. Built on Apache Lucene

---

# 8. Example Production Usage

Example: Product search

User -> Frontend -> Backend -> Elasticsearch -> Results

Used in:

- E-commerce search
- Log analytics
- Observability systems
- Document search

---

# Summary

Elasticsearch works by:

1. Receiving documents
2. Routing them to shards
3. Creating inverted index
4. Distributing shards across nodes
5. Searching shards in parallel
6. Merging results quickly
