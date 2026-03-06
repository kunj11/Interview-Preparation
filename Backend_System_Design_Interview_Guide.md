
# Backend System Design Interview Guide

A practical guide for **backend engineers (5–10 years experience)** preparing for **system design interviews**.

This document covers common interview problems and how to approach them.

---

# Table of Contents

1. System Design Interview Framework
2. URL Shortener
3. Rate Limiter
4. Notification System
5. File Upload Service
6. Distributed Cache
7. Message Queue System
8. Search Service
9. Chat System
10. Key Scalability Concepts
11. Common Interview Mistakes

---

# System Design Interview Framework

Use this structure when answering system design questions.

```
1. Clarify requirements
2. Estimate scale
3. High-level architecture
4. API design
5. Database design
6. Scaling strategy
7. Caching
8. Failure handling
9. Monitoring
```

---

# URL Shortener

Example: TinyURL / Bitly

## Requirements

| Type | Details |
|---|---|
| Functional | Convert long URL to short |
| Functional | Redirect short URL to original |
| Non-functional | Highly available |
| Non-functional | Low latency |

## High-Level Architecture

```
Client
  |
API Gateway
  |
URL Service
  |
Database
```

## Database Schema

| Field | Type |
|---|---|
| id | bigint |
| short_code | varchar |
| long_url | text |
| created_at | timestamp |

## Scaling Ideas

- Use **base62 encoding**
- Cache popular URLs using Redis
- Use **CDN for redirects**
- Partition DB by hash

---

# Rate Limiter

Used in APIs to prevent abuse.

## Algorithms

| Algorithm | Description |
|---|---|
| Fixed Window | Simple counter per time window |
| Sliding Window | More accurate rate limiting |
| Token Bucket | Allows burst traffic |
| Leaky Bucket | Smooth traffic flow |

## Architecture

```
Client
  |
API Gateway
  |
Rate Limiter (Redis)
  |
Backend Service
```

## Implementation Idea

```
key = user_id + timestamp_window
INCR key
EXPIRE key
```

---

# Notification System

Used for email, SMS, push notifications.

## Requirements

| Type | Details |
|---|---|
| Functional | Send notifications |
| Functional | Support multiple channels |
| Non-functional | Scalable |

## Architecture

```
Client
  |
Notification API
  |
Message Queue
  |
Worker Services
  |        |        |
Email    SMS      Push
```

## Technologies

| Component | Tech |
|---|---|
| Queue | Kafka / RabbitMQ |
| Workers | Python / Node |
| Storage | PostgreSQL |

---

# File Upload Service

Example: Google Drive / Dropbox

## Requirements

- Upload large files
- Resume uploads
- Secure storage

## Architecture

```
Client
  |
Upload API
  |
Object Storage (S3)
  |
Metadata DB
```

## Techniques

- Chunk uploads
- Pre-signed URLs
- CDN for downloads

---

# Distributed Cache

Used to improve performance.

## Example

Redis / Memcached

## Architecture

```
Application
   |
Cache Layer (Redis Cluster)
   |
Database
```

## Strategies

| Strategy | Description |
|---|---|
| Cache Aside | App checks cache first |
| Write Through | Write cache + DB |
| Write Back | Cache updates DB later |

---

# Message Queue System

Example: Kafka / RabbitMQ

## Why Use

- Async processing
- Decoupling services
- Load buffering

## Architecture

```
Producer
   |
Message Broker
   |
Consumer Workers
```

## Use Cases

| Use Case |
|---|
| Notification processing |
| Order processing |
| Log ingestion |

---

# Search Service

Example: product search.

## Architecture

```
Client
  |
Search API
  |
Search Engine (Elasticsearch)
  |
Indexing Pipeline
```

## Key Concepts

- inverted index
- ranking algorithms
- sharding

---

# Chat System

Example: WhatsApp / Slack.

## Requirements

| Type | Details |
|---|---|
| Functional | Send messages |
| Functional | Real-time delivery |
| Non-functional | Scalable |

## Architecture

```
Client
  |
WebSocket Server
  |
Message Queue
  |
Chat Service
  |
Database
```

## Storage

| Component | Storage |
|---|---|
| Messages | Cassandra |
| Metadata | PostgreSQL |

---

# Key Scalability Concepts

## Horizontal Scaling

Add more servers.

## Load Balancing

```
Client
   |
Load Balancer
   |
Servers
```

## Database Sharding

Split data across multiple databases.

## Replication

Primary → replicas for reads.

---

# Common Interview Mistakes

| Mistake | Why it's bad |
|---|---|
| Jumping to solution | No requirement clarification |
| Ignoring scale | System may not work in production |
| No trade-off discussion | Interviewers expect reasoning |
| Overengineering | Keep design simple |

---

# Final Advice

In system design interviews:

Focus on:

- Clear architecture
- Scalability
- Trade-offs
- Communication

Remember:

```
Simple design
+
Clear explanation
=
Great interview performance
```
