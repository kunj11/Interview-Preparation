
# System Design Interview Cheat Sheet

A **quick revision guide** for backend engineers before system design interviews.

Use this to refresh the **core concepts, patterns, and answering strategy**.

---

# 1. System Design Answer Framework

Always structure your answer like this:

1. Clarify Requirements
2. Estimate Scale
3. Define APIs
4. High Level Architecture
5. Database Design
6. Identify Bottlenecks
7. Scaling Strategy

Example line to start with:

"I will start with a simple architecture and evolve the system as the scale increases."

---

# 2. Key Questions To Ask Interviewer

Before designing the system ask:

• Expected number of users  
• Requests per second  
• Read vs Write ratio  
• Real-time requirements  
• Data retention period  
• Consistency requirements  

These questions help determine architecture.

---

# 3. Core Architecture Components

| Component | Purpose |
|---|---|
Load Balancer | distribute traffic |
Cache (Redis) | reduce DB load |
Message Queue | async processing |
CDN | deliver static content |
Database | store data |
Search Engine | fast text search |
Object Storage | store files |

---

# 4. Common Architecture Pattern

Typical scalable backend architecture:

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

---

# 5. Caching Strategy

Cache frequently accessed data.

Cache Flow:

Client
↓
API
↓
Cache
↓
Database

If cache hit → return immediately.

If cache miss → query DB then update cache.

Tools:

• Redis  
• Memcached

---

# 6. Database Scaling

### Vertical Scaling

Increase server capacity.

### Horizontal Scaling

Add multiple database nodes.

### Replication

Master → Write  
Replicas → Read

### Sharding

Split database by key.

Examples:

user_id  
region  
hash key

---

# 7. Handling High Traffic

Techniques:

• Load balancing  
• Caching  
• Async queues  
• Database sharding  
• CDN  

---

# 8. Message Queue Use Cases

Queues help handle background tasks.

Example tasks:

• Sending emails  
• Notifications  
• Video processing  
• Log processing  

Popular tools:

Kafka  
RabbitMQ  
AWS SQS

---

# 9. Common Bottlenecks

Always mention these in interviews.

• Database overload  
• Cache misses  
• Network latency  
• Large payloads  
• Hot keys

---

# 10. Scaling To Millions Of Users

Stage 1 — Simple System

Client
↓
API Server
↓
Database

---

Stage 2 — Add Load Balancer

Client
↓
Load Balancer
↓
Multiple API Servers
↓
Database

---

Stage 3 — Add Cache

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

Stage 4 — Add Async Processing

Client
↓
API Servers
↓
Message Queue
↓
Worker Services
↓
Database

---

Stage 5 — Massive Scale

Client
↓
CDN
↓
Load Balancer
↓
API Servers
↓
Cache
↓
Message Queue
↓
Worker Services
↓
Sharded Databases

---

# 11. Most Asked System Design Questions

Practice these systems:

• URL Shortener  
• Chat System  
• Rate Limiter  
• Notification System  
• File Upload System  
• News Feed  
• Logging System  

These cover most backend interviews.

---

# 12. Interview Communication Tips

Good candidates:

• Explain assumptions
• Start simple
• Identify bottlenecks
• Add scaling solutions

Bad candidates:

• Jump directly to complex architecture
• Mention tools without reasoning

---

# Final Reminder

System design interviews are about:

• clear thinking  
• structured explanation  
• understanding tradeoffs  

Not about memorizing architectures.

