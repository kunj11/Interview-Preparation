
# Advanced System Design Interview Pack (Non‑FAANG)

A practical guide for backend engineers preparing for **system design interviews**.  
Focus is on **real interview questions**, **clear architecture**, and **how to scale to millions of users**.

---

# Contents

1. System Design Thinking Framework
2. Most Asked System Design Questions
3. Design: URL Shortener (TinyURL)
4. Design: Chat System (WhatsApp / Slack)
5. Design: Notification System
6. Design: Rate Limiter
7. Design: File Upload System
8. Design: News Feed System
9. How To Scale Systems to Millions of Users
10. Practice Strategy for Interviews

---

# 1. System Design Thinking Framework

Always answer system design questions in this order.

Step 1 — Requirements  
Step 2 — Scale Estimation  
Step 3 — High Level Architecture  
Step 4 — Database Design  
Step 5 — Bottlenecks  
Step 6 — Scaling Strategy

Interviewers want to see **your thinking process**.

---

# 2. Most Asked System Design Questions (Non‑FAANG)

| Question | Frequency |
|---|---|
Design URL Shortener | ⭐⭐⭐⭐⭐ |
Design Chat System | ⭐⭐⭐⭐⭐ |
Design Rate Limiter | ⭐⭐⭐⭐ |
Design Notification System | ⭐⭐⭐⭐ |
Design File Storage | ⭐⭐⭐ |
Design News Feed | ⭐⭐⭐ |
Design Logging System | ⭐⭐ |

Learning these covers **70‑80% of interviews**.

---

# 3. Design URL Shortener (TinyURL)

Functional Requirements

• Convert long URL → short URL  
• Redirect short URL → original URL  

Non‑Functional

• High read traffic  
• Low latency redirect  

High Level Architecture

Client
→ Load Balancer
→ API Server
→ Database
→ Cache

Database Table

short_url | long_url | created_at

Scaling

Problem: Database becomes bottleneck

Solution:

Client
→ Load Balancer
→ API Servers
→ Redis Cache
→ DB

Cache stores frequently accessed URLs.

At very large scale:

Add **database sharding**.

Shard key: short_url hash.

---

# 4. Design Chat System

Requirements

• Send messages  
• Real‑time delivery  
• Message history  

Architecture

Client
→ WebSocket Server
→ Message Queue
→ Message Service
→ Database

Flow

User A sends message
→ WebSocket server receives
→ message pushed to queue
→ worker saves message
→ message delivered to receiver

Scaling

Multiple chat servers

Client
→ Load Balancer
→ Chat Servers
→ Redis Pub/Sub
→ Database

Redis syncs messages between servers.

---

# 5. Design Notification System

Types

• Push notification
• Email
• SMS

Architecture

Client Action
→ Notification API
→ Message Queue
→ Workers
→ Notification Services

Example

User places order
→ Event generated
→ Queue
→ Worker sends email / push

Why Queue?

Prevents system overload during spikes.

---

# 6. Design Rate Limiter

Goal

Prevent abuse of APIs.

Example

Limit:

100 requests / minute per user.

Architecture

Client
→ API Gateway
→ Rate Limiter (Redis)
→ API Server

Redis stores counters.

Key:

user_id + timestamp

Algorithm

Token Bucket  
or  
Leaky Bucket

---

# 7. Design File Upload System

Requirements

• Upload images/videos
• Large files
• Reliable storage

Architecture

Client
→ Upload API
→ Object Storage (S3)
→ Metadata DB

Large files use:

**chunked uploads**.

Scaling

Use CDN to deliver files globally.

Client
→ CDN
→ Storage

---

# 8. Design News Feed

Example: Facebook / Twitter

Requirements

• Show posts from friends
• Fast loading

Two approaches

Pull Model

Feed generated when user opens app.

Push Model

Feed pre‑generated when post created.

Hybrid approach used in real systems.

Architecture

Client
→ Feed API
→ Cache
→ Feed Service
→ Database

Scaling

Cache feeds in Redis.

---

# 9. How Systems Scale to Millions of Users

Stage 1 — Small Startup

Client
→ API Server
→ Database

---

Stage 2 — Growing Product

Client
→ Load Balancer
→ Multiple API Servers
→ Database

---

Stage 3 — High Traffic

Client
→ Load Balancer
→ API Servers
→ Redis Cache
→ Database

---

Stage 4 — Massive Scale

Client
→ CDN
→ Load Balancer
→ API Servers
→ Cache
→ Message Queue
→ Worker Services
→ Sharded Databases

---

# 10. Practice Strategy

Practice like this:

Day 1
URL Shortener

Day 2
Rate Limiter

Day 3
Chat System

Day 4
Notification System

Day 5
File Storage

Day 6
News Feed

Day 7
Mock interview practice

Repeat cycle 2‑3 times.

Goal:

Explain architecture **clearly in 15 minutes**.

---

# Final Advice

You do not need to memorize complex distributed systems.

Focus on:

• Load balancers
• Caching
• Queues
• Database scaling
• Sharding

Most system design interviews reuse **these same building blocks**.
