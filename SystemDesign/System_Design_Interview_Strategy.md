
# System Design Interview Strategy (Non‑FAANG)

A focused guide covering **5 most asked backend system design questions** and a **step‑by‑step strategy to answer them in interviews**.

---

# The Standard System Design Answer Framework

Use this structure whenever an interviewer asks you to design a system.

1. Clarify Requirements
2. Estimate Scale
3. Define APIs
4. High‑Level Architecture
5. Database Design
6. Identify Bottlenecks
7. Scaling Strategy

Goal: Start simple and **evolve architecture as traffic grows**.

---

# 1. Design URL Shortener (TinyURL / Bitly)

## Requirements

• Convert long URL → short URL  
• Redirect short URL → original URL  
• Low latency redirects  

Example:

```
https://example.com/very/long/url
```

becomes

```
tinyurl.com/abc123
```

## Basic Architecture

Client  
↓  
Load Balancer  
↓  
API Server  
↓  
Database

## Database Schema

| Field | Description |
|---|---|
short_id | Generated short key |
long_url | Original URL |
created_at | Timestamp |
expiry_date | Optional |

## Scaling

Add caching.

Client  
↓  
Load Balancer  
↓  
API Servers  
↓  
Redis Cache  
↓  
Database

Shard database by:

```
hash(short_id)
```

---

# 2. Design Chat System (WhatsApp / Slack)

## Requirements

• Send messages  
• Real‑time delivery  
• Message history  

## Architecture

Client  
↓  
WebSocket Server  
↓  
Message Queue  
↓  
Chat Service  
↓  
Database

## Message Flow

User A sends message  
→ WebSocket server receives  
→ message added to queue  
→ worker stores message  
→ delivered to User B

## Scaling

Multiple chat servers:

Client  
↓  
Load Balancer  
↓  
Chat Server 1  
Chat Server 2  
Chat Server 3  
↓  
Redis Pub/Sub  
↓  
Database

Redis synchronizes servers.

---

# 3. Design Rate Limiter

## Goal

Prevent abuse of APIs.

Example:

```
100 requests per minute per user
```

## Architecture

Client  
↓  
API Gateway  
↓  
Rate Limiter  
↓  
API Servers

## Implementation

Use Redis counters.

Example key:

```
user_id + timestamp
```

## Algorithms

• Token Bucket  
• Leaky Bucket  
• Fixed Window  

---

# 4. Design Notification System

Used in:

• E‑commerce  
• Social apps  
• Banking apps  

Example notifications:

• Email  
• Push notifications  
• SMS  

## Architecture

User Action  
↓  
Notification Service  
↓  
Message Queue  
↓  
Workers  
↓  
Email / SMS / Push providers

## Why Queue?

Queues handle traffic spikes and prevent overload.

---

# 5. Design File Upload System (Google Drive / Dropbox)

## Requirements

• Upload large files  
• Reliable storage  
• Fast downloads  

## Architecture

Client  
↓  
Upload API  
↓  
Object Storage (S3)  
↓  
Metadata Database

Files stored in **object storage**, not database.

## Large File Upload

Use chunked uploads.

Example:

```
Split file into chunks
Upload chunks separately
Merge after upload
```

## Scaling

Use CDN for downloads.

Client  
↓  
CDN  
↓  
Storage

---

# How Systems Scale to Millions of Users

Interviewers often ask:

"What happens if your system grows to millions of users?"

Explain scaling step‑by‑step.

---

## Stage 1 — Startup Scale

Client  
↓  
API Server  
↓  
Database

---

## Stage 2 — Growing Traffic

Client  
↓  
Load Balancer  
↓  
Multiple API Servers  
↓  
Database

---

## Stage 3 — Heavy Reads

Add caching.

Client  
↓  
Load Balancer  
↓  
API Servers  
↓  
Redis Cache  
↓  
Database

---

## Stage 4 — Heavy Writes

Add asynchronous processing.

Client  
↓  
API Servers  
↓  
Message Queue  
↓  
Workers  
↓  
Database

---

## Stage 5 — Massive Scale

Client  
↓  
CDN  
↓  
Load Balancer  
↓  
API Servers  
↓  
Cache (Redis)  
↓  
Message Queue (Kafka)  
↓  
Worker Services  
↓  
Sharded Databases

This architecture supports **millions of users**.

---

# Practice Plan

Practice one system per day.

Day 1 – URL Shortener  
Day 2 – Chat System  
Day 3 – Rate Limiter  
Day 4 – Notification System  
Day 5 – File Upload System  

Then repeat cycle.

Goal:

Explain system clearly in **15 minutes**.

---

# Key Interview Tip

Always say:

"I'll start with a simple architecture and evolve the system as scale increases."

This shows **mature system design thinking**.

